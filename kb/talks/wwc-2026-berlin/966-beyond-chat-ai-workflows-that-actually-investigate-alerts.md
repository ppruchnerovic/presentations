---
id: 966
title: "Beyond Chat: AI Workflows That Actually Investigate Alerts (So You Don't Have To Know Everything)"
slug: beyond-chat-ai-workflows-that-actually-investigate-alerts
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "DevOps"
type: "Keynote/Talk"
stage: "Stage 12"
tags: ["Automation", "DevOps", "Generative AI (GenAI)", "LLMOps", "Site Reliability Engineering (SRE)", "Workflow Automation"]
speakers: ["Aram Hakobyan", "Nune Isabekyan"]
speaker_companies: ["OpsWorker", "zooplus"]
day: 2
starts_at: 2026-07-10T12:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=fK6Ck1OdvoI
video_id: fK6Ck1OdvoI
session_page: https://app.wearedevelopers.com/events/16/session/966
transcript: false
---

# Beyond Chat: AI Workflows That Actually Investigate Alerts (So You Don't Have To Know Everything)

**Aram Hakobyan (Head of Platform Engineering — zooplus), Nune Isabekyan (CTO — OpsWorker)**

`Track: DevOps` · `Type: Keynote/Talk` · `Stage: Stage 12`

`#Automation` `#DevOps` `#Generative AI (GenAI)` `#LLMOps` `#Site Reliability Engineering (SRE)` `#Workflow Automation`

[Watch the recording](https://www.youtube.com/watch?v=fK6Ck1OdvoI) · [Session page](https://app.wearedevelopers.com/events/16/session/966)

## Abstract

"You build it, you run it" sounds great until you're on-call for a Kafka consumer lag spike at 3 AM—and you spent the last six months building the React frontend, not the event pipeline. Modern teams own their services end-to-end, but no one can be an expert in everything. And the AI chatbots we've been promised? They just add another window to alt-tab through while the pager screams.

This talk argues that chat-based AI is fundamentally wrong for incident investigation. I'll break down why the chat paradigm fails: it expects you to provide context you don't have at 3 AM, assumes you know where to look, burns time with back-and-forth, and interrogates instead of investigates.

Then I'll show what actually works: AI workflows that investigate like a teammate who knows the system—automatically discovering affected resources, correlating metrics with deployments, querying the right logs without being asked, and delivering hypotheses with evidence.

We'll cover real engineering challenges: orchestrating tools across Kubernetes, logs, and metrics; solving the "where do I even start?" problem; building outputs that explain unfamiliar systems; and what breaks when you let AI loose on production.

Live Demo: A simulated 3 AM alert comparing the chatbot experience ("Can you tell me more about your cluster configuration?") versus a workflow that delivers: "Your deployment rolled out 47 minutes ago with a memory limit reduction. Three pods are OOMKilling. Here's the diff and the kubectl command to rollback."

## Speakers

### Aram Hakobyan

*Head of Platform Engineering — zooplus*

Platform Engineering Lead and Infrastructure Expert with over 25 years of experience designing and operating highly scalable, distributed systems. Currently serving as Head of Platform Engineering at zooplus SE, where I lead container orchestration and observability teams, running 40 k8s clusters and 3000 microservices, supporting one of Europe's largest online pet retailers.

### Nune Isabekyan

*CTO — OpsWorker*

Nune Isabekyan is a Berlin-based founder and cloud architecture expert with over 15 years of experience building scalable, intelligent systems. With a mathematics background and deep expertise in AWS, AI, and DevOps, she specializes in practical AI implementation and cloud-native architectures.
As founder and CTO of OpsWorker, Nune is building AI-powered alert investigation automation. When an alert fires, OpsWorker automatically investigates, pulls logs, checks dashboards, correlates events, and gives on-call engineers a summary of what's wrong and suggested next steps. Previously, as CIO of powerdata GmbH, she led teams building SaaS products and AI-powered customer service automation for the utilities sector. Her earlier career includes engineering roles at Teradata, Amadeus, and high-scale startups handling millions of daily users.
