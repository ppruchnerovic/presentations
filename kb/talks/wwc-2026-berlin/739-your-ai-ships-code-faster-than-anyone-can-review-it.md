---
id: 739
title: "Your AI Ships Code Faster Than Anyone Can Review It"
slug: your-ai-ships-code-faster-than-anyone-can-review-it
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Quality & Reliability"
type: "Startup Presentation"
stage: "Airstream 1"
tags: ["AppSec", "Agents", "DevSecOps", "Security", "Threat Modelling"]
speakers: ["Rasmus Klärck"]
speaker_companies: ["Oplane"]
day: 1
starts_at: 2026-07-09T12:55:00+00:00
duration_min: 5
recording_url: https://www.youtube.com/watch?v=pDhlie4JR0I
video_id: pDhlie4JR0I
session_page: https://app.wearedevelopers.com/events/16/session/739
transcript: false
---

# Your AI Ships Code Faster Than Anyone Can Review It

**Rasmus Klärck (Founding GTM Lead — Oplane)**

`Track: Quality & Reliability` · `Type: Startup Presentation` · `Stage: Airstream 1`

`#AppSec` `#Agents` `#DevSecOps` `#Security` `#Threat Modelling`

[Watch the recording](https://www.youtube.com/watch?v=pDhlie4JR0I) · [Session page](https://app.wearedevelopers.com/events/16/session/739)

## Abstract

You shipped code this week that an AI mostly wrote. Did a human read every line before it merged? GitHub logged a billion commits in all of 2025; this year it is on pace for 14 billion, a 14x jump in a single year, almost all of it AI-driven. We now produce code faster than any person, or any scanner, can review it.

The risks that matter most in this new world usually are not line-level bugs. They are architectural: an over-permissioned service, a coding agent that can be steered into misusing a tool, an MCP server with more reach than anyone mapped, a prompt-injection path that crosses a trust boundary. Traditional SAST reads files one at a time and cannot see these. A human reviewing one PR at a time cannot hold the whole system in their head. So threat modeling, the one review built to catch architectural risk, is exactly the review that stops happening, because it is slow, manual, and needs a senior security engineer you probably cannot spare.

This talk is about closing that gap. I will show why AI coding velocity breaks traditional security review, the real difference between a code-level bug and an architecture-level threat, and what continuous, automated threat modeling looks like when it runs inside the developer workflow instead of in a quarterly audit. Then I will show the loop Oplane runs: it finds the real architectural risks, drives the fix in the pull request and the AI coding loop, and proves the fix actually closed the gap. Find, fix, prove, at the speed you already ship.

If you build with AI and want security to keep up without slowing you down, this one is for you.

## Speakers

### Rasmus Klärck

*Founding GTM Lead — Oplane*

Rasmus Klärck is the Founding GTM Lead at Oplane. He is a repeat founder and operator: he co-founded the fintech startup CasaPay and spent four years as the first employee at the Nordic VC Icebreaker.vc, backing and building early-stage software companies. He is not a security engineer, and that is the point. He builds AI products himself (like Cosos, an AI agent that runs sales pipeline inside Slack), which is how he ran headfirst into the problem Oplane solves: AI now writes and ships code faster than any team can review it, and the risks that matter most are architectural, not line-level. Oplane is an AI security engineer that continuously threat-models your codebase, surfaces the real architectural risks in minutes, and drives the fix inside the developer workflow. It works with AI-native and regulated software companies, including Tandem Health and Miro, and is backed by a $5.2M seed round.
