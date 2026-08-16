# Conference talk knowledge base

Every recorded talk from the WeAreDevelopers World Congress, with abstracts,
speakers, track / type / stage tags, recording links and — once fetched — full
searchable transcripts.

**Browse it here: <https://ppruchnerovic.github.io/presentations/kb/>**
(no install, works on a phone, and the URL carries the search so you can send
someone a link straight to a query).

## Where the data comes from

The agenda app at `app.wearedevelopers.com` gates its agenda route behind login
plus a linked ticket, but the data it renders comes from one public endpoint
that needs no authentication:

```
https://wad-api.wearedevelopers.com/api/v2/events/16
```

One response carries every session, the track / stage / session-type lookup
tables, the speaker roster with bios, and the YouTube recording links.
Transcripts come separately, from YouTube's caption tracks.

## Layout

```
kb/
├── index.html                    zero-install search UI (GitHub Pages)
├── data/
│   ├── talks.json                canonical corpus — the source of truth
│   ├── talks.csv                 same thing for spreadsheets
│   ├── transcripts/<id>.json     timestamped segments, one file per talk
│   ├── talks.db                  SQLite + FTS5, used by query.py
│   ├── search-meta.json          compact metadata the browser loads up front
│   └── tindex/                   transcript inverted index, sharded, lazy-loaded
│                                 postings carry segment positions, so the browser
│                                 can rank passages, not just whole transcripts
├── talks/<event>/<id>-<slug>.md  one readable file per talk
└── tools/
    ├── wadkb.py                  shared helpers
    ├── sync_agenda.py            conference API  -> talks.json + markdown
    ├── fetch_transcripts.py      YouTube captions -> transcripts/   (run locally)
    ├── build_index.py            everything      -> talks.db + browser index
    ├── query.py                  ranked search from the terminal
    └── uitest/                   browser tests for index.html
```

### Why three representations

They serve different readers and cost almost nothing to keep in sync, since all
three are generated from the same run.

| Artifact | For | Why not the others |
|---|---|---|
| `talks.json` / `.csv` | scripts, spreadsheets, any future tool | exact, complete, no parsing of prose |
| `talks/**.md` | humans, `grep`, Claude Code | git-diffable per talk; a coding agent can read one file and have the whole talk |
| `talks.db` + `tindex/` | ranked search | generated; delete them any time and rebuild |

## Searching

### In a browser (anyone, nothing to install)

<https://ppruchnerovic.github.io/presentations/kb/> — type a topic, filter by
track / type / stage, sort by relevance / schedule / title, and click
**Find this in the talk** to jump to the exact seconds where a phrase is
spoken. That link only appears once you have searched for something, since
what it finds are the moments matching your query; clicking it again hides
them.

Abstracts are shown in full. Anything longer than four lines gets a **Show
full description** toggle rather than being cut off mid-sentence.

The **Transcript only** filter shows itself only when transcript coverage is
partial. All 358 talks currently have one, so it stays hidden — a filter that
matches everything is just a dead control.

Multi-word searches rank talks that say the words *together*, in one passage,
above talks that merely say each of them somewhere — so "spec driven
development" finds the talks arguing about it, not every talk that says
"development" a lot.

### From the terminal

```bash
cd kb/tools
python3 query.py "ai driven sdlc"
python3 query.py "spec driven development" -n 20
python3 query.py "agents" --track "AI Agents" --type Keynote/Talk
python3 query.py "code review" --json          # for scripts and agents
```

Both the abstracts and the transcripts are searched. Transcript hits carry the
timestamp, so results deep-link into the video. FTS5 syntax works:
`"exact phrase"`, `OR`, `NOT`, `prefix*`.

### With Claude Code

The `conference-talks` skill (`.claude/skills/conference-talks/`, at the root of
this repo, so any Claude Code session started here loads it) drives `query.py`
and then reads the matching talk files, which is what you want for questions like
*"what do different speakers think about AI-driven SDLC"* — retrieval finds the
talks, the model compares the positions.

