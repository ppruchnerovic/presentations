#!/usr/bin/env python3
"""Fetch YouTube transcripts for every talk in the knowledge base.

Three routes, tried in that order:

  1. youtube-transcript-api — real caption timings ("timing": "exact"), so a
     search hit deep-links to the precise second. Only works from an IP YouTube
     has not flagged, which in practice means a normal home connection: from
     CI runners and cloud containers it returns 429 / "Sign in to confirm
     you're not a bot". A corporate proxy counts as a datacenter IP too —
     Zscaler and friends will get you blocked just as fast.

  2. yt-dlp — also exact, and reaches the caption track through a different
     Innertube client, so it sometimes works when route 1 is refused. Needs
     yt-dlp on PATH (or in the same venv as this script).

  3. kome.ai — fetches the captions server-side from its own IPs, so it works
     from anywhere, but returns plain text with no timing. Starts are
     interpolated from word position ("timing": "estimated"), which lands you
     near a quote rather than exactly on it.

After three consecutive failures of route 1 the script stops trying it and
uses the fallbacks for the rest of the run.

    pip install youtube-transcript-api yt-dlp
    python3 fetch_transcripts.py                 # auto: exact where possible
    python3 fetch_transcripts.py --source exact     # routes 1-2 only, never estimate
    python3 fetch_transcripts.py --source youtube   # route 1 only
    python3 fetch_transcripts.py --source ytdlp     # route 2 only
    python3 fetch_transcripts.py --source kome      # skip YouTube entirely

YouTube rate limits by IP and by volume, so the fetch paces itself: a jittered
delay between requests on every worker, and a hard stop the moment a block is
reported rather than burning the rest of the corpus against a closed door. A
block is *not* recorded as a miss — it says nothing about the video — so a
plain rerun picks the remaining talks straight back up.

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
import glob
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

import wadkb

KOME_API = "https://kome.ai/api/transcript"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/131.0.0.0 Safari/537.36")


class BlockedError(Exception):
    """YouTube refused this IP, rather than this video."""


def is_block(e: Exception) -> bool:
    """A network verdict, not a fact about the talk — so never cached as a miss."""
    if isinstance(e, BlockedError):
        return True
    name = type(e).__name__
    return any(k in name for k in ("IpBlocked", "TooManyRequests", "RequestBlocked"))


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

def ytdlp_binary() -> str | None:
    """yt-dlp next to the running interpreter (venv install) wins over PATH."""
    local = os.path.join(os.path.dirname(sys.executable), "yt-dlp")
    return local if os.path.exists(local) else shutil.which("yt-dlp")


def parse_json3(path: str) -> list[dict]:
    """YouTube's json3 caption format -> our segment shape.

    Auto-generated tracks carry the text twice: real events, plus 'aAppend'
    rollup events that repeat the previous line so the caption box can scroll.
    Keeping those would duplicate most of the transcript, so they are dropped.
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    out = []
    for ev in data.get("events") or []:
        if ev.get("aAppend"):
            continue
        text = " ".join("".join(s.get("utf8", "") for s in (ev.get("segs") or [])).split())
        if not text:
            continue
        start = float(ev.get("tStartMs", 0)) / 1000.0
        dur = float(ev.get("dDurationMs", 0)) / 1000.0
        out.append({"start": round(start, 2),
                    "duration": round(max(dur, 0.5), 2),
                    "text": text})
    return out


def fetch_ytdlp(video_id: str, proxy: str | None = None) -> tuple[list[dict], str]:
    """Exact timings via yt-dlp, which asks a different Innertube client.

    Writes the caption track to a temp dir as json3 and parses it; --skip-download
    means no media is ever fetched, only the subtitle file.
    """
    exe = ytdlp_binary()
    if not exe:
        raise LookupError("yt-dlp is not installed")

    with tempfile.TemporaryDirectory() as tmp:
        cmd = [exe, "--skip-download", "--write-auto-subs", "--write-subs",
               "--sub-langs", YTDLP_SUB_LANGS, "--sub-format", "json3",
               "--no-warnings", "--no-progress",
               "-o", os.path.join(tmp, "%(id)s.%(ext)s"),
               f"https://www.youtube.com/watch?v={video_id}"]
        if proxy:
            cmd += ["--proxy", proxy]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

        found = sorted(glob.glob(os.path.join(tmp, "*.json3")))
        if not found:
            err = (proc.stderr or proc.stdout or "").strip().splitlines()
            detail = err[-1][:160] if err else "no caption file written"
            # yt-dlp reports a throttle in its stderr rather than its exit code,
            # so surface it under the name the block handling looks for.
            if "429" in detail or "Too Many Requests" in detail:
                raise BlockedError(f"yt-dlp: {detail}")
            raise LookupError(f"yt-dlp: {detail}")

        # LANGUAGES is a preference order; pick the earliest one that came back.
        def rank(p: str) -> int:
            tag = os.path.basename(p).split(".")[-2].lower()
            for i, want in enumerate(LANGUAGES):
                if tag == want.lower() or tag.startswith(want.lower()):
                    return i
            return len(LANGUAGES)

        best = min(found, key=rank)
        segments = parse_json3(best)
        if not segments:
            raise LookupError("yt-dlp: caption file had no usable events")
        lang = os.path.basename(best).split(".")[-2].replace("-orig", "")
        return segments, lang


