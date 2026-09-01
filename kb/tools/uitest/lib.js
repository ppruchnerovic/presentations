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
  await ctx.addInitScript(RENDER_PROBE);
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
// done when fill() returns — something has to wait for the answer to land.
//
// The page's only settle signal is the render itself: render() reassigns
// #results.innerHTML, which always replaces that element's children, so one
// mutation of #results means exactly one repaint of the result list. This probe
// counts them. (The obvious-looking alternative, waiting for `#results .spinner`
// to clear, waits for nothing at all: the only spinner in the page belongs to
// the per-talk moment loader, so during a search that selector is already empty
// and the wait resolves on its first evaluation.)
const RENDER_PROBE = () => {
  window.__renders = 0;
  const attach = () => {
    const res = document.querySelector('#results');
    if (!res) { setTimeout(attach, 10); return; }
    new MutationObserver(() => { window.__renders++; }).observe(res, { childList: true });
  };
  attach();
};

// A search that never settles is a failure, not something to shrug off: the
// suite would otherwise carry on and assert against the *previous* query's DOM.
// Every query the suites run does re-render — an empty or stopword-only query
// renders the whole catalogue, a hopeless one renders the empty state — so
// waiting is the default. `{ settle: false }` is the explicit opt-out for a call
// site that genuinely expects the results list to be left alone.
async function search(page, q, { settle = true, timeout = 15000 } = {}) {
  const before = await page.evaluate(() => window.__renders);
  if (typeof before !== 'number') {
    throw new Error('search(): no render probe on this page — it must come from newPage().');
  }
  await page.fill('#q', q);
  if (!settle) { await page.waitForTimeout(450); return; }

  const t0 = Date.now();
  try {
    await page.waitForFunction(n => window.__renders > n, before, { timeout, polling: 25 });
  } catch (_) {
    const seen = await page.evaluate(() => ({
      input: document.querySelector('#q')?.value,
      status: (document.querySelector('#status')?.textContent || '').trim().slice(0, 80),
      cards: document.querySelectorAll('#results .card').length,
      empty: document.querySelector('.empty h3')?.textContent || null,
    })).catch(e => ({ unreadable: String(e) }));
    throw new Error(`search(${JSON.stringify(q)}) never re-rendered #results: ` +
      `waited ${Date.now() - t0}ms of ${timeout}ms and the render count stayed at ${before}. ` +
      `The list still shows ${JSON.stringify(seen)} — anything asserted from here on ` +
      `would be asserting against the query before this one.`);
  }
  // render() is synchronous, so the mutation means the DOM, the status line and
  // the hash are all already written; this only lets the layout settle.
  await page.waitForTimeout(60);
}

// page.__errors accumulates for the life of the page, so `__errors.length === 0`
// reddens every check after the one that actually threw. Snapshot first, and a
// check can then speak only about its own step.
function sinceErrors(page) {
  const mark = page.__errors.length;
  return () => page.__errors.slice(mark);
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

// locator('.empty h3').textContent() blocks for the full locator timeout when
// there is no empty state, which is the interesting case as often as not.
const emptyState = page =>
  page.evaluate(() => document.querySelector('.empty h3')?.textContent ?? null);

module.exports = {
  BASE, chromium, check, newPage, boot, search, sinceErrors,
  statusText, cardCount, titles, cardIds, resultCount, emptyState, meta, suite,
};
