# Presentations

HTML recaps of conference talks from the AI Dev Community, plus a searchable
knowledge base of every recorded talk from the WeAreDevelopers World Congress.
Both are published via GitHub Pages.

- **Live site:** <https://ppruchnerovic.github.io/presentations/>
- **Talk knowledge base:** <https://ppruchnerovic.github.io/presentations/kb/>

GitHub Pages serves the `gh-pages` branch. On every push to `main`, the
`Deploy GitHub Pages` workflow (`.github/workflows/pages.yml`) mirrors `main`
into `gh-pages`, so the site redeploys automatically — never edit `gh-pages`
directly — the one workflow that does is the weekly knowledge base refresh, for
the reason described below.

## Structure

- `index.html` — landing page listing all presentations
- `posts/<slug>/index.html` — one self-contained HTML page per talk recap
- `kb/` — the conference talk knowledge base (see below)
- `.nojekyll` — serve files as-is, no Jekyll processing

## Adding a new presentation

1. Copy the post's HTML file to `posts/<new-slug>/index.html`.
2. Add a card for it in `index.html`.
3. Push to `main` — the workflow redeploys automatically.

## Where the pages come from

The recaps are not written by hand. They are produced by the
`youtube-community-post` Claude Code skill in the second-brain vault
(`.claude/skills/youtube-community-post/`), which turns a YouTube link into a
transcript, a community post in three formats, and finally a page on this
site.

```
YouTube URL
    │
    ▼
1. FETCH TRANSCRIPT        yt-dlp → kome.ai fallback → user paste
    │                      (cloud IPs get bot-checked, hence the fallbacks)
    ▼
2. SAVE TO VAULT           Posts/In/<Video Name>/transcript.md
    │                      cleaned captions, no invented timestamps
    ▼
3. DRAFT POST              Title → bold TL;DR → context → core content
    │                      → numbers → caveats → why it matters → CTA
    ▼
4. HUMANIZE + 3 FORMATS    humanizer runs once, then:
    │                      .md (reference) · .html (styled) · teams.html (paste)
    ▼
5. REVIEW GATE             deliver, commit on branch, stop.
    │                      push to main only on explicit approval
    ▼
6. PUBLISH (optional)      copy to presentations-site, inject Copy-for-Teams
                           button, add card, publish.sh
```

Two rules shape the pipeline: transcript fetching fails often, so every route
has a fallback, and nothing reaches `main` until a human has read the post.

Step 6 is what fills this repo. It adds the `Web version:` link to all three
post formats first, copies `community-post.html` to `posts/<slug>/index.html`,
runs `scripts/add_teams_button.py` to inject the floating "Copy for Teams"
button (it copies the post as clean rich text so Teams applies its own theme),
adds the card to `index.html` with a `Speaker · Company · ~XX min` meta line,
and pushes with `publish.sh`.

## The talk knowledge base (`kb/`)

Every recorded talk from the WeAreDevelopers World Congress — 358 at the last
refresh — with abstracts, speakers, track / type / stage tags, recording links
and full timestamped transcripts. It is a self-contained corpus plus its own
tooling, and it has nothing to do with the post recaps above beyond sharing this
repo and its Pages deployment.

### The corpus, in three shapes

All three are generated from the same run, so they never drift apart:

- `kb/data/talks.json` / `talks.csv` — the canonical corpus, for scripts and
  spreadsheets
- `kb/talks/<event>/<id>-<slug>.md` — one git-diffable file per talk, for
  humans, `grep` and coding agents
- `kb/data/talks.db` (SQLite + FTS5), `search-meta.json` and `tindex/` — the
  search indexes; derived, and rebuildable in seconds

Transcript timings are currently **estimated** (interpolated from word
position), because the exact route needs a non-datacenter IP — see the timing
caveat in `kb/README.md`.

### Three ways to search

| | |
|---|---|
| **Browser**, nothing to install | <https://ppruchnerovic.github.io/presentations/kb/> — searches abstracts *and* what was actually said on stage, filters by track / type / stage, sorts by relevance / schedule / title, and deep-links to the second where a phrase is spoken. The query lives in the URL, so results are shareable |
| **Terminal** | `cd kb/tools && python3 query.py "spec driven development"` — with `-n`, `--track`, `--type`, `--stage`, `--event`, `--no-moments` and `--json`. FTS5 syntax works (`"exact phrase"`, `OR`, `NOT`, `prefix*`), and the index builds itself on first use |
| **Claude Code** | the `conference-talks` skill in the `second-brain` repo. It drives `query.py` and then reads the matching talk files — the right tool for *"what do different speakers think about AI-driven SDLC"*, where retrieval finds the talks and the model compares the positions |

Browser and terminal both rank on passages rather than whole transcripts, so a
multi-word query surfaces the talks that say the words *together*.

### How it fits together

```
  WeAreDevelopers API                    YouTube captions
  (public, no auth)                      (kome.ai fallback)
         │                                      │
         ▼                                      ▼
   sync_agenda.py                       fetch_transcripts.py
         │                              run on a real machine, not CI
         │                                      │
         ▼                                      ▼
   data/talks.json  ─────┐          data/transcripts/<id>.json
   data/talks.csv        │                      │
   talks/**.md   ◄───────┴──────────────────────┘
         │
         ▼
   build_index.py
         │
         ├──► data/talks.db (FTS5)  ──► query.py ──► terminal, Claude Code skill
         │    derived, gitignored
         └──► search-meta.json + tindex/  ──► kb/index.html ──► browser
```

**`kb/README.md` is the guide** — layout, how to rebuild, where the data comes
from. `kb/STATE.md` is the build log: design decisions, dead ends, and the
transcript routes that do and do not work from a cloud container. Read STATE.md
before changing anything in `kb/tools/`.

### What runs on its own

The `Refresh talk metadata` workflow (`.github/workflows/kb-refresh.yml`) pulls
the conference API every Monday at 06:17 UTC, rebuilds the search indexes, and
commits to `main` if the conference changed anything, then mirrors to
`gh-pages` itself so the live search updates the same minute.

That last step looks redundant next to `Deploy GitHub Pages` and is not: a push
made with the default `GITHUB_TOKEN` does not start another workflow, because
GitHub suppresses those triggers to avoid recursive runs. Before the refresh
mirrored to `gh-pages` on its own, new data landed in `main` and then sat there
unpublished until someone happened to push for an unrelated reason. Keep the
mirror step when editing that workflow.

Two things the refresh deliberately does **not** do:

- **Fetch transcripts.** YouTube blocks GitHub's IP ranges, so
  `kb/tools/fetch_transcripts.py` has to run on a real machine. See the timing
  caveat in `kb/README.md`.
- **Commit `kb/data/talks.db`.** It is derived, rebuilds in seconds, and is
  gitignored so it does not push megabytes of churning binary into every weekly
  commit. The browser index (`search-meta.json`, `tindex/`) *is* committed,
  because Pages can only serve files that exist in the repo.
