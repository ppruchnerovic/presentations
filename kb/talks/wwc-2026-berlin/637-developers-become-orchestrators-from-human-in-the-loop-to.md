---
id: 637
title: "Developers become Orchestrators: From Human-in-the-Loop to Spec-in-the-Loop"
slug: developers-become-orchestrators-from-human-in-the-loop-to
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Developer Experience"
type: "Keynote/Talk"
stage: "Stage 3 - powered by AWS"
tags: ["AI Coding Assistants", "APIs", "Agents", "Automation", "Developer Experience (DevEx)", "Generative AI (GenAI)", "Governance", "Microservices", "Test-Driven Development (TDD)"]
speakers: ["Bastian Heilemann", "Stefan Bley"]
speaker_companies: ["Carl Zeiss", "ZEISS Digital Innovation"]
day: 1
starts_at: 2026-07-09T09:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=M74vomMsLRQ
video_id: M74vomMsLRQ
session_page: https://app.wearedevelopers.com/events/16/session/637
transcript: false
---

# Developers become Orchestrators: From Human-in-the-Loop to Spec-in-the-Loop

**Bastian Heilemann (Lead Cloud Solution Architect — Carl Zeiss), Stefan Bley (Software Architect — ZEISS Digital Innovation)**

`Track: Developer Experience` · `Type: Keynote/Talk` · `Stage: Stage 3 - powered by AWS`

`#AI Coding Assistants` `#APIs` `#Agents` `#Automation` `#Developer Experience (DevEx)` `#Generative AI (GenAI)` `#Governance` `#Microservices` `#Test-Driven Development (TDD)`

[Watch the recording](https://www.youtube.com/watch?v=M74vomMsLRQ) · [Session page](https://app.wearedevelopers.com/events/16/session/637)

## Abstract

Development teams still struggle with a fundamental question: what can we safely delegate to AI, and what must remain human-owned?
Despite rapid progress in AI tooling, most teams are stuck in “copilot mode” — gaining speed, but also increasing cognitive load, risk, and inconsistency.

In this talk, we show why and how the role of the developer must evolve: from writing code and managing endless shift-left concerns, to designing intent, constraints, and guarantees — and orchestrating AI-driven execution.

We introduce spec-driven development as a governance and execution model for AI-assisted software delivery. Instead of focusing on prompts or tools, we frame AI delegation as a risk- and criticality-aware decision: humans define what must be true (functional specs, architecture decisions, security, SRE, and compliance constraints), and AI is delegated everything else.

To make this concrete, we present a realistic end-to-end experiment:
a non-critical internal service built with maximum AI delegation. Humans provide: Functional specifications and ADRs, Non-functional requirements (security, reliability, coding standards) and Release and compliance constraints

From there, AI generates implementation, tests, CI/CD pipelines, packaging, and deployment artifacts — fully automated.

On stage, we demonstrate how changing a specification (for example an SLO or security requirement) triggers repeatable, auditable regeneration of code and infrastructure — without manual re-implementation. We deliberately push this approach to its limits to show where it works, where it breaks, and why it must never be applied blindly to critical systems.

Attendees will leave with:

A clear understanding of the guardrails required for safe AI delegation.
A practical delegation matrix for AI-assisted development.
A mental model for specifications as an execution boundary, not documentation.
A realistic, experience-based view of fully automated delivery for low- and medium-critical systems.

## Speakers

### Bastian Heilemann

*Lead Cloud Solution Architect — Carl Zeiss*

Studied mathematics and computer science. Software developer roles across multiple industries. Moved on to the Software Architect role and leading role. Since 09/2022 Lead Cloud Native Solution Architect at Zeiss.

### Stefan Bley

*Software Architect — ZEISS Digital Innovation*

Stefan is a software architect at ZEISS Digital Innovation in Berlin and has worked on various Angular projects in different industries throughout his career. He loves experimenting with new technologies and sharing his knowledge by speaking at conferences and contributing at community events. Recently, he has been leading an engineering design team focused on leveraging micro frontend architecture for performant healthcare digitization.
