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
kb/tools/query.py           ranked search: which talks to open
kb/tools/excerpt.py         the parts of those talks that bear on the question
```

**Always retrieve before answering. Never answer from memory** — you do not
know this conference's content, and inventing a speaker's position is the one
failure mode that makes this KB worthless.

Two commands, in this order. Every command runs from the repo root; the tools
resolve their own paths, so there is nothing to `cd` into.

## 1. `query.py --brief` — choose the talks

```bash
python3 kb/tools/query.py "spec driven development" -n 12 --brief
```

`--brief` gives you what choosing needs and nothing else: id, title, speakers,
track, duration, recording link, `has_transcript`, the abstract snippet and two
timestamped transcript moments. Add `--json` for the same fields machine-
readable. Plain `--json` returns the full record — tags, companies, stage, type,
`session_page` — and is worth the bytes only when the question is *about* those
fields.

Useful flags: `--track "AI Agents"`, `--type Keynote/Talk`, `--stage "Stage 1"`,
`-n 25`, `--no-moments`, `--ids`. (`--event` exists too, but this corpus holds
one event.) FTS5 syntax works: `"exact phrase"`, `OR`, `NOT`, `prefix*` — with
porter stemming, so `"quantum computing"` legitimately matches a passage saying
"quantum computers". Phrase search is stem-based, not literal.

**Cover the vocabulary inside one query, not across five.** A bare two-word
query ANDs its terms across unrelated talks: `agent security` ranks the
obviously on-topic talk ("The day the chatbot asked for sudo") only 6th, behind
generic security talks and generic agent talks. Put the domain's own words in
one `OR` and FTS5 ranks the union for you — a talk hitting several of the terms
rises by itself:

```bash
python3 kb/tools/query.py 'agent OR agents OR "prompt injection" OR guardrails OR identity OR "trust boundary"' -n 12 --brief
```

That puts the sudo talk 2nd and surrounds it with the neighbouring talks that
actually answer the question. Five separate searches unioned by hand find much
the same thing and are paid for five times.

`abstract_snippet` is `""` whenever the hit came from the transcript layer
only: the query did not match the abstract, **not** that the talk has none.
Every talk has one, and step 2 prints it.

## 2. `excerpt.py` — read what they actually say

```bash
python3 kb/tools/excerpt.py 913 844 628 -q "spec driven development"
```

Or pipe step 1 straight into it:

```bash
cd kb/tools && python3 query.py "agent memory" -n 6 --ids | xargs python3 excerpt.py -q "agent memory"
```

For each talk it prints the metadata, the full abstract, the **opening** — where
the speaker states what they are about to argue — and a window of speech either
side of each passage that matched, deep-linked to the second. Those passages are
ranked by the same bm25 that ranked the talk, restricted to that talk, so **what
you read is what put the talk in the results**. It closes with `499 of 4767
words (10%)`, so a thin excerpt is visible as one rather than mistaken for the
talk.

Flags: `-n` (how many windows' worth of speech, default 6), `--window` (seconds
either side of a hit, default 40), `--opening` (default 60, `0` for none),
`--full` (the whole transcript), `--json`. It accepts a talk id, a YouTube id or
URL, or a `kb/talks/**.md` path.

**Never `cat` a talk markdown file to find out what a speaker said.** Those
files inline the whole transcript — 28 KB, about 7,000 tokens each — and eight
of them is 60,000 tokens spent to use a few paragraphs. `excerpt.py` returns the
same eight for about 8,000. Measured over eight topics and 43 talks, 138 of 138
search-ranked moments land inside the excerpt, on 20% of the words. Reach for
`--full` or `cat` only when the user asks for a whole talk — a summary of one
specific session, a full walkthrough — and say that is what you are doing.

`cat` is still right for **lookups**: "what is talk 864 about", "who gave it",
"what's its recording link" are one `cat kb/talks/wwc-2026-berlin/864-*.md`,
or `excerpt.py 864 --opening 0` for the header and abstract alone.

## 3. Synthesize

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

## The budget

A one-sentence question is one search and a handful of excerpts — on the order
of **15k tokens, not 150k**. If a plan involves reading more than one or two
transcripts whole, it is the wrong plan; narrow the `-q` or raise `-n` on the
excerpt instead. There is no signal in a 28 KB file saying it cost 7,000 tokens
to learn one paragraph, so nothing but this section will tell you.

## Notes and limits

- **Every talk has an exact-timed transcript.** All 358 of them —
  `has_transcript = 1` throughout, `"timing": "exact"`, `"source": "yt"`,
  1,513,943 words over 53,982 indexed passages — so no answer here ever has to
  rest on an abstract alone. Word counts are the `transcript_words` column in
  `talks.db` and `word_count` in the transcript JSON; they are *not* `w`, which
  is a compact key in `kb/data/search-meta.json` that only the browser UI reads.
  Deep links land on a **passage boundary**, not on the word: captions are
  grouped into ~28-word passages and a passage keeps its first caption's start,
  so the phrase you searched is spoken 0–4 seconds *after* the timestamp and
  never before it. Link straight to it rather than hedging; `--json` carries the
  exact float (`"start": 1344.28`) if a consumer needs the precision. If a
  transcript ever turns up marked `"timing": "estimated"` — the kome.ai
  fallback, unused since the corpus was re-fetched — its starts are interpolated
  from word position, and only then should a timestamp be read as "around here".
- Two ids are in play. `talks.id` is this corpus's own integer — what `--ids`
  prints, what the markdown files are named after, what `excerpt.py` takes.
  `video_id` is YouTube's and is what the deep links carry. `excerpt.py` accepts
  either.
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
