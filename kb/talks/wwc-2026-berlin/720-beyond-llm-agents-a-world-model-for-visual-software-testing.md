---
id: 720
title: "Beyond LLM Agents: A World Model for Visual Software Testing"
slug: beyond-llm-agents-a-world-model-for-visual-software-testing
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Quality & Reliability"
type: "Startup Presentation"
stage: "Airstream 1"
tags: ["AI Models", "Agents", "Agentic AI", "Automation Testing", "CI/CD", "Compliance", "Cross-Platform", "Deep Learning", "E2E Testing", "HTML", "Model Training", "Neural Networks", "Playwright", "Reinforcement Learning", "RPA", "Selenium", "Testing"]
speakers: ["Manuel Weichselbaum"]
speaker_companies: ["anyconcept"]
day: 1
starts_at: 2026-07-09T12:15:00+00:00
duration_min: 5
recording_url: https://www.youtube.com/watch?v=6eYCoqtsBYs
video_id: 6eYCoqtsBYs
session_page: https://app.wearedevelopers.com/events/16/session/720
transcript: true
---

# Beyond LLM Agents: A World Model for Visual Software Testing

**Manuel Weichselbaum (CTO — anyconcept)**

`Track: Quality & Reliability` · `Type: Startup Presentation` · `Stage: Airstream 1`

`#AI Models` `#Agents` `#Agentic AI` `#Automation Testing` `#CI/CD` `#Compliance` `#Cross-Platform` `#Deep Learning` `#E2E Testing` `#HTML` `#Model Training` `#Neural Networks` `#Playwright` `#Reinforcement Learning` `#RPA` `#Selenium` `#Testing`

[Watch the recording](https://www.youtube.com/watch?v=6eYCoqtsBYs) · [Session page](https://app.wearedevelopers.com/events/16/session/720)

## Abstract

What if a model could learn software the way humans do, through pixels, mouse, and keyboard alone? This talk introduces the Vision Action Model, a foundation model that understands UI concepts, not coordinates, and executes them deterministically. Purpose-built for software testing. Trained purely on interaction data.

## Speakers

### Manuel Weichselbaum

*CTO — anyconcept*

Manuel Weichselbaum is co-founder and CTO of anyconcept, a research company building a world model for software interfaces. His background spans physics, telematics, and computer science, and he has spent over a decade doing AI research before that was the obvious thing to do. In 2020 he began exploring a question that the industry had largely ignored: what if a model could learn to understand software purely through visual interaction data, the way a human does, without ever reading a line of code. That question became the Vision Action Model, a domain-specific foundation model trained on pixels, mouse, and keyboard data alone. Manuel leads all VAM research and architecture at anyconcept. GHOSTS, the first product built on the VAM, is already running in production for enterprise customers. He is based in Graz, Austria.

## Transcript

*799 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=6eYCoqtsBYs&t=0s)** I'm Manuel from Any Concept. Um we've been building AI models um agentic AI models long before LLMs even started to become a thing. And it kind of means we kind of don't have a benchmark that applies to us. We're demonstrations automation instead of prompt automation. Let's like it Let's take a step back. Um the OS world benchmark is basically what all of our competitors are using and it seems saturated. You've got 80% human average is even 72. So, is this solved now? The real world looks a bit different and we see the goal post move now. It's not about can you do this computer task once? It's can you do it repeatedly like the same kind of task the same way? And um the metric flipped. So, what's going on? Isn't like computer use, clicking on a computer, using it something that's easily done by AI? Can't you like verify and that really well-trained AI models on this? Well,

**[0:57](https://www.youtube.com/watch?v=6eYCoqtsBYs&t=57s)** Tworkish Patel in a recent YouTube video said um it's not enough for it to mean to be verifiable. It also has to be very grindable. In a sense that you have to to run lots of parallel rollouts against a deterministic and replayable simulator. With code, that's easy. A thousand containers, you start up a thousand agents, let it attack a repo. But with computer use, you can't just or you shouldn't run a thousand agents against a real Amazon checkout webpage. And in the real world, it gets even worse. So, what's our solution to this kind of bottleneck problem that AI is facing in many domains now? We think that to act in any environment, you have to abstract behavior. So, what we built over the last years and iterated on it is our data set of abstracted UI inter- interactions. We kind of have like 30 concepts and these kind of concepts build up everything you can do. To use this, you kind of have to build

**[1:57](https://www.youtube.com/watch?v=6eYCoqtsBYs&t=117s)** this map, this concept library. That's also why we have to launch our own platform for everybody to use this. And then as soon as you have that, you can plan ahead and then step-by-step run a sub-agent to solve um anything in this abstracted space. This is not much more secure, this is not only much more secure, you're basically below passwords and prompt injection with everything. And it's also much more um cheap. We can run many hours just by using a CPU if nothing else is available. Um we call it vision action model. And we kind of follow a line of world model thinking that you should not try to um have learning targets that are very dense, like text or every single picture of an image. We on purpose keep our targets very simple. This induces a different kind of mental model in the AI that is very useful for this kind of agentic behavior. Very important for us are visual concepts and these kind of target

**[2:57](https://www.youtube.com/watch?v=6eYCoqtsBYs&t=177s)** states. Our AI has kind of checkpoints it sets itself to go step-by-step and to really figure out if it's doing everything correctly. This also means that testing for us is kind of an architectural side effect. This is why we attack visual testing first. Another thing that makes it much better for testing is that we use sigmoid not softmax activation, which kind of means if there's no good solution, well, then there's just no good solution. You're not forcing the AI to choose something like most other trainings do. So, um this also gives you like a confidence signal you can use. Especially for testing useful if you can figure out with high confidence that you found a bug or if you're causing it yourself as an agent. This is very important for the testing reports. All right, so this is kind of what we're building. Sign up for our Ghosts platform and when it goes live,

**[3:53](https://www.youtube.com/watch?v=6eYCoqtsBYs&t=233s)** find us at anyconcept.ai and um I'm Manuel Weissbaum from Any Concept. If you're curious, you can also come find us at our booth. >> Thank you very much. Um so, real quick, we have some time for questions. Uh you said that um well, my understanding is vision models are generally expensive. You said that's actually quite cheap. >> Yeah. >> Can you explain a bit? >> Even the slow smallest model of the best competitor, >> Yeah. >> we're 10 times smaller and on our trust me bro benchmark, we're at least compatible. >> Excellent. Uh that's that's really great. Uh anybody want to try this out? Yeah? Yeah? Good. I want to try out as well. That's cool. Thank you so much. Give him another round of applause. Any Concept.
