// The controls the script shows and hides as state changes: pagination, the
// abstract unfold, tag chips and the keyboard shortcut.
//
// The first two checks are a regression guard. `#more` and `.abs-more` are
// hidden by setting the `hidden` property, and an author rule that sets
// `display` on either of them outranks the UA stylesheet's [hidden] — which
// silently turns both into permanent fixtures. That shipped once: a four-hit
// search offered "Show more (-16 left)".

const L = require('./lib');

const visibility = sel => `(() => {
  const b = document.querySelector('${sel}');
  return b && { hiddenAttr: b.hidden, display: getComputedStyle(b).display,
                visible: b.offsetParent !== null, text: b.textContent };
})()`;

L.suite('controls', async browser => {
  const page = await L.newPage(browser);
  await L.boot(page);

  // ---------- "Show more" hides when there is nothing more ----------
  await L.search(page, 'zzzqqqxyzzy');
  const onEmpty = await page.evaluate(visibility('#more'));
  L.check('"Show more" is hidden on an empty result set', !onEmpty.visible,
    `hidden=${onEmpty.hiddenAttr} display=${onEmpty.display} text="${onEmpty.text}"`);

  await L.search(page, 'gpt-4');
  const oneShort = await page.evaluate(visibility('#more'));
  L.check('"Show more" is hidden when every hit already fits on one page',
    !oneShort.visible,
    `${await L.cardCount(page)} cards, hidden=${oneShort.hiddenAttr} display=${oneShort.display}`);

  // ---------- the unfold appears only where text is truncated ----------
  await L.search(page, '');
  await page.evaluate(() => { for (let i = 0; i < 8; i++) document.querySelector('#more').click(); });
  await page.waitForTimeout(400);
  const abs = await page.evaluate(() => {
    const rows = [...document.querySelectorAll('#results .card')].map(c => {
      const p = c.querySelector('.abs'), b = c.querySelector('.abs-more');
      if (!p || !b) return null;
      return { overflows: p.scrollHeight > p.clientHeight + 2, visible: b.offsetParent !== null };
    }).filter(Boolean);
    return { total: rows.length, short: rows.filter(r => !r.overflows).length,
             wrong: rows.filter(r => !r.overflows && r.visible).length };
  });
  L.check('the unfold button appears only where the clamp actually hides something',
    abs.wrong === 0, `${abs.wrong} wrong of ${abs.short} untruncated / ${abs.total} cards`);
  L.check('the corpus contains untruncated abstracts, so that check means something',
    abs.short > 0, `${abs.short} of ${abs.total}`);

  // ---------- pagination ----------
  await L.search(page, 'ai');
  const total = await L.resultCount(page);
  L.check('the first page is 20 cards', (await L.cardCount(page)) === 20);
  L.check('the button reports how many are left',
    (await page.textContent('#more')) === `Show more (${total - 20} left)`,
    await page.textContent('#more'));
  await page.click('#more');
  await page.waitForTimeout(250);
  L.check('a click adds another 20', (await L.cardCount(page)) === 40);
  await page.click('#more');
  await page.waitForTimeout(250);
  L.check('and again', (await L.cardCount(page)) === 60);
  await L.search(page, 'rust');
  L.check('a new query resets to the first page', (await L.cardCount(page)) <= 20,
    `${await L.cardCount(page)} cards`);

  // ---------- abstract unfold ----------
  await L.search(page, 'kubernetes');
  const card = page.locator('#results .card').filter({ has: page.locator('.abs-more') }).first();
  const read = () => card.evaluate(c => ({
    h: c.querySelector('.abs').clientHeight,
    clamped: c.querySelector('.abs').classList.contains('clamped'),
    label: c.querySelector('.abs-more').textContent,
  }));
  const before = await read();
  await card.locator('.abs-more').click();
  await page.waitForTimeout(200);
  const opened = await read();
  L.check('unfolding expands the paragraph and relabels the button',
    !opened.clamped && opened.label === 'Show less' && opened.h >= before.h,
    `${before.h}px "${before.label}" -> ${opened.h}px "${opened.label}"`);
  await card.locator('.abs-more').click();
  await page.waitForTimeout(200);
  const closed = await read();
  L.check('folding restores the clamp and the label',
    closed.clamped && closed.label === 'Show full description', JSON.stringify(closed));

  // ---------- tag chips ----------
  await L.search(page, 'kubernetes');
  await page.evaluate(() => window.scrollTo(0, 600));
  const chip = page.locator('#results .b.tag').first();
  const tagVal = await chip.getAttribute('data-tag');
  const tagText = await chip.textContent();
  await chip.click();
  await page.waitForTimeout(500);
  L.check('clicking a tag chip searches for it',
    (await page.inputValue('#q')) === tagVal, `"${tagText}" -> q="${await page.inputValue('#q')}"`);
  L.check('the tag search returns something', (await L.cardCount(page)) > 0);
  L.check('the page scrolls back to the top', (await page.evaluate(() => window.scrollY)) < 50);

  // ---------- keyboard ----------
  await page.evaluate(() => document.querySelector('#q').blur());
  await page.keyboard.press('/');
  await page.waitForTimeout(120);
  const focus = await page.evaluate(() => document.activeElement.id);
  L.check('"/" focuses the search box without typing a slash',
    focus === 'q' && !(await page.inputValue('#q')).includes('/'), `focus=${focus}`);
  // Once the box has focus the shortcut must get out of the way and let the
  // slash through. Where it lands depends on the caret, which is not the point.
  const v = await page.inputValue('#q');
  await page.keyboard.press('/');
  await page.waitForTimeout(100);
  const typed = await page.inputValue('#q');
  L.check('"/" types normally once the box already has focus',
    typed.length === v.length + 1 && typed.includes('/'), `"${v}" -> "${typed}"`);

  L.check('no uncaught errors', page.__errors.length === 0, page.__errors.join('; '));
});
