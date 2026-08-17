---
id: 883
title: "20 billion requests a week: Upgrading Twilio's API gateway at scale"
slug: 20-billion-requests-a-week-upgrading-twilio-s-api-gateway
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Backend & APIs"
type: "Keynote/Talk"
stage: "Stage 7"
tags: ["APIs", "Microservices"]
speakers: ["Ainhoa Arruabarrena Ortiz", "Mario Román Dono", "Marius Obert"]
speaker_companies: ["Twilio"]
day: 2
starts_at: 2026-07-10T09:00:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=PoQymqm7cNo
video_id: PoQymqm7cNo
session_page: https://app.wearedevelopers.com/events/16/session/883
transcript: true
---

# 20 billion requests a week: Upgrading Twilio's API gateway at scale

**Ainhoa Arruabarrena Ortiz (Senior Software Engineer — Twilio), Mario Román Dono (Software Engineer — Twilio), Marius Obert (Developer Evangelist — Twilio)**

`Track: Backend & APIs` · `Type: Keynote/Talk` · `Stage: Stage 7`

`#APIs` `#Microservices`

[Watch the recording](https://www.youtube.com/watch?v=PoQymqm7cNo) · [Session page](https://app.wearedevelopers.com/events/16/session/883)

## Abstract

Twilio's API Gateway is the front door for over 20 billion requests a week, regularly sustaining peaks of 60,000+ requests per second.

Over the past four years, Twilio has migrated from a legacy system built on a decade of rapid growth to a modern, hardened ingress stack. In this session, we'll go under the hood of how we modernized our gateway by unifying behind a common core, requiring explicit, contract-first development, and utilizing cellularized and redundant infrastructure principles.

Join us to learn how we successfully untangled ten years of technical debt, crossed the river, and built for the future to simplify Twilio’s enterprise ingress, all with zero major disruptions to customer traffic.

## Speakers

### Ainhoa Arruabarrena Ortiz

*Senior Software Engineer — Twilio*

Ainhoa is a Senior Software Engineer at Twilio specializing in cloud infrastructure. Over the past four years, she has driven initiatives to modernize Twilio's public and internal edge infrastructure, executing a long-term vision that has systematically elevated security and performance standards. As an infrastructure owner, she and her team build the tooling that abstracts away complexity, enabling internal teams to seamlessly deploy their own ingresses while ensuring a reliable, high-performance experience for end users.
When she isn't modernizing edge routing, Ainhoa can usually be found away from the terminal—either hitting the basketball court or out on a trail hiking.

### Mario Román Dono

*Software Engineer — Twilio*

Mario is a Software Engineer on the Edge Services team at Twilio, where he works on building the company’s high-volume, public-facing edge infrastructure. Previously he worked at EPAM, where he developed large-scale media software for several of the biggest European tier-1 TV operators. Specializing in Infrastructure and Platform Engineering, he focuses on creating developer platforms that help internal customers ship software at a higher pace, while also ensuring a reliable, high-performance experience for the end users relying on those services.

### Marius Obert

*Developer Evangelist — Twilio*

Marius' passion is exploring the latest communication technologies – and, even more, sharing his knowledge and learning from others. Originally from the Black Forest in Germany, he started his software development career as a UI developer in Silicon Valley, where he discovered his love for web technologies, especially JavaScript and the entire Node.js ecosystem.

After countless creative (and sometimes frustrating) battles with CSS, he relocated to Munich, where he now works as a Developer Evangelist at Twilio. In this role, he inspires and empowers developers around the world to build cloud-native apps with outstanding customer engagement. He has also spent nearly a decade working on enterprise frontend development and even wrote a book on the topic.

Whether on stage, in workshops, or through hands-on prototypes, Marius loves exchanging ideas with fellow developers and pushing the boundaries of what’s possible. When he’s not doing that, he dives into the world of Web 3.0 – always on the lookout for the next exciting technology.

## Transcript

*3,205 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=PoQymqm7cNo&t=3s)** So, hello. Thanks to everyone for coming. My name is Ainur and this is my colleague Mario. We're both software engineers at Twilio and we're currently part of the team that manages and maintains all of nearly all of the Twilio's ingresses um including the REST API. Under this talk, we're going to get an overview of the behind the scenes of the REST API ingress, how we've changed it in the last few years. First, let me start with a bit of a contest to understand how we reached to this point. I wasn't so long ago that you needed tons of euros to invest to connect to an SMS gateway, get your own phone lines, you have needed to program low-level protocols, even have some Cisco call managers. It was complicated, complex, and not accessible for everyone.

