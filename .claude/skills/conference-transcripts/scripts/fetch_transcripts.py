#!/usr/bin/env python3
"""Fetch YouTube transcripts for a list of videos, gently.

Generalised from the fetcher that pulled 358 WeAreDevelopers talks; it takes
any work list rather than one conference's corpus. Three routes, in order:

  1. youtube-transcript-api — real caption timings ("timing": "exact"), so a
     hit deep-links to the precise second. Only works from an IP YouTube has
     not flagged, which in practice means an ordinary home connection: from CI
     runners and cloud containers it returns 429 / "Sign in to confirm you're
     not a bot". A corporate proxy egresses from a datacenter range and counts
     the same way.

  2. yt-dlp — also exact, and reaches the caption track through a different
     Innertube client, so it sometimes works when route 1 is refused. Both
     routes draw on the same per-IP allowance, so it is a fallback for a
     *refusal*, not for an exhausted quota.

  3. kome.ai — fetches captions server-side from its own IPs, so it works from
     anywhere, but returns plain text with no timing. Starts are interpolated
     from word position ("timing": "estimated"), which lands you near a quote
     rather than on it — measured against the same corpus, a median of 16s off
     and up to 88s at worst.

After three consecutive failures of route 1 the script stops trying it and
uses the fallbacks for the rest of the run.

    pip install youtube-transcript-api yt-dlp

    python3 fetch_transcripts.py --from videos.json --out transcripts/
    python3 fetch_transcripts.py --playlist <url> --out transcripts/
    python3 fetch_transcripts.py dQw4w9WgXcQ <more ids or urls...>

    --source exact       routes 1-2 only, never fall back to estimates
    --source auto        exact where possible, else kome.ai (default)
    --probe              one request: is this network worth a run right now?

Captions are taken in a language you asked for (--languages, English first), or
machine-translated into one (--translate-to). A track in some other language is
refused unless you pass --allow-other-languages: YouTube occasionally
auto-detects an English talk as another language and returns the ASR as
transliteration, which is useless for search and, saved as a success, never
re-fetched.

YouTube meters the caption endpoint per egress IP with an allowance that
refills over hours — it is not a rate limit, and slowing down does not buy more
(see SKILL.md). So the fetch paces itself, stops dead on the first block rather
than burning the rest of the list against a closed door, and can park and
resume:

    --retry-after 20     wait 20 min on a block, then resume where it stopped
    --max-rounds 24      give up after this many blocked rounds

A block is *not* recorded as a miss — it says nothing about the video — so a
plain rerun picks the remaining videos straight back up. Videos that genuinely
have no captions land in <out>/_misses.json and are not retried forever
(--retry-misses tries them again).

Resumable: it skips videos already on disk. That also means a rerun will NOT
upgrade an estimated transcript to an exact one — delete those files first.

Output: <out>/<video_id>.json
    {"video_id":"...","title":"...","language":"en","source":"yt",
     "timing":"exact","word_count":4210,
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
from pathlib import Path

KOME_API = "https://kome.ai/api/transcript"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/131.0.0.0 Safari/537.36")

# Preference order for caption languages. `en` variants first.
LANGUAGES = ["en", "en-US", "en-GB", "de", "es", "fr", "pt", "it", "nl", "pl", "uk"]
# Same list for yt-dlp, whose --sub-langs takes patterns. `en.*` is what catches
# the auto track YouTube names `en-orig`.
YTDLP_SUB_LANGS = "en.*,en,de,es,fr,pt,it,nl,pl,uk"

VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")

# youtube-transcript-api exceptions that mean "this IP, this environment", not
# "this video". Matched by class where the package is installed, by name where
# it is not (and for versions that renamed them: `TooManyRequests` is the pre-1.0
# name of what 1.x calls `IpBlocked`).
#   RequestBlocked / IpBlocked        the bot wall and the 429
#   YouTubeRequestFailed              any transport-level failure, 403/5xx included
#   PoTokenRequired                   YouTube demanded a proof-of-origin token
#   FailedToCreateConsentCookie       stuck behind the EU consent wall
# Deliberately NOT here: AgeRestricted, VideoUnavailable, TranscriptsDisabled,
# VideoUnplayable, NoTranscriptFound — those are facts about the video, and a
# block stops the whole run, so misclassifying one would park the run on it.
BLOCK_EXC_NAMES = ("IpBlocked", "TooManyRequests", "RequestBlocked",
                   "YouTubeRequestFailed", "PoTokenRequired",
                   "FailedToCreateConsentCookie")

# yt-dlp reports a refusal in its stderr text rather than its exit code, so the
# text is all there is to tell "YouTube is refusing this IP" (retryable, never a
# miss) from "this video has no captions" (a real miss). The bot wall is the
# expensive one: cached as a miss it is skipped on every later rerun.
YTDLP_BLOCK_MARKERS = (
    "sign in to confirm",            # "…you're not a bot" — the bot wall
    "not a bot",
    "confirm you are not a bot",
    "too many requests", "rate limit", "rate-limit",
    "http error 403", "http error 401",
    "captcha",
    "consent", "cookies are required", "cookies to prove",
    "login required", "requires login", "please sign in", "sign in to view",
    "po token", "potoken", "proof of origin",
    "content is not available on this app",
    "is likely being blocked", "has been blocked", "temporarily blocked",
    "your ip", "this ip",
)
# …but these are facts about the *video*, and several of them also match a
# marker above ("Sign in to confirm your age" contains "sign in to confirm"), so
# they are checked first. Treating an age gate as an IP block would stop the
# whole run — and every retry round — on one video that no amount of waiting fixes.
YTDLP_VIDEO_MARKERS = (
    "confirm your age", "age-restricted", "age restricted",
    "inappropriate for some users",
    "private video", "members-only", "members only",
    "video unavailable", "removed by the uploader", "has been terminated",
)
# Bare status codes, matched on word boundaries so an unlucky video id
# ("a429Xy...") cannot masquerade as a throttle.
YTDLP_BLOCK_CODES = re.compile(r"\b(429|403|401)\b")


class BlockedError(Exception):
    """YouTube refused this IP, rather than this video."""


_block_types: tuple | None = None


def block_exception_types() -> tuple:
    """The installed library's own block exceptions, so matching survives renames."""
    global _block_types
    if _block_types is None:
        types = [BlockedError]
        try:
            import youtube_transcript_api as _yta
        except ImportError:
            _yta = None
        if _yta is not None:
            for n in BLOCK_EXC_NAMES:
                t = getattr(_yta, n, None)
                if isinstance(t, type) and issubclass(t, BaseException):
                    types.append(t)
        _block_types = tuple(types)
    return _block_types


