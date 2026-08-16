# Presentations

HTML recaps of conference talks from the AI Dev Community, published via GitHub Pages.

**Live site: https://ppruchnerovic.github.io/presentations/**

GitHub Pages serves the `gh-pages` branch. On every push to `main`, the
`Deploy GitHub Pages` workflow (`.github/workflows/pages.yml`) mirrors `main`
into `gh-pages`, so the site redeploys automatically — never edit `gh-pages`
directly.

## Structure

- `index.html` — landing page listing all presentations
- `posts/<slug>/index.html` — one self-contained HTML page per talk recap
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
