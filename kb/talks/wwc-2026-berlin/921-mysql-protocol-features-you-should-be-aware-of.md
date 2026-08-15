---
id: 921
title: "MySQL Protocol Features You Should Be Aware Of"
slug: mysql-protocol-features-you-should-be-aware-of
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Data & Databases"
type: "Lightning Talk"
stage: "Airstream 1"
tags: ["Databases", "MySQL", "Networking", "SQL"]
speakers: ["Daniël van Eeden"]
speaker_companies: ["PingCAP"]
day: 2
starts_at: 2026-07-10T10:35:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=PqrERF7rmkM
video_id: PqrERF7rmkM
session_page: https://app.wearedevelopers.com/events/16/session/921
transcript: false
---

# MySQL Protocol Features You Should Be Aware Of

**Daniël van Eeden (Technical Support Engineer — PingCAP)**

`Track: Data & Databases` · `Type: Lightning Talk` · `Stage: Airstream 1`

`#Databases` `#MySQL` `#Networking` `#SQL`

[Watch the recording](https://www.youtube.com/watch?v=PqrERF7rmkM) · [Session page](https://app.wearedevelopers.com/events/16/session/921)

## Abstract

This talk goes over some less used protocol features like Connection Attributes, Query Attributes, Session Tracking and zstd compression.

These features can help you to create better integrations and applications.

Connection Attributes are somewhat more known, but many people don't know that applications can (and should) add their own information.

And where Connection Attributes are connection based, Query attributes are query based. These are useful today, but they also have the potential to help with future improvements.

And Session Tracking can really help in cases where you write to a primary and then read from a replica. This can give you the GTID from the commit so you can wait for that when reading from the replica. This could replace cases where you would now directly read from the primary to get the read-after-write behavior that you need.

And compression has been in the protocol for a long time, but this was always based on zlib. Now zstandard has entered the picture.

## Speakers

### Daniël van Eeden

*Technical Support Engineer — PingCAP*

Daniël has been working on TiDB and related projects. Before that he worked on scaling MySQL for a large company that sells hotel rooms. One of the side projects he has been working in is the MySQL protocol dissector in Wireshark.
