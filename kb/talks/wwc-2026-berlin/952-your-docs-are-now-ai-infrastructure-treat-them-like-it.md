---
id: 952
title: "Your Docs Are Now AI Infrastructure (Treat Them Like It)"
slug: your-docs-are-now-ai-infrastructure-treat-them-like-it
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Developer Experience"
type: "Lightning Talk"
stage: "Airstream 1"
tags: ["Advocacy", "AI Coding Assistants", "APIs", "Documentation", "Embeddings", "Retrieval-Augmented Generation (RAG)", "Vector Databases"]
speakers: ["Emil Sorensen"]
speaker_companies: ["kapa.ai"]
day: 2
starts_at: 2026-07-10T11:35:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=yYU2V1aN91I
video_id: yYU2V1aN91I
session_page: https://app.wearedevelopers.com/events/16/session/952
transcript: true
---

# Your Docs Are Now AI Infrastructure (Treat Them Like It)

**Emil Sorensen (CEO and Co-founder — kapa.ai)**

`Track: Developer Experience` · `Type: Lightning Talk` · `Stage: Airstream 1`

`#Advocacy` `#AI Coding Assistants` `#APIs` `#Documentation` `#Embeddings` `#Retrieval-Augmented Generation (RAG)` `#Vector Databases`

[Watch the recording](https://www.youtube.com/watch?v=yYU2V1aN91I) · [Session page](https://app.wearedevelopers.com/events/16/session/952)

## Abstract

Your documentation has three audiences now. Customers reading the docs site. Support agents drafting replies. And AI tools, Cursor, Claude Code, Codex, answering questions about your product on behalf of developers who never visit your site at all.

That last one changes everything. The same docs that used to be a static reference are now the grounding layer for every AI feature your developers touch, including ones you didn't build. If your docs are messy, outdated, or missing the answers users actually need, every agent querying them inherits the problem and your product takes the hit.

In this lightning talk, we'll show how kapa.ai operates as the knowledge engine behind production AI deployments at companies like Sentry, Netlify, Monday.com, and n8n, processing millions of developer questions per month. We'll walk through real analytics revealing the "dark matter" of documentation like which topics generate the most uncertainty, which pages quietly underperform, and how unanswered questions cluster into a prioritized backlog for content and product teams.

The takeaway: stop guessing what to document. Let your users, and the agents querying on their behalf, tell you. With concrete benchmarks: 20-40% support ticket deflection, hundreds of developer-days saved per year, and a path to treating docs as the grounded foundation every AI feature in your product needs.

## Speakers

### Emil Sorensen

*CEO and Co-founder — kapa.ai*

Emil Sorensen and kapa.ai has been on the forefront of AI-based documentation assistants since they launched in June 2023 and completed the YCombinator S23 batch.

Now Emil works closely with top tech companies including OpenAI, Docker, Mapbox and OSS projects to help provide instant AI-answers to developers worldwide.

## Transcript

*1,984 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=yYU2V1aN91I&t=0s)** Appreciate it. It's super super fun to be here. Hopefully you're all staying reasonably hidden in the shade. Um My goal today is to convince you sort of in the next 10 minutes that there's a new increasingly important reader of your documentation and that's of course agents to no surprise. But agents come in many different flavors. Um With that in mind, just maybe a quick intro beyond uh um beyond what's already said. I'm Emil and one of the co-founders of of Kappa. Um we're a startup that work with more than 200 companies to kind of provide um AI chat um and agent experiences. So we get to work with a lot of the cool folks that are exhibiting here today. Lots of developer tools, folks like Netlify, Sentry, Grafana, OpenAI to kind of power their customer-facing AI experiences in various um shapes and forms. Um and because of that, we've seen an interesting shift that essentially happened since Claude Code dropped um that I'm sure many of you are experiencing that are developing too that there's a new reader of documentation and that is of course AI agents and that changes a lot of things. Um [snorts] But before we get into that,

