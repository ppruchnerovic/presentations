---
id: 796
title: "One Pipeline, Three Regulator - SBOM Compliance for the Developer"
slug: one-pipeline-three-regulator-sbom-compliance-for-the
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Security & Privacy"
type: "Keynote/Talk"
stage: "Airstream 1"
tags: ["Automation", "Compliance", "DevSecOps", "People & Culture", "SBOM", "Software Architecture"]
speakers: ["Marcus Ross"]
speaker_companies: ["Die Techniker"]
day: 1
starts_at: 2026-07-09T14:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=zuHMlS9697I
video_id: zuHMlS9697I
session_page: https://app.wearedevelopers.com/events/16/session/796
transcript: false
---

# One Pipeline, Three Regulator - SBOM Compliance for the Developer

**Marcus Ross (Platform Engineering and Process Framework — Die Techniker)**

`Track: Security & Privacy` · `Type: Keynote/Talk` · `Stage: Airstream 1`

`#Automation` `#Compliance` `#DevSecOps` `#People & Culture` `#SBOM` `#Software Architecture`

[Watch the recording](https://www.youtube.com/watch?v=zuHMlS9697I) · [Session page](https://app.wearedevelopers.com/events/16/session/796)

## Abstract

You shipped your app to the EU market, and three people are knocking: a CRA auditor, a NIS-2 assessor and your ISO 27001 lead. Different paragraphs, same question - what's in your software, and can you prove it?

This hands-on session answers it with engineering, not paperwork! We clarify the steps: sign commits keylessly with Sigstore gitsign (and find them in the Rekor transparency log), generate an SBOM in both SPDX and CycloneDX with OpenSSF Protobom and bomctl, then scan it against trustworthy data with OSV-Scanner - because in 2024 the NVD backlog broke CVE feeds, and the OpenSSF OSV schema is how you route around it.

We map each step to the clause it satisfies:
- CRA Annex I
- NIS-2 Article 21,
- ISO27001 A.5.21/A.8.8.
The twist: only the CRA names the SBOM - the other two simply can't be met without one.

You'll leave with four commands that turn three compliance regimes into a by-product of how you already ship. No legal background needed.

What you'll learn
- Which exact CRA, NIS-2 and ISO 27001 clauses drive SBOM and provenance work - and the "one names it, two need it" distinction.
- Keyless commit signing with Sigstore gitsign, verified in the Rekor transparency log.
- Ending the SPDX-vs-CycloneDX fight with OpenSSF Protobom and bomctl.
- Why CVE data fragmented in 2024, and how the OpenSSF OSV schema + OSV-Scanner give version-accurate results from your SBOM.

## Speakers

### Marcus Ross

*Platform Engineering and Process Framework — Die Techniker*

Marcus Ross is a Member of the Platform Engineering & Process Framework team. He's developing the next step in scalable telematics and healthcare digitalization by building platforms with Kubernetes, GitOps, and platform tooling that put the Golden Path ahead of cognitive load. He's also keen to turn AI into real value in his everyday work.
