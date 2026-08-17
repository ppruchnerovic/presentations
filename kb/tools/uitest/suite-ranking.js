// Ranking quality. Two kinds of check:
//
//   * agreement with query.py, which ranks the same corpus in SQLite with a
//     different algorithm. Neither is ground truth, but a browser scorer that
//     has drifted badly from the CLI is worth knowing about.
//   * properties that hold regardless of algorithm: the best hit for an
//     unambiguous topic is a talk about that topic, and the same query twice
//     gives the same answer.
//
// The CLI half is skipped when data/talks.db has not been built — query.py
// would otherwise spend a minute building it mid-test.

const L = require('./lib');
const { execFileSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const TOOLS = path.join(__dirname, '..');
const DB = path.join(TOOLS, '..', 'data', 'talks.db');

const CLI_QUERIES = ['spec driven development', 'ai driven sdlc', 'code review', 'kubernetes',
  'rust', 'prompt injection', 'developer experience', 'observability'];

// A query whose answer is not in doubt, and the shape its top hit must have.
const ON_TOPIC = {
  kubernetes: /kubernetes|k8s/i,
  rust: /rust/i,
  typescript: /typescript|\bts\b/i,
  webassembly: /webassembly|wasm/i,
};

L.suite('ranking', async browser => {
  const page = await L.newPage(browser);
  await L.boot(page);

  if (!fs.existsSync(DB)) {
    console.log('SKIP  CLI agreement — data/talks.db not built (run: python3 build_index.py)');
  } else {
    for (const q of CLI_QUERIES) {
      const cli = JSON.parse(execFileSync('python3', ['query.py', q, '-n', '10', '--json'],
        { cwd: TOOLS, maxBuffer: 1 << 26 }).toString()).map(h => h.id);
      await L.search(page, q);
      const web = (await L.cardIds(page)).slice(0, 10);
      const overlap = web.filter(i => cli.includes(i)).length;
      // The CLI's segment query needs every term inside one ~28-word passage, so on
      // a sparse query it finds a handful of rows and the browser legitimately
      // finds more. Judge the overlap against what the CLI actually returned.
      L.check(`"${q}": the web top 10 agrees with the CLI`,
        overlap >= Math.min(4, cli.length),
        `${overlap} of the CLI's ${cli.length} hits are in the web top 10`);
    }
  }

  for (const [q, re] of Object.entries(ON_TOPIC)) {
    await L.search(page, q);
    const title = (await L.titles(page))[0] || '';
    const badges = await page.$$eval('#results .card:first-child .b', bs => bs.map(b => b.textContent).join(' '));
    L.check(`"${q}": the top hit is on topic`, re.test(title) || re.test(badges), title);
  }

  await L.search(page, 'agents');
  const first = await L.cardIds(page);
  await L.search(page, 'zzz');
  await L.search(page, 'agents');
  L.check('the same query twice gives the same order',
    JSON.stringify(first) === JSON.stringify(await L.cardIds(page)));

  L.check('no uncaught errors', page.__errors.length === 0, page.__errors.join('; '));
});
