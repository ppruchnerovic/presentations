---
id: 683
title: "The 8th Layer: Building the Open AI Stack Before It Builds You"
slug: the-8th-layer-building-the-open-ai-stack-before-it-builds
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Cloud & AI Infrastructure"
type: "Lightning Talk"
stage: "Stage 7"
tags: ["AI Models", "Agents", "Innovation", "Linux", "Motivation", "Open Source", "Privacy"]
speakers: ["Raffi Krikorian"]
speaker_companies: ["Mozilla"]
day: 1
starts_at: 2026-07-09T11:10:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=Lb77eiIwi1E
video_id: Lb77eiIwi1E
session_page: https://app.wearedevelopers.com/events/16/session/683
transcript: true
---

# The 8th Layer: Building the Open AI Stack Before It Builds You

**Raffi Krikorian (CTO — Mozilla)**

`Track: Cloud & AI Infrastructure` · `Type: Lightning Talk` · `Stage: Stage 7`

`#AI Models` `#Agents` `#Innovation` `#Linux` `#Motivation` `#Open Source` `#Privacy`

[Watch the recording](https://www.youtube.com/watch?v=Lb77eiIwi1E) · [Session page](https://app.wearedevelopers.com/events/16/session/683)

## Abstract

We’ve spent decades perfecting the software stack — from LAMP to cloud-native to platform engineering. But AI is reshaping that stack in real time.

The real risk isn’t just technical debt. It’s strategic dependency.

In this lightning talk, Raffi Krikorian explores “the 8th layer” of the AI stack — the layer beyond infrastructure, models, and APIs — where incentives, governance, and control determine who actually benefits from AI.

What would a true “LAMP Stack for AI” look like? One that is open, composable, inspectable, and community-governed. One where developers aren’t just API consumers but builders of durable systems.

We’ll break down the emerging Open AI stack — from data to models to orchestration — and why openness at each layer matters for security, sovereignty, and long-term innovation.

If you’re building with AI, you’re already choosing a stack.

The question is: are you building it — or renting it?

## Speakers

### Raffi Krikorian

*CTO — Mozilla*

Raffi Krikorian is Chief Technology Officer at Mozilla, where he leads efforts to build trustworthy technology that serves the public interest and strengthens human agency. A long-time member of the Mozilla community - serving on the Mozilla Foundation Board since 2023, Mozilla.ai’s Board since 2024, and the Mozilla.org Board since its inception - Raffi brings a record of impact across technology, politics, media, and philanthropy.

He previously served as CTO of Emerson Collective, where he focused on how technology and data can be used to drive solutions that promote social good; as the first CTO of the Democratic National Committee, where he built the technology, data, and security infrastructure that supported Democratic candidates nationwide; as Director of Uber’s Advanced Technologies Center, where he led the rollout of the first passenger-carrying self-driving car fleet; and as Vice President of Platform Engineering at Twitter, where he designed and scaled the systems that powered Twitter’s global platform.

He also created Technically Optimistic - a podcast and Substack exploring technology’s impact on society - which during its run reached #2 on Apple’s tech podcast charts and featured conversations with leaders including Sal Khan, Nobel Peace Prize laureate Maria Ressa, Cory Doctorow, and Congressman Jay Obernolte.

## Transcript

*1,972 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=0s)** We have leading work on trustworthy public interest technology on Mozilla Foundation and Mozilla AI boards. He is the CTO of Mozilla, Rafi, and he's going to tell us about the eighth layer, building the open AI stack before it builds you. Welcome to the stage. Round of applause, please. >> Hello. Hello. Uh it's such a pleasure to be here. Uh my name is Rafi Krikorian. I'm sure you all recognize uh this string on the screen. Um I'm sure you've all parsed it, you've spoofed it, you've cursed at it. Um maybe this is the most told lie on the internet. So, it's sent about a trillion times a day. Um it's Chrome introducing itself as Mozilla. Or is it Apple WebKit? Or is it KHTML? Or is it Gecko? Or is it Safari? It's one browser by five names, four of them kind of borrowed, but every browser on Earth opens with their conversation with some form of this string. And I'm the CTO,

**[0:53](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=53s)** Rafi Krikorian, of the company that every browser pretends to be. So, let me tell you for a second why they lie and because I think it's about to happen all over again. So, maybe my small little history lesson for everyone. So, 25 years ago, there was a war for the internet and the prize was this string, the user agent, the software that was acting on your behalf. Like we called it is called a user agent because it's supposed to be the piece of software that represents you to the open web. It has your preferences, it has your values, it does things on your behalf, and you can control it. You can ask it to do things for you and not think for someone else. And so, that was the browser's entire job was to represent you on that web. And if you said you were a Mozilla 25 years ago, you got the good web, right? You got JavaScript, you got frames, you got all the stuff that made the web exciting back then. So,

**[1:51](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=111s)** everyone lied because otherwise you would get the junk version. So, everyone started saying that they were a Mozilla, and the main kind of froze. But, the what didn't freeze was whether or not the software is acting for you. And what I mean by that is sort of like that question of layer eight. Like, for all the networking nerds in the room, you know, OSI has the seven layers all the way to application, and the joke was always that layer eight was the problem between the keyboard and the chair. It was the human. And so, what we're starting to see right now is just new layer eight showing up. It's sort of like AI acting as a human. And it's one of the things I get most concerned about because it's it's the agent is becoming the new user agent. It's sitting in the same seat, but it's a different occupant. But, that that agent is now booking for you, it's buying things for you, it's writing for you, it's deciding