MISSES = wadkb.TRANSCRIPTS / "_misses.json"

# Preference order. `en` variants first, then the majors seen on this conference.
LANGUAGES = ["en", "en-US", "en-GB", "de", "es", "fr", "pt", "it", "nl", "pl", "uk"]

# Same list for yt-dlp, whose --sub-langs takes patterns. `en.*` is what catches
# the auto track YouTube names `en-orig`.
YTDLP_SUB_LANGS = "en.*,en,de,es,fr,pt,it,nl,pl,uk"


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


def fetch_one(api, vid: str, source: str, proxy: str | None = None):
    """Walk the routes in preference order: exact timings first, estimates last.

    Returns (segments, language, auto_generated, timing, source_used). A block
    from an exact route propagates rather than being papered over with an
    estimate — the caller stops the run and the talk stays unfetched, which is
    recoverable; a silently estimated transcript is not.
    """
    exact_only = source in ("exact", "youtube", "ytdlp")

    if source in ("auto", "exact", "youtube") and not (source == "auto" and _yt_strikes[0] >= 3):
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
        except Exception as e:
            if source == "youtube" or is_block(e):
                raise
            _yt_strikes[0] += 1
            if _yt_strikes[0] == 3:
                print("   (youtube-transcript-api keeps failing — trying yt-dlp from here on)")

    if source in ("auto", "exact", "ytdlp"):
        try:
            segments, lang = fetch_ytdlp(vid, proxy)
            return segments, lang, True, "exact", "ytdlp"
        except Exception as e:
            if exact_only or is_block(e):
                raise

    segments, lang, _total = fetch_kome(vid)
    return segments, lang, True, "estimated", "kome"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=("auto", "exact", "youtube", "ytdlp", "kome"),
                    default="auto",
                    help="auto: exact timings if YouTube allows it, else kome.ai. "
                         "exact: routes 1-2 only, never fall back to estimates")
    ap.add_argument("--limit", type=int, help="only attempt the first N talks")
    ap.add_argument("--workers", type=int, default=2,
                    help="parallel fetches (default 2; 1 disables threading). "
                         "Requests are paced on every worker, so raising this "
                         "raises the request rate — which is what gets you blocked")
    ap.add_argument("--retry-misses", action="store_true")
    ap.add_argument("--proxy", help="http(s) proxy URL, if your IP gets rate limited")
    ap.add_argument("--min-delay", type=float, default=3.0)
    ap.add_argument("--max-delay", type=float, default=7.0)
    ap.add_argument("--retry-after", type=float, default=0, metavar="MINUTES",
                    help="when YouTube blocks the IP, wait this long and resume "
                         "where it stopped. 0 (default) stops on the first block. "
                         "The quota refills with time, so a long wait finishes a "
                         "corpus that no single run can")
    ap.add_argument("--max-rounds", type=int, default=24,
                    help="give up after this many blocked rounds (default 24)")
    args = ap.parse_args()

    talks = wadkb.load_talks()
    wadkb.TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    misses = {} if args.retry_misses else load_misses()
    api = build_api(args.proxy)
    total_ok = total_fail = 0

    # Each round re-derives its work from what is on disk, so a blocked round
    # costs nothing but time — nothing is lost and nothing is refetched.
    for rnd in range(1, args.max_rounds + 1):
        todo = [
            t
            for t in talks
            if t.get("video_id")
            and not wadkb.transcript_path(t["id"]).exists()
            and str(t["id"]) not in misses
        ]
        have = sum(1 for t in talks if wadkb.transcript_path(t["id"]).exists())
        label = f"round {rnd}: " if rnd > 1 else ""
        print(f"{label}{len(talks)} talks · {have} already fetched · "
              f"{len(misses)} known misses · {len(todo)} to try\n")
        if not todo:
            break

        if args.limit:
            todo = todo[: args.limit]

        if args.workers > 1:
            ok, fail, blocked = run_parallel(api, todo, misses, args)
        else:
            ok, fail, blocked = run_serial(api, todo, misses, args)
        total_ok += ok
        total_fail += fail
        wadkb.write_json(MISSES, misses)

        if not blocked or not args.retry_after or args.limit:
            break
        if rnd == args.max_rounds:
            print(f"\ngiving up after {rnd} blocked rounds — rerun when the quota recovers")
            break
        print(f"waiting {args.retry_after:g} min for the quota to recover, then resuming "
              f"({total_ok} fetched so far)\n", flush=True)
        try:
            time.sleep(args.retry_after * 60)
        except KeyboardInterrupt:
            print("\ninterrupted — finished work is saved, rerun to continue")
            break

    wadkb.write_json(MISSES, misses)
    print(f"\ndone: {total_ok} fetched, {total_fail} missed. Misses recorded in {MISSES.name}")
    if total_ok:
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