## Rebuilding

```bash
cd kb/tools
python3 sync_agenda.py        # refresh metadata from the conference API
python3 fetch_transcripts.py  # ON YOUR OWN MACHINE — see below
python3 build_index.py        # rebuild both search indexes
```

`sync_agenda.py` and `build_index.py` are idempotent — rerunning gives byte-identical
output, so a git diff shows exactly what the conference changed.

### Transcripts, and the timing caveat

`fetch_transcripts.py` tries two routes:

| Route | Timing | Works from |
|---|---|---|
| `youtube-transcript-api` | **exact** — deep links land on the second | only un-flagged IPs, in practice a home connection |
| `kome.ai` | **estimated** — interpolated from word position | anywhere, including CI and cloud containers |

YouTube blocks datacenter IP ranges (`429` / *"Sign in to confirm you're not a
bot"*), so anything running in the cloud falls back to kome.ai. Estimated starts
land you *near* a quote — good enough to find the passage, off by roughly a
sentence or two. Every transcript records which it is in its `timing` field.

```bash
pip install youtube-transcript-api
cd kb/tools && python3 fetch_transcripts.py
```

It is resumable — stop it with Ctrl-C and rerun. Talks whose video has no
captions are recorded in `data/transcripts/_misses.json` so they are not retried
forever; `--retry-misses` forces another attempt. Then rerun `sync_agenda.py`
(to inline transcripts into the markdown) and `build_index.py`, and commit.

**To upgrade estimated timings to exact ones**, delete the transcripts you want
redone and rerun from a home connection — the script skips talks it already has,
so it will not re-fetch them otherwise.

The `Refresh talk metadata` workflow keeps the metadata current automatically;
it deliberately does not attempt transcripts.

## Testing the browser UI

`index.html` is one self-contained file with no build step, which makes it easy
to change and easy to break quietly — a search that silently stops matching
looks exactly like a search with no results.

```bash
cd kb/tools/uitest
npm install            # playwright + chromium, ignored by git
node run.js            # ~165 checks, about a minute
node run.js search filters      # just those suites
KB_URL=https://ppruchnerovic.github.io/presentations/kb/ node run.js   # the live site
```

`run.js` serves the repo on a free port, runs each suite in its own process,
and exits non-zero if anything failed. Every check prints what it actually saw,
so a red line tells you the story without re-instrumenting the test.

| Suite | Covers |
|---|---|
| `load` | catalogue loads, filters built from the data, one card end to end |
| `search` | every field, phrases, prefixes, the transcript layer, tokenising |
| `controls` | pagination, abstract unfold, tag chips, `/` shortcut |
| `filters` | track / type / stage, the three sorts, Reset, the shareable hash |
| `moments` | "Find this in the talk" — ranking, deep links, caching |
| `resilience` | missing data at each layer, hostile queries, a 390px phone |
| `a11y` | accessible names, keyboard reach, announcements, contrast |
| `ranking` | agreement with `query.py`, plus properties that hold regardless |
| `navigation` | load cost, lazy shards, history, links in and out |

Two things worth knowing when adding a check:

* **The transcript cache is per page.** Anything asserting a cold fetch has to
  open its own page — an earlier click in the same session has already warmed
  it, and the assertion passes without testing anything.
* **`ranking` skips its CLI half** when `data/talks.db` is missing, rather than
  making `query.py` build it mid-test. Run `build_index.py` first for the full
  set.

## Adding another event

Add its id to `EVENTS` in `tools/wadkb.py` and rerun the pipeline. The corpus is
shared rather than split per event, so a search can compare what speakers said
across years; every record keeps `event_id` / `event_name`, and `query.py
--event <slug>` narrows to one.

Event ids are listed at
<https://wad-api.wearedevelopers.com/api/v2/events>.
