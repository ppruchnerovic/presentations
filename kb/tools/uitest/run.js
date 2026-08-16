#!/usr/bin/env node
//
// Runs every suite against a throwaway static server and prints a tally.
//
//     node run.js                    # all suites
//     node run.js search filters     # only the named ones
//     KB_URL=https://… node run.js   # against a deployed copy, no local server
//
// Exits non-zero if anything failed, so it can gate a commit or a workflow.

const { spawn, spawnSync } = require('child_process');
const net = require('net');
const path = require('path');
const fs = require('fs');

const HERE = __dirname;
const SITE = path.join(HERE, '..', '..', '..');   // repo root, so /kb/ resolves

const SUITES = fs.readdirSync(HERE)
  .filter(f => /^suite-.*\.js$/.test(f))
  .sort();

const only = process.argv.slice(2);
const chosen = only.length
  ? SUITES.filter(f => only.some(o => f === `suite-${o}.js` || f === o))
  : SUITES;

if (!chosen.length) {
  console.error(`No suite matched ${only.join(', ')}. Available: ` +
    SUITES.map(s => s.replace(/^suite-|\.js$/g, '')).join(', '));
  process.exit(2);
}

const freePort = () => new Promise((resolve, reject) => {
  const s = net.createServer();
  s.once('error', reject);
  s.listen(0, '127.0.0.1', () => { const { port } = s.address(); s.close(() => resolve(port)); });
});

const waitFor = async url => {
  for (let i = 0; i < 100; i++) {
    try { if ((await fetch(url)).ok) return true; } catch (_) {}
    await new Promise(r => setTimeout(r, 100));
  }
  return false;
};

// Each suite is its own process: a suite that crashes outright still leaves the
// others' results intact, and one browser is never shared across suites.
const runSuite = (file, env) => new Promise(resolve => {
  const child = spawn(process.execPath, [path.join(HERE, file)],
    { env: { ...process.env, ...env }, stdio: ['ignore', 'pipe', 'pipe'] });
  let out = '';
  child.stdout.on('data', d => { out += d; process.stdout.write(d); });
  child.stderr.on('data', d => process.stderr.write(d));
  child.on('close', code => {
    const m = out.match(/##RESULT (\d+) (\d+)/);
    resolve(m
      ? { pass: +m[1], fail: +m[2] }
      // No tally line means the suite died before it could report one.
      : { pass: 0, fail: 1, crashed: true, code });
  });
});

(async () => {
  let server = null, base = process.env.KB_URL;

  if (!base) {
    if (!spawnSync('python3', ['-c', 'pass']).status === 0) {
      console.error('python3 is needed to serve the site, or set KB_URL to a deployed copy.');
      process.exit(2);
    }
    const port = await freePort();
    base = `http://127.0.0.1:${port}/kb/`;
    server = spawn('python3', ['-m', 'http.server', String(port), '-d', SITE],
      { stdio: 'ignore', detached: false });
    if (!await waitFor(base + 'index.html')) {
      server.kill();
      console.error(`Could not start a static server on ${port}.`);
      process.exit(2);
    }
  }
  console.log(`Testing ${base}\n`);

  const results = [];
  for (const file of chosen) {
    const name = file.replace(/^suite-|\.js$/g, '');
    console.log(`── ${name} ${'─'.repeat(Math.max(0, 60 - name.length))}`);
    const r = await runSuite(file, { KB_URL: base });
    results.push({ name, ...r });
    console.log('');
  }

  if (server) server.kill();

  const pass = results.reduce((a, r) => a + r.pass, 0);
  const fail = results.reduce((a, r) => a + r.fail, 0);
  console.log('═'.repeat(63));
  for (const r of results) {
    console.log(`  ${r.name.padEnd(12)} ${String(r.pass).padStart(3)} pass  ${String(r.fail).padStart(2)} fail` +
      (r.crashed ? `   (suite exited ${r.code} without reporting)` : ''));
  }
  console.log('═'.repeat(63));
  console.log(`  ${pass + fail} checks, ${fail} failing`);
  process.exit(fail ? 1 : 0);
})();
