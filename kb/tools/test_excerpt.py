#!/usr/bin/env python3
"""Offline checks for excerpt.py — no database, no network.

What is worth testing here is the budget, because the failure it prevents is
silent and expensive: a query whose terms are spread through a long talk used
to chain every window into one span, and the "excerpt" came back as the whole
transcript — 7,000 tokens where 1,500 was asked for, with nothing in the
output saying so. The selection and the merge are pure functions of the hit
times, so they are testable without a corpus, and that is what is tested.

The other silent failure is a query that matches no single segment falling
through to a full read; that one lives in `excerpt.py`'s relaxation, so the
relaxed query it depends on is checked here too.

    cd kb/tools && python3 test_excerpt.py
"""

import sys

sys.path.insert(0, ".")
import excerpt as E
import query as Q

FAILS = []


def check(name, cond, extra=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        FAILS.append(name)


def secs(spans):
    return sum(hi - lo for lo, hi in spans)


print("\n-- merging --")
check("disjoint windows stay separate", E.merge([(0, 10), (50, 60)]) == [(0, 10), (50, 60)])
check("overlapping windows become one", E.merge([(0, 60), (40, 100)]) == [(0, 100)])
check("touching windows become one", E.merge([(0, 60), (60, 100)]) == [(0, 100)])
check("out of order input comes back in time order",
      E.merge([(90, 100), (0, 10)]) == [(0, 10), (90, 100)])
check("a window inside another is absorbed", E.merge([(0, 100), (20, 30)]) == [(0, 100)])

print("\n-- the budget --")
# A hit every 30 seconds through a 40-minute talk: the shape that used to
# return the transcript.
dense = [float(t) for t in range(0, 2400, 30)]
sp = E.spans_for(dense, window=40, limit=6)
check("a talk that matches throughout stays within budget", secs(sp) <= 6 * 2 * 40 + 80,
      f"{secs(sp)}s of a possible 2400")
check("and does not come back as the whole talk", secs(sp) < 2400 * 0.5, secs(sp))

spread = [100.0, 900.0, 1800.0, 2500.0]
sp = E.spans_for(spread, window=40, limit=6)
check("well-separated hits each get their own passage", len(sp) == 4, sp)
check("each is the hit plus its window either side", secs(sp) == 4 * 80, secs(sp))

check("a hit at the very start is not given negative time",
      E.spans_for([5.0], window=40, limit=6)[0][0] == 0.0)

# Rank order is what the budget is spent in, so an unranked hit past the
# budget must not displace a better one that came first.
sp = E.spans_for([100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 5000.0],
                 window=40, limit=2)
check("the budget is spent on the best-ranked hits first",
      sp[0][0] == 60.0 and all(hi <= 400 for _, hi in sp), sp)

check("more windows than hits costs only the hits",
      secs(E.spans_for([100.0], window=40, limit=6)) == 80)

print("\n-- what --window and -n buy --")
check("a wider window buys more speech per hit",
      secs(E.spans_for([500.0], window=90, limit=6)) == 180)
# On a talk that matches throughout, the windows are contiguous, so what -n
# buys is a longer passage rather than more of them — and it must buy it.
check("a bigger -n buys more speech",
      secs(E.spans_for(dense, window=40, limit=2)) < secs(E.spans_for(dense, window=40, limit=8)))
check("well-separated hits, though, come back as separate passages",
      len(E.spans_for(spread, window=40, limit=6)) == 4)

print("\n-- the relaxation that keeps a miss from costing a full read --")
check("a multi-word query has a relaxation to fall back on",
      Q.relaxed_query("spec driven development")
      == '"spec" OR "driven" OR "development"', Q.relaxed_query("spec driven development"))
check("stopwords are dropped from it",
      Q.relaxed_query("the future of testing") == '"future" OR "testing"',
      Q.relaxed_query("the future of testing"))
check("a query that is all stopwords keeps its words rather than becoming empty",
      Q.relaxed_query("how do we") == '"how" OR "do" OR "we"', Q.relaxed_query("how do we"))
check("one word has nothing to relax to", Q.relaxed_query("kubernetes") is None)
check("explicit FTS5 syntax is never relaxed — it says what it wants",
      Q.relaxed_query('"prompt injection" OR jailbreak') is None)
check("and the strict query is still the AND that ranks talks",
      Q.fts_query("spec driven development") == '"spec" AND "driven" AND "development"')

print("\n-- ids that argparse would otherwise refuse --")
rest, ids = E.split_ids(["-stDHMwbBRw", "586", "-q", "agent memory", "--json"])
check("a hyphen-leading YouTube id is lifted out of argv", ids == ["-stDHMwbBRw"], ids)
check("and everything else is left for argparse",
      rest == ["586", "-q", "agent memory", "--json"], rest)
check("a flag's value is never mistaken for an id",
      E.split_ids(["-q", "-stDHMwbBRw"])[1] == [], E.split_ids(["-q", "-stDHMwbBRw"]))
check("real flags are left alone", E.split_ids(["--full", "586"]) == (["--full", "586"], []))

print("\n" + (f"{len(FAILS)} FAILED: {FAILS}" if FAILS else "all checks passed"))
sys.exit(1 if FAILS else 0)
