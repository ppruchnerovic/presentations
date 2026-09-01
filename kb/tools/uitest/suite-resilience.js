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
  //
  // "It did not throw" is the weakest thing that can be said about a search: an
  // input that silently returns the wrong talks passes that bar. Each case below
  // therefore names the result set it expects, derived from what the page
  // promises rather than from what it happened to return — a metacharacter query
  // must equal its declawed twin, an em dash must vanish, an AND must narrow.
  //
  // page.__errors accumulates for the life of the page, so asserting
  // `__errors.length === 0` makes one throw redden every check after it and
  // hides which input was responsible. L.sinceErrors snapshots it so each check
  // reports only its own step.
  {
    const page = await L.newPage(browser);
    await L.boot(page);
    const N = (await L.meta(page)).talks.length;

    const outcome = async q => {
      const since = L.sinceErrors(page);
      await L.search(page, q);
      return {
        q,
        n: await L.resultCount(page),
        ids: await L.cardIds(page),
        empty: await L.emptyState(page),
        errs: since(),
      };
    };
    const threw = o => o.errs.length ? ` · threw: ${o.errs.join('; ')}` : '';
    const same = (a, b) => a.n === b.n && JSON.stringify(a.ids) === JSON.stringify(b.ids);

    // The status line echoes the query back, so it is the obvious injection point.
    const injected = L.sinceErrors(page);
    await L.search(page, '<img src=x onerror=alert(1)> kubernetes');
    const status = await page.evaluate(() => document.querySelector('#status').innerHTML);
    const smuggled = await page.evaluate(() => document.querySelectorAll('#status img, #results img').length);
    L.check('the echoed query is HTML-escaped',
      !/<img/i.test(status) && smuggled === 0 && injected().length === 0,
      status.replace(/\s+/g, ' ').slice(0, 110) + (injected().length ? ` · threw: ${injected().join('; ')}` : ''));

    const scripted = L.sinceErrors(page);
    await L.search(page, '"><script>window.__x=1</script>');
    L.check('script injection through the query does not execute',
      !(await page.evaluate(() => window.__x === 1)) && scripted().length === 0,
      scripted().join('; ') || 'window.__x unset');

    // highlight() builds a RegExp out of the query terms and tokenize() keeps
    // only [a-z0-9+#.-], so every one of these has a plain-text twin that must
    // return the identical result set. Compiled rather than escaped, `c++ (*)`
    // would throw "nothing to repeat" and `[test]` would quietly match t, e or s
    // — both of which this catches, where counting exceptions did not.
    for (const [q, twin] of [['c++ (*)', 'c++'], ['a\\b', ''], ['[test]', 'test'], ['$^.*+?', '']]) {
      const hostile = await outcome(q);
      const plain = await outcome(twin);
      L.check(`regex metacharacters in "${q}" are treated literally`,
        same(hostile, plain) && hostile.errs.length === 0,
        `${hostile.n} hits vs ${plain.n} for ${twin ? `"${twin}"` : 'no query at all'}` +
        ` · top ids [${hostile.ids.slice(0, 3)}] vs [${plain.ids.slice(0, 3)}]${threw(hostile)}`);
    }

    const long = await outcome('a'.repeat(400));
    L.check('a 400-character query matches nothing and shows the empty state',
      long.n === 0 && long.empty === 'Nothing matched' && long.errs.length === 0,
      `${long.n} hits, empty state ${JSON.stringify(long.empty)}${threw(long)}`);

    // The tokeniser is ASCII-only, so a CJK query yields no terms at all. That
    // is the same road a stopword-only query takes: browse the catalogue rather
    // than claim nothing matched.
    const cjk = await outcome('日本語 テスト');
    const browsing = await outcome('');
    L.check('non-Latin input falls back to browsing the catalogue, not to an empty result',
      cjk.n === N && same(cjk, browsing) && cjk.errs.length === 0,
      `${cjk.n} hits vs ${N} talks, and the same first ids as no query at all` +
      ` [${cjk.ids.slice(0, 3)}] vs [${browsing.ids.slice(0, 3)}]${threw(cjk)}`);

    const dashed = await outcome('ai — agents');
    const spaced = await outcome('ai agents');
    L.check('punctuation-only tokens are dropped, not searched for',
      same(dashed, spaced) && dashed.errs.length === 0,
      `"ai — agents"=${dashed.n} vs "ai agents"=${spaced.n}` +
      ` · top ids [${dashed.ids.slice(0, 3)}] vs [${spaced.ids.slice(0, 3)}]${threw(dashed)}`);

    // Every term has to appear somewhere, so eight of them can only ever narrow.
    const TERMS = ['ai', 'agents', 'security', 'testing', 'kubernetes', 'rust',
      'typescript', 'observability'];
    const singles = {};
    for (const t of TERMS) singles[t] = (await outcome(t)).n;
    const narrowest = Math.min(...Object.values(singles));
    const all8 = await outcome(TERMS.join(' '));
    L.check('an eight-term AND query narrows to a subset of its rarest term',
      all8.n <= narrowest && all8.errs.length === 0 &&
      (all8.n === 0 ? all8.empty === 'Nothing matched' : all8.ids.length > 0),
      `8 terms = ${all8.n} hits, rarest single term = ${narrowest} ` +
      `(${Object.entries(singles).map(([t, n]) => `${t}:${n}`).join(' ')})` +
      `, empty state ${JSON.stringify(all8.empty)}${threw(all8)}`);
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
