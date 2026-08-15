---
id: 658
title: "Speed up your CI/CD pipelines by caching build & runtime artifacts"
slug: speed-up-your-ci-cd-pipelines-by-caching-build-runtime
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "DevOps"
type: "Keynote/Talk"
stage: "Stage 1"
tags: ["Caching", "CI/CD", "Containers", "DevOps", "Docker", "GitHub Actions", "Go", "NPM", "Varnish", "Web Performance"]
speakers: ["Thijs Feryn"]
speaker_companies: ["Varnish Software"]
day: 1
starts_at: 2026-07-09T12:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=pS07-h1XQ4k
video_id: pS07-h1XQ4k
session_page: https://app.wearedevelopers.com/events/16/session/658
transcript: false
---

# Speed up your CI/CD pipelines by caching build & runtime artifacts

**Thijs Feryn (Technical Evangelist — Varnish Software)**

`Track: DevOps` · `Type: Keynote/Talk` · `Stage: Stage 1`

`#Caching` `#CI/CD` `#Containers` `#DevOps` `#Docker` `#GitHub Actions` `#Go` `#NPM` `#Varnish` `#Web Performance`

[Watch the recording](https://www.youtube.com/watch?v=pS07-h1XQ4k) · [Session page](https://app.wearedevelopers.com/events/16/session/658)

## Abstract

Slow CI/CD pipelines delay code from reaching production and frustrate development teams. Beyond testing and compilation, a major bottleneck comes from repeatedly fetching dependencies from remote artifact repositories, a slowdown that also affects developers in their daily work.

This presentation will show how to eliminate these delays by caching build and runtime artifacts such as Docker images, NPM packages, Go modules, and even Git clones and fetches.

Since most artifact repositories deliver dependencies over HTTP, a reverse caching proxy like Varnish can dramatically accelerate artifact delivery at scale.

We’ll break down the actual HTTP requests behind docker pull, git clone, go get, and npm install, and demonstrate how Varnish can be configured to cache these assets effectively, without compromising access control or security.

We’ll also compare the power of an HTTP reverse caching proxy like Varnish to other optimization strategies such as disk caching & shallow fetches.

## Speakers

### Thijs Feryn

*Technical Evangelist — Varnish Software*

As the Technical Evangelist at Varnish Software, Thijs Feryn focuses on web performance, software scalability, and content delivery. He demonstrates content-driven and technical messaging through presentations, videos, books, blog posts, social media posts, podcasts, and other media.

Thijs is a published author and wrote Getting Started with Varnish Cache and Varnish 6 by Example. As a public speaker, he has a track record of over 340 presentations in 23 different countries, where he is often praised for his energetic and engaging presentation style.

As an evangelist, Thijs is also active in many open-source communities, most notably the Varnish and PHP community. He has contributed to various communities for over 15 years both technically and as an organizer and facilitator.

Prior to joining Varnish Software, Thijs Feryn spent 15 years in the web hosting industry, tackling web performance and scalability issues on a daily basis and evangelizing these topics.
