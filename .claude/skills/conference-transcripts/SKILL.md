---
name: conference-transcripts
description: |
  Build a transcript corpus from a conference's YouTube recordings — enumerate
  a playlist or channel into a work list, then fetch captions with exact
  timings, gently enough not to get the IP blocked. Use this whenever the user
  wants to pull talks, sessions or recordings from a conference channel (AI
  conferences, developer conferences, meetup channels), fetch YouTube
  transcripts or subtitles in bulk, resume a fetch that got rate limited or
  "429"-ed, or turn a set of talk videos into searchable text. Also use it
  when a transcript fetch is failing with "Sign in to confirm you're not a
  bot", when transcripts came out with wrong or approximate timestamps, or to
  decide whether the current network can fetch at all. Do NOT use it to
  download video or audio, and do not use it to *query* the existing
  WeAreDevelopers corpus — that is the `conference-talks` skill.
---

# Fetching conference talk transcripts from YouTube

Two scripts in `scripts/`, next to this file:

```
list_videos.py        playlist/channel URL -> videos.json      (cheap, unmetered)
fetch_transcripts.py  videos.json          -> transcripts/     (metered — ration it)
```

They were generalised from the fetcher that built the 358-talk WeAreDevelopers
corpus in this repo (`kb/`), and carry what that cost a day to learn. Read
*The quota* before starting a run of any size — it is the difference between
finishing a corpus and burning an IP on the first hundred.

## Setup

```bash
python3 -m venv .venv                       # Ubuntu's system Python refuses pip installs
.venv/bin/pip install youtube-transcript-api yt-dlp
```

Use `.venv/bin/python` in the commands below. `yt-dlp` is optional but worth
having: it is a second exact-timing route through a different Innertube client.

## The normal run

```bash
S=.claude/skills/conference-transcripts/scripts

# 1. Enumerate. Costs nothing against the transcript quota — this reads the
#    playlist page, not the caption endpoint. Enumerate freely.
.venv/bin/python $S/list_videos.py "<playlist-or-channel-url>" \
    --min-duration 300 --exclude 'trailer|teaser|livestream' -o videos.json

# 2. Check the list before spending quota on it. Conference channels mix talks
#    with stings, sponsor clips and re-runs of the same stream.
head -40 videos.json

# 3. Is this network usable right now? One request, before committing to a run.
.venv/bin/python $S/fetch_transcripts.py --probe --source exact

# 4. Fetch. --source exact refuses to silently downgrade to estimated timings;
#    --retry-after parks the run on a block and resumes.
.venv/bin/python $S/fetch_transcripts.py --from videos.json --out transcripts/ \
    --source exact --workers 2 --retry-after 20
```

Output is one `transcripts/<video_id>.json` per talk:

```json
{"video_id":"...","title":"...","language":"en","source":"yt","timing":"exact",
 "word_count":4210,"segments":[{"start":12.3,"duration":4.1,"text":"..."}]}
```

Check the corpus afterwards — `timing` must be `exact` for deep links to land
on the quote:

```bash
python3 -c "
import json,glob,collections
c=collections.Counter(json.load(open(f))['timing']
                      for f in glob.glob('transcripts/*.json') if '_misses' not in f)
print(c)"
```

## The quota — read this before a big run

**YouTube meters the caption endpoint per egress IP, with an allowance that
refills over hours. It is not a rate limit, and slowing down does not buy more.**

| Egress | Fetched before the block |
|---|---|
| Corporate NAT (Zscaler) | 235, then 52 in a later sitting |
| Residential ISP | 25 |
| Mobile carrier | 22 |

A run at four unpaced workers (~40 req/min) got 235; a later, gentler run at
two paced workers (~24 req/min) stopped at 25. What is metered is the
allowance, not the rate. Consequences:

- **Plan for several sittings.** A few hundred talks will not come down in one
  run from one network. `--retry-after 20` parks and resumes; each round
  re-derives its work from disk, so a blocked round costs only time.
