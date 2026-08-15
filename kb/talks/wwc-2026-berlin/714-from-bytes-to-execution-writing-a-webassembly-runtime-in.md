---
id: 714
title: "From Bytes to Execution: Writing a WebAssembly Runtime in Rust"
slug: from-bytes-to-execution-writing-a-webassembly-runtime-in
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Languages & Runtimes"
type: "Keynote/Talk"
stage: "Stage 10 - powered by TikTok"
tags: ["Rust", "Runtimes", "WebAssembly"]
speakers: ["Gaurav Gahlot"]
speaker_companies: ["IONOS Cloud"]
day: 1
starts_at: 2026-07-09T12:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=wRBDzv9Ai7E
video_id: wRBDzv9Ai7E
session_page: https://app.wearedevelopers.com/events/16/session/714
transcript: false
---

# From Bytes to Execution: Writing a WebAssembly Runtime in Rust

**Gaurav Gahlot (Staff Software Engineer — IONOS Cloud)**

`Track: Languages & Runtimes` · `Type: Keynote/Talk` · `Stage: Stage 10 - powered by TikTok`

`#Rust` `#Runtimes` `#WebAssembly`

[Watch the recording](https://www.youtube.com/watch?v=wRBDzv9Ai7E) · [Session page](https://app.wearedevelopers.com/events/16/session/714)

## Abstract

WebAssembly runtimes power everything from serverless platforms to container sandboxes — but their internals often feel opaque. In this talk, I demystify those internals by presenting Whisk, a minimal WebAssembly runtime I built entirely in Rust.

Rather than focusing on a production-grade engine, Whisk intentionally strips the runtime down to its essential components: module parsing, validation, memory handling, and instruction execution. Walking through these pieces makes the architecture of a WASM runtime clear and approachable, while also showing how Rust’s enums, traits, and safety guarantees naturally support VM design.

We’ll explore how an interpreter is built step-by-step, what trade-offs arise in a minimal design, and how Whisk differs from larger runtimes like Wasmtime or Wasmer. I’ll also demo Whisk running real WebAssembly modules (non-WASI), illustrating where the boundaries of a tiny runtime lie.

Attendees will learn:
- How a WebAssembly runtime works from the inside out
- How to design a small interpreter in Rust
- Why Rust is well-suited for building VMs and sandboxes
- The trade-offs between minimal and production-grade runtimes
- How lightweight engines fit into today’s WASM and cloud-native ecosystem

This talk offers a practical and accessible deep dive into WebAssembly internals — with Rust as the guide.

## Speakers

### Gaurav Gahlot

*Staff Software Engineer — IONOS Cloud*

Gaurav Gahlot is a Software Engineer passionate about building low-level systems, Rust, and Cloud Native ecosystem. He loves to share his learning via his blog, and is also a maintainer of CNCF’s Akri project.
