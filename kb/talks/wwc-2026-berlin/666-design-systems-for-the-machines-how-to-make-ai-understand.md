---
id: 666
title: "Design Systems for the Machines - How to Make AI Understand Your UI"
slug: design-systems-for-the-machines-how-to-make-ai-understand
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Keynote/Talk"
stage: "Stage 11"
tags: ["Accessibility", "AI Models", "Automation", "Design Systems", "Large Language Models (LLMs)", "Productivity"]
speakers: ["Jennifer Wjertzoch"]
speaker_companies: ["DKB Code Factory"]
day: 1
starts_at: 2026-07-09T08:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=S2Z6jwexHgc
video_id: S2Z6jwexHgc
session_page: https://app.wearedevelopers.com/events/16/session/666
transcript: true
---

# Design Systems for the Machines - How to Make AI Understand Your UI

**Jennifer Wjertzoch (Senior Frontend Engineer — DKB Code Factory)**

`Track: Frontend, Web & Mobile` · `Type: Keynote/Talk` · `Stage: Stage 11`

`#Accessibility` `#AI Models` `#Automation` `#Design Systems` `#Large Language Models (LLMs)` `#Productivity`

[Watch the recording](https://www.youtube.com/watch?v=S2Z6jwexHgc) · [Session page](https://app.wearedevelopers.com/events/16/session/666)

## Abstract

Design systems were created to make interfaces predictable for humans, now we need to make them predictable for machines.
In a world where AI agents analyse, navigate and document our UIs, a component is only as useful as it is machine-readable.

This talk shows how to embed semantic metadata, accessibility signals and structural intent directly into your design-system components, so AI can correctly interpret their purpose, behaviour and constraints.

Jennifer demonstrates how machine-readable components unlock automatic documentation, AI-assisted accessibility reviews, intelligent refactoring and design-to-code pipelines that actually understand your product.

The session delivers a forward-looking, practical blueprint for design systems that aren't just beautiful and consistent, but self-descriptive, inspectable and fully compatible with the AI-driven workflows of the future.

## Speakers

### Jennifer Wjertzoch

*Senior Frontend Engineer — DKB Code Factory*

Jennifer Wjertzoch is a Senior Frontend Engineer at DKB Code Factory GmbH, where she builds scalable and accessible web systems in the financial domain.
She specializes in accessibility architecture and believes that inclusion is not an add-on but a fundamental principle of software quality and risk management.
Her work focuses on integrating accessibility into system design, developer workflows, and CI/CD processes to create products that are resilient, compliant, and user-centered.

## Transcript

*2,773 words · source: yt (en)*

**[0:02](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=2s)** Yeah, hello everyone. My name is Jennifer. I'm a senior front-end engineer at DKB Code Factory, Deutsche Kreditbank here in Berlin. Oh, wait a second. Yeah. So, a quick full disclosure before we start. I'm deeply, stubbornly analog. So, outside of work, I shoot 8-mm film. Yes, real film. You have to develop it. You cannot delete anything, and each frame costs a lot of money. I do pottery, and I also create things out of marble. So, now you're probably wondering, why is someone like this standing here talking about AI agents? And I totally

**[0:51](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=51s)** get it, honestly. But, here's the thing. The more analog your hobbies, the higher your standards for digital interfaces. You simply know what real craft has to feel like. And this talk is about craft, the craft of building interfaces that do not just look good, but actually communicate to humans and now, increasingly, also to machines. So, let me tell you about a button I built. It was a beautiful one, perfect proportion, right contrast, and the hover state felt like butter. But then, an AI agent arrived and simply ignored it.

**[1:39](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=99s)** Not because it couldn't see it. It could actually see its pixels. It could see the DOM parts of the accessibility tree. But, seeing something and understanding it is something totally different. And for the first time I asked myself who were we actually building interfaces for? For humans, exclusively. So we have spent over 30 years to optimize our interfaces so they work for humans. So they are intuitive, they are predictable, and they are consistent. Design systems were born out of that desire to make our interfaces predictable for humans.

**[2:31](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=151s)** But the world is changing and our interfaces are no longer consumed only by humans and maybe assistive technologies. AI agents start to interact with them as well. And they rely on signals like structure, semantics, labels, and most of all, intent. And to be honest, many of these in our interfaces are surprisingly hard for them to understand. So the future of design systems is not visual consistency. It's reducing ambiguity for humans and machines alike. That's the thesis for today.

**[3:18](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=198s)** And some of the practices I will show you are already available to us right now. Some of them are emerging, but all together they point towards a future where our interfaces are understandable to humans and machines alike. So I want to briefly take you into the world of an AI agent. Not as a metaphor, but quite concretely. So what happens when an say cloud with computer use, enters a web application? Right. First of all, it has to make sense of it. So as I said, some of the agents primarily see um screenshots. They see

**[4:07](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=247s)** pixels. Um what one rectangle after another. Some of them have access to the DOM or also the accessibility tree. But regardless of the implementation, they still face the same challenge. They need to understand what really matters. So imagine you're looking at this blue rectangle with white text inside. Is it a button? Is it a banner? Or is it just decoration? A human would instantly know this is a primary action. But an agent has to infer that from whatever signals we provide them. And that is surprisingly difficult.

**[4:57](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=297s)** So if we zoom out of this, the problem comes down to three things. The first one is missing meaning. So machines don't automatically understand what an element is. A div can look like a button, but semantically it doesn't mean anything. That's uh called Moravec's paradox in UI. So a human instantly what a human instantly recognizes, machines often have to guess that from pixels. Second is missing behavior. Machines don't know why an action matters. Even if a machine recognizes a button,

**[5:45](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=345s)** it still doesn't automatically know about its state or the behavior. So, is it disabled? Is it loading? Is it submitting a form or is it opening um a menu, for example? So, knowing something is not this not knowing what something is and um knowing how it behaves are two very different problems we have to tackle here. And the third one is missing intent. Machines don't know which action is the important one. So, now imagine a page with 10 different buttons. So, a human instantly knows which one matters, which one moves the user forward, which one completes a checkout,

**[6:35](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=395s)** and which one is maybe just second navigation. A machine usually has to infer that intent, and that's exactly where the things get very interesting for us. A study showed modern agents never scroll more than two viewports. They ignore purely visual CTAs and respond far more reliably when semantic information is available alongside visual elements. Think about that. So, we keep talking about better models all the time, but this study points somewhere else. Right, the problem is in our interfaces. And that is great news because

**[7:24](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=444s)** interfaces, that's our job. So, we don't have to wait for a better models and shiny better models, we just can fix this right now. So, remember the three problems I talked about: missing meaning, missing behavior, and missing intent. It turns out we have layers to solve each of them. The first one is semantic HTML. That solves the first problem, missing meaning. So look at both examples. Both examples look the same in the UI. They are buttons. A human doesn't care what the code looks like. A machine does.

**[8:12](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=492s)** So on the left side it sees a div. And on the right side it sees a proper semantic button. Same UI, completely different signals. And that's the whole point of semantic HTML. It answers the first question, what am I? A button. So semantic HTML gives the machine the basic identity. This is a button. And then comes area signals. Area adds now the information around this. A name, a description, gives information about the state. So the machine does not only see the element now, it also understands more of

**[9:02](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=542s)** the whole situation. For example, area label answers how should I call this thing? Area described by what else should I know before I interact with it? And area busy answers should I wait or not? The important part is none of this changes the visual interface. So for a human the button still looks exactly the same. But for the machine the signal now got much much richer. All right, so far we have answered two questions. Semantic HTML helps the machine to understand what is this?

**[9:50](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=590s)** And aria helps the machine to understand what is actually happening right now. But the third question is harder. Why does this matter? So, this is something we usually don't put into our interfaces. We put it into our design reviews. We put it also into our product decisions. We put it in the documentation. We have it in our heads, but machines don't cannot read our heads. So, structural metadata is one possible way to make that intent visible. Not visually visible, but machine readable visible. I have three examples. So, for example,

**[10:38](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=638s)** data component answers what am I in the system? A button? We had that. Data intent, why do I exist? Submit bank transfer. Data context, where do I belong? You belong to the bank transfer. So, the user still sees a button, but the machine gets one more signal. This is not just any button. This is the action that completes the transfer. And to be clear, this is not yet a standard, but the idea is simple. So, if intent already exists in our design systems, then we should not hide that from the machines.

**[11:30](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=690s)** Okay, let's make this concrete. Um, I I switch to code for a few minutes and show a simple button component. Um, important to know is it's just a control it's it's a very controlled demo, so simplified on purpose. I'm not trying to show any full AI autonomy, but what I want to show is what changes when the interface gives clearer signals. Um, before I explain I explain a little bit. So, technically this demo I will show you compares two versions. It's the baseline UI and agent-ready UI. It's the same interface. We have um, yeah, same interface and the task is exactly the same on both runs. Sending a

**[12:18](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=738s)** transfer with the same form fields and the same action. And the automation is the same, too. I'm using a reproducible um, Playwright script that runs the same flow against both variants. So, the only thing that changes is how well the interface communicates what's going on. So, semantics, labels, um, also machine-readable intent and context metadata. So, yeah, same task, same automation, different interface signals, and um, but very different reliability. You will see that. Okay, let's run this. And we can already see we get critical

**[13:13](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=793s)** issues. And now I want you to think about these issues not just as accessibility issues, they are actually signal gaps. And when signal signal signals are missing, then agents have to guess. And when agents start guessing, reliability goes down. So, let's improve this. So, my first step was semantic HTML. So, in the agent ready UI, I replaced the generic element with a real button. Visually, nothing would change, but the machine gets now um a uh for for the machine, it's actually a lot of changes because um the interface gets much clearer now.

**[14:02](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=842s)** It says this is interactive. This can be reached by keyboard. And that's actually a real action. And I think that's already a big improvement for a very small change. The next step was um aria. So, now the button has a clear name and a better state communication and also more workflow context. So, for humans again, UI doesn't change at all, but for the machine, the signal quality is much better now. So, now we run the scan again on the agent ready UI. So, then we can already see

**[14:58](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=898s)** that brings us down to zero critical errors errors and that doesn't mean the component is perfect forever, but it means we have a much stronger baseline now for reliable behavior. I want to add one more layer and this is the component manifest. So far we have improved the interface um at runtime. But the manifest adds um a contract at component level. So, the DOM tells us what is this button right now, and the manifest tells us what can this button component do in general. So, for example, what state does it support, what variants exist, what

**[15:47](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=947s)** behavior is expected, where are the limits, where do we need extra care, for example. And this is useful for documentation, this is useful for testing also, for CI, and also for our future agents workflows. It's not a finished standard, but it's a very practical directional, I think, to to to go to. Okay. So, we we just saw the agent succeed because the interface gave better signals. But this is not the only that's it's not only about helping an agent to click the right button. This is about verification. So, the next bottleneck is not only how

**[16:36](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=996s)** smart the model is, it is whether the interface gives the agent enough structure to make its action understandable, make it also testable, and verifiable. And that starts in our UI. So, the next question is, what do machine-readable interfaces actually unlock? And for me, there are four very practical areas. The first one is AI accessibility reviews. So, accessibility reviews often happen or happened as a manual spot check. So, someone looks at a screen, runs a tool, and then writes some findings, and then

**[17:25](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=1045s)** the team fixes them later in the in the process. But if your component already exposes meaning, behavior, and also its intent, then the reviews can become much more continuous. Not perfect and and also not replacement for an accessibility expert, but a much stronger safety net. Because instead of finding issues at the end of the of the process, teams can get feedback much earlier now. Second is safe refactoring. And this one is really important. So, most refactoring tools understand code structure.

**[18:12](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=1092s)** Uh they understand syntax. But they often don't understand intent. And that's where mistakes happen. So, if a tool knows that this is a button, this is a primary action in a payment flow, it can make much safer decisions. So, the refactoring also becomes less risky because tools understand now the intent of our application and not just the code. The third one is design to code. So, a lot of design to code tools are good at copying appearance. They can see color, they see the spacings, typography, they see the layout, but they often miss meaning. And that's why we get this famous diff

**[19:01](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=1141s)** soup. So, something may look like a button, but the generated code does not behave like a real button. And our machine-readable interfaces would definitely change that. They help agents generate code with meaning and not just styling. And fourth, self-describing components. So, this I think is the foundation underneath all of this. So, the component becomes the source of true truth. Not a separate documentation that is then outdated after two or three weeks already and nobody cares about this anymore. But the component itself describes what it is and what state it states it

**[19:51](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=1191s)** supports, how it behaves, and also where it should be used. And that means docs, tests, and also tools and agents, they can all work from that same source, this one single source of truth. To wrap this up, um the pattern behind all four examples is the same. We want less guessing, more understanding, we want less ambiguity, and more reliable automation. Yeah, and that's what machine readable interfaces are about. Not replacing any developers, but reducing the ambiguity. All right.

**[20:38](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=1238s)** Before I finish, I also want to give you a a concrete blueprint for maybe the first quarter. Four steps you can start immediately with. Let's start with step one. The audit. So, a simple thing, just install XCore and run it through your design system. Or even better, you can also um open one of your core pages with an AI agent and then simply watch watch it try to complete one task. And then watch where does it hesitate? Where is it guessing and where is it maybe also failing? And I guarantee within 5 minutes you will see things you that were invisible

**[21:27](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=1287s)** to you before. So the second one is introduce team conventions. Write an ADR that establishes uh interactive elements must use uh semantic HTML. Every interactive component must expose an accessible name. Area states are required when behavior changes. And then div and span are definitely not not button alternatives. Enforce that also in ESLint. And then you maybe pilot one component manifest. Not as extra work, not as a burden, but as a see it as a contract, as a standard that

**[22:15](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=1335s)** reduces the ambiguity. Step three, CI/CD integration. So build a GitHub action step that checks every PR. Does the XCode scan pass without critical errors? If not, block the merge. It sounds tough, I know, I know, and it's really difficult, but in 6 months you will see. And then step four, establish agent testing. So do you already test with screen readers? Anybody? Yeah? Great. So now you test with AI agents, too. Just treat the agent like a new user

**[23:03](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=1383s)** type with specific requirements, right? Write a use case like agent should be able to navigate to the payment method in the transfer flow. And then test whether it can. If not, debug just as you do with the screen reader. All right. Um yeah, as I said in the beginning um for 20 years we've been building design systems, so interfaces are predictable for humans. The next challenge is simple. Can we also make the interfaces predictable for machines? And that's not because AI deserves a special treatment, but because more and more of our users interact with our interfaces through AI.

**[23:53](https://www.youtube.com/watch?v=S2Z6jwexHgc&t=1433s)** And maybe that's also why it feels so familiar to me, because when I work in marble, there's no undo button. Every cut matters, and every mistake becomes part of the final piece. And machine-readable interfaces are similar. So, agents make decisions based on the signals we provide them. So, let's make sure the stone has no cracks. Thank you. >> [applause] >> Woo!
