---
id: 673
title: "Software Engineering for Muggles"
slug: software-engineering-for-muggles
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "People & Culture"
type: "Lightning Talk"
stage: "Airstream 1"
tags: ["Communication", "Soft Skills"]
speakers: ["Theresa Heine"]
speaker_companies: ["ING"]
day: 1
starts_at: 2026-07-09T10:25:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=tpzodlvfVGA
video_id: tpzodlvfVGA
session_page: https://app.wearedevelopers.com/events/16/session/673
transcript: true
---

# Software Engineering for Muggles

**Theresa Heine (Software Engineer — ING)**

`Track: People & Culture` · `Type: Lightning Talk` · `Stage: Airstream 1`

`#Communication` `#Soft Skills`

[Watch the recording](https://www.youtube.com/watch?v=tpzodlvfVGA) · [Session page](https://app.wearedevelopers.com/events/16/session/673)

## Abstract

Have you ever tried to explain software engineering to someone who’s never written a line of code? It’s surprisingly hard, because unlike building a house, software projects rarely go according to plan. They end up more like… the Weasley house from Harry Potter.

What starts as a simple, sturdy home becomes an ever-expanding, slightly chaotic structure of extensions, workarounds, last-minute rooms, and “temporary” solutions that somehow end up permanent. Software engineering isn't about a single big construction project, it's an ongoing journey of planning, building, testing, and fixing. Using the Weasley house as a metaphor, I’ll explain why we’re always “renovating” (maintenance), why swapping out doors (libraries) means checking the versions of the hinges and door frames, and how, in software, we can simply “copy the whole house” to test new windows — without anyone catching a cold.

After this session you will never struggle again explaining software engineering concepts to your mum, your non technical friend, or your nephew again. Give it a try!

## Speakers

### Theresa Heine

*Software Engineer — ING*

Theresa Heine is a Product Owner with a software engineering background, focused on software quality, test automation, and release processes. Passionate about improving reliability in legacy systems while adapting quality practices for AI-driven development. Known for making complex technical topics understandable and bridging the gap between technical and non-technical stakeholders.

## Transcript

*1,409 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=tpzodlvfVGA&t=3s)** So, welcome everyone. Have you ever tried to explain software engineering to someone who is not from tech? Like, have you ever tried to explain to your mom the details of the bug you're trying to fix or the details of the API specification you're just currently defining? Who had who tried to explain this to someone? Yeah, a few people here. quite a lot actually. I did many times. I failed many times I think. Um but I think I also found a solution that maybe also works for you. So I'm Theresa. I'm an like introduced an engineer at ING and I just recently switched to a new role as a product

