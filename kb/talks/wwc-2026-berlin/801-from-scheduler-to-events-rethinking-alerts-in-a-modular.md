---
id: 801
title: "From Scheduler to Events: Rethinking Alerts in a Modular System"
slug: from-scheduler-to-events-rethinking-alerts-in-a-modular
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Software Architecture"
type: "Keynote/Talk"
stage: "Stage 2"
tags: ["C#", "Clean Code", "Event-Driven Architecture (EDA)", "Legacy", "Migration", "Modularization", "Performance", "Software Architecture", "SQL", "System Design"]
speakers: ["Cristina Musceleanu"]
speaker_companies: ["European Central Bank"]
day: 1
starts_at: 2026-07-09T15:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=XYsECn5IRn4
video_id: XYsECn5IRn4
session_page: https://app.wearedevelopers.com/events/16/session/801
transcript: true
---

# From Scheduler to Events: Rethinking Alerts in a Modular System

**Cristina Musceleanu (IT Application Development Expert — European Central Bank)**

`Track: Software Architecture` · `Type: Keynote/Talk` · `Stage: Stage 2`

`#C#` `#Clean Code` `#Event-Driven Architecture (EDA)` `#Legacy` `#Migration` `#Modularization` `#Performance` `#Software Architecture` `#SQL` `#System Design`

[Watch the recording](https://www.youtube.com/watch?v=XYsECn5IRn4) · [Session page](https://app.wearedevelopers.com/events/16/session/801)

## Abstract

Many enterprise systems rely on a central scheduler to run alerts and notifications - until that scheduler becomes a bottleneck for change, reliability, and scalability.
In this talk, I’ll share our ongoing journey of replacing a traditional scheduler-based approach with event-driven processing in a large, modular system. Instead of rewriting everything or introducing heavy infrastructure, we focused on changing the architecture step by step: decoupling alert logic, isolating failures per module, and moving from time-based execution to meaningful triggers.

I’ll walk through the design decisions we made, the trade-offs we faced, and the mistakes we learned from while transforming how alerts are generated and processed. This session is not about a perfect end state, but about the real work of evolving a legacy system under real constraints and how small architectural shifts can lead to big improvements in resilience, clarity, and team ownership.

## Speakers

### Cristina Musceleanu

*IT Application Development Expert — European Central Bank*

Cristina Musceleanu is a software developer in large-scale enterprise systems, with a strong focus on software architecture, modular design, and sustainable modernization. She is currently involved in evolving a legacy alert and notification platform from a centralized scheduler-based model to a more modular, event-driven architecture, applying principles from Clean Architecture and Onion Architecture to improve resilience, maintainability, and team ownership.
Cristina is passionate about turning complex systems into clear, understandable designs and believes that great architecture is built through small, thoughtful steps rather than big rewrites. She enjoys sharing real-world lessons from ongoing projects and helping teams modernize responsibly in regulated and high-impact environments.

## Transcript

*2,306 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=XYsECn5IRn4&t=0s)** Okay, it's the last presentation of the day. And we're turning to a very familiar challenge in enterprise systems. How to modernize something important without pretending you can rewrite the whole world overnight. Cristina Musculino is a software developer working in a a large scale enterprise systems with a strong focus on software architecture, modular design, and sustainable modernization. In this session from scheduler to events, rethinking alerts in a modular system, Cristina will share the design decisions, trade-offs, and mistakes learned while transforming how alerts are generated and processed under real constraints. So, for this presentation, remember questions through the app. Cristina has prizes for the best

