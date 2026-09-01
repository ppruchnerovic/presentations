// Every search option the UI offers: free text over each indexed field, the
// transcript layer, quoted phrases, prefixes, and the tokenising rules that
// keep a search for "rust" out of every talk that says "trust".

const L = require('./lib');

L.suite('search', async browser => {
  const page = await L.newPage(browser);
  await L.boot(page);
  const meta = await L.meta(page);
  const N = meta.talks.length;
  const count = q => L.search(page, q).then(() => L.resultCount(page));

  // ---------- one term ----------
  await L.search(page, 'kubernetes');
  const st = (await L.statusText(page)).trim();
  const n = await L.resultCount(page);
  L.check('a single term returns a bounded result set', n > 0 && n < N, st);
  L.check('the status line echoes the query', st.includes('matching') && st.includes('kubernetes'), st);
  const tops = await L.titles(page);
  L.check('the top hits are on topic', /kubernetes|k8s/i.test(tops.slice(0, 3).join(' | ')), tops[0]);

  const marks = await page.$$eval('#results mark', ms => ms.map(m => m.textContent.toLowerCase()));
  L.check('matched terms are highlighted',
    marks.length > 0 && marks.every(m => m.startsWith('kub')), [...new Set(marks)].slice(0, 5).join(','));

  // ---------- several terms are ANDed ----------
  const nAgents = await count('agents');
  const nSecurity = await count('security');
  const nBoth = await count('agents security');
  L.check('a multi-term query is AND, not OR',
    nBoth <= Math.min(nAgents, nSecurity) && nBoth > 0,
    `agents=${nAgents} security=${nSecurity} both=${nBoth}`);

  const idsA = await L.cardIds(page);
  await L.search(page, 'security agents');
  L.check('term order does not change the ranking',
    JSON.stringify(idsA) === JSON.stringify(await L.cardIds(page)), `${idsA.length} cards`);

  await L.search(page, 'ai ai ai');
  const dup = await L.resultCount(page);
  L.check('repeated terms are de-duplicated', dup === await count('ai'), `${dup}`);

  // ---------- tokens, not substrings ----------
  await L.search(page, 'rust');
  const rustMarks = await page.$$eval('#results mark', ms => [...new Set(ms.map(m => m.textContent.toLowerCase()))]);
  L.check('"rust" is never highlighted inside "trust"',
    !rustMarks.some(m => m.startsWith('trust')), rustMarks.join(','));
  L.check('"rust" still finds the Rust talks', /rust/i.test((await L.titles(page)).join(' ')),
    (await L.titles(page))[0]);

  // ---------- prefixes ----------
  const nAgentic = await count('agentic');
  L.check('a prefix search widens the result set ("agent" also finds "agentic")',
    nAgents >= nAgentic && nAgentic > 0, `agents=${nAgents} agentic=${nAgentic}`);
  await L.search(page, 'agent');
  const agentMarks = await page.$$eval('#results mark', ms => [...new Set(ms.map(m => m.textContent.toLowerCase()))]);
  L.check('a prefix hit is highlighted at the stem',
    agentMarks.every(m => m.startsWith('agent')), agentMarks.join(','));

  // ---------- quoted phrase ----------
  await L.search(page, '"code review"');
  const phraseN = await L.resultCount(page);
  const topId = (await L.cardIds(page))[0];
  const top = meta.talks.find(t => t.i === topId);
  const hay = [top.t, top.d, (top.a || []).join(' ')].join(' ').toLowerCase();
  L.check('a quoted phrase returns results', phraseN > 0, `${phraseN} hits, top: ${top.t}`);
  L.check('the phrase bonus puts an exact-phrase talk first', hay.includes('code review'), top.t);
  L.check('quoting never widens the result set', phraseN <= await count('code review'), `${phraseN}`);

  // ---------- each indexed field ----------
  const speaker = meta.talks.find(t => (t.s || []).length && t.s[0].split(' ').length >= 2).s[0];
  await L.search(page, speaker);
  const who = await page.$$eval('#results .who', ws => ws.map(w => w.textContent.toLowerCase()));
  L.check(`a speaker name ("${speaker}") finds their talk`,
    who.some(w => w.includes(speaker.split(' ')[0].toLowerCase())), who[0]);

  const company = meta.talks.find(t => (t.c || []).length && t.c[0].trim()).c[0];
  await L.search(page, company);
  const co = await page.$$eval('#results .who', ws => ws.map(w => w.textContent.toLowerCase()));
  L.check(`a company ("${company}") finds its talks`,
    co.some(w => w.includes(company.toLowerCase().split(' ')[0])), co[0]);

  const tag = meta.talks.find(t => (t.a || []).length).a[0];
  L.check(`a tag ("${tag}") returns hits`, await count(tag) > 0);

  const track = [...new Set(meta.talks.map(t => t.k).filter(Boolean))][0];
  L.check(`a track name ("${track}") returns hits`, await count(track) > 0);

  // ---------- the transcript layer ----------
  let spoken = null;
  for (const q of ['nginx', 'kafka', 'postgres', 'monolith', 'burnout']) {
    await L.search(page, q);
    const s = (await L.statusText(page)).trim();
    if (/found only in the spoken transcript/.test(s)) { spoken = `${q} -> ${s}`; break; }
  }
  L.check('talks matched only by what was said are counted separately', !!spoken,
    spoken || 'no sampled query surfaced a transcript-only hit');

  // A word said once, in one talk, is the sharpest search key there is — the
  // index used to prune every such term, and the AND across query terms then
  // turned the search into "Nothing matched". The word is chosen offline to be
  // a transcript singleton that no title, abstract or tag starts with.
  await L.search(page, 'torvalds');
  const single = await L.cardIds(page);
  L.check('a word spoken once in the whole corpus finds exactly that talk',
    single.length === 1 && single[0] === 586, `ids=[${single.join(',')}]`);

  // ---------- compounds and punctuation ----------
  await L.search(page, 'spec driven development');
  L.check('"spec driven" matches the hyphenated "spec-driven"',
    /spec[- ]driven/i.test((await L.titles(page)).join(' | ')), (await L.titles(page))[0] || '(none)');

  for (const q of ['.net', 'c#', 'ci/cd', 'gpt-4']) {
    await L.search(page, q);
    L.check(`a punctuation-bearing query ("${q}") resolves`, page.__errors.length === 0,
      (await L.statusText(page)).trim().slice(0, 55) || 'empty state');
  }

  // ---------- queries that match nothing, or everything ----------
  await L.search(page, 'zzzqqqxyzzy');
  L.check('a nonsense query shows the empty state',
    (await page.locator('.empty h3').textContent().catch(() => null)) === 'Nothing matched');

  await L.search(page, 'the and of');
  L.check('a stopword-only query falls back to browsing the catalogue',
    (await L.resultCount(page)) === N, `${await L.resultCount(page)} vs ${N}`);

  await L.search(page, '   ');
  L.check('a whitespace-only query resets to browsing', (await L.resultCount(page)) === N);

  await L.search(page, '""');
  L.check('bare quotes do not throw', page.__errors.length === 0, page.__errors.join(';'));

  // ---------- input handling ----------
  const lower = await count('kubernetes');
  L.check('the query is case- and whitespace-insensitive',
    lower === await count('KUBERNETES') && lower === await count('  Kubernetes  '), `${lower}`);

  await page.fill('#q', '');
  await page.type('#q', 'kubernetes', { delay: 20 });
  await page.waitForTimeout(700);
  L.check('typing settles on the same result as pasting (no lost race)',
    (await L.resultCount(page)) === lower, `${await L.resultCount(page)} vs ${lower}`);

  // The native ✕ on a type=search input fires `input` with an empty value.
  await page.evaluate(() => {
    const q = document.querySelector('#q');
    q.value = '';
    q.dispatchEvent(new Event('input', { bubbles: true }));
  });
  await page.waitForTimeout(400);
  L.check('the field\'s native ✕ clears the search', (await L.resultCount(page)) === N);

  L.check('no uncaught errors across the suite', page.__errors.length === 0, page.__errors.join('; '));
  L.check('no failed requests', page.__requests.length === 0, page.__requests.slice(0, 3).join('; '));
});
