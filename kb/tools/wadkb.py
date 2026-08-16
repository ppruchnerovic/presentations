"""Shared helpers for the WeAreDevelopers talk knowledge base.

Paths are all resolved relative to the `kb/` directory so the tools can be run
from anywhere.
"""

from __future__ import annotations

import json
import pathlib
import re
import unicodedata

KB_ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = KB_ROOT / "data"
TALKS_MD = KB_ROOT / "talks"
TRANSCRIPTS = DATA / "transcripts"
TINDEX = DATA / "tindex"

TALKS_JSON = DATA / "talks.json"
TALKS_CSV = DATA / "talks.csv"
SEARCH_META = DATA / "search-meta.json"
TALKS_DB = DATA / "talks.db"

API_EVENT = "https://wad-api.wearedevelopers.com/api/v2/events/{event_id}"
API_EVENTS = "https://wad-api.wearedevelopers.com/api/v2/events"
SESSION_PAGE = "https://app.wearedevelopers.com/events/{event_id}/session/{session_id}"

# Events tracked by the knowledge base. Add new ones here; the corpus is shared
# so a query can compare what speakers said across years.
EVENTS = {
    16: "wwc-2026-berlin",
}

STOPWORDS = set(
    """a about above after again against all am an and any are aren as at be because been
before being below between both but by can cannot could couldn did didn do does doesn doing
don down during each few for from further had hadn has hasn have haven having he her here
hers herself him himself his how i if in into is isn it its itself just me more most mustn my
myself no nor not now of off on once only or other ought our ours ourselves out over own re
s same shan she should shouldn so some such t than that the their theirs them themselves then
there these they this those through to too under until up ve very was wasn we were weren what
when where which while who whom why will with won would wouldn you your yours yourself
yourselves ll m d o y ain aren couldn didn doesn hadn hasn haven isn ma mightn mustn needn
shan shouldn wasn weren won wouldn also get got going like make makes really thing things way
ways lot lots kind sort going gonna yeah okay ok right well actually basically just even
""".split()
)


def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text or "")
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rsplit("-", 1)[0]
    return text or "untitled"


VIDEO_ID_RE = re.compile(r"(?:v=|youtu\.be/|/embed/|/live/)([A-Za-z0-9_-]{11})")


def video_id(url: str | None) -> str | None:
    if not url:
        return None
    m = VIDEO_ID_RE.search(url)
    return m.group(1) if m else None


TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9+#.\-]*")


def tokenize(text: str) -> list[str]:
    """Lowercase word tokens, stopwords dropped, short junk dropped.

    Keeps things like `c++`, `ci/cd` halves, `gpt-4`, `.net` reasonably intact.
    """
    out = []
    for t in TOKEN_RE.findall((text or "").lower()):
        t = t.strip(".-")
        if len(t) < 2 or t in STOPWORDS:
            continue
        out.append(t)
        # Also index the parts of a compound, so "spec driven" finds
        # "spec-driven" and "ai assisted" finds "ai-assisted".
        if "-" in t or "." in t:
            for part in re.split(r"[.\-]+", t):
                if len(part) >= 2 and part not in STOPWORDS and part != t:
                    out.append(part)
    return out


def load_talks() -> list[dict]:
    if not TALKS_JSON.exists():
        raise SystemExit(f"{TALKS_JSON} not found — run sync_agenda.py first")
    with TALKS_JSON.open(encoding="utf-8") as f:
        return json.load(f)["talks"]


def transcript_path(talk_id: int) -> pathlib.Path:
    return TRANSCRIPTS / f"{talk_id}.json"


def load_transcript(talk_id: int) -> dict | None:
    p = transcript_path(talk_id)
    if not p.exists():
        return None
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def write_json(path: pathlib.Path, obj, compact: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        if compact:
            json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
        else:
            json.dump(obj, f, ensure_ascii=False, indent=2)
            f.write("\n")


def human_size(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1024.0
    return f"{n:.1f}GB"
