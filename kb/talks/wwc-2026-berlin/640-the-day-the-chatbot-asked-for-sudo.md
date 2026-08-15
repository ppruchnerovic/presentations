---
id: 640
title: "The day the chatbot asked for sudo"
slug: the-day-the-chatbot-asked-for-sudo
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Security & Privacy"
type: "Keynote/Talk"
stage: "Stage 6 - powered by Microsoft"
tags: ["AGI (Artificial General Intelligence)", "AI Standards", "Security"]
speakers: ["Alex Olivier"]
speaker_companies: ["Cerbos"]
day: 1
starts_at: 2026-07-09T09:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=gKymuV9JaeA
video_id: gKymuV9JaeA
session_page: https://app.wearedevelopers.com/events/16/session/640
transcript: false
---

# The day the chatbot asked for sudo

**Alex Olivier (Co-founder and CPO — Cerbos)**

`Track: Security & Privacy` · `Type: Keynote/Talk` · `Stage: Stage 6 - powered by Microsoft`

`#AGI (Artificial General Intelligence)` `#AI Standards` `#Security`

[Watch the recording](https://www.youtube.com/watch?v=gKymuV9JaeA) · [Session page](https://app.wearedevelopers.com/events/16/session/640)

## Abstract

Early enterprise AI systems were mostly read-only. Chat over documents, search, and summarization. The blast radius was small. As soon as agents can take actions, issue refunds, change limits, modify data, or trigger workflows, the risk profile changes completely.

At that point, prompts and guardrails are no longer enough. You are no longer evaluating whether an answer sounds reasonable. You are responsible for justifying why an action was allowed, under audit, during an incident, or in front of a regulator.

This session introduces a practical way to secure agentic systems by drawing a hard boundary between probabilistic reasoning and deterministic execution. Instead of trusting the model to behave, every proposed action is treated as a structured intent, evaluated against explicit policy, and enforced at runtime close to the protected system.

We will walk through a reference architecture for “shift down” security, where authorization decisions live below the AI layer. The focus is on preserving developer velocity and system performance while making agent behavior reviewable, explainable, and safe to operate in production.

Attendees will leave with a clear framework for integrating AI agents into real systems without turning them into ungovernable sources of risk.

## Speakers

### Alex Olivier

*Co-founder and CPO — Cerbos*

Alex Olivier is the Co-founder & CPO at Cerbos, an open-source authorization platform, and co-chair of the OpenID AuthZEN working group, which standardizes fine-grained authorization. He specializes in authorization systems, with a recent focus on workload identity and AI security.

With over a decade of experience building and scaling authorization systems at Microsoft, Qubit, Zencargo, and multiple startups, Alex has published extensively on securing Model Context Protocol (MCP) servers and AI agents. A frequent speaker at events on authorization, AI, security, and identity, including KubeCon, Google Cloud NEXT, Identiverse, and EIC, he combines standards development with practical implementation experience, focusing on the future of authorization for traditional applications, distributed workloads, and emerging AI systems.
