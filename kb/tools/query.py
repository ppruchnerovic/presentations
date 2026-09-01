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
    python3 query.py --facets                      # every track / type / stage, with counts

Flags: -n/--limit, --track, --type, --stage, --event, --no-moments, --json,
--brief, --ids, --facets.
Facet values are matched exactly and case-sensitively; a value the corpus does
not have is an error that lists the ones it does — `--facets` lists them all.

A bare query is ANDed: every content word has to appear in the record.
Stopwords are dropped first, so "what do speakers think about vibe coding"
searches for "speakers think vibe coding" rather than for nothing; hyphens and
slashes split, so "AI-driven" is "ai" AND "driven", the same as with a space.
When the strict AND finds fewer than -n talks, the rest of the list is filled
from an OR of the same words, appended after the strict hits and marked
`relaxed` — the strict order never changes, only the tail of a short list.

FTS5 syntax works: quoted "exact phrase", OR, NOT, prefix*. A query that uses
it is passed through as written, neither rewritten nor relaxed.
"""

from __future__ import annotations

import argparse
import json
import os
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


# Bare words are split on the punctuation FTS5's tokenizer splits on anyway.
# Kept whole and quoted, "AI-driven" was the *phrase* "ai driven" — adjacent
# words — while "ai driven" was "ai" AND "driven", anywhere in the record; a
# hyphen made the query stricter than a space. Split, the two are the same.
SPLIT_RE = re.compile(r"[-/.]+")


def query_words(raw: str, warn: bool = True) -> list[str]:
    """The bare words of a query, split on hyphens, de-duplicated and capped."""
    words, seen = [], set()
    for chunk in re.findall(r"[\w'+#.\-/]+", raw):
        for w in SPLIT_RE.split(chunk):
            if w and w.lower() not in seen:  # repeating a term only makes FTS5 work harder
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


def content_words(raw: str, warn: bool = True) -> list[str]:
    """`query_words` minus stopwords — unless that leaves nothing, in which
    case the stopwords are the query and they stay.

    A question carries its own scaffolding ("what do speakers think about")
    and ANDing that with the topic words matched no record at all. Dropping it
    is what turns a question into the search its asker meant.
    """
    words = query_words(raw, warn)
    return [w for w in words if w.lower() not in wadkb.STOPWORDS] or words


def fts_query(raw: str) -> str:
    """Pass FTS5 operators through, otherwise AND the content words together."""
    if EXPLICIT_RE.search(raw):
        return raw
    return " AND ".join(f'"{w}"' for w in content_words(raw))


def relaxed_query(raw: str) -> str | None:
    """The same query as an OR of its content words, or None if it must not be
    relaxed.

    ANDing is right for ranking *talks*: every term has to appear somewhere in
    the record. Inside a single ~28-word segment it is nearly always too
    strict — "eval driven development" is spoken across two of them — so a
    caller that matches segments within one talk (`excerpt.py`) needs a
    fallback, or it finds nothing and concludes the talk never says it. The
    same fallback fills the tail of a short result list in `search()`. Still
    ranked by bm25, so the record carrying more of the terms still wins.
    """
    if EXPLICIT_RE.search(raw):
        return None
    words = query_words(raw, warn=False)
    if len(words) < 2:  # one word cannot be relaxed into anything but itself
        return None
    content = [w for w in words if w.lower() not in wadkb.STOPWORDS] or words
    if len(content) < 2:
        return None
    return " OR ".join(f'"{w}"' for w in content)


def layer_hits(con, q: str, limit: int, filters: dict) -> tuple[list[dict], bool]:
    """Every talk matching `q` in either layer, best first, before the cut.

    Returns the ranked hits and whether the transcript layer was truncated at
    its row cap — the caller only says so if it cost results asked for.
    """
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

    ranked = sorted(hits.values(), key=lambda h: -h["score"])
    return ranked, len(seg_rows) >= seg_cap


def fill_relaxed(strict: list[dict], relaxed: list[dict], limit: int) -> list[dict]:
    """Top up a short strict list from the relaxed one — appended, never
    interleaved, and flagged.

    A relaxed hit matched *some* of the words; a strict hit matched all of
    them, and outranks it however the scores compare. Keeping the strict order
    intact is what lets the browser's ranking be measured against this one.
    """
    out = [{**h, "relaxed": False} for h in strict[:limit]]
    have = {h["id"] for h in out}
    for h in relaxed:
        if len(out) >= limit:
            break
        if h["id"] not in have:
            have.add(h["id"])
            out.append({**h, "relaxed": True})
    return out


def search(con, q: str, limit: int, filters: dict, relaxed: str | None = None) -> list[dict]:
    strict, truncated = layer_hits(con, q, limit, filters)
    extra = layer_hits(con, relaxed, limit, filters)[0] if relaxed and len(strict) < limit else []
    ranked = fill_relaxed(strict, extra, limit)
    if truncated and len(strict) < limit:
        # Only worth saying when it cost the caller results they asked for.
        print(f"note: stopped after {max(SEG_ROWS, limit * SEG_PER_HIT)} transcript hits — "
              f"talks that match only further down are missing", file=sys.stderr)

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


# Escape codes only when a person is looking. Piped into a file or an agent,
# every title and every highlighted word used to arrive wrapped in \033[…],
# so the [[…]] hit markers are printed as they are instead.
COLOR = sys.stdout.isatty() and not os.environ.get("NO_COLOR")


def paint(s: str, code: str) -> str:
    return f"\033[{code}m{s}\033[0m" if COLOR else s


def render(hits: list[dict], show_moments: bool, brief: bool = False) -> None:
    if not hits:
        print("no matches")
        return
    for i, h in enumerate(hits, 1):
        who = h["speakers"] or "—"
        if h["companies"]:
            who += f" ({h['companies']})"
        tag = "  (relaxed)" if h.get("relaxed") else ""
        print("\n" + paint(f"{i}. {h['title']}", "1") + tag)
        print(f"   {who}")
        print(f"   {h['track']} · {h['type']} · {h['duration_min']}min"
              + ("  · transcript" if h["has_transcript"] else ""))
        if h["abstract_snippet"]:
            print(f"   {paint(clean_snip(h['abstract_snippet']), '2')}")
        moments = h["moments"][:BRIEF_MOMENTS] if brief else h["moments"]
        if show_moments and moments:
            for m in moments:
                link = f"https://www.youtube.com/watch?v={h['video_id']}&t={int(m['start'])}s"
                print(f"   {paint(fmt_ts(m['start']), '36')} {clean_snip(m['text'])}")
                print(f"        {link}")
        print(f"   {h['recording_url']}")


def clean_snip(s: str) -> str:
    s = " ".join((s or "").split())
    return s.replace("[[", "\033[33m").replace("]]", "\033[0m") if COLOR else s


def plain_snip(s: str) -> str:
    """Same text without the [[…]] hit markers — a JSON consumer wants the
    sentence, not the terminal's highlighting."""
    return " ".join((s or "").split()).replace("[[", "").replace("]]", "")


