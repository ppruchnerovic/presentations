#!/usr/bin/env python3
"""Enumerate a YouTube playlist or channel into a videos.json work list.

This is the cheap half of the job: yt-dlp reads the playlist page itself, not
the caption endpoint, so it does not touch the per-IP transcript quota that
fetch_transcripts.py has to ration. Enumerate freely; fetch carefully.

    python3 list_videos.py <playlist-or-channel-url> -o videos.json

Conference channels mix talks with trailers, sponsor clips and livestream
re-runs, so the filters matter more than they look:

    --min-duration 300        drop shorts, stings and teasers
    --keep-unknown-duration   keep entries yt-dlp reported no duration for
                              (a duration filter drops them by default —
                              nothing checked them)
    --match 'Day [12]'        keep only titles matching a regex
    --exclude 'Livestream'    drop titles matching a regex
    --limit 50                first N after filtering

Output (also accepted directly by fetch_transcripts.py --from):

    {"source": "...", "count": 120,
     "videos": [{"video_id": "...", "title": "...", "duration_s": 1834,
                 "url": "...", "uploader": "...", "upload_date": "20260317"}]}
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys


def ytdlp_binary() -> str:
    """yt-dlp next to the running interpreter (venv install) wins over PATH."""
    local = os.path.join(os.path.dirname(sys.executable), "yt-dlp")
    if os.path.exists(local):
        return local
    found = shutil.which("yt-dlp")
    if not found:
        sys.exit("yt-dlp is not installed:\n    pip install yt-dlp")
    return found


def enumerate_playlist(url: str, timeout: int = 300, first: int = 0) -> list[dict]:
    """Flat-list a playlist/channel. One request per page, no media touched.

    `first` caps how far yt-dlp pages in, which matters on a channel with
    thousands of uploads — the filters below only run on what came back.
    """
    cmd = [ytdlp_binary(), "--flat-playlist", "--dump-json",
           "--no-warnings", "--ignore-errors"]
    if first:
        cmd += ["--playlist-end", str(first)]
    cmd.append(url)
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)

    videos = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        vid = e.get("id")
        # A channel URL can yield nested playlist entries; those have no video id
        # of their own and would otherwise land in the list as phantom talks.
        if not vid or e.get("_type") == "playlist":
            continue
        videos.append({
            "video_id": vid,
            "title": " ".join((e.get("title") or "").split()),
            "duration_s": int(e["duration"]) if e.get("duration") else None,
            "url": e.get("url") or f"https://www.youtube.com/watch?v={vid}",
            "uploader": e.get("uploader") or e.get("channel"),
            "upload_date": e.get("upload_date"),
        })

    if not videos:
        err = (proc.stderr or "").strip().splitlines()
        sys.exit("no videos found" + (f": {err[-1][:200]}" if err else ""))
    return videos


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", help="playlist, channel or /videos URL")
    ap.add_argument("-o", "--out", default="videos.json")
    ap.add_argument("--min-duration", type=int, default=0, metavar="SECONDS",
                    help="drop videos shorter than this (0 keeps everything)")
    ap.add_argument("--max-duration", type=int, default=0, metavar="SECONDS")
    ap.add_argument("--keep-unknown-duration", action="store_true",
                    help="keep entries whose duration yt-dlp did not report; by "
                         "default a duration filter drops them, since nothing "
                         "checked them")
    ap.add_argument("--match", help="keep only titles matching this regex")
    ap.add_argument("--exclude", help="drop titles matching this regex")
    ap.add_argument("--limit", type=int, help="keep only the first N after filtering")
    ap.add_argument("--first", type=int, default=0, metavar="N",
                    help="only page N entries deep into the playlist/channel before "
                         "filtering — use this on big channels")
    ap.add_argument("--dry-run", action="store_true",
                    help="print what would be written, write nothing")
    args = ap.parse_args()

    videos = enumerate_playlist(args.url, first=args.first)
    total = len(videos)

    keep, dropped = [], {"short": 0, "long": 0, "unknown-duration": 0,
                         "match": 0, "exclude": 0}
    filtering_duration = bool(args.min_duration or args.max_duration)
    rx_in = re.compile(args.match, re.I) if args.match else None
    rx_out = re.compile(args.exclude, re.I) if args.exclude else None
    for v in videos:
        d = v["duration_s"]
        if d is None and filtering_duration:
            # yt-dlp leaves duration out for live/premiere entries and some
            # flat-playlist rows. Such an entry used to slip past --min-duration
            # untouched, which is how a 40-second sting ends up in a talk corpus.
            if not args.keep_unknown_duration:
                dropped["unknown-duration"] += 1
                continue
        if args.min_duration and d is not None and d < args.min_duration:
            dropped["short"] += 1
            continue
        if args.max_duration and d is not None and d > args.max_duration:
            dropped["long"] += 1
            continue
        if rx_in and not rx_in.search(v["title"]):
            dropped["match"] += 1
            continue
        if rx_out and rx_out.search(v["title"]):
            dropped["exclude"] += 1
            continue
        keep.append(v)

    if args.limit:
        keep = keep[: args.limit]

    print(f"{total} videos found · {len(keep)} kept")
    for k, n in dropped.items():
        if n:
            print(f"  dropped {n} ({k})")
    if dropped["unknown-duration"]:
        print("  (--keep-unknown-duration keeps those instead)")
    unknown_kept = sum(1 for v in keep if v["duration_s"] is None)
    if unknown_kept:
        print(f"  {unknown_kept} kept with an unknown duration")
    for v in keep[:5]:
        mins = f"{v['duration_s'] // 60}m" if v["duration_s"] else "?"
        print(f"  {v['video_id']}  {mins:>5}  {v['title'][:60]}")
    if len(keep) > 5:
        print(f"  … and {len(keep) - 5} more")

    if args.dry_run:
        return

    payload = {"source": args.url, "count": len(keep), "videos": keep}
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"\nwrote {args.out}")
    print(f"Next:  python3 fetch_transcripts.py --from {args.out} --out transcripts/ "
          f"--source exact --retry-after 20")


if __name__ == "__main__":
    main()
