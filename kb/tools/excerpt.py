#!/usr/bin/env python3
"""Read a talk without reading the whole talk.

`query.py` ranks talks and shows a ~26-word snippet per hit; the answer to
"what did this speaker actually argue" is longer than that. The obvious next
step is `cat talks/<event>/<id>-<slug>.md`, and it is the expensive one: a
talk file here averages 28 KB — roughly 7,000 tokens — and every talk in this
corpus has a transcript, so eight hits read whole is ~58,000 tokens before
the model has thought about anything. Most of what that buys is the parts of
the talk that have nothing to do with the question.

So this prints the parts that do: the talk's metadata and abstract, its
opening — where the thesis nearly always is — and a window of continuous
speech either side of each passage that matched, merged where those windows
overlap, with a deep link on each. Typically 1-2 K tokens instead of 7-8 K,
and what is left out is stated rather than silently dropped, so a thin
excerpt is visible as one and `--full` is a keystroke away.

The passages are ranked by the same `bm25(segments_fts)` that ranked the
talk, restricted to that one talk — so what you read is what put the talk in
the results.

    python3 excerpt.py 586 -q "agentic assembly line"
    python3 excerpt.py 586 1042 -q evals --window 60 -n 8
    python3 excerpt.py 586 --full            # the whole transcript
    python3 excerpt.py ggh3kdcer2U -q agents --json
    python3 query.py "agent memory" -n 6 --ids | xargs python3 excerpt.py -q "agent memory"
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys

import query
import wadkb

# A YouTube id is 11 characters of [A-Za-z0-9_-] and about one in thirty starts
# with a hyphen — `-stDHMwbBRw` is a real talk id elsewhere. argparse reads such
# a token as an unknown option and refuses the run. This corpus's own `--ids`
# prints integer ids, which never start with a hyphen, so the pipe is safe; the
# moment anyone pastes a YouTube id it is not, and the failure is a refused run
# with a confusing message. So ids are lifted out of argv before argparse.
ID_RE = re.compile(r"^-[A-Za-z0-9_-]{10}$")

# The options that take a value, so their value is never mistaken for an id.
TAKES_VALUE = {"-q", "--query", "-n", "--passages", "--window", "--opening"}

# A bare YouTube id, as opposed to one embedded in a URL.
YT_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")

# Seconds either side of a matching segment. A segment is ~28 words, which is
# a sentence fragment; 40 seconds either side is ~200 words of context, which
# is a point being made rather than a phrase being said.
WINDOW = 40

# The opening is always included when there is a query, because a speaker
# states what they are arguing in the first minute and then argues it — a
# passage lifted from minute 34 is much harder to attribute without it.
OPENING = 60

PASSAGES = 6

# Candidates to rank before selecting: neighbouring hits collapse into one
# passage, so more raw hits than passages is what gives the selection below
# something to choose between.
OVERSAMPLE = 4

# What `-n` actually buys: n windows' worth of speech, which the merge may
# hand back as fewer and wider passages. A budget rather than a count, because
# counting passages bounds nothing — on a talk that says the query word every
# other minute, six windows that each grow to meet their neighbours are the
# whole transcript again, which is the thing being avoided.

# 128 + SIGPIPE and 128 + SIGINT, which is what a shell reports for a process
# killed by either — the closest thing to a right answer for `| head`.
EXIT_SIGPIPE = 141
EXIT_SIGINT = 130

COLS = ("id video_id title speakers companies track type stage event_name "
        "duration_min recording_url session_page description has_transcript "
        "transcript_words").split()


def split_ids(argv: list[str]) -> tuple[list[str], list[str]]:
    """argv, with hyphen-leading video ids pulled out of it."""
    rest, ids, i = [], [], 0
    while i < len(argv):
        a = argv[i]
        if a in TAKES_VALUE:
            rest += argv[i:i + 2]
            i += 2
        elif ID_RE.match(a):
            ids.append(a)
            i += 1
        else:
            rest.append(a)
            i += 1
    return rest, ids


def connect() -> sqlite3.Connection:
    if not wadkb.TALKS_DB.exists():
        # The index is derived and not committed, so build it on first use.
        print("building the search index (one-off)…", file=sys.stderr)
        import build_index

        build_index.main()
    return sqlite3.connect(f"file:{wadkb.TALKS_DB}?mode=ro", uri=True)


def find_talk(con, ident: str) -> dict | None:
    """Accept the talk id, a YouTube id or URL, or a talk's markdown path.

    Two ids are in play and both turn up on a command line: `talks.id` is this
    corpus's own integer, which `segments.talk_id` joins on and which the
    markdown files are named after, while `video_id` is YouTube's and is what
    the deep links and recording URLs carry.
    """
    ident = (ident or "").strip()
    if ident.endswith(".md"):  # talks/<event>/<id>-<slug>.md
        ident = ident.rsplit("/", 1)[-1].split("-", 1)[0]
    if ident.isdigit():
        col, key = "id", int(ident)
    else:
        col, key = "video_id", (wadkb.video_id(ident)
                                or (ident if YT_ID_RE.match(ident) else None))
    if key is None:
        return None
    row = con.execute(f"SELECT {','.join(COLS)} FROM talks WHERE {col}=?", (key,)).fetchone()
    return dict(zip(COLS, row)) if row else None


def spans_for(starts: list[float], window: float, limit: int) -> list[tuple[float, float]]:
    """Windows around the best-ranked hits, up to a fixed budget of speech.

    Best hit first, each contributing ±`window` seconds, until the union of
    what has been taken reaches `limit` windows' worth. Neighbouring hits
    therefore cost almost nothing — their windows overlap — and a hit in a
    part of the talk already shown costs nothing at all, so the budget is
    spent on distinct passages rather than on the same one repeatedly.
    """
    budget = limit * 2 * window
    spans: list[tuple[float, float]] = []
    for s in starts:
        if spans and covered(spans) >= budget:
            break
        spans.append((max(0.0, s - window), s + window))
    return merge(spans)


def covered(spans: list[tuple[float, float]]) -> float:
    return sum(hi - lo for lo, hi in merge(spans))


def merge(spans: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Union of overlapping windows, in time order.

    Two windows that touch are one passage, not two — printing them separately
    would repeat the speech between them and read as though the speaker said
    it twice.
    """
    out: list[list[float]] = []
    for lo, hi in sorted(spans):
        if out and lo <= out[-1][1]:
            out[-1][1] = max(out[-1][1], hi)
        else:
            out.append([lo, hi])
    return [(lo, hi) for lo, hi in out]


