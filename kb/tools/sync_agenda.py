#!/usr/bin/env python3
"""Sync the WeAreDevelopers agenda into the knowledge base.

Pulls the public event API (no auth needed) and writes:

  data/talks.json          canonical corpus, one record per talk WITH a recording
  data/talks.csv           spreadsheet view
  talks/<event>/<id>-<slug>.md   one readable markdown file per talk

Idempotent: re-running produces the same output, so the git diff shows exactly
what the conference changed.

    python3 sync_agenda.py                 # all events in wadkb.EVENTS
    python3 sync_agenda.py --event-id 16
    python3 sync_agenda.py --keep-all      # include talks without a recording
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import shutil
import sys
import urllib.request

import wadkb
from wadkb import EVENTS


def fetch_event(event_id: int) -> dict:
    url = wadkb.API_EVENT.format(event_id=event_id)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)["data"]


# Characters the event API leaks into otherwise fine text. They are invisible
# in the CMS preview, so nobody upstream ever sees them, but they reach every
# artefact we publish. The rule below is deliberately narrow: scrub what renders
# as nothing, keep what renders as a glyph. Accented and non-Latin speaker names,
# typographic quotes, en/em/non-breaking dashes, NBSP and emoji (including the
# U+FE0F variation selector) are legitimate corpus content and must survive.
SCRUB = {
    # Zero-width. Seen as a BOM glued to the front of a speaker bio, where it
    # corrupts the first token for every downstream tokenizer and sort.
    0xFEFF: None,  # ZERO WIDTH NO-BREAK SPACE / BOM
    0x200B: None,  # ZERO WIDTH SPACE
    0x2060: None,  # WORD JOINER (U+FEFF's modern stand-in, same noise)
    # Unicode line/paragraph separators. Pasted in where a blank line belongs:
    # they render as a hard break with no space, and JS treats them as real line
    # terminators, so they would break search-meta.json the day it gets inlined
    # into a <script> block. "\n\n" is the paragraph break the API otherwise
    # sends and the one the markdown template expects.
    0x2028: "\n\n",  # LINE SEPARATOR
    0x2029: "\n\n",  # PARAGRAPH SEPARATOR
    # Lone CR (old-Mac line ending); CRLF is folded just below.
    0x0D: "\n",
}
# Stray C0/C1 controls, minus the whitespace we handle on purpose.
SCRUB.update({c: None for c in range(0x00, 0x20) if c not in (0x09, 0x0A, 0x0D)})
SCRUB.update({c: None for c in range(0x7F, 0xA0)})


def clean(text: str | None) -> str:
    if not text:
        return ""
    text = text.replace("\r\n", "\n").translate(SCRUB)
    return "\n".join(line.rstrip() for line in text.split("\n")).strip()


def build_speaker(sp: dict) -> dict:
    links = {
        k: sp.get(f"link_{k}")
        for k in ("linkedin", "twitter", "github", "website")
        if sp.get(f"link_{k}")
    }
    return {
        "id": sp.get("id"),
        "name": sp.get("full_name"),
        "company": sp.get("company_name"),
        "position": sp.get("company_position"),
        "bio": clean(sp.get("bio")),
        "image": sp.get("image_url"),
        "links": links,
    }


def duration_minutes(s: dict) -> int | None:
    a, b = s.get("starts_at_timestamp"), s.get("ends_at_timestamp")
    if not a or not b:
        return None
    return int((b - a) / 60000)


def build_talk(s: dict, event: dict, event_id: int, types: dict) -> dict:
    rec = s.get("recording_url")
    return {
        "id": s["id"],
        "slug": wadkb.slugify(s.get("title") or ""),
        "title": clean(s.get("title")),
        "description": clean(s.get("description")),
        "track": (s.get("track") or {}).get("name"),
        "type": types.get(s.get("session_type")),
        "stage": (s.get("stage") or {}).get("as_string"),
        "tags": s.get("tags") or [],
        "speakers": [build_speaker(sp) for sp in s.get("speakers", []) if isinstance(sp, dict)],
        "day": s.get("event_day"),
        "starts_at": s.get("starts_at"),
        "ends_at": s.get("ends_at"),
        "duration_min": duration_minutes(s),
        "recording_url": rec,
        "video_id": wadkb.video_id(rec),
        "live_url": s.get("live_url"),
        "session_page": wadkb.SESSION_PAGE.format(event_id=event_id, session_id=s["id"]),
        "is_workshop": bool(s.get("is_workshop")),
        "event_id": event_id,
        "event_name": event.get("name"),
        "event_slug": EVENTS.get(event_id, wadkb.slugify(event.get("name", ""))),
    }


MD_TEMPLATE = """---
id: {id}
title: {title_q}
slug: {slug}
event: {event_name_q}
event_slug: {event_slug}
track: {track_q}
type: {type_q}
stage: {stage_q}
tags: {tags_json}
speakers: {speaker_names_json}
speaker_companies: {speaker_companies_json}
day: {day}
starts_at: {starts_at}
duration_min: {duration_min}
recording_url: {recording_url}
video_id: {video_id}
session_page: {session_page}
transcript: {has_transcript}
---

