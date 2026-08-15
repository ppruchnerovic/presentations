---
id: 710
title: "Tour de Force: Open-Source LLM Inference Optimization from Simple to Sophisticated"
slug: tour-de-force-open-source-llm-inference-optimization-from
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Engineering"
type: "Keynote/Talk"
stage: "Stage 6 - powered by Microsoft"
tags: ["Azure", "Generative AI (GenAI)", "Infrastructure", "LLMOps", "Python", "Software Architecture"]
speakers: ["Christin Pohl"]
speaker_companies: ["Microsoft"]
day: 1
starts_at: 2026-07-09T12:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=4sQuYydV4Aw
video_id: 4sQuYydV4Aw
session_page: https://app.wearedevelopers.com/events/16/session/710
transcript: false
---

# Tour de Force: Open-Source LLM Inference Optimization from Simple to Sophisticated

**Christin Pohl (Global Black Belt Solution Engineer — Microsoft)**

`Track: AI Engineering` · `Type: Keynote/Talk` · `Stage: Stage 6 - powered by Microsoft`

`#Azure` `#Generative AI (GenAI)` `#Infrastructure` `#LLMOps` `#Python` `#Software Architecture`

[Watch the recording](https://www.youtube.com/watch?v=4sQuYydV4Aw) · [Session page](https://app.wearedevelopers.com/events/16/session/710)

## Abstract

Azure OpenAI and similar managed APIs are the right default for serving language models. But they don't cover every case. Maybe you need to deploy in a region where your model isn't available yet, you want to run a Qwen or Mistral variant that no provider hosts, or you've fine-tuned a model and there's simply no API to call. At that point, you're self-hosting on GPUs.

Making your GPUs go brrr is complex. Efficient LLM inference requires navigating a maze of optimization techniques each with different trade-offs. This session provides a practical journey through inference optimizations, clearly categorized by implementation effort.

We'll explore techniques across three levels:

- Model choices (start here): Model selection, quantization, smart routing

- Library-level improvements (using PyTorch-based frameworks like vLLM, SGLang, TensorRT-LLM): Continuous batching, KV-cache management

- Custom implementations: Speculative decoding with custom draft heads, disaggregated inference, fine-tuning smaller models

The session covers practical trade-offs and key metrics: time to first token, inter-token latency, and cost per token.

Whether deploying your first model or optimizing at scale, this talk delivers actionable insights into which techniques to prioritize for deeper investigation.

## Speakers

### Christin Pohl

*Global Black Belt Solution Engineer — Microsoft*

Christin Pohl is a Global Black Belt Solution Engineer for AI Infrastructure at Microsoft (Switzerland), now in her third year. After building her first chatbot in 2018 and 5+ years at SAP, she helps enterprises worldwide choose the right GPU, run LLM training and inference end-to-end (LLMOps), and optimize performance (latency, throughput, and cost per token). She studied Information Technology and Computer Science in Berlin, Toronto, and at Harvard.
