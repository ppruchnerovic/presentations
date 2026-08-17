---
id: 875
title: "Hard Problems Hide in Boring Places: Turning Accounting Workflows into AI Products"
slug: hard-problems-hide-in-boring-places-turning-accounting
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Engineering"
type: "Keynote/Talk"
stage: "Airstream 1"
tags: ["Automation", "Data", "Large Language Models (LLMs)", "Security", "Software Architecture"]
speakers: ["Oleksandr Korotkykh", "Tolga Sümer"]
speaker_companies: ["Pliant"]
day: 2
starts_at: 2026-07-10T08:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=v_u6NpIAwzk
video_id: v_u6NpIAwzk
session_page: https://app.wearedevelopers.com/events/16/session/875
transcript: true
---

# Hard Problems Hide in Boring Places: Turning Accounting Workflows into AI Products

**Oleksandr Korotkykh (CTO — Pliant), Tolga Sümer (Senior Software Engineer — Pliant)**

`Track: AI Engineering` · `Type: Keynote/Talk` · `Stage: Airstream 1`

`#Automation` `#Data` `#Large Language Models (LLMs)` `#Security` `#Software Architecture`

[Watch the recording](https://www.youtube.com/watch?v=v_u6NpIAwzk) · [Session page](https://app.wearedevelopers.com/events/16/session/875)

## Abstract

Accounting and B2B payments are often seen as boring, solved problems — until you try to apply AI to them. The moment a system can misread an invoice, suggest the wrong action, or leak sensitive financial data, “cool AI demos” turn into serious engineering challenges.

In this talk, I’ll share how we at Pliant build AI features in one of the most constrained domains possible, where correctness, trust, auditability, and permissions are non-negotiable. Instead of treating LLMs as smart oracles, we design them as untrusted components that propose actions, operate on structured data, and are constrained by strict policies and approval flows.

We’ll walk through concrete patterns for turning existing accounting workflows into real AI products: grounding models in financial data, using schemas instead of free text, enforcing authorization at the system level, and designing human-in-the-loop interactions that users actually trust. Along the way, I’ll share failure modes we hit in production and how we fixed them.

This talk is about where innovation really happens: not in flashy demos, but in making AI work reliably in the places where mistakes are expensive.

## Speakers

### Oleksandr Korotkykh

*CTO — Pliant*

Alex Korotkykh is a fintech engineering leader with over 15 years of experience building large-scale, regulated software systems. Originally from Ukraine, he has been living and working in Germany for more than 10 years.

He has spent most of his career in fintech and data-driven products, working at companies such as Kreditech, figo, and Zalando, where he helped design, build, and scale complex platforms at the intersection of finance, data, and software engineering.

Alex joined Pliant at a very early stage and now leads its technology organisation of nearly 100 people, focusing on scalable architecture, security, and building reliable AI-powered products for B2B payments and accounting.

### Tolga Sümer

*Senior Software Engineer — Pliant*

I’m a Senior Software Engineer based in Berlin, currently working at Pliant, where I build internal and customer-facing AI features. My focus is on designing end-to-end AI workflows that combine multiple agents, tools, and data sources, from BI-style database interactions to RAG-based systems. Before moving into AI, I spent several years working on integrations, building APIs and connecting Pliant with accounting and PayOps platforms like DATEV, Lexoffice, and Circula, as well as helping shape our Partner API.

Before Pliant, I worked on large-scale backend systems in telecom and enterprise software, mainly around integrations, and high-throughput data pipelines. Earlier on, I explored game development and computer vision through internships and student roles, which helped shape my interest in building things end to end. I enjoy working on complex systems, turning ideas into production-ready solutions, and learning new technologies along the way.

## Transcript

*3,156 words · source: yt (en)*

**[0:02](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=2s)** Hello, hello. Thank you. My name is Alex. I'm CTO at Plant. Here is Tolga, a senior engineer at Plant. And yeah, today we want to talk to you about some interesting problems that we solved with AI. But first, I want to tell you a few things about Plant because I guess you guys don't spend your weekends thinking about B2B corporate payments. So, what does Plant do? Um probably you live through this. Someone in finance give you a credit card so that you can pay for the cloud tool, for dinner with business partner, for business trip. And the only problem you usually have with that is by the end of the month, someone from finance calls you and say, "Hey, where is the receipt

**[0:50](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=50s)** for this payment you made 2 weeks ago?" >> [snorts] >> Now flip the situation around. Imagine you are that guy or girl in finance. Um you have hundreds of cards. You need to uh make sure all the receipts are in place because otherwise you won't be able to do the accounting or to pass the audit. You need to make sure that the money on these cards are spent exactly for the purpose they intend to be spent, um that the expense policy has been followed, things like this. So, it's it's a lot of problems and pain that the finance people have that we at Plant trying to help them solve. So, what do we do? We issue cards, physical, virtual, Apple Pay, Google Pay, single-use cards, all of them.

**[1:40](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=100s)** Uh we help them control the cards, how they spend, uh how how they used. We help them track every payment, every cent that's moved from one account to another. And we help them automate boring and tasks. And this is probably the most important part for for this conversation. Um to put it in the um terms Actually, I need to Sorry, I just realized I I was standing in front of the screen. To make it um What? Okay. Okay. Ah, sure. Apologies. Um to make it uh to put it in the in the terms

**[2:28](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=148s)** that probably is more relatable to you guys. Uh imagine an API token which you probably um issued many times. API token is something you can issue and revoke at any moment. Uh it has an expiration date. It has its called some endpoints. And our virtual cards is basically works the same. Uh just the resource being scoped is not the endpoint, but money. A virtual card that is available only to be to work with a certain merchant, only up to 500 euros, only until next Friday. That's That's how our core product work. And now if now when I tell told you a bit about Pleo, let's talk about uh boring problems.

**[3:17](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=197s)** Please raise your hand who has expense policy at your company. Okay. And now please keep your hand up if you read it until the very end. Okay. Way fewer people. Um that's what I thought. That's usually a long boring documents um written in a in a not the most clean clearest language. And it can come in forms of notion pages, PDF, sometimes even handwritten notes. And we at Pleo need to read all of them. Each of them for our customers because following the expense policy or helping them to follow an expense policy is one of the tasks that we help them solve. And if they do not follow the policy, if they if their card holders do not follow the policy, they might have problem in

**[4:06](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=246s)** the next audit or or with regulators or something. And here is where the problems we are trying to solve leaves. >> So, here is our problem statement. On one side, we have hundreds of thousands of transactions coming in and on the other side, we have something called an expense policy, which is written in legal English, which is an obfuscated form of English. And somehow we need to make sure every transaction complies to the expense policy of this specific customer. And an expense policy is not very clear, as you might know. Like, there are rules hidden in between long documents. So, if we dive deeper into what an

**[4:54](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=294s)** expense policy looks like, is there are rules written in human language. Every customer might bring their own rules. There There could There could be rules like no alcohol on company cards, taxi rides outside of certain hours cannot be reimbursable, or entertainment over certain amount needs manager approval. So, the core problem here is we have sentences unstructured sentences, let's say. And somehow we need to enforce them concretely with logic. And each of those policies are growing in their own pace. They can change or they can remove some rules. So, and if you take a look at the other side, here is how a transaction looks like. Hope it's visible with the glare. It's basically a huge chunk of JSON. We

**[5:43](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=343s)** have the amount, the category of the transaction, the time, who spent this transaction, team and project, which are accounting related fields. We have the merchant, the MCC code. You might be familiar with this if you worked in a fintech before. Uh we have the card type and if the customer uploads the receipt to this transaction, we also scan the receipt with OCR and extract every line item. A line item on the receipt means actually every item that you bought from the store, basically every line that you see with the VAT and the amount. So, according to this, how would you detect non-compliant transactions according to your policy? We had three attempts to solve this and each attempt

**[6:32](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=392s)** kind of led to other. The first one we tried was the most obvious choice, the rule engine. We can build a rule engine and we can encode every rule as a as logic, basically. The second take would be an LLM-based one. So, this was 2024 and LLMs were just taking off. So, why don't we try an LLM to make the judgment if a transaction is compliant or not. And the third approach would be the also another obvious choice that you might have heard in every conference talk or blog post. Why don't we combine a rule engine and then LLM? How maybe we can get the best of both worlds, but let's see. So, if you go to the rule engine, the first approach,

**[7:21](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=441s)** we just get the policy PDF, a human implements these rules into the rule engine, and the rule engine just runs deterministically and flags the transaction if it's compliant or not. So, what could be the problem with this is every change in the policy or when you onboard a new customer, somebody needs to code these rules into the into the rule engine, right? You might be thinking why don't you just build a rule builder and give it to the customer? But actually, that doesn't really solve the problem. You just delegate the customer to do this coding even if you build a very user-friendly UI for this rule builder, whatsoever. And another problem would be a rule engine can only test if [snorts] a field exists or if you built this field into

**[8:11](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=491s)** the rule engine. So, you might end up needing to build thousands of thousands of fields and you might have huge drop-downs in this rule engine. So, why didn't we choose this? It's It doesn't seem very scalable. Every policy change needs manual work and you need to implement endless options to this rule engine. But, obviously, it's very good at speed, cost, and almost perfectly auditable because it's just a rule engine, the one we we are used to for many years before the LLMs. The second take we will go [snorts] through was the LLM-based one. So, in this one, we take the policy PDF plus the transaction data, we give it to the LLM in a very basic

**[9:01](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=541s)** naive manner, let's say, and just ask it is is given this policy PDF, is this taxi charge of 100 euros at 11:00 a.m. compliant? So, you just give the PDF, the data, and ask a very basic question, is this transaction compliant? And it will give you an answer in a way that like, no, it doesn't comply, or yes, it's compliant with this policy. But, the problem is with this very naive approach, if it says no, you don't really know why the LLM said no. So, basically, we cannot really make this auditable. Compare compared to the rule engine. So, uh but otherwise it's very good at handling ambiguity. It already knows

**[9:49](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=589s)** about all the real world cases and it's actually very low maintenance. You basically delegate all the work to the LLM. You give the PDF the transaction, just ask it if it's compliant. So, no development effort or maintenance effort. And you can onboard any client without any change. But the deal breaker here was also auditability. So, that's why we moved on to the third approach, the hybrid one, the textbook answer that you might have heard from other talks as well. But let's see if it works at the end. So, the approach here was in two stages. Now we use the rule engine in combination with the LLM. We only

**[10:35](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=635s)** uh we we split it into two phases, onboarding and runtime. During the onboarding we give the PDF to the LLM again. The LLM extracts structured rules, but the core idea here is that now the LLM writes the code into this rule engine. So, LLM is basically a compiler. It gets the PDF, it codes the logic into the rule engine. And at the runtime the benefit we would have is we have a completely deterministic setup. We don't deal with the LLM on runtime, which makes this solution perfectly auditable, traceable, reproducible, however you call it. And it's very scalable because the onboarding is handled by LLM and the rule engine

**[11:22](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=682s)** is also the rules are implemented by the LLM. Performance-wise also no issues. We know how to deal with rule engines. So, it seems like the perfect solution. It's the architecture that always works in blog posts and conference talks. It also worked for us almost, but just until we run a real transaction through this logic. So, then a grocery receipt came and broke all of this. It looks very clean at the beginning. It's groceries from REWE. You might be familiar with this market if you're from Germany or maybe you visited one during your stay here. So, you might have already noticed the problem if you remember the no alcohol

**[12:11](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=731s)** policy on your company credit card. So, between the coffee and the paper, there is one Heineken. And no merchant category, no keyword list would really tell you this is alcohol. You just know it from your real world knowledge that Heineken is alcohol. And it took you maybe two, three seconds to understand this. But, how would you make a rule engine really catch this amongst thousands of transactions? So, where the rule engine failed was not every real world case can be formulated as a rule, apparently. How would you detect alcohol? Well, you can imagine building building a complex map of thousands of brands of alcohol, and maybe you can do some regex to check the

**[13:02](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=782s)** receipt OCR line items. You can catch it, but this requires huge maintenance, and it's not even guaranteed that you can maintain this huge word list of alcohol, non-alcohol, whatever. Every category you need to maintain. And another case would be if you if you remember the rule about not having entertainment over 200 euros in your company policy. Imagine you get a transaction for 250 euros at a karaoke bar. Is it really team building or is it just a fun night with your colleagues? So, no no field in data can also tell you. So, that's how we ended up giving up the rule engine for the evaluation phase. Now, it was clear that to to have a

**[13:51](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=831s)** feature like this, we really need an LLM. So, at first we had only one hard requirement. We imagined auditability was very important, the key to this feature, but then we realized, yeah, we need real-world judgment to evaluate a transaction, which basically means what an LLM can do. So, we added one more hard requirement, a gate to to our scorecard. Now, it looks like this. So, the LLM can actually LLM actually works. It can evaluate any transaction and it's actually mostly correct almost every time. But, it's not auditable. So, we we actually went out looking for a

**[14:39](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=879s)** fourth approach. The hybrid couldn't catch the case, but an LLM would have caught this case. But, now the question actually became, how do you make an LLM-based feature auditable at the end? So, here is the plot twist of this talk. The textbook solution was actually not so textbook, so we went on to find another solution at the end. So, here is the pipeline we actually run now. We use LLMs on both sides, both on onboarding and on runtime to actually evaluate transactions. But, how do we fix auditability is first, the policy PDF comes, uh the LLM extracts the rules from this policy PDF. But while extracting the rules, we save

**[15:29](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=929s)** the links to the original sentences on the original PDF. So, there is a link between the answer of the LLM onto the original input it it took. And at the end, the rules are extracted, a human verifies just after this step. So, a human actually approves that, "Okay, I like these rules." And now it became a approved set of rules, a closed set of rules we can work with. And right on runtime, we get this closed set of approved rules, and the LLM makes the judgment. Plus, the LLM gives the answer and the reasoning, and which clearly states which rule is broken, which rule was violated. And

**[16:17](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=977s)** since those set of rules were already approved by the customer during the human in the loop, uh everything is trackable to the original sentence on the original expense policy PDF, which was approved by a human. So, how we fixed auditability actually comes down to this. This is how the onboarding step looks like. On the left side, there is the actual PDF. And on the right side are the rules that were extracted from by the LLM, which are more simpler rules rather than this huge mess of legal text. And on the right side, shown on the UI, uh the customer can actually edit, delete, modify some of the rules. And if they like the rule set, they can approve and save this rule set as the

**[17:07](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=1027s)** working copy. And during runtime, uh we also asked the LLM to give us the result plus give us the IDs of which rules are violated and why does it think that rule is violated? So, it cannot really invent a rule. It has to choose from a specific set of rules which, as I mentioned, approved by the customer, reviewed. So, at the end, everything points back to the original text. And this is how we try to handle transparency. We we show all the broken rules on the UI. So, this is the details of a transaction that was reviewed by our feature. You have these

**[17:56](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=1076s)** little labels which indicates those rules are broken. And if you click on any rule, it points you back to the original extracted rule set which was taken from which also contains a link to the original sentence from the PDF. But, yes, our journey was more about, yeah, nothing is perfect. We are not claiming this is perfect, as well. We had to have some trade-offs, as usual. We traded latency and costs. Obviously, the rule engine much must much more cheaper, much more faster. For us, it wasn't really feasible to do an LLM call for every transaction. So, what we ended up doing to mitigate this was Now, we batch the transactions into

**[18:45](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=1125s)** piles and we queue them and review them periodically. If you if you really had a rule engine, you could have done it in runtime. But, with the LLM, you need to, yeah, think about the latency and cost more. And another problem was LLMs are not meant to give reproducible results. So, we ended up trading away reproducibility, as well. With LLMs, you can try to force to make it reproducible with play maybe playing with the temperature or some things maybe even fine-tuning it, but at the end there is no guarantee that you will get the same results every day. But that was something we were willing to give away to make the feature work. And actually the two requirements we

**[19:35](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=1175s)** tackle tackled on by trading these away was now we have the judgment of the world perceiving the world this solution handles real world edge cases without an engineer having to maintain a a very complex rule engine with thousands of rules, products, brands, or any kind of logic. And at the end we somehow made it auditable. We thought with an LLM no it's not possible to make it really auditable on Fintech grade. Let's say but at the end every result links to the violated rule from your company policy, why it was violated, and the rules are already approved in the beginning by a human and everything points to the original PDF. So the real scorecard turned out to be

**[20:28](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=1228s)** our solution can do the judgment, it's auditable, it can handle out of ambiguity, it's scalable, but we traded away latency and now this solution is not very reproducible because of the reason I told you LLMs are not meant to give reproducible results. >> Thank you. So what have we learned uh in this journey? Uh lesson one and this is probably the most important one if you guys going to take only one lesson uh one idea from this talk please take this one. >> [sighs] >> If you build a feature with LLM try to find the most inconsistent, the most realistic, real real life, unprepared, not cleaned data that you can

**[21:17](https://www.youtube.com/watch?v=v_u6NpIAwzk&t=1277s)** and use it for your test set as as soon as possible. Otherwise, you might end like us and almost ship a solution that doesn't really work with real life data. Um lesson number two, be very precise with what your requirements are. Auditability and repeatability are not the same and as Tolga just explained, LLMs are not meant to always to be able to provide repeatable, exactly reproducible, 100% results.