def is_block(e: Exception) -> bool:
    """A network verdict, not a fact about the video — so never cached as a miss."""
    if isinstance(e, block_exception_types()):
        return True
    name = type(e).__name__
    return any(k in name for k in BLOCK_EXC_NAMES)


def looks_like_block(text: str) -> bool:
    """Does this yt-dlp output describe a refusal of us, rather than of the video?"""
    t = (text or "").lower()
    if any(m in t for m in YTDLP_VIDEO_MARKERS):
        return False
    return any(m in t for m in YTDLP_BLOCK_MARKERS) or bool(YTDLP_BLOCK_CODES.search(t))


def ytdlp_sub_langs(languages=None) -> str:
    """--sub-langs patterns for a preference list. `xx.*` catches `en-orig` etc."""
    if not languages:
        return YTDLP_SUB_LANGS
    out: list[str] = []
    for lang in languages:
        base = str(lang).split("-")[0].lower()
        for pat in (f"{base}.*", base):
            if pat not in out:
                out.append(pat)
    return ",".join(out)


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
    tmp.replace(path)          # atomic, so a Ctrl-C cannot leave half a file


# --- work list ---------------------------------------------------------------

def extract_video_id(s: str) -> str | None:
    s = s.strip()
    if not s:
        return None
    if VIDEO_ID_RE.match(s):
        return s
    m = re.search(r"(?:v=|youtu\.be/|/embed/|/shorts/|/live/)([A-Za-z0-9_-]{11})", s)
    return m.group(1) if m else None