def hit_starts(con, talk_id: int, strict: str, relaxed: str | None, limit: int) -> list[float]:
    """Where in this talk the query was said, best passage first.

    Relaxed the way `query.py` would relax it: a segment is ~28 words, so a
    three-word question almost never has all three inside one, and the strict
    AND that ranks talks correctly matches no single segment. Without the
    fallback every multi-word query would come back empty here — and an empty
    result is what used to fall through to printing the whole transcript.
    """
    sql = ("SELECT s.start FROM segments_fts JOIN segments s ON s.rowid = segments_fts.rowid "
           "WHERE segments_fts MATCH ? AND s.talk_id = ? "
           "ORDER BY bm25(segments_fts) LIMIT ?")
    for expr in (strict, relaxed):
        if not expr:
            continue
        try:
            rows = con.execute(sql, (expr, talk_id, limit)).fetchall()
        except sqlite3.OperationalError as e:
            raise SystemExit(f"bad query: {e}")
        if rows:
            return [r[0] for r in rows]
    return []


def passages(con, talk: dict, terms, window: float, limit: int,
             opening: float) -> tuple[list[dict], int]:
    """The windows worth printing, and how many words the transcript has."""
    segs = con.execute(
        "SELECT start, text FROM segments WHERE talk_id=? ORDER BY start", (talk["id"],)
    ).fetchall()
    if not segs:
        return [], 0
    total = sum(len(t.split()) for _, t in segs)
    end = segs[-1][0] + 30

    spans: list[tuple[float, float]] = []
    if terms:
        # Ranked by the same bm25 as query.py, restricted to this talk, so the
        # passage shown here is the passage that put the talk in the results.
        starts = hit_starts(con, talk["id"], terms[0], terms[1], limit * OVERSAMPLE)
        if not starts:
            # The talk is in the results on its abstract alone. The opening is
            # the honest answer — never the whole transcript, which is what a
            # query matching nothing must not silently cost.
            head = opening or 60
            return [{"start": 0.0, "end": head,
                     "text": " ".join(" ".join(t for st, t in segs if st < head).split()),
                     "words": 0, "note": "nothing in the transcript matched"}], total
        spans = spans_for(starts, window, limit)
    if opening > 0:
        spans.append((0.0, opening))
    if not spans:
        spans = [(0.0, end)]

    out = []
    for lo, hi in merge(spans):
        text = " ".join(t for st, t in segs if lo <= st < hi)
        if text:
            out.append({"start": lo, "end": hi, "text": " ".join(text.split()),
                        "words": len(text.split())})
    return out, total


