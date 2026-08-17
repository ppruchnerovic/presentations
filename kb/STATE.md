# Build state and handoff notes

Working notes for whoever (or whichever session) picks this up next. The
user-facing documentation is `README.md`; this file records decisions, dead
ends and what is left.

## Where things stand

| Piece | State |
|---|---|
| Metadata pipeline (`sync_agenda.py`) | Done. 358 talks with recordings, from the public API. |
| Per-talk markdown | Done. Regenerated from `talks.json` on every sync. |
| Search indexes (`build_index.py`) | Done. SQLite FTS5 + sharded browser index. |
| CLI (`query.py`) | Done. Auto-builds the index on first use. |
| Browser UI (`index.html`) | Done. Ranks on passages, not just whole transcripts. Shares the site's dark palette and type — see below. |
| Browser UI tests (`tools/uitest/`) | Done. ~165 checks over search, filters, sorting, abstracts, moments, pagination, shareable URLs, resilience and a11y. `node run.js`. |
| Claude Code skill | Done — `conference-talks`, in this repo at `.claude/skills/conference-talks/`. Moved here from `second-brain` so the skill ships with the corpus it queries. |
| Transcripts | All 358 fetched with **exact** timings via `youtube-transcript-api`. See below. |
| Scheduled refresh | `.github/workflows/kb-refresh.yml`, weekly, metadata only. |

## Visual design — shared with the rest of the site

`index.html` deliberately carries the same tokens as `../index.html` and
`../posts/*/index.html`. Keep them in sync if any page changes; the explorer is
meant to read as part of the site, not as a separate tool bolted on.

```
--bg #0f1115   --card #181b22   --accent #e8b64c
--text #e6e6e6 --muted #9aa3b2  --border #262b36
```

System font stack, `line-height: 1.6`, 860px column, 12px card radius, pill
(`999px`) chips and buttons, gradient header (`135deg, #14161c → #1d2027`) with
an uppercase gold kicker, and gold uppercase section labels.

Two notes on where the explorer needs more than the recap pages have:

- **Dark only.** The recaps have no light mode, so the explorer dropped its
  `prefers-color-scheme` block rather than being the one page that flips.
  `<meta name="color-scheme" content="dark">` keeps the native form controls
  dark too.
- **The status line is not uppercased**, unlike the recap `.meta` lines it
  otherwise resembles. It echoes back the visitor's own query, and their text
  is not ours to restyle.

All foreground/background pairs introduced here clear WCAG AA (lowest is the
badge text at 6.1:1).

## Transcript routes — what works from where

This cost real time to establish, so it is written down.

| Route | Result from a cloud container | Timings |
|---|---|---|
| `youtube-transcript-api` | blocked — `IpBlocked` | exact |
| `yt-dlp` caption download | blocked — "Sign in to confirm you're not a bot" | exact |
| YouTube `timedtext` endpoint | blocked — HTTP 429 | exact |
| YouTube Innertube `/player` | blocked — `LOGIN_REQUIRED` | exact |
| YouTube watch page scrape | blocked — 302 to `google.com/sorry` | exact |
| YouTube **oEmbed** | **works** — title/channel/thumbnail only | n/a |
| **kome.ai** `POST /api/transcript` | **works** — full text, server-side fetch | none (interpolated) |

The kome.ai route was borrowed from the existing `youtube-community-post` skill
in `second-brain`, which had already solved this. Its docstring also records
routes that do *not* work from a sandbox: tactiq.io (needs a Firebase App Check
token), notegpt.io (needs login), youtubetotranscript.com (Cloudflare JS
challenge).

Because kome.ai returns untimed text, `fetch_transcripts.py` interpolates each
segment's start from its word position across the runtime and marks the
transcript `"timing": "estimated"`. Text is verbatim; only the offsets are
approximate — expect to land within a sentence or two of a quote.

The corpus has since been re-fetched end to end from ordinary connections, so
every transcript now carries `"timing": "exact"` and `"source": "yt"`. kome.ai
stays in the script as the fallback for anything that must run where YouTube is
blocked.

### The limit is a per-IP quota, not a rate limit

This is the part that cost a day, so it is written down.

