---
id: 729
title: "Rules, Heuristics, or LLMs? Lessons from Solving the Same Problem Twice"
slug: rules-heuristics-or-llms-lessons-from-solving-the-same
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Engineering"
type: "Keynote/Talk"
stage: "Stage 6 - powered by Microsoft"
tags: ["AI Models", "Large Language Models (LLMs)", "Small Language Models (SLMs)", "Software Architecture", "System Design"]
speakers: ["Artur Naumenko"]
speaker_companies: ["Softeta"]
day: 1
starts_at: 2026-07-09T12:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=gAjwsmSvtIM
video_id: gAjwsmSvtIM
session_page: https://app.wearedevelopers.com/events/16/session/729
transcript: false
---

# Rules, Heuristics, or LLMs? Lessons from Solving the Same Problem Twice

**Artur Naumenko (Senior Software Engineer — Softeta)**

`Track: AI Engineering` · `Type: Keynote/Talk` · `Stage: Stage 6 - powered by Microsoft`

`#AI Models` `#Large Language Models (LLMs)` `#Small Language Models (SLMs)` `#Software Architecture` `#System Design`

[Watch the recording](https://www.youtube.com/watch?v=gAjwsmSvtIM) · [Session page](https://app.wearedevelopers.com/events/16/session/729)

## Abstract

Not every problem needs an LLM. But at the same time some problems are asking for LLMs as the solution. So, when to choose which?

I ran into this while working on a subjective text transformation problem. It’s hard to specify and hard to test. That made it into a brilliant grey zone. When the answer to the regular regular question "can it be done without LLM" is "yes, but...".

To understand the trade-offs, I built two solutions to the same problem. Both of them produce similar result, they just work in a very different way.

One is a "just code and math": rule-based stochastic system using Markov chains, edit-distance mutations and so on. The other is a LoRA fine tuned LLM trained on the examples.

In this talk, I'll share what I learned, so that you could build just one system, instead of two:

Where deterministic models offer better control
Where LLMs produce more natural results
How the results are different
Maintenance cost

As the problems sits in a grey zone and hard to properly measure, I will show a result of blind comparison between rule-based output and LLM output to determine whether LLM solution was necessary or overkill.

This is not a tutorial or an AI demo. You’ll leave with a practical way to understand and decide when the problem is LLM-worthy and when to stick to the good old code and algorithms.
It's a case study on how over-engineering once on purpose can save future effort and resources.

## Speakers

### Artur Naumenko

*Senior Software Engineer — Softeta*

I am a senior software engineer and consultant with 9+ years of experience working in banking, telecom, government, and enterprise domains.

A systems thinker and pragmatic generalist. Backend-first, infrastructure-aware and privacy-minded. Currently exploring applied AI direction.

Experienced mentor, speaker, and consultant, organizer of "summer academies" and different internal knowledge-sharing sessions with a strong focus on practical learning and software engineering reality.
