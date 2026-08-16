// How the page loads, what it costs, and whether a URL someone sends you shows
// them what you were looking at.

const L = require('./lib');

L.suite('navigation', async browser => {
  const page = await L.newPage(browser);

  // ---------- cold load ----------
  const t0 = Date.now();
  await L.boot(page);
  const bootMs = Date.now() - t0;
  const perf = await page.evaluate(() => {
    const r = performance.getEntriesByType('resource');
    return {
      n: r.length,
      kb: Math.round(r.reduce((a, x) => a + (x.transferSize || x.encodedBodySize || 0), 0) / 1024),
      biggest: r.map(x => [x.name.split('/').slice(-2).join('/'), Math.round((x.encodedBodySize || 0) / 1024)])
        .sort((a, b) => b[1] - a[1]).slice(0, 3),
    };
  });
  L.check('the catalogue is usable within a couple of seconds', bootMs < 4000,
    `${bootMs}ms, ${perf.n} requests, ~${perf.kb}KB — ${JSON.stringify(perf.biggest)}`);
  // The whole point of sharding the transcript index is that a visitor who
  // never searches never downloads it.
  L.check('the transcript shards are not loaded up front',
    perf.n <= 3, `${perf.n} requests before any query`);

  const before = await page.evaluate(() => performance.getEntriesByType('resource').length);
  await L.search(page, 'observability');
  const after = await page.evaluate(() => performance.getEntriesByType('resource').length);
  L.check('a query lazily fetches only the shards it needs',
    after - before <= 3, `${after - before} extra fetches`);

  const warm = Date.now();
  await L.search(page, 'observability platform');
  L.check('a warm query stays responsive', Date.now() - warm < 1500, `${Date.now() - warm}ms`);

  // ---------- history ----------
  // Searching rewrites the hash in place rather than pushing an entry, so Back
  // leaves the explorer instead of stepping backwards through queries. That is
  // a deliberate trade: it keeps a session of typing out of the back stack.
  await L.search(page, 'rust');
  const h1 = await page.evaluate(() => location.hash);
  await L.search(page, 'kubernetes');
  const h2 = await page.evaluate(() => location.hash);
  await page.goBack().catch(() => {});
  await page.waitForTimeout(500);
  const h3 = await page.evaluate(() => location.hash);
  L.check('searching updates the URL in place', h1 !== h2 && h3 !== h1,
    `"${h1}" -> "${h2}" -> back gives "${h3}"`);

  // ---------- a shared link ----------
  await page.goto(L.BASE);
  await page.waitForFunction(() => !/Loading/.test(document.querySelector('#sub').textContent),
    null, { timeout: 20000 });
  await L.search(page, 'prompt injection');
  await page.selectOption('#f-sort', 'title');
  await page.waitForTimeout(400);
  const url = await page.evaluate(() => location.href);
  const mine = await L.cardIds(page);

  const theirs = await L.newPage(browser);
  await theirs.goto(url);
  await theirs.waitForFunction(() => !/Loading/.test(document.querySelector('#sub').textContent),
    null, { timeout: 20000 });
  await theirs.waitForTimeout(700);
  L.check('pasting the URL into a fresh tab reproduces the same view',
    JSON.stringify(mine) === JSON.stringify(await L.cardIds(theirs)),
    `${mine.length} vs ${(await L.cardIds(theirs)).length} cards`);
  await theirs.close();

  // ---------- the explorer sits inside the site ----------
  await page.goto(L.BASE.replace(/kb\/$/, ''));
  await page.waitForTimeout(400);
  const into = await page.evaluate(() =>
    [...document.querySelectorAll('a')].map(a => a.getAttribute('href')).filter(h => /kb/.test(h || '')));
  L.check('the site index links to the explorer', into.length > 0, into.join(', '));

  await L.boot(page);
  const out = await page.evaluate(() =>
    [...document.querySelectorAll('.kicker a, footer a')].map(a => a.getAttribute('href')));
  L.check('the explorer links back to the site', out.includes('../'), out.join(', '));

  L.check('no failed requests', page.__requests.length === 0, page.__requests.slice(0, 3).join('; '));
});
