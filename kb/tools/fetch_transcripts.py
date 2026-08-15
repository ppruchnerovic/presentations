#!/usr/bin/env python3
"""Fetch YouTube transcripts for every talk in the knowledge base.

RUN THIS ON YOUR OWN MACHINE, not in CI. YouTube blocks datacenter IP ranges
(GitHub Actions runners, cloud containers) with 429 / "Sign in to confirm you're
not a bot". From a normal home connection it just works.

    pip install youtube-transcript-api
    python3 fetch_transcripts.py

The script is resumable — it skips talks it already has, so you can stop it with
Ctrl-C and start it again. Talks whose video has no captions are recorded in
data/transcripts/_misses.json so they are not retried forever.

    python3 fetch_transcripts.py --retry-misses     # try the failures again
    python3 fetch_transcripts.py --limit 20         # small trial run
    python3 fetch_transcripts.py --proxy http://user:pass@host:port

Output: data/transcripts/<talk_id>.json
    {"talk_id":591,"video_id":"...","language":"en","word_count":4210,
     "segments":[{"start":12.3,"duration":4.1,"text":"..."}]}
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time

import wadkb

MISSES = wadkb.TRANSCRIPTS / "_misses.json"

# Preference order. `en` variants first, then the majors seen on this conference.
LANGUAGES = ["en", "en-US", "en-GB", "de", "es", "fr", "pt", "it", "nl", "pl", "uk"]


def load_misses() -> dict:
    if MISSES.exists():
        with MISSES.open(encoding="utf-8") as f:
            return json.load(f)
    return {}


def build_api(proxy: str | None):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        sys.exit("youtube-transcript-api is not installed:\n    pip install youtube-transcript-api")

    if proxy:
        from youtube_transcript_api.proxies import GenericProxyConfig

        return YouTubeTranscriptApi(proxy_config=GenericProxyConfig(http_url=proxy, https_url=proxy))
    return YouTubeTranscriptApi()


def pick_and_fetch(api, video_id: str):
    """Return (segments, language, is_generated). Prefers a manual transcript."""
    listing = api.list(video_id)
    transcript = None
    try:
        transcript = listing.find_manually_created_transcript(LANGUAGES)
    except Exception:
        try:
            transcript = listing.find_generated_transcript(LANGUAGES)
        except Exception:
            # Fall back to whatever single transcript exists, translated to English.
            for t in listing:
                transcript = t.translate("en") if t.is_translatable else t
                break
    if transcript is None:
        raise LookupError("no transcript tracks")

    fetched = transcript.fetch()
    raw = fetched.to_raw_data() if hasattr(fetched, "to_raw_data") else list(fetched)
    return raw, transcript.language_code, transcript.is_generated


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="stop after N successful fetches")
    ap.add_argument("--retry-misses", action="store_true")
    ap.add_argument("--proxy", help="http(s) proxy URL, if your IP gets rate limited")
    ap.add_argument("--min-delay", type=float, default=1.0)
    ap.add_argument("--max-delay", type=float, default=2.5)
    args = ap.parse_args()

    talks = wadkb.load_talks()
    wadkb.TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    misses = {} if args.retry_misses else load_misses()

    todo = [
        t
        for t in talks
        if t.get("video_id")
        and not wadkb.transcript_path(t["id"]).exists()
        and str(t["id"]) not in misses
    ]
    have = sum(1 for t in talks if wadkb.transcript_path(t["id"]).exists())
    print(f"{len(talks)} talks · {have} already fetched · {len(misses)} known misses · {len(todo)} to try\n")

    api = build_api(args.proxy)
    ok = fail = 0

    for i, t in enumerate(todo, 1):
        if args.limit and ok >= args.limit:
            break
        vid = t["video_id"]
        label = t["title"][:58]
        try:
            raw, lang, generated = pick_and_fetch(api, vid)
            segments = [
                {"start": round(float(s["start"]), 2),
                 "duration": round(float(s["duration"]), 2),
                 "text": " ".join(str(s["text"]).split())}
                for s in raw
                if str(s.get("text", "")).strip()
            ]
            words = sum(len(s["text"].split()) for s in segments)
            wadkb.write_json(
                wadkb.transcript_path(t["id"]),
                {
                    "talk_id": t["id"],
                    "video_id": vid,
                    "title": t["title"],
                    "language": lang,
                    "auto_generated": bool(generated),
                    "word_count": words,
                    "segments": segments,
                },
                compact=True,
            )
            ok += 1
            print(f"[{i}/{len(todo)}] ok   {words:>6,}w {lang:<5} {label}")
        except KeyboardInterrupt:
            print("\ninterrupted — progress is saved, rerun to continue")
            break
        except Exception as e:
            fail += 1
            reason = type(e).__name__
            misses[str(t["id"])] = {"video_id": vid, "reason": reason, "detail": str(e)[:200]}
            print(f"[{i}/{len(todo)}] MISS {reason:<28} {label}")
            if "IpBlocked" in reason or "TooManyRequests" in reason:
                print("\n!! YouTube is rate limiting this IP. Stopping.")
                print("   Wait a while, use --proxy, or run from a different network.")
                break
        time.sleep(random.uniform(args.min_delay, args.max_delay))

    wadkb.write_json(MISSES, misses)
    print(f"\ndone: {ok} fetched, {fail} missed. Misses recorded in {MISSES.name}")
    if ok:
        print("Next:  python3 sync_agenda.py && python3 build_index.py")


if __name__ == "__main__":
    main()
