---
id: 779
title: "The OpenTelemetry mistakes I keep seeing (and how to stop making them)"
slug: the-opentelemetry-mistakes-i-keep-seeing-and-how-to-stop
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "DevOps"
type: "Keynote/Talk"
stage: "Stage 12"
tags: ["CNCF", "Observability", "OpenTelemetry"]
speakers: ["Juraci Paixão Kröhling"]
speaker_companies: ["OllyGarden"]
day: 1
starts_at: 2026-07-09T14:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=zRJgo3bZ6AI
video_id: zRJgo3bZ6AI
session_page: https://app.wearedevelopers.com/events/16/session/779
transcript: false
---

# The OpenTelemetry mistakes I keep seeing (and how to stop making them)

**Juraci Paixão Kröhling (Software Engineer — OllyGarden)**

`Track: DevOps` · `Type: Keynote/Talk` · `Stage: Stage 12`

`#CNCF` `#Observability` `#OpenTelemetry`

[Watch the recording](https://www.youtube.com/watch?v=zRJgo3bZ6AI) · [Session page](https://app.wearedevelopers.com/events/16/session/779)

## Abstract

OpenTelemetry is becoming the standard for application telemetry, but bad telemetry is a natural part of the learning curve. Most teams start by turning on auto-instrumentation and figuring out what works as they go. That is fine. The problem is when the same mistakes persist: personally identifiable information leaking into traces, spans wrapping every function, happy paths instrumented in detail while errors get a single log line, and teams reaching for traces when a simple counter would do.

As a long-time OpenTelemetry maintainer and contributor, I have reviewed countless implementations where these four anti-patterns stuck around long after they should have been fixed. This talk walks through each one with real code examples, showing what goes wrong and why. Each pattern includes a before-and-after fix you can apply to your own codebase.

You will walk away knowing how to spot these mistakes sooner, choose the right signal type for each use case, and build telemetry that actually helps you debug problems.

## Speakers

### Juraci Paixão Kröhling

*Software Engineer — OllyGarden*

Juraci Paixão Kröhling is a software engineer at OllyGarden, a maintainer of the OpenTelemetry project, a member of the project's governing board and CNCF Ambassador. He has presented about distributed tracing, OpenTelemetry, and other related topics at conferences like KubeCon, OpenSource Summit, FOSDEM, and a few DevOpsDays, among others. Previously, he was also a maintainer of both the OpenTracing and Jaeger projects, having also delivered talks about those projects.
