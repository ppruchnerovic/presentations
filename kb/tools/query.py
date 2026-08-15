#!/usr/bin/env python3
"""Search the talk knowledge base from the command line.

Two layers are searched and merged:
  * talk metadata + abstracts (always available)
  * transcript segments (only for talks whose transcript has been fetched),
    which also gives the timestamp — and a deep link — for each hit.

    python3 query.py "ai driven sdlc"
    python3 query.py "spec driven development" --moments
    python3 query.py "agents" --track "AI Agents" --type Keynote/Talk
    python3 query.py "code review" --json          # for scripts and agents

FTS5 syntax works: quoted "exact phrase", OR, NOT, prefix*.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys

import wadkb

# Transcript hits weigh more than abstracts: an abstract is marketing copy, the
# transcript is what the speaker actually said.
W_META = 1.0
W_SEG = 1.6


def fts_query(raw: str) -> str:
    """Pass FTS5 operators through, otherwise AND the bare words together."""
    if re.search(r'["*]|\b(OR|NOT|AND|NEAR)\b', raw):
        return raw
    words = [w for w in re.findall(r"[\w'+#.-]+", raw) if w]
    if not words:
        raise SystemExit("empty query")
    return " AND ".join(f'"{w}"' for w in words)


def search(con, q: str, limit: int, filters: dict) -> list[dict]:
    where, params = [], {"q": q}
    for col, val in filters.items():
        if val:
            where.append(f"t.{col} = :{col}")
            params[col] = val
    clause = (" AND " + " AND ".join(where)) if where else ""

    hits: dict[int, dict] = {}

    meta_sql = f"""
        SELECT t.id, bm25(talks_fts, 8.0, 2.0, 4.0, 3.0, 1.0, 2.0) AS rank,
               snippet(talks_fts, 1, '[[', ']]', ' … ', 24) AS snip
        FROM talks_fts JOIN talks t ON t.id = talks_fts.rowid
        WHERE talks_fts MATCH :q{clause}
        ORDER BY rank LIMIT 400
    """
    try:
        rows = con.execute(meta_sql, params).fetchall()
    except sqlite3.OperationalError as e:
        raise SystemExit(f"bad query: {e}")
    for tid, rank, snip in rows:
        hits[tid] = {"id": tid, "score": -rank * W_META, "abstract_snippet": snip, "moments": []}

    seg_sql = f"""
        SELECT s.talk_id, s.start, bm25(segments_fts) AS rank,
               snippet(segments_fts, 0, '[[', ']]', ' … ', 26) AS snip
        FROM segments_fts JOIN segments s ON s.rowid = segments_fts.rowid
        JOIN talks t ON t.id = s.talk_id
        WHERE segments_fts MATCH :q{clause}
        ORDER BY rank LIMIT 1500
    """
    try:
        seg_rows = con.execute(seg_sql, params).fetchall()
    except sqlite3.OperationalError:
        seg_rows = []

    for tid, start, rank, snip in seg_rows:
        h = hits.setdefault(tid, {"id": tid, "score": 0.0, "abstract_snippet": "", "moments": []})
        if len(h["moments"]) < 4:
            h["moments"].append({"start": start, "text": snip})
            h["score"] += -rank * W_SEG / (len(h["moments"]) ** 0.5)

    ranked = sorted(hits.values(), key=lambda h: -h["score"])[:limit]

    cols = ("id title track type stage tags speakers companies duration_min "
            "recording_url video_id session_page event_name has_transcript").split()
    for h in ranked:
        row = con.execute(f"SELECT {','.join(cols)} FROM talks WHERE id=?", (h["id"],)).fetchone()
        h.update(dict(zip(cols, row)))
    return ranked


def fmt_ts(sec: float) -> str:
    return f"{int(sec) // 60}:{int(sec) % 60:02d}"


def render(hits: list[dict], show_moments: bool) -> None:
    if not hits:
        print("no matches")
        return
    for i, h in enumerate(hits, 1):
        who = h["speakers"] or "—"
        if h["companies"]:
            who += f" ({h['companies']})"
        print(f"\n\033[1m{i}. {h['title']}\033[0m")
        print(f"   {who}")
        print(f"   {h['track']} · {h['type']} · {h['duration_min']}min"
              + ("  · transcript" if h["has_transcript"] else ""))
        if h["abstract_snippet"]:
            print(f"   \033[2m{clean_snip(h['abstract_snippet'])}\033[0m")
        if show_moments and h["moments"]:
            for m in h["moments"]:
                link = f"https://www.youtube.com/watch?v={h['video_id']}&t={int(m['start'])}s"
                print(f"   \033[36m{fmt_ts(m['start'])}\033[0m {clean_snip(m['text'])}")
                print(f"        {link}")
        print(f"   {h['recording_url']}")


def clean_snip(s: str) -> str:
    return " ".join((s or "").split()).replace("[[", "\033[33m").replace("]]", "\033[0m")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="+")
    ap.add_argument("-n", "--limit", type=int, default=10)
    ap.add_argument("--track")
    ap.add_argument("--type", dest="type_")
    ap.add_argument("--stage")
    ap.add_argument("--event", dest="event_slug")
    ap.add_argument("--no-moments", dest="moments", action="store_false",
                    help="hide the timestamped transcript hits")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not wadkb.TALKS_DB.exists():
        # The index is derived and not committed, so build it on first use.
        print("building the search index (one-off)…", file=sys.stderr)
        import build_index

        build_index.main()

    con = sqlite3.connect(f"file:{wadkb.TALKS_DB}?mode=ro", uri=True)
    q = fts_query(" ".join(args.query))
    hits = search(con, q, args.limit, {
        "track": args.track, "type": args.type_,
        "stage": args.stage, "event_slug": args.event_slug,
    })

    if args.json:
        for h in hits:
            h["tags"] = [x for x in (h["tags"] or "").split(", ") if x]
            h["abstract_snippet"] = " ".join((h["abstract_snippet"] or "").split())
        json.dump(hits, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        render(hits, args.moments)


if __name__ == "__main__":
    main()
