---
id: 933
title: "What If We've Been Scaling Stream Processing Wrong All Along?"
slug: what-if-we-ve-been-scaling-stream-processing-wrong-all-along
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Data & Databases"
type: "Keynote/Talk"
stage: "Stage 12"
tags: ["Apache Kafka", "Kotlin", "Software Architecture", "Streaming"]
speakers: ["Hartmut Armbruster"]
speaker_companies: ["StoatFlow"]
day: 1
starts_at: 2026-07-09T14:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=hBdsdDGOk_U
video_id: hBdsdDGOk_U
session_page: https://app.wearedevelopers.com/events/16/session/933
transcript: false
---

# What If We've Been Scaling Stream Processing Wrong All Along?

**Hartmut Armbruster (Software Architect — StoatFlow)**

`Track: Data & Databases` · `Type: Keynote/Talk` · `Stage: Stage 12`

`#Apache Kafka` `#Kotlin` `#Software Architecture` `#Streaming`

[Watch the recording](https://www.youtube.com/watch?v=hBdsdDGOk_U) · [Session page](https://app.wearedevelopers.com/events/16/session/933)

## Abstract

Your Kafka Streams application just rebalanced. Again. Your Flink checkpoint is timing out. Again.

Here's an uncomfortable truth: most stream processing applications don't operate at Uber scale. They handle thousands of events per second—complex joins, stateful aggregations, valid use cases—but nowhere near the volumes that justify the operational complexity we've accepted as normal.

Yet we pay the full distributed systems tax anyway. Repartition topics doubling network I/O. Repeated serialization burning CPU cycles. Standby replicas sitting idle. State migration or restoration during deployments. And the human cost: specialized expertise that takes years to develop, expert teams that are expensive to build and painful to lose.

We've normalized extraordinary inefficiency in the name of horizontal scalability that many applications will never need.
But rethinking stream processing in 2026 doesn't mean "just use Postgres."

In this talk, I'll share an early-stage exploration of a different approach. A framework that preserves the Kafka Streams DSL, borrows Flink's approach to exactly-once semantics, leverages Project Loom for high concurrency—and challenges a fundamental assumption that both frameworks share.

This isn't a production-ready announcement. It's an invitation to question conventional wisdom and explore what stream processing could look like when we stop distributing by default.

## Speakers

### Hartmut Armbruster

*Software Architect — StoatFlow*

Hartmut is a software engineer and tech lead with a strong passion for architecture, data streaming, and distributed systems. He has designed and delivered solutions for mission-critical platforms, working with clients including HSBC, NEX Group plc, Raiffeisen Switzerland, Deutsche Bahn, and eu-LISA. Hartmut is driven by a desire to see the bigger picture and excels at aligning engineering teams through clear, compelling architectural designs.