| Egress | Fetched before the block |
|---|---|
| Corporate NAT (Zscaler) | 235, then 52 in a later sitting |
| Residential ISP | 25 |
| Mobile carrier | 22 |

Slowing down does not help. The 235-talk run used four *unpaced* workers
(~40 req/min); a later run at two paced workers (~24 req/min) stopped at 25.
What is metered is an allowance per egress IP that refills over hours, and both
exact routes draw on the same one — yt-dlp is a fallback for a *refusal*, not
for an exhausted quota.

Corporate NAT addresses front many users and carry a correspondingly larger
allowance, which is the one case where a datacenter-ish IP does better, provided
it is not already flagged. Recovery is slow and uneven: a carrier IP was still
blocked after ~2.5 hours, while the corporate one came back in about two.

Hence `--retry-after MINUTES`, which parks the run and resumes where it stopped;
each round re-derives its work from disk, so a blocked round costs only time.
A block is **not** written to `_misses.json` — that file means "this video has
no captions". Keeping the two apart is what lets a plain rerun collect
everything a block skipped.

Probe before restarting a parked run; one request is enough to tell whether the
current network is worth spending a round on.

### The official API is a dead end

Do not reach for the YouTube Data API. `captions.download` requires OAuth *and*
permission to edit the video, so third-party talks return 403; and at 200 quota
units against a 10,000/day default it would cap at 50 transcripts a day even if
permission existed. The `timedtext` endpoint these routes use is undocumented,
so there is no published limit to tune against and no quota-extension form that
applies to it.

**To re-fetch specific talks**, delete them first — the script skips talks it
already has, so the delete is the point:

```bash
cd kb/tools
rm -rf ../data/transcripts          # or just the ids you want redone
python3 fetch_transcripts.py --source exact --retry-after 20
python3 sync_agenda.py && python3 build_index.py
```

## Design decisions worth not relitigating

- **One shared corpus, event as a field** rather than a directory per
  conference, so a query can compare across years. Add event ids to `EVENTS` in
  `wadkb.py`.
- **`talks.db` is gitignored.** It is derived, rebuilds in seconds, and would
  otherwise push megabytes of churning binary into every weekly commit.
  `search-meta.json` and `tindex/` *are* committed — GitHub Pages can only serve
  files that exist in the repo.
- **`talks_fts` stores its content** (it is not a contentless FTS5 table) so
  `snippet()` works. Transcript text lives in `segments`, indexed through an
  external-content FTS5 table, which is what makes timestamped hits possible.
- **Ranking**: two bugs found by testing, do not reintroduce them.
  Without IDF weighting, "ai driven sdlc" ranked a generic AI talk first because
  "ai" counted as much as "sdlc". With raw substring matching, "rust" matched 57
  talks, most of them containing only the word "t*rust*". The browser index now
  matches on tokens with prefix support, and compound tokens like "spec-driven"
  are also indexed as their parts.
  The substring bug had in fact survived in two places the index fix did not
  reach — `showMoments()` scored segments with `text.includes(term)` and
  `highlight()` marked matches with an unanchored regex, so a search for "rust"
  offered up moments about *t*rust and highlighted them. Both now go through
  `tokenize()` / `\b`-anchored matching. If you touch either, keep them on
  tokens.
- **Passage positions in the browser index.** Each posting is
  `[talk_id, term_freq, segments]`, where `segments` is the base36 gap-encoded
  list of segments the term falls in (`"2f.1.4"` -> 87, 88, 92). This is what
  lets `index.html` reward talks that say the query terms *inside one passage*,
  the way `query.py` does by scoring segments — see below. Coarser buckets were
  measured and rejected: separating on-topic talks from bag-of-words noise
  scored 58 points with exact segments, 48 with 64 buckets, and 2 with 4. The
  positions cost 1.7 MB raw / ~90 KB gzipped per shard, and shards are still
  fetched lazily, one letter at a time.
  Existing `f`/`p` values are untouched by the change, so a stale `index.html`
  keeps working against a fresh index — it just ignores the third element.
