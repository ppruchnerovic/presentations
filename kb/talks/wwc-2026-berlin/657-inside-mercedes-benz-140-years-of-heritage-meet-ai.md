---
id: 657
title: "Inside Mercedes-Benz: 140 Years of Heritage meet AI"
slug: inside-mercedes-benz-140-years-of-heritage-meet-ai
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: null
type: "Keynote/Talk"
stage: "Stage 11"
tags: ["AI Standards", "Best Practices", "Developer Experience (DevEx)", "Generative AI (GenAI)", "Innovation"]
speakers: ["Daniel Geisel", "Jens Petersohn"]
speaker_companies: ["Mercedes-Benz Tech Innovation"]
day: 1
starts_at: 2026-07-09T10:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=G-1L3tKM6bM
video_id: G-1L3tKM6bM
session_page: https://app.wearedevelopers.com/events/16/session/657
transcript: true
---

# Inside Mercedes-Benz: 140 Years of Heritage meet AI

**Daniel Geisel (CEO — Mercedes-Benz Tech Innovation), Jens Petersohn (CTO — Mercedes-Benz Tech Innovation)**

`Track: —` · `Type: Keynote/Talk` · `Stage: Stage 11`

`#AI Standards` `#Best Practices` `#Developer Experience (DevEx)` `#Generative AI (GenAI)` `#Innovation`