def load_work(args) -> list[dict]:
    """Build the video list from --from / --playlist / positional arguments."""
    videos: list[dict] = []

    if args.playlist:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from list_videos import enumerate_playlist
        videos += enumerate_playlist(args.playlist)

    if args.from_file:
        raw = Path(args.from_file).read_text(encoding="utf-8")
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            # plain text: one id or URL per line
            data = [l for l in raw.splitlines() if l.strip() and not l.startswith("#")]
        if isinstance(data, dict):
            data = data.get("videos") or data.get("talks") or []
        for e in data:
            if isinstance(e, str):
                vid = extract_video_id(e)
                if vid:
                    videos.append({"video_id": vid, "title": ""})
            elif isinstance(e, dict):
                vid = e.get("video_id") or extract_video_id(str(e.get("url") or ""))
                if vid:
                    videos.append({**e, "video_id": vid})

    for s in args.videos:
        vid = extract_video_id(s)
        if vid:
            videos.append({"video_id": vid, "title": ""})

    seen, out = set(), []
    for v in videos:
        if v["video_id"] not in seen:
            seen.add(v["video_id"])
            out.append(v)
    return out


# --- route 3: kome.ai (estimated timings) ------------------------------------

def kome_length_seconds(s: str) -> float:
    """kome.ai reports '26m 12s' / '1h 2m 3s'. Returns 0 if unparseable."""
    m = re.fullmatch(r"\s*(?:(\d+)h\s*)?(?:(\d+)m\s*)?(?:(\d+)s)?\s*", s or "")
    if not m or not (s or "").strip():
        return 0.0
    h, mn, sec = (int(g) if g else 0 for g in m.groups())
    return h * 3600 + mn * 60 + sec


def fetch_kome(video_id: str) -> tuple[list[dict], str, float]:
    """Server-side caption fetch, used when YouTube has flagged this IP.

    Returns plain text with no timing, so starts are interpolated from word
    position across the runtime. Good enough to jump near a quote; not
    frame-accurate. Segments carry timing='estimated' so nothing downstream
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
    segments, buf, buf_words, seen, start_words = [], [], 0, 0, 0
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
    for i, (sw, chunk) in enumerate(segments):
        start = (sw / n_words) * total if total else float(sw)
        nxt = segments[i + 1][0] if i + 1 < len(segments) else n_words
        end = (nxt / n_words) * total if total else float(nxt)
        out.append({"start": round(start, 2),
                    "duration": round(max(end - start, 0.5), 2),
                    "text": chunk})
    return out, "en", total


# --- route 2: yt-dlp (exact timings) -----------------------------------------

def ytdlp_binary() -> str | None:
    """yt-dlp next to the running interpreter (venv install) wins over PATH."""
    local = os.path.join(os.path.dirname(sys.executable), "yt-dlp")
    return local if os.path.exists(local) else shutil.which("yt-dlp")


def parse_json3(path: str) -> list[dict]:
    """YouTube's json3 caption format -> our segment shape.

    Auto-generated tracks carry the text twice: real events, plus 'aAppend'
    rollup events that repeat the previous line so the caption box can scroll.
    Keeping those would duplicate most of the transcript — this dedup is what
    makes yt-dlp's output match youtube-transcript-api's exactly.
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
        out.append({"start": round(float(ev.get("tStartMs", 0)) / 1000.0, 2),
                    "duration": round(max(float(ev.get("dDurationMs", 0)) / 1000.0, 0.5), 2),
                    "text": text})
    return out


