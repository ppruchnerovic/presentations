---
name: conference-talks
description: |
  Answer questions from the WeAreDevelopers conference talk knowledge base —
  358 recorded talks from World Congress 2026 Berlin with abstracts, speakers,
  track/type/stage tags, YouTube recordings and (where fetched) full
  transcripts. Use this whenever the user asks what was said at the
  conference, who talked about a topic, what different speakers think about
  something, which talks to watch on a subject, or asks to compare or
  synthesize positions across presenters — e.g. "how do people say to do
  AI-driven SDLC", "what did speakers say about agent security", "find me
  talks about spec-driven development", "who disagreed about vibe coding".
  Also use it to pull a specific talk's recording link, abstract or tags.
  Do NOT use it for talks outside the WeAreDevelopers corpus.
---

# WeAreDevelopers conference talk knowledge base

The corpus lives in this repo under `kb/`, and every path below is relative to
the repo root. If you are working from a different checkout, clone
`https://github.com/ppruchnerovic/presentations` and run the commands there.

```
kb/data/talks.json          canonical records (358 talks with recordings)
kb/data/transcripts/<id>.json   timestamped transcript segments, when fetched
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
cd kb/tools
python3 query.py "spec driven development" -n 12 --json
```

`--json` gives you, per hit: title, speakers, companies, track, type, stage,
tags, duration, `recording_url`, `session_page`, an abstract snippet, and
`moments` — timestamped transcript hits with the exact seconds.

Useful flags: `--track "AI Agents"`, `--type Keynote/Talk`, `-n 25`,
`--no-moments`. FTS5 syntax works: `"exact phrase"`, `OR`, `NOT`, `prefix*`.

For a broad question, **run several queries with different vocabulary** rather
than one. People say the same thing many ways — for AI-driven SDLC try
`sdlc`, `spec driven development`, `coding agents workflow`,
`ai assisted delivery`, `verification`, `code review agents`. Union the results.

### 2. Read the strong hits

`query.py` ranks and snippets; it does not give you the argument. For the
talks that matter, read the full record:

```bash
cat kb/talks/wwc-2026-berlin/591-*.md          # abstract + speaker bio + transcript
```

When a talk has a transcript, the markdown contains it, chunked into ~45s
paragraphs each carrying a deep link into the video. That is where a speaker's
actual position lives — the abstract is marketing copy written months earlier.

### 3. Synthesize

For "what do different speakers think about X" questions, structure the answer
around **positions, not talks**:

- Group speakers who broadly agree; name the axis they disagree on.
- Attribute every claim to a named speaker and their company.
- Quote sparingly and only from transcripts, never from abstracts (an abstract
  is a promise, not a statement).
- Link each point to the recording, deep-linked to the timestamp when you have
  one: `https://www.youtube.com/watch?v=<video_id>&t=<seconds>s`.
- Say plainly when the corpus is thin: if only two talks touch the topic, or if
  none of the matching talks have transcripts, the user needs to know the
  answer rests on abstracts alone.

Close with a short "worth watching" list — 3-5 talks, each with one line on why.

## Notes and limits

- **Transcript coverage may be partial.** Check `has_transcript` / the `w` word
  count. A talk without a transcript can only be described from its abstract —
  say so rather than implying you know what was said.
- **Timestamps may be approximate.** Each transcript records `timing`: `exact`
  (real caption timings) or `estimated` (fetched via kome.ai, which returns
  untimed text, so starts are interpolated from word position). When linking to
  an estimated timestamp, point slightly early and treat it as "around here"
  rather than an exact cue. The transcript *text* is verbatim either way.
- Rebuild the index after new transcripts land:
  `python3 kb/tools/build_index.py`.
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
