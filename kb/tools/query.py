#!/usr/bin/env python3
"""Search the talk knowledge base from the command line.

Two layers are searched and merged:
  * talk metadata + abstracts (always available)
  * transcript segments (only for talks whose transcript has been fetched),
    which also gives the timestamp — and a deep link — for each hit.

    python3 query.py "ai driven sdlc"
    python3 query.py "spec driven development" -n 20
    python3 query.py "agents" --track "AI Agents" --type Keynote/Talk
    python3 query.py "code review" --no-moments    # just the talks, no timestamps
    python3 query.py "code review" --json          # for scripts and agents
    python3 query.py "code review" --json --brief  # the same choice, a third of the bytes
    python3 query.py "code review" --ids | xargs python3 excerpt.py -q "code review"

Flags: -n/--limit, --track, --type, --stage, --event, --no-moments, --json,
--brief, --ids.
Facet values are matched exactly and case-sensitively; a value the corpus does
not have is an error that lists the ones it does.

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

# A real query is a handful of words. Past this it is a paste or a generated
# string, and ANDing thousands of terms together costs FTS5 minutes.
MAX_TERMS = 32

# How many rows each layer pulls before ranking. Both scale with -n so a large
# limit is honoured rather than silently truncated; the floors keep an ordinary
# search cheap. Metadata has one row per talk, so its floor already covers the
# whole corpus; a talk keeps at most 4 moments, hence the segment multiplier.
META_ROWS = 400
SEG_ROWS = 1500
SEG_PER_HIT = 50


# A query that names its own operators is passed through untouched — it says
# what it wants, so it is neither rewritten nor relaxed.
EXPLICIT_RE = re.compile(r'["*]|\b(OR|NOT|AND|NEAR)\b')


def query_words(raw: str, warn: bool = True) -> list[str]:
    """The bare words of a query, de-duplicated and capped."""
    words, seen = [], set()
    for w in re.findall(r"[\w'+#.-]+", raw):
        if w.lower() not in seen:  # repeating a term only makes FTS5 work harder
            seen.add(w.lower())
            words.append(w)
    if not words:
        raise SystemExit("empty query")
    if len(words) > MAX_TERMS:
        if warn:  # the second caller of the same query would say it twice
            print(f"query has {len(words)} terms — searching the first {MAX_TERMS}",
                  file=sys.stderr)
        words = words[:MAX_TERMS]
    return words


def fts_query(raw: str) -> str:
    """Pass FTS5 operators through, otherwise AND the bare words together."""
    if EXPLICIT_RE.search(raw):
        return raw
    return " AND ".join(f'"{w}"' for w in query_words(raw))


def relaxed_query(raw: str) -> str | None:
    """The same query as an OR of its content words, or None if it must not be
    relaxed.

    ANDing is right for ranking *talks*: every term has to appear somewhere in
    the record. Inside a single ~28-word segment it is nearly always too
    strict — "eval driven development" is spoken across two of them — so a
    caller that matches segments within one talk (`excerpt.py`) needs a
    fallback, or it finds nothing and concludes the talk never says it. Still
    ranked by bm25, so the passage carrying more of the terms still wins.
    """
    if EXPLICIT_RE.search(raw):
        return None
    words = query_words(raw, warn=False)
    if len(words) < 2:  # one word cannot be relaxed into anything but itself
        return None
    content = [w for w in words if w.lower() not in wadkb.STOPWORDS] or words
    return " OR ".join(f'"{w}"' for w in content)


def search(con, q: str, limit: int, filters: dict) -> list[dict]:
    where, params = [], {"q": q}
    for col, val in filters.items():
        if val:
            where.append(f"t.{col} = :{col}")
            params[col] = val
    clause = (" AND " + " AND ".join(where)) if where else ""
    params["meta_cap"] = max(META_ROWS, limit)
    params["seg_cap"] = seg_cap = max(SEG_ROWS, limit * SEG_PER_HIT)

    hits: dict[int, dict] = {}

    meta_sql = f"""
        SELECT t.id, bm25(talks_fts, 8.0, 2.0, 4.0, 3.0, 1.0, 2.0) AS rank,
               snippet(talks_fts, 1, '[[', ']]', ' … ', 24) AS snip
        FROM talks_fts JOIN talks t ON t.id = talks_fts.rowid
        WHERE talks_fts MATCH :q{clause}
        ORDER BY rank LIMIT :meta_cap
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
        ORDER BY rank LIMIT :seg_cap
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
    if len(seg_rows) >= seg_cap and len(ranked) < limit:
        # Only worth saying when it cost the caller results they asked for.
        print(f"note: stopped after {seg_cap} transcript hits — talks that match only "
              f"further down are missing", file=sys.stderr)

    cols = ("id title track type stage tags speakers companies duration_min "
            "recording_url video_id session_page event_name has_transcript").split()
    for h in ranked:
        row = con.execute(f"SELECT {','.join(cols)} FROM talks WHERE id=?", (h["id"],)).fetchone()
        h.update(dict(zip(cols, row)))
    return ranked