def fetch_ytdlp(video_id: str, proxy: str | None = None,
                languages=None) -> tuple[list[dict], str]:
    """Exact timings via yt-dlp, which asks a different Innertube client.

    --skip-download means no media is ever fetched, only the subtitle file.
    Only the wanted languages are requested, and YouTube offers its machine
    translations under those codes too — so an English talk whose ASR track
    YouTube filed as Hindi still comes back in English here.
    """
    exe = ytdlp_binary()
    if not exe:
        raise LookupError("yt-dlp is not installed")
    langs = list(languages or LANGUAGES)

    with tempfile.TemporaryDirectory() as tmp:
        cmd = [exe, "--skip-download", "--write-auto-subs", "--write-subs",
               "--sub-langs", ytdlp_sub_langs(langs), "--sub-format", "json3",
               "--no-warnings", "--no-progress",
               "-o", os.path.join(tmp, "%(id)s.%(ext)s"),
               f"https://www.youtube.com/watch?v={video_id}"]
        if proxy:
            cmd += ["--proxy", proxy]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

        found = sorted(glob.glob(os.path.join(tmp, "*.json3")))
        if not found:
            output = f"{proc.stderr or ''}\n{proc.stdout or ''}"
            lines = [l.strip() for l in output.splitlines() if l.strip()]
            errs = [l for l in lines if "error" in l.lower()] or lines
            detail = errs[-1][:160] if errs else "no caption file written"
            # yt-dlp reports a refusal in its output rather than its exit code, so
            # surface it under the name the block handling looks for. The whole
            # output is searched, not just the last line: the bot wall's own line
            # ("Sign in to confirm you're not a bot") is often followed by a hint.
            if looks_like_block(output):
                raise BlockedError(f"yt-dlp: {detail}")
            raise LookupError(f"yt-dlp: {detail}")

        def rank(p: str) -> int:
            tag = os.path.basename(p).split(".")[-2].lower()
            for i, want in enumerate(langs):
                if tag == want.lower() or tag.startswith(want.lower()):
                    return i
            return len(langs)

        best = min(found, key=rank)
        segments = parse_json3(best)
        if not segments:
            raise LookupError("yt-dlp: caption file had no usable events")
        return segments, os.path.basename(best).split(".")[-2].replace("-orig", "")


# --- route 1: youtube-transcript-api (exact timings) -------------------------

def build_api(proxy: str | None):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        sys.exit("youtube-transcript-api is not installed:\n"
                 "    pip install youtube-transcript-api")

    if proxy:
        from youtube_transcript_api.proxies import GenericProxyConfig
        return YouTubeTranscriptApi(
            proxy_config=GenericProxyConfig(http_url=proxy, https_url=proxy))
    return YouTubeTranscriptApi()


def pick_and_fetch(api, video_id: str, languages=None, translate_to: str = "en",
                   allow_other_languages: bool = False):
    """Return (raw, language, is_generated), in a language you asked for.

    Preference: a manual track in a wanted language, then an auto one, then any
    track machine-translated into `translate_to`. A track in a language nobody
    asked for is the last resort and off by default — YouTube sometimes
    auto-detects an English talk as another language, and the ASR then comes
    back as transliteration (English speech spelled in Devanagari, in the two
    cases that reached this corpus): unusable for search, and written to disk as
    a success, so no rerun ever replaces it.
    """
    languages = list(languages or LANGUAGES)
    listing = api.list(video_id)

    transcript = None
    for find in (listing.find_manually_created_transcript,
                 listing.find_generated_transcript):
        try:
            transcript = find(languages)
            break
        except Exception:
            continue          # only the lookup is swallowed; fetch errors propagate

    if transcript is None and translate_to:
        # Nothing in a wanted language: have YouTube translate one instead of
        # taking whatever it happens to have. Manual tracks first, as above.
        for t in sorted(listing, key=lambda t: bool(getattr(t, "is_generated", True))):
            if not getattr(t, "is_translatable", False):
                continue
            try:
                transcript = t.translate(translate_to)
                break
            except Exception:
                continue

    if transcript is None:
        others = list(listing)
        if not others:
            raise LookupError("no transcript tracks")
        codes = ",".join(dict.fromkeys(str(t.language_code) for t in others))
        if not allow_other_languages:
            raise LookupError(
                f"only {codes} captions: nothing in {'/'.join(languages[:3])} and "
                f"nothing translatable to {translate_to or '-'} "
                f"(--allow-other-languages takes them as-is)")
        transcript = others[0]

    fetched = transcript.fetch()
    raw = fetched.to_raw_data() if hasattr(fetched, "to_raw_data") else list(fetched)
    return raw, transcript.language_code, transcript.is_generated


