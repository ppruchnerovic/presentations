---
id: 593
title: "Goodbye Microservices, Hello Self-Contained Systems"
slug: goodbye-microservices-hello-self-contained-systems
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Software Architecture"
type: "Keynote/Talk"
stage: "Stage 5"
tags: ["Microservices", "Software Architecture"]
speakers: ["Simon Martinelli"]
speaker_companies: ["Martinelli"]
day: 1
starts_at: 2026-07-09T08:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=O4q-6vPHkg0
video_id: O4q-6vPHkg0
session_page: https://app.wearedevelopers.com/events/16/session/593
transcript: true
---

# Goodbye Microservices, Hello Self-Contained Systems

**Simon Martinelli (Programming Architect — Martinelli)**

`Track: Software Architecture` · `Type: Keynote/Talk` · `Stage: Stage 5`

`#Microservices` `#Software Architecture`

[Watch the recording](https://www.youtube.com/watch?v=O4q-6vPHkg0) · [Session page](https://app.wearedevelopers.com/events/16/session/593)

## Abstract

Microservices are a popular approach to building modern software, offering scalability and flexibility. But many teams face challenges such as increased complexity, difficult debugging, and managing too many small services.

In this talk, I'll introduce an alternative: Self-Contained Systems (SCS). Unlike microservices, SCS allows each part of your application to operate independently with its UI, logic, and database, simplifying both development and deployment.

You'll learn why SCS can be a better fit for many projects, how it reduces the complexity of distributed systems, and when it makes sense to use this approach over microservices. Based on my current customer project, I'll show you how to build self-contained systems with pure Java.

If you're ready to rethink your architecture and say goodbye to microservice headaches, this talk will show you the way!

## Speakers

### Simon Martinelli

*Programming Architect — Martinelli*

Simon Martinelli is a Java Champion, Vaadin Champion, and Oracle ACE Pro, with over three decades of experience as a software architect, developer, consultant, and trainer.
As the owner of Martinelli LLC, he specializes in optimizing full-stack development with Java using AI and has a deep focus on modern architectures and software modernization.
He frequently shares his expertise by speaking at international conferences, writing articles, and maintaining his blog, Keep IT Simple: https://martinelli.ch.
His passion for teaching is reflected in his work as a lecturer at two universities in Switzerland.

## Transcript

*2,144 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=0s)** something called eventual consistency. That means you have data that is created in some self-contained system, and it takes a while until it's probably distributed to all the self-contained systems that need the same data to work on. The integration between self-contained system usually is not through service calls, as I said, but through web interfaces that just link to each other. So, that means you usually create kind of a design system that the self-contained systems share, but most often that's not that important because if you look at the users that are working with your self-contained system, you will find out that usually just the user group or kind of a group of people just are working with one self-contained system and not with many, so they wouldn't even realize that they don't look the same. But you're really linked with through the web interface, and so you have completely decoupled that. Now, what happens if you want to

**[1:03](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=63s)** interchange data in kind of real time? Then you should go for asynchronous, so you can send events, for example, that other micro self-contained systems can consume and use that to update their data or use it in in the system. And this, what I already said, means that the consistency is relaxed, so you have this eventual consistency. Now, if you look at the advantages of self-contained systems, then we see four, maybe there are more, but I just picked these four, so it's resilient because it's loosely coupled. You can replace a single self-contained system. It's also very important to see that, depending on your application, not all self-contained systems have the same, quality requirements. For example, if you have an e-commerce system and you have product management self-contained system, that's probably less important than your order management system. Because if the order management system doesn't work, the company loses money because no one can order something. But if the product management doesn't work,

**[2:09](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=129s)** who cares? The product managers care, they have to change the data, but for selling the goods, that's not very important right? You can also scale your self-contained systems, again, depending on how important or what actually the self-contained systems are doing. And you can also put some self-contained system or this make or buy decision can be done as well. So, for example, I will talk about a project that I'm currently working on. We have parts of the system that is not self-made. So, these are also kind of self-contained systems. And if you do migration, and that's what I will talk about in a minute, you're independent. So, you don't have this big bang releases. And a lot of people say, "Hey, do not do microservices. Always start with a monolith." I wouldn't do that, right? Because plating a monolith later on,

**[3:06](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=186s)** even if you're doing it in a good way, uh requires a bit of work. But if you do self-contained systems from the beginning, this may be a better idea. Now, something else that turned out uh is that self-contained systems are a good size for AI. Because usually it's a part of your application, it forms a bounded context, means AI knows everybody everything about your application or the self-contained systems, and you can work on that. And because UI, business logic, and data is in the same application, it can work on both. Because traditionally we were splitting UI and back-end mostly because of different technologies, right? So, we have like JavaScript in the front-end, maybe Java or any other language in the back-end, and then we have to split the team. That's kind of reverse Conway maneuver, so to say. So,

**[4:03](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=243s)** we introduce communication where we shouldn't have communication from an architecture standpoint, right? And if you have everything together, now AI can work on that because AI is a full-stack developer. So, you don't need special teams for for both of them. So, that's kind of what self-contained systems help. Now, currently I'm working on ERP system. So, we have an ERP system that's a Java application built around year 2000 and uh we have to replace that because we have parts of the application that no longer run on on Java. And what we do, we replace the whole ERP system with that. And what we did, we also created self-contained system. That's just an example um of that. But, you can see the ID. So, what we did, we found out that we have different bound contexts, for example, inventory, the customer, the order management, and logistics. Logistics, and these are independent applications now. Now, the point is, if you look at the

