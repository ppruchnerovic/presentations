---
id: 700
title: "Edge Orchestration for the Physical World: Connecting Cameras, Sensors, and Devices with MQTT"
slug: edge-orchestration-for-the-physical-world-connecting
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Emerging Technologies"
type: "Startup Presentation"
stage: "Airstream 1"
tags: ["Edge AI", "Internet of Things (IoT)", "Observability", "Raspberry Pi", "Startups"]
speakers: ["Irina Terekhova"]
speaker_companies: ["Banalytics"]
day: 1
starts_at: 2026-07-09T11:35:00+00:00
duration_min: 5
recording_url: https://www.youtube.com/watch?v=gwSsWmPKdTU
video_id: gwSsWmPKdTU
session_page: https://app.wearedevelopers.com/events/16/session/700
transcript: true
---

# Edge Orchestration for the Physical World: Connecting Cameras, Sensors, and Devices with MQTT

**Irina Terekhova (Co-founder and CPO — Banalytics)**

`Track: Emerging Technologies` · `Type: Startup Presentation` · `Stage: Airstream 1`

`#Edge AI` `#Internet of Things (IoT)` `#Observability` `#Raspberry Pi` `#Startups`

[Watch the recording](https://www.youtube.com/watch?v=gwSsWmPKdTU) · [Session page](https://app.wearedevelopers.com/events/16/session/700)

## Abstract

You have cameras, sensors, or edge devices. You have custom scripts glueing them together. And somewhere in production, those scripts are quietly failing.

In 5 minutes, I'll show you what an edge orchestration layer looks like in practice — a single platform that connects mixed cameras and sensors, publishes events to MQTT, and gives you a browser dashboard with zero cloud dependency. Runs on Windows, Linux and Raspberry Pi. Free to start.

Four use cases, one architecture: Home Assistant makers unifying mixed-brand cameras without per-vendor apps; SMB operators getting Telegram alerts with video clips across multiple sites; AI teams running event-triggered multimodal capture for training data pipelines; and industrial sensing teams wrapping a processing module with dashboards, lifecycle management, and MQTT publishing — without touching the module itself.

## Speakers

### Irina Terekhova

*Co-founder and CPO — Banalytics*

Irina Terekhova is Co-founder and Chief Product Officer at Banalytics, an open edge orchestration platform for cameras, sensors, and industrial devices.

At Banalytics she owns the product strategy, use-case definition, and roadmap across four customer segments: industrial sensing teams, AI data collection pipelines, SMB operations, and homelab builders. Her focus is on making edge infrastructure observable and deployable without requiring teams to build the operational layer from scratch.

Before Banalytics, Irina spent nearly two decades in product management and business analysis across AI, security, and financial services — including launching an AI line of business at an industrial hardware company and leading product teams at a global software consultancy.

## Transcript

*856 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=gwSsWmPKdTU&t=0s)** Hello everybody. I'm presenting Banalitics and this is surprisingly not an AI. But this is a software platform. >> [laughter] >> So, what our platform does? Imagine that you have I don't know a deep tech module or an algorithm. And everything is fine, works good. You tested it with the large amount of data, but you need to reliably deploy it to production. You have to you need to run a pilot, but you do not have any infrastructure around it. You do not have real-time data that you can fetch into your module or an algorithm. And here is where Banalitics comes up. And what we are doing is that we are making your deep tech module or an AI model or any algorithm observable, monitorable, and ready to pilot. Good. We are able to combine any types

**[0:57](https://www.youtube.com/watch?v=gwSsWmPKdTU&t=57s)** of devices of any manufacturer working just with open protocols. Um This is how it looks like. So, it is module-based and component-driven and you're able to drag and drop all the components and monitor and not only how data flows in and out your module, but also the health of every module that you have plugged via wire or wireless. Um we are offering um our software in two domains. This is for industrial sensing, for the research labs, and for the AI data teams that need to collect large amounts of data and supply them in real-time either to AI pipeline or to a working model. Bonalitics also offers software for all the tech enthusiasts. We have a community that are absolutely free, so you can download it and enjoy >> [laughter] >> and building your own robot or home

**[1:55](https://www.youtube.com/watch?v=gwSsWmPKdTU&t=115s)** automation. You can install it in 5 minutes and a configure a basic surveillance use cases just 60 seconds. We configure all the rules for you. And you have if you have any feedback, if you are interested in looking a real demo, in looking some demo robots that we have built for you, you're welcome to visit us at the startup area near stage eight. That's it. Thank you. >> Thank you very much. You can you can hang on to that. We actually have a Naomi here from Nvidia who might ask you some questions. >> Sure. >> Naomi, do you have some something? >> Well, yes. I'm sorry. Let's test it again. Okay, I just I'm going to go further back. Thank you so much for the presentation. You say it starts with Raspberry Pi. You were kind of like alluding to it as a platform. Can you maybe like expand a bit on that? Like where does it also run? Because physical AI is coming up.

**[3:05](https://www.youtube.com/watch?v=gwSsWmPKdTU&t=185s)** You have more intelligent robots. Raspberry Pi is of course like a very small device. Are you also integrating with like other hardware components? And then the second part of the question would be a platform is great because it's universal, but it also makes it a bit intangible. Do you have a customer success story where you can give us like an example of how your platform benefited your your customers? >> Right now we Yes, I can start answering. >> [laughter] >> Good. So about the sensors. This not actually the software that runs as an H AI on any but uh what we do is that we install our software on a Linux or a Windows based PC as well as on Raspberry PI. So, it's not that we install it or create it for any kind of sensors. And afterwards, you can integrate any kind of sensors to the

**[4:08](https://www.youtube.com/watch?v=gwSsWmPKdTU&t=248s)** computer where you have installed our software. So, this is what we do. And regarding our customers, right now we have only end users as our customers. So, this is kind of enthusiasts >> [laughter] >> we have here. And right now, we are in the negotiations phase. We are coming up to B2B customers, to the research labs, for which we discovered that we can save terabytes of storage because we are able to provide them with that orchestrational and data acquisition layer for conditional recording of data. And we are able to fetch data to their modules in real time. This would be don't have the mostly the research labs they collect data for a week. Terabytes of data and then they fetch it once to their processing module. And then if they have if they made some corrections, they need another week to collect another chunk of data. So, that's it. We store terabytes of storage for them and

**[5:14](https://www.youtube.com/watch?v=gwSsWmPKdTU&t=314s)** provide this real time work. >> Since you guys have a home assistant integration, I'm I'm guessing people on your team also been using it at home. What's the what's the most fun thing that you've seen one of your co-workers use Ban Analytics for in their home? >> Pet monitoring. We use it instead of a pet camera. >> [laughter] >> That's amazing. >> That's it. And we send video footage into Telegram. This is a messenger uh real time. >> Cool. Very nice. Thank you so much.
