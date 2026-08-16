// Shared harness for the talk explorer's browser tests.
//
// Every suite is an ordinary Node script: require this, call `suite(...)`, and
// assert with `check(...)`. Suites are run as separate processes by run.js, so
// one crashing suite cannot take the rest of the run down with it.

const { chromium } = require('playwright');

// run.js sets this; a suite run by hand falls back to the default port.
const BASE = process.env.KB_URL || 'http://localhost:8765/kb/';

let passed = 0, failed = 0;

// A failing check prints what it actually saw. Chasing a red line without that
// detail means re-instrumenting the test to learn anything, so `detail` is
// worth filling in even on the checks you expect to pass.
function check(name, cond, detail = '') {
  if (cond) passed++; else failed++;
  console.log(`${cond ? 'PASS' : 'FAIL'}  ${name}${detail ? '  — ' + detail : ''}`);
}

// A page that remembers what went wrong on it. Console errors, uncaught
// exceptions and dead requests are failures in their own right — several of
// the checks below assert these stayed empty.
async function newPage(browser, opts = {}) {
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 }, ...opts });
  const page = await ctx.newPage();
  page.__console = [];
  page.__errors = [];
  page.__requests = [];
  page.on('console', m => {
    if (m.type() === 'error' || m.type() === 'warning') page.__console.push(`${m.type()}: ${m.text()}`);
  });
  page.on('pageerror', e => page.__errors.push(String(e)));
  page.on('requestfailed', r => page.__requests.push(`${r.url()} ${r.failure()?.errorText}`));
  return page;
}

// The catalogue is fetched after load, so "the page responded" is not the same
// as "the page is usable". Wait for the subtitle to stop saying "Loading".
async function boot(page, hash = '') {
  await page.goto(BASE + hash, { waitUntil: 'load' });
  await page.waitForFunction(() => !/Loading/.test(document.querySelector('#sub').textContent),
    null, { timeout: 20000 });
  await page.waitForTimeout(150);
  return page;
}

// Typing is debounced by 140ms and the shard fetch is async, so a search is not
// done when fill() returns.
async function search(page, q) {
  await page.fill('#q', q);
  await page.waitForTimeout(450);
  await page.waitForFunction(() => !document.querySelector('#results .spinner'),
    null, { timeout: 15000 }).catch(() => {});
}

const statusText = page => page.textContent('#status');
const cardCount = page => page.locator('#results .card').count();
const titles = page => page.$$eval('#results .card h2 a', a => a.map(x => x.textContent.trim()));
const cardIds = page => page.$$eval('#results .card', cs => cs.map(c => Number(c.dataset.id)));

// The leading number in the status line, which is the result count.
const resultCount = async page =>
  Number((((await statusText(page)).trim().match(/^(\d+)/)) || [0, 0])[1]);

const meta = page => page.evaluate(() => fetch('data/search-meta.json').then(r => r.json()));

// Wraps a suite body: owns the browser, reports the tally in the form run.js
// parses, and turns a thrown error into a failure rather than a silent exit.
async function suite(name, body) {
  const browser = await chromium.launch();
  try {
    await body(browser);
  } catch (err) {
    check(`${name}: suite ran to completion`, false, String(err && err.stack || err));
  } finally {
    await browser.close();
  }
  console.log(`##RESULT ${passed} ${failed}`);
  process.exit(failed ? 1 : 0);
}

module.exports = {
  BASE, chromium, check, newPage, boot, search,
  statusText, cardCount, titles, cardIds, resultCount, meta, suite,
};
