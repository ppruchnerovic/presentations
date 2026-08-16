// "Find this in the talk": the per-talk transcript is fetched on demand, the
// matching passages are ranked, and each one deep-links into the recording at
// the second it is spoken.
//
// Every check that depends on the transcript cache being cold opens its own
// page — a click earlier in the same session would have warmed it and made the
// assertion vacuous.

const L = require('./lib');

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
