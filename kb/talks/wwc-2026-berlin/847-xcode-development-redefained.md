---
id: 847
title: "Xcode development redefAIned"
slug: xcode-development-redefained
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Keynote/Talk"
stage: "Stage 12"
tags: ["AI Coding Assistants", "Code Generation", "Generative AI (GenAI)", "iOS", "Objective-C", "Productivity", "Swift", "XCode"]
speakers: ["MIlan Todorović"]
speaker_companies: ["Crossover"]
day: 2
starts_at: 2026-07-10T07:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=4MGmd8YQR9A
video_id: 4MGmd8YQR9A
session_page: https://app.wearedevelopers.com/events/16/session/847
transcript: true
---

# Xcode development redefAIned

**MIlan Todorović (Apple Certified Trainer — Crossover)**

`Track: Frontend, Web & Mobile` · `Type: Keynote/Talk` · `Stage: Stage 12`

`#AI Coding Assistants` `#Code Generation` `#Generative AI (GenAI)` `#iOS` `#Objective-C` `#Productivity` `#Swift` `#XCode`

[Watch the recording](https://www.youtube.com/watch?v=4MGmd8YQR9A) · [Session page](https://app.wearedevelopers.com/events/16/session/847)

## Abstract

Xcode development redefAIned: The Impact of Generative AI on iOS Development

The landscape of iOS engineering is undergoing a fundamental shift. With the integration of Generative AI directly into the developer workflow, the focus is moving from manual syntax construction to high-level architectural orchestration. This session explores how AI-driven tools are redefining the standards of productivity, code quality, and app performance within the Apple ecosystem.

To demonstrate the practical power of these technologies, this session features a comprehensive live coding demonstration. We will build a complete, non-trivial iOS application from scratch, showcasing how Generative AI can be leveraged in real-time to handle complex logic, UI architecture, and data management.

Key topics include:

Live Application Synthesis: Building a functional, non-trivial app from a blank slate to a finished product using AI-assisted workflows.

Accelerated Development Cycles: How AI reduces boilerplate code and streamlines SwiftUI implementation during the live build.

Privacy-First AI: Navigating Apple’s unique approach to integrating intelligence while maintaining strict data security.

The Evolving Role of the Developer: Moving from manual coding to validating and refining AI-generated logic in a high-pressure environment.

Automated Testing: Utilizing generative tools to instantly produce robust unit tests for our newly created features.

Attendees will witness firsthand how these tools are not just for simple automation, but catalysts for a new era of software craftsmanship. This session provides a roadmap and a real-world proof of concept for staying ahead in an increasingly AI-centric development environment.

## Speakers

### MIlan Todorović

*Apple Certified Trainer — Crossover*

Milan Todorović is an Apple Certified Trainer, Consultant, and Software Engineer with decades of experience in high-level developer training. A Swift expert since its inception, he serves as an associate lecturer at the Apple Authorized Training Centre in Serbia, specializing in machine learning, AR, and advanced software architecture.

With a background in Electrical Engineering, Milan has a long history of IT leadership, including heading Borland’s regional office (2001–2010). Since becoming a certified Apple trainer in 2017, he has been a regular speaker at the WeAreDevelopers world congresses in Vienna and Berlin, focusing on ML and IT education methodology.

As a consultant for major European companies and founder of Edulibris (Estonia), Milan currently focuses on leading engineering teams using advanced ALM techniques. His unique approach combines deep technical mentorship with real-world project delivery to solve the global talent shortage in high-end software engineering.

## Transcript

*3,649 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=0s)** Welcome back to the we are developer uh congress 2026 and we are with our next speaker uh Milan Toodorovich. I apologize if the pronunciation is not perfect. Uh Milan is a regular speaker at the we are developers world congress. uh he spoke in Vienna in Berlin and he focuses uh often on um machine learning and IT education uh methodology. He's a certified uh Apple trainer, a consultant and a software engineer. Um and he's also the founder of his own company Edu Libris um focusing on leading engineering teams using advanced application life cycle management techniques. Today he will talk about its code development. Um and uh he will focus on generative AI on iOS development and on how AIdriven tools are defining or redefining the standard of productivity, code quality and app performance in the Apple ecosystem. I

**[1:13](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=73s)** remind you you can submit your question through the uh congress app. uh please respect respect our code of conduct and at the end we will try to um answer one or two question uh hopefully we will have time um welcome to the stage Milan thank you >> thank you hi I'm really happy to see you again I was here for many times first to mention that this is not a typo this is by intention because we are talking about uh AI we are talking about u uh up u iOS application development using programming language swift and uh generally it's not only about swift it is about uh practically a lot of other

