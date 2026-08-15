---
id: 697
title: "Beyond authentication: an open-source trust model for the agentic web"
slug: beyond-authentication-an-open-source-trust-model-for-the
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Quality & Reliability"
type: "Keynote/Talk"
stage: "Stage 13"
tags: ["AI Standards", "Authentication", "AWS", "Agents", "Agentic AI", "Infrastructure", "Open Source", "Software Architecture"]
speakers: ["Alexander Günsche", "Sabrina Engling"]
speaker_companies: ["AWS", "Trusted Shops SE"]
day: 1
starts_at: 2026-07-09T11:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=5SWCbrxp8Z4
video_id: 5SWCbrxp8Z4
session_page: https://app.wearedevelopers.com/events/16/session/697
transcript: false
---

# Beyond authentication: an open-source trust model for the agentic web

**Alexander Günsche (Senior Solutions Architect — AWS), Sabrina Engling (AI Lead — Trusted Shops SE)**

`Track: Quality & Reliability` · `Type: Keynote/Talk` · `Stage: Stage 13`

`#AI Standards` `#Authentication` `#AWS` `#Agents` `#Agentic AI` `#Infrastructure` `#Open Source` `#Software Architecture`

[Watch the recording](https://www.youtube.com/watch?v=5SWCbrxp8Z4) · [Session page](https://app.wearedevelopers.com/events/16/session/697)

## Abstract

Authenticating an agent tells you who it is, but not whether to let it transact, access data, or act on a user's behalf. As autonomous agents begin crossing organisational boundaries, the systems they reach face a binary choice: block all agent traffic or accept it without verification - neither of which scales as agent traffic grows.

TSAI (Trust Signals for Agentic Interactions) is an open source protocol that fills this gap. Built on W3C Verifiable Credentials and Decentralised Identifiers (DIDs), it carries trust signals beyond identity - reputation, economic stake, authorization, and endorsements - in cryptographically signed credentials that any system can verify offline. Independent Trust Authorities issue them and agents present them when accessing a service, while receiving systems make their own access decisions based on the signals. Credentials describe the agent, not the user, which preserves user privacy and keeps existing user authentication unchanged.

In this talk, we walk through the architecture - the four-tier trust model that scales from offline verification at low risk to real-time checks at high stakes, the credential format and lifecycle, and how TSAI composes with agent protocols like MCP and A2A. TSAI is developed by AWS and Trusted Shops, combining agent infrastructure expertise with decades of online trust certification.

## Speakers

### Alexander Günsche

*Senior Solutions Architect — AWS*

Alex is a Senior Solutions Architect at AWS with 20 years of IT experience in expert and leadership roles. He is a strong advocate of agile and DevOps practices, and he enjoys seeing serverless, cloud-native and event-driven architectures deployed at scale. He has delivered large transformation projects and successfully developed own and customers’ businesses. As an international speaker, he has held advanced technology sessions at a wide range of events.

### Sabrina Engling

*AI Lead — Trusted Shops SE*

Sabrina Engling leads the AI Solutions Team at Trusted Shops and drives AI adoption and innovation across the entire company. Her focus is on scalable AI solutions, AI operations, and agentic commerce. She combines technical expertise with strategic business acumen, bringing together both perspectives - from the architecture of scalable AI systems to business value.

Beyond her corporate role, Sabrina is a dedicated advocate for tech education and serves as Chairwoman of the NGO TechLabs, helping thousands of people build digital skills. As an AWS Commmunity Builder for AI Engineering, alumna of the AWS She Builds mentoring program, a certified AI Manager, and a recent AI hackathon winner, she is committed to empowering more women to take the leap into AI and cloud technologies.
