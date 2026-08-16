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

## The talk knowledge base (`kb/`)

Every recorded talk from the WeAreDevelopers World Congress — 358 at the last
refresh — with abstracts, speakers, track / type / stage tags, recording links
and full searchable transcripts. It is a self-contained corpus plus its own
tooling, and it has nothing to do with the post recaps above beyond sharing this
repo and its Pages deployment.

Three ways in:

| | |
|---|---|
| Browser, nothing to install | <https://ppruchnerovic.github.io/presentations/kb/> — searches abstracts *and* what was actually said on stage, and deep-links to the second where a phrase is spoken |
| Terminal | `cd kb/tools && python3 query.py "spec driven development"` |
| Claude Code | the `conference-talks` skill in the `second-brain` repo |

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