_yt_strikes = [0]   # consecutive YouTube failures; 3 in a row means this IP is blocked


def fetch_one(api, vid: str, source: str, proxy: str | None = None,
              languages=None, translate_to: str = "en",
              allow_other_languages: bool = False):
    """Walk the routes in preference order: exact timings first, estimates last.

    Returns (segments, language, auto_generated, timing, source_used). A block
    from an exact route propagates rather than being papered over with an
    estimate — the caller stops the run and the video stays unfetched, which is
    recoverable; a silently estimated transcript is not.
    """
    exact_only = source in ("exact", "youtube", "ytdlp")

    if source in ("auto", "exact", "youtube") and not (source == "auto" and _yt_strikes[0] >= 3):
        try:
            raw, lang, generated = pick_and_fetch(
                api, vid, languages, translate_to, allow_other_languages)
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
            segments, lang = fetch_ytdlp(vid, proxy, languages)
            return segments, lang, True, "exact", "ytdlp"
        except Exception as e:
            if exact_only or is_block(e):
                raise

    segments, lang, _total = fetch_kome(vid)
    return segments, lang, True, "estimated", "kome"


def fetch_with_args(api, vid: str, args):
    """fetch_one with the language/route options the CLI collected."""
    return fetch_one(api, vid, args.source, args.proxy,
                     languages=getattr(args, "languages", None),
                     translate_to=getattr(args, "translate_to", "en"),
                     allow_other_languages=getattr(args, "allow_other_languages", False))


# --- run ---------------------------------------------------------------------

BLOCK_ADVICE = (
    "\n!! YouTube is rate limiting this IP. Stopping so the rest stay retryable.\n"
    "   The allowance refills over hours, so waiting is what helps — --retry-after\n"
    "   parks the run and resumes. Switching networks (a phone hotspot) resets it;\n"
    "   a corporate VPN/proxy egresses from a datacenter range and is blocked\n"
    "   hardest, so drop it before retrying. Blocked videos are NOT recorded as\n"
    "   misses, so a plain rerun picks them up.\n"
)


def out_path(out_dir: Path, v: dict) -> Path:
    return out_dir / f"{v['video_id']}.json"


def save(out_dir: Path, v: dict, segments, lang, generated, timing, source) -> int:
    words = sum(len(s["text"].split()) for s in segments)
    rec = {
        "video_id": v["video_id"],
        "title": v.get("title", ""),
        "language": lang,
        "auto_generated": bool(generated),
        "source": source,
        "timing": timing,            # "exact" or "estimated"
        "word_count": words,
        "segments": segments,
    }
    # Carry through any id the caller keyed its own corpus by.
    for k in ("talk_id", "id", "url", "duration_s", "upload_date", "uploader"):
        if v.get(k) is not None and k not in rec:
            rec[k] = v[k]
    write_json(out_path(out_dir, v), rec)
    return words


def probe(api, args) -> int:
    """One request against a known-captioned video: is this network usable now?"""
    vid = args.probe_video
    print(f"probing {vid} via {args.source} …")
    try:
        segments, lang, _gen, timing, src = fetch_with_args(api, vid, args)
    except Exception as e:
        verdict = "BLOCKED — this IP's allowance is spent" if is_block(e) else \
                  f"failed: {type(e).__name__}: {str(e)[:160]}"
        print(f"  {verdict}")
        return 2 if is_block(e) else 1
    print(f"  ok — {len(segments)} segments, {lang}, {timing} via {src}. "
          f"This network is worth a run.")
    return 0


