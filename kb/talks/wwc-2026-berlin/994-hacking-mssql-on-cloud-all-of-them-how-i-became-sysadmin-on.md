---
id: 994
title: "Hacking MSSQL on Cloud. All of them. How I became sysadmin on Azure, AWS, GCP and Alibaba."
slug: hacking-mssql-on-cloud-all-of-them-how-i-became-sysadmin-on
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Security & Privacy"
type: "Keynote/Talk"
stage: "Stage 9"
tags: ["Cloud Security", "Databases", "Microsoft SQL Server", "Security"]
speakers: ["Fabiano Amorim"]
speaker_companies: ["Pythian"]
day: 2
starts_at: 2026-07-10T13:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=B-UUA_XBaG0
video_id: B-UUA_XBaG0
session_page: https://app.wearedevelopers.com/events/16/session/994
transcript: false
---

# Hacking MSSQL on Cloud. All of them. How I became sysadmin on Azure, AWS, GCP and Alibaba.

**Fabiano Amorim (Principal Consultant — Pythian)**

`Track: Security & Privacy` · `Type: Keynote/Talk` · `Stage: Stage 9`

`#Cloud Security` `#Databases` `#Microsoft SQL Server` `#Security`

[Watch the recording](https://www.youtube.com/watch?v=B-UUA_XBaG0) · [Session page](https://app.wearedevelopers.com/events/16/session/994)

## Abstract

It started as a simple security research project on a local SQL Server instance. A single vulnerability led me down a rabbit hole — from compromising Azure SQL Database to successfully escalating privileges on GCP CloudSQL for SQL Server, Amazon RDS, and Alibaba ApsaraDB.

In this session, I’ll walk you through the techniques I used to escalate from a limited user to sysadmin on managed SQL Server platforms offered by the four biggest cloud providers. I’ll also demonstrate post-exploitation techniques, including how I retrieved plaintext [sa] passwords from internal logs and accessed highly sensitive internal metadata.

More importantly, I’ll share lessons on how these vulnerabilities were possible in the first place — and what you, as a developer, DBA, or security professional, can do to secure your applications against similar attack vectors.

Finally, I’ll share how each cloud provider responded to the vulnerabilities I disclosed, the remediation timelines, and the broader lessons this experience teaches us about cloud security.

## Speakers

### Fabiano Amorim

*Principal Consultant — Pythian*

Fabiano Amorim is a Microsoft Data Platform most valuable professional (MVP) since 2011. With over two decades of experience, Fabiano is well known in the database community for his performance tuning abilities and the many conference speaking engagements around the world.
He writes articles for Simple-Talk (https://www.simple-talk.com/author/fabiano-amorim/) and his blog is on http://blogfabiano.com.
