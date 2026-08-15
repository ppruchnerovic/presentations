---
id: 875
title: "Hard Problems Hide in Boring Places: Turning Accounting Workflows into AI Products"
slug: hard-problems-hide-in-boring-places-turning-accounting
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Engineering"
type: "Keynote/Talk"
stage: "Airstream 1"
tags: ["Automation", "Data", "Large Language Models (LLMs)", "Security", "Software Architecture"]
speakers: ["Oleksandr Korotkykh", "Tolga Sümer"]
speaker_companies: ["Pliant"]
day: 2
starts_at: 2026-07-10T08:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=v_u6NpIAwzk
video_id: v_u6NpIAwzk
session_page: https://app.wearedevelopers.com/events/16/session/875
transcript: false
---

# Hard Problems Hide in Boring Places: Turning Accounting Workflows into AI Products

**Oleksandr Korotkykh (CTO — Pliant), Tolga Sümer (Senior Software Engineer — Pliant)**

`Track: AI Engineering` · `Type: Keynote/Talk` · `Stage: Airstream 1`

`#Automation` `#Data` `#Large Language Models (LLMs)` `#Security` `#Software Architecture`

[Watch the recording](https://www.youtube.com/watch?v=v_u6NpIAwzk) · [Session page](https://app.wearedevelopers.com/events/16/session/875)

## Abstract

Accounting and B2B payments are often seen as boring, solved problems — until you try to apply AI to them. The moment a system can misread an invoice, suggest the wrong action, or leak sensitive financial data, “cool AI demos” turn into serious engineering challenges.

In this talk, I’ll share how we at Pliant build AI features in one of the most constrained domains possible, where correctness, trust, auditability, and permissions are non-negotiable. Instead of treating LLMs as smart oracles, we design them as untrusted components that propose actions, operate on structured data, and are constrained by strict policies and approval flows.

We’ll walk through concrete patterns for turning existing accounting workflows into real AI products: grounding models in financial data, using schemas instead of free text, enforcing authorization at the system level, and designing human-in-the-loop interactions that users actually trust. Along the way, I’ll share failure modes we hit in production and how we fixed them.

This talk is about where innovation really happens: not in flashy demos, but in making AI work reliably in the places where mistakes are expensive.

## Speakers

### Oleksandr Korotkykh

*CTO — Pliant*

Alex Korotkykh is a fintech engineering leader with over 15 years of experience building large-scale, regulated software systems. Originally from Ukraine, he has been living and working in Germany for more than 10 years.

He has spent most of his career in fintech and data-driven products, working at companies such as Kreditech, figo, and Zalando, where he helped design, build, and scale complex platforms at the intersection of finance, data, and software engineering.

Alex joined Pliant at a very early stage and now leads its technology organisation of nearly 100 people, focusing on scalable architecture, security, and building reliable AI-powered products for B2B payments and accounting.

### Tolga Sümer

*Senior Software Engineer — Pliant*

I’m a Senior Software Engineer based in Berlin, currently working at Pliant, where I build internal and customer-facing AI features. My focus is on designing end-to-end AI workflows that combine multiple agents, tools, and data sources, from BI-style database interactions to RAG-based systems. Before moving into AI, I spent several years working on integrations, building APIs and connecting Pliant with accounting and PayOps platforms like DATEV, Lexoffice, and Circula, as well as helping shape our Partner API.

Before Pliant, I worked on large-scale backend systems in telecom and enterprise software, mainly around integrations, and high-throughput data pipelines. Earlier on, I explored game development and computer vision through internships and student roles, which helped shape my interest in building things end to end. I enjoy working on complex systems, turning ideas into production-ready solutions, and learning new technologies along the way.
