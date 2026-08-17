---
id: 925
title: "Why your codebase lies to AI?"
slug: why-your-codebase-lies-to-ai
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Engineering"
type: "Keynote/Talk"
stage: "Stage 2"
tags: ["AI Coding Assistants", "AI Standards", "Anthropic", "Agents", "Case Study", "Claude", "Copilot", "DeepSeek", "Developer Experience (DevEx)", "GitHub", "GitLab", "Heroku", "Jira", "OpenAI", "Product Management", "Project Management", "Startups", "VS Code"]
speakers: ["Zaak Chalal"]
speaker_companies: ["Mobioos"]
day: 2
starts_at: 2026-07-10T11:00:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=ADcdC7L8VkM
video_id: ADcdC7L8VkM
session_page: https://app.wearedevelopers.com/events/16/session/925
transcript: true
---

# Why your codebase lies to AI?

**Zaak Chalal (CEO — Mobioos)**

`Track: AI Engineering` · `Type: Keynote/Talk` · `Stage: Stage 2`

`#AI Coding Assistants` `#AI Standards` `#Anthropic` `#Agents` `#Case Study` `#Claude` `#Copilot` `#DeepSeek` `#Developer Experience (DevEx)` `#GitHub` `#GitLab` `#Heroku` `#Jira` `#OpenAI` `#Product Management` `#Project Management` `#Startups` `#VS Code`