**[2:47](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=167s)** for you, and it's increasingly doing it without you. And so, before we dive into a bit more, I want to try to introduce a few new pieces of terminology to the conversation. Like, most of the time when we talk about these things, we get into the conversation of open versus closed. So, I want to bring up maybe rented versus owned. Because we can all agree on what open versus closed means, but the question is like, do you control software anymore, or is the software starting to control you? Do you get to choose what the software does, or are you living under someone else's incentive plans in order to try to make that happen? So, I really want us to start thinking about this frame of like, are we using software that is by someone else's incentives, or are we using software that's on our incentives? So we think about that user agent for a second. That user agent was under my incentives. It gets to do the things that I ask it to go do. It's not trying to shape the things that I'm trying to

**[3:49](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=229s)** do on the open web. So we'll get to that in a second. And the other one thing I think a lot about is like the industry has sort of thinks it's figured out what agents really mean. And it's all about this equation, right? Like agents are models plus a harness plus something else which I'll get to. Um right now both parts are open, right? Like we live in a world where the models are getting just as good as the closed one. So we have open models, GLM 52, like it actually works in a way that's pretty good compared to what the closed one does. And the same thing happens on the harness side. The harnesses are getting pretty good like open code has 175,000 stars, goose client alder. So like it's not the fact that the labs are doing all the work. You're starting to do the work. You're building all this stuff. But I think the thing that's missing like if you look at what we all used this morning, like I'm

**[4:46](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=286s)** still using cloud code. So I'm still I'm like the CTO one of the biggest open source organizations on the planet and even I use cloud code cloud code every single day. Even I am rent using rented software and not owned software. And I think that's because of this missing term which is you in all of this. Your identity, your credentials, your memory, your authority. We don't have good open standards on how to build that kind of stuff just yet. So if you think about what we're doing with cloud code, like it has my repo. In some cases some of you probably gave it your get identity. Some of it probably gave it your prod keys. We should probably talk if you did that. Um so we're actually all renters in this situation. We're not early adopters. We're the first tenants in this system. The parts that we thought were good got opened, but we forgot about some parts that we need to go solve. And so, I think about this a lot

**[5:43](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=343s)** because coding is probably the only the opening door. So, again, CTO of a company that builds one of the biggest browsers on the planet, my browsing is down these days. So, about 70% of browsing right now on the web is having on by some form of agentic agent doing that browsing for me, and I'm guilty of this, too, right? Like I run an Hermes agent in my closet and it's basically taking a bunch of my browsing from me. It just does stuff on my behalf. And this is starting to happen everywhere. We don't need search tabs anymore. We just open a chat tab. We're not browsing the web anymore. We're being served it. And I know it because this is happening to me that the web is now arriving at a single answer, and I'm not the exception. You know, we used to make fun of these 10 blue links on a web page. We used to dunk on them all the time because it's full of spam,

**[6:38](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=398s)** it's full of SEO, it's full of ads. But what do we forget about? Like my mom can look at these 10 blue links and get a general sense of what's happening on the internet. But if you only get one single response from a chat agent, you don't have a good sense of what's going on anymore. And we're now rapidly starting to build a world where the web is being read by machines, is not being read by humans, incentives are starting to be pointed in a particular direction. And I want us all as developers to really start to think about that. Because I'm not scared of this world. I think we can actually do something about it. So, this number is that 25-year-old history lesson. Like when Microsoft was trying to take over the web, 95% of web traffic was run through Internet Explorer. And look, that number has gone down. And it's because of people like us that we didn't want to build toward IE's quirks.

**[7:33](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=453s)** We wanted to build toward standards. We We were the kids who installed Firefox on our parents' computers because we wanted to try something different. So, Mozilla didn't beat Internet Explorer, people like you did, because we just built our way around it. So, I don't think we're actually into a second battle, I think we're onto a sequel of the original battle that happened 25 years ago, and I think we can do something about that. So, like the closed stack in my mind has one simple business model. So, going back to that oak owners versus renters, is that they want to rent it to you. The open stack, however, can be built by all 15,000 developers that are floating around this conference. Like, there are so many examples around Mozilla right now. Like, we run a data company, and one of the things that we're doing is like we're trying to license provenance based data to any developers on the planet. And a market in Basque decided to build their own LLM based on data that's now freely available and are have right provenance on it. So, and it's beating GPT-4 on

**[8:36](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=516s)** what it can do. So, I really believe that we can start to build what that future looks like. I was talking to the Home Assistant developers the other day, and they built a virtual home assistant, voice home assistant, that doesn't leave your house. Like, none of the data ever traverses your firewall to get out in the public internet. All prob- it's all processed inside, because no one would sell that to them, we had to go build it instead. And I think we can do this. Like, right now, the open stack isn't finished. There isn't a lamp stack for AI yet. And that's one of the things that I would challenge us all that we need to go build. Like, right now, open source AI is served like this construction site, and what's missing is private inference, what's missing is credentials, what's missing is memory, what's missing is authority. And so, we're going to be building a map of what all those missing pieces look like.

**[9:31](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=571s)** We'll be publishing it next week. And so, I really want all of you to look at it to be like, what are the things that we can contribute to make sure we can get to a world where open source AI is actually owned by all of us, and we're not just renting it. Because I really feel that 25 years ago the question was whose side was the browser on, but right now the question is like whose side is all the agents that we're relying on actually on. How do we make it so that they're running on our hardware, on our data, in our closet, under our control? You know, the labs have the capital in order to do the things they do, but we lived this before where open source allowed us all to come together, all the developers, and we can outbuild them in the process. So, I really want us all to think about how we can build that new layer eight in a way that's

**[10:26](https://www.youtube.com/watch?v=Lb77eiIwi1E&t=626s)** owned by us and not rented by us. So thanks. >> [applause] >> I have you you want to do a little
