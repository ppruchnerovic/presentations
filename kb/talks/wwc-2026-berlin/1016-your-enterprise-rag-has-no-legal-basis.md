---
id: 1016
title: "Your Enterprise RAG Has No Legal Basis"
slug: your-enterprise-rag-has-no-legal-basis
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Security & Privacy"
type: "Keynote/Talk"
stage: "Stage 10 - powered by TikTok"
tags: ["AI Coding Assistants", "AI Standards", "Agentic AI", "Best Practices", "Documentation", "Generative AI (GenAI)", "Governance", "Next.js", "Node.js", "PostgreSQL", "Privacy", "React", "Software Architecture", "TypeScript", "Vector Databases", "Vibe Coding"]
speakers: ["David Klemme", "Tilman Mürle"]
speaker_companies: ["Komplyzen"]
day: 2
starts_at: 2026-07-10T14:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=UpwAj792WvI
video_id: UpwAj792WvI
session_page: https://app.wearedevelopers.com/events/16/session/1016
transcript: true
---

# Your Enterprise RAG Has No Legal Basis

**David Klemme (Co-founder and CTO — Komplyzen), Tilman Mürle (Managing Director and Co-founder — Komplyzen)**

`Track: Security & Privacy` · `Type: Keynote/Talk` · `Stage: Stage 10 - powered by TikTok`

`#AI Coding Assistants` `#AI Standards` `#Agentic AI` `#Best Practices` `#Documentation` `#Generative AI (GenAI)` `#Governance` `#Next.js` `#Node.js` `#PostgreSQL` `#Privacy` `#React` `#Software Architecture` `#TypeScript` `#Vector Databases` `#Vibe Coding`

