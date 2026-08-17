---
id: 728
title: "5 Years in Cloud Native: The Good, the Bad, and the Bill"
slug: 5-years-in-cloud-native-the-good-the-bad-and-the-bill
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Cloud & AI Infrastructure"
type: "Keynote/Talk"
stage: "Stage 5"
tags: ["Cloud Security", "DevOps", "Google Cloud (GCP)", "Infrastructure", "Microservices", "MongoDB", "Performance", "Security"]
speakers: ["Simone Desantis"]
speaker_companies: ["Openapi SPA"]
day: 1
starts_at: 2026-07-09T12:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=WNuNfWEeWGQ
video_id: WNuNfWEeWGQ
session_page: https://app.wearedevelopers.com/events/16/session/728
transcript: true
---

# 5 Years in Cloud Native: The Good, the Bad, and the Bill

**Simone Desantis (CTO — Openapi SPA)**

`Track: Cloud & AI Infrastructure` · `Type: Keynote/Talk` · `Stage: Stage 5`

`#Cloud Security` `#DevOps` `#Google Cloud (GCP)` `#Infrastructure` `#Microservices` `#MongoDB` `#Performance` `#Security`

[Watch the recording](https://www.youtube.com/watch?v=WNuNfWEeWGQ) · [Session page](https://app.wearedevelopers.com/events/16/session/728)

## Abstract

What happens when your data center literally catches fire? Five years ago, a literal disaster was the catalyst for our total migration to Cloud Native. But moving from on-prem microservices to a fully scalable cloud architecture was a journey filled with scars, paranoia, and expensive lessons.
In this session, I will share my perspective as a CTO who led a team through a deep cultural transformation: the metamorphosis from traditional system administration to a DevOps mindset, where Infrastructure as Code (IaC) became our most valuable asset. We will dive into "scalability paranoia"—how we optimized container orchestration to beat the competition without losing our sanity (or the entire budget).
We will break down the financial reality of elasticity: while on-prem environments force you to distribute workloads over time to avoid saturating fixed hardware, Cloud Native demands a complete mental reboot. I’ll share how we shifted from 'squeezing every cycle' out of static servers to an event-driven model designed to scale to zero. We'll discuss the danger of misconfigured scaling—the 'blank check' risk—and how we learned to orchestrate resources so they only exist when there is actual work to do, finally aligning our infrastructure costs with real business value. This isn't a polished success story; it’s an honest breakdown of complex solutions to simple problems, and how this journey finally allowed us to sleep at night.

## Speakers

### Simone Desantis

*CTO — Openapi SPA*

With years of experience in internet technologies, he specializes in designing, developing, and maintaining robust and stable IT infrastructures. Naturally inclined toward problem-solving, he thrives on complex systems: analyzing them to identify bottlenecks, then driving optimization and improvement. Currently, he is focused on designing and developing a new high-performance API infrastructure.

## Transcript

*2,092 words · source: yt (en)*

**[0:14](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=14s)** Hi everyone. Thank you for being here. My name is Simone DeSantis. I'm the CTO of developer.api.com. Today, I'm not going to give you a typical architecture talk. I'm going to tell you a story, our story. It has a fire, some expensive mistake, and a promise, and a happy ending. Let me start with a question. What happened when your data center is on fire? I don't mean a metaphor, real flames, real smoke. Five years ago, this stopped being a hypothetical question for us. And one specific night, and the honest answer one of the question changed almost everything about my team build and run software today. I want you to tell this story the way movie tells story. As a hero journey. A hero lives an

**[1:03](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=63s)** ordinary life, something force them to leave it behind. They face trials they didn't choose. They meet mentors along the way. They almost fail more than once, and eventually they come home changed carrying something valuable enough to share with others. This is essentially what happened to my team and to me. I'm the CTO who lived through every stage of it, from the first phone call about the fire to where we stand today. Today, I'm not going to give you a polished highlight reel. I want to share the scares, the paranoia, and yes, the bill, so that you don't have to learn every one of this lesson in the expensive way like we did. Here's the map for where we're going

**[1:52](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=112s)** today. We start in our ordinary world, a private cloud that felt safe and stable. Then disaster strikes without warning. Then come the first attempt to fix things using tool we already knew, and it turns out to be very expensive attempt. We meet our mentors. We cross threshold into real cloud native architecture. We survive a series of trial, each one harder and more specific than the last. We win a genuine reward. Then, and this is the part almost nobody tells you in advance, winning bringing bring a whole new set of problems. And finally, we return with the lesson. Every hero journey starts in an ordinary world, and our look pretty comfortable.

**[2:42](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=162s)** We had physical host running in our private cloud. We had backups, real one, tested one, not checks in a compliance form. Uh And we were not living in the stone age. Part of our infrastructure was already as microservices. On paper On paper we were in generally good shapes, stable, predictable, boring, even safe. I want you to hold on that feeling for a moment, because it's exactly what disappear in a single night. And then the disaster. A fire broke out in our data center. Not a joke, not a drill. A real fire that destroyed our physical server. The actual machine gone. That alone would have been a serious problem, the kind you can usually cover from in a few painful day. But here is

**[3:31](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=211s)** the part that really hurt. The fire destroyed our backups, too. The safety net we trusted, the thing that existed in exactly this situation, gone. In the very same event, the hero's journey, there's a moment where the hero's world is destroyed, and there's no path back to how things were. For us, that moment was very real and very literal. We were at zero, completely. Every line of code, every configuration, every safety net we thought we had gone in one night. I still remember getting that phone call. When you are in survival mode, you don't redesign everything from scratch. You reach for what you already know how to do, as fast as you can. So, we

**[4:19](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=259s)** rebuilt from zero using the same paradigm we had before, virtual machine server we configure and manage ourselves, the same mental model we had used for here. The one real difference was where it all lived, not in our own data center anymore, but at a major hyperscaler. And honestly, it felt safe precisely because it was familiar. What we learned very quickly and very painfully is that it was also the most expensive option available to us. Every hero at some point need a mentor, someone who's someone like Gandalf, okay? Who has already walked a version of this path.

**[5:07](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=307s)** Our arrives in a form of external consultant. And to their credit, they didn't just come in and fix our infrastructure for us. They changed the way our whole team thought about it. The starting point was Terraform. Instead of clicking through cloud console and configuring server by hand, one at a time, we began describing our entire infrastructure as code, version controlled like any other software, reviewable by teammate before it ships, and fully repeatable on demand every single time. It sounds like a small technical detail on the side. It was not small at all. Over the following year, infrastructure as code become uh without much competition the single most valuable uh asset of our engineer organization

**[5:55](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=355s)** own. More valuable than any individual server, any individual service, and any individual piece of application code we had written. Everything else in the story get built on that foundation. With Terraform underneath as as as a foundation, we made a decision with no way back. A complete refactoring of our systems and a genuine cultural transformation along its alongside it. We were leaving traditional system administration behind for good, stepping a full into DevOps mindset. This is the moment in every hero's journey where the hero crossed the threshold. Where they leave the familiar world behind completely. With no easy way to return to it. For us, it meant that every single assumption we had have we

**[6:44](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=404s)** made about server, our capacity planning, and about cost was about to be questioned one assumption at time. Refactoring sound clean and simple on slide. In reality, it meant facing almost almost philosophical decision one right after another. Often with no clearly correct answer. The first big one, which hyper scalar? AWS, Google Cloud, Azure. Each one represent its own philosophy, its own pricing logic, and its own ecosystem of tool and trade-offs. The second decision right behind it was which orchestration technology? Fully managed Kubernetes service? A cluster we build and run entirely ourselves? Or different approach? I'm not going to pretend there's one

**[7:32](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=452s)** universal correct answer to either question. There is only the answer that fit your specific team, your existing skill, and and your actual budget. We spent real weeks on just this two decision alone and we generally change our mind more than once along the way. The next trial waiting for us was vendor lock-in. Every managed service you adopt make your team faster today and just a little more dependent on that one provider tomorrow. There's no way around that trade-off. You can only manage it consciously. We had to decide service by service exactly how much convenience was worth how much dependency. And tied directly to that question was another hard one, data persistence. Containers are by

**[8:22](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=502s)** design meant to be temporary. They can disappear and start at any moment, often on purpose of part of normal operation. So, where does your data actually live, physical and logical, when specific container that create is already gone? Get this one wrong and it doesn't cost you extra money down the line. It costs your data permanently. Then came a very practical, very physical trial, memory. Every single container carries some amount of RAM overhead just to exist before it had done any real useful work at all. If your application is heavy and you want to scale it horizontally and overhead multiply very quickly and so does your monthly bill. Also silently. So, we had to optimize our own

**[9:11](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=551s)** software at the code level. A smaller memory footprint, a faster startup time, an architecture designed from day one to run as many small efficient containers side by side. This trial deserved its own name, scalability paranoia. On premise, the challenge you face is fundamentally different. You distribute your workload carefully over time because your physical hardware is fixed and generally limited. In the cloud, your hardware is no longer fixed. It's practical infinite on demand. Nothing technical stopping you your system from scaling out of hundreds of instance in matter of minute. Nothing except your configured the configuration that you personally wrote. We had to

**[9:59](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=599s)** master several thing at once under real pressure. Cold start, how long a brand new instance takes before it actually useful to a real wedding user. An upper limit on instance. Deliberate ceiling so that a bug, unexpected traffic spikes, or even an attack cannot silently scale you straight into back bankruptcy overnight. Incorrect instance sizing, making sure you never quietly paying for compute power you never actually use. After 5 year of this approach, here's roughly where where we landed. Our reference try our infrastructure became generally cost-efficient, truly scalable without the drama it used to involve, more secure. Our deployment became

**[10:49](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=649s)** frequent, fast, and properly controlled instead of chaotic and nerve-breaking. And for the first time in our company's history, our infrastructure costs were actually aligned with real business value. We pay for what generally create value for the business. We stopped paying quietly for idle machines sitting around waiting for work that might never actually arrive. In the movie, this is where the heroes come home celebrated and the credits roll. In real infrastructure work, the story simply continue. This new architecture creates its own set of brand new problem. Small smaller than a little file, sure, but very real and very costly if if ignored. Let me work through four of them one at a time.

**[11:37](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=697s)** First, we need to forge our own sword. The generic framework available to us on the market were either too heavy in memory for our containers or too unstructured for dozen of independent team buildings APIs on their own individual style. So, we built a small micro framework optimized for low RAM usage that standardized exactly how every team at our company design and ship APIs. It's not glamorous work. It will never be open source, but it's one of the quiet and glamorous reason our containers stay small and our monthly bill stayed low. Second, shielding. We learn how to use multiple layer of CDN working together instead of competing with each other. CloudFlare handling one layer, Google handling

**[12:27](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=747s)** another. Every single request that get fully handled at the edge before it even reach us is a request that never touch our expensive compute layer at all. It wasn't only a performance improvement for our user, although it was that, too. Over time, it quietly become one of our most single effective tool for controlling monthly cost. Third, data. Database cluster are some of the most expensive expensive thing to scale in the cloud, and they simply don't scale as gracefully or cheaply as as stateless container. Our answer to this was simple to say and hard to execute well in practice. Cache aggressively everywhere it makes sense to do so. Every single request that get served from a cache is a request our database cluster never has

**[13:16](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=796s)** to fill and never has to bill. Fourth, rhythm. We had to build a real CI/CD pipeline from the ground up, adopted and learned to trust it completely. Moving from manual deployment done late at night to a controlled, repeatable, almost boring pipeline was its own cultural journey. And boring, by the way, is exactly what you want a deploying pipeline to feel like. So, what we bring back from this entire journey, infrastructure as code comes first, always. It's not an optional nice to have. It's the foundation that everything else in this story depends on. Design for scale to zero, not for your load peak. On-premise think optimize for fixed hardware you already own. Cloud

**[14:07](https://www.youtube.com/watch?v=WNuNfWEeWGQ&t=847s)** native thinking optimize for real current actual demand. Respect the blank check that auto scaling represent. Every single limit you don't set yourself is dangerous. Keep your containers small and keep your APIs standardized across team. And cache before scaling your This was not a clean success story. It has It was 5 years error of real scares, real paranoia, and yes, very some expensive lesson. But today, for the first time in a long time, my team and I actually sleep at night. Thank you for listening this to our story. I'm happy to take your question now there. Thank you.
