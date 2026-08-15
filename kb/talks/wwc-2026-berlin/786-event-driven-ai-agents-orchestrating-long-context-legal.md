---
id: 786
title: "Event-Driven AI Agents: Orchestrating Long-Context Legal Processing at Scale"
slug: event-driven-ai-agents-orchestrating-long-context-legal
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Agents"
type: "Keynote/Talk"
stage: "Stage 3 - powered by AWS"
tags: ["Anthropic", "AWS", "Agents", "Agentic AI", "CDK", "Event-Driven Architecture (EDA)"]
speakers: ["Luca Bianchi"]
speaker_companies: ["MESA"]
day: 1
starts_at: 2026-07-09T14:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=TgSEdc2Pu_I
video_id: TgSEdc2Pu_I
session_page: https://app.wearedevelopers.com/events/16/session/786
transcript: false
---

# Event-Driven AI Agents: Orchestrating Long-Context Legal Processing at Scale

**Luca Bianchi (CTIO — MESA)**

`Track: AI Agents` · `Type: Keynote/Talk` · `Stage: Stage 3 - powered by AWS`

`#Anthropic` `#AWS` `#Agents` `#Agentic AI` `#CDK` `#Event-Driven Architecture (EDA)`

[Watch the recording](https://www.youtube.com/watch?v=TgSEdc2Pu_I) · [Session page](https://app.wearedevelopers.com/events/16/session/786)

## Abstract

Building AI agents that process legal documents with 10,000+ pages requires more than throwing context at an LLM. This talk dissects our production event-driven architecture.

You'll learn:
- Why synchronous LLM calls fail at legal document scale - the cold start and a timeout problem
- Event-driven orchestration patterns for multi-step agent workflows (planning, dynamic loading, context assembly)
- Long-context chunking strategies that preserve legal reasoning chains
- Cost optimization: how we reduced per-request costs 73% through intelligent caching and selective context loading
- Production failure modes: what breaks when agents plan incorrectly

Concrete architecture, real metrics, battle-tested patterns. No theoretical frameworks - this is what actually runs in production, processing legal contracts for 10M+ users.

## Speakers

### Luca Bianchi

*CTIO — MESA*

Over the past decade, I've architected production AI/ML systems processing
100M+ daily events through event-driven serverless architectures. AWS Serverless
Hero and Cursor Ambassador focused on cost-optimized AI infrastructure and real-time data pipelines.

Production track record:
- Built production AI Agents for legal domains, managing very long contexts,
  planning, and dynamic loading through event-driven orchestration
- Built production GenAI platform serving 500K+ requests/day with <200ms p95 latency
- Scaled cloud SaaS to 10M+ users, reducing p99 latency from 2s to 1.2s through
  event-driven architecture migration
- Migrated 80% of workloads to serverless event-driven patterns, cutting
  infrastructure costs 10x while improving deployment velocity

Led engineering teams of 100+ through cultural transformation toward continuous
delivery and experimentation-driven development. Co-founder of the Serverless Italy
community, Milano Mongo User Group, and Cursor Meetup Milano.
