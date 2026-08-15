---
id: 731
title: "Docker build without Docker"
slug: docker-build-without-docker
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "DevOps"
type: "Keynote/Talk"
stage: "Stage 8 - powered by Red Hat"
tags: ["Containers", "DevOps", "Docker", "Linux"]
speakers: ["Oliver Seitz"]
speaker_companies: ["Accenture"]
day: 1
starts_at: 2026-07-09T12:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=AVr_6VN1-24
video_id: AVr_6VN1-24
session_page: https://app.wearedevelopers.com/events/16/session/731
transcript: false
---

# Docker build without Docker

**Oliver Seitz (Associate Manager — Accenture)**

`Track: DevOps` · `Type: Keynote/Talk` · `Stage: Stage 8 - powered by Red Hat`

`#Containers` `#DevOps` `#Docker` `#Linux`

[Watch the recording](https://www.youtube.com/watch?v=AVr_6VN1-24) · [Session page](https://app.wearedevelopers.com/events/16/session/731)

## Abstract

Ever wondered what a Docker image really is? How do layers work? Why are images content-addressed? And how does Docker turn a sequence of filesystem changes into something a container runtime can execute?

Let’s continue the "Docker * without Docker" series and take a deep dive into Docker image builds - without relying on Docker itself. We use docker build every day, but what actually happens under the hood?

We’ll explore the Linux and OS concepts that make builds possible: root filesystems, filesystem diffs, OverlayFS, tar archives, hashes, and image metadata. Step by step, we’ll reconstruct the core ideas behind docker build directly from the terminal, to see how much of Docker is clever orchestration rather than magic.

Join me for a hands-on exploration of what Docker images truly are - and why understanding the build process changes how you think about performance, image size, caching, and container behavior.

## Speakers

### Oliver Seitz

*Associate Manager — Accenture*

I've been a software developer at heart for ten years and am interested in everything related to software development, like containerization and orchestration, machine learning, security, and the cloud. I work as an Associate Manager @ Accenture in Munich, Germany. I love fishing, Microsoft Flight Simulator, and TikTok.
