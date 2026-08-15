---
id: 670
title: "Go's Concurrency and Parallelism Inside Containers"
slug: go-s-concurrency-and-parallelism-inside-containers
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Languages & Runtimes"
type: "Keynote/Talk"
stage: "Stage 10 - powered by TikTok"
tags: ["Concurrency", "Containers", "Go"]
speakers: ["Rick Rackow"]
speaker_companies: ["Schwarz Digits"]
day: 1
starts_at: 2026-07-09T10:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=DIgR4mb1fqc
video_id: DIgR4mb1fqc
session_page: https://app.wearedevelopers.com/events/16/session/670
transcript: false
---

# Go's Concurrency and Parallelism Inside Containers

**Rick Rackow (Senior Professional Engineer — Schwarz Digits)**

`Track: Languages & Runtimes` · `Type: Keynote/Talk` · `Stage: Stage 10 - powered by TikTok`

`#Concurrency` `#Containers` `#Go`

[Watch the recording](https://www.youtube.com/watch?v=DIgR4mb1fqc) · [Session page](https://app.wearedevelopers.com/events/16/session/670)

## Abstract

A common assumption is that if a program is concurrent, it will also run in parallel, and that containers simply get a number of CPU cores to work with. In practice, neither of these assumptions holds.

In this talk we explore how concurrency and parallelism behave inside containers, and why the same program can show very different performance characteristics when run on the host versus inside a container with CPU limits applied.

Using a small Go program as an example, we start with a simple sequential implementation, introduce concurrency to structure the work, and then add parallelism to scale CPU bound processing. We observe how the program behaves under different container CPU configurations, and where expectations break down.

## Speakers

### Rick Rackow

*Senior Professional Engineer — Schwarz Digits*

Rick Rackow is a seasoned professional in the IT industry with a strong background in cloud and container infrastructure. An SRE at heart, he has worked extensively with distributed systems, Linux, and Go, and focuses on building and operating reliable, observable systems in real world production environments.
