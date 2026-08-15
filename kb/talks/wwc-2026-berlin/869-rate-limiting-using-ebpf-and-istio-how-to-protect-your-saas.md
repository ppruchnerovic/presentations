---
id: 869
title: "Rate-limiting using eBPF and Istio: How to protect your SaaS customers from themselves"
slug: rate-limiting-using-ebpf-and-istio-how-to-protect-your-saas
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Security & Privacy"
type: "Keynote/Talk"
stage: "Stage 8 - powered by Red Hat"
tags: ["Infrastructure", "Networking", "Observability"]
speakers: ["Jan Mensch"]
speaker_companies: ["ClickHouse"]
day: 2
starts_at: 2026-07-10T08:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=qSfoXvef8Lg
video_id: qSfoXvef8Lg
session_page: https://app.wearedevelopers.com/events/16/session/869
transcript: false
---

# Rate-limiting using eBPF and Istio: How to protect your SaaS customers from themselves

**Jan Mensch (Software Developer — ClickHouse)**

`Track: Security & Privacy` · `Type: Keynote/Talk` · `Stage: Stage 8 - powered by Red Hat`

`#Infrastructure` `#Networking` `#Observability`

[Watch the recording](https://www.youtube.com/watch?v=qSfoXvef8Lg) · [Session page](https://app.wearedevelopers.com/events/16/session/869)

## Abstract

Do you offer a SaaS product? Is your entire infrastructure sitting behind a couple of reverse proxies that got overloaded because one customer decided to "stress test" your service? Then this talk is for you!

This presentation covers rate limiting at ClickHouse Cloud, makers of the open-source database of the same name. We'll discuss how to cut off connections at L3 using eBPF before they overwhelm your proxies. You'll learn how we guess which customer is the (accidental) bad actor, even though our rate limiter never parses the TLS SNI header that would tell us which customer instance is being hit. You'll also learn why eBPF rate limiting isn't enough on its own, and why we use Istio as well.

## Speakers

### Jan Mensch

*Software Developer — ClickHouse*

I am a Software Developer working at ClickHouse. My work touches databases, distributed systems, networking, and cloud infrastructure.

In my free time I enjoy learning Spanish, cooking, and windsurfing.
