// What the explorer looks like before anyone has typed anything: the catalogue
// loaded, the filters populated from the data rather than hardcoded, and one
// card rendered correctly end to end.

const L = require('./lib');

L.suite('load', async browser => {
  const page = await L.newPage(browser);
  await L.boot(page);

  const meta = await L.meta(page);
  const n = meta.talks.length;
  const withTr = meta.talks.filter(t => t.w > 0).length;

  const sub = await page.textContent('#sub');
  L.check('subtitle reports the catalogue size', /\d+ recorded talks/.test(sub), sub);
  L.check('subtitle count matches the data', sub.includes(String(n)),
    `${sub} vs ${n} talks / ${withTr} transcripts`);

  const cards = await L.cardCount(page);
  L.check('first page renders 20 cards', cards === 20, `got ${cards}`);

  const status = (await L.statusText(page)).trim();
  L.check('status shows the total and the schedule-order note',
    status.includes(String(n)) && /ordered by schedule/.test(status), status);

  // ---------- filter dropdowns are built from the data ----------
  const opts = await page.evaluate(() => ({
    track: [...document.querySelectorAll('#f-track option')].map(o => o.value),
    type: [...document.querySelectorAll('#f-type option')].map(o => o.value),
    stage: [...document.querySelectorAll('#f-stage option')].map(o => o.value),
    sort: [...document.querySelectorAll('#f-sort option')].map(o => o.value),
  }));
  const uniq = key => [...new Set(meta.talks.map(t => t[key]).filter(Boolean))].sort();
  for (const [label, sel, key] of [['track', opts.track, 'k'], ['type', opts.type, 'y'], ['stage', opts.stage, 'g']]) {
    L.check(`${label} options match the data`,
      JSON.stringify(sel.slice(1)) === JSON.stringify(uniq(key)), `${sel.length - 1} options`);
  }
  L.check('sort offers relevance / schedule / title',
    JSON.stringify(opts.sort) === JSON.stringify(['rel', 'sched', 'title']));

  // A filter that matches every talk is a dead control, so the UI hides the
  // transcript toggle until coverage is actually partial.
  const trHidden = await page.locator('#f-tr').isHidden();
  L.check('"Transcript only" is hidden exactly when every talk has a transcript',
    trHidden === (withTr === n), `hidden=${trHidden}, ${withTr}/${n} with transcripts`);

  // ---------- default order ----------
  const byId = new Map(meta.talks.map(t => [t.i, t]));
  const starts = (await L.cardIds(page)).map(i => new Date(byId.get(i).st).getTime());
  L.check('the unsearched listing is in schedule order',
    starts.every((v, i) => i === 0 || starts[i - 1] <= v), JSON.stringify(starts.slice(0, 3)));

  // ---------- one card, in full ----------
  const first = page.locator('#results .card').first();
  const a = await first.evaluate(c => ({
    href: c.querySelector('h2 a')?.getAttribute('href'),
    target: c.querySelector('h2 a')?.getAttribute('target'),
    rel: c.querySelector('h2 a')?.getAttribute('rel'),
    badges: [...c.querySelectorAll('.badges .b')].map(b => b.textContent),
    session: [...c.querySelectorAll('.links a')].map(x => x.getAttribute('href'))[1],
    findLink: !!c.querySelector('.mo-load'),
  }));
  L.check('the title links to the YouTube recording',
    /^https:\/\/www\.youtube\.com\/watch\?v=/.test(a.href), a.href);
  L.check('external links open in a new tab with noopener',
    a.target === '_blank' && a.rel === 'noopener');
  L.check('the session page is linked', /wearedevelopers\.com\/events\//.test(a.session || ''), a.session);
  L.check('badges carry track, type, stage, slot and duration',
    a.badges.length >= 4, JSON.stringify(a.badges));
  L.check('"Find this in the talk" is absent until something is searched for', a.findLink === false);

  // The API reports UTC; the conference runs on Berlin time.
  const slot = a.badges.find(b => /^Day \d/.test(b));
  const expect = await page.evaluate(t => {
    const f = new Intl.DateTimeFormat('en-GB',
      { timeZone: 'Europe/Berlin', hour: '2-digit', minute: '2-digit', hour12: false });
    return `Day ${t.day} · ${f.format(new Date(t.st))}`;
  }, byId.get((await L.cardIds(page))[0]));
  L.check('the slot badge is formatted in Europe/Berlin', slot === expect, `${slot} vs ${expect}`);

  L.check('no uncaught errors', page.__errors.length === 0, page.__errors.join('; '));
  L.check('no failed requests', page.__requests.length === 0, page.__requests.join('; '));
  L.check('no console errors', page.__console.length === 0, page.__console.join('; '));
});
