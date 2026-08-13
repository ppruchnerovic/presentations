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