[Watch the recording](https://www.youtube.com/watch?v=G-1L3tKM6bM) · [Session page](https://app.wearedevelopers.com/events/16/session/657)

## Abstract

How do you turn AI into real enterprise value—beyond pilots and hype?

Mercedes-Benz shares lessons from operating AI at scale: across legacy systems, compliance constraints, and complex organizations. The key insight: tools don’t make you AI-native—architecture, culture, and leadership do.

## Speakers

### Daniel Geisel

*CEO — Mercedes-Benz Tech Innovation*

Daniel Geisel is CEO of Mercedes‑Benz Tech Innovation. In this role, he is responsible for the global software organization within Mercedes‑Benz IT, driving technological development and innovation in close collaboration with the business functions.

Under his leadership, the organization is evolving from individual tech hubs into a globally integrated software tech organization, combining software engineering excellence, digital solutions and strong execution capabilities. He works closely with international teams across locations including Spain, South Africa, India and Malaysia.

### Jens Petersohn

*CTO — Mercedes-Benz Tech Innovation*

Jens is CTO of Mercedes-Benz Tech Innovation. His journey into tech began around 2006: debugging Internet Explorer 6, writing PHP that would make any modern linter weep, and genuinely believing that document.all was a reasonable API. Somehow, that did not scare him off.

He joined Mercedes-Benz as a software engineer in 2014, and by 2017 had taken on additional responsibility as Principal for Connected Vehicle Services, shaping how cars talk to the cloud and, occasionally, back. Since 2023, he serves as CTO, driving innovation, embedding AI across the product development lifecycle, and steering a 7,500-person engineering organization at the heart of Mercedes-Benz's global software ecosystem.

He still has opinions about JavaScript. They've just gotten harder to revert.

## Transcript

*3,052 words · source: yt (en)*

**[0:18](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=18s)** Hello everyone, welcome back. Um, in our next session, we will hear about turning AI into real enterprise value. uh inside Mercedes-Benz 140 years of heritage uh meeting AI and uh our speakers will be Danielle Gazel and Yans Peterson. Welcome [applause] >> [applause]

**[1:06](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=66s)** >> Welcome. We are developers. It's great to have you here at the stage 11 to our talk about inside Mercedes-Benz and how we will bring AI into our 140 years of heritage. When you look at Mercedes, there are three dimensions where we apply AI already today. You find AI in our products. You will find AI in our software engineering processes. And every employee in Mercedes spends over 107,000 70,000 uh colleagues around the world are already using AI in their daily work. And this is uh where we are at as Mercedes-Benz as of now. Today Yens and myself we want to focus at the middle part and that's what we are

**[1:53](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=113s)** developers is all about. It's about developers software engineers and we want to dig deeper what AI really means for us in operating it. Last year Marknos and Katherine talked about the product side they talked about the knowledge worker side and today it's all about software engineering and the details around of that when we dig a bit deeper. So who we are? My name is Daniel as introduced I'm responsible for the techups in recep and together with Yens my CTO. We will dig deeper as I said in the different dimensions of operating AI. What is uh my responsibility our responsibility all about? In Mercedes-Benz we invested couple of years ago already in building out uh building up inhouse captive

**[2:41](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=161s)** knowledge for software engineering. So we have tech experts around the globe. You see the locations on the slide. And we are forming a captive tech environment within Mercedes-Benz. We provide software across the whole life cycle from the first draw of a car when it starts at the designing phase when it comes to engineering to the incar software development part when it comes to the production to sales after sales and financial services. That means the software we build it runs across the globe in every production plant in over um in all of uh our 240 locations worldwide and this combined with our heritage you could imagine it's kind of a complex

**[3:29](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=209s)** environment and uh what we have to find it as an in-house software tech unit is a bit of the management core belief AI will solve all your problems terms, don't forget about it. Just apply AI and everything will go away. But you could imagine over the last decades, we have lots of different ownerships. We have a legacy environment. We have mainframe still running in Mercedes-Bench which are older than me and Yens. Um and um when we also look at the technical depth, it's quite huge. So maybe we start with a short question. How many observability text and tools do you believe we are using in Mercedes-Benz as of now? I give you three choices. Hands up when you think

**[4:17](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=257s)** you hit the right one. So, who believes in Mercedes we are using 10 observability text tools uh across? Hands up for 10. Okay. So, my introduction Oh, at least one core belief really good. Who believes we are using around 25 tools 50 100. Okay, we are not that bad. So [laughter] um in Mercedes-Benz we have across roughly 50 different observability tools. Our developer ecosystem incorporates more than 140 different tools, tech stacks and that is the heritage uh which we are currently heavily fighting against. Uh the IT landscape more than 7,000 different

**[5:07](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=307s)** applications as I said mainframe SAP brings up quite uh big complexity in and this is which we are in and it's not just of uh it's not just about how we apply AI. The question is how do we operate AI as Mercedes-Benz at a broader scale? Therefore, we brought you our five engineering bets and our core belief and this is what the whole speech and talk is all about and I'm handing over to Yans. >> Thanks Danielle and uh welcome everyone from my side. Um these five engineering bets we have we are heavily heavily focusing on especially this year and last year and we'll see whether we need additional ones but um the ones we brought with us today actually brought

**[5:54](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=354s)** us on good speed um in order to um move forward applying AI with our heritage. And the first one is about that we have a a very strong base with coding tools and coding harnesses um for coding, for testing, for releasing, for reviewing. But actually there is more to it. It's not just the simple product development we are facing. It's also about the the full product development life cycle. So we need to take into account people working in uh design thinking in idea creation um also the roll out in the end and and the whole product sundown also is a is a big thing on our end as you heard mainframe migrations we have a lot of legacy migrations um that we move

**[6:44](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=404s)** from a legacy stack into the cloud. So we actually have to take a close look not what is hype at the market but what fits to us and what is a pressuring pain also for us and this goes way further than just um looking into plain software development. This also leads us to not only focusing on engineers, plane engineers or or shredding code um but brings us to our second bet which is that we have the core belief and the bet that every role independent of um the profession has an agentic harness. So yes, there are good harnesses out there that we can leverage, but the agentic harnesses are there also for people that are supporting the product development. So

**[7:33](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=453s)** we are looking into harnesses for project managers, for um agile coaches and so on and so forth that we have actually a decent support and a decent coverage and um this is something that um some of our folks adopted quite early to be honest. Um so especially the UX guys um started back in end of 24 applying and developing skills and agents um over the past um roughly one one and a half years that can be used for user research for um UI design and it's built on top of copilot and as you can see these are our major let's say coding agents that we currently have in place at Mercedes um which is GitHub copilot where we have a strong base, a

**[8:22](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=502s)** strong ecosystem which um which we have in the company spread widely. Um and this adoption grew over the past years quite steadily and beginning of this year we introduced um also for for other um roles especially um um Devon and also Claude there was the necessity out of the engineering community to provide something else than GitHub copilot for some of the roles but also the the the need um um to extend our ecosystem offering in general. Speaking about the ecosystem, it is way more complex than simply putting out tools there. So um what we discovered um across our journey of the past two to three years is that if you

**[9:12](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=552s)** want to scale impact within your organization when it comes to software development and if you have such a diverse organization culturally culturally technically uh and also process-wise um the tools are just one part of the equation. We have a very strong AI ecosystem that provides central models to everyone that can be consumed centrally. We provide central agents. We provide central skills to have a certain governance layer uh in our agents and to build individual journey or text tech dependent agents on top. And um where we invested quite heavily is the evaluation of exactly the the coding tools um that we rolled out. We wanted to make sure

**[10:01](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=601s)** that we have the tools that fit our way of working that fit a text which is close to the vehicle or inside the vehicle but also a tech that helps us build mobile apps, web front ends, SAP um and and for example X XR. And it's not that easy to just pick offtheshelf stuff. This is why the whole topic of the ecosystem closely governing what goes in there closely monitoring how it's used apply new standards roll out new standards test new standards this is why this third horizon that you guys can see is super important to us to get in the MB specifics that help us to actually scale AI. One thing that was a feedback from our developer community without AI is that

**[10:50](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=650s)** compliance to be compliant in our world in our um in our organization and in our texts um is a super painful process. You have to know a lot of manual guidelines and I think um it's it's quite commonly known that we are good in guidelines, processes and and regulations. Um, but the closer you move to the vehicle, the regulations get tighter. H, and we have to make sure that those regulations that we have are baked in to that ecosystem. So, we make sure that continuous compliance is something especially now with AI because there is a lot of uh a lot of um um ecosystem drift otherwise um we have to make sure that continuous compliance is built in by default. This

**[11:37](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=697s)** is why our experts are hardly governing um this ecosystem to make sure that compliance is built in. We have agents running in CI/CD pipelines that do static code analysis, dynamic application testing to make sure that if we deploy a backend that we can do a quick ad hoc pen test of a new feature for example. And last but not least, if we look at governance and governing AI access to a certain degree, um, we have a a central, we call it nexus, we have a central product that is our gateway, our LLM gateway for everything we build, for every use case you already saw in the beginning. So the products are using that gateway, the developers are using that gateway um in order to have a

**[12:27](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=747s)** central way of releasing models, having a certain model clearance process and providing the latest frontier models but also open- source models. this gateway heavily pays into um also our fifth bet and um I think it's it's common knowledge also uh also in this round um that first when we started to push the AI adoption we told everyone use AI as much as possible go for token spend then there was I don't know some of you folks does anyone know Strad Strad anyone str audi So it's like Straa but for cloud code and they had a a ranking how many tokens um you have you're burning basically and

**[13:16](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=796s)** um I think the the the world record or the currently the the person on first place has something like half a million tokens so half a million dollars worth in tokens spent on one person only. So it's the the whole dynamics of what is actually important um when it comes to token spend to AI usage um is shifting from use it as much use it as much as you can going back to ah don't use it that much um and we settle for something that we say it's our duty to identify the business value or to give our teams context to determine their business value there is no oneizefits all a business value in cloud in cloud environments is way more easy um to point out than it is for example in a very regulated ECU or incar environment.

**[14:05](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=845s)** So what we provide to the organization is that um we have on an individual level we can show developers what are you currently consuming across the different tools be it claude be it Devon or be it uh GitHub copilot um because as you as you have saw as you have seen the numbers that we had up there um were quite so there were more than 5,000 people than that is covering our organization um and people are jumping from tool to tool and We experienced that people are simply if they have certain quotota issues with one or the other tool, they just jump back and forth and just use the next tool. So what we wanted to provide and make a certain yeah reasonable insight for for our developers and their respective organizations, teams and and um units is

**[14:54](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=894s)** that they have a transparency on what are they spending on an individual basis. So they can actually start calculating their business value that they get out of that. We um coach our teams when it comes to token optimization. So the harness um that I showed you guys earlier, we have certain skills in place. Many of you maybe know um caveman as a skill or ponytail or whatever which reduces the bloatiness of the of the LLM but also the generated code. So we provide that to our teams um ecosystemwise but also coaching wise giving them uh the best fit uh and the best coaching for the tools they have in place. And last but not least it's our duty to also see and also um challenge

**[15:44](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=944s)** ourselves constantly what's the best average token cost for us. So um I don't know a lot of people just went with let's go with the default Opus 4.8 for quite some time. Um but if you throw one of the other force models which are very capable as of now uh into the mix the average token cost drastically decreases which also helps certain business units um to have a decent mix when it comes to um what is actually my my token spend and what is my business value I get out of it. Having said that, all of these five bets as you or as I pointed out from time to time um do not work if we do not enable the people properly. Uh and this is where we're looking into our core principle

**[16:32](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=992s)** which I would hand back over to you. So the core belief I think it's obvious um it's not uh it's only working uh with capable people in our organization and therefore we said we need to analyze what's the need of our organization what's the need of our people um we need to coach them on different levels and we need to scale the expertise uh with different formats and when you look at the analyze phase um it's pretty simple we had big employee service surveys pulse surveys and so on. Um, but we never had a developer survey. Last year we started the first developer survey in Mercedes-Benz and over 3,000 engineers gave us quite some good feedback, drastic feedback, clear feedback where

**[17:20](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=1040s)** we had to act on. One of the feedback was the little game which we played earlier about observability. Another feedback was by the engineering team. It takes us on average more than 20 days as a cloud native team to set the whole environment up to get uh the whole coding work start. So it takes them 20 days before they can do actual work and this is something um which we take up quite serious as our organization is also forming um since um since 12 12 um 18 months quite new. So we are heavily using now that feedback in driving and optimizing that. So we need to come down from days to hours. That's a clear ambition and we already have a huge progress there. On the coaching side,

**[18:10](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=1090s)** it's not just coaching our developers on an individual level, on a team level or on an organizational level. As I said earlier, um we have also um a training and a coaching need towards the management uh at a broader scale within Mercedes. You could imagine 5,000 developers hitting 170,000 people at different stages knowing less or limited about AI. So it's also a training exercise for the whole company. So it's not just the coding part as Yens described, it's also about the product owners, the the business process owners, the whole roles when it comes to a product life cycle. And last but not least, when it's about scaling, um we have communities set up for the different areas we applying uh

**[18:59](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=1139s)** with gamification. um a nice belt system so you could uh build up your belts to get uh even higher in the ranking when it comes to AI and that's a huge progress. Um we have already over 6,000 belts in MB uh being distributed. It's being rolled out uh even more uh over the time. So that all summing up the five engineering bets our core belief. Um let me uh finish uh our talk maybe with that uh with with a statement. Whatever we do in Mercedes-Benz building software there's a high probability that the software will run for decades either on a production plant in a car at a dealership in a sales organization wherever worldwide. So the software we

**[19:48](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=1188s)** built might stay for quite some time. We are clear that AI won't solve the won't solve the software problems we have. It will exposes them. The weak architecture we've seen over decades will even be more accelerated. The unclear ownership which we have in our company is now something which we heavily address because unclearership is super cost intense. And that means when you look at it, the key question is not how you personally adopt uh AI. It's more about how your engineering foundation embeds AI fully so to that you are able to apply to the whole company. Thanks a lot for listening. Thanks. [applause] [applause]

**[20:42](https://www.youtube.com/watch?v=G-1L3tKM6bM&t=1242s)** Thank you so much guys. Enjoy. We are developers and if you see us wandering around, have any questions, feel free to hit us up. >> Have a nice day. Bye-bye. [applause]