**[2:14](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=134s)** technologies but at this very moment we are focused strictly to iOS development and Xcode using Xcode as a as a tool as uh mentioned uh I'm u tightly ly connected with Apple. I am uh most of time trainer for app development with programming language swift swift and this is the reason why this all will be about Xcode swift and the iOS applications. Let's go on. So uh for many years um we spoke about uh adding AI in our applications. So we are making application we are using some u form of of AI. Uh but now actually we have a uh another approach. It's about using AI to create applications. So we are talking about two two flows uh two shifts and within one one context. Uh just to mention uh that of course this is not my first time that uh I talk

**[3:31](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=211s)** about AI on VR developers events. uh uh if you take a look to this uh red listed uh items, it is about my presentations from this point uh within the last few years and you can see that is uh mostly about using AI. Uh now for the first time this is about uh using AI for development. Uh it's [laughter] it's funny. I spent the whole career as a developer but now I it looks like I'm doing something against this uh uh this occupation. So uh but it is actually it is not like this. It is about making things things better. But uh as I mentioned this is all about adding uh adding uh feature AI features in our applications about uh uh first was in 2018 Vienna about uh image classification then about hand moves

**[4:44](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=284s)** recognition uh body and hand pose with using vision framework and uh and so on. uh as I mentioned we are talking now now about uh building applications and about AI that lives in our applications uh I will not go too too deeply within this but as needed. So in next uh 20 minutes 20 minutes we will say a few words about the whole landscape about uh uh I will create u one application live here from scratch uh using AI of course uh and um uh we will then demonstrate how does it works on the device and uh finally we will u do the honest part. I will try to get the answers to questions with which uh target this topic honestly because you know all of you know that

**[5:54](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=354s)** there is a big u big story about using AI and we need to be honest. We need to say the truth what it can what it cannot. Uh Xcode now is in major version 2026. When 20 when Xcode 26 has been introduced, it had the so-called assistant starting from version 26.3. It became so to say so to speak the colleague. It became the partner of coding. you as developer, you have a partner uh right now. Okay. Uh I have some explanations here and uh as I mentioned I will let me take a look. Okay. I have plenty of time now. Uh but uh you can read this but this and this is important. Um before 26.3 the general loop of developers working was you you set the goal then you get the suggestions from the system from the

**[7:08](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=428s)** machine you accept it or you do not accept it but if you accept it then you build it you read if there are any errors and then you paste it back you come back here and here and so on. So the mainly it was about suggestions not about actions not about doing things. Uh so you as developer you were the loop you was the one okay paste click paste click check paste click check error yes no and so on. Now it is a little bit different. Now Xcode has agents who can do job for us. Now it's you again have a goal then you have a plan okay then you edit the plan you build it actually the machine build builds it for us are there any error the machine will fix it agents

**[8:20](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=500s)** will fix it we'll verify and job is done the whole loop will be done uh within the Xcode so uh maybe in a few minutes I will go back to those two lines. Let's go on. Uh we talk about agentic development. So few agents many agents work work for us. Uh they read the project, they read the docs for us. Okay. analyzing project reading the docs to collect the necessary knowledge required for development. They configure everything. Libraries, frameworks, so on. Tools, tool sets, uh, agents build, agents verify, agents iterate. I'm not the loop again. Okay, I'm just someone who is watching and who has the project. Okay. [sighs] uh in Xcode it's not required that you use only Apple's tools only Apple's models Xcode is open for other other model uh mod

**[9:31](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=571s)** models like clot like uh CH GPT codeex like geminy and other of additionally Xcode supports MCP so you can use practically any other language model if you use and set properly some MCP server. So uh it can be expanded as as necessary. You're not stuck into the Xcode like it is. Uh so let's talk just a little bit about settings. I will demonstrate. I will show you actually here in Xcode. Xcode and settings. Okay. So the main um the main option is intelligence. So here is how do you set you set you can set code [snorts] agent you set can set codex you can set geminy you can add additional agent anyone as I mentioned before just by setting uh [sighs] where is the exactible file on your on your machine and of course

**[10:44](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=644s)** set the proper parameters required by by model. Okay. Of course, it is not necessary that we go through this deep deeply. Uh I already set cloud agent because u to be honest mostly we developers use use cloud. I'm using cloud mostly uh not only cloud from my personal suggestion it is good to use different models. try you need to make some uh some exploration. I suggest you to do some exploration but at this moment we will demonstrate how do you work it with clot. I have of course my account and everything has been set properly. I've been signed in and I choose cloud agent as I mentioned.

**[11:42](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=702s)** Okay. Uh first let me demonstrate how we can check if we have the the model. I will use playground Xcode playground as it as usual and uh I will start a new project. So new project iOS app. So uh foundation model check. Okay. So let's go somewhere. This better let maybe here. Okay. Okay. You see what I used including cobble. Okay. It's just for for uh for fun. But here is swift what's interested with us. And so 2026 we are developers and uh I already set a name for the project and I now I'm creating it. Okay. So this is the standard uh view of Xcode. some boilerplate code. Let's go further. I have uh prepared this one small code which will first list if system see some language model uh what is the availability then it will