def run_serial(api, todo, misses, args, out_dir):
    ok = fail = 0
    blocked = False
    for i, v in enumerate(todo, 1):
        label = (v.get("title") or v["video_id"])[:52]
        try:
            segments, lang, generated, timing, source = fetch_with_args(
                api, v["video_id"], args)
            words = save(out_dir, v, segments, lang, generated, timing, source)
            ok += 1
            print(f"[{i}/{len(todo)}] ok   {words:>6,}w {source:<5} {timing:<9} {label}")
        except KeyboardInterrupt:
            print("\ninterrupted — progress is saved, rerun to continue")
            break
        except Exception as e:
            if is_block(e):
                print(f"[{i}/{len(todo)}] BLOCKED  {label}")
                print(BLOCK_ADVICE)
                blocked = True
                break
            fail += 1
            misses[v["video_id"]] = {"title": v.get("title", ""),
                                     "reason": type(e).__name__, "detail": str(e)[:200]}
            print(f"[{i}/{len(todo)}] MISS {type(e).__name__:<28} {label}")
        time.sleep(random.uniform(args.min_delay, args.max_delay))
    return ok, fail, blocked


def run_parallel(api, todo, misses, args, out_dir):
    """Threads spend nearly all their time waiting on the network.

    Each worker sleeps before its request, so the request rate is roughly
    workers / mean-delay. Pacing here is not optional: a parallel path without
    it is exactly how an IP gets blocked.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading

    blocked = threading.Event()
    ok = fail = 0
    done = 0          # real outcomes only — see the skip below

    def work(v):
        if blocked.is_set():
            raise BlockedError("skipped — run already stopped by a block")
        time.sleep(random.uniform(args.min_delay, args.max_delay))
        # Checked again after the pacing sleep: a worker that queued before the
        # block was seen would otherwise still put its request on the wire. This
        # closes all but the requests already in flight when the block landed.
        if blocked.is_set():
            raise BlockedError("skipped — run already stopped by a block")
        segments, lang, generated, timing, source = fetch_with_args(
            api, v["video_id"], args)
        return save(out_dir, v, segments, lang, generated, timing, source), timing, source

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(work, v): v for v in todo}
        try:
            # This loop is the only thread touching the counters, so no lock.
            for fut in as_completed(futures):
                v = futures[fut]
                label = (v.get("title") or v["video_id"])[:48]
                try:
                    words, timing, source = fut.result()
                except Exception as e:
                    if is_block(e):
                        # Says nothing about this video, so it is neither a miss
                        # nor an attempt — once blocked the rest of the round
                        # fails instantly, and counting those would race the
                        # progress number to the end while nothing was fetched.
                        if not blocked.is_set():
                            blocked.set()
                            print(BLOCK_ADVICE)
                        continue
                    done += 1
                    fail += 1
                    misses[v["video_id"]] = {"title": v.get("title", ""),
                                             "reason": type(e).__name__,
                                             "detail": str(e)[:200]}
                    print(f"[{done}/{len(todo)}] MISS {type(e).__name__:<24} {label}")
                    continue
                done += 1
                ok += 1
                print(f"[{done}/{len(todo)}] ok   {words:>6,}w {source:<5} {timing:<9} {label}")
        except KeyboardInterrupt:
            print("\ninterrupted — finished work is saved, rerun to continue")
            pool.shutdown(wait=False, cancel_futures=True)
            return ok, fail, False
    return ok, fail, blocked.is_set()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("videos", nargs="*", help="video ids or URLs")
    ap.add_argument("--from", dest="from_file", metavar="FILE",
                    help="videos.json from list_videos.py, a JSON array, or one id/URL per line")
    ap.add_argument("--playlist", help="enumerate this playlist/channel first")
    ap.add_argument("--out", default="transcripts", help="output directory (default: transcripts)")
    ap.add_argument("--source", choices=("auto", "exact", "youtube", "ytdlp", "kome"),
                    default="auto",
                    help="auto: exact timings if YouTube allows it, else kome.ai. "
                         "exact: routes 1-2 only, never fall back to estimates")
    ap.add_argument("--limit", type=int,
                    help="only attempt the first N videos (a trial run: this also "
                         "turns off the --retry-after rounds)")
    ap.add_argument("--languages", default=",".join(LANGUAGES), metavar="LIST",
                    help="caption languages to accept, best first (default: %(default)s)")
    ap.add_argument("--translate-to", default="en", metavar="LANG",
                    help="when no track is in a wanted language, have YouTube translate "
                         "one into this instead (default: en; empty disables)")
    ap.add_argument("--allow-other-languages", action="store_true",
                    help="last resort: accept a track in a language you did not ask "
                         "for and that cannot be translated. Off by default — a "
                         "mis-detected ASR track (English speech transcribed as Hindi) "
                         "is unusable for search and never gets re-fetched")
    ap.add_argument("--workers", type=int, default=2,
                    help="parallel fetches (default 2; 1 disables threading). "
                         "Requests are paced on every worker, so raising this "
                         "raises the request rate — which is what gets you blocked")
    ap.add_argument("--retry-misses", action="store_true")
    ap.add_argument("--proxy", help="http(s) proxy URL")
    ap.add_argument("--min-delay", type=float, default=3.0)
    ap.add_argument("--max-delay", type=float, default=7.0)
    ap.add_argument("--retry-after", type=float, default=0, metavar="MINUTES",
                    help="when YouTube blocks the IP, wait this long and resume where "
                         "it stopped. 0 (default) stops on the first block. The quota "
                         "refills with time, so a long wait finishes a corpus that no "
                         "single run can")
    ap.add_argument("--max-rounds", type=int, default=24,
                    help="give up after this many blocked rounds (default 24)")
    ap.add_argument("--probe", action="store_true",
                    help="fetch one known-captioned video and report whether this "
                         "network is usable right now, then exit")
    ap.add_argument("--probe-video", default="dQw4w9WgXcQ",
                    help="video id used by --probe")
    args = ap.parse_args()
    args.languages = [l.strip() for l in args.languages.split(",") if l.strip()] \
        or list(LANGUAGES)

    # Only route 1 needs the library, so --source kome / ytdlp must not require
    # it — those are the routes that still work where route 1 is refused.
    api = build_api(args.proxy) if args.source in ("auto", "exact", "youtube") else None

    if args.probe:
        sys.exit(probe(api, args))

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    misses_path = out_dir / "_misses.json"

    videos = load_work(args)
    if not videos:
        sys.exit("no videos to fetch — pass ids, --from FILE or --playlist URL")

    misses = {}
    if misses_path.exists() and not args.retry_misses:
        misses = json.loads(misses_path.read_text(encoding="utf-8"))

    total_ok = total_fail = 0

    # Each round re-derives its work from what is on disk, so a blocked round
    # costs nothing but time — nothing is lost and nothing is refetched.
    for rnd in range(1, args.max_rounds + 1):
        # Strikes are per round: three failures parked route 1 for the rest of
        # *that* round, but after a --retry-after wait the quota has recovered
        # and exact timings are worth trying again.
        _yt_strikes[0] = 0
        todo = [v for v in videos
                if not out_path(out_dir, v).exists() and v["video_id"] not in misses]
        have = sum(1 for v in videos if out_path(out_dir, v).exists())
        label = f"round {rnd}: " if rnd > 1 else ""
        print(f"{label}{len(videos)} videos · {have} already fetched · "
              f"{len(misses)} known misses · {len(todo)} to try\n")
        if not todo:
            break

        if args.limit:
            todo = todo[: args.limit]

        runner = run_parallel if args.workers > 1 else run_serial
        ok, fail, blocked = runner(api, todo, misses, args, out_dir)
        total_ok += ok
        total_fail += fail
        write_json(misses_path, misses)

        if not blocked or not args.retry_after:
            break
        if args.limit:
            print(f"--limit {args.limit} is a trial run, so stopping here instead of "
                  f"retrying: rerun without --limit to let --retry-after park and "
                  f"resume.", file=sys.stderr)
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

    write_json(misses_path, misses)
    print(f"\ndone: {total_ok} fetched, {total_fail} missed. "
          f"Misses recorded in {misses_path}")


if __name__ == "__main__":
    main()