BLOCK_ADVICE = (
    "\n!! YouTube is rate limiting this IP. Stopping so the rest stay retryable.\n"
    "   Wait a few hours, switch networks (a phone hotspot resets it), or use\n"
    "   --proxy. A corporate VPN/proxy egresses from a datacenter range and is\n"
    "   blocked hardest — drop it before retrying. Blocked talks are NOT recorded\n"
    "   as misses, so a plain rerun picks them up.\n"
)


def run_parallel(api, todo, misses, args):
    """Threads spend nearly all their time waiting on the network, so a handful
    of workers cuts a ~70 minute run to well under half that.

    Each worker sleeps before its request, so the request rate is roughly
    workers / mean-delay — pacing that the serial path always had and this one
    used to skip entirely, which is exactly how a run gets an IP blocked.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading

    blocked = threading.Event()
    ok = fail = 0
    done = 0          # real outcomes only — see the skip below

    def work(t):
        if blocked.is_set():
            raise BlockedError("skipped — run already stopped by a block")
        time.sleep(random.uniform(args.min_delay, args.max_delay))
        segments, lang, generated, timing, source = fetch_one(
            api, t["video_id"], args.source, args.proxy)
        return save(t, segments, lang, generated, timing, source), timing, source

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(work, t): t for t in todo}
        try:
            # This loop is the only thread touching the counters, so no lock.
            for fut in as_completed(futures):
                t = futures[fut]
                try:
                    words, timing, source = fut.result()
                except Exception as e:
                    if is_block(e):
                        # Says nothing about this video, so it is neither a miss
                        # nor an attempt — once blocked, the rest of the round
                        # fails instantly, and counting those would race the
                        # progress number to the end while nothing was fetched.
                        if not blocked.is_set():
                            blocked.set()
                            print(BLOCK_ADVICE)
                        continue
                    done += 1
                    fail += 1
                    misses[str(t["id"])] = {"video_id": t["video_id"],
                                            "reason": type(e).__name__, "detail": str(e)[:200]}
                    print(f"[{done}/{len(todo)}] MISS {type(e).__name__:<24} {t['title'][:48]}")
                    continue
                done += 1
                ok += 1
                print(f"[{done}/{len(todo)}] ok   {words:>6,}w {source:<5} {timing:<9} {t['title'][:48]}")
        except KeyboardInterrupt:
            print("\ninterrupted — finished work is saved, rerun to continue")
            pool.shutdown(wait=False, cancel_futures=True)
            return ok, fail, False
    return ok, fail, blocked.is_set()


def run_serial(api, todo, misses, args):
    ok = fail = 0
    blocked = False
    for i, t in enumerate(todo, 1):
        vid = t["video_id"]
        label = t["title"][:52]
        try:
            segments, lang, generated, timing, source = fetch_one(api, vid, args.source, args.proxy)
            words = save(t, segments, lang, generated, timing, source)
            ok += 1
            print(f"[{i}/{len(todo)}] ok   {words:>6,}w {source:<5} {timing:<9} {label}")
        except KeyboardInterrupt:
            print("\ninterrupted — progress is saved, rerun to continue")
            break
        except Exception as e:
            reason = type(e).__name__
            if is_block(e):
                print(f"[{i}/{len(todo)}] BLOCKED  {label}")
                print(BLOCK_ADVICE)
                blocked = True
                break
            fail += 1
            misses[str(t["id"])] = {"video_id": vid, "reason": reason, "detail": str(e)[:200]}
            print(f"[{i}/{len(todo)}] MISS {reason:<28} {label}")
        time.sleep(random.uniform(args.min_delay, args.max_delay))
    return ok, fail, blocked


if __name__ == "__main__":
    main()
