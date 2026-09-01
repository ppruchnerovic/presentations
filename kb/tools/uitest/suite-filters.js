// Track / type / stage filters, the three sort orders, Reset, and the hash
// that makes any view a shareable link.

const L = require('./lib');

L.suite('filters', async browser => {
  const page = await L.newPage(browser);
  await L.boot(page);
  const meta = await L.meta(page);
  const N = meta.talks.length;
  const byId = new Map(meta.talks.map(t => [t.i, t]));

  // ---------- each filter, against the data ----------
  const track = [...new Set(meta.talks.map(t => t.k).filter(Boolean))].sort()[1];
  await page.selectOption('#f-track', track);
  await page.waitForTimeout(300);
  const expTrack = meta.talks.filter(t => t.k === track).length;
  L.check(`track "${track}" returns exactly the talks in it`,
    (await L.resultCount(page)) === expTrack, `${await L.resultCount(page)} vs ${expTrack}`);
  L.check('every card shown belongs to that track',
    (await L.cardIds(page)).every(i => byId.get(i).k === track));

  const typesIn = [...new Set(meta.talks.filter(t => t.k === track).map(t => t.y).filter(Boolean))];
  await page.selectOption('#f-type', typesIn[0]);
  await page.waitForTimeout(300);
  const expBoth = meta.talks.filter(t => t.k === track && t.y === typesIn[0]).length;
  L.check(`track and type stack ("${typesIn[0]}")`,
    (await L.resultCount(page)) === expBoth, `${await L.resultCount(page)} vs ${expBoth}`);

  const stage = [...new Set(meta.talks.map(t => t.g).filter(Boolean))].sort()[0];
  await page.selectOption('#f-track', '');
  await page.selectOption('#f-type', '');
  await page.selectOption('#f-stage', stage);
  await page.waitForTimeout(300);
  const expStage = meta.talks.filter(t => t.g === stage).length;
  L.check(`stage "${stage}" returns exactly the talks on it`,
    (await L.resultCount(page)) === expStage, `${await L.resultCount(page)} vs ${expStage}`);

  // ---------- a filter narrows a search rather than replacing it ----------
  await page.selectOption('#f-stage', '');
  await page.waitForTimeout(200);
  await L.search(page, 'ai');
  const aiAll = await L.resultCount(page);
  await page.selectOption('#f-stage', stage);
  await page.waitForTimeout(350);
  const aiStage = await L.resultCount(page);
  L.check('a filter narrows an existing search',
    aiStage > 0 && aiStage < aiAll && (await L.cardIds(page)).every(i => byId.get(i).g === stage),
    `ai=${aiAll} -> ai+${stage}=${aiStage}`);

  const impossible = [...new Set(meta.talks.map(t => t.k).filter(Boolean))]
    .find(k => !meta.talks.some(t => t.k === k && t.g === stage));
  await page.selectOption('#f-track', impossible);
  await page.waitForTimeout(300);
  L.check('contradictory filters show the empty state',
    (await page.locator('.empty h3').textContent().catch(() => null)) === 'Nothing matched');

  // ---------- sorting ----------
  await page.selectOption('#f-track', '');
  await page.selectOption('#f-stage', '');
  await L.search(page, 'kubernetes');
  await page.selectOption('#f-sort', 'title');
  await page.waitForTimeout(350);
  const alpha = await L.titles(page);
  L.check('Title A–Z sorts alphabetically',
    JSON.stringify(alpha) === JSON.stringify([...alpha].sort((a, b) => a.localeCompare(b))),
    alpha.slice(0, 2).join(' | '));

  await page.selectOption('#f-sort', 'sched');
  await page.waitForTimeout(350);
  const starts = (await L.cardIds(page)).map(i => new Date(byId.get(i).st).getTime());
  L.check('Schedule order is chronological',
    starts.every((v, i) => i === 0 || starts[i - 1] <= v), JSON.stringify(starts.slice(0, 3)));

  await page.selectOption('#f-sort', 'rel');
  await page.waitForTimeout(350);
  const ranked = await L.titles(page);
  L.check('Most relevant restores the ranked order',
    /kubernetes/i.test(ranked[0]) && JSON.stringify(ranked) !== JSON.stringify(alpha), ranked[0]);

  // Relevance means nothing without a query, so it degrades to schedule order
  // and the status line says so rather than leaving the picker looking broken.
  await L.search(page, '');
  L.check('relevance without a query explains its fallback',
    /ordered by schedule/.test((await L.statusText(page)).trim()),
    (await L.statusText(page)).trim().slice(0, 70));

  // ---------- reset ----------
  await L.search(page, 'kubernetes');
  await page.selectOption('#f-track', track);
  await page.selectOption('#f-sort', 'title');
  await page.waitForTimeout(300);
  await page.click('#clear');
  await page.waitForTimeout(350);
  const after = await page.evaluate(() => ({
    q: document.querySelector('#q').value,
    track: document.querySelector('#f-track').value,
    type: document.querySelector('#f-type').value,
    stage: document.querySelector('#f-stage').value,
    sort: document.querySelector('#f-sort').value,
    tr: document.querySelector('#f-tr').classList.contains('on'),
    hash: location.hash,
  }));
  L.check('Reset clears the query, the filters and the sort',
    after.q === '' && !after.track && !after.type && !after.stage && after.sort === 'rel' && !after.tr,
    JSON.stringify(after));
  L.check('Reset restores the whole catalogue', (await L.resultCount(page)) === N);
  L.check('Reset clears the URL hash', after.hash === '', `hash="${after.hash}"`);

  // ---------- the hash ----------
  const reload = async hash => {
    await page.goto(L.BASE + hash);
    await page.reload();
    await page.waitForFunction(() => !/Loading/.test(document.querySelector('#sub').textContent),
      null, { timeout: 20000 });
    await page.waitForTimeout(500);
  };

  await reload(`#q=kubernetes&track=${encodeURIComponent(track)}&sort=title`);
  const restored = await page.evaluate(() => ({
    q: document.querySelector('#q').value,
    track: document.querySelector('#f-track').value,
    sort: document.querySelector('#f-sort').value,
  }));
  L.check('q, track and sort are restored from the hash',
    restored.q === 'kubernetes' && restored.track === track && restored.sort === 'title',
    JSON.stringify(restored));
  const dl = await L.titles(page);
  L.check('the restored state is actually applied to the results',
    dl.length > 0 && JSON.stringify(dl) === JSON.stringify([...dl].sort((a, b) => a.localeCompare(b))),
    `${dl.length} cards`);

  await L.search(page, 'rust');
  const hash = await page.evaluate(() => location.hash);
  L.check('the hash tracks the live state', /q=rust/.test(hash) && /sort=title/.test(hash), hash);

  // tr=1 must not switch on a filter the UI is deliberately hiding.
  await reload(`#stage=${encodeURIComponent(stage)}&tr=1`);
  const rt = await page.evaluate(() => ({
    stage: document.querySelector('#f-stage').value,
    tr: document.querySelector('#f-tr').classList.contains('on'),
    trHidden: document.querySelector('#f-tr').hidden,
  }));
  L.check('stage round-trips, and tr=1 is ignored while that toggle is hidden',
    rt.stage === stage && rt.tr === false && rt.trHidden === true, JSON.stringify(rt));

  // The production case for "Transcript only". suite-a11y.js exercises that
  // toggle and the per-card "transcript" badge, but only against a catalogue it
  // rewrites on the way in to zero every third talk's word count — with the real
  // corpus at full coverage the control is hidden and unclickable, so nothing
  // over there says what the shipped page does. What it must do is nothing at
  // all: a hidden filter that quietly dropped rows would leave a shared #tr=1
  // link returning an empty page, and no other check would notice.
  const withTr = meta.talks.filter(t => t.w > 0).length;
  const shown = await L.resultCount(page);
  if (withTr === N) {
    L.check('at full transcript coverage the hidden toggle filters nothing',
      rt.trHidden === true && shown === expStage,
      `${withTr}/${N} talks have a transcript · #tr=1 on "${stage}" shows ${shown}, expected ${expStage}`);
  } else {
    L.check('at partial transcript coverage the toggle is offered instead of hidden',
      rt.trHidden === false, `${withTr}/${N} talks have a transcript`);
  }

  await reload('#track=NoSuchTrack&sort=bogus&q=agents');
  const bad = await page.evaluate(() => ({
    track: document.querySelector('#f-track').value,
    sort: document.querySelector('#f-sort').value,
    cards: document.querySelectorAll('#results .card').length,
  }));
  L.check('unknown filter and sort values fall back safely',
    bad.track === '' && bad.sort === 'rel' && bad.cards > 0, JSON.stringify(bad));

  L.check('no uncaught errors', page.__errors.length === 0, page.__errors.join('; '));
});
