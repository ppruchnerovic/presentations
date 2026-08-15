---
id: 943
title: "From Perception to Autonomy: Building Agentic Edge AI Robots with ROS 2"
slug: from-perception-to-autonomy-building-agentic-edge-ai-robots
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Emerging Technologies"
type: "Keynote/Talk"
stage: "Stage 5"
tags: ["AI Models", "Agentic AI", "Cryptography", "Edge AI", "Embedded Systems", "Raspberry Pi", "Robotics"]
speakers: ["Moe Sani"]
speaker_companies: ["Edge Impulse"]
day: 2
starts_at: 2026-07-10T11:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=ZKSJ18Uekgs
video_id: ZKSJ18Uekgs
session_page: https://app.wearedevelopers.com/events/16/session/943
transcript: false
---

# From Perception to Autonomy: Building Agentic Edge AI Robots with ROS 2

**Moe Sani (Solutions Architect — Edge Impulse)**

`Track: Emerging Technologies` · `Type: Keynote/Talk` · `Stage: Stage 5`

`#AI Models` `#Agentic AI` `#Cryptography` `#Edge AI` `#Embedded Systems` `#Raspberry Pi` `#Robotics`

[Watch the recording](https://www.youtube.com/watch?v=ZKSJ18Uekgs) · [Session page](https://app.wearedevelopers.com/events/16/session/943)

## Abstract

AI in robotics is moving fast — from cloud-dependent pipelines to fully autonomous, on-device systems that perceive, reason, and act without connectivity. But for most developers, the gap between "cool demo" and "working robot" is still wide. This talk bridges that gap.
I'll walk you through the evolution of Physical Edge AI — what it actually means in practice, not just in keynotes — and show you how to build a real autonomous system using ROS 2, Edge Impulse, and Qualcomm edge hardware.
The centrepiece is a live architecture walkthrough of an autonomous inspection robot I built and demoed at Embedded World 2026. It runs two AI models on-device: a fast object detector to decide where to look, and a close-up anomaly scorer to decide is this a problem? — all orchestrated as ROS 2 nodes on a Qualcomm QCS6490 (RubikPi 3), with zero cloud dependency.
From there, I'll zoom out to what's coming next: agentic edge AI — robots that don't just detect and classify, but plan, decide, and adapt using lightweight LLMs/VLMs running locally on edge hardware. I'll cover the practical building blocks available today (TensorRT Edge-LLM, quantised VLMs on Jetson, vision-language-action models), the ROS 2 integration patterns that make this work, and the honest gaps that still need solving.
What you'll take away:

A reusable architecture pattern for multi-model edge AI robotics (detect → inspect → decide)
How to integrate Edge Impulse ML models as native ROS 2 nodes
What "agentic" actually means at the edge — and what's real vs. hype in 2026
Practical guidance on edge hardware selection (Jetson, Qualcomm, NPUs) and when to go hybrid edge-cloud
Where the open-source ecosystem (ROS 2, Edge Impulse, NVIDIA Isaac) is headed for developers who want to build physical AI systems

## Speakers

### Moe Sani

*Solutions Architect — Edge Impulse*

Moe is an Edge AI Solutions Architect at Edge Impulse (A Qualcomm Company), where he empowers partners and customers to bring cutting-edge machine learning into a diverse range of industries. Prior to Edge Impulse, Moe was leading the research and implementation of the first ML based navigation system for Dyson robots. With over 10 years of experience in robotics, machine learning, and embedded systems, Moe has a proven track record in architecting, leading, and implementing state-of-the-art AI and IoT solutions. His expertise spans predictive maintenance to smart automation, turning complex technologies into practical, real-world applications
