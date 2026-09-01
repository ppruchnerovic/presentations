---
name: conference-talks
description: |
  Answer questions from the WeAreDevelopers conference talk knowledge base —
  358 recorded talks from World Congress 2026 Berlin with abstracts, speakers,
  track/type/stage tags, YouTube recordings and a full transcript for every
  talk. Use this whenever the user asks what was said at the conference, who
  talked about a topic, what different speakers think about something, which
  talks to watch on a subject, or asks to compare or synthesize positions
  across presenters — e.g. "how do people say to do AI-driven SDLC", "what did
  speakers say about agent security", "find me talks about spec-driven
  development", "who disagreed about vibe coding".
  Also use it to pull a specific talk's recording link, abstract or tags.
  Do NOT use it for talks outside the WeAreDevelopers corpus.
---

# WeAreDevelopers conference talk knowledge base

The corpus lives in this repo under `kb/`, and every path below is relative to
the repo root. If you are working from a different checkout, clone
`https://github.com/ppruchnerovic/presentations` and run the commands there.

```
kb/data/talks.json          canonical records (358 talks with recordings)
kb/data/transcripts/<id>.json   timestamped transcript segments, one per talk
kb/data/talks.db            SQLite FTS5 index — the thing you actually query
kb/talks/<event>/<id>-<slug>.md  one readable file per talk
kb/tools/query.py           ranked search over both layers
```

## How to answer

**Always retrieve before answering. Never answer from memory** — you do not
know this conference's content, and inventing a speaker's position is the one
failure mode that makes this KB worthless.

### 1. Retrieve

```bash
python3 kb/tools/query.py "spec driven development" -n 12 --json
```

Every command here runs from the repo root; the tools resolve their own paths,
so there is nothing to `cd` into.

`--json` gives you, per hit: `id`, title, speakers, companies, track, type,
stage, tags, `duration_min`, `recording_url`, `video_id`, `session_page`,
`has_transcript`, `abstract_snippet`, and `moments` — timestamped transcript
hits, each with an exact float `start`. `abstract_snippet` is `""` whenever the
hit came from the transcript layer only: that means the query did not match the
abstract, **not** that the talk has none. Every talk has an abstract; it lives
in the talk's markdown (step 2).

Useful flags: `--track "AI Agents"`, `--type Keynote/Talk`, `--stage "Stage 1"`,
`-n 25`, `--no-moments`. (`--event` exists too, but this corpus holds one
event.) FTS5 syntax works: `"exact phrase"`, `OR`, `NOT`, `prefix*` — with
porter stemming, so the phrase `"quantum computing"` legitimately matches a
passage saying "quantum computers". Phrase search is stem-based, not literal.

**Run several queries with different vocabulary rather than one.** This is the
highest-leverage habit here, and it rescues narrow questions as much as broad
ones — a bare two-word query ANDs its terms across unrelated talks. `agent
security` ranks the obviously on-topic talk ("The day the chatbot asked for
sudo") only 6th, behind generic security talks and generic agent talks. Asking
again in the domain's own vocabulary fixes it at once: `identity for agents`
puts that talk 1st and `prompt injection` puts it 3rd, while `guardrails` and
`agentic trust boundaries` surface the neighbouring talks that actually answer
the question. Fan out the same way on a broad question: for AI-driven SDLC try
`sdlc`, `spec driven development`, `coding agents workflow`,
`ai assisted delivery`, `verification`, `code review agents`. Union the results.

### 2. Read the full record

`query.py` ranks and snippets; it gives you neither the argument nor the full
abstract. Both live in the talk's markdown, and every file is named
`<id>-<slug>.md`, so an `id` from step 1 is one glob away:

```bash
cat kb/talks/wwc-2026-berlin/864-*.md          # abstract + speaker bio + transcript
```

**Go straight here for lookups.** "What is talk 864 about", "who gave it",
"what's its recording link", "read me the abstract" are all one `cat` — do not
try to answer them from search snippets. And for the talks that carry a
comparison question, read the file before you characterise anyone's position.

The markdown contains the whole transcript, chunked into ~45s paragraphs each
carrying a deep link into the video. That is where a speaker's actual position
lives — the abstract is marketing copy written months earlier.

### 3. Synthesize

For "what do different speakers think about X" questions, structure the answer
around **positions, not talks**:

- Group speakers who broadly agree; name the axis they disagree on.
- Attribute every claim to a named speaker and their company.
- Quote sparingly and only from transcripts, never from abstracts (an abstract
  is a promise, not a statement).
- Link each point to the recording, deep-linked to the timestamp when you have
  one: `https://www.youtube.com/watch?v=<video_id>&t=<seconds>s`.
- Say plainly when the corpus is thin: if only two talks touch the topic, the
  user needs to know the answer rests on a narrow base rather than a consensus.

Close with a short "worth watching" list — 3-5 talks, each with one line on why.

## Notes and limits

- **Every talk has an exact-timed transcript.** All 358 of them —
  `has_transcript = 1` throughout, `"timing": "exact"`, `"source": "yt"`,
  1,514,014 words over 53,988 indexed passages — so no answer here ever has to
  rest on an abstract alone. Word counts are the `transcript_words` column in
  `talks.db` and `word_count` in the transcript JSON; they are *not* `w`, which
  is a compact key in `kb/data/search-meta.json` that only the browser UI reads.
  Deep links land on a **passage boundary**, not on the word: captions are
  grouped into ~25-word passages and a passage keeps its first caption's start,
  so the phrase you searched is spoken 0–4 seconds *after* the timestamp and
  never before it. Link straight to it rather than hedging; `--json` carries the
  exact float (`"start": 1344.28`) if a consumer needs the precision. If a
  transcript ever turns up marked `"timing": "estimated"` — the kome.ai
  fallback, unused since the corpus was re-fetched — its starts are interpolated
  from word position, and only then should a timestamp be read as "around here".
- Rebuild after new transcripts land, **both steps and in this order**:
  `python3 kb/tools/sync_agenda.py` inlines the transcripts into
  `kb/talks/*.md`, then `python3 kb/tools/build_index.py` rebuilds `talks.db`
  and the browser index. `build_index.py` alone leaves the markdown stale.
- Refresh metadata from the conference API any time:
  `python3 kb/tools/sync_agenda.py` (public endpoint, no auth).
- Transcripts must be fetched from a normal network connection —
  `python3 kb/tools/fetch_transcripts.py`. YouTube blocks datacenter IPs, so
  this fails from CI and cloud containers.
- Non-technical colleagues can use the same corpus without installing anything
  at <https://ppruchnerovic.github.io/presentations/kb/> — the search UI
  supports shareable URLs, so you can hand someone a link to a live query.
- `kb/README.md` documents the layout and the rebuild steps; `kb/STATE.md` is
  the build log. Read STATE.md before changing anything under `kb/tools/`.
