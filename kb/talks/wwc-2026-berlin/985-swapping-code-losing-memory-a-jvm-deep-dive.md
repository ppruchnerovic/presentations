---
id: 985
title: "Swapping Code, Losing Memory: A JVM Deep Dive"
slug: swapping-code-losing-memory-a-jvm-deep-dive
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Languages & Runtimes"
type: "Keynote/Talk"
stage: "Stage 8 - powered by Red Hat"
tags: ["C++", "Java", "JVM"]
speakers: ["Marco Sussitz"]
speaker_companies: ["Dynatrace"]
day: 2
starts_at: 2026-07-10T13:00:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=1eNznlNuJBQ
video_id: 1eNznlNuJBQ
session_page: https://app.wearedevelopers.com/events/16/session/985
transcript: false
---

# Swapping Code, Losing Memory: A JVM Deep Dive

**Marco Sussitz (Senior Software Developer — Dynatrace)**

`Track: Languages & Runtimes` · `Type: Keynote/Talk` · `Stage: Stage 8 - powered by Red Hat`

`#C++` `#Java` `#JVM`

[Watch the recording](https://www.youtube.com/watch?v=1eNznlNuJBQ) · [Session page](https://app.wearedevelopers.com/events/16/session/985)

## Abstract

You’ve probably seen the option to hot swap code while debugging in your IDE, but have you ever wondered how it actually works under the hood? And more importantly, what could go wrong?
While stress testing an application that made heavy use of class reloading, I discovered a surprising issue: we were leaking memory and not just heap memory. This kicked off a deep dive into the internals of the JVM to understand what really happens when a class is reloaded.
In this talk, I’ll explain how I investigated the problem, what I learned about class representation in the JVM, and how code hot swapping really works in OpenJDK. You’ll leave with practical insights into debugging class reloading issues and a better understanding of what’s happening behind the scenes when your code changes on the fly.

## Speakers

### Marco Sussitz

*Senior Software Developer — Dynatrace*

Marco Sussitz is an engineer at Dynatrace who lives at the boundary of Java and C++. He writes JVMTI agents, instruments bytecode, and digs into JIT, memory, and thread behavior. You’ll often find him sorting out class loaders or, reading the spec longer than he should. Before Dynatrace, he worked on cloud video encoding with FFmpeg. Off hours he’s bouldering or in the mountains.
