---
id: 656
title: "The Hidden Costs of CPU Limits in Kubernetes"
slug: the-hidden-costs-of-cpu-limits-in-kubernetes
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Cloud & AI Infrastructure"
type: "Keynote/Talk"
stage: "Stage 8 - powered by Red Hat"
tags: ["DevOps", "Google Cloud (GCP)", "Infrastructure", "Observability", "Performance"]
speakers: ["Pavel Malyarevsky"]
speaker_companies: ["Deutsche Bank"]
day: 1
starts_at: 2026-07-09T10:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=AW9iRjKIqj0
video_id: AW9iRjKIqj0
session_page: https://app.wearedevelopers.com/events/16/session/656
transcript: false
---

# The Hidden Costs of CPU Limits in Kubernetes

**Pavel Malyarevsky (Director PCCP — Deutsche Bank)**

`Track: Cloud & AI Infrastructure` · `Type: Keynote/Talk` · `Stage: Stage 8 - powered by Red Hat`

`#DevOps` `#Google Cloud (GCP)` `#Infrastructure` `#Observability` `#Performance`

[Watch the recording](https://www.youtube.com/watch?v=AW9iRjKIqj0) · [Session page](https://app.wearedevelopers.com/events/16/session/656)

## Abstract

CPU limits in Kubernetes are widely recommended as a best practice—but in real production systems they often introduce performance problems that are hard to observe, explain, or debug.

In this talk, we explore what actually happens inside the Linux kernel when CPU limits are enforced via cgroups, and how this impacts modern application runtimes. We’ll examine how CPU throttling interacts with the Linux scheduler, increases context switching, and restricts runnable threads in ways that are invisible at the Kubernetes abstraction layer.

A key focus of the session is how different runtimes manage their own concurrency. We’ll show that the number of runnable threads is not always fixed and can often be influenced, sometimes directly, sometimes indirectly, through runtime configuration and scheduling behavior. Using examples from Go, the JVM, and native C/C++ applications, we’ll demonstrate how aligning runtime-level concurrency with actual CPU availability can significantly reduce throttling and improve stability.

We’ll connect these mechanisms to real-world symptoms such as increased tail latency, unstable throughput, misleading autoscaling signals, and confusing observability data. The session concludes with practical guidance for DevOps and platform engineers on when CPU limits help, when they hurt, and how to design Kubernetes workloads that balance isolation, performance, and predictability.

## Speakers

### Pavel Malyarevsky

*Director PCCP — Deutsche Bank*

Pavel Malyarevsky is an engineering leader and infrastructure practitioner with nearly 20 years of experience running large-scale, mission-critical systems. He is currently the Engineering Owner of the Container as a Service part of Private Cloud at Deutsche Bank in Berlin, where he designs and operates Kubernetes-based platforms supporting latency-sensitive and high-throughput workloads.

Pavel has led cloud and infrastructure organizations across multiple countries, managing fleets of tens of thousands of servers and network devices in highly regulated environments. His background spans Linux internals, distributed systems, observability, and production engineering, with a strong focus on performance and operational correctness.

Having worked extensively with containerized runtimes in real production environments, Pavel focuses on closing the gap between Kubernetes abstractions and the underlying behavior of the Linux kernel and application runtimes—especially where hidden performance costs emerge.
