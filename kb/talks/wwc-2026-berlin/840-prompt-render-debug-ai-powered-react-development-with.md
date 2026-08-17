---
id: 840
title: "Prompt, Render, Debug: AI-Powered React Development with Chrome DevTools"
slug: prompt-render-debug-ai-powered-react-development-with
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Keynote/Talk"
stage: "Stage 5"
tags: ["AI Coding Assistants", "AI Standards", "Edge AI", "React"]
speakers: ["Suchitra Swain"]
speaker_companies: ["Delivery Hero"]
day: 2
starts_at: 2026-07-10T07:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=Cmj9StnAF28
video_id: Cmj9StnAF28
session_page: https://app.wearedevelopers.com/events/16/session/840
transcript: true
---

# Prompt, Render, Debug: AI-Powered React Development with Chrome DevTools

**Suchitra Swain (Senior Frontend Engineer — Delivery Hero)**

`Track: Frontend, Web & Mobile` · `Type: Keynote/Talk` · `Stage: Stage 5`

`#AI Coding Assistants` `#AI Standards` `#Edge AI` `#React`

[Watch the recording](https://www.youtube.com/watch?v=Cmj9StnAF28) · [Session page](https://app.wearedevelopers.com/events/16/session/840)

## Abstract

A live walkthrough of the modern React workflow — from AI-generated UI to a running app, then debugging and optimizing it with Chrome DevTools MCP. See how agents scaffold components, interact with real Chrome, and inspect runtime behavior instead of guessing from static code.
WebMCP is a proposed web standard that lets websites expose specialized tools (search, book, filter, etc.) directly to visiting AI agents. With experimental Chrome support, you can debug those tools in DevTools → Application → WebMCP — list registered tools, watch live agent calls, and inspect inputs and results.

## Speakers

### Suchitra Swain

*Senior Frontend Engineer — Delivery Hero*

I’m a frontend engineer with over five years of experience in building scalable, user-focused web applications. For the past 2.5 years, I’ve been working at Delivery Hero in Berlin, developing modern, high-performance interfaces using React, Next.js, and TypeScript.

My journey includes impactful work with Adevinta (mobile.de) and SUSTLabs – IIT Bombay, where I contributed to projects in blockchain, energy informatics, and e-commerce. I’ve published research with ACM e-Energy and explored AR-based ideation tools at IDC School of Design, IIT Bombay.

I’m passionate about creating clean, accessible interfaces and integrating design with sustainability and innovation. I’ve attended Google I/O Connect in 2024 and 2025, staying connected to the evolving developer ecosystem and the latest in web technologies.

## Transcript

*3,146 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=Cmj9StnAF28&t=3s)** Hello everyone and I'm Suja Swai work as a senior software engineer and a fullstack web developer based here in Berlin. So today I will talk about prompt render and debug. So what about prompt render and debug? It's a workflow of react. We just write something render something but we fail to debug it. Because in the last few years from my personal experience what I felt is AI is everywhere. AI is faster for the front- end development and for the backend development and many more. But what it fails is debugging. Debugging didn't quite actually