[Watch the recording](https://www.youtube.com/watch?v=UpwAj792WvI) · [Session page](https://app.wearedevelopers.com/events/16/session/1016)

## Abstract

Your RAG system works beautifully. Under GDPR, it has no legal basis to exist.

Clean architecture. Proper embeddings. Maybe even agentic tool calling. You followed best practices. But when the auditor asks "what's the legal basis for this processing?" there's no answer. General-purpose "ask anything" chatbots have no defined purpose. Without a defined purpose, no legal basis can exist under GDPR. The architecture itself is the violation.

In this talk, I'll live-code a "best practices" enterprise knowledge bot, then ask the questions nobody asks: Where is purpose limitation enforced? Where is legal basis documented? I'll show why anonymization doesn't save you. 97% accuracy isn't "anonymous" under GDPR. It's still PII.

Then I'll show you the fix: a purpose-scoped bot architecture where legal basis is a first-class configuration item. Each bot gets a defined purpose, scoped data access, configured tools, and documented legal basis. The architecture enforces the boundaries. The retrieval layer can only access documents within that bot's scope. Non-compliance becomes architecturally impossible.

The good news? You didn't waste your investment. This is a 50k governance layer, not a rewrite.

Takeaways:
  - Why your RAG has no legal basis and how to fix it
  - The purpose-scoped bot pattern: document, enforce, and audit compliance by design
  - A brownfield rescue roadmap for existing systems

## Speakers

### David Klemme

*Co-founder and CTO — Komplyzen*

Hybrid AI and enterprise technology leader with 10+ years designing, implementing, and scaling production-grade AI platforms in complex enterprise environments. Bridges executive vision with technical delivery. From strategy and governance down to architecture, infrastructure, and code.

As Enterprise Architect at Rödl & Partner (~7,000 employees), architected a multi-tenant generative AI platform serving 6,000+ users with EU AI Act-aligned access controls. Led enterprise data strategy and Azure Integration Services rollout at enterprise scale. Previous experience includes ITSM transformation for German public sector (VBG) and AWS data architecture for Deutsche Bahn subsidiary.

### Tilman Mürle

*Managing Director and Co-founder — Komplyzen*

Tilman Mürle is Managing Director and Co-Founder of Komplyzen, where he helps organizations turn AI governance from a compliance exercise into an operational capability. He brings over a decade of leadership experience across SaaS, enterprise IT, and regulated environments, including his role as former CEO EMEA at Valiantys.

Tilman works with engineering, risk, and leadership teams to design AI systems that are measurable, auditable, and production-ready by design. His focus lies on operational AI governance, AI risk management, and translating regulatory expectations into practical architecture and workflows that scale.

He regularly speaks at industry conferences on AI risk, governance, and the realities of bringing AI safely into production.

## Transcript

*4,040 words · source: yt (en)*

**[0:02](https://www.youtube.com/watch?v=UpwAj792WvI&t=2s)** I introduce David Clemming and Yulia Clemming for the session. Thank you so much. >> Um thank you so much. So, now there's two names on here and it doesn't quite fit as you might have noticed. I'm David. This is not Tilman. Tilman is sick. He sends his compliments, but I've was able to convince my beautiful wife to join me here on stage. So, I'm eternally grateful that she did this on like 3-hour notice. Um we'll make do. So, um your enterprise rag has no legal base. Now, we're going to going to do a little demo. We're going to be interactive, um I hope. Um you'll get out of this what what what we

**[0:50](https://www.youtube.com/watch?v=UpwAj792WvI&t=50s)** want you to. Now, I'm going to do a little demo now. You've seen this a couple times. We're going to do a little twist. Okay? Now, what are we going to what are we going to build here? Enterprise chatbot. I'm not sure who of you, maybe give me a hand, uh has never used a internal chat with your documents kind of bot. Okay, I'm taking this uh uh okay, somebody has not. Now, my point is um they have sprung up like wildlife. We're going to build one now. We're going to look at it and we're going to see what's wrong with it and afterwards, um we're going to we're going to fix it. Now, I'll do this a little differently than I usually would. Can you read this okay? Can you read this okay-er?

**[1:51](https://www.youtube.com/watch?v=UpwAj792WvI&t=111s)** Thanks for that feedback. Um we usually do this a lot different, okay? Usually we rely very very heavily when we when we write production code for our customers um uh on on B map personas and workflows and gates. Now, this wouldn't fit into the next 8 minutes, so I cheated a bit, okay? I've been very comprehensive here. Um I compacted this as much as I could uh possibly could. Um and I already gave it extremely um specific instructions as you might um imagine. No. So, let me let me jump out of this one. Let's get this party started. Now, the agent will will run it. We'll take the specifications. It's more than one in

**[2:39](https://www.youtube.com/watch?v=UpwAj792WvI&t=159s)** this case because we split this up in a couple of things. And it will um it will guide us through to create an app for us that we're going to look at in a moment. Now, introducing my wife, I did just notice that I forgot to introduce me in the company. So, David uh I'm David Tillman, who's not here today. We are Complison, and we make sure you can ship AI systems without getting a fine. Now, while this is running, uh it's a chatbot, okay? We're doing nothing fancy. I'm trying to be as um as uh cookie-cutter as possible in order to actually have a running system in the next 8 minutes. Um and the funky thing is well, I I have run this about 10 15 times beforehand. It turns out a little different every time. This is where my

**[3:29](https://www.youtube.com/watch?v=UpwAj792WvI&t=209s)** strategist came from. He wants to do a git checkout. So, okay, I'll I'll I'll I'll try to keep this under control while this is running. So, it's running uh Vercel AI SDK. It's uh running uh with the with the standard libraries. We're not going to do anything super fancy here on the technical side. Um but we're going to use a sub-agent. Okay. So, it's a little more interactive. Um I think you've you've all seen this. Um this will now scaffold the app. This will install a couple libraries. We're going to use um we're going to use Tailwind. You can see the SDKs that are coming up, I hope. And luckily

**[4:18](https://www.youtube.com/watch?v=UpwAj792WvI&t=258s)** there's some things um the I will take off our hands now. I'm not sure if you uh if you remember using uh streaming response data from LLMs in the early days, I I didn't have too much fun, but I really really appreciate some of the libraries taking off the load. Other than that, it's just a a a simple component to now go and upload the document that we want to look at in a moment. Now, if we look at the subagent here, this is running through. It got as I as I mentioned, very specific um instructions here. Um it's running along nicely. Let's see where we are. Okay. Great. I did tell it to not make any mistakes,

**[5:07](https://www.youtube.com/watch?v=UpwAj792WvI&t=307s)** so I'm hoping uh that'll do for today. Um What else while this is running? So, what I should have maybe done before is check our knowledge graph um to see if there's anything interesting that we learned from the last couple of runs. Um doing this a little bit on the fly now cuz the subagents are already running, but this is our interpretation of context, so giving context to an agent in order to um not have to repeat myself, not have to explain everything over and over again, but be able to enforce the standards that we have

**[5:56](https://www.youtube.com/watch?v=UpwAj792WvI&t=356s)** established when we usually write production um kind of code. Now, this will give me a couple learnings. I will go live here. This is running localhost, that's why that's why he wants to um wants to have approval on everything. Um usually I would do this on a remote box, but I did not trust the Wi-Fi enough uh to dare to run this completely on the cloud. Um so, this is fantastic. So, told you a little bit about this. Chat component could should be coming up, and what we're not going to do, but I mean, you've seen this probably a couple times. Um at the end of this, we could just use uh Vercel CLI to uh push this prototype in the cloud,

**[6:46](https://www.youtube.com/watch?v=UpwAj792WvI&t=406s)** and in a minute we'd have something running um not on localhost, but in a network with SSL uh search set up and all of this, but I think we can we can skip this for this uh session here. You've done this before. Um the moments that take a little longer are um the quality gates. So, I did put in uh I think two quality gates just to make sure, you know, something is up when the agent actually tells me, so I'm not that surprised. Um this takes a moment, but it's usually um it helps quality a lot. Um not sure about you all, I've noticed that running this kind of demo with very specific instructions uh on Haiku, for example, if we stay in the cloud

**[7:34](https://www.youtube.com/watch?v=UpwAj792WvI&t=454s)** or in the Entropic Universe, it's absolutely fine. Uh it'll it'll do well. Um I'm using Sonnet now for the simple reason it's uh it's it's still fast, but it's a little less back and forth. So, looking at the time, this guarantees me that I don't have to do too much fixing um while it's there, but um doesn't always need to be opus. That's my message here. So. So, let's see if that helps. I doubt it, but I think or I know that it's almost

**[8:21](https://www.youtube.com/watch?v=UpwAj792WvI&t=501s)** there. This might still fail for a second, but if we are almost at the styling phase, um then we are almost through the first gate. Okay, run it yourself. That's a That's a new one. That's nice. See if I actually have to go in.

**[9:08](https://www.youtube.com/watch?v=UpwAj792WvI&t=548s)** So, what we did here is since I didn't want any keys anywhere, it's triggering one password CLI automatically just to have something. Now, I know that once it asks for this, it's uh more or less up and running. And then we should have a little chat site here. Okay, so now you understand why I asked it to do another styling pass cuz this is you would usually came out with the with the uh smaller models. Um it it'll work, but it looks like this. So, um let's give it just uh a a second until this is up. And while

**[9:55](https://www.youtube.com/watch?v=UpwAj792WvI&t=595s)** we are doing this, we will look at what we're going to upload in a second because what we want to do is chat with my document. What's the document? So, in this case, it's a vendor proposal. So, this is made up, as you can see. Couple gimmicks in there, maybe. Um but we're going to ask it in a moment what this is about and how expensive this vendor is. Okay, so this is about to be ready. You can see styling is applied. Would this be the the way that I would usually

**[10:42](https://www.youtube.com/watch?v=UpwAj792WvI&t=642s)** do this? I'm not sure, but, you know, um otherwise, it wouldn't fit into this uh window. >> [snorts] >> Let's give it a second. I guess we all know how this feels by now. So, I have a little bit of lighting, but I think we can see something. Now, we'll take the vendor proposal, the final final final version, and we'll ask a question. I want to chat with my document. So,

**[11:39](https://www.youtube.com/watch?v=UpwAj792WvI&t=699s)** we'll ask it about this proposal. I skipped the markdown part. Forgive me, please. But, I think the message here is it reads the content. It gives us back something. It's a cheeky answer. Um And that gives us um a chat with the document app with I mean, I faked the right part here, but I think you get the point. Works the same way if you have the vector database behind or not. Um it's ephemeral. Nothing is stored. It's self-hosted. It's You know, the EI act stuff is uh documented. So, I mean, it took a little longer, but it's under 14 minutes, and we have a fantastic little app that lets you chat with your documents. Does that ring familiar?

**[12:32](https://www.youtube.com/watch?v=UpwAj792WvI&t=752s)** >> Um David, I really would like to see this again because what I saw in here >> is um personal data. And whose personal data was in there? >> Um well, personal data, I mean, you know, you have the consultants in there. Their emails, maybe an address, I I guess. >> Mhm. This is what I saw. And uh what is the actual purpose of using this data? >> I want to know about their pricing strategy and you know, answer any questions I I have for the proposal. >> Okay. And um have you somewhere in your architecture defined the purpose? Because I could ask you many, many questions

**[13:19](https://www.youtube.com/watch?v=UpwAj792WvI&t=799s)** about yeah, about the person, about I can bring up some ideas about the person I could you could enter other documents there with personal data. So where did you define a purpose to use it? Well, I mean the documentation is in the code. No. Because if it's in the code, you do not have a legal basis. You need a legal basis to Yeah, to handle the data and you need to define and document what you would like to do with the data. This needs to be in there. So what we have seen is not a purpose. That's the absence of purpose. So

**[14:12](https://www.youtube.com/watch?v=UpwAj792WvI&t=852s)** you own this deck. Your models run on your hardware. The data is processed within your network. And you still do not have a legal basis. Because GDPR requires purpose legal limitation. That means it needs to be defined why you use this data. You need to define with your stakeholders why you need to document data for example this particular personal data and you need to do this before Yeah, you do the actual coding with it. Well, but we've seen this so often over the last couple of days. Okay. So Yeah. So the reason is general ask

**[15:01](https://www.youtube.com/watch?v=UpwAj792WvI&t=901s)** anything chatbot has no no defined purpose limitation or by design so to say insert. Um So without a legal basis or without a defined purpose you you do not have a legal basis. So what do we do now? We can fix it. >> Can we? Uh do I have to fix it? >> You have to fix it and you can. And you can show uh in parallel how to do it. >> Um Okay. So, the whole point is there is a fix, but you need to bake this in. Um I'm going to just uh build in a little interface here, share share the points, see how you how how how we how we do this, and how then this would look.

**[15:49](https://www.youtube.com/watch?v=UpwAj792WvI&t=949s)** So, what do we have to do here? >> So, maybe I can guide a little bit through um the back end needs to route uh by use case. So, before you have the user, then you have the chat UI, then you have the LLM, and um any document. So, ask anything. What uh David wants to create here is um the picture afterwards. So, we have the user, we have the bot picker, we had and we have bot config, the LLM, and uh scope retrieval. Then you have purpose, you have uh the legal uh base, and you have a scope. So, that means actually real work, but it's a re-

**[16:37](https://www.youtube.com/watch?v=UpwAj792WvI&t=997s)** refactor, not a rebuild. And you build the platform, and what is missing is uh the governance layer. And this is what David um will show you in a in a bit. >> I'm working on it. Okay, so that's the this is this is kind of the point. So, instead of routing user to the chat UI to the LLM, then the document, and take it all in, we need to route this. >> Can you make it a little bit bigger? I think it's legible. >> Doesn't have to be perfect. You get Yeah. Um so, I'll cheat here for time. No, I can't. Ah! Um

**[17:24](https://www.youtube.com/watch?v=UpwAj792WvI&t=1044s)** Okay. So, point is this is an interface on on the code side now to do this, but um again, this is not code documentation. So, we've been harping on the legal base now. The legal base here for our interface is just an attribute that we will pick uh pick up in a moment. But, maybe you can give me two or three more sentences on how you get to that legal base in a in a in a real-life company and not on stage. >> To a legal base, yeah, you need to um so, what is we we are talking about the purpose, right? At the moment, there are many many other Okay, at there are not so much or many topics um from GDPR, but if you want that are really important. And uh we are concentrating uh today on purpose. And you need before you um

**[18:13](https://www.youtube.com/watch?v=UpwAj792WvI&t=1093s)** >> [sighs] >> when you when you have um yeah, an interview, for example, and you have um um yeah, the the resume of someone or um what is it called? It's the >> Sorry? >> The interview uh sorry. I I I will come to whatever you have, and you have a document where there's a name on it, an email address, some personal data, yeah? Uh you need to define what you want to do with it. So, there needs to be a purpose. Um just people that are um that need to deal with this um uh kind of sheet, for example, or document has to uh need to get access. So, you need to store it separately. Um then you need to make sure that you delete the data afterwards, for example.

**[19:02](https://www.youtube.com/watch?v=UpwAj792WvI&t=1142s)** So, this is um something you need to define prior. And this is what you do usually within an enterprise, or you should do, to define what do you want to do with a personal data and yeah, have restricted handling of those. And this is [snorts] what David wants to show within the coding that there are some regularities where you can create a legal basis for the purpose. And there are some more other details for other GDPR topics, of course, but as mentioned we focus on GDPR. So, and what David shows here I have I've seen it somewhere was he

**[19:51](https://www.youtube.com/watch?v=UpwAj792WvI&t=1191s)** implemented legal basis. And this field legal basis, this is what the data privacy officer for example wants to see. This is what an auditor wants to see. The auditor does not want to see the whole code. He just wants to see or he or she wants to see that yeah. There is um that there is a regular regularity or a regulament within your coding. >> Yeah, sorry. I made a mistake and I'm having brain freeze. I can't fix it, but I think you get my point. >> [laughter] >> Or mine. >> No, no, no, no. So, thank you so much. >> Yeah. >> Um We'll implement this in a second. >> Yeah. Could you um

**[20:38](https://www.youtube.com/watch?v=UpwAj792WvI&t=1238s)** solve the the issue? >> No, but you know what? I'm I'm I'm chickening out now. I'm I know the I can fix it in 30-40 seconds. >> Okay. That's good. >> So, this is kind of what what what Julia talked about. Thank you. Sorry, I was so unresponsive, but the others watched me fail. If you bake it in in in code in front in business process, you're good. It's it might sound like a like a big hassle before. Ultimately, it's easier to fix first. If you bake it in, talk with the people, and so forth. But even if you haven't, it's solvable. >> Yeah, and I think that's a good thing,

**[21:25](https://www.youtube.com/watch?v=UpwAj792WvI&t=1285s)** right? Because whenever someone hears about GDPR, usually it's like, "Okay, hmm. Yeah, we need to do something." And everybody is using chatbots at the moment, so it's really necessary to think about that there is actually legal basis that everyone of us needs to fulfill if we're handling data. >> Okay, small mistake. Let's see if this works anyways. Okay.

**[22:37](https://www.youtube.com/watch?v=UpwAj792WvI&t=1357s)** So, let's see if I can get this done in the next 6 seconds. So, I I already saw the correct answer in the background as I think you saw you saw if you could if you could read it. Um but this would then be the technical fix. And with this it should then look something like this. So, now we have our same interface but with a layer on top where you can pick. I mean, this is what I did here now is a purely technical solution and not sufficient as we've talked about this. Usually we'll need internal processes. But just by having a documented use case and already

**[23:27](https://www.youtube.com/watch?v=UpwAj792WvI&t=1407s)** you know, you would probably give the user a little more interface of you know, what are you what are you allowed to put in here? Why? What is it for? What shouldn't you put in here? But that will already help you on the technical side tremendously to make sure you are on target. And this is not an AI problem. I'm not I I think you probably said this. Let me repeat it. This is a data processing issue. It becomes amplified with AI in my opinion with all that we've seen. But this is a boring 10-year-old GDPR challenge. Let's call it a challenge. Um so this was me dabbling around here a little bit needing the needing the LLM to fix uh uh a simple variable. Potentially yours is in

**[24:14](https://www.youtube.com/watch?v=UpwAj792WvI&t=1454s)** production. Um doable, fixable, but needs fix needs >> to be fixed. >> To be fixed a second eye. However, you want to look at this. Thank you so much. Thanks for jumping in. >> You're [laughter] welcome. Thanks. >> [applause] >> Uh thank you so much. Uh David and you there for the awesome presentation. >> Sorry. >> And can Can you hear me? >> Yeah. >> Barely. Perfect. We're fine. Thank you so much David and Yury for the awesome presentation.

**[25:01](https://www.youtube.com/watch?v=UpwAj792WvI&t=1501s)** >> Thank you. >> And I think we have a few minutes. So, we do not have any question from the audience, but I do have some. >> Yeah. >> So, maybe I would like to understand So, it really looked pretty simple to me. I think we just added a tiny bit of code there with a somewhat understanding that it had a legal basis statement to it. Is it that simple? Are there other specifications which one needs to extend upon? >> Mhm. Need and should. Um for that's the nice thing as a developer in this in this instance, it could be that simple. Um you usually have a lot more process in front to define this legal base. It is not what I just put in there

**[25:50](https://www.youtube.com/watch?v=UpwAj792WvI&t=1550s)** just to get something in the string field. That's not sufficient. It'll need a documented process. It'll need some sort of legal or expert or data protection officer or whatever sign-off or analysis to actually tell you what to go in there. Depending on your use case and the potential data you put in there, you might need more. Sometimes a pure organizational demand of dear user, please don't put HR data in here might not be enough, especially when when you deal with um with sensitive data or any of that sort. Then you will need more, but that's procedural and maybe technical. Depends on the case. >> Thank you. If I write that bit of code does it also impact the large language

**[26:39](https://www.youtube.com/watch?v=UpwAj792WvI&t=1599s)** model? Does it also understand that in terms of developing newer code? >> So, for us it didn't cuz I was lazy, but it should. Um you should make very clear to the large language model, you know, what is the context that you're operating in for quality reasons and for compliance reasons. I just said, give me a cheeky answer. So. Thank you. >> Does some of these, uh, you know, use case specific like the legal constraint need to be communicated to the user who is operating through the chat? >> Mhm. Absolutely. Sorry, I'm being so rude, but >> [laughter] >> Yes, you need to show it. So, in here it was a one-liner. All right, sorry off. Uh, it was a one-liner, you know, what you need a more you more you need to be more descriptive and you need to somehow

**[27:25](https://www.youtube.com/watch?v=UpwAj792WvI&t=1645s)** ensure the user understands the contact that he's operating in. So, he doesn't accidentally think I, you know, use the, what was it, the vendor analyzer to upload, um, CVs from, uh, applicants. So, you need to be very explicit and usually, depending on the data and on the risk, you need to document that consent. So, you need to tell the user and you need to know that you told the user and you need to know that the user acknowledges this and knows this. >> Understood. Thank you. Uh, just a last question. So, I understand many here, you know, could be potential freelancer, startups, etc. Where do they go from here to understand this process? Is there a documentation or specification which says for GDPR specific we need to

**[28:13](https://www.youtube.com/watch?v=UpwAj792WvI&t=1693s)** do this, you know? >> Uh, give me a call. Um, no, but there's there's lots of resources out there. Um, especially on the GDPR stuff, you you can find good stuff. If you're uncertain, I mean, we as Compliancy obviously do this as a business, but there's also other agencies out there who who've started to specialize in this. Um, take take what you can from, uh, publishers like a lot of lawyers, data protection officers, they have uh, they have good stuff on their website. That's good to understand and that will already give you get you a lot of the way there, and then um, um if you're a freelancer working for clients, the clients should usually have strong opinions. >> Understood. Um I think we are very close to the end

**[29:01](https://www.youtube.com/watch?v=UpwAj792WvI&t=1741s)** of the session. Uh I would like to thank Julia and David for this awesome presentation, and I hope you all enjoyed it. Let's have a uh one round of applause for them. You know?
