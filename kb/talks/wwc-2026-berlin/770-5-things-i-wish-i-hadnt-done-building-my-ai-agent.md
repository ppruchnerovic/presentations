---
id: 770
title: "5 things I wish I hadn’t done building my AI agent"
slug: 5-things-i-wish-i-hadnt-done-building-my-ai-agent
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Agents"
type: "Keynote/Talk"
stage: "Stage 3 - powered by AWS"
tags: ["Agentic AI", "Best Practices", "Startups"]
speakers: ["Shachar Azriel"]
speaker_companies: ["Baz"]
day: 1
starts_at: 2026-07-09T14:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=NjSDmkjUV-Q
video_id: NjSDmkjUV-Q
session_page: https://app.wearedevelopers.com/events/16/session/770
transcript: false
---

# 5 things I wish I hadn’t done building my AI agent

**Shachar Azriel (VP Product — Baz)**

`Track: AI Agents` · `Type: Keynote/Talk` · `Stage: Stage 3 - powered by AWS`

`#Agentic AI` `#Best Practices` `#Startups`

[Watch the recording](https://www.youtube.com/watch?v=NjSDmkjUV-Q) · [Session page](https://app.wearedevelopers.com/events/16/session/770)

## Abstract

Most talks about AI agents focus on success stories and best-case outcomes. This talk is about what can actually go wrong when you ship an scale-up AI agent in a start-up.

Over the past 18 months, our team in Baz built and scaled an AI-powered Code Review Agent used daily by thousands of across the world.
To move fast in this crazy market, we made several architectural, product, and UX decisions that seemed reasonable at the time, but later turned into expensive mistakes. Some cost us users, and some hit our precious revenue.

In this session, I’ll share five concrete pitfalls we encountered while building a real AI coding agent, why they happened, how we detected them, and the pivots that ultimately worked.

This is not a theoretical talk: every example comes from a production system, and will include real system diagrams, usage data, and how the fixes changed behavior in production.(alongside a lot of self humor :)

1. We built a “smarter” agent, and it got "dumber"
Why adding more context, tools, and responsibilities reduced accuracy instead of improving it

2. We let users choose the model, and lost control of the results
How exposing LLM choice destroyed consistency and meaningful feedback

3. We optimized for an AI app, not for developer behavior
Why real adoption only starts when the agent lives where decisions were already being made (GH, GL or the IDE)

4. Our guardrails worked, until the providers changed the models
How silent model updates broke engineering assumptions and eroded user trust

5. Our metrics looked great, but users were still churning
Why industry-standard AI metrics (like accepted suggestions and time-to-merge) missed the signal that actually won (or lost) customers

## Speakers

### Shachar Azriel

*VP Product — Baz*

For the past decade, I’ve helped startups and mid-sized tech companies scale teams, establish systems, and launch products that stick.
Today, I’m VP of Product at Baz, where we’re on a mission to reinvent code review with AI: making it faster, smarter, and (believe it or not) more fun for developers.

We’re working at the bleeding edge of technology, facing unique challenges that many other product and development teams are only beginning to encounter. That’s why I regularly share real stories from building AI-powered features in the wild, and from the journey of building an AI-driven company itself.

Beyond the product, I love connecting with people. I co-founded the AI-Dev community in Israel, dedicated to accelerating innovation in AI coding and product development.