- **`sync_agenda.py` refuses to shrink the corpus by more than 10%.** The
  refresh workflow runs unattended: it commits whatever the pipeline produces
  and force pushes it to `gh-pages`. A 200 from the agenda API is not the same
  as a good answer — the conference is over, so sessions can lose
  `recording_url` at any time, and every talk without one is silently skipped.
  Measured on a scratch copy: stripping `recording_url` yields 0 talks, deletes
  all 358 markdown files (`main()` rmtrees `kb/talks/` and rebuilds it) and
  empties the index, and *nothing exits non-zero* — the workflow would have
  published it. Transcripts are never at risk (nothing outside
  `fetch_transcripts.py` writes to `data/transcripts/`), so a revert restores
  everything, but only after the live search has served an empty corpus.
  `--allow-shrink` is the escape hatch when a drop is real.
- **Passages are cut at index time, not by whoever fetched the transcript.**
  `build_index.py` groups consecutive captions into ~28-word passages
  (`PASSAGE_WORDS`) before indexing; each keeps its first caption's start.
  Both rankers make a segment the unit that two query terms must share, so
  segment size silently decides what counts as "said together". kome.ai
  returned ~27-word chunks; YouTube's captions arrive as ~6-word lines, which
  quietly broke that contract — "spec driven development" is spoken across
  three caption lines and so matched none of them, and `query.py` went from
  8 hits to 6. Re-grouping restored the CLI's pre-upgrade ranking exactly on
  three of five sampled queries and as a set on the fourth. Do not remove this
  in favour of raw captions: it is what keeps ranking independent of the fetch
  route. Deep links are unaffected — the browser reads
  `data/transcripts/<id>.json` directly, so a moment still points at the
  caption, not at the start of its passage.
- **Hiding a control needs more than `hidden`.** `index.html` hides `#more`,
  `.abs-more` and `#f-tr` by setting the `hidden` property, but any author rule
  that sets `display` on one of them outranks the UA stylesheet's `[hidden]` —
  so the element stays on screen while the script believes it is gone. This
  shipped: a four-hit search offered "Show more (-16 left)", and a fifth of the
  cards offered to unfold an abstract that was already complete. A
  `[hidden] { display: none !important; }` reset now covers all three, and
  `uitest/suite-controls.js` guards it. If you add a control the script hides,
  you get this for free — but do not remove the reset.
- Talks without a recording (135 of 493) are excluded by design; `--keep-all`
  overrides.

## Environment gotchas

- Headless Chromium cannot reach external HTTPS through this session's egress
  proxy — the TLS ClientHello is reset on every host, `example.com` included.
  It works fine against `localhost`, which is what `tools/uitest/run.js` does —
  it serves the repo on a free port and points Playwright at that. Passing
  `KB_URL` to test a deployed copy therefore only works off this proxy.
- The conference API is unauthenticated but slow: ~2.3 MB, give it a long
  timeout.

## Not done

- No semantic/vector search. The abstracts total ~75k tokens and transcripts
  ~2.5M; BM25 plus an agent reading the top hits has covered the query patterns
  so far. If "find talks that mean X without saying X" becomes a real need,
  embeddings over the transcript chunks are the next step — the chunking in
  `segments` is already the right granularity.
Previously listed here and now done: the static site ranked whole talks by
transcript relevance worse than the CLI, because it scored each transcript as
one bag of words while `query.py` scores individual ~28-word passages. A talk that
said "development" throughout and "spec" once in an unrelated aside scored as
well as one arguing about spec-driven development. `index.html` now reads the
segment positions described above and applies a saturating co-occurrence bonus
(`PASSAGE_W`/`NEAR_W`, mirroring `W_SEG` in `query.py`).

Measured in headless Chromium over 15 queries, counting only the queries where
some talk *does* put all the terms in one passage: the top 10 captured 48% of
those talks before and 71% after. No query got worse. The bonus only ever
promotes — about a fifth of the talks `query.py` ranks well never put the terms
in a single segment, so treating missing co-occurrence as disqualifying would
have cost recall.

The two rankers still disagree on ordering, and that is expected rather than a
defect: `talks.db` tokenizes with Porter stemming, the browser matches on token
prefixes, and their field weights differ. Overlap of the top 10 is around 40%.
Use the CLI when you want `query.py`'s exact semantics; the site is now a fair
tool for precision work rather than a rough one.