- **Both exact routes share the allowance**, so yt-dlp is a fallback for a
  *refusal*, not for an exhausted quota: a run that has genuinely run dry stops
  on both. But one refusal is not proof the quota is gone — translated tracks
  meter separately, and `--probe` only ever asks about an ordinary one. See
  *A block on one route is not a block on all of them*.
- **Switching networks resets it.** A phone hotspot is a fresh allowance.
  Corporate NAT fronts many users and carries a bigger one — the one case where
  a datacenter-ish IP does better, if it is not already flagged.
- **Recovery is uneven**: a carrier IP was still blocked after ~2.5h, a
  corporate one recovered in ~2h. Probe before restarting a parked run.
- **CI, cloud containers and VPNs are datacenter ranges** and are refused
  fastest. Run this from an ordinary connection.

### The official API is a dead end

Do not reach for the YouTube Data API. `captions.download` needs OAuth *and*
edit permission on the video, so third-party talks return 403; and at 200 quota
units against a 10,000/day default it caps at 50 transcripts a day even if
permission existed. The `timedtext` endpoint these scripts use is undocumented
— no published limit, no quota-extension form.

## Three routes, and why the order matters

| Route | Timing | Works from |
|---|---|---|
| `youtube-transcript-api` | exact | an unflagged, ordinary IP |
| `yt-dlp` | exact | as above, different Innertube client — survives some refusals |
| `kome.ai` | **estimated** | anywhere; it fetches server-side from its own IPs |

kome.ai returns plain text with no timing, so starts are interpolated from word
position. Measured against the same 109 talks fetched both ways, that lands a
deep link a median of **16.5s** from the quote, 46.5s at p90, 88s at worst —
fine for "which talk said this", useless for "jump to where they said it".

So: `--source exact` for a corpus you will link into, and accept a longer
calendar time. `--source auto` (the default) falls back to kome.ai and is right
when you only need the text. `--source kome` skips YouTube entirely — the one
that works from CI, and the only source that runs with neither
`youtube-transcript-api` nor `yt-dlp` installed.

### Which caption track, and in which language

Both exact routes take a track in the same order, and stop at the first that
exists:

1. a manual track in a wanted language — `--languages`, English variants first,
   then `de,es,fr,pt,it,nl,pl,uk`;
2. an auto-generated track in a wanted language;
3. any track YouTube will machine-translate into `--translate-to` (default
   `en`; pass an empty value to disable);
4. nothing — unless `--allow-other-languages`, which takes a track in a
   language you never asked for, as it is.

Step 4 is opt-in because of a defect it caused in a real corpus. Taking the
first track on offer when none was translatable saved two English talks as
Devanagari transliterations of the speech. They passed every check the pipeline
had — a file on disk, a word count, `timing: "exact"` — while carrying about
thirty indexable tokens each, so the corpus counted them as fully transcribed
and search never found them. A talk you failed to fetch is visible in
`_misses.json`; a talk you fetched wrongly is not.

### A block on one route is not a block on all of them

The meter is finer-grained than "this IP". A machine-translated track (step 3
above) is metered apart from the original it is translated from, and the two
exact routes reach it through different Innertube clients. So a refusal can be
local to one route-and-track combination while everything else still answers.

Repairing those two Devanagari talks, same IP, minutes apart:

| Request | Result |
|---|---|
| `--probe --source exact`, an ordinary original track | ok |
| route 1, the translated `en` track | **blocked** |
| route 1, the same video's original `hi` track | ok, 5,385 words |
| route 2 (`--source ytdlp`), that same translated `en` track | ok, 5,335 words |

Taking that one block as "the quota is gone" would have parked the run for
hours. It was never gone: the translation was the only thing refused, and the
other client had it.

So when a fetch is refused, spend three requests before spending three hours:

