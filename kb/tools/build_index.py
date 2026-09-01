#!/usr/bin/env python3
"""Build the search indexes from data/talks.json + data/transcripts/.

Produces two independent indexes from the same corpus:

  data/talks.db          SQLite + FTS5. Used by query.py and by anything that
                         can open a database. Includes a per-segment index so a
                         hit can point at the exact second in the video.

  data/search-meta.json  Every talk's metadata + abstract, compact keys. Small
  data/tindex/*.json     enough for a browser to load up front. The transcript
  data/tindex/_manifest  inverted index is sharded by first letter and fetched
                         lazily, so the site stays fast without a backend.

    python3 build_index.py
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import shutil
import sqlite3
import sys

import wadkb

SCHEMA = """
PRAGMA journal_mode = OFF;
DROP TABLE IF EXISTS talks;
DROP TABLE IF EXISTS talks_fts;
DROP TABLE IF EXISTS segments;
DROP TABLE IF EXISTS segments_fts;

CREATE TABLE talks (
    id INTEGER PRIMARY KEY, title TEXT, description TEXT, track TEXT, type TEXT,
    stage TEXT, tags TEXT, speakers TEXT, companies TEXT, day INTEGER,
    starts_at TEXT, duration_min INTEGER, recording_url TEXT, video_id TEXT,
    session_page TEXT, event_name TEXT, event_slug TEXT,
    has_transcript INTEGER, transcript_words INTEGER
);

-- Content-carrying so snippet()/highlight() work. This is only the metadata and
-- abstracts (~500KB); transcript text lives in `segments` and is searched
-- through segments_fts, which also gives us the timestamp of each hit.
CREATE VIRTUAL TABLE talks_fts USING fts5(
    title, description, tags, speakers, companies, track,
    tokenize='porter unicode61'
);

CREATE TABLE segments (
    rowid INTEGER PRIMARY KEY, talk_id INTEGER, start REAL, text TEXT
);
CREATE INDEX idx_segments_talk ON segments(talk_id);