def render(talk: dict, parts: list[dict], total_words: int, full: bool) -> None:
    vid = talk["video_id"]
    print(f"\n## {talk['title']}")
    who = talk["speakers"] or "speaker not recorded"
    if talk["companies"]:
        who += f" ({talk['companies']})"
    meta = [x for x in (who, talk["track"], talk["type"], talk["stage"],
                        f"{talk['duration_min']} min" if talk["duration_min"] else "") if x]
    print(" · ".join(meta))
    print(talk["recording_url"] or f"https://www.youtube.com/watch?v={vid}")

    if talk["description"]:
        # A real conference abstract, written by the speaker — unlike a YouTube
        # description it is worth quoting.
        print(f"\n_Abstract:_ {' '.join(talk['description'].split())}")

    if not talk["has_transcript"]:
        print("\n**No transcript.** Title and abstract are all this talk has — "
              "enough to recommend it, not enough to quote it.")
        return

    shown = sum(p["words"] for p in parts)
    for p in parts:
        print(f"\n**[{query.fmt_ts(p['start'])}]"
              f"(https://www.youtube.com/watch?v={vid}&t={int(p['start'])}s)** {p['text']}")
    if not full and shown < total_words:
        pct = round(100 * shown / total_words) if total_words else 0
        print(f"\n_{shown} of {total_words} words ({pct}%). "
              f"For the rest: excerpt.py {talk['id']} --full, or another -q._")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Print the parts of a talk that answer a question, not the whole talk.")
    ap.add_argument("ids", nargs="*", metavar="ID",
                    help="talk id, YouTube id or URL, or talks/<event>/<id>-<slug>.md")
    ap.add_argument("-q", "--query", default="",
                    help="what to excerpt around; FTS5 syntax works, as in query.py")
    ap.add_argument("-n", "--passages", type=query.positive_int, default=PASSAGES,
                    help=f"how many windows' worth of speech to keep (default {PASSAGES})")
    ap.add_argument("--window", type=float, default=WINDOW,
                    help=f"seconds of speech either side of a hit (default {WINDOW})")
    ap.add_argument("--opening", type=float, default=OPENING,
                    help=f"seconds of the start to always include (default {OPENING}; 0 for none)")
    ap.add_argument("--full", action="store_true", help="the whole transcript")
    ap.add_argument("--json", action="store_true")
    argv, hyphenated = split_ids(sys.argv[1:])
    args = ap.parse_args(argv)
    args.ids += hyphenated
    if not args.ids:
        ap.error("at least one talk id is required")

    terms = None
    if args.query and not args.full:
        terms = (query.fts_query(args.query), query.relaxed_query(args.query))

    con = connect()
    out, missing = [], []
    for ident in args.ids:
        talk = find_talk(con, ident)
        if not talk:
            missing.append(ident)
            continue
        parts, total = [], 0
        if talk["has_transcript"]:
            parts, total = passages(con, talk, terms, args.window, args.passages,
                                    0 if args.full else args.opening)
            if parts and parts[0].get("note"):
                print(f"note: nothing in talk {talk['id']}'s transcript matches "
                      f"{args.query!r} — showing the opening", file=sys.stderr)
                parts[0]["words"] = len(parts[0]["text"].split())
        out.append((talk, parts, total))

    if args.json:
        json.dump([{**{k: t[k] for k in COLS},
                    "speakers": [s for s in (t["speakers"] or "").split(", ") if s],
                    "excerpt_words": sum(p["words"] for p in parts),
                    "passages": parts}
                   for t, parts, total in out], sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        for talk, parts, total in out:
            render(talk, parts, total, args.full)
    for ident in missing:
        print(f"not in the corpus: {ident}", file=sys.stderr)
    return 1 if missing and not out else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(EXIT_SIGINT)
    except BrokenPipeError:
        sys.exit(EXIT_SIGPIPE)
