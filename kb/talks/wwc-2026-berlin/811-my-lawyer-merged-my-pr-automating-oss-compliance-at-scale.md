---
id: 811
title: "My Lawyer Merged My PR: Automating OSS Compliance at Scale"
slug: my-lawyer-merged-my-pr-automating-oss-compliance-at-scale
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "DevOps"
type: "Keynote/Talk"
stage: "Stage 12"
tags: ["Automation", "CI/CD", "Compliance", "Developer Experience (DevEx)", "GitHub Actions", "Open Source", "SBOM"]
speakers: ["Uwe Korn"]
speaker_companies: ["QuantCo"]
day: 1
starts_at: 2026-07-09T15:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=kn2Np9tnYsU
video_id: kn2Np9tnYsU
session_page: https://app.wearedevelopers.com/events/16/session/811
transcript: false
---

# My Lawyer Merged My PR: Automating OSS Compliance at Scale

**Uwe Korn (CTO — QuantCo)**

`Track: DevOps` · `Type: Keynote/Talk` · `Stage: Stage 12`

`#Automation` `#CI/CD` `#Compliance` `#Developer Experience (DevEx)` `#GitHub Actions` `#Open Source` `#SBOM`

[Watch the recording](https://www.youtube.com/watch?v=kn2Np9tnYsU) · [Session page](https://app.wearedevelopers.com/events/16/session/811)

## Abstract

Everyone agrees that OSS license compliance is critical, yet nobody enjoys the process. It usually involves spreadsheets, long email chains, and "shipping anxiety." We decided to treat (legal) license compliance not as a distinct administrative phase, but as a standard CI/CD failure state.

In this talk, I will demonstrate how we built a fully automated license defence line. We utilised package manager metadata to build a centralised "allow-list" enforced by CI checks across all repositories.

But the real innovation is the exception handling:

- **Get Blocked:** When a developer introduces a new license, the build fails with a direct link to our central license repository.
- **Review:** The developer opens a PR to add the new license to the allow list.
- **And Approved!** Our lawyer, whom we onboarded to GitHub, reviews the legal implications and merges the PR.
- **Instant Enablement:** The check turns green, and the code ships.

I will share the technical setup, how we cleaned up our metadata, and how integrating Legal into the Pull Request workflow eliminated "showstopper" risks and gave our engineers instant feedback. Additionally, I will also share how we handle the exceptional cases where we cannot add something to a global list.

## Speakers

### Uwe Korn

*CTO — QuantCo*

Uwe Korn is a CTO at the EconAI company QuantCo. His expertise is in building scalable architectures for machine learning services and the teams & culture around them. Nowadays, he focuses on the software engineering infrastructure needed to provide the building blocks for bringing ML/AI projects into production. As part of his work, he became a core committer to the Apache Parquet, Apache Arrow and conda-forge projects.