**[0:52](https://www.youtube.com/watch?v=tpzodlvfVGA&t=52s)** owner. Um and like I said in my personal in in my professional life I had many encounters where I had to explain technical topics to non-technical people and this caused quite some problems and now especially in my new role as a product owner this becomes more and more important. So we kind of have to bridge the gap between tech and business. And there's a situation I think you are all probably familiar with. Just imagine a situation where you as an engineer say we really have to do some maintenance. We they dep prioritize it the last few releases and you're talking to your business stakeholders and they're just saying but

**[1:42](https://www.youtube.com/watch?v=tpzodlvfVGA&t=102s)** I need this new feature. This is much more important. How do you convince these business stakeholders to prioritize maintenance? And you can do this or you by making them understanding the implications of not doing maintenance because I think we all know what the implications are but maybe they don't and we can do this by using a metaphor and in my talk we will use the metaphor of using the Wasley house of Harry Potter. I hope you're all familiar with the Wasley house and Harry Potter but if you're not don't worry. um you still will be able to follow. So, let's jump into the Harry Potter world. A very, very long, long time ago,

**[2:35](https://www.youtube.com/watch?v=tpzodlvfVGA&t=155s)** Apha and Molly Wasley only had two children called Bill and Charlie. And they had built themselves this beautiful small house, and they were quite happy. But over the years, they had more and more children until they had seven instead of two. And they had to adapt their house to keep and had to add more rooms to keep accommodating everyone. So everyone could have their own room that they have enough bathrooms and stuff. And this is actually very similar to how software evolves. So the v3 house actually works great as a baseline metaphor for explaining the software engineering and how software architecture evolves. Um and software is kind of just a house

**[3:26](https://www.youtube.com/watch?v=tpzodlvfVGA&t=206s)** built for change. So in the beginning all requirements are simple and easy and it's easy to start with an first implementation but then your house has to adapt to some new changes and requirements like having seven instead of two children and over the years your architecture can become quite complex and at the same time your architecture has to support changes in the future and because if it's not supporting changes of in the future it will not bring any value anymore. So if we go back to our original example we wanted to explain business stakeholders why maintenance is sometimes really complicated expensive and time consuming. We will just use our

**[4:14](https://www.youtube.com/watch?v=tpzodlvfVGA&t=254s)** whisley house as an example and we use something that everyone is familiar with. I think security upgrades are one of the most common things we do or should do. Um, and we can also do this with our Wasley house. So, let's say in our Whisley house, we want to upgrade now our door because the security of the door is not really great. We cannot even lock it. So, we want to do a major upgrade of the store. So, from version 3 something to version 4 something. Um but now when we do this um upgrade we realize that our new door version now is incompatible with other components of our house. So when we upgrade to door version 4 something we now suddenly also

**[5:02](https://www.youtube.com/watch?v=tpzodlvfVGA&t=302s)** have to upgrade our door frame version. We also have to upgrade our floor version because now the door is wider or taller and the the new door is scratching the floor. So our originally simple maintenance task now became quite complicated and much more time consuming and expensive and upgrading the door of the Whisley house actually helps to understand maintenance. I'm sorry why this happened but um my presentation was not able to sh be shared so this is my backup. [laughter] [snorts] Um yeah, but overall when you upgrade the door of the Weasley house, people who are not from tech can actually understand what you're talking about because even if you don't own a house, you know what maintenance is. You

**[5:51](https://www.youtube.com/watch?v=tpzodlvfVGA&t=351s)** know that there's always something to do. And you also understand the larger your house grows, the more maintenance there is to do. Um, and you also understand it when you replace the door and how it can affect other components, what this means. And this just helps people to naturally understand maintenance because they are able to understand the implications of not doing maintenance with something everyone can relate to. And you could also use this Weasley house metaphor to explain other software engineering concepts like when you want to explain to someone what's actually the difference between a test and a production environment because you kind of can copy your house and use it for testing. Or if you want to explain to

**[6:39](https://www.youtube.com/watch?v=tpzodlvfVGA&t=399s)** someone what a canary release is, you could also say, "Yeah, the parents at and Molly Weasley are still living in the Weasley house with the new doors, but their children, they still have the old door version and only if the parents approve, then they can move in. So could work. So what are the benefits of this or why should we even do this?" So first of all, I think we as engineers have to realize that we are in a bubble. We talk about things nobody else understands. We all know what a pull request is, what an API is, what a legacy system means, but many people don't. And we kind of have to bridge this gap because non- tech people, people who don't

**[7:29](https://www.youtube.com/watch?v=tpzodlvfVGA&t=449s)** understand these things do make decisions that impact us as engineers. And if they don't understand us, they cannot make good decisions. Um so metaphors can actually help them to understand the topics that that are important to us and in the end they can make better prioritizations because they actually understand the implications of their decisions and I think overall this helps to generate just better collaboration between tech and non- tech people um and improves decision making and we also probably get better um priorities And in the end for us from an engineering perspective this means probably less stress because we get the

**[8:18](https://www.youtube.com/watch?v=tpzodlvfVGA&t=498s)** things we want and the deadlines are probably more realistic if the people deciding on those things really understand what we are talking about. So, next time when you're in a meeting with some people or just talking to your mom, I don't know, um just ask yourself if you're talking about some technical things, if they can actually follow and understand what you're talking about. And if you are unsure, please ask those people if they can really understand what you're talking about because sometimes saying I cannot follow what you're talking about is really really hard. So I I really want to motivate you to ask sometimes if people can follow and if they have difficulties to follow

**[9:08](https://www.youtube.com/watch?v=tpzodlvfVGA&t=548s)** just explain it to them using a metaphor and you could use the Weasley house but you could also be inspired by explain like I'm five or try to explain it to your grandma. I think the important thing is making it easier and simpler than you think it should be to make them actually be able to understand it. So I would say give it a try. I thank you very much for listening and [applause] I'm here at the stage if you want to exchange about how to better communicate or you can find me also at our booth.
