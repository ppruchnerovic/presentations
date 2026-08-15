---
id: 616
title: "Your Distributed System Just Got a Brain. Now What?"
slug: your-distributed-system-just-got-a-brain-now-what
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Software Architecture"
type: "Lightning Talk"
stage: "Airstream 2"
tags: ["AI Standards", "Cross-Platform", "Distributed Systems", "Large Language Models (LLMs)", "Microservices", "Scaling", "System Design"]
speakers: ["Marcin Makowski"]
speaker_companies: ["BeOne"]
day: 1
starts_at: 2026-07-09T08:40:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=VBDnbJx2EEE
video_id: VBDnbJx2EEE
session_page: https://app.wearedevelopers.com/events/16/session/616
transcript: false
---

# Your Distributed System Just Got a Brain. Now What?

**Marcin Makowski (CEO — BeOne)**

`Track: Software Architecture` · `Type: Lightning Talk` · `Stage: Airstream 2`

`#AI Standards` `#Cross-Platform` `#Distributed Systems` `#Large Language Models (LLMs)` `#Microservices` `#Scaling` `#System Design`

[Watch the recording](https://www.youtube.com/watch?v=VBDnbJx2EEE) · [Session page](https://app.wearedevelopers.com/events/16/session/616)

## Abstract

Distributed systems were designed around predictable behavior.

Retries assume idempotency. State transitions assume determinism. Consistency models assume repeatable outcomes.

Then we added AI.

Now:
- the same input may produce different outputs
- retries may change decisions
- context mutates state unpredictably
- model upgrades alter behavior silently
- deterministic workflows depend on probabilistic components

Your distributed system just got a brain.
And distributed systems don’t tolerate ambiguity.

In this session, we explore what really changes when AI becomes part of a distributed architecture.

We’ll cover:
- how probabilistic inference breaks retry semantics
- why idempotency assumptions fail with LLMs
- separating state from inference
- deterministic checkpoints in AI workflows
- replayable execution paths
- handling model version drift
- designing hybrid architectures where AI proposes - but systems enforce

AI doesn’t just add intelligence. It changes the fundamental assumptions of your system design.

If you treat AI as just another microservice, your architecture will eventually collapse.

## Speakers

### Marcin Makowski

*CEO — BeOne*

Marcin Makowski is CEO at BeOne and a software architect focused on building production-grade AI and orchestration platforms. With over 20 years of experience in distributed systems, enterprise automation, and large-scale process execution, he specializes in designing deterministic architectures in non-deterministic environments.
Marcin works at the intersection of AI infrastructure, workflow orchestration, and decision modeling. His recent focus includes LLM platform engineering, model gateways, hybrid retrieval architectures, and building reproducible AI systems with strong observability and auditability guarantees.
He is a strong advocate of open ecosystems and engineering-first approaches to AI adoption. Instead of treating AI as a feature, he designs it as a runtime component that must meet the same standards of reliability, scalability, and traceability as any other production system.
Marcin co-authored research on dynamic decision model generation for tax compliance (accepted at ISD 2025) and regularly speaks about distributed systems, AI platform design, and deterministic orchestration in intelligent systems.