**[12:56](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=776s)** instantiate and will do some some small some small job for us. So I will copy this and put to the to here to the code. Okay. So I just copied it here. You will see what's the execution. Okay. Uh so uh oops [laughter] it's some error of Xcode. I don't know if it will produce some uh problems further. Let's see. But okay. Uh it's obvious that we started the session, we get a date and we said prompt. So say hello in three words. Uh what we use here we use foundation model which is incorporated uh in practically every application like this. It is small model only three billions parameters and uh it's uh been

**[13:58](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=838s)** using for uh some let's say middle middle layer and it's been used uh on the on the device uh because Apple forces the approach without uh calling um some services outside if it is not necessary. It is all about security. It's about permissions. It is about keeping data on on your your device. But uh take a look here. Okay, we told them say hello in three words. We said the prompt. He answered hi. Hello there. How can I assist you today? Uh okay. What's what's wrong here? Say hello in three words. He answered in five, six, seven. I don't know. Okay. The main question is how to require something from our model.

**[14:59](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=899s)** We need something. We require something. We need help from the model. But uh we cannot let model hallucinate or give us some answers we uh cannot use further. Okay. Uh so how to solve this? Let me show you. We will change it a little bit. And now first I will paste this code down there. Then I will change everything. So uh the input is practically the same input zone. Okay. But now we have this content view. It is here. But in this code we have this part. We have this annotation generable. Okay. Where we define okay of course at this very moment the source is not uh not doing well but we require a

**[16:01](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=961s)** guide. [snorts] We give the guide to the model with description exactly three words. This is the place where we set our constraints. And then um after that in further execution we have uh just to demonstrate so to say loose call and the strict call without constraints and with constraints and what actually we get in the execution time. With lose, we require three words. The model responds with some text. But in strict mode, we got exactly three words. Hello world again. Okay, this is very simple uh very simple demonstration but this is the exactly the way how we can set much more complex constraints. Okay. And let's see how it it works on real in real thing. Now we will make a blank project. We will set it to the minimum

**[17:11](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1031s)** deployment to iOS 26. Pick up simulator. open the assistant and give the prompt to the Xcode to create the whole application for for us. Uh it looks like this. I will close this previous and uh I'm about oops this is not what I wanted. This is the project. It's again iOS. It's again application. And now I will check it [snorts] flashc card. What are flashc cards? Uh I will make application where we can set any text and the application will create questions from do that text based on the paragraphs with uh with truth. Yeah. Well, and it will uh give us the flash cards with answers to to those questions. Pretty useful. I'm sure you agree. Okay. And here it is. So here, this is the empty code. Standard empty code. If I start

**[18:23](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1103s)** it, it looks like this. Okay, pretty much standard. And now and now the magic. Okay. Uh this is the option which is the most important. So this is the conversation where we can choose that we use cloud agent agent or codex or geminy or something else. And here is my prompt. How does it looks like? Build an iOS app. We call it flash cards. He already knows what does it mean flash cards. It keeps a lot of information already. Uh it will be on one screen with the text editor. Very simple. It will use foundation models with framework. Okay. Just to mention this corals. So cloud corals. Uh later I will give you the link to this presentation. You can take it on and use it in any way you want.

**[19:34](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1174s)** Okay. Um uh I do not go too deep because we have time uh uh we have 20 25 minutes of time. Uh so these are suggestions within the prompt and let me show you how does it work. So I will copy this. Okay it's prompt like any other prompt. Let's go here. Let's paste it here. Okay. and I press enter it starts working. I don't know it will take three minutes maybe four maybe plus or minus you uh will be able to read here how does it what is it doing okay in background but when this process is on ongoing uh let's read a little bit about what

**[20:33](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1233s)** agents are doing first thinking explanation user wants to build a new iOS app called flashcards using this and that using foundation models network. You see small links with prompt. Okay. Flash cards foundation model and similar things. Okay. Uh now it continues. It's uh reading documentation. Okay. language model session part generated actually he's identifying what information is he looking he's looking for some documentation where he's looking for uh uh explanation how to do things and he found it so you can see this here so he's now thinking and thinking but important is that now I have enough information to write the complete content view And now he is planning the implementation. Okay. Uh to be honest, I'm I hope uh it will finish this [laughter] properly. Okay. I know I need to be honest, you

**[21:45](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1305s)** know. I [laughter] told you. But okay, I checked this for for really plenty of times and yesterday I did it maybe five, six times. Yeah. [laughter] Okay. So, I'm an optimist. It still works, but okay. It's no no reason to worry yet. Okay. Um, now wait. Now we are waiting. [laughter] Okay. [snorts] >> Okay. Prepare questions. Yes. How many? >> Wait. Maybe we can answer this question. >> Yes, please. Uh, can you can you need to to read this or or let me take my glasses? Okay, >> I I can read it. >> Okay, sure. Sure, sure, sure, sure, sure. Let me just uh let it here. Good. Okay, it's still working. >> In guide, you [clears throat] add two par two parameters. Second one being dot constant. How do you constrain it

