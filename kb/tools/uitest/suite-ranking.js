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

// Measured agreement between the two rankers on the corpus as it stands (358
// talks), counted as overlap / min(10, hits the CLI returned):
//
//   spec driven development  8/8  1.00     rust                  7/10  0.70
//   ai driven sdlc           1/1  1.00     code review           6/10  0.60
//   kubernetes               8/10 0.80     developer experience  6/10  0.60
//   prompt injection         7/10 0.70     observability         4/10  0.40
//
// Mean 0.72; and for the seven queries the CLI answers with enough rows to rank
// at all, the browser's own top hit is somewhere in the CLI's top 10 in all
// seven cases. The bar this replaced — overlap >= min(4, cli.length) — was met
// exactly by "observability", so every query in the list could have decayed to
// 4-of-10 without turning anything red. These three bars are set under the
// measured figures with room for a corpus refresh to move them, and no longer
// let a uniform collapse to the per-query floor through.
const FLOOR = 0.40;   // no single query may agree less than this
const WEAK  = 0.50;   // ... and at most one may sit below this (today: observability)
const MEAN  = 0.60;   // the eight taken together (today 0.72)

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
    const rows = [];
    for (const q of CLI_QUERIES) {
      const cli = JSON.parse(execFileSync('python3', ['query.py', q, '-n', '10', '--json'],
        { cwd: TOOLS, maxBuffer: 1 << 26 }).toString()).map(h => h.id);
      await L.search(page, q);
      const web = (await L.cardIds(page)).slice(0, 10);
      const overlap = web.filter(i => cli.includes(i)).length;
      // The CLI's segment query needs every term inside one ~28-word passage, so on
      // a sparse query it finds a handful of rows and the browser legitimately
      // finds more. Judge the overlap against what the CLI actually returned.
      const denom = Math.min(10, cli.length);
      const ratio = denom ? overlap / denom : 0;
      rows.push({ q, cli, web, overlap, denom, ratio, topInCli: cli.includes(web[0]) });

      const floor = Math.max(1, Math.ceil(FLOOR * denom));
      L.check(`"${q}": the web top 10 still agrees with the CLI`,
        overlap >= floor,
        `${overlap}/${denom} = ${ratio.toFixed(2)}, floor ${floor}  ·  ` +
        `web=[${web.join(',')}]  cli=[${cli.join(',')}]`);
    }

    // The per-query floor only catches one query collapsing. Broad drift — every
    // query giving up a hit or two — shows up in the mean, and nowhere else.
    const mean = rows.reduce((a, r) => a + r.ratio, 0) / rows.length;
    L.check(`the two rankers agree on at least ${MEAN.toFixed(2)} of the CLI's hits on average`,
      mean >= MEAN,
      `mean ${mean.toFixed(2)} over ${rows.length} queries  ·  ` +
      rows.map(r => `${r.q}=${r.ratio.toFixed(2)}`).join(', '));

    const weak = rows.filter(r => r.ratio < WEAK);
    L.check(`at most one query agrees on less than ${Math.round(WEAK * 100)}% of the CLI's hits`,
      weak.length <= 1,
      weak.length
        ? weak.map(r => `${r.q} ${r.overlap}/${r.denom}`).join('; ')
        : `none below ${WEAK.toFixed(2)}`);

    // Set overlap says nothing about order. A query the CLI answers with one or
    // two rows cannot speak to rank, so only the properly ranked ones count.
    const rankable = rows.filter(r => r.cli.length >= 5);
    const off = rankable.filter(r => !r.topInCli);
    L.check("the browser's own top hit is one the CLI also ranks in its top 10",
      off.length <= 1,
      `${rankable.length - off.length}/${rankable.length} agree  ·  ` +
      (off.map(r => `${r.q}: web #1 is ${r.web[0]}, cli=[${r.cli.join(',')}]`).join('; ')
        || 'every one of them'));
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