**[0:51](https://www.youtube.com/watch?v=PoQymqm7cNo&t=51s)** But, Twilio came in and was able to abstract all this into a API and suddenly with a few lines you were able to engage using different channels, messaging, voice, video, email, all through the world just with a few lines of code. And I think this worked pretty well because uh Twilio traffic grew exponentially for the first few years and that also translated into Twilio growing, teams growing very fast. The guidance was let's just move fast and deliver. And right now we're in around 20 billion requests weekly. But, that came with a high price. Um we had no governance. It was let's just grow, open governance, do whatever you

**[1:38](https://www.youtube.com/watch?v=PoQymqm7cNo&t=98s)** can. That moved us very fast in the beginning, but it became a nightmare when we wanted to maintain this scale of traffic. There was lots of teams that were doing changes into the ingress infrastructure, various gateway APIs, undocumented behaviors, there was no single source of truth. So, we reached the point in which we had to stop and ask ourselves if we were going to do something about this. So, we decided we were scoring to start from scratch, we unify everything, and hopefully we don't break anything along the way. So, 5 years ago, we took this big project and completely redid the REST API ingress. So, now that we've decided that we are going to redo everything, this is the

**[2:24](https://www.youtube.com/watch?v=PoQymqm7cNo&t=144s)** moment that we get the requirements, we put everything together. What does Twilio need? What does What do the Twilio clients need for us? So, we put everything together. So, we want aligned to our industry standards, we want to be scalable, we want to be secure, we want to use a global CDN, we want to be reliable, we want to distribute performant, we want to use open API, we need to ensure that it's maintainable. We need developer focus, we need it to be auditable, backwards compatibility. Okay, I hope I didn't miss anything. But, there was one important thing. We needed to not break anything that was working till now. There's There was real world world scenarios that were being solved with Twilio APIs, and we didn't need this not

**[3:13](https://www.youtube.com/watch?v=PoQymqm7cNo&t=193s)** to break. If we weren't weren't able to do this migration without breaking anything, there was no point in doing this at all. [snorts] So, it may sound easy to just maintain whatever was working right now. We knew what what we were pro- providing to the clients, we knew what was going on behind the scenes, but I think that 10 years is probably too long to have everyone patching in and putting some kind of some lines and then forget to document it. So, we ended up with a lot of unintended dependencies, probably coming from these undocumented code paths, and we knew that we were going to face a lot of unknowns unknowns that we couldn't foresee nor plan for. So, this was our our starting point. Um

**[4:01](https://www.youtube.com/watch?v=PoQymqm7cNo&t=241s)** this was how the infrastructure looked like. We had a network load balancer, we had a bunch of instances behind. First, traffic went through an Nginx um fleet acting as a reverse proxy, and then we had two API gateways that were one behind the other for which I have no answer why. And then in these API gateways, we had a lot of legacy behavior, undocumented timeouts, file sizes. We didn't even know why. And then it would flow into the um business logic. While these instances were quite good when they were starting fresh and clean, they would not scale at the rate that we needed them to. So, we

**[4:48](https://www.youtube.com/watch?v=PoQymqm7cNo&t=288s)** ended up with huge instance fleets so that we could just handle anything that would come to us. And also, this was an infrastructure that we were maintaining all across nine different local edge points so that we could give better performance to all over the world and also comply with any compliance requirement that we may have for our clients. The first decisions that we took was we just need one single API gateway. There's no reason to maintain two of them. And we would need this API gateway to have very defined clearly defined actions taken. For that, we wanted to have contract-driven development, and we defined and created our own open API spec definitions so that everyone at

**[5:36](https://www.youtube.com/watch?v=PoQymqm7cNo&t=336s)** Twilio would use them. This is an example of them of it. We define all the transformations that are required for the each path. At this one at this documents so that there's a single sort of truth. We introduce governance to the process and at the end of the day there's no surprises when we uh deploy our open the API gateway and there's no unwanted behavior added there. But we can define the best API gateway, but if we don't surround it with a correct infrastructure or if we don't do it right, we don't we end up just with a great gateway that doesn't do its its job. So, we needed to build to scale. It needed to be maintainable, resilient,

**[6:25](https://www.youtube.com/watch?v=PoQymqm7cNo&t=385s)** and scalable at any chance. And this is after 5 years with the infrastructure that we ended with. We've replaced the engine X configurations. We added some global CDNs, which in the end it gave us much more point of presence that just nine edge locations. It was very managed by from for us. We didn't need to worry about any implicit behavior. It was self-managed for security updates, redundancy. It was taking care for us all around the world. And our clients saw that. And then we split the API gateway into different functional cells. This didn't only gave us isolation in case of failures. This also let us scale

**[7:15](https://www.youtube.com/watch?v=PoQymqm7cNo&t=435s)** depending on the workload that we had. It's not the same if we have messaging traffic or if we have voice or video traffic. The requirements are different and the idea was that they needed to scale into different rates. We used Kubernetes and with Cube we also were able to give the rate of scalability that we required. Now I will let Mario guide you through the migration process that we took. >> Thank you. So, we have explained our legacy infrastructure and the new one, but we haven't talked about the process. How did we get there? And most importantly, how did we get there in a safe way? Because we can go like Mr. Magoo here, blindly walking and not knowing if we are going to fall and

**[8:03](https://www.youtube.com/watch?v=PoQymqm7cNo&t=483s)** break down our customers. And this is something that at a at our scale it it can happen. So, the first thing that we want to mention is that this process takes time. We can wake up one day and say, "Hey, let's migrate everything to a CDN." Uh like I know I has explained, this was done over the course of more than 5 years. And we have highlighted some of the biggest steps that we took over the time. And some of them were non-glamorous tasks. For example, the first one or one of the first ones was removing support for TLS V1. Uh to give you an idea of how was the the state of the infrastructure.

**[8:52](https://www.youtube.com/watch?v=PoQymqm7cNo&t=532s)** But it was important because we have to lay down the foundations of an infrastructure that had less moving pieces, that required less maintenance, so that we could tackle more challenging migrations uh in the future. Uh Okay. Um now, going into the technical details, how do we actually migrate the traffic? We relied on two of the most beloved tools by any software engineer. The first one is DNS because you know the haiku, in the end is always DNS. And the second one are YAML files because I'm sure that everyone loves hesitation, the weird behaviors that

**[9:41](https://www.youtube.com/watch?v=PoQymqm7cNo&t=581s)** this file format has. And yeah, nothing can go wrong with these two. But in our case, they really worked for us because we leveraged DNS records by creating intermediate records between the customer-facing uh DNS records, for example, the CNAME for api.twilio.com, and both the old and new infrastructure. These records were weighted so that we could select the amount of traffic, the amount of requests that were going to either the old or the new setup. And this is a real example of how the api.twilio.com ingress looks like. We have a YAML file that is integrated with our infrastructure as code uh tool,

**[10:29](https://www.youtube.com/watch?v=PoQymqm7cNo&t=629s)** and we have this section called inbound rules, where we define the regions where we want to deploy api.twilio.com, and both the new, in this case, uh it's called this, uh which is the CDN infrastructure, and the legacy ALB. So, we can start sending the traffic um the 100% to the legacy ALB. Then, we can split the traffic, see if everything is working, and after checking that we have no problems, we can end up sending all the traffic to to the new CDN infrastructure just by using DNS and YAML. The same mechanism was leveraged by with the migration to the API gateway. Once we had all the traffic going to the

**[11:19](https://www.youtube.com/watch?v=PoQymqm7cNo&t=679s)** CDN infrastructure, we had yet another uh intermediate DNS record that is weighted, and it's between the CDN and the the old and new API gateways. In this case, we start with the 100% of requests going to the legacy origin and we can see here that we define all the clusters and all the cells of the new API gateway. And we can start sending just 1% of the request to each cluster. And if everything works, we end up with an spread distribution of the request, 20% for each cluster. This is not only useful for migrations. This is useful in case of incident mitigation. Let's say that our automatic

**[12:08](https://www.youtube.com/watch?v=PoQymqm7cNo&t=728s)** mitigation don't work. We can go here to this sample file, drain the cluster that is malfunctioning and everything works in a very simple way. But you can imagine that at our scale we are going to face problems and we hit some bumps in the road. The first one that we want to talk about is that you are going to have to deal with legacy systems that you can't change. In our case for example, we found that some customers were using non-SNI connections and our CDN wasn't prepared for this. So once we saw that customers were being impacted we have to stop the migration, roll back the changes and implement a fix. So that like you know as I explained earlier, we

**[12:59](https://www.youtube.com/watch?v=PoQymqm7cNo&t=779s)** don't want to break customer traffic. The second one is that we experienced Hyrum's Law first hand. I'm not sure if everyone is knows this law but it basically states that for every for every API that has an enough number of users, it doesn't matter what what you promise in the contract. If you have an observable observable behavior it can be relied by somebody and it will be. And in our case, uh our old API was returning some JSON objects with an specific order every time, and this wasn't defined anywhere. And we didn't know about that, and when we started migration to the new gateway, this ordering was it disappeared.

**[13:50](https://www.youtube.com/watch?v=PoQymqm7cNo&t=830s)** The thing is we had a customer that was relying on that JSON ordering. Uh don't ask me why. The reason was that uh they wanted to check if there was any configuration drift. And whenever we were slowly rolling out the changes, the ordering changed and engineers were being paged, the engineers of the um customer company, because you know, they were seeing these drifting configuration. They got in touch with us. They told us, "Hey, what's going on?" We had to explain them and we had to again apply another fix so that we didn't break this behavior. And the last one is that we even find some surprises in our own

**[14:40](https://www.youtube.com/watch?v=PoQymqm7cNo&t=880s)** infrastructure. I mean, um the API infrastructure has been there since 2008 and we had some strange things. We found an static file called cowbell.mp3 in the gateway. And you can imagine it, it's the sound of a cowbell. And we didn't know why it was there, who put it there, or if it was being used. So, we were just about to remove it when we found that it was heavily used. There were a lot of requests going to that file. And the cause is that it is currently referenced in some of the Twilio tutorials that people use to get to know about how Twilio works. And we couldn't remove that file and break those tutorials. So, again, we have to find a solution, find another

**[15:29](https://www.youtube.com/watch?v=PoQymqm7cNo&t=929s)** In this case, we moved the file to a static bucket, and that way we we don't break the tutorials. But actually, if you go here to api.twilio.com/cowbell.mp3, you will see the file, and it's a good thing to have. Well, uh overall, even if we hit these bumps, um you have to have the mindset and the right tooling for accomplish these migrations. And three things that are I think they are primordial are having the right observability tools so that you can know if your customers are being impacted. If they are being impacted, having the

**[16:17](https://www.youtube.com/watch?v=PoQymqm7cNo&t=977s)** ability of uh quickly roll back the changes. In our case, like we have explained before, using DNS and YAML files so that customers are impacted the least time possible. And having some degree of flexibility because you can't force customers to adapt to our changes always. Okay. So, after crossing the bridge, after moving all of the requests to the new infrastructure, um what we have accomplished? Was this migration a success? Let's talk about the results. So, the first thing that we want to talk about is the results for the S team, the the team that we work on, and we we manage the infrastructure.

**[17:07](https://www.youtube.com/watch?v=PoQymqm7cNo&t=1027s)** Um we have experienced a shift in our mindset because we no longer have to be the maintenance of the infrastructure and have this manual work of uh setting up ingresses for the um other Trilio teams. And now we have created a platform where we spend the time where is important, and that means um reducing the the amount of maintenance, uh improving the reliability, and improving the experience for the uh internal Trilio teams. For those teams, we can say that have reduced the amount of cognitive load, we have improved their developer experience, and they have now a greater agility to deliver

**[17:57](https://www.youtube.com/watch?v=PoQymqm7cNo&t=1077s)** things, deliver features, because they don't have to care about the edge infrastructure, they only have to care about understanding open API, and knowing what is uh an API and how to define it, because we are going to take care of that, and we are going to create an edge infrastructure that can handle all the traffic in a reliable way. So, it's faster for everyone. And the most important thing, the people that pays uh our bills and our salaries, our customers, we can say that now our infrastructure is more reliable, is high performance, and the experience is better thanks to the CDN, because we have more points of presence, we have um a bigger geographical redundancy, and even has decreased in some cases up to a

**[18:48](https://www.youtube.com/watch?v=PoQymqm7cNo&t=1128s)** 30%, which you can imagine is a a good thing for them. And also the new API gateway, which is cellularized based on Kubernetes, is more reliable in case of incidents, uh it's more scalable, we don't have to have these big number of instances deployed anytime. And it has been accomplished with zero out time, maintaining all of our SLOs for up time and success rate. So, what's next for us? Um Twilio is earning its spot as the platform for conversations in the AI era. We are not longer just a platform to send messages or create phone calls. We have developed new products that take that improve these the experience of our

**[19:39](https://www.youtube.com/watch?v=PoQymqm7cNo&t=1179s)** customers with AI-based solutions. For example, we have customer conversations memory to remember the previous interaction with our customer, conversational orchestrator, and if you're interested, you can go into Twilio's website and we have a surprise for you at the end of the presentation if you want to play around with with Twilio. And you can imagine that the edge infrastructure must rise to the challenge because we have to um in first place, we have to still be reliable and don't let down our customers so that they can build on top of Twilio and the infrastructure can handle the greater amount of requests. And also, the internal teams like they want to create new innovative features. They

**[20:28](https://www.youtube.com/watch?v=PoQymqm7cNo&t=1228s)** want to be quick and we have to improve their developer experience. So, we are on that path. So, we can talk about two different things. Uh the first one is that we are improving our support for agentic workflows. Uh if you go to this repository, you can see some of the things that we are working on, but basically, we have created a new MCP server so that agents can work with Twilio services. We are creating new cloud skills and a lot of work is going on. And the other thing is that we are modernizing our SDKs and APIs. I don't know if you have work with V2010 APIs, but they are basing XML and the experience is not the best. So, we are

**[21:17](https://www.youtube.com/watch?v=PoQymqm7cNo&t=1277s)** working on JSON for support. We are working on unified versioning. Um and overall we are trying to uh improve the developer experience and the agent experience uh by making it more modern and idiomatic. Okay, I think that's all. Um thank you very much for attending. And like I promised, we have this little gift for you. Uh this is a promo code. Uh if you use it when you create your account, you will get $30 to spend on Twilio products. And if you want, you can also scan this QR code to give us feedback about the talk. And yeah, like the uh I think we I'm not sure if we have any questions, but we have time for it. So, thank you. >> [applause]
