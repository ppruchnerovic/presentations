---
id: 735
title: "TiDB, One Layer at a Time: How Distributed SQL Became an Agentic AI Backbone"
slug: tidb-one-layer-at-a-time-how-distributed-sql-became-an
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Data & Databases"
type: "Keynote/Talk"
stage: "Stage 12"
tags: ["Agentic AI", "Databases", "Distributed Systems", "Multi-Cloud", "Open Source", "Scaling", "SQL", "Vector Databases"]
speakers: ["Daniël van Eeden", "Mattias Jonsson"]
speaker_companies: ["PingCAP", "TiDB"]
day: 1
starts_at: 2026-07-09T12:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=FzIkKiYJU-Q
video_id: FzIkKiYJU-Q
session_page: https://app.wearedevelopers.com/events/16/session/735
transcript: false
---

# TiDB, One Layer at a Time: How Distributed SQL Became an Agentic AI Backbone

**Daniël van Eeden (Technical Support Engineer — PingCAP), Mattias Jonsson (Principal Software Engineer — TiDB)**

`Track: Data & Databases` · `Type: Keynote/Talk` · `Stage: Stage 12`

`#Agentic AI` `#Databases` `#Distributed Systems` `#Multi-Cloud` `#Open Source` `#Scaling` `#SQL` `#Vector Databases`

[Watch the recording](https://www.youtube.com/watch?v=FzIkKiYJU-Q) · [Session page](https://app.wearedevelopers.com/events/16/session/735)

## Abstract

Every distributed database is a stack of hard problems solved in order, and the order tells a story. This talk traces how TiDB grew, layer by layer, from a single idea into a system now serving agentic AI platforms.
It began over a decade ago with one job: speak SQL, but scale beyond a single machine. That demanded a distributed storage layer that could grow writes and capacity horizontally, and then a brain to keep that storage balanced, available, and consistent as machines come and go. Three layers, three clean responsibilities: a MySQL-compatible SQL engine, a Raft-replicated key-value store, and a placement driver. That separation is why the system kept absorbing new use cases, real-time analytics, change streaming, Vector and full text search, each as a new layer rather than a rewrite.
Then the twist: none of this was designed for AI. Yet the very properties that make a good distributed database, elastic scale, strong consistency, fresh data, a clean interface, turn out to be exactly what AI agents need from their data backbone.

## Speakers

### Daniël van Eeden

*Technical Support Engineer — PingCAP*

Daniël has been working on TiDB and related projects. Before that he worked on scaling MySQL for a large company that sells hotel rooms. One of the side projects he has been working in is the MySQL protocol dissector in Wireshark.

### Mattias Jonsson

*Principal Software Engineer — TiDB*

Mattias is a Principal Software Engineer at PingCAP, where he works on TiDB's SQL layer and currently on the optimizer's statistics management. He has worked with databases, and MySQL in particular, for more than 20 years. Before PingCAP he spent years at Booking.com working with MySQL at scale, and earlier worked on the MySQL Server code at MySQL AB, Sun, and Oracle. Table partitioning is a recurring theme across his career: he built native partitioning in InnoDB for MySQL, and global indexes for partitioned tables in TiDB.
