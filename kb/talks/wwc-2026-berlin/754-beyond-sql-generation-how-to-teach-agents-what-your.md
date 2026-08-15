---
id: 754
title: "Beyond SQL Generation: How to Teach Agents What Your Database Actually Means"
slug: beyond-sql-generation-how-to-teach-agents-what-your
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Data & Databases"
type: "Keynote/Talk"
stage: "Stage 12"
tags: ["AI Coding Assistants", "Databases"]
speakers: ["Celeste Horgan"]
speaker_companies: ["Snowflake"]
day: 1
starts_at: 2026-07-09T13:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=vd6Hfb9WW_o
video_id: vd6Hfb9WW_o
session_page: https://app.wearedevelopers.com/events/16/session/754
transcript: false
---

# Beyond SQL Generation: How to Teach Agents What Your Database Actually Means

**Celeste Horgan (Senior Developer Advocate — Snowflake)**

`Track: Data & Databases` · `Type: Keynote/Talk` · `Stage: Stage 12`

`#AI Coding Assistants` `#Databases`

[Watch the recording](https://www.youtube.com/watch?v=vd6Hfb9WW_o) · [Session page](https://app.wearedevelopers.com/events/16/session/754)

## Abstract

Coding agents like Claude struggle to get meaningful information from databases. Even though they're good at writing correct SQL, they fall short where it matters - fetching the right answers. When asked a complex question, they consistently fumble their way through the schema catalogs and table descriptions, and then make best-guesses about how to join them, hoping to find some data that looks reasonable.

The reason for this is simple - they don't know your domain. It's like hiring an expert in database syntax and expecting them to know how your company works. The solution is equally simple - teach the agent what the data means. Give them a guide to how your database is laid out, how its joined, what column names mean and what kind of queries make sense. All the folk knowledge that that expert hire would eventually acquire in their first 6 months.

The technique for teaching agents the meaning of a schema is called a semantic model, there's an open standard that's easy to stick to, and the results are pretty terrific. A single file can take an agent from burning tokens to hallucinate an answer, to one-shotting the correct results.

In this talk we'll go through the details of semantic models and the standard, why it's worth using the standard rather than rolling your own, and techniques for creating effective semantic models quickly. All in the service of a simple outcome - making a scalable database analyst that's effective from day one.

## Speakers

### Celeste Horgan

*Senior Developer Advocate — Snowflake*

Celeste is a Sr. OSS Developer Advocate at Snowflake, focusing on open source data communities. She is a previous member of Kubernetes SIG Docs, founded the Inclusive Naming Committee at the Linux Foundation, and is a regular speaker on open source data topics for the past 3 years. Her work on inclusive language in tech has been featured in the New York Times. She currently resides in London, UK.
