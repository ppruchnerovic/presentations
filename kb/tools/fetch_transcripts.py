#!/usr/bin/env python3
"""Fetch YouTube transcripts for every talk in the knowledge base.

This is a thin wrapper. The fetcher itself is the `conference-transcripts`
skill's `scripts/fetch_transcripts.py` — three routes (youtube-transcript-api,
yt-dlp, kome.ai), the per-IP quota handling, `--probe`, `--retry-after`,
atomic writes — and this file only tells it which videos the corpus needs and
where the files go. Every flag of that fetcher works here; `--help` lists them.

    pip install -r requirements.txt
    python3 fetch_transcripts.py --probe --source exact      # is this network usable now?
    python3 fetch_transcripts.py --source exact --retry-after 20
    python3 fetch_transcripts.py --retry-misses               # try the failures again
    python3 fetch_transcripts.py --limit 20                   # small trial run

Output: data/transcripts/<talk_id>.json, named after the corpus's own talk id
and carrying both `talk_id` and `video_id`. Talks whose video has no captions
are recorded in data/transcripts/_misses.json, keyed by video id. A block is
never recorded there — it says nothing about the video — so a plain rerun
picks blocked talks straight back up. Talks already on disk are skipped; to
redo one, delete its file first.

Why a wrapper rather than a copy: the two had drifted 649 diff lines apart.
The copy that lived here had no `--probe` (which README.md and STATE.md tell
the operator to run) and wrote each transcript in place, so a Ctrl-C mid-write
left a truncated `<id>.json` that crashed the next `sync_agenda.py` and
`build_index.py`. One fetcher, one set of lessons.

Afterwards:  python3 sync_agenda.py && python3 build_index.py
"""

from __future__ import annotations

import importlib.util
import sys

import wadkb

FETCHER = (wadkb.KB_ROOT.parent / ".claude" / "skills" / "conference-transcripts"
           / "scripts" / "fetch_transcripts.py")


def load_fetcher():
    """Import the skill's fetcher by path, under its own module name — this
    file is also called fetch_transcripts, and must not import itself."""
    if not FETCHER.exists():
        raise SystemExit(f"{FETCHER} not found — the fetcher lives in the "
                         f"conference-transcripts skill; is this a full checkout?")
    spec = importlib.util.spec_from_file_location("conference_transcripts_fetch", FETCHER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def work_list(talks: list[dict]) -> list[dict]:
    """One entry per talk with a recording, keyed for the corpus: the file is
    `<talk_id>.json`, and `talk_id` rides along into the record."""
    return [{"video_id": t["video_id"], "talk_id": t["id"], "title": t["title"],
             "file": str(t["id"])}
            for t in talks if t.get("video_id")]


def main() -> None:
    fetcher = load_fetcher()
    talks = wadkb.load_talks()
    # --out last, so it wins over anything on the command line: the corpus has
    # one place for transcripts and everything else reads from it.
    fetched = fetcher.main(sys.argv[1:] + ["--out", str(wadkb.TRANSCRIPTS)],
                           work=work_list(talks))
    if fetched:
        print("Next:  python3 sync_agenda.py && python3 build_index.py")


if __name__ == "__main__":
    main()
