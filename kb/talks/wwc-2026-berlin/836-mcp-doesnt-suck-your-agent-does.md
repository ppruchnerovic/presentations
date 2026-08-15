---
id: 836
title: "MCP doesn’t suck — your agent does"
slug: mcp-doesnt-suck-your-agent-does
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Agents"
type: "Keynote/Talk"
stage: "Stage 1"
tags: ["AI Coding Assistants", "Generative AI (GenAI)"]
speakers: ["Jan Curn"]
speaker_companies: ["Apify"]
day: 2
starts_at: 2026-07-10T07:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=mE3RC3hhtHE
video_id: mE3RC3hhtHE
session_page: https://app.wearedevelopers.com/events/16/session/836
transcript: false
---

# MCP doesn’t suck — your agent does

**Jan Curn (Founder and CEO — Apify)**

`Track: AI Agents` · `Type: Keynote/Talk` · `Stage: Stage 1`

`#AI Coding Assistants` `#Generative AI (GenAI)`

[Watch the recording](https://www.youtube.com/watch?v=mE3RC3hhtHE) · [Session page](https://app.wearedevelopers.com/events/16/session/836)

## Abstract

Most AI agents misuse MCP and treat tools as prompt-time function calls: tool definitions and results are repeatedly injected into the context, tokens are wasted, and context rots. The result? Slower, less reliable agents, and the misleading conclusion that “MCP sucks, CLIs are better.”

To challenge this narrative and show how agents can get the best of both MCP and CLI, we’ve built mcpc, an open-source universal CLI client for MCP. It maps MCP operations to intuitive CLI commands, which agents quickly pick up through --help without external skills.

It turns out, CLI is the perfect local interface for agents to interact with MCP, giving them access to full protocol capabilities, including modern features like code mode or progressive tool discovery through a single Bash() tool call, while leveraging MCP’s standard remote interface for server discovery, authentication, payments, and access control.

To once and for all kill the MCP vs. CLI debate and show those two technologies are not exclusive but complementary, we’ll present evals comparing the performance of agents using naive MCP, modern MCP, native CLIs, other MCP CLIs, and mcpc, in various real-world scenarios.

## Speakers

### Jan Curn

*Founder and CEO — Apify*

Jan Curn is the founder and CEO of Apify (https://apify.com), a full-stack web scraping and automation platform that powers (not only) AI agents with up-to-date data. He has a lifelong passion for software engineering, which earned him an MSc and PhD in computer science and eventually led him to founding Apify. Jan lives between SF and Prague, is active in the tech community in both cities, organizes meetups, and talks about software, startups, or AI.
