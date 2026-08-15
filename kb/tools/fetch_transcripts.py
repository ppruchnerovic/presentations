#!/usr/bin/env python3
"""Fetch YouTube transcripts for every talk in the knowledge base.

Two routes, tried in that order:

  1. youtube-transcript-api — real caption timings ("timing": "exact"), so a
     search hit deep-links to the precise second. Only works from an IP YouTube
     has not flagged, which in practice means a normal home connection: from
     CI runners and cloud containers it returns 429 / "Sign in to confirm
     you're not a bot".

  2. kome.ai — fetches the captions server-side from its own IPs, so it works
     from anywhere, but returns plain text with no timing. Starts are
     interpolated from word position ("timing": "estimated"), which lands you
     near a quote rather than exactly on it.

After three consecutive YouTube failures the script stops trying route 1 and
uses kome.ai for the rest of the run.

    pip install youtube-transcript-api
    python3 fetch_transcripts.py                 # auto: exact where possible
    python3 fetch_transcripts.py --source youtube   # exact only, fail otherwise
    python3 fetch_transcripts.py --source kome      # skip YouTube entirely

Re-running from a home connection will NOT upgrade estimated transcripts to
exact ones — it skips talks already fetched. Delete the ones you want redone
(or the whole data/transcripts directory) first.

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
import re
import sys
import time
import urllib.error
import urllib.request

import wadkb

KOME_API = "https://kome.ai/api/transcript"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/131.0.0.0 Safari/537.36")


def kome_length_seconds(s: str) -> float:
    """kome.ai reports '26m 12s' / '1h 2m 3s'. Returns 0 if unparseable."""
    m = re.fullmatch(r"\s*(?:(\d+)h\s*)?(?:(\d+)m\s*)?(?:(\d+)s)?\s*", s or "")
    if not m or not (s or "").strip():
        return 0.0
    h, mn, sec = (int(g) if g else 0 for g in m.groups())
    return h * 3600 + mn * 60 + sec


def fetch_kome(video_id: str) -> tuple[list[dict], str, float] | None:
    """Server-side caption fetch, used when YouTube has flagged this IP.

    kome.ai returns plain text with no timing, so starts are interpolated from
    word position across the video's runtime. Good enough to jump near a quote;
    not frame-accurate. Segments carry timing='estimated' so nothing downstream
    presents them as exact.
    """
    req = urllib.request.Request(
        KOME_API,
        data=json.dumps({"video_id": f"https://www.youtube.com/watch?v={video_id}",
                         "format": True}).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": UA},
        method="POST",
    )
    # Connections drop intermittently (SSL EOF, read timeouts), more so with
    # several workers in flight. These are transient, so retry before giving up.
    last = None
    for attempt in range(4):
        if attempt:
            time.sleep(2 ** attempt + random.uniform(0, 1.5))
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            break
        except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError) as e:
            last = e
    else:
        raise last

    text = (data.get("transcript") or "").strip()
    if not text:
        raise LookupError("kome returned an empty transcript")
    if data.get("hasMore"):
        # A truncated transcript silently misrepresents the talk — refuse it.
        raise LookupError("kome returned a truncated transcript (hasMore)")

    total = kome_length_seconds(str(data.get("length") or ""))
    lines = [" ".join(l.split()) for l in text.splitlines() if l.strip()]
    if not lines:
        lines = [" ".join(text.split())]
    counts = [len(l.split()) for l in lines]
    n_words = sum(counts) or 1

    # Group the short caption-style lines into ~25-word chunks so the segment
    # list stays a sensible size, then spread them over the runtime.
    segments, buf, buf_words, seen = [], [], 0, 0
    for line, c in zip(lines, counts):
        if not buf:
            start_words = seen
        buf.append(line)
        buf_words += c
        seen += c
        if buf_words >= 25:
            segments.append((start_words, " ".join(buf)))
            buf, buf_words = [], 0
    if buf:
        segments.append((start_words, " ".join(buf)))

    out = []
    for i, (start_words, chunk) in enumerate(segments):
        start = (start_words / n_words) * total if total else float(start_words)
        nxt = segments[i + 1][0] if i + 1 < len(segments) else n_words
        end = (nxt / n_words) * total if total else float(nxt)
        out.append({"start": round(start, 2),
                    "duration": round(max(end - start, 0.5), 2),
                    "text": chunk})
    return out, "en", total

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


_yt_strikes = [0]   # consecutive YouTube failures; 3 in a row means this IP is blocked


def fetch_one(api, vid: str, source: str):
    """Try the timestamped route first, fall back to the server-side one.

    Returns (segments, language, auto_generated, timing, source_used).
    """
    if source == "youtube" or (source == "auto" and _yt_strikes[0] < 3):
        try:
            raw, lang, generated = pick_and_fetch(api, vid)
            segments = [
                {"start": round(float(s["start"]), 2),
                 "duration": round(float(s["duration"]), 2),
                 "text": " ".join(str(s["text"]).split())}
                for s in raw
                if str(s.get("text", "")).strip()
            ]
            if segments:
                _yt_strikes[0] = 0
                return segments, lang, generated, "exact", "yt"
        except Exception:
            if source == "youtube":
                raise
            _yt_strikes[0] += 1
            if _yt_strikes[0] == 3:
                print("   (YouTube is blocking this IP — using kome.ai from here on)")
    segments, lang, _total = fetch_kome(vid)
    return segments, lang, True, "estimated", "kome"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=("auto", "youtube", "kome"), default="auto",
                    help="auto: exact timings if YouTube allows it, else kome.ai")
    ap.add_argument("--limit", type=int, help="only attempt the first N talks")
    ap.add_argument("--workers", type=int, default=4,
                    help="parallel fetches (default 4; 1 disables threading)")
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

    if args.limit:
        todo = todo[: args.limit]

    api = build_api(args.proxy)
    if args.workers > 1:
        ok, fail = run_parallel(api, todo, misses, args)
    else:
        ok, fail = run_serial(api, todo, misses, args)

    wadkb.write_json(MISSES, misses)
    print(f"\ndone: {ok} fetched, {fail} missed. Misses recorded in {MISSES.name}")
    if ok:
        print("Next:  python3 sync_agenda.py && python3 build_index.py")


def save(t: dict, segments, lang, generated, timing, source) -> int:
    words = sum(len(s["text"].split()) for s in segments)
    wadkb.write_json(
        wadkb.transcript_path(t["id"]),
        {
            "talk_id": t["id"],
            "video_id": t["video_id"],
            "title": t["title"],
            "language": lang,
            "auto_generated": bool(generated),
            "source": source,
            "timing": timing,          # "exact" or "estimated"
            "word_count": words,
            "segments": segments,
        },
        compact=True,
    )
    return words


def run_parallel(api, todo, misses, args):
    """Threads spend nearly all their time waiting on the network, so a handful
    of workers cuts a ~70 minute run to under 20 without hammering anyone."""
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading

    lock = threading.Lock()
    ok = fail = 0
    done = 0

    def work(t):
        segments, lang, generated, timing, source = fetch_one(api, t["video_id"], args.source)
        return save(t, segments, lang, generated, timing, source), timing, source

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(work, t): t for t in todo}
        try:
            for fut in as_completed(futures):
                t = futures[fut]
                with lock:
                    done += 1
                    n = done
                try:
                    words, timing, source = fut.result()
                    ok += 1
                    print(f"[{n}/{len(todo)}] ok   {words:>6,}w {source:<5} {timing:<9} {t['title'][:48]}")
                except Exception as e:
                    fail += 1
                    misses[str(t["id"])] = {"video_id": t["video_id"],
                                            "reason": type(e).__name__, "detail": str(e)[:200]}
                    print(f"[{n}/{len(todo)}] MISS {type(e).__name__:<24} {t['title'][:48]}")
        except KeyboardInterrupt:
            print("\ninterrupted — finished work is saved, rerun to continue")
            pool.shutdown(wait=False, cancel_futures=True)
    return ok, fail


def run_serial(api, todo, misses, args):
    ok = fail = 0
    for i, t in enumerate(todo, 1):
        vid = t["video_id"]
        label = t["title"][:52]
        try:
            segments, lang, generated, timing, source = fetch_one(api, vid, args.source)
            words = save(t, segments, lang, generated, timing, source)
            ok += 1
            print(f"[{i}/{len(todo)}] ok   {words:>6,}w {source:<5} {timing:<9} {label}")
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
    return ok, fail


if __name__ == "__main__":
    main()