**[22:57](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1377s)** specifically to number of words? >> Uh ahuh. Okay. uh it is about uh it it is about about uh about the guide uh so I don't want to to now to to change the uh but uh uh okay I will answer like this in documentation there is a very specific place where you require uh array with exact [snorts] numbers of of of uh of what what is the exact count Okay. Um uh later I can I can demonstrate something like this. In the meantime things changed on the screen. [laughter] Okay. Because uh agents uh a agents did did the work properly and you see it is the standard swift code. Now he's finishing. It's not finished yet, but it will be soon because he's building the project

**[24:05](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1445s)** and some description what it is inside. And I'm about to start the application. You see those are flashcards and let us check. I prepared some uh some text. Okay, here it is. Okay. And so you see this is a text about foundation model is applus framework for the ondevice language model and so on and so on and I say generate. Okay. The application is generating the flash cards. Here are flash cards. Okay. So what is the foundation model in applas framework? Foundation model then explanation what it is. Okay. Second flash card and so on. Okay. Let us check with some other text. Okay. And now flash cards are coming as synchronously as the system finishes its uh its work. Okay. So, so here it is. Yes. Okay. Um let's go

**[25:15](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1515s)** let's go one step back. Uh actually practically only three parts did the key uh did the key uh they uh uh it's this part with generable uh the second part is this where we instantiate the language model session and uh the third one is where we actually are uh uh calling this uh this this model to do some uh some work uh we call it asynchronously using triate. Okay. In this moment we cannot go deeply with of course to explain it. Okay. So uh do we have uh other questions? Yes. >> One more. >> Yeah. Yes. >> Because I have some some questions prepared uh with answers but okay please

**[26:15](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1575s)** be be open. >> So let's do one more question. >> Yeah. We have Zakaria asking uh so you prefer using cloud code integrated in in Xcode or the particular app cloud code. Is there a difference? >> Uh yes uh I use cloud code generally for uh many many things uh because sometimes uh we need uh to complete back end or something like that. uh this is the uh situation when we use cloud code me personally but when it comes to the uh iOS application uh when it comes to Xcode it is better to incorporate it in Xcode because uh in this case Xcode is the loop you know Xcode is calling agent it is not about specific tool it is about the process and the whole process has been handled by Xcode >> one more we have

**[27:29](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1649s)** Um, is it possible to do text to actions from pro a prompt call uh the intents in the app? >> Um, can you repeat please because [laughter] I'm not sure. >> I also didn't understand exactly um so the question is is it possible to do text to actions from a prompt call? >> Oh yes it is. Yes. Yes it is. Yes it is. Yes. You can uh you can type uh if I understand. Okay. So uh clear the content view file. Okay. Then he's telling me something that is maybe not. So thinking user wants to content use file. Okay. But uh just delete. Okay. So it's uh I will see just delete it. Okay. Okay, it's empty now. Okay, it deleted it. So, okay. Uh you can I if I

**[28:39](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1719s)** understood the questions question well. But >> then one last uh question to close. Um do you have any tips for prototyping iOS app using AI for example, how do we guarantee that it follows uh Apple human interface guidelines? >> Um okay. So um I have a few tips. I can give few tips. Uh uh first do chunks uh small as possible. Do not take too big by otherwise you will have wipe coding because uh wipe coding is not uh word with nice which sounds nice but uh try to do it uh with smallest chunks possible because it is about quality. It is not about only about time. uh of course you will need some time to finish

**[29:43](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1783s)** the the thing but uh the main issue is quality. You need to deliver good thing. The machine will I in my personal opinion be never be will never be able to understand fully what does it mean uh quality required for a human being. We create applications for human beings not for other machines. >> [gasps] >> Uh so uh um follow guidelines you know [laughter] you can you can find it everywhere you can find on Apple site uh a lot of a lot of them um I uh okay I had some okay I had some questions and answers which covered this topics in this presentation you can uh scan this okay I created one

**[30:44](https://www.youtube.com/watch?v=4MGmd8YQR9A&t=1844s)** small repo which is accessible using this QR code. You can as I mentioned you can download it. You you have this presentation in full and you can click on all those corals which explains uh uh the things in depth uh what I couldn't do here. Okay hopefully. Okay. Thank you very much Milan for your presentation and if you have additional question I invite you to approach Milan now. Yes and uh in 10 minutes we will start with the next talk. Thank you very much. Thank you. Bye. >> Thank you patience [laughter] >> for so many years.
