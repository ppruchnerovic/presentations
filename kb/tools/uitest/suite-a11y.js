// Screen-reader and keyboard access, plus text contrast.
//
// Also the partial-transcript-coverage path, which no amount of clicking can
// reach today: all 358 talks have a transcript, so the "Transcript only" toggle
// and the per-card "transcript" badge stay hidden. The catalogue response is
// rewritten on the way in to simulate the refresh that brings in a talk whose
// captions could not be fetched.
//
// READ THIS BEFORE TRUSTING THE FIRST BLOCK. Its coverage is against a mock and
// nothing else: the interception below zeroes `t.w` on every third talk, which
// is why this suite reports "238 full transcripts" while the site reports 358.
// Production data cannot reach that toggle or that badge, so no check here says
// anything about how the shipped page behaves. The production case — full
// coverage, therefore the toggle hidden and filtering nothing — is asserted in
// suite-filters.js instead, and the two need to be read together.

const L = require('./lib');

// A contrast figure is only meaningful once each translucent layer is
// composited over the one beneath it — the chips sit on rgba() backgrounds.
const parse = c => { const p = c.match(/[\d.]+/g).map(Number); return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
const over = (fg, bg) => ({ r: fg.r * fg.a + bg.r * (1 - fg.a), g: fg.g * fg.a + bg.g * (1 - fg.a),
                            b: fg.b * fg.a + bg.b * (1 - fg.a), a: 1 });
const lum = c => { const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
  return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
const ratio = (fg, bg, base) => {
  const b = over(parse(bg), parse(base));
  const [hi, lo] = [lum(over(parse(fg), b)), lum(b)].sort((p, q) => q - p);
  return (hi + 0.05) / (lo + 0.05);
};

L.suite('a11y', async browser => {
  // ---------- partial transcript coverage ----------
  {
    const page = await L.newPage(browser);
    // Every third talk loses its transcript word count. From here to the end of
    // this block the page is running on data the site never serves.
    await page.route('**/data/search-meta.json', async route => {
      const json = await (await route.fetch()).json();
      json.talks.forEach((t, i) => { if (i % 3 === 0) t.w = 0; });
      await route.fulfill({ json });
    });
    await L.boot(page);

    L.check('"Transcript only" appears when coverage is partial',
      await page.locator('#f-tr').isVisible(), await page.textContent('#sub'));
    const badged = await page.evaluate(() =>
      [...document.querySelectorAll('#results .card')]
        .filter(c => [...c.querySelectorAll('.b')].some(b => b.textContent === 'transcript')).length);
    L.check('a "transcript" badge marks the talks that have one', badged > 0, `${badged}/20 cards`);

    await L.search(page, 'ai');
    const all = await L.resultCount(page);
    await page.click('#f-tr');
    await page.waitForTimeout(400);
    const only = await L.resultCount(page);
    const allBadged = await page.evaluate(() =>
      [...document.querySelectorAll('#results .card')]
        .every(c => [...c.querySelectorAll('.b')].some(b => b.textContent === 'transcript')));
    L.check('"Transcript only" filters the result set',
      only > 0 && only < all && allBadged, `ai=${all} -> transcript only=${only}`);
    L.check('the toggle shows its on state',
      await page.evaluate(() => document.querySelector('#f-tr').classList.contains('on')));
    L.check('the toggle round-trips through the URL',
      /tr=1/.test(await page.evaluate(() => location.hash)), await page.evaluate(() => location.hash));

    await page.click('#f-tr');
    await page.waitForTimeout(400);
    L.check('clicking again turns it off', (await L.resultCount(page)) === all);
    await page.click('#clear');
    await page.waitForTimeout(300);
    L.check('Reset clears it too',
      !(await page.evaluate(() => document.querySelector('#f-tr').classList.contains('on'))));
    await page.close();
  }

  // ---------- names, roles, keyboard ----------
  {
    const page = await L.newPage(browser);
    await L.boot(page);
    await L.search(page, 'kubernetes');

    const a = await page.evaluate(() => {
      // A placeholder is not an accessible name: it disappears once the field
      // has content, and several screen readers never announce it.
      const named = el => !!(el.getAttribute('aria-label') || el.getAttribute('title') ||
        (el.id && document.querySelector(`label[for="${el.id}"]`)) || el.closest('label'));
      const chip = document.querySelector('.b.tag');
      return {
        q: named(document.querySelector('#q')),
        selects: ['f-track', 'f-type', 'f-stage', 'f-sort']
          .map(id => ({ id, named: named(document.getElementById(id)) })),
        live: !!document.querySelector('[aria-live]'),
        chip: chip && { tag: chip.tagName, tabindex: chip.tabIndex },
        buttons: [...document.querySelectorAll('#more, #clear, .abs-more, #f-tr')]
          .every(b => b.tagName === 'BUTTON'),
        landmarks: !!document.querySelector('header') && !!document.querySelector('main') &&
                   !!document.querySelector('footer'),
        h1: document.querySelectorAll('h1').length,
        lang: document.documentElement.lang,
      };
    });
    L.check('landmarks are present and there is exactly one h1', a.landmarks && a.h1 === 1, `h1=${a.h1}`);
    L.check('the document declares its language', a.lang === 'en', a.lang);
    L.check('the controls are real buttons, not clickable divs', a.buttons);
    L.check('the search box has an accessible name', a.q, `named=${a.q}`);
    L.check('every filter has an accessible name',
      a.selects.every(s => s.named), JSON.stringify(a.selects));
    L.check('the result count is announced', a.live, `aria-live present=${a.live}`);
    L.check('tag chips are reachable by keyboard',
      a.chip && (a.chip.tag === 'BUTTON' || a.chip.tabindex >= 0), JSON.stringify(a.chip));

    await page.evaluate(() => document.querySelector('#q').focus());
    const order = [];
    for (let i = 0; i < 6; i++) {
      await page.keyboard.press('Tab');
      order.push(await page.evaluate(() => document.activeElement.id || document.activeElement.tagName));
    }
    L.check('Tab from the search box reaches the filters',
      order.join(',').includes('f-track'), order.join(' > '));
    L.check('the search box has a visible focus indicator',
      (await page.evaluate(() => {
        document.querySelector('#q').focus();
        return getComputedStyle(document.querySelector('#q')).boxShadow;
      })) !== 'none');

    // ---------- contrast ----------
    await page.locator('#results .card').first().locator('.mo-load').click();
    await page.waitForSelector('.mo', { timeout: 15000 });
    const c = await page.evaluate(() => {
      const g = (sel, p) => { const e = document.querySelector(sel); return e ? getComputedStyle(e)[p] : null; };
      return {
        body: g('body', 'backgroundColor'), card: g('.card', 'backgroundColor'),
        title: g('.card h2 a', 'color'), abs: g('.abs', 'color'),
        track: g('.b.track', 'color'), trackBg: g('.b.track', 'backgroundColor'),
        chip: g('.b:not(.track)', 'color'), chipBg: g('.b:not(.track)', 'backgroundColor'),
        mark: g('mark', 'color'), markBg: g('mark', 'backgroundColor'),
        ts: g('.mo a.ts', 'color'), tsBg: g('.mo a.ts', 'backgroundColor'),
        link: g('.links a', 'color'), status: g('.status', 'color'),
      };
    });
    const pairs = [
      ['card title', c.title, c.card, c.body],
      ['abstract', c.abs, c.card, c.body],
      ['track badge', c.track, c.trackBg, c.card],
      ['plain badge', c.chip, c.chipBg, c.card],
      ['highlighted match', c.mark, c.markBg, c.card],
      ['moment timestamp', c.ts, c.tsBg, c.card],
      ['card links', c.link, c.card, c.body],
      ['status line', c.status, c.body, c.body],
    ];
    for (const [name, fg, bg, base] of pairs) {
      const r = ratio(fg, bg, base);
      L.check(`contrast: ${name} meets WCAG AA (4.5:1)`, r >= 4.5, `${r.toFixed(2)}:1`);
    }
    await page.close();
  }
});