**[1:06](https://www.youtube.com/watch?v=XYsECn5IRn4&t=66s)** questions. So, put your questions in there. There are no bad questions. Competition time, people, and these are good prizes. So, please welcome Cristina Musculino. >> Thank you. Thank you, Ryan, for the introduction. Good afternoon, everyone, and thank you so much for attending my session. Let me start it. Uh One second. I think I have an issue. Okay. Here we go. So, uh Yeah. Before we start, let me briefly introduce myself. I'm Kristina. I'm a team lead at European Central Bank, where I work on supervisory applications that support European banking supervision. And with that, I'd like to tell you a

**[2:11](https://www.youtube.com/watch?v=XYsECn5IRn4&t=131s)** story about a notification engine that grew far beyond what we originally designed it for. Before starting, let me ask you something. How many of you have ever inherited a system where your very first thought was, "I really hope I don't have to change this." Be honest. I see quite a few hands raised. And if you didn't raise yours, maybe it's simply because you've luck You've been lucky so far. Because sooner or later, every engineer meets that system. So, let me start tell you the the story of ours. It's not a story about Kafka. It's not even a story about notifications. It's a story about growth.

**[3:19](https://www.youtube.com/watch?v=XYsECn5IRn4&t=199s)** About what happens when more and more people start depending on a system until changing it starts to feel risky, but also difficult to evolve. Let me show you how a notification was created. Every minute, our scheduler woke up. It connected to the database of IMAS. Let me zoom in for a second. IMAS is one of the largest supervisory application in the ECB. It supports single supervisory mechanism, the supervisors, to support the the supervision of insignificance banks across Europe. It generates alerts notifications that are sent to supervisors whenever their attention is required. If a task is completed where a decision has to be

**[4:25](https://www.youtube.com/watch?v=XYsECn5IRn4&t=265s)** approved, where or an important task status task changed. So, back to our scheduler. Every minute connected to database, it loaded everything it might possibly need. Then, prepare the data, evaluated the expressions, generated notifications, and finally, deliver them. That's simple. At least, that's how it looked. But, honestly, when this was first uh this solution was first designed, it was exactly the right solution. We had only five entities, a bunch of business rules. Everything was simple. The code was easy to follow. Everything was fast, easy to understand, easy to test, easy to change. At that moment, there There nothing wrong with this architecture. The real challenge came later.

**[5:34](https://www.youtube.com/watch?v=XYsECn5IRn4&t=334s)** The best part, the business loved it. Every time someone asked for a notification, we could deliver it. Every new feature created real value. And that's what we we usually want, isn't it? Success. But success has an interesting side effect. Once people notice something works, they all want to use it. And that's what exactly happened. More teams asked for notifications. Then, five entities became 20. The rest, nothing changed. The same database, same scheduler, same architecture. We just kept adding more. More notifications, more business rules. And because every single addition worked, nobody had a reason to stop. But then came the day. It wasn't that we had more entities,

**[6:43](https://www.youtube.com/watch?v=XYsECn5IRn4&t=403s)** but those entities started depending on one another. Some required subscriptions, dynamic subscriptions. Others depended on reference data. There were special cases, exceptions, business-specific logic. And of course, more rules. But our scheduler didn't know any of that. Every single minute, it loaded more data than before, whether anything had changed or not. Then came the day when our architecture started talking back. The first sign was memory usage. Every execution loaded more data than before. The second, processing time started to grow. Remember, many more entities, more dependencies, more notifications. And that happened every single minute. Debugging became harder, too. When something went wrong,

**[7:48](https://www.youtube.com/watch?v=XYsECn5IRn4&t=468s)** it was immediately obvious what had when the problem actually started. And probably the the hardest one was this one. Changing one notification could unexpectedly affect another. But this wasn't the real problem. Our engine still worked, the notification was still being sent. But every single minute, it became just a little bit more expensive. Then came the day none of us forgot. One script could update 10,000 records. Our SMTP server couldn't keep up. The emails started flying out. Inboxes exploded. It was memorable. But we were we realized that all those issues actually exposed weaknesses over the years. So eventually gave those weaknesses names.

**[8:54](https://www.youtube.com/watch?v=XYsECn5IRn4&t=534s)** The first one was what we called the blast radius. Changing one notification could affect many. A very small change could surprisingly affect have large consequences. Then polling the past. Every minute we were searching the database hoping something would change. Most of the time nothing happened. Then came the email storm. It wasn't that the scheduler was sending too many notification the wrong notifications. It was simply sending far too many of them. And then the one that worried us the most was this one. Imagine an alert becomes active. Few seconds later someone resolves it. Our scheduler checks every minute and by the time it wakes up

**[10:01](https://www.youtube.com/watch?v=XYsECn5IRn4&t=601s)** the alert has already disappeared. The notification was never sent. So we had to um we had to um decide how to fix this issue. We explored three different directions. The first was the lowest risk one. The second moved us much closer to a real processing time. And the third was the most scalable one. On paper they all look good. But we weren't trying to choose the most impressive architecture. We were trying to choose the best next step. Because good architecture isn't about making the biggest leap. It's about making the right one. We chose option A. Why? Let's compare the two approaches.

**[11:07](https://www.youtube.com/watch?v=XYsECn5IRn4&t=667s)** Before, our scheduler rebuilt the entire picture. It loaded everything. And only after that it evaluated the rules. So, we asked ourselves a very simple question. What if we turn the process around? What if instead of loading any data, why not start with the rules? Because every rule knows already which entities it depends on. Only after that, we asked, "What has changed since the previous execution?" And then, we load only the data required for those rules. Instead of rebuilding the entire world, we fetch only what's needed. One simple idea. One different way of thinking. And that changed everything. While improving while while while uh implementing the option A,

**[12:16](https://www.youtube.com/watch?v=XYsECn5IRn4&t=736s)** we were realizing something. We weren't improving uh the performance. We were improving the architecture itself. So, that led us to a design principle. Keep the core stable. Make the edges replaceable. Everything in this purple box it's where the business value lives. The rule engine loading only the required data creating notifications. Today our schedule triggers the process. Simple reliable. That's what we exactly need today. Tomorrow maybe an IM service will publish Kafka events. That's perfectly fine. We don't have to change the business logic. We only replace the trigger. And one day if our system evolves even further CDC together with Kafka might become another option.

**[13:23](https://www.youtube.com/watch?v=XYsECn5IRn4&t=803s)** Again the core remains exactly the same. Three different triggers. One identical notification system. Do you remember all those uh six problems? Memory usage, performance missed alerts. They all had the same root cause. But for many years we treated them as separate completely separate problems. Once we fix that the improvements came naturally. Less data loaded. 90% uh unnecessary data. And that means also less memory usage. Because we stopped we simply stopped loading more data. Faster execution times. And those were not all the improvements that our users noticed. The notifications became relevant. Failures became isolated. Alerts became reliable. Those were the improvements our users

**[14:30](https://www.youtube.com/watch?v=XYsECn5IRn4&t=870s)** noticed. Looking back, I don't think we fixed six different problems. We solved one architectural issue and six different symptoms. Simply disappeared. If there is one thing I'd like to take you take away from this talk is these three ideas. Architecture is a team sport. The hardest part of this project wasn't about writing the code. It was about disagreeing where responsibilities belong. Once boundaries became clear, the implementation was straightforward. Because good architecture starts with good conversations. Second, make your system systems observable. Because when something goes wrong, you don't want to guess. You want to know. And finally, simplicity wins. We explored Kafka, CDC, different event-driven approaches.

**[15:38](https://www.youtube.com/watch?v=XYsECn5IRn4&t=938s)** In the end, the best solution was the one that fixed today's problem without closing the door on tomorrow. If I have to summarize this entire project in one simple sentence, great architecture makes change boring. Because when change Adding a feature isn't stressful. When one change doesn't bring five others. And when deployments are not scary. That's when you know an architecture is doing its job. And this is not the end of the story. This is simply the next chapter. The next step is moving to uh toward domain events. Instead of constantly asking what has changed, the business simply tells us. It's a

**[16:43](https://www.youtube.com/watch?v=XYsECn5IRn4&t=1003s)** much cleaner model. We are also integrating with the ECB central notification system. Because notifications shouldn't belong to one application. They should become a shared capability. And the one that I'm most proud of We don't know what the future will next trigger will be in the future. Maybe domain events, maybe Kafka, maybe something none of us has even imagined yet. We simply replace the trigger. We don't have to redesign the entire notification engine. From one notification engine to a shared platform. For me, that's designing for change looks like. As engineers, we usually measure success in uh milliseconds, CPU, performance. All those things matters. But I don't think that's what makes

**[17:54](https://www.youtube.com/watch?v=XYsECn5IRn4&t=1074s)** an architecture successful. For me success is much simpler. Can another developer add a new feature without wondering what else might break? If the answer is yes, the architecture, the good architecture, is the one that gave the people confidence. So, I'd like to leave you with one simple thought. Build for change, not for today. Because today's software will probably become tomorrow's legacy. Thank you so much. I'd be happy to take any questions. And as Ryan said, for the three first three questions, I have some ECB souvenirs with me. They are very cool. Thank you. >> [applause] >> Oh, wow. You guys did great. I mean,

**[19:01](https://www.youtube.com/watch?v=XYsECn5IRn4&t=1141s)** there's so many questions in here that just came in in the last couple of minutes. >> Thank you. >> Wonderful. All right. So, what do we have here? >> Nice to meet you and congratulations. >> Uh, how long did it take to implement the changes? >> Yeah. >> Uh, almost uh 1 year and we are still working on it because uh as I mentioned, we are integrating it with the ECB central notification system. >> Okay. >> Uh, I think this one is a very good one. Uh, hi. What are your alerts actually about? It's a very good one because I didn't mention it. There are so many things in there.

**[20:12](https://www.youtube.com/watch?v=XYsECn5IRn4&t=1212s)** Um, okay. Uh, what types of data are you loading? And, uh, does it contain right time logic? Okay, I will try to, uh, answer this. So, notifications are simply, uh, messages to, uh, keep the supervisor in, uh, notified on something. But, alerts, uh, they are more a bit more complicated. There are, uh, we have rules for open and close alert. What that means? Um, there is an expression on both uh, open and close alerts. When something change, I will give you an example. When When a supervisor has to approve a decision, they receive an alert. And they can click on on a link and go

**[21:20](https://www.youtube.com/watch?v=XYsECn5IRn4&t=1280s)** to iMAS and click on the button approve. And those alerts will be sent to the supervisor until the supervisor actually will take that action. When they When they take it, the the alert can be closed. So, that is That's why we have open and close to make sure that the action required is, um, is completed. >> Okay. One more. >> Um, Okay. How to Oh, okay. I will I'm trying to Yeah. >> Yeah. >> Uh, I think also this one is good because it's related to alerts. How does the new scheduler actually solve the ghost issue? That's That's a very good one. And I think that comes from from a

**[22:32](https://www.youtube.com/watch?v=XYsECn5IRn4&t=1352s)** colleague of mine. Before, when the scheduler started to to process everything, uh, they checked both opening and closing rules. And when the alert was fixed, the closing rule was was completed, and it didn't open it yet. So now every time the scheduler triggers the process, we don't start with a closing rule. We start with the open rule. That was That was it. >> Okay, so we've got three winners. I think it was a What's that? >> Yeah, uh, Caesar? >> Caesar, >> Uh, yeah. >> Lin Tao, and Tomas. >> Please come here. >> to the stage. >> Thank you so much.

**[23:37](https://www.youtube.com/watch?v=XYsECn5IRn4&t=1417s)** >> All right. So, thank you very much, Cristina. >> Thank you. Thank you, Ryan.