**[0:59](https://www.youtube.com/watch?v=yYU2V1aN91I&t=59s)** maybe interesting to just context set historically, right? Who's who's been readers of documentation in the past and and what does that look like today? Um historically of course, it's been users, it's been developers like yourselves in the audience that go to documentation sites and still do. Um but just as importantly, the folks that work for these companies, be it support engineers, account executives, etc. that need constant context about a product. They spend a lot of time in documentation. And that is still true, but that's now of course being disintermediated by various sorts of AI agents. The obvious ones of course being things like Claude Code, Codex, etc. But there's a lot more nuance here. Um and and maybe to introduce those other types of agents that are consuming your documentation, really it's it's it's workflow agents. Perhaps at your companies already, you're spinning up your own personal agents that, you know, read context from documentation to answer RFPs, transfer support questions, and so on. That's an interesting second category, but but really the third and and arguably most interesting one because it's the one

**[1:53](https://www.youtube.com/watch?v=yYU2V1aN91I&t=113s)** that we can actually look at and understand how agents are behaving. Are these types of sort of agents that folks deploy in product? I'm sure if you all have been kind of walking the hall today, you've seen a lot of these sort of in-product co-pilots, agents, sidekicks. They have lots of different names, shapes, and forms, but kind of the the the the the obvious one is a if you've seen any sort of app that has a sidebar where you're talking to it and you're interacting with with a product now, chances are that has some awareness of your product or of your documentation. Um these are really interesting. We we personally as a as a company have gotten to sit at the forefront of working with lots of cool teams that are building these to understand where these fall short because essentially in today, it's still incredibly early. Most of these aren't eval. Most of these aren't um like don't have um too much like there's a lot of thought that go into these, but there's not a lot of consistency in how a lot of these agents are essentially built. Um and I thought for today's talk, we could perhaps provide a unique

**[2:52](https://www.youtube.com/watch?v=yYU2V1aN91I&t=172s)** perspective given we get to work with a lot of these companies and and essentially say how are agents working with documentation. Um it's a little bit harder to know things like cloud code and so on because well, only Anthropic and OpenAI has that data and lots of incentives to not share that with us, but here we can actually look under the hood to say, "Hey, how are agents actually consuming documentation?" Um A data point so far and and maybe what will kind of frame the rest of this talk is we as a company have one of these agents deployed, too. No surprise, it'll look very familiar to any other sort of company agent that you've used in the past. It'll, you know, have some sort of chat interface deployed within a within a web app. For us, the context is is pretty straightforward. You know, for for someone like a Netlify or a Grafana or Juniper Networks that will use us to power all their kind of user-facing AI interactions. Well, there's just a ton of questions that goes through a system like this, and analyzing this by hand or

**[3:48](https://www.youtube.com/watch?v=yYU2V1aN91I&t=228s)** even sort of aggregation is hard. So, having sort of an AI agent can be really really helpful to sort of understand the the kind of underlying data. Um so, we have one of these deployed. It has about 30 native tool calls. We've iterated a ton on this, updated the harness, and people use this like crazy. So, it's like a really really interesting um really interesting data point because we just looked like, "Hey, this thing has 30 tools. It can do pretty much everything our UI can do." And we also added knowledge-based search because it's very close to our heart as as a company. Um and over not a long period, I think this is just over a couple days, like a few thousand or thousand or so conversations, we kind of broke down to say, "Hey, how how is this agent actually using its tool calls?" And I think the thing that shocked us under the hood was just how frequently knowledge-based search is being used. It's by far the single most dominant tool call that that an agent like this uses. Um just for context, you know, I think in 50% of cases, like these native

**[4:46](https://www.youtube.com/watch?v=yYU2V1aN91I&t=286s)** tools are only used, you know, things like create a chart, create an API key, do something in the app. Um [snorts] contrast that with a third of cases, it's just knowledge-based search. You know, you put an agent like in your app, people are going to start asking it questions about your product. And the interesting things happen when you combine the two, and I'll show you a few examples here. Um because essentially rest of the talk now is just going to be the three most interesting things we found when looking at this data. Um first one, it's actually just looking at what happens when like an agent just interacts with your documentation. Like again, as I'm sure you've been walking the stands, you've seen a lot of these. People have lots of cool ideas of how, you know, you can integrate an AI agent into your product. When you do that, like the numbers don't lie. Over a third of cases, people just ask it questions about your thing. They think it's a support bot. They think, you know, it's an onboarding assistant. And having some sort of fallback as a

**[5:41](https://www.youtube.com/watch?v=yYU2V1aN91I&t=341s)** documentation search tool call or knowledge base search tool call will totally be helpful there because it can just go figure things out. So, super super helpful to have these. The second kind of out of three findings, um this was the first one with that kind of made her scratch her head and go like, "Huh?" Like this is kind of neat. The first one you can kind of reason to if you give an agent access to this, it's going to help you answer kind of supporty questions. Here we actually saw it had interaction effects with the native tool calls. So, what happened was a lot of times, you know, the user would ask the agent to do something, take an action in the app, and it wasn't perfectly clear what the the response of the tool call was without searching a knowledge base to understand, "Hey, what is this result mean in the context of um in the context of your app?" Again, impossible to read this on the screen um here, but yeah, a canonical example of like, "Hey, you know um what kind of MCP integrations do I have

**[6:37](https://www.youtube.com/watch?v=yYU2V1aN91I&t=397s)** installed?" Some user was asking this in our app. Uh lists the different integration types, and only by searching the knowledge base because the engineer who implemented the the agent hadn't thought to fully write like a really really long like um like skill or something explaining our different types of MCP tools, but only by having this did it understand that, "Oh, okay, you know, there's different types of off to these MCP servers." So, like just kind of the first case of like a really interesting like interaction effect between the two. Um the third and last finding I'll leave you all on is it gets really weird sometimes. Like when we looked at a lot of like the more advanced agent traces, what we saw happen quite frequently in these agents is that um a user would ask a question, and users ask questions and do so usually like pretty poorly. And it wasn't clear based on the tools that we had given it, based on the full context, what exactly to do. So, the agent kept reaching for knowledge base search to kind of help it figure things

**[7:32](https://www.youtube.com/watch?v=yYU2V1aN91I&t=452s)** out and plan. Um there's some really cool examples of this we found that the trace again impossible to read here. Um, but but but I think the one to kind of like maybe bring this to life. We had an example of a user that came in to kind of try to figure out whether any like examples of conversations um, where users had really negative sentiment. Turns out when you have these AI assistant live and it's doing lots of volume for you know, lots of users. People don't really say negative things to these. So, the answer is no, we don't have native functionality built in, but we have lots of proxies like you can down vote things and you can tag things after the fact. Um, and because it had knowledge base search the agent was actually able to find uh, these things out and then go look for in conversations to actually satisfy the user request. So, just some like really interesting interaction effects when you add knowledge base search. That's what I'll leave you all on. The final thing to say, um, and of course I have to say this here, but like the

**[8:29](https://www.youtube.com/watch?v=yYU2V1aN91I&t=509s)** quality of knowledge base search matters a lot. Hopefully at this [snorts] point I've convinced you all that like it's pretty important when you're building agents to have these. Um, there's a lot of different ways of implementing them. If you're lucky enough that your product information lives in the web, you could use things like, you know, web search APIs, you know, if if you could build your own like rag retrieval system and so on. Or you could just like use something super state of the art. That's what we do. Uh, that's what most of our time is spent doing e-valuing and so on. Super agentic uh, a retriever under the hood. Um, it just works really really well. And given it's important for agents, we think um, you know, building these types of systems on top of Compass many of the companies that are here today have done um, is is is is a super super cool thing. Um, that's it. I set out to make the point that uh, docs are important for your agents. Hopefully by this point um, you at least learned something and you

**[9:24](https://www.youtube.com/watch?v=yYU2V1aN91I&t=564s)** found that mildly interesting. Cool. That's it. >> [applause]
