---
id: 917
title: "Future of Mobile AI. What On-Device Intelligence Means for App Developers"
slug: future-of-mobile-ai-what-on-device-intelligence-means-for
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Keynote/Talk"
stage: "Stage 12"
tags: ["AI Models", "Agents", "Agentic AI", "Android", "iOS", "WebAssembly"]
speakers: ["Sasha Denisov"]
speaker_companies: ["Brainform.ai"]
day: 2
starts_at: 2026-07-10T10:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=nCeUgrWjBMo
video_id: nCeUgrWjBMo
session_page: https://app.wearedevelopers.com/events/16/session/917
transcript: false
---

# Future of Mobile AI. What On-Device Intelligence Means for App Developers

**Sasha Denisov (CTO and Co-founder — Brainform.ai)**

`Track: Frontend, Web & Mobile` · `Type: Keynote/Talk` · `Stage: Stage 12`

`#AI Models` `#Agents` `#Agentic AI` `#Android` `#iOS` `#WebAssembly`

[Watch the recording](https://www.youtube.com/watch?v=nCeUgrWjBMo) · [Session page](https://app.wearedevelopers.com/events/16/session/917)

## Abstract

Two years ago, adding AI to your app meant one thing: cloud APIs. You sent data to a server, waited for a response, paid per request, and hoped your users had good internet. Privacy? A terms-of-service checkbox.

That world is ending.

Today, you can run a large language model directly on a phone. No internet required. No per-request costs. Data never leaves the device. This isn't a research demo — it's production-ready technology that changes what's possible for app developers.

I built flutter_gemma, an open-source plugin that lets developers run AI  models like Gemma locally on iOS, Android, and Web. Through this work,  I've learned what on-device AI actually means in practice — not the marketing version, but the real tradeoffs, limitations, and opportunities.

In this talk, I'll share what I've discovered:

What's now possible — Running models like Gemma 3 on a smartphone. The hardware (NPU, Neural Engine) that makes it work. The formats (.task, .litertlm) that matter.

What changes for developers — New architectural patterns: offline-first AI, hybrid cloud/edge approaches. New decisions: which model size, which format, where to store gigabytes of weights. New skills: fine-tuning, conversion, optimization.

The honest tradeoffs — Not every phone can run every model. Smaller models are faster but less capable. Some support separate LoRA weights for easy updates, others require full model replacement. I'll explain what works where.

Where we're heading — Multimodal models (text + images) on device. Function calling — AI that controls your app. Personalization through on-device fine-tuning. Models designed specifically for edge, like Gemma 3n.

The future of mobile AI isn't about replacing cloud — it's about giving developers a new option. One that's private, fast, and works anywhere.

## Speakers

### Sasha Denisov

*CTO and Co-founder — Brainform.ai*

Sasha is CTO at Brainform.ai with over 20 years of experience architecting scalable enterprise systems. With a strong engineering background, his expertise spans frontend, backend, cloud infrastructure, mobile development, and AI — from cloud-based generative AI to on-device solutions. He specializes in building robust, production-ready products using a variety of technologies and frameworks. Sasha has delivered solutions across fintech, digital media, and entertainment. He is a Google Developer Expert for Cloud, AI, Firebase, Flutter, and Dart, co-organizes the Flutter Berlin Community, and is a recognized international speaker and writer, having presented at 30+ conferences worldwide.