[Watch the recording](https://www.youtube.com/watch?v=ADcdC7L8VkM) · [Session page](https://app.wearedevelopers.com/events/16/session/925)

## Abstract

AI coding tools promise to understand your codebase and accelerate software delivery. Yet developers keep hitting the same wall: hallucinations, context overload, fragile fixes, and AI systems that struggle to understand real-world projects.

The problem is not the model.

The problem is the assumption that your codebase contains the truth.

In reality, code is only a projection of business intent. The reasons behind architectural decisions, production constraints, customer feedback, operational risks, and business objectives are rarely visible in the code itself.

In this session, Zaak Chalal challenges one of the most widely accepted assumptions in AI-assisted development: that indexing and vectorizing a codebase is enough for AI to understand a project.

Through real-world examples and live demonstrations, he explores why AI fails on legacy systems, why context engineering is becoming the new bottleneck, and how organizations can move from code-centric AI to intent-centric AI.

If we want AI to become truly effective in software engineering, we need to stop asking it to guess the truth from code and start giving it the context it actually needs.

## Speakers

### Zaak Chalal

*CEO — Mobioos*

Zaak Chalal is the founder and CEO of Mobioos, a company pioneering context engineering for software development and AI-assisted delivery.

A software engineer and entrepreneur for more than 28 years, Zaak wrote his first programs on a Commodore 64 and later contributed to some of Europe’s earliest large-scale digital initiatives, including Ooshop, Carrefour’s pioneering e-commerce platform.

Throughout his career, he has led software engineering, architecture, and digital transformation initiatives across multiple industries. His experience exposed a recurring challenge: organizations struggle to preserve and operationalize the business context behind their software systems.

Today, through Mobioos, Zaak focuses on helping organizations transform business and technical context into a strategic asset that can be understood and activated by humans, AI systems, and autonomous agents.

His work challenges the traditional assumption that code alone is the source of truth and explores how context can become the foundation for reliable AI-driven software engineering.

## Transcript

*2,881 words · source: yt (en)*

**[0:37](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=37s)** It Ah, okay. That good. Hello everyone. I'm so happy to be here with you. I'm a CEO of Mobius, Mobius AI. Uh I would like to love to talk uh code. It's my passion. >> [snorts] >> Uh the code is very my passion. It's my first experience. I start with the Commodore 64. Uh with the basic, assembler. It's a long time ago. I have around 11 years. Uh now I I I I have 54 years uh year old. Uh and uh it The code is my passion and I still love a good line of code today. That's It's uh

**[1:27](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=87s)** It It's important for me the the good line of line of code. My message is also for the developer because you know the AI the AI it's a a lot of change for the developers. I code a lot of time. I just want to share the message. Don't fear AI because I think for my point of view the next area belong the the to developers. It's very important to think that that just to focus on the volume impact of line of code on the market. Line of code it's everywhere. You take the escalator, you take the elevator, you have line of code.

**[2:15](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=135s)** Uh you have line of code around the world. That's uh if you see the the IoT device uh you have a lot a lot of million device on the market. It's the same case for the developers. Uh 30 million now uh 45 million uh next years. It's very huge and it's the same case for line of code. Uh around the last 60 years we build uh 70 uh 76 million line of code. For the next 5 years we build 500 million line of code. Uh 500 sorry uh million application. That's huge. That's huge. Yes, with the AI it's very interesting

**[3:06](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=186s)** part to help to build the that. For the developer the market for the job it's also very important. It's increase. You you you need to uh to have more job more more uh hearing developer for the market. That's it's a it's important to know the developer. We need always with the AI. Why? Because you have a lot of massive line of code on the project. We need to manage this. Yes, the role of the developer change because it not not focus on the build line of code but we need also to manage line of code. The the role of the developer change. We need also to manage the

**[3:56](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=236s)** uh the requirement, the uh uh the business inside the line of code. Another aspect it's very important. It's the volume line of code built by developers. Uh before AI area, we we build uh 780 uh line of code around, you know. Uh when AI come on the market, we increase the volume line of code, uh but uh we need also with a to build a lot of application to increase this line of code to build. Another aspect on uh when we build the application, it's uh the code overhead. The code overhead, you have two parts. One part built by

**[4:45](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=285s)** the AI, another part built by developer. The 60% built by the AI, it's the more simple line of code. The other line of code built by developer, it's a complex line of code. You know, the you need a developer to build very complex parts. Another aspect, it's uh the overhead with the AI, it's huge. Why? Because you need to iterate. You always you need to iterate. For this reason, you have a lot of wasted uh and a lot of overhead line of code with a AI. Uh for the complex parts, uh you have also a lot of iteration, not with the AI, with you. Because the part of the complex line of code, it's uh

**[5:34](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=334s)** necessary to focus, uh to thinking, to build the best uh component. That's it's important to know the cover of AI is not complete. Why? Because you have a complex part and you need to to focus on this complex part. I think the the role of the developer is to manage the AI, to build the the commodities of your application, and you need also to have a very high skills to build the complex parts. Another aspect of the AI, well, okay. It's the context board. I know a lot of developer use Obsidian example. You have a lot of markdown.

**[6:22](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=382s)** That's is crazy. Why? Because your code grow, in the same time, your context grow. You you need to have both code and context, but the impact of this is huge because if you start with a LLM, you start with a you need to load your context. If you load the context, you have you charge the memory of the LLM and you touch another effect. It's more important. It's the context route. The context route you decrease the the accurate thing of the AI. You need to avoid to charge the memory of the LLM to enter and this context route effect. That's

**[7:12](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=432s)** the context is very interesting to store it. To focus on these parts. If you load the context, the context route with accurate context, the context route is avoid. You need not to have a mass context, you need to have more accurate in context. This very different. If you you have accurate in context, not a mass context, you you your AI it's more accurate. For this reason, if you charge a lot of markdown in your same side of the code, you you enter in this context blood. After in context road.

**[8:00](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=480s)** My recommendation, it's less less context. You you you don't exceed 80k on the context. Very small context is better, but small and accurate context. This is for for pain. The The next pain, it's the business intent. The business intent it's so very important. You have a lot a lot of work with a business user, project manager to to formalize your specification. But one one the effect on the business intent, it's the build the implementation. What is the

**[8:48](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=528s)** pain? Well, the pain it's the implementation it's an interpretation. If you have one business intent, but you have 100 developers or 100 AI, you have 200 implement interpretation. This is it's the problem, but the the software industry, it's crazy. Why? Because historical, we want to master the code base from the code base with a reverse engineering. Always, but this path it's not very good. Why? Because you start from the interpretation to the business intention. You need to reverse this situation. You need to to to business intention and to look your

**[9:38](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=578s)** code and to look your interpretation. This is the best way and with my PhD team, we work on this pain. We work on this very important pain to find on your code base your business intention and to start from the business intention to the code base, not the code base to the business intention. And with with this way, we create a very accurate in context, more precise for your code base. Just to explain this situation. On the top, we have the software industry. On the below, we have the PhD work on my with my team.

**[10:28](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=628s)** The software industry with the AI, we understand your code base with a technical approach. You understand the technical aspect, not the business intention. Okay? And And if we ask a request on your code base, the request is only focus on the technical aspect. With With Mobius, we work to augment semantically the code. Behind the line of code, we create a semantic solution to understand the code with a business intention. After that, we cover a lot of information of your code base. We cover the technical, the business intention,

**[11:18](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=678s)** a lot of information of the of the code base. For this, we have three step. The first step is create a semantic perspective on your code base. You have a lot of ontology. You have a lot of domain context to explain the business perspective on your code base. On this sample, we have three, your user journey, your risk, and your your feature. And to create this business semantic view on your code base, you have two ways. One ways, it's a one AI to talk with your team, to retrieve a lot of data like specification,

**[12:06](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=726s)** requirement. If you don't have requirement, that possible to to use video to explain your application, your solution, and to retrieve from this video a feature of your application. After that, we design the feature of your application for this uh domain context. It's the same case for another context. This is it's the first year, AI, sorry, to design the the domain context like the feature. The second way, it's another AI. It's AI to crawl your code base. This AI knows the semantic feature of your project and crawl your code base to understand the interpretation, you know? This is

**[12:55](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=775s)** not the classic way or the uh historic way of the software engineering start you from the code base to understand your business intention. No, we we create this business intention, and after that, we crawl on your code base to highlight this business intention. After that, we link this business intention to the semantic, and we understand semantically your code base. This is its first step. The second step, it's a data. It's most important part to understand your code base because the data it's available on all in your system information for the requirement, for the development, for the design, for the projection, and also for the customer success. That possible

**[13:45](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=825s)** to retrieve a lot of this data like example for the ticket with your customers from Salesforce. We retrieve this ticket and we filter because we need to avoid the noise of the data and we we project this data on this on the this semantic view. After that, we have very complete information semantically on your code not in technical perspective like classical but with a semantically for different domain context. Let show a demo to to explain that with a

**[14:35](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=875s)** demonstration. I don't know if it starts. Okay. Here we go. This is it's a project called Gronod Gronod sorry just pause. Gronod it's a e-commerce project from GitHub is not built by Mobius team and in this GitHub project we find an issue. This issue it's a simple but it's a it's a very strong. If you add a project in your basket, you increment the quantity, the price that

**[15:25](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=925s)** doesn't change. Okay? Uh we need to fix this bug without uh to understanding the semantic code uh your code base and with to understand the semantic in your code base. You have two ways and uh uh each ways it's different because you you you have some issue of the of the way. You I increment the quantity, the price doesn't doesn't change. It's okay. I ask uh Cursor uh with a prompt and I said uh "Please fix this this bug." But I don't use the semantic context of of this sample, okay? Look that. It's

**[16:15](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=975s)** very uh strange but normal. Uh Cursor need to crawl your database. But before to crawl, business uh Cursor knows your database because it's vectorized. Uh after that, you need also to to crawl to find this issue. During this uh uh uh crawling, the context window of the LLM it's slowed. You enter in the uh context right effect. Oh, sorry. Sorry. It's uh Okay. Okay. During uh

**[17:08](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=1028s)** 40 minutes Cursor crawl your data crawl your database and to know to um to uh fix this issue. 40 minutes and during this step you lose a lot of token, you increase your context window because it don't know really truly your your feature. After that, Cursor suggests to modify your line of code with a with a new sorry. It's so long. But it's really real Yeah. That's Okay. This is it's Cursor suggestion.

**[17:59](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=1079s)** The the suggestion is to update two line of code. Okay? To fix this bug. I need to accelerate this. Okay. I try, you know? I try, but the bug didn't fix. Why? Because the context is not accurate, you know? For this reason. Now I roll back all this change. But now I use a semantic context on your code base to change the the to fix this issue.

**[18:48](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=1128s)** I roll back. I ask the same prompt, sorry. But now I use Mobius from MCP, but that possibility to use from skills, from CLI, from API. We We have a lot of protocol to retrieve a lot of semantic context. And after that, look that it's very in it's very nice. You it's a sniper mode. You find where is your issue and you fix very quickly this issue. You switch to 4 minutes to 40 seconds. And you don't lose your token.

**[19:38](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=1178s)** You don't You don't lose the time. Sorry, I need to accelerate this. Okay. Look that. The the suggestion is not two line of code, but it's four line of code. Why? Because the context the semantic context is more accurate. It's a sniper mode. You know where we need to modify the the code and to fix this issue. That after that, okay. Sorry. After that, we need to test. I refresh the application and I increment

**[20:26](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=1226s)** that it's fixed. Just to come back here just for the the conclusion. That's if you have some code base with a markdown on the side on the same side of the of the code base, you enter on the effect it's called context bloat. And if you charge, you load a lot of context for LLM on the session and you force to When to enter another effect it's called context fraud. You need to have less context and more accurate context for the better

**[21:16](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=1276s)** accurate option. That's another aspect. It's most important. You need to to understand your code base call for LLM. It's just understanding the technical aspect. Uh not really functional aspect. You need for this reason to add a lot of markdown context to explain your code, to explain your architectures. That's it's a it's a way actually and you need also to charge a lot of markdown. But uh that's if you context very shortly, very accurate, you have uh more information about your your code base.

**[22:09](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=1329s)** That's all for me. Thank you for your presentation. Thank you. >> Thank you so much, Zach. What an incredible job. One more round of applause for Zach, everybody. >> Woo! >> Fantastic. We have time for like one question. In fact, submit your questions here so I can ask them if you have any. Question number one comes from Lennart. He wants to know what's the highest impact change a team can make in an existing code base to improve AI assistance but without rewriting everything. >> For for the team? >> Yeah. The highest impact change they can make to get the benefits of AI but without rewriting all the code. >> Ah you you you have a big change. Very big change because the

**[22:56](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=1376s)** Now we need a small small team. Why? Because the role of the developer change. The developer is not developer to create a line of code. It's manage a line of code. But also the project manager, the role is change. Why? Because for the project manager, we don't need to detail the the specification because this role move to the developers. The project manager need to explain the topic, the goal, the objective and the you have a little team, little technical team to retrieve this topic, this goal and to explain the detail of the specification. And after that, to manage the agent to AI to build your

**[23:46](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=1426s)** application. It's a very very a big change. You don't need a large team, small team, but very focused on the business and developer need to increase the role not only to build a line of code to manage the code and to manage the business for the code. >> Okay, wait. Thank you so much. Everybody one more round of applause for Zach, everybody. So cool. Thank you. Thank you, Zach. >> Thank you, too. >> It's time for the next talk. Our next talk comes to us from from Dynatrace. It comes to us from Shawn Odell, the head of developer experience, and Gala Dwaratskaya, the observability experience lead at Dynatrace. This is a very exciting talk. I don't know why anyone's leaving, honestly, because I would stay. It's a wonderful talk about one interface and two audiences. It's a it's a developer experience talk. And at

**[24:35](https://www.youtube.com/watch?v=ADcdC7L8VkM&t=1475s)** a conference like We Are Developers, um developer experience matters. So, we're going to hear about designing applications that are CLIs, but both for humans and for AI agents. Um there are agent experience primitives here that are high value. So, while the next speakers come in, that's what's going to happen here on this stage. Thanks.