def fmt_ts(sec: float) -> str:
    s = int(sec)
    if s >= 3600:
        return f"{s // 3600}:{s // 60 % 60:02d}:{s % 60:02d}"
    return f"{s // 60}:{s % 60:02d}"


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


def plain_snip(s: str) -> str:
    """Same text without the [[…]] hit markers — a JSON consumer wants the
    sentence, not the terminal's highlighting."""
    return " ".join((s or "").split()).replace("[[", "").replace("]]", "")


# What --brief keeps. Choosing *which* talks to open needs different fields
# from reading one: the tags, the companies, the stage, the type and the
# session page are all one lookup by id away, and across a dozen hits they are
# most of the bytes and none of the decision.
BRIEF = ("id score title speakers track duration_min recording_url video_id "
         "event_name has_transcript abstract_snippet").split()

# Moments kept per hit under --brief. One passage says whether the talk is
# about the query; the fourth says it again.
BRIEF_MOMENTS = 2


def emit_json(hits: list[dict], show_moments: bool, brief: bool = False) -> None:
    """The default shape is a contract — `uitest/suite-ranking.js` compares its
    own ranking against it — so --brief subsets that shape rather than
    reshaping it."""
    for h in hits:
        h["tags"] = [x for x in (h["tags"] or "").split(", ") if x]
        h["abstract_snippet"] = plain_snip(h["abstract_snippet"])
        h["moments"] = ([{"start": m["start"], "text": plain_snip(m["text"])}
                         for m in h["moments"]] if show_moments else [])
    if brief:
        hits = [{**{k: h[k] for k in BRIEF if k in h},
                 "moments": h["moments"][:BRIEF_MOMENTS]} for h in hits]
    json.dump(hits, sys.stdout, ensure_ascii=False, indent=None if brief else 2)
    print()


def positive_int(value: str) -> int:
    """A limit of 0 or less is never what was meant: 0 looked like 'no matches'
    and a negative one sliced results off the tail."""
    try:
        n = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"invalid int value: {value!r}")
    if n < 1:
        raise argparse.ArgumentTypeError(f"must be 1 or more, got {n}")
    return n


def check_facet(con, col: str, val: str | None, flag: str) -> None:
    """Filters are exact and case-sensitive, so a typo is indistinguishable from
    an honest miss — reject it and show what the corpus actually has."""
    if not val:
        return
    valid = [r[0] for r in con.execute(
        f"SELECT DISTINCT {col} FROM talks WHERE {col} <> '' ORDER BY {col}")]
    if val not in valid:
        shown = ", ".join(valid[:12])
        if len(valid) > 12:
            shown += f", … ({len(valid)} in all)"
        raise SystemExit(f"unknown {flag} {val!r} — values are exact and case-sensitive\n"
                         f"  valid: {shown}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="+")
    ap.add_argument("-n", "--limit", type=positive_int, default=10)
    ap.add_argument("--track")
    ap.add_argument("--type", dest="type_")
    ap.add_argument("--stage")
    ap.add_argument("--event", dest="event_slug")
    ap.add_argument("--no-moments", dest="moments", action="store_false",
                    help="hide the timestamped transcript hits")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--brief", action="store_true",
                    help="only the fields and passages needed to choose a talk")
    ap.add_argument("--ids", action="store_true",
                    help="print only the talk ids, one per line — feeds excerpt.py")
    args = ap.parse_args()

    if not wadkb.TALKS_DB.exists():
        # The index is derived and not committed, so build it on first use.
        print("building the search index (one-off)…", file=sys.stderr)
        import build_index

        build_index.main()

    con = sqlite3.connect(f"file:{wadkb.TALKS_DB}?mode=ro", uri=True)
    check_facet(con, "track", args.track, "--track")
    check_facet(con, "type", args.type_, "--type")
    check_facet(con, "stage", args.stage, "--stage")
    check_facet(con, "event_slug", args.event_slug, "--event")

    q = fts_query(" ".join(args.query))
    hits = search(con, q, args.limit, {
        "track": args.track, "type": args.type_,
        "stage": args.stage, "event_slug": args.event_slug,
    })

    if args.ids:
        # So that reading the hits is a pipe rather than eight ids retyped:
        #   query.py "…" --ids | xargs python3 excerpt.py -q "…"
        for h in hits:
            print(h["id"])
    elif args.json:
        emit_json(hits, args.moments, args.brief)
    else:
        render(hits, args.moments and not args.brief)


if __name__ == "__main__":
    main()
