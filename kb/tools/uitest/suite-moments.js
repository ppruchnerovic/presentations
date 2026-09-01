// "Find this in the talk": the per-talk transcript is fetched on demand, the
// matching passages are ranked, and each one deep-links into the recording at
// the second it is spoken.
//
// Every check that depends on the transcript cache being cold opens its own
// page — a click earlier in the same session would have warmed it and made the
// assertion vacuous.

const L = require('./lib');
const fs = require('fs');
const path = require('path');

L.suite('moments', async browser => {
  // ---------- the passages themselves ----------
  {
    const page = await L.newPage(browser);
    await L.boot(page);
    await L.search(page, 'kubernetes');
    const card = page.locator('#results .card').first();
    const link = card.locator('.mo-load');
    L.check('the "Find this in the talk" link appears once a query exists',
      (await link.count()) === 1);

    await link.click();
    await page.waitForSelector('#results .card .moments .mo', { timeout: 15000 });
    const mo = await card.evaluate(c => {
      const rows = [...c.querySelectorAll('.mo')];
      return {
        n: rows.length,
        stamps: rows.map(r => r.querySelector('a.ts').textContent),
        hrefs: rows.map(r => r.querySelector('a.ts').getAttribute('href')),
        marks: rows.flatMap(r => [...r.querySelectorAll('mark')].map(m => m.textContent.toLowerCase())),
        label: c.querySelector('.mo-load').textContent,
      };
    });
    const secs = mo.hrefs.map(h => +h.match(/t=(\d+)s/)[1]);
    L.check('at most six passages are shown', mo.n > 0 && mo.n <= 6,
      `${mo.n} moments: ${mo.stamps.join(', ')}`);
    L.check('timestamps read as m:ss and ascend',
      mo.stamps.every(s => /^\d+:\d{2}$/.test(s)) && secs.every((v, i) => i === 0 || secs[i - 1] < v),
      mo.stamps.join(', '));
    L.check('each timestamp deep-links into the recording at that second',
      mo.hrefs.every(h => /^https:\/\/www\.youtube\.com\/watch\?v=[\w-]+&t=\d+s$/.test(h)), mo.hrefs[0]);
    // Passages within a minute of each other are the same moment said twice.
    L.check('the passages are at least 60s apart',
      secs.every((v, i) => i === 0 || v - secs[i - 1] >= 60), secs.join(','));
    L.check('query terms are highlighted in the passage text',
      mo.marks.length > 0 && mo.marks.every(m => m.startsWith('kub')), [...new Set(mo.marks)].join(','));
    L.check('the link relabels to "Hide moments"', mo.label === 'Hide moments', mo.label);

    await link.click();
    await page.waitForTimeout(200);
    const shut = await card.evaluate(c => ({
      hidden: c.querySelector('.mo-slot').hidden, label: c.querySelector('.mo-load').textContent }));
    L.check('a second click collapses them',
      shut.hidden === true && shut.label === 'Find this in the talk', JSON.stringify(shut));

    await link.click();
    await page.waitForTimeout(300);
    const back = await card.evaluate(c => ({
      hidden: c.querySelector('.mo-slot').hidden, n: c.querySelectorAll('.mo').length }));
    L.check('a third click re-opens them', back.hidden === false && back.n > 0, JSON.stringify(back));
    await page.close();
  }

  // ---------- the transcript is fetched once ----------
  {
    const page = await L.newPage(browser);
    const reqs = [];
    page.on('request', r => { if (/data\/transcripts\//.test(r.url())) reqs.push(r.url()); });
    await L.boot(page);
    await L.search(page, 'kubernetes');
    const link = page.locator('#results .card').first().locator('.mo-load');
    await link.click();
    await page.waitForSelector('.mo', { timeout: 15000 });
    const onOpen = reqs.length;
    await link.click(); await page.waitForTimeout(200);   // hide
    await link.click(); await page.waitForTimeout(600);   // show again
    L.check('the transcript is fetched once and then served from cache',
      onOpen === 1 && reqs.length === 1, `${onOpen} on open, ${reqs.length} total`);
    await page.close();
  }

  // ---------- a term in the metadata that is never actually spoken ----------
  {
    const page = await L.newPage(browser);
    await L.boot(page);
    // Build the case from real data rather than guessing a word: find a talk
    // with a title word that its own transcript never says.
    const pair = await page.evaluate(async () => {
      const meta = await fetch('data/search-meta.json').then(r => r.json());
      for (const t of meta.talks.slice(0, 120)) {
        const words = (t.t || '').toLowerCase().match(/[a-z]{5,}/g) || [];
        if (!words.length) continue;
        const tr = await fetch(`data/transcripts/${t.i}.json`).then(r => r.ok ? r.json() : null).catch(() => null);
        if (!tr) continue;
        const said = (tr.segments || []).map(s => s.text).join(' ').toLowerCase();
        const miss = words.find(w => !said.includes(w.slice(0, Math.max(4, w.length - 2))));
        if (miss) return { id: t.i, term: miss };
      }
      return null;
    });
    if (pair) {
      await L.search(page, pair.term);
      const card = page.locator(`#results .card[data-id="${pair.id}"]`);
      await card.locator('.mo-load').click();
      await page.waitForTimeout(1200);
      const txt = (await card.locator('.mo-slot').textContent()).trim();
      L.check('a term that is never spoken in a talk says so',
        /None of those words are spoken in this talk\./.test(txt), `"${pair.term}" in #${pair.id}: ${txt}`);
    } else {
      L.check('a term that is never spoken in a talk says so', false, 'could not construct the case');
    }
    await page.close();
  }

  // ---------- two words, said together ----------
  // Moments are ranked on the window that is shown, not on one ~6-word
  // caption: a two-word query almost never lands inside a single caption, so
  // scored that way the moments offered were wherever either word happened to
  // be, not where the speaker said them together — which is what put the talk
  // in the results in the first place.
  {
    const page = await L.newPage(browser);
    await L.boot(page);
    // Two words the top talk says together but not side by side — a phrase
    // like "vibe coding" shares a caption and would pass either way. Against
    // the caption-by-caption scorer this reads 2 of 6; against the window
    // scorer, 6 of 6.
    const [A, B] = ['agent', 'security'];
    await L.search(page, `${A} ${B}`);
    const card = page.locator('#results .card').first();
    const id = Number(await card.getAttribute('data-id'));
    await card.locator('.mo-load').click();
    await page.waitForSelector('#results .card .moments .mo', { timeout: 15000 });
    // How many windows in this talk say both words, at least 60s apart. The
    // page's tokeniser is inside its closure, so this is a small replica of
    // it — prefix matching included, as the page does for words of 4+ letters
    // — and MO_SPAN = 2 is the page's window width.
    const tr = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '..', 'data', 'transcripts', `${id}.json`), 'utf8'));
    const segs = tr.segments || [];
    const toks = segs.map(x => (x.text.toLowerCase().match(/[a-z0-9][a-z0-9+#.\-]*/g) || [])
      .map(t => t.replace(/^[.\-]+|[.\-]+$/g, '')));
    const says = (i, w) => toks[i].some(t => t.startsWith(w));
    let both = 0, last = -Infinity;
    for (let i = 0; i < segs.length; i++) {
      const lo = Math.max(0, i - 2), hi = Math.min(segs.length - 1, i + 2);
      let a = false, b = false;
      for (let j = lo; j <= hi; j++) { a = a || says(j, A); b = b || says(j, B); }
      if (a && b && segs[i].start - last >= 60) { both++; last = segs[i].start; }
    }
    const rows = await card.locator('.mo').allTextContents();
    const withBoth = rows.filter(r => new RegExp(`\\b${A}`, 'i').test(r) && new RegExp(`\\b${B}`, 'i').test(r)).length;
    L.check('the moments shown for a two-word query are the ones that say both words',
      both > 0 && withBoth >= Math.min(6, both),
      `${withBoth} of ${rows.length} moments say both; the talk (#${id}) has ${both} such windows`);
    await page.close();
  }

  // ---------- a transcript that will not load ----------
  {
    const page = await L.newPage(browser);
    await L.boot(page);
    await page.route('**/data/transcripts/*.json', r => r.fulfill({ status: 404, body: 'nope' }));
    await L.search(page, 'kubernetes');
    const card = page.locator('#results .card').first();
    await card.locator('.mo-load').click();
    await page.waitForTimeout(1200);
    L.check('a missing transcript degrades to a message, not a broken card',
      /Transcript unavailable\./.test((await card.locator('.mo-slot').textContent()).trim()),
      (await card.locator('.mo-slot').textContent()).trim());
    L.check('the 404 does not throw', page.__errors.length === 0, page.__errors.join(';'));
    await page.close();
  }
});
