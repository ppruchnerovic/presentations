---
id: 900
title: "Building a Cross-Platform BLE Client with Kotlin Multiplatform and Kable"
slug: building-a-cross-platform-ble-client-with-kotlin
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Keynote/Talk"
stage: "Stage 13"
tags: ["Android", "Cross-Platform", "iOS", "Kotlin", "Kotlin Multiplatform"]
speakers: ["Georg Dresler"]
speaker_companies: ["Ray Sono"]
day: 2
starts_at: 2026-07-10T09:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=3BC96e1K-9A
video_id: 3BC96e1K-9A
session_page: https://app.wearedevelopers.com/events/16/session/900
transcript: false
---

# Building a Cross-Platform BLE Client with Kotlin Multiplatform and Kable

**Georg Dresler (Principal Software Architect — Ray Sono)**

`Track: Frontend, Web & Mobile` · `Type: Keynote/Talk` · `Stage: Stage 13`

`#Android` `#Cross-Platform` `#iOS` `#Kotlin` `#Kotlin Multiplatform`

[Watch the recording](https://www.youtube.com/watch?v=3BC96e1K-9A) · [Session page](https://app.wearedevelopers.com/events/16/session/900)

## Abstract

Building Bluetooth Low Energy features has long been challenging since every platform behaves differently and the code quickly fragments. Kotlin Multiplatform changes that story by letting you build reliable Bluetooth functionality once, so even if you’re new to BLE, you can start with confidence instead of chaos.

With Kotlin Multiplatform (KMP) and the Kable library, you can create a single BLE layer that runs across Android, iOS, and macOS, with experimental Web support. Kable abstracts platform quirks through coroutines and Flow, delivering predictable async behavior across targets.

We'll briefly cover BLE fundamentals such as clients, peripherals, services, and characteristics to lay the groundwork.

In a live demo, we'll control a Bluetooth-enabled light from a shared KMP CLI app. You’ll see how coroutines make reads and writes feel sequential, while Flows stream live updates like connection state, battery level, or sensor data. Structured concurrency keeps the client stable and predictable, even when devices disconnect or data changes rapidly.

Key takeaways:
- Build a cross-platform BLE client
- Use coroutines and Flow for reliable, idiomatic async BLE operations
- Apply structured concurrency for robust connection management and cleanup

## Speakers

### Georg Dresler

*Principal Software Architect — Ray Sono*

Georg studied computer science and decided to become an app developer when the first iPhone was released. He learned Objective-C, then later Swift and Kotlin. Today, he focuses on architecting and developing apps with Kotlin Multiplatform, Flutter, and native technologies.

With over a decade of experience, he specializes in application architecture, data modeling, testing, and code quality. Georg has spoken at WeAreDevelopers, InfoQ Dev Summit, and Almato DevCon, as well as several meetups. He has also been a guest on a podcast and taught a course on mobile app development.
