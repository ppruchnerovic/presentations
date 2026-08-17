---
id: 603
title: "Designing UX for SRE Agents in High-Stakes Incidents"
slug: designing-ux-for-sre-agents-in-high-stakes-incidents
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Agents"
type: "Lightning Talk"
stage: "Airstream 2"
tags: ["Agentic AI", "Site Reliability Engineering (SRE)", "UI/UX"]
speakers: ["Osmar Matos"]
speaker_companies: ["Hyground"]
day: 1
starts_at: 2026-07-09T08:10:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=8EAnGIUNu_U
video_id: 8EAnGIUNu_U
session_page: https://app.wearedevelopers.com/events/16/session/603
transcript: true
---

# Designing UX for SRE Agents in High-Stakes Incidents

**Osmar Matos (UX/UI Design and Frontend Lead — Hyground)**

`Track: AI Agents` · `Type: Lightning Talk` · `Stage: Airstream 2`

`#Agentic AI` `#Site Reliability Engineering (SRE)` `#UI/UX`

[Watch the recording](https://www.youtube.com/watch?v=8EAnGIUNu_U) · [Session page](https://app.wearedevelopers.com/events/16/session/603)

## Abstract

Incident analysis isn't a straight-line calculation, it's a maze. Every alert opens a fork: deploy regression, dependency flap, or the first step of something larger. Older LLMs stumbled at the first fork. Newer models navigate these branches and backtrack when a hypothesis doesn't hold. At Hyground, we don't hand our SRE agents exhaustive runbooks. We give them a foundation in operations work and pointers to metrics, logs, and wikis, then let them run.

That forces us to rethink what UX means. When the trajectory isn't one you can wireframe in advance, what are you actually designing? Engineers want control, most of all at 3am with a pager going off. How do you surface an agent's reasoning without burying the operator in text? How do you give the human steering authority over a process whose next step doesn't exist yet? We will walk through the interface patterns we landed on in Hyground, the ones we discarded, and close with a question: when the thing on the other side of the screen is an intelligence of its own, is "user interface" still the right word?

## Speakers

### Osmar Matos

*UX/UI Design and Frontend Lead — Hyground*

Designer by degree, frontend dev by passion, manager when necessary. 15+ years in web development. After designing and coding for blockchain stable coin financial infrastructure, shifted to AI SRE agents — helping SREs and DevOps engineers finally get some sleep.

## Transcript

*1,040 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=8EAnGIUNu_U&t=3s)** It becomes harder to plan or to design a UI that you don't really know what it's going to show to the user. >> [snorts] >> And when you think about generative, if you are a little bit nerd, you know the AI from Iron Man, the Jarvis. Um we want to get to a point where we don't have to worry about UI. Um you ask and it gets it done. It sends commands, it sends orders to the factory, to a message to your family, and controls uh the robotic suit you are wearing at the same uh the same time. >> [clears throat] >> But until we get there, we're going to take some time still. And now we are in this in between where we mix the the deterministic UIs

**[0:52](https://www.youtube.com/watch?v=8EAnGIUNu_U&t=52s)** with the generative uh paradigm. And yeah, that's what we have to solve at the moment. So, again, we have the same problem. We have infinite possibilities behind a chat interface. So, before I continue, I'm going to give you a bit of context. Uh an SRE is a site reliability engineer. So, he's the person that if your application crashes or if your e-commerce goes down at 3:00 in the morning on a Sunday, they are the ones that are going to wake up and fix it. All right, so we even joke that they're going to wake up at 3:00 in the morning to fix a problem they didn't create in codes they didn't write. >> [snorts]

**[1:40](https://www.youtube.com/watch?v=8EAnGIUNu_U&t=100s)** >> At AI Ground, the an AI SRE agent, it is an agent that lives inside your infrastructure. So, it's beside your app in production and it connects to everything. It connects to your metrics, to your logs, to your code base, to um your error [clears throat] system, your ticket management, to everything. So, uh it knows what's going on to answer the most important question, if you are waking up at 3:00 in the morning to fix something, that is what the [ __ ] is going on. >> [snorts] >> So, a bit of uh how we solve it there. We also started with a chat interface. Yeah, I didn't know it would be outside, so

**[2:26](https://www.youtube.com/watch?v=8EAnGIUNu_U&t=146s)** I can show you the get after the um the light version. Now, it's hard to see there. We started also with the chart um interface. We have a generative back end, so we also had to adapt and use generative UI. And you probably know the main types of generative UI are the static, uh open-ended, and declarative. I'm not going to get into much too much details here. Static, it's a very strict. You code every component. If the component's not there, and the and the LLM tries to use it, you don't show it. An open-ended, it's kind of you give the LLM an HTML and CSS, and it's going to build something for you.

**[3:14](https://www.youtube.com/watch?v=8EAnGIUNu_U&t=194s)** And declarative, you kind of give guidelines, and the LLM has some freedom within your guidelines. So, your colors, uh you build some components or uh chart library, and it's going to use it based on the criteria you predefine. And that's how we we solve it at High Ground. So, we have a chat session, and based on the content of the investigation the engineer is doing at the moment, it's going to build um the UI elements. So, here we have a table. Um Yeah, a chart. Uh a

**[4:02](https://www.youtube.com/watch?v=8EAnGIUNu_U&t=242s)** flow of fluxogram. Here a bit more complex. It shows to the engineer exactly the command that the AI is running in the server and the response it gets and it shows the whole trail of the investigation. And um and then we noticed that our customers were not really being able to get to these nice features, to get to charts and that to flows if they didn't have some sort of training before. So, we started thinking about ways to show these capabilities in a way that are more familiar with. And then we we call it the un-shell pattern that um we basically um

**[4:51](https://www.youtube.com/watch?v=8EAnGIUNu_U&t=291s)** yeah, extract the um these features to a specific UI. Um here for example, the dynamic dashboards. Um if a user goes to the chat and asks, "Can I visualize the performance for the last last 7 days?" HighGround will go to the server and will get all the metrics and logs and will um will print some charts. But the user will have to have this in mind and have to know before they have to ask for that. So, to facilitate that, we built a specific UI that will use the same the same background the same back end to generate uh dashboards that um the user can then save and then revisit um anytime they want. Uh another example is a search.

**[5:42](https://www.youtube.com/watch?v=8EAnGIUNu_U&t=342s)** Um since we are connected already to Jira, to Confluence, to enter base, to Kubernetes, the user can use one text input and search everywhere. So, if you want to know about the checkout system, you type checkout system there and you're going to find the last commits, the last PRs, where in Kubernetes, which cluster you have it running, um what was the last commit that was related to it, which is very cool. And the last one is more of a concept and a pattern that is proactivity. So, if the LLM can do things and it knows what's going on, it can do it by itself. So, there's not even a point to

**[6:30](https://www.youtube.com/watch?v=8EAnGIUNu_U&t=390s)** generate a UI for that. It's basically just informing the user what's going on, right? For our scenario, that wouldn't apply exactly like this. Um so, we have this auto RCA um feature where the LLM receives the alert. Yeah, they receive the alert, they list it, it investigates automatically, and the user just have to go there and understand from the from the text and the metrics and the charts what happened, how to fix it now, and how to prevent it from happening in the future. >> [snorts] >> Well, that's it.

**[7:19](https://www.youtube.com/watch?v=8EAnGIUNu_U&t=439s)** If you want to know more about Highground or me, just follow there. Thank you very much.