```bash
S=.claude/skills/conference-transcripts/scripts
python3 $S/fetch_transcripts.py --probe --source exact   # is the network usable at all?
python3 $S/fetch_transcripts.py VIDEO_ID --source ytdlp  # is it only route 1?
python3 $S/fetch_transcripts.py VIDEO_ID --allow-other-languages  # only the translation?
```

The allowance is still real, so do not read this as "retry forever": the very
next video blocked on route 2 as well, and only `--retry-after` finished it.
The rule is **exhaust the routes before you spend the hours** — and, because a
block is never recorded as a miss, none of these attempts costs you the talk.

## Rules the scripts enforce, which are easy to break by hand

- **A block is not a miss.** A refusal describes the network; "no captions"
  describes the video. Only the latter goes in `_misses.json`. Conflating them
  means a plain rerun silently skips good talks — this is the single most
  expensive bug in this workflow, and it hides in the wording: a block is not
  only an HTTP 429. "Sign in to confirm you're not a bot" is the same verdict
  in different words, and both exact routes have to read it that way. yt-dlp
  puts it in stderr rather than in its exit code, which is precisely where a
  429-only check misses it and caches a perfectly good talk as captionless.
- **An age gate is not a block.** "Sign in to confirm your age" reads like
  "Sign in to confirm you're not a bot" and contains the same substring, but it
  describes the video, and no amount of waiting fixes it. Treated as a block it
  would park the run — and every retry round after it — on one video forever, so
  it is recorded as an ordinary miss. The video-specific markers are matched
  *before* the block markers for exactly this reason: with these two, the order
  of the check is the check.
- **Stop on the first block.** Continuing burns the rest of the list against a
  closed door and inflates the progress counter while nothing lands.
- **Pace every worker, not just the serial path.** A parallel fetcher whose
  delay flags are wired only into the serial branch is how an IP gets blocked
  while the operator believes they are being gentle.
- **A rerun does not upgrade estimated transcripts to exact ones** — it skips
  what is already on disk. Delete those files first; that is the point.
- **json3 carries every line twice** (real events plus `aAppend` scroll
  rollups). Naive parsing doubles the transcript. `parse_json3` drops the
  rollups, which is what makes yt-dlp's output match the API's exactly.

## If you index the result

Do not index raw captions as your search unit. YouTube captions arrive as
~6-word lines, and both a SQLite FTS query requiring all terms in one segment
and a browser-side co-occurrence bonus then ask for terms to share a ~6-word
window — "spec driven development" is spoken across three caption lines and
matches none of them. Group consecutive captions into ~28-word passages at
index time, keeping each passage's first caption start so deep links stay
precise. `kb/tools/build_index.py` in this repo does exactly that
(`to_passages`, `PASSAGE_WORDS`); `kb/STATE.md` records why. `PASSAGE_WORDS` is
25, but that is the threshold a passage flushes at — captions are appended
whole, so the passages come out averaging ~28 words.

## Reference

- `list_videos.py --help` — `--match`/`--exclude` regexes, `--min-duration`
  and `--max-duration`, `--first N` to avoid paging through a whole channel,
  `--dry-run` to see what a filter keeps without writing the work list.
  Note the behaviour change: when either duration filter is on, entries yt-dlp
  reported no duration for are now dropped rather than waved through, because
  nothing checked them — that is how a 40-second sting used to survive
  `--min-duration 300`. `--keep-unknown-duration` opts back in.
- `fetch_transcripts.py --help` — sources, `--retry-misses`, `--proxy`,
  `--min-delay`/`--max-delay` for the pause between requests (3–7s, on every
  worker), `--probe-video` to probe with a video you know has captions rather
  than the built-in default, and `--limit` for a trial run — which turns off
  `--retry-after` parking, and now says so on stderr instead of quietly
  stopping at the first block.
- `--languages`, `--translate-to` and `--allow-other-languages` choose the
  caption track, on both exact routes — see *Which caption track* above.
- Accepts bare ids and URLs too: `fetch_transcripts.py <id> <url> --out t/`.
