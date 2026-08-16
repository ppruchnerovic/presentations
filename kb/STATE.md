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
| Browser UI (`index.html`) | Done. Tested headless: search, filters, sorting, foldable abstracts, moments, pagination, shareable URLs, both themes. Ranks on passages, not just whole transcripts. |
| Claude Code skill | Done — `conference-talks` in the `second-brain` repo. |
| Transcripts | Fetched via kome.ai with **estimated** timings. See below. |
| Scheduled refresh | `.github/workflows/kb-refresh.yml`, weekly, metadata only. |

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

**To upgrade to exact timings**, from a home connection:

```bash
cd kb/tools
rm -rf ../data/transcripts          # or just the ids you want redone
python3 fetch_transcripts.py --source youtube
python3 sync_agenda.py && python3 build_index.py
```

The script skips talks it already has, so an in-place rerun will *not* upgrade
anything — the delete is the point.

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
- Talks without a recording (135 of 493) are excluded by design; `--keep-all`
  overrides.

## Environment gotchas

- Headless Chromium cannot reach external HTTPS through this session's egress
  proxy — the TLS ClientHello is reset on every host, `example.com` included.
  It works fine against `localhost`, which is how the UI was tested
  (`python3 -m http.server` + Playwright).
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
one bag of words while `query.py` scores individual ~45s segments. A talk that
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
