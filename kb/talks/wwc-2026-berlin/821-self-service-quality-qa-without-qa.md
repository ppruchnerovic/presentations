---
id: 821
title: "Self-service Quality: QA Without QA"
slug: self-service-quality-qa-without-qa
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Quality & Reliability"
type: "Keynote/Talk"
stage: "Stage 1"
tags: ["AI Models", "Quality Assurance (QA)", "Testing"]
speakers: ["Ondřej Gróf"]
speaker_companies: ["Canva"]
day: 2
starts_at: 2026-07-10T07:00:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=4l-PnH0UUrY
video_id: 4l-PnH0UUrY
session_page: https://app.wearedevelopers.com/events/16/session/821
transcript: true
---

# Self-service Quality: QA Without QA

**Ondřej Gróf (Senior QA Engineer — Canva)**

`Track: Quality & Reliability` · `Type: Keynote/Talk` · `Stage: Stage 1`

`#AI Models` `#Quality Assurance (QA)` `#Testing`

[Watch the recording](https://www.youtube.com/watch?v=4l-PnH0UUrY) · [Session page](https://app.wearedevelopers.com/events/16/session/821)

## Abstract

As of tomorrow, teams will not need QA engineers.

Sounds crazy? That is precisely what we are building at Canva.

AI changed the game overnight. Development teams were shipping faster than ever, and QA needed to adapt. We flipped the script. Instead of teams waiting for us, we empowered them to completely own quality through our self-service approach.

To achieve this, we built AI tools that support key parts of the QA process: test plans, test generation, a test parties assistant, and more. Teams gained what they needed without the wait, while quality signals and indicators ensure they remain relentless about quality standards.

But what about QAs? They no longer test. We shifted our focus to exploring new frontiers and enabling quality across the organization, thereby significantly increasing the impact of our work given the rapid pace of change.

I will walk you through our transformation journey: the practical tooling approaches we adopted, how we adapted our QA processes to facilitate this change, the key breakthrough moments that made it work, and why this shift is critical now.

## Speakers

### Ondřej Gróf

*Senior QA Engineer — Canva*

Ondřej is a Senior QA Engineer at Canva who has spent 9 years in testing, always with an eye toward what's next. He has a knack for finding innovative approaches that others might consider 'out of the box' for QA, specializing in visual testing, quality measurement, and AI applications in quality.

## Transcript

*3,151 words · source: yt (en)*

**[0:02](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=2s)** We are going to kick off today with Andre who is a senior QA engineer at Canva and he is going to talk about how Canva didn't replace Q&A with AI but how they enhanced Q&A with AI. So Andre stage is yours. >> Thank you. >> Hello. Good morning Berlin. It's fantastic to be here. It's like 9:00 first sessions of the last day and you chose to talk about QA. So we are already mind kind of kind of people. I'm fairly sure that uh just overnight while we were all asleep something new was shift in AI and maybe in AI for QA2 and that's not a joke because in last few months QA has made tremendous progress and it keeps evolving at very fast pace

**[0:50](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=50s)** which means for us as a QAS that staying active learning and adapting is not optional anymore it's the job and today I would like to share with you how we at Canva embrace this learning and adapting. But before we start, uh let me set the context. This talk it's not about or this talk is about AI in QA. It's not about AI in testing and that's and I'm the person who distinguish between these two terms on purpose and this distinguish matters because when we talk about AI transforming QA we are not talking just about uh self-healing uh autonomous testing smartest execution. We are talking about how AI enhancing

**[1:39](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=99s)** thinking, strategy, decision making, planning and other QA activities and with this foundation let me set uh the strong and bold statement. As of tomorrow, teams will not need QA engineers. It's a fact or fiction for us. It's a fact. That's precisely what we are trying or we are bu we are building at Canva. And by the end of this talk, I hope that you will not that you will see not just how we did it but also why this why this shift might be inevitable for all of us. But it's said it's 9:00 so it's time to do some quick exercise. So just let things think about self service. Raise your hand you have

**[2:28](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=148s)** ever used selfchecking at hotel or before your flight. Oh, nice. It seems to be pretty common here. The second one, raise your hands. You have ever use selfch checkart or scan and go at supermarket also. I like this one. And the last one, have you ever thought about self-serviceing QA except where you reading this abstract? No. Oh, I see a few hands. That's great. And that's exactly where we were more than more than a year ago. And yeah, that question about can go it wasn't random because if you look closely, you can find there the real inspiration quirk UA hiding in it. And inspiration like this is all around us. You basically have to look. So let's

**[3:16](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=196s)** take a scan and go as our first not first but like our f our inspiration and think about old check out everyone blame the queue but the queue wasn't the problem the queue was the symptom the real problem was cashure one person scanning one item at a time for one customer at a time and everyone else just waits fortunately somebody smart removed that bottleneck but not by hiring by hiring more cashiers, but by sharing the responsibility. They handed the scanner to the customer. The work shift left to the person closest to it. And the cashier didn't disappear. Their role just evolved into helping, supervising, and handling things uh that

**[4:06](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=246s)** needs a human. And remember that shape finding the bottleneck share the responsibility and evolve the role because that's the exact story of QA at Canva. Uh quick words on who is saying all this. I'm Andre Gra, senior Q engineer at Canva and as a slide said uh I'm the man who never dream about being QA. Uh to be honest, I believe that almost nobody does and uh none of us grew up uh with wanting this job. We just basically fell into it. I did too 10 years ago totally by accident and now I can say it was the best career decision I've ever ever made. Uh for those not familiar, Canva is a

**[4:56](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=296s)** global online visual communication platform on the mission empower the world. uh to design and today uh there is more than 260 million uh people around the world using our platform every month and our community has generated over 30 billions of designs to date which is staggering. So yes we do software at scale. Now next questions. Let me ask you something concrete. In your team or your current project, what is your defa ratio? Don't say it aloud. Just picture it and put a number on it. Got your number? Great. Uh hold on it because I have two others. The first one

**[5:48](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=348s)** 3 to one free developers to one and one engineer based on some uh resources. This is the industry standard. The number could moves around. It depends if it's regulated industry or not. It should be less or more. But 3 to one, one QA should be able to handle all testing activities for free developers. In other words, the queue stays short. The second time it's quite different. It's 2 to1 like 22 developers to one QA engineers. And that's our ratio at Canva. uh what I said on previous slide like 3 to one QA stays short 2021 it's like a real problem like a real bottleneck

**[6:35](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=395s)** because if we can you can imagine like a queue out of door around the block and that's insane but maybe there is something else and yes there is but what is something else it comes down to the difference between two words. At many companies, uh, QA means quality assurance, dedicated team or dedicated person that checks for bugs at the end, like a gatekeeper, like a gate before release, like the casher at the end of the queue. At Canva, QA stands for quality assistance. Same initials, QA, but totally different philosophy. Quality isn't one team's job. It's owned

**[7:26](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=446s)** by everyone. Engineering team, product managers, product designers, data analytics and QAS together instead of standing at the end. QA and the quality is embedded from the day one from the planning and QAS are not gatekeepers QAS are enab [clears throat] teams owns the quality and team activities the team run and the model and uh the model that it holds it together

**[8:13](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=493s)** and now you can see the model the model has four key pillars the first one's shared ownership like as I said quality is everyone responsibility always no excuse everyone cares about their or part because the quality has multiple uh perspectives embedded practices we build uh quality into every development stage shift left, shift right from the planning uh building but also to the monitoring the coaching uh coaching culture the most important thing that we empower team to test instead of testing for them. We are basically trying to learn them how to think as a QA to be able do the QA work by themselves and the

**[9:01](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=541s)** continuous feedback who measure who uh who measured and drives. So yeah the automation data driven is really important because you can make uh decisions. This is what of the quality. And now let's move to the activities. We have more than these four. I just want to highlight these four. The first one QA kickoff. That's something what we do at the beginning of the project. It's the meeting of the thing or the activity when the team comes together and just discuss uh risk test ideas. We clarify the feature scope so everyone is aware what is going on and everyone can think about it during the development. The next thing it's QA demo. It's

**[9:51](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=591s)** something that QA and dev goes together and do some testing before we move to the next stage. It's also really good because me as a QA I can learn the code and the development develop uh developer can learn how to test the test party. Yeah, it's party. That's really fancy name. Uh, there is a food, there could be a music, but definitely there is no alcohol and dancing. Instead of dancing, there is a testing. It's still fun. And yeah, basically the whole team tested together the feature and again during this activity the whole team learn more about the QA and there are everyone developers, product managers but also customer support anyone who was not involved in the feature at the beginning

**[10:38](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=638s)** because you want to get some insights from the people outside. And last one but not least but back end quality triage. So the reviewing, prioritization, basically classic bug triage, but also the quality triage because you want to uh be on the top what matters because not only fixing uh bugs improves the quality itself and uh yeah this is the key uh further everything what will follow this this model these activities they are constant They didn't change with the AI and they won't only thing what changes is who does them and how. At the beginning it was the QA then it

**[11:30](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=690s)** was the team supported by QA and now it's a team by supported AI. When AI entered the picture, one thing happened immediately. We got faster, much faster. For the most people, it's a great news for from the QA perspective. Uh it's a warning because there is one thing we refuse to become again the bottleneck. And AI didn't land in one place. It hit you at once. Our processes and our product. in our processes helping us to plan, build, test, triage, whatever. And our products car had been delivering uh

**[12:20](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=740s)** AI products for some times. But suddenly AI [snorts] were everywhere, much more sophisticated and we shipping faster than ever. All both were enormous opportunities but also both bro brand new challenges and threats. On the process side, AI could speed us up but only if we directed it. For example, like assistance, agents, skills, prompts. On the product side, we suddenly had to test things Q had never tested before. features that they are not deterministic can hallucinate can be biased and every single time you run them they provide you a different output.

**[13:08](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=788s)** So the team owning the quality, yeah, that never the worry. We already built it. Uh the worry was keeping up, more to test, risky things to test and the company moving faster than ever. And Guay had a choice to make about what it does next. So we came up with the mission helping Canva move faster with confidence and every words in it matters because speed or be being fast it's easy. It's easy to do but without confidence it's recklessness. Confidence without fast it's old way. Bottlenecks gates sign off. The most

**[13:59](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=839s)** difficult part but the most valuable one is to be able to deliver both at once. Uh shipping fast and trusting what you ship. And notice that the mission doesn't say QA assure quality. QA test everything. It says QA helps Canva uh the whole company uh move. So we are not the gatekeepers, we are enablers. And that singory frame changed everything about how UA spends the time. And now let's move to the things what I call

**[14:46](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=886s)** uh infinitive QA evolution or that's my name. I believe that you can create the better one but it's infinite because it never stops and every turn evolves the role itself. There are key four steps. Innovate. take a process, tools, piece of manual work and make it better or automate. Then the second stage is enable hand it to the team so it becames theirs and that's the key. The next one reclaim the repetitive work leaves our plate as a QAS and times come back and the next one eleate

**[15:36](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=936s)** spended time on bigger more impactful challenge which becames the next thing we innovate on and the round it goes and it it was fine but [snorts] what was what was changed by AI I AI has supercharged this loop. The lab that used to take weeks or months now we are able to run in fraction of time. We are achieving things we couldn't imagine or we couldn't dream about year ago. There is and there is the catch. Uh and that's good one. So don't worry. uh none of us know or what the next AI model will unlock

**[16:26](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=986s)** and what it's impossible today may be possible next week. So the key is that we don't bet everything on one giant plan. We take small iteration and quick laps and let them compound into big goals. And it's just theory. It's our journey. And I want to be honest about how it actually looks like. And these aren't for neat single steps. Uh each one is a phase made many of uh the loop I already mentioned. Lots of little iteration. no big jump jump between between them. So the [snorts] road towards QA without QAS like many years ago we started like with

**[17:16](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=1036s)** the quality assistance like building quality with the teams then we realized that the team is mature enough and we can be somewhere else sometimes. So we come up with a template to be sure that every team follows the same things everything what we need and they don't miss anything and then AI step in so we start to we started building our prompt library basically the set of sophisticated prompts that helps team to run or facilitate the QA activities much faster with a confident and then one a anthropic release skills. So we were able to move everything not or a lot of things to the skills and we are able to

**[18:07](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=1087s)** start building a QA agent that help us uh to do autonomous that testing and uh other QA things without involving QA. And we as a QA we can focus on improving our AI skills and get for to stage level like to be able to orchestrate all of these agents and each phase handed more to the teams and freed us to go farther and faster and that's the key. So I just want to show you some uh example how our newest phase actually look like. It's a center on things that we call QA agent and our QA agent it's

**[18:59](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=1139s)** you can think about it's like a closed code. It's living on our dev box and anyone can just point at QA job and what kind of QA job? You can we can run like the exploratory testing on Canva. We can uh basically uh work with the bug management. We can uh reproduce incomings tab against Jira. Uh recommend keep recommend close. We can gather more information from our lock system that could help developer to fix it or maybe to their agents to fix it. We do QA kickoffs that are basically we are able to uh provide the documentation about the project and the agent run uh or schemmit and uh prepare uh the whole QA code document for the team without any

**[19:49](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=1189s)** QA or team involvement. Definitely it's about writing test integration and unit one. And last but not least, it's a a metrics because it's great when when the team knows where the current quality is and what they should do better or just celebrate the things what they do really well. And uh yeah when when one agent isn't enough we are working on something what we call Q agent and it's orchestrating the whole fleet of itself running in parallel. So now like we can say hey I need to test it this and when I woke wake up in the morning I see the

**[20:37](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=1237s)** results. So yeah, QA agent does the thing and a human me as a QA just give the goals but still we review at least the result and that's the thing like the QA without QA we didn't add more developers we just reduce the number so it's 22 to one and but let me be precise what does it mean because it's not that the QA They disappear. They're just evolved around. They are no longer dedicated to the teams. Basically, the team handle their day-to-day quality work by themsel with agent helping and the QA engineer. We dedicate them to the key company goal

**[21:28](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=1288s)** through more complex things that could help moving company faster or some quality work that a single team cannot handle by themsel. It's like just cashure. The role didn't vanish. It moved to where is the most value. So we stop only running test. We start building the skills orchestrating the agents to run them and the bar for Q engineer now isn't just can you test but it's also can you run a fleet of agents but still one principle holds its to all together AI safe typing but it doesn't do thinking for us it frees us to think more about harder

**[22:19](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=1339s)** things so the orchestration, the taste, the calls about what Kalip means. That is the QA engineers new job. So let me back let me go back to my B statement from the beginning and treat it carefully. Now as of tomorrow, teams will not need QA engineers. I never said the company won't and that's the whole truth. Teams won't need the QA QA as they own the quality with agents helping. But the company the company will need QA engineers more than ever to build the skills, master the agents and take on quality challenges no single team can.

**[23:09](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=1389s)** This is the evolution of QA role. This is the fact not fiction. And here it is. As of tomorrow, company will need QA engineers more than ever. Uh I would like to share three quick uh lessons. First one is find a real bottleneck. It's rarely the queue. It's usually the thing everyone's waiting on. The second one is don't automate work away to shrink the team. automated to free the team for bigger work. That's the loop. And the free iterate small because you can't predict the next model. So quick laps and let them compound into some big one.

**[24:00](https://www.youtube.com/watch?v=4l-PnH0UUrY&t=1440s)** And the one I opened with inspiration is all around us. A supermarket could teach us how to scale quality. So you just have to look. And I'm curious what uh you will use as your own inspiration for your own use cases. Thank you so much. Last words. Uh teams won't need QAs. The company will need us more than ever. And that's not the end of QA. It's the best chapter yet. Thank you.
