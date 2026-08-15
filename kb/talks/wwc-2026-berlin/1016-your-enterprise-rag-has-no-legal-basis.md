---
id: 1016
title: "Your Enterprise RAG Has No Legal Basis"
slug: your-enterprise-rag-has-no-legal-basis
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Security & Privacy"
type: "Keynote/Talk"
stage: "Stage 10 - powered by TikTok"
tags: ["AI Coding Assistants", "AI Standards", "Agentic AI", "Best Practices", "Documentation", "Generative AI (GenAI)", "Governance", "Next.js", "Node.js", "PostgreSQL", "Privacy", "React", "Software Architecture", "TypeScript", "Vector Databases", "Vibe Coding"]
speakers: ["David Klemme", "Tilman Mürle"]
speaker_companies: ["Komplyzen"]
day: 2
starts_at: 2026-07-10T14:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=UpwAj792WvI
video_id: UpwAj792WvI
session_page: https://app.wearedevelopers.com/events/16/session/1016
transcript: false
---

# Your Enterprise RAG Has No Legal Basis

**David Klemme (Co-founder and CTO — Komplyzen), Tilman Mürle (Managing Director and Co-founder — Komplyzen)**

`Track: Security & Privacy` · `Type: Keynote/Talk` · `Stage: Stage 10 - powered by TikTok`

`#AI Coding Assistants` `#AI Standards` `#Agentic AI` `#Best Practices` `#Documentation` `#Generative AI (GenAI)` `#Governance` `#Next.js` `#Node.js` `#PostgreSQL` `#Privacy` `#React` `#Software Architecture` `#TypeScript` `#Vector Databases` `#Vibe Coding`

[Watch the recording](https://www.youtube.com/watch?v=UpwAj792WvI) · [Session page](https://app.wearedevelopers.com/events/16/session/1016)

## Abstract

Your RAG system works beautifully. Under GDPR, it has no legal basis to exist.

Clean architecture. Proper embeddings. Maybe even agentic tool calling. You followed best practices. But when the auditor asks "what's the legal basis for this processing?" there's no answer. General-purpose "ask anything" chatbots have no defined purpose. Without a defined purpose, no legal basis can exist under GDPR. The architecture itself is the violation.

In this talk, I'll live-code a "best practices" enterprise knowledge bot, then ask the questions nobody asks: Where is purpose limitation enforced? Where is legal basis documented? I'll show why anonymization doesn't save you. 97% accuracy isn't "anonymous" under GDPR. It's still PII.

Then I'll show you the fix: a purpose-scoped bot architecture where legal basis is a first-class configuration item. Each bot gets a defined purpose, scoped data access, configured tools, and documented legal basis. The architecture enforces the boundaries. The retrieval layer can only access documents within that bot's scope. Non-compliance becomes architecturally impossible.

The good news? You didn't waste your investment. This is a 50k governance layer, not a rewrite.

Takeaways:
  - Why your RAG has no legal basis and how to fix it
  - The purpose-scoped bot pattern: document, enforce, and audit compliance by design
  - A brownfield rescue roadmap for existing systems

## Speakers

### David Klemme

*Co-founder and CTO — Komplyzen*

Hybrid AI and enterprise technology leader with 10+ years designing, implementing, and scaling production-grade AI platforms in complex enterprise environments. Bridges executive vision with technical delivery. From strategy and governance down to architecture, infrastructure, and code.

As Enterprise Architect at Rödl & Partner (~7,000 employees), architected a multi-tenant generative AI platform serving 6,000+ users with EU AI Act-aligned access controls. Led enterprise data strategy and Azure Integration Services rollout at enterprise scale. Previous experience includes ITSM transformation for German public sector (VBG) and AWS data architecture for Deutsche Bahn subsidiary.

### Tilman Mürle

*Managing Director and Co-founder — Komplyzen*

Tilman Mürle is Managing Director and Co-Founder of Komplyzen, where he helps organizations turn AI governance from a compliance exercise into an operational capability. He brings over a decade of leadership experience across SaaS, enterprise IT, and regulated environments, including his role as former CEO EMEA at Valiantys.

Tilman works with engineering, risk, and leadership teams to design AI systems that are measurable, auditable, and production-ready by design. His focus lies on operational AI governance, AI risk management, and translating regulatory expectations into practical architecture and workflows that scale.

He regularly speaks at industry conferences on AI risk, governance, and the realities of bringing AI safely into production.
