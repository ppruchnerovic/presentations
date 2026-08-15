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
├── talks/<event>/<id>-<slug>.md  one readable file per talk
└── tools/
    ├── wadkb.py                  shared helpers
    ├── sync_agenda.py            conference API  -> talks.json + markdown
    ├── fetch_transcripts.py      YouTube captions -> transcripts/   (run locally)
    ├── build_index.py            everything      -> talks.db + browser index
    └── query.py                  ranked search from the terminal
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
track / type / stage, click **Find this in the talk** to jump to the exact
seconds where a phrase is spoken.

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

The `conference-talks` skill in the `second-brain` repo drives `query.py` and
then reads the matching talk files, which is what you want for questions like
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

### Transcripts must be fetched locally

YouTube blocks datacenter IP ranges. From GitHub Actions or any cloud container
you get `429` / *"Sign in to confirm you're not a bot"*; from a home connection
it just works. So:

```bash
pip install youtube-transcript-api
cd kb/tools && python3 fetch_transcripts.py
```

It is resumable — stop it with Ctrl-C and rerun. Talks whose video has no
captions are recorded in `data/transcripts/_misses.json` so they are not retried
forever; `--retry-misses` forces another attempt. Then rerun `sync_agenda.py`
(to inline transcripts into the markdown) and `build_index.py`, and commit.

The `Refresh talk metadata` workflow keeps the metadata current automatically;
it deliberately does not attempt transcripts.

## Adding another event

Add its id to `EVENTS` in `tools/wadkb.py` and rerun the pipeline. The corpus is
shared rather than split per event, so a search can compare what speakers said
across years; every record keeps `event_id` / `event_name`, and `query.py
--event <slug>` narrows to one.

Event ids are listed at
<https://wad-api.wearedevelopers.com/api/v2/events>.
