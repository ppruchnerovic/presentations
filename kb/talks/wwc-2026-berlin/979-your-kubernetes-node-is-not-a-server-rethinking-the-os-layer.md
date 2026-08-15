---
id: 979
title: "Your Kubernetes Node Is Not a Server: Rethinking the OS Layer"
slug: your-kubernetes-node-is-not-a-server-rethinking-the-os-layer
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Cloud & AI Infrastructure"
type: "Keynote/Talk"
stage: "Stage 2"
tags: ["Best Practices", "DevOps", "Linux"]
speakers: ["Natanael Copa"]
speaker_companies: ["Mirantis"]
day: 2
starts_at: 2026-07-10T13:00:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=e5vqHo_9XzA
video_id: e5vqHo_9XzA
session_page: https://app.wearedevelopers.com/events/16/session/979
transcript: false
---

# Your Kubernetes Node Is Not a Server: Rethinking the OS Layer

**Natanael Copa (Software Engineer — Mirantis)**

`Track: Cloud & AI Infrastructure` · `Type: Keynote/Talk` · `Stage: Stage 2`

`#Best Practices` `#DevOps` `#Linux`

[Watch the recording](https://www.youtube.com/watch?v=e5vqHo_9XzA) · [Session page](https://app.wearedevelopers.com/events/16/session/979)

## Abstract

Kubernetes already treats nodes as disposable, but most platform stacks still run them as long-lived servers. This mismatch creates unnecessary complexity in upgrades, security, and operations, especially for edge, bare-metal, and high-churn environments.

In this talk, I’ll present an alternative model: treating Kubernetes worker nodes as firmware, not operating systems. Using k0s, Linux Unified Kernel Images (UKI), and an initramfs-only OS, we build immutable workers that boot entirely from RAM, fetch configuration from metadata (cloud-init style), and optionally persist state using a single mounted /var directory.

## Speakers

### Natanael Copa

*Software Engineer — Mirantis*

Natanael Copa is the creator of Alpine Linux and a maintainer of the k0s Kubernetes distribution. He has over 20 years of experience in Linux and open-source infrastructure, with a focus on minimal, secure systems.
