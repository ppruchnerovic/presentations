---
id: 917
title: "Future of Mobile AI. What On-Device Intelligence Means for App Developers"
slug: future-of-mobile-ai-what-on-device-intelligence-means-for
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Keynote/Talk"
stage: "Stage 12"
tags: ["AI Models", "Agents", "Agentic AI", "Android", "iOS", "WebAssembly"]
speakers: ["Sasha Denisov"]
speaker_companies: ["Brainform.ai"]
day: 2
starts_at: 2026-07-10T10:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=nCeUgrWjBMo
video_id: nCeUgrWjBMo
session_page: https://app.wearedevelopers.com/events/16/session/917
transcript: true
---

# Future of Mobile AI. What On-Device Intelligence Means for App Developers

**Sasha Denisov (CTO and Co-founder — Brainform.ai)**

`Track: Frontend, Web & Mobile` · `Type: Keynote/Talk` · `Stage: Stage 12`

`#AI Models` `#Agents` `#Agentic AI` `#Android` `#iOS` `#WebAssembly`

[Watch the recording](https://www.youtube.com/watch?v=nCeUgrWjBMo) · [Session page](https://app.wearedevelopers.com/events/16/session/917)

## Abstract

Two years ago, adding AI to your app meant one thing: cloud APIs. You sent data to a server, waited for a response, paid per request, and hoped your users had good internet. Privacy? A terms-of-service checkbox.

That world is ending.

Today, you can run a large language model directly on a phone. No internet required. No per-request costs. Data never leaves the device. This isn't a research demo — it's production-ready technology that changes what's possible for app developers.

I built flutter_gemma, an open-source plugin that lets developers run AI  models like Gemma locally on iOS, Android, and Web. Through this work,  I've learned what on-device AI actually means in practice — not the marketing version, but the real tradeoffs, limitations, and opportunities.

In this talk, I'll share what I've discovered:

What's now possible — Running models like Gemma 3 on a smartphone. The hardware (NPU, Neural Engine) that makes it work. The formats (.task, .litertlm) that matter.

What changes for developers — New architectural patterns: offline-first AI, hybrid cloud/edge approaches. New decisions: which model size, which format, where to store gigabytes of weights. New skills: fine-tuning, conversion, optimization.

The honest tradeoffs — Not every phone can run every model. Smaller models are faster but less capable. Some support separate LoRA weights for easy updates, others require full model replacement. I'll explain what works where.

Where we're heading — Multimodal models (text + images) on device. Function calling — AI that controls your app. Personalization through on-device fine-tuning. Models designed specifically for edge, like Gemma 3n.

The future of mobile AI isn't about replacing cloud — it's about giving developers a new option. One that's private, fast, and works anywhere.

## Speakers

### Sasha Denisov

*CTO and Co-founder — Brainform.ai*

Sasha is CTO at Brainform.ai with over 20 years of experience architecting scalable enterprise systems. With a strong engineering background, his expertise spans frontend, backend, cloud infrastructure, mobile development, and AI — from cloud-based generative AI to on-device solutions. He specializes in building robust, production-ready products using a variety of technologies and frameworks. Sasha has delivered solutions across fintech, digital media, and entertainment. He is a Google Developer Expert for Cloud, AI, Firebase, Flutter, and Dart, co-organizes the Flutter Berlin Community, and is a recognized international speaker and writer, having presented at 30+ conferences worldwide.

## Transcript

*3,930 words · source: yt (en)*

**[0:00](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=0s)** Hello everybody. Welcome back to stage 12. Um happy Friday afternoon and hope you had some lunch today. Um yesterday we touched the edge of AI and today our next speaker is talking that conversation a little bit further. Two years ago mobile um AI meant slow cloud calls and m massive API calls. Today we're talking about running AI completely offline, fast, and privately on our smartphone. He's the CTO of Brainform AI, a Google developer expert and creator of the open-source plug-in Flutter Gemmer. Please give a massive weird developers applause to Sasha Denisov with his talk, Future of Mobile AI, what's on device intelligence means for app developers.

**[0:51](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=51s)** >> Hello. Hello. Uh hello everyone. Yeah, can you hear me? Well, yeah. Okay, good. So, nice to see you. Uh actually, yeah. Uh moderator uh mentioned that yesterday we already were talking about HA. Please plus raise your hand if you been yesterday on my talk on one, two, three. Yeah, nice. At least three uh three people. uh but you know probably the order could be better if this talk will be the first one and yesterday's will be second one because yesterday it was uh mostly demo. So I was uh showing how uh on device AI can be run and on device AI and on device uh

**[1:39](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=99s)** rack uh can work uh even on weak devices. I demonstrate how it works on smart glasses. Uh so you can if you missed it yesterday you will be able to watch it in recording or find me at the booth of quadrant and I can show you in person personally uh and today's talk it's you know more highlight overview where we are where we going uh and my vision of this direction actually one more interaction please raise your hand if you are mobile developer Yeah, me of course. Uh uh and if you uh like AI engineer or machine learning engineer. Mhm. Okay. Nice. So I think for both uh

**[2:31](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=151s)** of this engineering direction uh talk should be interesting. Uh so let's get started. Actually I prepared about 60 slides and I will try to put this in 30 minutes. So I will try to be fast. Uh first about who am I? So I'm CTO and co-ounder brand for AI. Uh but brain form AI it's not exactly related to ondevice AI. It's more about commercial AI and work for businesses. Uh so this uh talk is about more a little bit different direction that we work in Brai. Uh also I'm coorganizer of flatter Berlin community. We organizing events here in Berlin. So if you're interested in flatter always welcome to our events

**[3:19](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=199s)** and Google developer expert and flatter firebase and cloud AI. Uh if you don't know what does mean Google developer expert uh and interested what is this please ask me after or welcome to Google cloud booth uh here and we will explain what does mean there is code to my personal website so don't hesitate to follow uh there's link to link it in uh and to uh book a conversation with me so welcome okay uh in the beginning short kind of prologue that I usually add to any talk related to AI. Uh so let's get started. This is my favorite quote by Louis Carroll. I always had to do the

**[4:10](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=250s)** first one. Uh and uh read it. It takes all the running you can do to keep in the same place. If you want to get somewhere else, you must run at least twice as fast as that. So just think about it. It was more than one century ago, but it perfectly describes the situation around like AI engineering now and so on. You have to uh uh learn a lot just to just to stay relevant. But if you would like to grow up or read something, you have to learn as at least twice as fast as that. So loose girl uh yeah everything is evolving. Yeah AI is evolving. It was just predictive AI like 10 years ago then chat GPT came and

**[5:00](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=300s)** brought us generative AI and now we are here in era of agentic AI. So aentic AI it's next level of generative AI when we uh give our agents opportunity to interact with real world and do something for us. Uh so we also have to evolve. Uh so developer with expertise is much more powerful now than just developer who don't know how to utilize AI. uh and AI applications also evolving and become more and more complicated and more more have more and more capabilities and of course every business uh would love to utilize AI somehow and even sometimes doesn't matter what to do like let's

**[5:49](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=349s)** have this AI right [snorts] uh and sometimes uh businesses don't care about some nuances like uh also we need this AI power in our application Doesn't matter how and let's take charge GPT. No, let's take Gveni. Uh, and what about uh privacy? Uh, what about about the price about cloud bills? And what about connectivity? Ah, who cares? But yes, there is an answer on device. Uh, or we can name it different word HI. Uh, so what does mean HI? So hi when we are running AI exactly on device uh it can be mobile device smart watches I

**[6:37](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=397s)** know robots glasses laptops uh it means that AI running on your device not in the cloud uh and uh three things had to happen at once uh to make it possible uh models got small uh hardware got faster uh and run times that allow you to do it got major Let's go step by step about all of these things like models. Uh so if you take a look to this pipeline to this timeline uh models are getting smaller and more powerful in months. So like uh in April 26 it was Deepseek V4 in June it was Gemma 4 with multi token prediction uh size 1 GB and

**[7:27](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=447s)** very powerful uh and every month uh vendors with more like smaller models and with more amount of capabilities. Uh the second part architecture uh so not only uh transformers. So many businesses are thinking about how to optimize architecture of models uh to make them uh more capable for weak uh hardware and give them more capabilities. Yeah. like liquid AI uh like approach of Moya mixture of experts or uh spike AI so all this approach it's making different type of

**[8:16](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=496s)** architecture to give more capabilities models of big devices uh and what else hardware uh so HCI without hardware is nothing it's also a lot of progress there uh all new mobile devices, laptops already shipped with NPU and more powerful uh processor unit like last iPhone with a bionic last pixel with the tensor G5, Galaxy Snapdragon 8 and MacBook also with NPU. So, and NPU it's processor unit that specifically prepared for uh get maximum effect of uh AI thinking. Uh last but not least, frameworks. Paragraph is a software that allows you

**[9:05](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=545s)** to do this inference on device. Now it's actually the next level after hardware and runtimes and between uh runtimes and exactly your mobile application and frameworks also evolving. A lot of vendors working on this type of software that simplify uh your uh uh to to simplify how you can use it on your devices. So why this matters? Cloud AI you rent the power of AI on device everything in your hands. Uh so uh no vendor API your data state of the

**[9:53](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=593s)** your phone uh your rules no locking uh and for your user it's private by default free to run you don't have to pay for anything uh it works offline anywhere in airplane and mountains and basement deep forest et you have no latency related to network yeah because you get answer immediately. [snorts] Uh so on device but there are some biases about it. Uh how it works on device. First does on device mean isolated? No isolated uh uh only your inference your reasoning but you can give your models handles to go to network to

**[10:43](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=643s)** search I don't know like call tools whatever. Uh so you decide uh what stay on device and what you can take from uh anything uh anywhere else. Uh what else? uh there is a buy that mobile device can run only narrow ML not LLMs uh like image recognition gesture recognition something that you get answer fast but of course it's uh not true and your devices that you have now in pockets also uh contain this capability already um for example Apple intelligence in your iPhone Gemini Nano in your pixel uh Galaxy in your Samsung smart TV, smart watches already has

**[11:32](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=692s)** builtin AI models that you can utilize actually. But uh this is builtin models. What if uh you would like more freedom? Uh what if you'd like to use your own model, fine-tune it, do something? There's also an answer. Open models. Who knows what does mean open model? So open model it's kind of open source in the world. Uh so model with open wide uh you can download it do whatever you want with this model. Uh and there are just few uh like rules when should you use open models. So when you would like to decide your own where you would like to

**[12:20](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=740s)** run it uh uh when you don't want to send data anybody else and uh when you like to train the model with your own data for example and already a lot of open models probably you know all of them so you know llama quen mistral uh deepseek all of them open and my favorite gemma I'm Google developer expert. I work mostly with Google models. Uh if you haven't heard about Gemma, Gemma is a Google prepared open model. Uh for preparing this model that was used the same technology as Gemini but different approach of distribution and Google and community prepared a lot of different

**[13:07](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=787s)** options of Gemma already. For example, the most powerful one is Gemma 4 that was released the last one. Uh it's multi multimodel uh thinking reasoning model and the small the size of this model 1 GB you can run it on your mobile devices or for example function gema. Function gemma is a model with size like less than 300 megabytes. It's actually this stupid model in case if you would like to talk with it but it's prepared specifically to uh execute tools. So if you like to have agentic behavior, function gemma is really nice option for you. Diffusion gemma is a gema prepared with not transformer. It's a diffusion model. It's a kind of tradeoff uh between quality and speed. It's much faster than the regular gemma. Uh but

**[13:57](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=837s)** maybe sometimes not uh not for the same type of tasks. Translate gemma. Gemma for translation different languages. uh embedding gemma to generate embeddings. Uh med jammer gemma trained on medical data uh to solve specific medical tasks and even dolphin jammer uh gemma trained to understand a language of dolphins. So if you like to implement application that is with dolphins welcome you have model for it. Uh there is Gemma cookbook you can uh follow this QR code and uh there are Google repository with a lot of examples and approaches that you can read. Uh okay uh so where you can get models hugging face kegel github uh many source for it

**[14:48](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=888s)** uh but uh model is not enough we need a runtime to run the model. So let's imagine that model is a car like base model with big context model with fast inference model trained for specific purposes and no hard drives without driver right so and runtime is a driver so no runtime no inference and runtime runtimes is a one layer between frameworks and hardware and uh so there are a lot of different runtimes it already existed the open source runtimes vendor runtimes vendor doesn't mean that it's not open source it means that there is a vendor uh that work on this runtime for example lighter t it's

**[15:38](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=938s)** partially open sourced uh on an ex runtime it's open sourced but initially it was created by Microsoft or by Google and a lot of startups uh that specifically works on very effective runtimes for running model on device like cactus or pm and so Uh so how to choose proper runtime? Uh uh actually there is no framework how to choose from proper run time for you because it depends on your task on model you need uh on your environment. So there is no answer. Don't think that I recommend lighter tea. It depends on your purposes. It I generated this image with Gemini Nanda. Gemini Nana made by Google. Who knows maybe it's was the reason why this guy show lighter tea. uh but so it's everything depends on your purposes your goals and uh what

**[16:29](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=989s)** you really want to do [snorts] there is simplified option of framework so if you uh would like just to try and don't know real purposes so pick any runtime and try you don't like it try another one okay So frameworks frameworks it's usually built on top of runtimes. Uh one runtime can have many different frameworks on top of it like llama CPP has lama probably lm studio or llama react native on top of lighter there are lighter TLM or media pipe mit by Google on top of runtime transformerjs windows option. Uh so a lot of them all of them just simplified your access to this

**[17:19](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1039s)** runtime. You utilize this runtime with uh this framework. Uh I actually created one framework as well on top of another framework on top of lighter TLM. Uh it's a flatter gemma. If you work with flatter probably you have to try uh this framework. It's kind of ecosystem for flatter developers for building on device AI. It's included support of inference embedding on device rack everything. Uh and there are a lot of nice examples of this website. You can check it and even try how it works in browser. You can go through the site uh tap try it out and check in your browser how it works because uh it's not related only to mobile. It works in browser as well. It's flatter. Flatter supports mobile uh

**[18:07](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1087s)** web and desktop. Okay. So actually a lot of project already created with flatter gema. Uh you can uh they all of them open source. You can open and check the source code. Uh but on device it's still a tradeoff from some tasks. Yeah. Sometimes you need more complex reasoning uh and capabilities of your device uh doesn't doesn't give you such opportunities and devices are different. Yeah. Uh mobile is usually the the most weak laptop more powerful desktop more powerful but sometimes even this not enough and you still need a cloud power. Uh what to do in this case? Yeah. How to choose uh

**[19:00](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1140s)** reduce your wishes and stay on device or okay let's go to cloud and do on the device but why not both right uh so there is a answer hybrid approach so you can uh try hybrid and I use on device for ondevice uh on device task and and cloud for uh something that uh you can't do on device. For example, uh privacy uh uh priv for privacy purpose on device for offline on device uh and for from front just cloud if you have a huge context go to cloud and so on. Uh so hypert is actually just routing

**[19:51](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1191s)** uh uh you have to uh choose when uh you go where for example if tax complex enough go to cloud it's not complex stay on device uh or connectivity if you're offline you have no choice you stay on device uh or privacy you have sensitive data you stay on device there are few HMS how it usually works. You have a router in your application uh and uh this router decides uh by complexity, by privacy, by cost or by connectivity uh where should you go or another approach you have intent classifier and you classify by intent. So for this intent we stay on device for this type of

**[20:38](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1238s)** intent we have to go cloud. Our third approach uh cascading you try to solve your task on device uh and if it wasn't successful okay let's go to cloud u most complex approach and uh most time consuming yeah but so it depends depends what you're implementing uh so there are already few hybrid approach for example firebase by Google or cactus startup provides there is DK uh already solution uh Firebase AI logic for example from out of the box has solution uh uh cloud first or mobile first uh cloud first uh means if you have internet you go to cloud if you

**[21:26](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1286s)** have no internet you stay on device mobile first means you try on mobile you do you have builtin AI model uh utilize on device no built-in model go to cloud uh or gen kit by Google also give opportunity to implement routing yourself and work with the open models because it's much more flexible uh but actually uh hybrid is a more routing so everything uh is a routing there uh so final thoughts uh here so we came to era of edge AI engineering uh from my perspective. So before we had a machine learning engineers or mobile engineers, I I asked

**[22:17](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1337s)** Gemini Nano Nana banana to generate for me like all biases about this type of engineering. So so in HI engineering we need to utilize both of the directions. So if you're from uh that area you need to learn a little bit from here. If you from machine learning but would like to try something on edge AI, you need to uh learn a little bit mobile technologies. So yeah uh uh uh but I think it shouldn't uh look like this. Uh [snorts] that's why I prepared another schema. uh we have mobile engineering area and

**[23:04](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1384s)** machine learning area. So in mobile engineering u you have expertise in application life cycle how to work with all device like tools camera battery uh you know how to work with different type of platforms how you you're expert on creation mobile application right uh and machine learning you know what what models are uh what does mean inference how to work with inference uh how to check whites of model and so on and so cross uh cross technology between them. So you should know uh a little bit from both sides and on this cross point we have a hi engineer. So you are able to create mobile or web

**[23:55](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1435s)** applications in browsers or or maybe like desktop but we're talking mostly about mobile so that's why mobile uh and uh you can create applications that will be uh that utilize AI uh and mobile so you need knowledge from both these areas. Uh so I just replay the title uh of this man. So probably it's a really interesting direction which you can grow up as a mobile engineer uh because uh so everything uh is going the direction. So people care about privacy uh people care about money and price of cloud AI uh I

**[24:46](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1486s)** think and becomes more and more higher. Uh so this is kind of tradeoff but I think a lot of businesses will watch uh this direction soon if started yet. So there are a few directions like narrow ML it's just machine learning and gesttor recognition kind of pipeline of uh object detection and security systems and so on. Uh built-in AI how to utilize AI that already integrated in your hardware. Uh open on device LLM uh gives you more freedom and work with your own model. Uh create specific uh high effective model for specific purposes. uh and hybrid how to create hybrid solutions uh that will work with cloud

**[25:36](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1536s)** and ondevice uh AI the shift itself I give you from oriented to own it from cloud to pocket from privilege to default uh from consumer to builder so you don't you you don't consume anymore so you build yourself on your device and yeah final slide it's just uh where should we go right uh so every application you build with hi uh it's a makes you driver of this direction of technology so you open your new horizons and check uh what happens there uh and you're also beneficial

**[26:25](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1585s)** because you will be kind of one of the in the first wave of people who are doing this such of uh direction of AI building and yeah perfect timing it's just started uh uh all frameworks even uh 0 something there is no released version yet because everything is just researching researching and making it more and more effective so we will be first here thank you uh there is my link in [applause] please don't hesitate following Uh yeah, sorry I was trying to be in time. Uh I actually had a much more to say that [laughter] I told but yeah uh uh anytime you can catch me around and we can discuss the

**[27:12](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1632s)** topic. >> We have some time for questions now because you were perfectly on time. >> Oh, thank you. >> So do you want to switch one or should I choose one? Not >> I think um how can a dev know if the ondevice model is capable of a task? >> Uh sorry >> that's the last one. Maybe you want to ask that. >> Mhm. Uh so uh it's a how def know uh when you develop your application of course you don't know which device uh will be used by your user. Yeah but uh you should think about all options. uh you can check if there uh builtin uh AI model on device or not uh and for example create kind of high approach if you have built

**[28:00](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1680s)** in utilize it if no download open model and work with open model for example uh and check the power of device and if device is absolutely not capable so show error message sorry your device is too weak go please to shop and Bye. Next one. Sorry, it's not possible. >> Okay. A second questions we have. Um, should users or developers also pay for the mobile app local model by the token usage? >> Of course, no. Uh, [laughter] uh, everything that you use is a capabilities of your device, power of your device. So, just electricity from socket, nothing else. Uh so maybe if you utilize AI a lot uh your device will be

**[28:51](https://www.youtube.com/watch?v=nCeUgrWjBMo&t=1731s)** like be more warming outside but [laughter] but yeah u and of course as a application creator you can [snorts] request your user to pay you for utilization but I think it will be wired. >> Okay perfect. Um there are some other questions but I think after here you can talk to him as well and visit him on his booth. So say thank you Zasha for joining us here and >> applause for him. [applause] >> Thank you very much. Thank you for your attention.
