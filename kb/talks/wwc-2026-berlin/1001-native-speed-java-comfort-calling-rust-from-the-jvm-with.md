---
id: 1001
title: "Native Speed, Java Comfort: Calling Rust from the JVM with Project Panama"
slug: native-speed-java-comfort-calling-rust-from-the-jvm-with
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Languages & Runtimes"
type: "Keynote/Talk"
stage: "Stage 8 - powered by Red Hat"
tags: ["Java", "JVM", "Performance", "Rust"]
speakers: ["Gonzalo Ortiz Jaureguizar"]
speaker_companies: ["Startree"]
day: 2
starts_at: 2026-07-10T13:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=KS6JBr3pAvk
video_id: KS6JBr3pAvk
session_page: https://app.wearedevelopers.com/events/16/session/1001
transcript: false
---

# Native Speed, Java Comfort: Calling Rust from the JVM with Project Panama

**Gonzalo Ortiz Jaureguizar (Performance Engineer — Startree)**

`Track: Languages & Runtimes` · `Type: Keynote/Talk` · `Stage: Stage 8 - powered by Red Hat`

`#Java` `#JVM` `#Performance` `#Rust`

[Watch the recording](https://www.youtube.com/watch?v=KS6JBr3pAvk) · [Session page](https://app.wearedevelopers.com/events/16/session/1001)

## Abstract

The JVM is one of the most impressive pieces of software engineering, making Java incredibly fast for most workloads. But sometimes, "fast" isn't enough. For domains like scientific computing, AI, or processing massive volumes of text, we need to call highly-optimized native libraries written in C++ or Rust to gain a critical performance edge or access functionality not available on the JVM. For decades, this meant using the Java Native Interface (JNI)—a powerful but notoriously complex and unsafe bridge to the native world.

Enter Project Panama. With the Foreign Function & Memory (FFM) API, Java finally has a safe, supported, and elegant way to call native code, eliminating the need for brittle glue code and manual memory management. This talk puts it to the test with a classic Java challenge: the regular expression engine.

Join me for a practical, hands-on session where we will replace Java's capable but often-outperformed regex engine with Rust's highly optimized regex crate. We will walk through two implementations side-by-side: the "old way" with JNI and the "new way" with Project Panama. You will see firsthand how Panama simplifies interfacing with native code and improves safety. We'll cap it off with live benchmarks to compare the performance of both approaches against standard Java regex, helping you understand not just how to call native code, but also when it's truly worth the effort.

## Speakers

### Gonzalo Ortiz Jaureguizar

*Performance Engineer — Startree*

I am a software engineer specialized in developing databases in Java. I love understanding how libraries and frameworks work under the hood and to design and implement high-performance systems. I have worked on prototypes such as ToroDB, the first Spanish database unicorn Devo and since 2022 I'm working at StarTree as an Apache Pinot contributor.