CREATE VIRTUAL TABLE segments_fts USING fts5(
    text, content='segments', content_rowid='rowid', tokenize='porter unicode61'
);
"""


# Both rankers treat a segment as the unit two query terms have to share, so
# how finely a transcript is cut decides what counts as "said together". That
# has to be a property of the index, not of whichever route fetched the
# transcript: YouTube's captions arrive as ~6-word lines, where "spec driven
# development" is spoken across three of them and matches none. Grouping them
# back into ~28-word passages restores the granularity the weights were tuned
# against. Deep links are unaffected — the browser reads the raw caption files.
PASSAGE_WORDS = 25

# Share of a transcript's words that survive tokenizing. A healthy English talk
# lands around 0.45; a transliterated one scores under 0.01, because none of its
# characters tokenize into terms the index can hold. Anything below this is not
# searchable whatever its word_count claims.
UNUSABLE_RATIO = 0.05


def to_passages(segs: list[dict]) -> list[dict]:
    """Group consecutive captions into ~PASSAGE_WORDS-word passages.

    Each passage keeps the start of its first caption, so a hit still points
    into the video; already-coarse segments pass through one per passage.
    """
    out: list[dict] = []
    texts: list[str] = []
    start, words = 0.0, 0
    for s in segs:
        if not texts:
            start = s["start"]
        texts.append(s["text"])
        words += len(s["text"].split())
        if words >= PASSAGE_WORDS:
            out.append({"start": start, "text": " ".join(texts)})
            texts, words = [], 0
    if texts:
        # A talk's last few words ("Thank you. [applause]") are not a passage.
        # Left on their own, bm25's length normalisation would over-score any
        # real word that happened to land there, so a short tail joins the
        # passage before it.
        if out and words < PASSAGE_WORDS / 2:
            out[-1]["text"] += " " + " ".join(texts)
        else:
            out.append({"start": start, "text": " ".join(texts)})
    return out


def transcript_text(talk_id: int) -> tuple[str, list[dict], int]:
    tr = wadkb.load_transcript(talk_id)
    if not tr:
        return "", [], 0
    segs = tr.get("segments", [])
    return " ".join(s["text"] for s in segs), to_passages(segs), tr.get("word_count", 0)


def build_sqlite(talks: list[dict]) -> tuple[int, int]:
    if wadkb.TALKS_DB.exists():
        wadkb.TALKS_DB.unlink()
    con = sqlite3.connect(wadkb.TALKS_DB)
    con.executescript(SCHEMA)

    n_tr = 0
    seg_rowid = 0
    for t in talks:
        text, segs, words = transcript_text(t["id"])
        if text:
            n_tr += 1
        speakers = ", ".join(sp["name"] or "" for sp in t["speakers"])
        companies = ", ".join(sorted({sp["company"] for sp in t["speakers"] if sp.get("company")}))
        tags = ", ".join(t["tags"])

        con.execute(
            "INSERT INTO talks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (t["id"], t["title"], t["description"], t["track"], t["type"], t["stage"], tags,
             speakers, companies, t["day"], t["starts_at"], t["duration_min"],
             t["recording_url"], t["video_id"], t["session_page"], t["event_name"],
             t["event_slug"], 1 if text else 0, words),
        )
        con.execute(
            "INSERT INTO talks_fts (rowid, title, description, tags, speakers, companies, track)"
            " VALUES (?,?,?,?,?,?,?)",
            (t["id"], t["title"], t["description"], tags, speakers, companies, t["track"] or ""),
        )
        for s in segs:
            seg_rowid += 1
            con.execute("INSERT INTO segments VALUES (?,?,?,?)",
                        (seg_rowid, t["id"], s["start"], s["text"]))

    con.execute("INSERT INTO segments_fts(segments_fts) VALUES('rebuild')")
    con.commit()
    con.execute("VACUUM")
    con.close()
    return n_tr, seg_rowid


# --- browser index -----------------------------------------------------------

def shard_key(term: str) -> str:
    c = term[0]
    if c.isalpha():
        return c
    if c.isdigit():
        return "0"
    return "_"


B36 = "0123456789abcdefghijklmnopqrstuvwxyz"


def b36(n: int) -> str:
    if n == 0:
        return "0"
    out = ""
    while n:
        n, r = divmod(n, 36)
        out = B36[r] + out
    return out


def encode_positions(seg_ids: list[int]) -> str:
    """Segment indices as base36 gaps: [3, 5, 12] -> "3.2.7".

    These are what let the browser tell a talk that says the query terms inside
    one passage from a talk that merely says each of them somewhere — which is
    the whole difference between its ranking and query.py's.
    """
    prev, parts = 0, []
    for i in seg_ids:
        parts.append(b36(i - prev))
        prev = i
    return ".".join(parts)


def keep_singleton(term: str) -> bool:
    """Whether a term said once, in one talk, still earns a posting.

    The browser needs *every* query term to match somewhere, so a word missing
    from the index makes the search that contains it show "Nothing matched".
    Pruning every singleton dropped 8,983 of 23,027 terms, and 6,677 of those
    were ordinary words — a name, a product, a place, said once in the one
    talk that is about it, which is exactly the search that ought to find it.
    Digits and fragments stay pruned; a word does not.
    """
    return term.isalpha() and len(term) >= 4


def build_browser_index(talks: list[dict]) -> dict:
    """Compact metadata file + sharded transcript postings for client-side search."""
    meta = []
    postings: dict[str, dict[int, int]] = collections.defaultdict(dict)
    positions: dict[str, dict[int, list[int]]] = collections.defaultdict(dict)
    doc_len: dict[int, int] = {}
    unusable: list[tuple[int, str, int, int]] = []

    for t in talks:
        text, segs, words = transcript_text(t["id"])
        meta.append({
            "i": t["id"],
            "t": t["title"],
            "d": t["description"],
            "k": t["track"],
            "y": t["type"],
            "g": t["stage"],
            "a": t["tags"],
            "s": [sp["name"] for sp in t["speakers"] if sp.get("name")],
            "c": sorted({sp["company"] for sp in t["speakers"] if sp.get("company")}),
            "u": t["video_id"],
            "p": t["session_page"],
            "m": t["duration_min"],
            "e": t["event_slug"],
            "day": t["day"],
            # Start time, so the browser can offer a real schedule order. Without
            # it the UI can only sort by day, which collapses into alphabetical.
            "st": t["starts_at"],
            "w": words,
        })
        if not text:
            continue
        toks = wadkb.tokenize(text)
        doc_len[t["id"]] = len(toks)
        # A transcript can be present, exactly timed and the right length in
        # words, and still be worthless to search: YouTube sometimes misdetects
        # the spoken language and returns a phonetic transliteration into
        # another script, which tokenizes to almost nothing. Nothing else in the
        # pipeline notices — the file exists and its word_count is honest — so
        # flag it here by symptom rather than by hard-coded id.
        if words and len(toks) / words < UNUSABLE_RATIO:
            unusable.append((t["id"], t["title"], len(toks), words))
        for term, tf in collections.Counter(toks).items():
            postings[term][t["id"]] = tf
        # Which segments each term falls in, so the browser can score passages
        # rather than the whole transcript as one bag of words.
        for i, s in enumerate(segs):
            for term in set(wadkb.tokenize(s["text"])):
                positions[term].setdefault(t["id"], []).append(i)

    wadkb.write_json(wadkb.SEARCH_META, {"talks": meta}, compact=True)

    if wadkb.TINDEX.exists():
        shutil.rmtree(wadkb.TINDEX)

    if not postings:
        return {"terms": 0, "shards": 0, "docs": 0, "unusable": unusable}

    n_docs = len(doc_len)
    avg_len = sum(doc_len.values()) / n_docs

    shards: dict[str, dict] = collections.defaultdict(dict)
    for term, docs in postings.items():
        if len(docs) == 1 and max(docs.values()) < 2 and not keep_singleton(term):
            continue  # a number or fragment used once in one talk is noise
        idf = math.log(1 + (n_docs - len(docs) + 0.5) / (len(docs) + 0.5))
        pos = positions.get(term, {})
        shards[shard_key(term)][term] = {
            "f": round(idf, 4),
            "p": [[tid, tf, encode_positions(pos.get(tid, []))]
                  for tid, tf in sorted(docs.items(), key=lambda kv: -kv[1])],
        }

    for key, terms in shards.items():
        wadkb.write_json(wadkb.TINDEX / f"{key}.json", terms, compact=True)

    wadkb.write_json(
        wadkb.TINDEX / "_manifest.json",
        {
            "shards": sorted(shards),
            "n_docs": n_docs,
            "avg_doc_len": round(avg_len, 2),
            "doc_len": doc_len,
            "stopwords": sorted(wadkb.STOPWORDS),
        },
        compact=True,
    )
    return {"terms": sum(len(v) for v in shards.values()), "shards": len(shards),
            "docs": n_docs, "unusable": unusable}


def main(argv: list[str] | None = None) -> None:
    # argv defaults to nothing rather than sys.argv, because query.py calls
    # main() directly when the index is missing — the flags on that command line
    # are query.py's, not ours. Parsing first also means --help and typos exit
    # before anything is rebuilt.
    argparse.ArgumentParser(
        description="Rebuild data/talks.db and the browser search index from "
                    "data/talks.json + data/transcripts/. Takes no options."
    ).parse_args([] if argv is None else argv)

    talks = wadkb.load_talks()
    n_tr, n_seg = build_sqlite(talks)
    stats = build_browser_index(talks)

    # All of this goes to stderr, not stdout: query.py builds the index on first
    # use, and its own stdout may be JSON that a script is about to parse.
    err = sys.stderr
    print(f"indexed {len(talks)} talks · {n_tr} with transcripts · {n_seg:,} segments", file=err)
    print(f"  data/talks.db          {wadkb.human_size(wadkb.TALKS_DB.stat().st_size)}", file=err)
    print(f"  data/search-meta.json  {wadkb.human_size(wadkb.SEARCH_META.stat().st_size)}", file=err)
    if stats["shards"]:
        total = sum(p.stat().st_size for p in wadkb.TINDEX.glob("*.json"))
        print(f"  data/tindex/           {wadkb.human_size(total)} in {stats['shards']} shards, "
              f"{stats['terms']:,} terms over {stats['docs']} transcripts", file=err)
    else:
        print("  data/tindex/           (empty — no transcripts fetched yet)", file=err)

    for tid, title, toks, words in stats.get("unusable", []):
        print(f"  ! talk {tid} indexes {toks} terms from {words:,} words "
              f"({toks / words:.1%}) — unsearchable: {title[:48]}", file=err)


if __name__ == "__main__":
    main(sys.argv[1:])