**[0:53](https://www.youtube.com/watch?v=Cmj9StnAF28&t=53s)** adopt it very fast. We were so so slow about the debugging stuff. Today I will talk about how we can debug. You write a code, you have your AI thing, you have your own code, you still have your own code with yourself, but the lacking is debugging. How you can debug your own generated AI code. So today I will talk about how you can debug with the help of DevTool MCP. What is DevTool MCP? Dev Tool MCP is open-source MCP which actually access your runtime browser. It opens your page, inspect the uh input

**[1:43](https://www.youtube.com/watch?v=Cmj9StnAF28&t=103s)** uh automation, emulations, debug, performance, Lightroom and many more. From my personal experience, I know I am from the era where I had to write all the code by myself. But when I talk about today, the front end is like very very very very fast right now with the help of AI. But I fail in a debugging. I still need to sick with a external QA engineer to find my performance to ex to test my own application. But now I think with the help of dev tool MCP I'm more to be a one-man army. I can write my code, I can write my prompt, I can render and debug

**[2:34](https://www.youtube.com/watch?v=Cmj9StnAF28&t=154s)** many more. So in the next slide I will show you the feature we have in the dev tools. It's a input automation, navigations, emulations, performance, network and debugging. If I talk about the input automation, it's like if you have a pre uh defined form or something, you can actually without having a mock data, you can test your own AI with the help of AI. You can test your form navigation. You can just ask your AI agent to navigate from one page to another page. But we talk about the emulation. Emulation is one of my favorite topic because being a front-end developer I work with a different

**[3:23](https://www.youtube.com/watch?v=Cmj9StnAF28&t=203s)** location, view ports and many more. Performance and debugging is also one of my favorite topic. So in the next slide I will walk through how we can actually connect our MCP with the chrome. you either you are using uh cursor or VS code or claude or any kind of CLI you have to import your config file and have this J JSON ready. You can see you can have your JSON ready uh Chrome web tools and you can give any kind of option you are ready with. But to access this config, you have to enable your remote debugging. So how you can enable your remote debugging? You

**[4:12](https://www.youtube.com/watch?v=Cmj9StnAF28&t=252s)** actually have to go to the Chrome inspect and remote debugging. You have to enable it and restart your browser and your browser will actually have a local access. Whatever you are running, it will be on a local access. So your agent is actually having a access to your browser in a real time. You don't have to mock any data. Secondly, then you have lot of config options ready. If I talk about the autoconnect, autoconnect is like if your browser is already running and you are giving your AI agent that I need to access my page, it will connect with your realtime browser opened. But if you're saying like browser URL, it will open in a

**[5:00](https://www.youtube.com/watch?v=Cmj9StnAF28&t=300s)** specific port and I'm I know how I struggle with a web socket. I used to work a lot with the websocket. Now I don't have to struggle a lot to debug my websocket response and many more because we have like websocket endpoint, websocket headers and you can actually access very fast with that. and I can move ahead with the live demo. So here I was talking about the input automations. What is input automations? Like it's a it's kind of a game changer for the testers. I don't have to go with the tester to automate my form, validate my form whether the form is like email ID is validate, phone number is

**[5:51](https://www.youtube.com/watch?v=Cmj9StnAF28&t=351s)** validated with the country based or not. I don't have to write any playright code. I don't have to write any end to end test cases. I just have to write one prompt to my AI agent and everything is ready. So in the next slide I will show I just ask my agent to navigate to my registration form fill with some data and just connect with me to the realtime Chrome MCP. If you can see in this video, I just asked my agent to fill the data with my first name, last name, email id. It opened the chrome and started filling the form everything and initially I just asked

**[6:41](https://www.youtube.com/watch?v=Cmj9StnAF28&t=401s)** him like just with a positive thing. If you want with a negative data like okay if you find any fixes or any bugs you can fix it in the real time and you are all set. It will actually fix in the real time and give you the audit report in the actually real time and you can actually fix your bugs already. And the most next topic is my one of the uh favorite topic is working with the sensors and emulators because emulation is like where you can actually change your geolocations, change your network, change view ports and many more. And for me working with geoloccation is very favorite topic

**[7:30](https://www.youtube.com/watch?v=Cmj9StnAF28&t=450s)** because I work with a lot of website where I actually have to work on the different geoloccation different time zone and different currencies and many more. I don't have to change my entire desktop or laptop uh timing zone. So I just ask geo uh my sensor to put a geoloccation to certain uh coordinates and it will render my whole scenario. If I tell you how to enable it, it's like you can see in this location you can actually add all the location and I already have a pre-location ready because I work with Berlin, London, Moscow and other cities.

**[8:19](https://www.youtube.com/watch?v=Cmj9StnAF28&t=499s)** So I already have my location ready. If I'm accessing any website, I can set my geolocation and I can get a currencies or maybe like uh pricing languages change at the real time. I don't need to go to like any desktop changes or something. And here actually you can get your you can see here this is your port for the sensor where you can actually change your all uh location orientation and anything from here I can actually change whatever I have prefilled in my location you have ready here Berlin, London, Moscow whatever you want to change

**[9:09](https://www.youtube.com/watch?v=Cmj9StnAF28&t=549s)** in The next slide I will show a realtime demo where I just ask my cursor agent just to connect me with the Berlin store and then show me change my emulator to the Paris. It will actually change in a real time my graphical location from Berlin to the Paris. I changed my geol location to the Paris and now you can see I have a location ready for the Paris. For me as a software engineer where I came from the era where I has to write all my code debugging this stuff was a hard for me. But right now I feel like I can render the code with one prompt but I can actually debug and test it without

**[10:01](https://www.youtube.com/watch?v=Cmj9StnAF28&t=601s)** any external help. This is what I actually like about and next topic is about uh emulation of the view ports. So I'm like a crazy front-end developer, website developer and web application developer. For me it's matter what is being render on desktop or on mobile or on iPad. For me I'm very crazy like my website my own website is being rendered properly on phone or in desktop is proper. So I just ask my AI agent to audit it. What it did on the audit audit formation? It went to mobile then

**[10:51](https://www.youtube.com/watch?v=Cmj9StnAF28&t=651s)** desktop and then iPad. It's check whether my hamburg menu is working properly. I'm having all links available and in the desktop and the tab I'm getting proper navbar ready or not. If there is any issue my AI agent is giving me more information about it. I can show you a quick video of it. I just asked my um AI agent just to go to my portfolio run a responsive audit. It went to my portfolio. First it started opening in the iPhone 14 Pro. You can see the hamburg menu is there. My chrome is open. Hamburg menu is open. Now it shift to a iPad and then the desktop. I don't

**[11:40](https://www.youtube.com/watch?v=Cmj9StnAF28&t=700s)** have to do anything. It's like my AI agent is doing everything for me and it's giving a real time uh audit for me like okay your task is completed and your chrome is perfectly working my all the navbar either it's in the mobile iPad or in the desktop is working perfectly if I move forward it's like okay whatever You write with the help of AI, you still owe the code but you fail how it perform. How how is your website performing? How is your web application is performing? You fail it. Like for me as a user, I also fail. If I'm doing VIP

**[12:29](https://www.youtube.com/watch?v=Cmj9StnAF28&t=749s)** coding or something, I am coming up with a okay, I have built this website, I wipe coded, I can generate the revenue. But when it comes to a performance, we fail. When it comes to SEO, we fail just because we don't know how we can actually operate the performance tab. We are just one browser, one prompt and no type switching. So here what we can do, I I I can actually show you. We already have a uh Chrome Dev Tool MCP ready as a extension in a visual studio code which actually give you lot of tools to access your

**[13:18](https://www.youtube.com/watch?v=Cmj9StnAF28&t=798s)** websites or AI agent. For example, right now if you see in my um slide, I have like performance trace. It's nothing. It's just a tool present inside my dev tool MCP which actually gives me a authority to perform like I will just ask my AI agent perform a per just perform trace for me give me a audit real time summarize me what my website look like and actually he does and I just ask just go through my uh website open a code open my chrome in a real time and perform the uh trace and just give me the report and you can see I got a actually real report of my

**[14:10](https://www.youtube.com/watch?v=Cmj9StnAF28&t=850s)** website. I can see I didn't get any good points on the instruction of the next point but I got a good point on the LCP and CLC. So I I haven't done anything but you can see in my uh here in the chat agent I actually got a whole report a audit report like how actually I can improve my website performance. So it's like you just have to write one prompt and you will get the summarize and the whole audit of your websites. And I I actually like uh performance trace because for me it's helpful that I want my website on the top of the Google

**[14:59](https://www.youtube.com/watch?v=Cmj9StnAF28&t=899s)** search. If I'm searching myself, I want to be on top. So for that we talk about the lighthouse and the screenshot. If you guys know lighthouse is nothing but it's actually help you to improve your accessibility, best practices and SEO. Obviously everyone wants to improve their SEO website and everything. For me SEO was important because if I'm giving someone is like I am Su please search in the Google I want to be on the top. So my website has to be on the top and I don't need a manual access or manual person to do SEO for me. I just ask my prompt like please audit my uh portfolio and run the lighthouse audit

**[15:48](https://www.youtube.com/watch?v=Cmj9StnAF28&t=948s)** and give me the improvement and summarize audit of it. You can see in this video I just ask my AI agent prompted it connected to my chrome dev tool and it opened the dev tool. I can see my SEO is good. Now you can search me in a Google I can be on the top but my website is lacking on the performance accessibility and the best practices. So it will actually my AI agent have given me a full summarization of how I can actually edit or improve my whole website on terms of the best practices or on the performance basis. SEO is fine. We have talked a lot about dev tool MCP

**[16:40](https://www.youtube.com/watch?v=Cmj9StnAF28&t=1000s)** but next I'm going to talk about it's it's in the beta version but I'm very much uh curious about curious to show you is the web MCP web MCP I can say that it's actually actually a agent for the dev tools whatever you were asking your AI agent to do you don't have to do that. You already have your MCP ready on your Chrome dev tool. You just have to enable it. It's in the beta version. I have used it for me. If I'm going to my API responses and my API is failing. I want to see how it is, why it's failing, my payload is lagging or my console is failing, my HTML or have

**[17:32](https://www.youtube.com/watch?v=Cmj9StnAF28&t=1052s)** you seen uh React having this annoying uh console errors like oh you have to give the key prompt or something. You don't have to see like which file or something you have to you don't have to go to your static code and do it. you can actually do with the help of your MCP. So it's like a web standalone uh MCP where you can actually have your website ready and you just have to run the MCP. Your website will get scanned on the basis of if you want the performance or if you want the Lightroom or if you want to test whether my input um input automations or debugging is working properly or not.

**[18:22](https://www.youtube.com/watch?v=Cmj9StnAF28&t=1102s)** Then you can actually filter your MCP with the help of complete error cancel and in progress. If you have run your MCP and it's still in progress and you didn't got any data about it, you can actually get why it's stuck and where you can actually improve about it. And I can next I can give you how you can actually enable your web MCP. You just have to go to the flag and you just search for web MCP and you can actually restart your browser and you will have this MCP ready with

**[19:11](https://www.youtube.com/watch?v=Cmj9StnAF28&t=1151s)** you in uh in applications. You can see WebMCP is ready. So you just have to scan your whole website whatever you want to ask. And if you know we already have a AI agent present in our dev tool with the AI agent and with the web MCP you actually have to just prompt uh your normal language whatever you want to and everything will be summarized. Your website performance is not good. It will give you how you can improve it. If your Lightroom best SEO is not there, you can still do it. If you want to improve your automation without writing any playright code, end to end test cases. I don't want to I

**[20:01](https://www.youtube.com/watch?v=Cmj9StnAF28&t=1201s)** don't want to write any end test cases. You can actually do it. So, I think that's all from my side today. If you have any questions, I'm ready to answer. You can scan to connect me with LinkedIn and I am available after the session. You can connect with me. [applause] Thank you so much for your presentation. We have a couple of questions also welcome to answer after the session. >> Uh so I will read a few of them. >> Yeah. Uh how does this compare to the claude chime plugin? >> Yeah. So as I told this is available whether you are using cursor VS code

**[20:50](https://www.youtube.com/watch?v=Cmj9StnAF28&t=1250s)** claude Gemini it's like you are giving your chrome access to your AI agent any AI agent you use it it's real time using your Chrome it's like I'm giving a remote access to access my Chrome whether what I have opened my WhatsApp just access my WhatsApp that's all >> yes uh is the MCP be uh specifically for Google Chrome or can it be used in other Chromium browsers? >> I actually I I uh it's a good question because uh when I was demoing with uh my presentation with my friend, I got the same question and actually it's present in the Firefox and Safari. You actually have to give command. You have to connect with the Chrome or Safari or

**[21:38](https://www.youtube.com/watch?v=Cmj9StnAF28&t=1298s)** with the Firefox. You can actually use this MCP. You can it's it's a global thing any browser it's all ready >> great um and another question uh has it improved token consumption >> sorry >> has it improved token consumption the MCP >> uh no I I would say no because I actually have spent 10 15 minutes to record a one video so my cloud token consumption is too high I would say like AI is working perfectly but if you have unlimited token things you are good >> clear um and um can you recommend any tools for evaluationdriven development for agent and skill evaluation?

**[22:28](https://www.youtube.com/watch?v=Cmj9StnAF28&t=1348s)** Yeah, like as I told you just have to install the MCP on your cursor or VS code. You have all the tools available per for performance for Lightroom and any other things. If you want to like do the input automations, it's all ready. You just have to install your extension. >> Sounds like a good start. And then the last question, does it replace the playright tool calling for? >> Exactly. For me it's completely replace the playright because I don't have to write any single code for my form submission my web application or something for me it's a game changer for the tester I don't have to go to the tester to automate my website like I will be like okay I can do for myself

**[23:19](https://www.youtube.com/watch?v=Cmj9StnAF28&t=1399s)** >> that's a great answer thank you so much for answering >> [applause]