# {title}

**{speaker_line}**

`Track: {track}` · `Type: {type}` · `Stage: {stage}`{tag_line}

[Watch the recording]({recording_url}) · [Session page]({session_page})

## Abstract

{description}
{speaker_block}{transcript_block}"""


def speaker_line(t: dict) -> str:
    parts = []
    for sp in t["speakers"]:
        bit = sp["name"] or ""
        role = " — ".join(x for x in (sp.get("position"), sp.get("company")) if x)
        if role:
            bit += f" ({role})"
        parts.append(bit)
    return ", ".join(parts) if parts else "No speaker listed"


def speaker_block(t: dict) -> str:
    if not any(sp.get("bio") for sp in t["speakers"]):
        return ""
    out = ["\n## Speakers\n"]
    for sp in t["speakers"]:
        head = sp["name"] or "Unknown"
        role = " — ".join(x for x in (sp.get("position"), sp.get("company")) if x)
        out.append(f"### {head}" + (f"\n\n*{role}*" if role else ""))
        if sp.get("bio"):
            out.append(f"\n{sp['bio']}")
        if sp.get("links"):
            out.append("\n" + " · ".join(f"[{k}]({v})" for k, v in sp["links"].items()))
        out.append("")
    return "\n".join(out)


def transcript_block(t: dict) -> str:
    tr = wadkb.load_transcript(t["id"])
    if not tr or not tr.get("segments"):
        return ""
    vid = t.get("video_id")
    lines = ["\n## Transcript\n"]
    lines.append(
        f"*{tr.get('word_count', 0):,} words · source: {tr.get('source', 'youtube')} "
        f"({tr.get('language', 'en')})*\n"
    )
    # Group segments into ~45s paragraphs so the text reads naturally and each
    # paragraph carries a deep link back into the video.
    bucket, bucket_start = [], None
    for seg in tr["segments"]:
        if bucket_start is None:
            bucket_start = seg["start"]
        bucket.append(seg["text"])
        if seg["start"] - bucket_start >= 45:
            lines.append(_para(bucket, bucket_start, vid))
            bucket, bucket_start = [], None
    if bucket:
        lines.append(_para(bucket, bucket_start or 0, vid))
    return "\n".join(lines)


def _para(texts: list[str], start: float, vid: str | None) -> str:
    body = " ".join(" ".join(texts).split())
    ts = f"{int(start)//60:d}:{int(start)%60:02d}"
    if vid:
        return f"**[{ts}](https://www.youtube.com/watch?v={vid}&t={int(start)}s)** {body}\n"
    return f"**{ts}** {body}\n"


def yaml_q(s: str | None) -> str:
    """Quote a YAML scalar safely."""
    if s is None:
        return "null"
    return json.dumps(s, ensure_ascii=False)


def render_md(t: dict) -> str:
    tags = t["tags"]
    return MD_TEMPLATE.format(
        id=t["id"],
        title=t["title"],
        title_q=yaml_q(t["title"]),
        slug=t["slug"],
        event_name_q=yaml_q(t["event_name"]),
        event_slug=t["event_slug"],
        track=t["track"] or "—",
        track_q=yaml_q(t["track"]),
        type=t["type"] or "—",
        type_q=yaml_q(t["type"]),
        stage=t["stage"] or "—",
        stage_q=yaml_q(t["stage"]),
        tags_json=json.dumps(tags, ensure_ascii=False),
        tag_line=("\n\n" + " ".join(f"`#{x}`" for x in tags)) if tags else "",
        speaker_names_json=json.dumps([sp["name"] for sp in t["speakers"]], ensure_ascii=False),
        speaker_companies_json=json.dumps(
            sorted({sp["company"] for sp in t["speakers"] if sp.get("company")}), ensure_ascii=False
        ),
        speaker_line=speaker_line(t),
        day=t["day"],
        starts_at=t["starts_at"],
        duration_min=t["duration_min"],
        recording_url=t["recording_url"],
        video_id=t["video_id"],
        session_page=t["session_page"],
        has_transcript=str(wadkb.transcript_path(t["id"]).exists()).lower(),
        description=t["description"] or "*No abstract published.*",
        speaker_block=speaker_block(t),
        transcript_block=transcript_block(t),
    )


CSV_FIELDS = [
    "id", "title", "track", "type", "stage", "tags", "speakers", "companies",
    "day", "starts_at", "duration_min", "recording_url", "session_page",
    "event_name", "description",
]


def csv_row(t: dict) -> dict:
    return {
        "id": t["id"],
        "title": t["title"],
        "track": t["track"],
        "type": t["type"],
        "stage": t["stage"],
        "tags": ", ".join(t["tags"]),
        "speakers": ", ".join(sp["name"] or "" for sp in t["speakers"]),
        "companies": ", ".join(sorted({sp["company"] for sp in t["speakers"] if sp.get("company")})),
        "day": t["day"],
        "starts_at": t["starts_at"],
        "duration_min": t["duration_min"],
        "recording_url": t["recording_url"],
        "session_page": t["session_page"],
        "event_name": t["event_name"],
        "description": t["description"],
    }


def check_not_shrinking(n_new: int, allow_shrink: bool) -> None:
    """Refuse to publish a corpus that suddenly lost most of its talks.

    This runs unattended: kb-refresh.yml commits whatever comes out and force
    pushes it to gh-pages. A 200 response is not the same as a good one — the
    conference is over, so the agenda can be edited or served without
    `recording_url` at any time, and every talk missing one is silently skipped.
    That path was measured, not imagined: stripping `recording_url` leaves 0
    talks, deletes all 358 markdown files and empties the index, and nothing in
    the pipeline exits non-zero. Transcripts survive (nothing here writes to
    data/transcripts), so the damage is recoverable with a revert — but only
    after the live search has been serving an empty corpus.

    Growth is fine; a sharp drop means the API, not the conference.
    """
    if allow_shrink or not wadkb.TALKS_JSON.exists():
        return
    try:
        with wadkb.TALKS_JSON.open(encoding="utf-8") as f:
            n_old = int(json.load(f).get("count") or 0)
    except (OSError, ValueError, TypeError):
        return
    if not n_old or n_new >= n_old * 0.9:
        return
    sys.exit(
        f"\nrefusing to overwrite: the API returned {n_new} talks with recordings, "
        f"down from {n_old}.\nNothing was written — talks.json, the markdown and the "
        f"index are untouched.\nIf the drop is real, rerun with --allow-shrink."
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--event-id", type=int, action="append", dest="event_ids")
    ap.add_argument("--keep-all", action="store_true", help="include talks without a recording")
    ap.add_argument("--allow-shrink", action="store_true",
                    help="write even if the API returned far fewer talks than last time")
    args = ap.parse_args()

    event_ids = args.event_ids or sorted(EVENTS)
    talks: list[dict] = []
    skipped = 0

    for eid in event_ids:
        event = fetch_event(eid)
        types = {t["id"]: t["name"] for t in event.get("session_types", [])}
        for s in event.get("sessions", []):
            if not args.keep_all and not s.get("recording_url"):
                skipped += 1
                continue
            talks.append(build_talk(s, event, eid, types))
        print(f"  {event.get('name')} (event {eid}): {len(event.get('sessions', []))} sessions")

    talks.sort(key=lambda t: (t["event_id"], t["starts_at"] or "", t["id"]))
    check_not_shrinking(len(talks), args.allow_shrink)

    wadkb.write_json(
        wadkb.TALKS_JSON,
        {
            "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
            "source": "https://wad-api.wearedevelopers.com/api/v2/events/<id> (public, no auth)",
            "events": [{"id": e, "slug": EVENTS.get(e)} for e in event_ids],
            "count": len(talks),
            "talks": talks,
        },
    )

    wadkb.TALKS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with wadkb.TALKS_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        for t in talks:
            w.writerow(csv_row(t))

    # Rebuild markdown from scratch so renamed/removed talks don't linger.
    if wadkb.TALKS_MD.exists():
        shutil.rmtree(wadkb.TALKS_MD)
    n_tr = 0
    for t in talks:
        d = wadkb.TALKS_MD / t["event_slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{t['id']}-{t['slug']}.md").write_text(render_md(t), encoding="utf-8")
        if wadkb.transcript_path(t["id"]).exists():
            n_tr += 1

    print(f"\n{len(talks)} talks with recordings written ({skipped} without a recording skipped)")
    print(f"  {wadkb.TALKS_JSON.relative_to(wadkb.KB_ROOT)}")
    print(f"  {wadkb.TALKS_CSV.relative_to(wadkb.KB_ROOT)}")
    print(f"  {wadkb.TALKS_MD.relative_to(wadkb.KB_ROOT)}/  ({n_tr} with transcripts inlined)")


if __name__ == "__main__":
    main()
