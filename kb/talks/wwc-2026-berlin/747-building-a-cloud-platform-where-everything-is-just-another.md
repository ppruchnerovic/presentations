---
id: 747
title: "Building a Cloud Platform Where Everything is Just Another Kubernetes Resource"
slug: building-a-cloud-platform-where-everything-is-just-another
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Cloud & AI Infrastructure"
type: "Keynote/Talk"
stage: "Stage 5"
tags: ["Automation", "DevOps", "DevSecOps", "GitOps", "Infrastructure", "Infrastructure as Code (IaC)"]
speakers: ["Patrick Koss"]
speaker_companies: ["STACKIT"]
day: 1
starts_at: 2026-07-09T13:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=jT5yIs8tvgQ
video_id: jT5yIs8tvgQ
session_page: https://app.wearedevelopers.com/events/16/session/747
transcript: false
---

# Building a Cloud Platform Where Everything is Just Another Kubernetes Resource

**Patrick Koss (Tech Lead — STACKIT)**

`Track: Cloud & AI Infrastructure` · `Type: Keynote/Talk` · `Stage: Stage 5`

`#Automation` `#DevOps` `#DevSecOps` `#GitOps` `#Infrastructure` `#Infrastructure as Code (IaC)`

[Watch the recording](https://www.youtube.com/watch?v=jT5yIs8tvgQ) · [Session page](https://app.wearedevelopers.com/events/16/session/747)

## Abstract

At STACKIT, we took the Kubernetes API and turned it into our entire platform control plane. Not just for running containers. For everything. S3 buckets, databases, DNS records, IAM credentials, even entire child Kubernetes clusters. All defined as YAML manifests. All managed via GitOps. All continuously reconciled by controllers.
We started with Terraform like everyone else. It worked fine until our infrastructure got complex. Monolithic state files that locked the whole team. Slow applies that recalculated everything when we only needed to change one thing. Drift that only surfaced when someone remembered to run a plan.
So we rebuilt the platform on Crossplane and ArgoCD. One management cluster provisions and orchestrates cloud infrastructure per environment. Developers get self-service APIs by applying Kubernetes resources. Ops teams enforce policies through admission webhooks. Everything reconciles in real-time. No external state to manage. No waiting for tickets to get unblocked.
This is the production architecture. How it works, why we designed it this way, what went wrong during the migration, and what we'd change if we started over today.

## Speakers

### Patrick Koss

*Tech Lead — STACKIT*

I'm a dedicated and highly skilled Tech Lead with a strong passion for Distributed Systems and Cloud-Native Development.

My key areas of expertise include:
- Backend Development (Go, Python, Rust)
- Distributed Systems (Microservices, Service Mesh, Message Queues)
- Cloud-Native Technologies (Kubernetes, Docker, Serverless)
- Scalable & High-Performance Systems
- Continuous Integration & Deployment (CI/CD)
