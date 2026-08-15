---
id: 792
title: "Building a Multi-Agent Orchestration Engine That Actually Follows the Rules"
slug: building-a-multi-agent-orchestration-engine-that-actually
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Agents"
type: "Keynote/Talk"
stage: "Stage 9"
tags: ["AI Models", "AI Standards", "Agentic AI", "Code Generation", "LangChain", "Multi-Agent Systems"]
speakers: ["Hussein Jundi", "Torsten Stiller"]
speaker_companies: ["E.ON Digital"]
day: 1
starts_at: 2026-07-09T14:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=r_6KVdMEIUA
video_id: r_6KVdMEIUA
session_page: https://app.wearedevelopers.com/events/16/session/792
transcript: false
---

# Building a Multi-Agent Orchestration Engine That Actually Follows the Rules

**Hussein Jundi (AI Engineering Lead — E.ON Digital), Torsten Stiller (Head of Automation Factory — E.ON Digital)**

`Track: AI Agents` · `Type: Keynote/Talk` · `Stage: Stage 9`

`#AI Models` `#AI Standards` `#Agentic AI` `#Code Generation` `#LangChain` `#Multi-Agent Systems`

[Watch the recording](https://www.youtube.com/watch?v=r_6KVdMEIUA) · [Session page](https://app.wearedevelopers.com/events/16/session/792)

## Abstract

At E.ON Digital Technology, we're building an AI-powered platform that spans the entire software development lifecycle—from ideation, requirements in Jira, through code generation and GitLab integration, to automated testing, infrastructure deployment, and production monitoring.

Enterprise environments don't tolerate agents going off script. We need them to follow our SDLC guardrails, and not to improvise.

While the workflow itself enforces standards, the graph controls transitions, embeds approval gates, and ensures compliance. Users just chat; the system handles the rest.

We'll walk through the architecture and share real examples: legacy application modernization, cloud-native migrations, and gains in developer productivity.

The Problem

AI coding assistants are powerful, but they're designed for autonomy. In an enterprise like E.ON, that's a problem. We have governance requirements, approval workflows, and integration points across the entire SDLC—Jira for planning, GitLab for code, our automation platform for deployments, our monitoring stack for observability. Letting an agent "figure it out" isn't an option.

What We Built

We created a multi-agent platform based on LangGraph where:

-Specialized agents handle distinct phases: requirements analysis, code generation, test creation, infrastructure provisioning, log analysis

-The workflow graph enforces our SDLC—agents don't decide when to ask for approval or which phase comes next; the graph does

-Graph disaggregation: the workflow breaks down complex tasks into manageable steps, improving task completion rates and reducing hallucinations

-Enterprise integrations connect each phase to our actual toolchain (Jira, GitLab, deployment automation, monitoring)

-Workflows are pluggable—different use cases get different flows with appropriate checkpoints

The result: developers interact through a conversational interface, but the underlying system enforces similar standards we'd expect from manual processes.

## Speakers

### Hussein Jundi

*AI Engineering Lead — E.ON Digital*

Hussein Jundi is a Munich-based AI Engineering Lead who enjoys turning ambiguous ideas into real, scalable solutions. At E.ON Digital Technology, he drives AI engineering projects across E.ON’s cloud native software engineering technology platforms, assessing new capabilities and leading initiatives that accelerate modernization and AI utilization. Previously, he led Data & AI squads at E.ON and helped build and scale data platforms that power reliable analytics and product development in the mobility/charging space.

### Torsten Stiller

*Head of Automation Factory — E.ON Digital*

Torsten Stiller is a seasoned tech leader and speaker, currently heading the Automation Factory Domain at E.ON Digital Technology. A former Microsoft and NVIDIA professional, he brings deep experience in cloud-native platforms, automation, and digital transformation. Torsten is passionate about the responsible use of AI and sustainable software engineering, combining hands-on expertise with strategic vision to drive ethical, impactful innovation.
