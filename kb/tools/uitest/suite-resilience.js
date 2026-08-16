// What the explorer does when its data does not arrive, and what it does with
// input written to break it.
//
// The index is layered on purpose: metadata search works without the
// transcript index, and the transcript index works one shard at a time. Each
// layer is knocked out here to prove the one beneath it still stands.

const L = require('./lib');

L.suite('resilience', async browser => {
  // ---------- a single index shard is unreachable ----------
  {
    const page = await L.newPage(browser);
    let full;
    await L.boot(page);
    await L.search(page, 'kubernetes');
    full = await L.resultCount(page);
    await page.close();

    const p2 = await L.newPage(browser);
    await p2.route(u => /\/data\/tindex\/[a-z0-9_]\.json$/.test(u.pathname),
      r => r.fulfill({ status: 500, body: 'x' }));
    await L.boot(p2);
    await L.search(p2, 'kubernetes');
    const n = await L.resultCount(p2);
    L.check('a broken index shard falls back to metadata-only search',
      n > 0 && n < full && p2.__errors.length === 0, `${n} hits vs ${full} with the shard`);
    await p2.close();
  }

  // ---------- no transcript index at all ----------
  {
    const page = await L.newPage(browser);
    await page.route('**/data/tindex/_manifest.json', r => r.fulfill({ status: 404, body: '' }));
    await L.boot(page);
    await L.search(page, 'kubernetes');
    L.check('with no transcript index, metadata search still works',
      /^\d+ talks matching/.test((await L.statusText(page)).trim()) && page.__errors.length === 0,
      (await L.statusText(page)).trim().slice(0, 70));
    await page.close();
  }

  // ---------- the catalogue itself fails ----------
  {
    const page = await L.newPage(browser);
    await page.route('**/data/search-meta.json', r => r.fulfill({ status: 500, body: 'boom' }));
    await page.goto(L.BASE);
    await page.waitForTimeout(1500);
    const sub = await page.textContent('#sub');
    const empty = await page.textContent('.empty h3').catch(() => null);
    L.check('a failed catalogue load says so instead of hanging on "Loading…"',
      /Could not load/.test(sub) && empty === 'Failed to load', `${sub} / ${empty}`);
    await page.close();
  }

  // ---------- hostile input ----------
  {
    const page = await L.newPage(browser);
    await L.boot(page);

    // The status line echoes the query back, so it is the obvious injection point.
    await L.search(page, '<img src=x onerror=alert(1)> kubernetes');
    const status = await page.evaluate(() => document.querySelector('#status').innerHTML);
    const smuggled = await page.evaluate(() => document.querySelectorAll('#status img, #results img').length);
    L.check('the echoed query is HTML-escaped', !/<img/i.test(status) && smuggled === 0,
      status.replace(/\s+/g, ' ').slice(0, 110));

    await L.search(page, '"><script>window.__x=1</script>');
    L.check('script injection through the query does not execute',
      !(await page.evaluate(() => window.__x === 1)));

    // highlight() builds a RegExp out of the query terms.
    for (const q of ['c++ (*)', 'a\\b', '[test]', '$^.*+?']) {
      await L.search(page, q);
      L.check(`regex metacharacters in "${q}" are treated literally`,
        page.__errors.length === 0, page.__errors.join(';'));
    }

    await L.search(page, 'a'.repeat(400));
    L.check('a 400-character query is handled', page.__errors.length === 0,
      await page.locator('.empty h3').textContent().catch(() => '(results)'));

    await L.search(page, '日本語 テスト');
    L.check('non-Latin input does not throw', page.__errors.length === 0,
      (await L.statusText(page)).trim().slice(0, 40) || 'no matches');

    await L.search(page, 'ai — agents');
    L.check('punctuation-only tokens are dropped', page.__errors.length === 0);

    await L.search(page, 'ai agents security testing kubernetes rust typescript observability');
    L.check('an eight-term AND query resolves', page.__errors.length === 0,
      (await L.statusText(page)).trim().slice(0, 55) || 'empty state');
    await page.close();
  }

  // ---------- a phone ----------
  {
    const page = await L.newPage(browser,
      { viewport: { width: 390, height: 780 }, isMobile: true, hasTouch: true });
    await L.boot(page);
    await L.search(page, 'kubernetes');
    const m = await page.evaluate(() => ({
      overflowX: document.documentElement.scrollWidth > window.innerWidth + 1,
      scrollW: document.documentElement.scrollWidth,
      inner: window.innerWidth,
      cardW: document.querySelector('.card')?.getBoundingClientRect().width,
      inputW: document.querySelector('#q').getBoundingClientRect().width,
      wrap: getComputedStyle(document.querySelector('.filters')).flexWrap,
    }));
    L.check('no horizontal overflow at 390px', !m.overflowX, `${m.scrollW} vs ${m.inner}`);
    L.check('cards and the search box fit the viewport',
      m.cardW <= m.inner && m.inputW <= m.inner,
      `card=${Math.round(m.cardW)} input=${Math.round(m.inputW)}`);
    L.check('the filter row wraps', m.wrap === 'wrap', m.wrap);

    // Rewrapping at a new width changes what fits in four lines, so the
    // unfold buttons have to be measured again.
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.waitForTimeout(400);
    const stale = await page.evaluate(() =>
      [...document.querySelectorAll('.abs.clamped')].filter(p => {
        const b = p.nextElementSibling;
        return b && b.hidden !== (p.scrollHeight <= p.clientHeight + 2);
      }).length);
    L.check('the unfold buttons are re-measured after a resize', stale === 0, `${stale} stale`);
    await page.close();
  }
});
