#!/usr/bin/env python3
"""Offline checks for query.py — no database, no network.

What is tested is the part that decides whether a search finds anything at
all: how a bare query becomes an FTS5 expression, and how a short strict
result list is topped up. Each failure guarded here was silent — a question
that returned "no matches" against a corpus that answers it, a hyphen that
made a query stricter than a space, relaxed hits interleaved with strict ones
so the ranking the browser is measured against quietly moved.

    cd kb/tools && python3 test_query.py
"""

import sys

sys.path.insert(0, ".")
import query as Q

FAILS = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        FAILS.append(name)


print("\n-- questions become topic searches --")
check("stopwords are dropped from a bare query",
      Q.fts_query("what do speakers think about vibe coding")
      == '"speakers" AND "think" AND "vibe" AND "coding"',
      Q.fts_query("what do speakers think about vibe coding"))
check("a plain topic is unchanged",
      Q.fts_query("spec driven development") == '"spec" AND "driven" AND "development"')
check("a query that is all stopwords keeps its words rather than becoming empty",
      Q.fts_query("how do we") == '"how" AND "do" AND "we"', Q.fts_query("how do we"))
check("a leading stopword does not stop a one-word query",
      Q.fts_query("the kubernetes") == '"kubernetes"', Q.fts_query("the kubernetes"))

print("\n-- hyphens are spaces, not phrases --")
for hyph, plain in (("AI-driven SDLC", "ai driven sdlc"),
                    ("spec-driven development", "spec driven development"),
                    ("test-driven", "test driven"),
                    ("ci/cd pipelines", "ci cd pipelines"),
                    ("node.js", "node js")):
    check(f'"{hyph}" searches the same as "{plain}"',
          Q.fts_query(hyph).lower() == Q.fts_query(plain).lower(),
          f"{Q.fts_query(hyph)!r} vs {Q.fts_query(plain)!r}")
check("the split does not manufacture empty words",
      Q.fts_query("spec-- driven") == '"spec" AND "driven"', Q.fts_query("spec-- driven"))
check("a duplicate produced by the split is dropped",
      Q.fts_query("ai ai-driven") == '"ai" AND "driven"', Q.fts_query("ai ai-driven"))

print("\n-- explicit FTS5 syntax is passed through --")
for raw in ('"spec-driven" development', 'agent OR agents', 'prompt* NOT injection',
            'security AND agents'):
    check(f"{raw!r} is untouched", Q.fts_query(raw) == raw, Q.fts_query(raw))
    check(f"{raw!r} is never relaxed", Q.relaxed_query(raw) is None)

print("\n-- the relaxation --")
check("a multi-word query relaxes to an OR of its content words",
      Q.relaxed_query("what do speakers think about vibe coding")
      == '"speakers" OR "think" OR "vibe" OR "coding"',
      Q.relaxed_query("what do speakers think about vibe coding"))
check("hyphens split there too",
      Q.relaxed_query("AI-driven SDLC") == '"AI" OR "driven" OR "SDLC"',
      Q.relaxed_query("AI-driven SDLC"))
check("one content word has nothing to relax to",
      Q.relaxed_query("the kubernetes") is None, Q.relaxed_query("the kubernetes"))
check("one word has nothing to relax to", Q.relaxed_query("kubernetes") is None)

print("\n-- topping up a short list --")
S = [{"id": 1, "score": 9.0}, {"id": 2, "score": 8.0}]
R = [{"id": 2, "score": 20.0}, {"id": 3, "score": 15.0}, {"id": 4, "score": 1.0}]
out = Q.fill_relaxed(S, R, 3)
check("strict hits come first, in their own order, whatever the relaxed scores say",
      [h["id"] for h in out] == [1, 2, 3], [h["id"] for h in out])
check("a talk in both lists is counted once, as strict",
      [h["relaxed"] for h in out] == [False, False, True], [h["relaxed"] for h in out])
check("the limit is honoured", len(Q.fill_relaxed(S, R, 2)) == 2)
check("a full strict list takes nothing from the relaxed one",
      all(not h["relaxed"] for h in Q.fill_relaxed(S + [{"id": 5, "score": 1}], R, 3)))
check("no relaxed hits leaves the strict list as it was",
      [h["id"] for h in Q.fill_relaxed(S, [], 5)] == [1, 2])
check("every hit says whether it was relaxed",
      all("relaxed" in h for h in Q.fill_relaxed(S, R, 5)))

print("\n" + (f"{len(FAILS)} FAILED: {FAILS}" if FAILS else "all checks passed"))
sys.exit(1 if FAILS else 0)
