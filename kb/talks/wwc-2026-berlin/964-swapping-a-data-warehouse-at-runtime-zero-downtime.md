---
id: 964
title: "Swapping a Data Warehouse at Runtime: Zero-Downtime Migration Without Changing a Single Client"
slug: swapping-a-data-warehouse-at-runtime-zero-downtime
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Data & Databases"
type: "Keynote/Talk"
stage: "Stage 10 - powered by TikTok"
tags: ["Apache Iceberg", "Data Lakes", "DuckDB", "Lakehouse", "Performance", "Python", "Rust", "SQL"]
speakers: ["Max Fischer", "Michael O'Toole"]
speaker_companies: ["Trade Republic"]
day: 2
starts_at: 2026-07-10T12:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=iFtXbl-lMew
video_id: iFtXbl-lMew
session_page: https://app.wearedevelopers.com/events/16/session/964
transcript: false
---

# Swapping a Data Warehouse at Runtime: Zero-Downtime Migration Without Changing a Single Client

**Max Fischer (Director Engineering — Trade Republic), Michael O'Toole (Data Staff Engineer — Trade Republic)**

`Track: Data & Databases` · `Type: Keynote/Talk` · `Stage: Stage 10 - powered by TikTok`

`#Apache Iceberg` `#Data Lakes` `#DuckDB` `#Lakehouse` `#Performance` `#Python` `#Rust` `#SQL`

[Watch the recording](https://www.youtube.com/watch?v=iFtXbl-lMew) · [Session page](https://app.wearedevelopers.com/events/16/session/964)

## Abstract

Trade Republic serves 10 million with €150 billion under management. Our data warehouse handles 4 million queries daily across analytics, product features, and the ML fraud detection that protects our customers. It replicates 220 databases into a 620 TB lakehouse. It cannot go down.

Moving to an open lakehouse architecture — Apache Iceberg & bring-your-own-compute  — "schedule a maintenance window" was not an option. Neither was asking hundreds of consumers — BI tools, pipelines, ML models, product services — to rewrite their connections.

The destination: decoupled storage-compute where teams choose the engine that fits their workload. Spark, Athena, DuckDB — all reading from the Iceberg. But the migration path matters as much as the destination.

Our approach: "Engy" build a protocol-compatible proxy that presents the exact wire interface of our existing warehouse. Every client connects the same way it always has. Behind that stable interface, we're free to change everything: swap compute engines, cache, add features — all invisible to consumers.

The key enabler is in-flight SQL transpilation. The proxy rewrites SQL, translates table references between catalogs, and normalises result, all in the request path. This gives us a multi-engine architecture with perfect interop.

Teams onboard without changing a driver, a connection string, or a line of code. We ship new engines and features behind the interface while production traffic is flowing — building the plane as we fly it. The interface becomes a contract that decouples the pace of infrastructure evolution from the pace of consumer adoption.

In this talk I'll walk through how we designed the Engy proxy interface for long-term stability that lets us migrate a 620 TB system query-by-query without downtime.

True to Trade Republic's engineering philosophy, the entire stack is built on open-source foundations — no vendor tooling, no proprietary middleware.

## Speakers

### Max Fischer

*Director Engineering — Trade Republic*

Director Engineering Trade Republic, responsible for the Engineering, Data and Cyber Security organisation.
Earlier CTO Bluestep Bank, VP Klarna, Executive VP Nordea, Chief Business Architect SEB, Chief Architect TeliaSonera

### Michael O'Toole

*Data Staff Engineer — Trade Republic*

Michael O'Toole is a Staff Engineer at Trade Republic. Over the past decade he's been building, breaking, and migrating data platforms across Europe and across the pong. When he's not obsessing over query performance, he plays in TwoFoxOut. He brings the same energy to both — loud, fast, and no unnecessary downtime.
