---
id: 1065
title: "One Interface, Two Audiences: Designing CLIs for Humans and AI Agents"
slug: one-interface-two-audiences-designing-clis-for-humans-and
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: null
type: "Keynote/Talk"
stage: "Stage 2"
tags: ["Agents", "Agentic AI", "Developer Experience (DevEx)", "Multi-Agent Systems", "Observability", "Open Source", "OpenTelemetry"]
speakers: ["Sean O'Dell", "Gala Dvoretskaya"]
speaker_companies: ["Dynatrace", "Dynatrance"]
day: 2
starts_at: 2026-07-10T11:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=Yqtm2lW5cTc
video_id: Yqtm2lW5cTc
session_page: https://app.wearedevelopers.com/events/16/session/1065
transcript: false
---

# One Interface, Two Audiences: Designing CLIs for Humans and AI Agents

**Sean O'Dell (Head of Developer Experience — Dynatrace), Gala Dvoretskaya (Observability Experience Lead — Dynatrance)**

`Track: —` · `Type: Keynote/Talk` · `Stage: Stage 2`

`#Agents` `#Agentic AI` `#Developer Experience (DevEx)` `#Multi-Agent Systems` `#Observability` `#Open Source` `#OpenTelemetry`

[Watch the recording](https://www.youtube.com/watch?v=Yqtm2lW5cTc) · [Session page](https://app.wearedevelopers.com/events/16/session/1065)

## Abstract

If a tool has to work equally well for a person typing in a terminal and an AI agent calling the same commands, how much of the design actually has to change? That's the question behind two CLIs rebuilt from the ground up: `dtwiz`, which analyzes a system and recommends how to instrument it, and `dtctl`, a kubectl-style CLI for managing platform resources like workflows and dashboards. Both are open source ([github.com/dynatrace-oss/dtwiz](https://github.com/dynatrace-oss/dtwiz), [github.com/dynatrace-oss/dtctl](https://github.com/dynatrace-oss/dtctl)), and both ship with an agent Skill so tools like Claude Code and GitHub Copilot can run the same commands a person would, no separate documentation required. This is a working session, not a pitch. We'll walk through the concrete decisions: zero-config defaults, dry-run previews, structured output modes, and a confirm-before-you-proceed prompt, plus the honest tradeoffs, like what "confirm" even means when nobody's watching the terminal. We'll also connect it to the GUI side: a new onboarding flow built on the same underlying logic. If you're deciding whether your product needs a GUI, a CLI, an agent skill, or all three, you'll leave with a concrete blueprint and two open-source repos to go read yourself.

## Speakers

### Sean O'Dell

*Head of Developer Experience — Dynatrace*

Sean O’Dell is a Principal PMM at Dynatrace, where he champions developer experience and modern application development practices. A reformed infrastructure administrator and architect, Sean brings experience from Infra, Cloud, Dev and Ops, with a passion for helping developers thrive in today’s cloud-native and AI-native world. With roots in infrastructure and a strong belief in DevOps principles, Sean advocates for a world where developers have the visibility, automation, and support they need to build, deploy, and innovate with confidence. Outside of work, Sean enjoys spending time with his family, gaming, watching TV, cheering on Arsenal, Alabama football, the New York Yankees, and the Tennessee Titans—and smoking Texas BBQ.

### Gala Dvoretskaya

*Observability Experience Lead — Dynatrance*

Gala Dvoretskaya believes the best developer tools disappear into the background, letting engineers focus on solving problems instead of fighting complexity. Leading Observability Experience at Dynatrace, she drives the strategy for next-generation AI-powered observability, bringing together product, engineering, design, and customer insights to shape how developers understand and optimize modern software systems.

Before joining Dynatrace, Gala founded a venture-backed startup and has spent her career building products, leading global teams, and turning complex technical challenges into intuitive experiences .She is passionate about the intersection of AI, observability, and product design, creating products that engineers genuinely love to use.
