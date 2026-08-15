---
id: 955
title: "API, MCP or MCP App? Choosing the right surface for AI agents"
slug: api-mcp-or-mcp-app-choosing-the-right-surface-for-ai-agents
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Agents"
type: "Keynote/Talk"
stage: "Stage 4"
tags: ["AI Coding Assistants", "AI Models", "AI Standards", "Anthropic", "APIs", "Agents", "Agentic AI", "Autonomous Systems", "Best Practices", "Case Study", "Claude", "Code Generation", "Developer Experience (DevEx)", "Documentation", "Future of Work", "Generative AI (GenAI)", "Integration", "LangChain", "Large Language Models (LLMs)", "LLMOps", "Prompt Engineering"]
speakers: ["Rishabh Budhiraja", "Rishi Deorukhkar"]
speaker_companies: ["idealo Internet"]
day: 2
starts_at: 2026-07-10T12:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=z1kRfBwwFN8
video_id: z1kRfBwwFN8
session_page: https://app.wearedevelopers.com/events/16/session/955
transcript: false
---

# API, MCP or MCP App? Choosing the right surface for AI agents

**Rishabh Budhiraja (Staff Engineer — idealo Internet), Rishi Deorukhkar (AI Engineer — idealo Internet)**

`Track: AI Agents` · `Type: Keynote/Talk` · `Stage: Stage 4`

`#AI Coding Assistants` `#AI Models` `#AI Standards` `#Anthropic` `#APIs` `#Agents` `#Agentic AI` `#Autonomous Systems` `#Best Practices` `#Case Study` `#Claude` `#Code Generation` `#Developer Experience (DevEx)` `#Documentation` `#Future of Work` `#Generative AI (GenAI)` `#Integration` `#LangChain` `#Large Language Models (LLMs)` `#LLMOps` `#Prompt Engineering`

[Watch the recording](https://www.youtube.com/watch?v=z1kRfBwwFN8) · [Session page](https://app.wearedevelopers.com/events/16/session/955)

## Abstract

AI-referred shoppers convert 54% higher and generate 53% more revenue per visit than non-AI traffic (Adobe, May 2026). AI sessions to retailers grew 138% year-over-year. As the customer journey collapses into a single conversation, "build an API" stops being the obvious answer when the consumer isn't a developer but an agent.

This talk distills what we learned shipping to ChatGPT, Claude, and our own internal agents – and the framework we use to decide what to build for whom.

API, MCP, and MCP App are three different products serving three different consumers: a developer building their own integration, an agent runtime where the host owns the UI, and an app surface where the UI returns but is shared with the model. Treating MCP as a drop-in replacement for an API is how teams end up with a tool surface their agents can't actually use.

From there, four engineering lessons stand out that don't appear in the MCP spec:

– Tool descriptions are prompts, not docs. A one-line change can flip whether the model calls your tool, or calls it with hallucinated arguments.

– Flow is a design surface. You're not designing tools in isolation – you're designing the path the model walks through them.

– Treat your tool surface like a prompt: version it, snapshot it, eval it. Unit tests don't catch the failures that matter.

– In an MCP app, the UI is part of the prompt. Widget state pushes back to the model as context; tools split between model-visible and widget-only – a new design discipline with little prior art.

Attendees leave with a decision framework for the three-way call, and a practical checklist for shipping a tool surface that agents can actually use.

## Speakers

### Rishabh Budhiraja

*Staff Engineer — idealo Internet*

Rishabh Budhiraja is Staff Engineer at idealo, specializing in cloud-native web applications, frontend modernization, performance engineering, and agentic system development. He works on high-traffic customer-facing systems across checkout and offer page experiences, building scalable features and improving user experience through experimentation and modern architecture.

His work includes migrating legacy frontend systems to modern micro frontend architectures, optimizing Core Web Vitals, contributing to idealo’s company-wide frontend framework, and exploring MCP-based integrations for AI-enabled engineering workflows. With experience across React, Astro, AWS, Kubernetes, server-side rendering, and AI-assisted development, Rishabh focuses on building robust, scalable systems that help teams deliver faster and create better digital experiences.

### Rishi Deorukhkar

*AI Engineer — idealo Internet*

Rishi Deorukhkar is AI Engineer at idealo specializing in AI-native systems, backend architecture, and cloud platform development. He builds agentic RAG pipelines, MCP applications, AI agents, and evaluation frameworks for automated compliance, audit workflows, document intelligence, and developer productivity.

His work spans scalable APIs, vector databases, specification-driven coding agents, enterprise SaaS platforms, and eval-driven AI systems deployed across AWS and Azure. With experience in TypeScript, Python, LangChain, OpenAI, Claude, CDK, Pulumi, Kubernetes, and microservices architecture, Rishi focuses on turning complex business workflows into reliable, automated, AI-powered systems.
