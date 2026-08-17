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
transcript: true
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

## Transcript

*671 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=pDhlie4JR0I&t=3s)** Okay, quick show of hands. Uh, who of you have coded or made a PR request this week that was mostly written by an AI? All right. And how many of you had a human actually review it line by line? Two, three, four, five. Okay. Surprisingly well. Uh but in in any case, that's right there is what I'm going to uh talk about. So [clears throat] here's what it looks like at scale. Uh last year, GitHub logged around 1 billion commits uh uh during 2025. And this year they're already on a pace for 14 billion. That's and by the way, that's their own COO saying it, not me making that claim, but theself. And uh all of that is almost

**[0:52](https://www.youtube.com/watch?v=pDhlie4JR0I&t=52s)** thanks to AI. So the question I keep coming back to is then who's actually checking whether any of this code is safe? Uh and I don't mean who owns the security in the org charts. I mean who actually reads the code your AI just merged. In most teams, if we're being honest, no one does that, at least at uh that kind of volume. Um, and here's the part that tends to surprise people. Um, the bugs that really hurt you in AI generated code is usually not in the code at all. They are in the architecture. So some untrusted content from a third party, a user walks over your trust boundary to the coding agent which then

**[1:41](https://www.youtube.com/watch?v=pDhlie4JR0I&t=101s)** calls tools over your MCP and meanwhile this whole in the background you have a backend API that does what it does in the background. So how can you actually catch this uh on a on a on a regular basis? The the none of that is actually a line level bug. you would catch by reading a file. Uh it lives in how all of these pieces trust each other. And the reason this slips true is that neither of the safety nets we lean on today is even looking at that layer. So your scanner reads lines one line at a time. Uh it was built to catch a bad string or a leakage secret. So it has no way to see that one service trusts another that trusts outside input. And a person

**[2:30](https://www.youtube.com/watch?v=pDhlie4JR0I&t=150s)** reviewing one pull request at a time can't hold the whole system in their head either at and at 14 times the volume uh there's simply no time to try. So uh that the kind of review that would actually catch this is called threat modeling. Uh but it's slow manual and it needs a security security engineer. So in practice it just never happens. Um so one minute left so I'll skip my own background but the simple way simplest way I could put uh what opin is is that it's an AI security engineer that threat models your codebase continuously right inside your own workflows. So point in a repo it reads uh your architecture in instead of just the diff and tells you where the real risks uh actually are. So um you are

**[3:20](https://www.youtube.com/watch?v=pDhlie4JR0I&t=200s)** finding it, fixing it and proving it uh all as you ship instead of getting a 40page PDF document that's already out of date uh the moment you you receive it. Um and this is actually working today already. So we across our teams that are using it uh we are doing around uh the threat modeling around 16,000 threat uh pull request per month. Uh a bit over 2,700 repository repos under coverage and last 30 days alone uh we supported in in pushing around 2,800 security fixes to to implement it. Um and um our customers or teams are from fast growing startups to enterprises. So AI native teams uh build build on play.

**[4:10](https://www.youtube.com/watch?v=pDhlie4JR0I&t=250s)** >> So uh yeah um out of time unfortunately but thank you so much for uh for uh getting through all of this technical difficulties and presenting. That was Oplane. Thank you very much Oplane. Thank you.