# What --brief keeps. Choosing *which* talks to open needs different fields
# from reading one: the tags, the companies, the stage, the type and the
# session page are all one lookup by id away, and across a dozen hits they are
# most of the bytes and none of the decision.
BRIEF = ("id score relaxed title speakers track duration_min recording_url video_id "
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
                         f"  valid: {shown}\n  (query.py --facets lists them all, with counts)")


FACETS = (("track", "--track"), ("type", "--type"), ("stage", "--stage"),
          ("event_slug", "--event"))


def facets(con) -> dict[str, list[tuple[str, int]]]:
    """Every value each filter accepts, with how many talks carry it.

    The filters are exact and case-sensitive, and until this existed the only
    way to learn the spelling of a track was to pass a wrong one.
    """
    return {col: con.execute(
        f"SELECT COALESCE(NULLIF({col}, ''), '(none)'), COUNT(*) FROM talks "
        f"GROUP BY 1 ORDER BY 2 DESC, 1").fetchall() for col, _ in FACETS}


def render_facets(fac: dict) -> None:
    for col, flag in FACETS:
        rows = fac[col]
        print(f"{paint(flag, '1')}  ({len(rows)} values)")
        for val, n in rows:
            print(f"  {n:4d}  {val}")
        print()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="*")
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
    ap.add_argument("--facets", action="store_true",
                    help="list every track, type, stage and event with counts, then exit")
    args = ap.parse_args()
    if not args.query and not args.facets:
        ap.error("a query is required (or --facets)")

    if not wadkb.TALKS_DB.exists():
        # The index is derived and not committed, so build it on first use.
        print("building the search index (one-off)…", file=sys.stderr)
        import build_index

        build_index.main()

    con = sqlite3.connect(f"file:{wadkb.TALKS_DB}?mode=ro", uri=True)
    if args.facets:
        fac = facets(con)
        if args.json:
            json.dump({col: [{"value": v, "talks": n} for v, n in rows]
                       for col, rows in fac.items()}, sys.stdout, ensure_ascii=False, indent=2)
            print()
        else:
            render_facets(fac)
        return

    check_facet(con, "track", args.track, "--track")
    check_facet(con, "type", args.type_, "--type")
    check_facet(con, "stage", args.stage, "--stage")
    check_facet(con, "event_slug", args.event_slug, "--event")

    raw = " ".join(args.query)
    hits = search(con, fts_query(raw), args.limit, {
        "track": args.track, "type": args.type_,
        "stage": args.stage, "event_slug": args.event_slug,
    }, relaxed=relaxed_query(raw))

    if args.ids:
        # So that reading the hits is a pipe rather than eight ids retyped:
        #   query.py "…" --ids | xargs python3 excerpt.py -q "…"
        for h in hits:
            print(h["id"])
    elif args.json:
        emit_json(hits, args.moments, args.brief)
    else:
        render(hits, args.moments, args.brief)


if __name__ == "__main__":
    main()
