---
id: 692
title: "From Static Rules to Reasoning Platforms: Scaling Intelligent Canary Delivery in 2026"
slug: from-static-rules-to-reasoning-platforms-scaling
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "DevOps"
type: "Keynote/Talk"
stage: "Stage 8 - powered by Red Hat"
tags: ["Agentic AI", "ArgoCD", "CI/CD", "Internal Platforms"]
speakers: ["Daniel Oh"]
speaker_companies: ["IBM"]
day: 1
starts_at: 2026-07-09T11:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=BImFCfZmb50
video_id: BImFCfZmb50
session_page: https://app.wearedevelopers.com/events/16/session/692
transcript: false
---

# From Static Rules to Reasoning Platforms: Scaling Intelligent Canary Delivery in 2026

**Daniel Oh (Senior Principal Developer Advocate — IBM)**

`Track: DevOps` · `Type: Keynote/Talk` · `Stage: Stage 8 - powered by Red Hat`

`#Agentic AI` `#ArgoCD` `#CI/CD` `#Internal Platforms`

[Watch the recording](https://www.youtube.com/watch?v=BImFCfZmb50) · [Session page](https://app.wearedevelopers.com/events/16/session/692)

## Abstract

As organizations scale their Kubernetes footprint, the "Day 2" reality of GitOps becomes clear: static thresholds are brittle. Standard Canary rollouts rely on fixed Prometheus queries (e.g., Error Rate < 1%), but these rules lack the context to distinguish between a minor transient blip and a systemic failure. For Platform Engineers, this results in "Alert Fatigue" and manual "promotion" gates that slow down the delivery pipeline.
In 2026, we are moving from Static Automation to Reasoning Platforms.
This session explores how to evolve your delivery infrastructure into an intelligent system that doesn't just follow rules, but reasons through data. We will demonstrate how to wrap ArgoCD Rollouts with an Agentic Reasoning Layer capable of cross-referencing metrics, logs, and distributed traces to make autonomous "Go/No-Go" decisions.

We will trigger a Canary deployment that passes basic health checks but introduces a "silent failure" (e.g., a cache hit-rate drop causing downstream latency). You will see the Reasoning Platform detect the anomaly, pause the rollout, "investigate" the root cause, and present a natural-language justification for the automated rollback.

## Speakers

### Daniel Oh

*Senior Principal Developer Advocate — IBM*

Daniel Oh is a Java Champion and Senior Principal Developer Advocate at IBM, where he leads efforts to advance cloud native innovation through open source technologies. Renowned for his ability to bridge technical and collaborative gaps, he empowers developers and organizations to build transformative solutions from AI-driven applications and serverless architectures to resilient microservices. As a CNCF Ambassador and TAG DevEx co-chair, Daniel actively shapes the cloud native ecosystem, fostering partnerships between enterprise developers, AI engineers, and platform engineering teams to accelerate hybrid cloud adoption. His technical leadership extends beyond code contributions, as he mentors communities and champions strategies that enable businesses to thrive in evolving digital landscapes. A dynamic storyteller and educator, Daniel captivates global audiences through keynote speeches, workshops, and interactive sessions, where he demystifies emerging technologies and inspires the tech community to embrace the future of open source innovation.