**[5:08](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=308s)** order management system or at the logistic system, you see that they have two kind of database boxes down there. And the point is, they need some data from other self-contained systems that's read-only, like product data, customer data, for example. And they create their own data, like the order, or logistics create some logistics data that are separated from that. And what we do, we replicate the data from the other self-contained systems into uh the systems that need the data to operate on. But the source of truth may only be in one self-contained system. So, it's not possible that two self-contained systems write on the same data. That's not allowed. They just write on their own data and this gets replicated. Uh the replication can be in in different styles. So, there are plenty of options to do that.

**[6:04](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=364s)** We do materialized views most most often. That means we have different database schemas that are linked together. Our database links and then we copy with the database mechanism the data from there. And people say, "Hey, now you're creating data redundancy." And we tried to normalize the data in the past few years just to remove the redundancies. But in that case, redundancy is very, very important and also is very helpful. And it doesn't affect the system because if you look at the data that is created, for example, at the wholesale company, if someone creates a new product in the product management or inventory system, this takes probably 2 weeks until it can be ordered by a customer. Because first of all, the person that is creating the product has to negotiate the price with the supplier. So, that's the first process.

**[7:01](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=421s)** Then if they agree on a process, they have to order the product that we can store it in the warehouse, right? And this all the whole process takes around 2 weeks. And so, it's no issue that the data takes time to be replicated. So, sometimes we just replicate the data overnight, for example, or the and that sometimes we replicate it more often. Now, sometimes this replication doesn't work. And we want to really have events. So, for example, if an order is created, we need to, for example, reduce the stock. So, that's why we have an order topic, for example, where we create events when orders are created. Or, if the people in the warehouse are picking the product, then we also send events that we can tell the customer in the order management system that he gets like uh the product, for example. Or, if if he gets a reduced amount of um what he ordered. If we did did that, we also defined some

**[8:08](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=488s)** macro-architecture. That means we want to kind of standardize parts of the whole system. For example, we want to have common user interface, so we created a design system for that. That's kind of a screenshot of that, where we have component styles. We also have information about the whole other self-contained systems, because if you want to link from one self-contained system to another, we have to find that. So, we have kind of a link database or service locator. And we have data integration. As I said, we have replication for read-only data, and we have asynchronous through events. And the question if you want to use replication or events depends on multiple um topics. So, first of all, if you need actual data or very up-to-date data, you better go with events. You can do that push-based. And you have kind of near real-time updates that you can use in your other self-contained systems. The problem with events is you have higher complexity.

**[9:14](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=554s)** So, you either have to use a kind of a messaging system like ActiveMQ or RabbitMQ, or you can use Kafka if you want to do streaming. But, this has to be operated by and you have to monitor it and stuff like that. And if you just do replication on a lower level of the data, then this is very simple to implement and you can define the frequency of the updates, but somehow um you have delays, right? And you don't want to do that all the time because probably put a lot of load on the database if you do replication like that. So, that's the difference that we have in our system. Now, we do the modernization. So, we have a monolith and how we can do that now or put that in self-contained system. Martin Fowler once wrote about the strangler fig. So, that's the strangler fig. That's kind of a a plant that lands on a tree and then it grows and it wraps around

**[10:21](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=621s)** the tree and finally when it's done, the tree in the middle dies and the picture on the right side, as you see, the structure of the tree is still there, but the tree is gone inside. And that's kind of the way how you can do modernization projects and that's what we do in the project as well. So, we have this uh uh thing on the left-hand side, we have this monolithic application and now we start to extract parts of the application in this new self-contained systems. You also see the red dotted lines. So, we have intermediate steps that may be possible that the old client is accessing the new business logic or the new business logic is accessing the database. That's this integration database that I was talking about. But finally, when we are done, we will uh have these self-contained systems. Maybe to give you an idea about the system, it's more or less a whole ERP system just without um

**[11:27](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=687s)** the logistics part and this will take around 5 years to get done. And so we can do step-by-step. We also have parts of the system that we can have a kind of a parallel mode where we have the old system running and the new system system running. So we can massively reduce the risk of putting the thing in production. So to get to an end, in my opinion, self-contained systems are an optimal modularity because they are based on business boundaries. And you create parts of an application that is also autonomous. So the team can operate on UI business logic and database. So you don't have any synchronous APIs that you have to maintain. And especially turned out that for AI, it's a great way to split the bigger application to parts that AI can operate on. Because we don't have any synchronous communication, we reduce runtime dependencies. And that's very important. So it's way easier to spin up new

**[12:32](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=752s)** versions or to replace systems on the go if you don't have dependencies on that. And once we are done with the modernization, we can continue to do that. Because probably in 5 years, maybe technology changes, AI is more capable. We can restart and replace self-contained systems just on the go. So that's it from my side. I think the time is over right? To Okay, thanks a lot for coming. >> [applause] >> If you have questions, I'm here to all day. Just approach me and we can discuss things. >> Thank you. I have one question. I think we have time for one. Based on your experience, how important Well, not important, but how complicated is for small companies to implement these systems? Is it Is it really easy for them? >> Yeah, it doesn't matter how big the

**[13:28](https://www.youtube.com/watch?v=O4q-6vPHkg0&t=808s)** company is, in fact. Um maybe the team size, I didn't talk about team size, but the team size gets reduced. So, before we had like teams of five people, now we reduce the team size because of AI, we don't need uh that much developers anymore, but we also have smaller teams because they are focusing on a single business domain. So, it's simpler for them to get the context and wrap around the head around uh the business domain, right? >> I see. Okay, thank you. Let's thank one more time, Simon. >> [applause]
