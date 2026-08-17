---
id: 948
title: "There Is No Such Thing as a Fair DBaaS Benchmark"
slug: there-is-no-such-thing-as-a-fair-dbaas-benchmark
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Data & Databases"
type: "Keynote/Talk"
stage: "Stage 10 - powered by TikTok"
tags: ["Cassandra", "MongoDB", "Multi-Cloud", "Performance", "PostgreSQL"]
speakers: ["Daniel Seybold"]
speaker_companies: ["benchANT"]
day: 2
starts_at: 2026-07-10T11:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=_aR4V7ima2Y
video_id: _aR4V7ima2Y
session_page: https://app.wearedevelopers.com/events/16/session/948
transcript: true
---

# There Is No Such Thing as a Fair DBaaS Benchmark

**Daniel Seybold (Co-founder — benchANT)**

`Track: Data & Databases` · `Type: Keynote/Talk` · `Stage: Stage 10 - powered by TikTok`

`#Cassandra` `#MongoDB` `#Multi-Cloud` `#Performance` `#PostgreSQL`

[Watch the recording](https://www.youtube.com/watch?v=_aR4V7ima2Y) · [Session page](https://app.wearedevelopers.com/events/16/session/948)

## Abstract

If you’ve ever tried to benchmark a managed database, you know the frustration: same vCPU, same RAM, same PostgreSQL version — and completely different results.

Designing a “fair” DBaaS benchmark today is not just about query workloads and metrics. It’s about understanding hidden IO limits, burst credits, storage backends, noisy neighbors, throttling behavior, and pricing tiers that influence performance in ways your dashboard doesn’t show.

In this talk, we break down what “fair” actually means in practice. Should you compare systems at equal cost, equal resources, or equal performance targets? Each approach answers a different engineering question — and can lead to opposite conclusions.

Using real-world examples from benchANT benchmarking projects, we’ll show where common benchmarking assumptions fail, how cloud abstractions distort performance expectations, and why reproducibility alone doesn’t guarantee comparability.

You’ll leave with practical guidance on how to design benchmarks that reflect production reality — so you can evaluate DBaaS platforms based on engineering truth, not marketing claims.

## Speakers

### Daniel Seybold

*Co-founder — benchANT*

Daniel started his career as PhD student in the  area of cloud computing with a focus on distributed databases in the cloud. Further interests cover cloud orchestration, model-driven engineering, and performance evaluations of distributed systems. After completing his PhD, Daniel has co-founded the Benchmarking-as-a-Service platform benchANT where he is responsible for the product development and large-scale benchmark projects.

## Transcript

*3,313 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=3s)** Um welcome in this talk. Um this is one of the talks where probably not going to be AI the topic but it's rather on database systems data infrastructure um and especially about how to run benchmarks how to interpret the data and what you can get out of it. And before we dive into the technical details a few words on myself um so that you know who's talking to you today. So, hi, I'm Daniel. Um, I'm co-founder of Benant. We are a spin-off out of the M University. So, we come from actually research running now for four, five years. Uh, doing now over 50 projects for large tech companies with a dedicated focus on well deep technical performance,

**[0:52](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=52s)** scalability, reliability evaluations in the data infra infrastructure domain. And for today, well, we're going to talk about benchmarking, database benchmarks. And they are, well, different kinds of viewpoints. What is actually benchmarking? So, some people would say it's kind of a black magic. You run some mysterious experiments, get some data, and tell you this going to be the how it works. Um some others would say it's rather kind of an art to get actually the number useful numbers where you can drive your decision process with um and then there is also an opinion by probably the pioneer or the creator of database benchmarking Jim Gray himself. So you see quite diverse um ideas on

**[1:41](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=101s)** database benchmarking. There is also a more formal definition again by Jim Gray uh that shows that this is actually with a methodological approach to assess the performance of a database system. So talking about real throughput numbers, latency numbers, resource utilization and we're also going to see talk a bit about costs today. Um so database benchmarking is probably the same time around as database systems are and database landscape evolved. Um so does the benchmarking and how to well interpret the numbers how to get the numbers here a brief timeline. So it's not when the each concept was invented

**[2:28](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=148s)** rather it was when it's adopted by the market. um started with the database appliances. There were the TPC benchmarks. Pretty simple. You got an Excel list. You got some numbers, probably 20 entries. That's it. Um then the the whole world changed. We got the cloud. Now we also have managed databases, serverless databases. In the end, databases get easier to use. Um but we also first we got some more control over the database systems. Now we're losing it again looking at serverless or autonomous databases and when we want to compare the systems well we have more options more knobs and bolts and it gets harder to compare but do we actually need to compare

**[3:16](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=196s)** database system these days there again two perspectives on that so one is probably the marketing perspective um well if you ask the vendors they're all the fastest scalable uh most elastic ones. I especially still wondering what is the still wondering what the hyperscalability looks like. Uh haven't found out yet on the on the different perspective still by the vendors. Um there is so yeah we have the same claims different vendors no decision basis but there are also vendors that actually encourage you to run benchmarks because this will get you the data to find out the best well configuration infrastructure or even technology for your use case. As you can

**[4:04](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=244s)** see this is also advertised by the big players in the database domain. This is just a few examples. And why do they do that? Well, actually with benchmarking, you you replace your gut feeling with some hard numbers. But when comparing the system there, you probably also read a lot about um some well benchmark wars or some claims by different vendors. um when you read or when you read benchmark results or you have to run them yourself, there's always one aspect which needs to be considered and this is well the fairness aspect which we're going to dive deeper today. So nowadays can a database benchmark actually be fair especially in the

**[4:51](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=291s)** managed database domain? There's a short answer to that. Well, it depends. There's also a bit more complex answer to that. um as fairness is not necessarily a property of a database benchmark. Um so what that is does this mean in in practice? Well, let's see. But before dive uh going deeper in that a few guidelines when it comes to benchmarking and when you see results they should always follow these principles. So they have to be transparent. Um the data needs to be publicly accessible. So not just some highle charts or aggregated data. Um and they should be rep reproducible. So there should be enough details or even

**[5:38](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=338s)** the scripts to rerun the benchmarks by yourself. Otherwise the results might not be that useful at all. And there there are way more guidelines on that. Uh encourage you to re look into that if you're really interested. They go way technical way more technical. Um and they not only apply for database systems, they also apply for other kind of distributed systems. So coming back to the database domain, well if you design and run a benchmark, it's basically three domains involved. So we have the infrastructure, the cloud infrastructure domain. We also have of course the database layer and we have the workload layer. And if you just flip or two play with one knob um on all the of each of these domains, you will end

**[6:27](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=387s)** up with a different kind of configuration which is fair. But you you need to consider that. Um and for today we mainly look into the cloud infrastructure domain and how that can affect or that may well influence the results that you get or that you see that some someone is publishing. So let's assume you want to design a fair um database as a service benchmark. There are basically four approaches how you can achieve that. Um you can look for a resource equal setup which is probably the most straightforward one. Um but already here it comes with the challenge that resource equal might not be possible across all the target systems you're

**[7:15](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=435s)** looking at. You can go for a cost equal setup which is you take your your current system or target system as a baseline and look for other systems in the same budget range. Um again this is a fair approach but you might end up with suboptimal results. So let's assume you have a compute intensive workload your your current system is rather a compute optimized flavor and then you pick something in the same budget range but with a highly storage optimized one. You can already guess how the results going to end up. There are also some more approaches. So performance equal where you can actually look which of the the other systems ex is achieving a similar performance and

**[8:04](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=484s)** comparing then the costs that would be required. This approach also uh a valid one but it would requires quite an iterative approach to measure a lot of data points on the competitor systems. And the last one which is probably the most accurate one but it requires so you have a very specific workload model and of your current system run that against other systems to see how it ends up performance-wise. Here uh the challenge is that it requires a really specific knowledge of your current workload model. So to sum it up um the fairness of the so all of these approaches are fair but each of the approaches defines fairness in its own um in in its own way.

**[8:57](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=537s)** Um and what are the implications? So this is what I going to show you now with some well case studies that we did uh very recently. Um and here I brought some results with me um to see how especially the resource equal and the cost equal approach going to work or not going to work out. So what we did is um recently we run a a huge study across the Postgress database as a service market comparing performance price performance also features um and I took some of the results for today. um to showcase you well how the how fair the results actually are or how fair you

**[9:47](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=587s)** can make them to look like. So these are basically the um the technical constraints for the results I brought for today. Um so we're using rather small Postgress debug instances. They're all uh located in the Frankfurt region. And we use Postgress 17 in a two node HA setup. We used a workload which is based on the TPCC like one. So transactional workload. Um nothing exceptional here rather standard stuff. So now let's have a look on some data points. So here we're going to see uh the results for that resource equal setup of

**[10:37](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=637s)** AWS versus Azure. So this is the standard AWS uh Postgress offer not Aurora for Azure the same not their very new horizon one. Uh we have a resource equal setup. We see well they're nearly the same. So don't worry about the the absolute numbers just the relatives uh are important for now. We see they're basically nearly identical. So looks like resource SQL seems like a fair approach. Um case closed. Well there might be some more to it. Um this goes in the same fits into the same resource e category. Now Azure is a slight winner while AWS is a slightly losing. It's still same spec 8 core 32

**[11:26](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=686s)** GB RAM same storage cheapest SSD storage. And there's a third one where we have now a clear winner for AWS. So well this you might see these kind of reports where um and they all claim this going to be a fair approach. They're all resource equal. Um but there's more to the story of resource equal because resource equal especially in the context of database as a service does not mean you get the same kind of system. Um so let's have a look at the more technical side. Um how come these differences in the performance? Well um on AWS you can uh select a lot of

**[12:14](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=734s)** different compute instance types for uh your RDS service. The same goes for Azure. Um here we played just a bit with the AWS ones. So to the left we have the rather old M5 instances. In the middle we got the uh M6, the Intel one. And to the right we got the more recent uh ARMbased Graviton one. There's even a newer one now available which provides even better throughput numbers. Um and for Azure we use their latest available intel generation. So this is already where you see that resource SQL might be fair might not so be fair. I leave it now to you if you consider it a more a fairer approach if we would only

**[13:03](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=783s)** use Intel instances because that's only available on Azure or if we use the latest available generation on the respective provider to have the fairest benchmark approach. So we what we also did is as I said the the study is quite broad. Uh we also benchmarked um not only the hyperscalers but also many tier 2 providers and native Postgress companies. Um good thing is well it gets easier on a design level because tier 2 providers native Postgress companies they only um provide you usually one or maybe two compute types and also only one storage type. While the hyperscalers offer you a lot

**[13:52](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=832s)** of different compute types, storage types already for that 8 core 32 GB thing. But what's about the performance? Do we see there a difference or are there more or less in the same ballpark? So I brought some of the data points that we have with me. Um, so we have Azure, we have AWS, another hyperscaler, some T2 providers, some native Postgress companies. They're all 8 core 32 GB RAM and their cheapest SSD storage. And well, we see that it's up to 19 times performance difference here, which was quite surprising. Um, and well, yeah, we we we have still the resource equal approach. Um

**[14:42](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=882s)** it's now the the question is well is resource equal still fair here um or is it probably a better approach to go for a cost equal appro uh comparison um as I said we also looked into the the costs and price performance uh numbers so let's have a quick look on on a cost equal approach so these are the the costs for these instances. Um, if we only have a look at compute and storage, if we would do a holistic approach, of course, we need to consider data transfer, backup, support costs, and so on, but only for compute and storage. And we here we see the hyperscalers are pretty well aligned and the four bars to the right, um, they're also roughly in

**[15:31](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=931s)** the same ballpark, but in a on a lower level, of course. So if we bring them to the same let's say budget ballpark that's of course possible. Um but what does it actually mean regarding the fairness? Well it would mean that the these four bars to the right. So these providers would have double the amount of resources available to match the same or to have a cost equal setup. So that means if we if you look at some results um where they claim it's a cost equal uh benchmarking study, you need to be aware that this probably means that you will have very heterogeneous setups. Um and of course that going to have direct impact on the performance numbers

**[16:20](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=980s)** that you get. Um yeah so we of course we would also could now have a look in that data but um especially in the in the context of cost equal setups um I brought another case study with me that targets a rather let's say modern or recent architecture of database as a services so serverless databases you probably heard a lot of serverless especially in the compute domain but that also is present in the database domain. Um where you basically pay per use in general. Um so the serverless databases abstract the co uh the infrastructure layer and also the

**[17:08](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=1028s)** scaling scaling of the database itself. There are different implementation approaches to it. um in the let's say in the online uh or in the OTP domain it gets more heterogeneous in the OLAP domain but that would be an a talk for on its own but in order or coming back to fairness well uh for a a serverless database it's basically not possible to define a resource equal approach as re resources are completely abstracted by uh the database offer itself. So what you can do is going rather for a a perform uh a cost comparison.

**[18:00](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=1080s)** Um we did that for one study. Um but there's also uh let's say uh a twist to the fairness. So let's see how you can compare um serverless with dedicated debus offers. What you see here is the costs for a dedicated couchbased Capella cluster. So we have four different cluster sizes. Um these are the monthly costs. And now we want to compare the costs to Google Fire Store which is actually a serverless database where you actually pay per issued request against the database. So how can this be done? Um well we need to map the the throughput

**[18:52](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=1132s)** that each of these clusters is able uh to provide for Capella. we need to map that the cost for this kind of throughput to the respective uh settings for Google fire store. So in particular we take the throughput level of couch base per each cluster um calculate the monthly operations that this throughput will will have um map that to Google fire store pricing model and then we have an estimate on what it would cost to have the same throughput that couchbase achieves for Google fire store. And when we now look at the costs, well, we see that can be pretty expensive. Um, in this assumption, we took or we

**[19:43](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=1183s)** assume that we have an 8 hour steady workload over one day. Uh, and it's already well quite expensive compared to a dedicated cluster. um it gets way more expensive if we would assume that this is a 24-hour steady workload, which is of course probably a bit uh an over assumption, but just wanted to showcase how costs might then be um diverging. So um not saying that serverless databases are bad in general. I just wanted to point out that comparing dedicated with serverless databases, it's a tricky uh tricky thing especially when you look at benchmarks um because actually to to have a fair benchmark of dedicated

**[20:32](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=1232s)** versus serverless instances, you need a really specific knowledge on the workload model of your application. So um if it's a steady workload or if it's a fluctuating workload over time um because otherwise it's barely possible to to have a fair comparison of serverless and dedicated database systems. Um it is definitely doable. We recently did that for a large analytic cluster of one of our customers where they were looking into dedicated setup and how that would end up on a serverless version of the same database type. So it's doable but it's a rather challenging approach. So and well there is of course um more

**[21:26](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=1286s)** to it. So there are some uh approaches we haven't went into the real in detail for now. So as I said performance equal benchmarking it's also valid approach comes with some pitfalls itself the workload equal um same same thing and what we didn't talk at all for today is about well fair benchmarking across different database technologies and about different kind of workloads which is probably again um a talk on its own. But coming back to my initial question, so is database benchmarking fair? Actually, what does it mean when you read results

**[22:16](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=1336s)** or when you have to conduct results by yourself? Um well, you need to be aware that it's can only be fair uh in the scope of the of the objective and this needs to be explicitly stated. So for research equal uh benchmarks the then not only the specs are important but also the technical implementation underneath if they're if they're uh publicly available and if not that needs to be clearly stated for the cost equal one which this is basically always possible but it also clearly needs to be stated that this have impact on the on heterogeneous is deployments that you're comparing different kind of

**[23:03](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=1383s)** resource sizes. And for serverless, it gets even harder to have a fair comparison because you need a really clear understanding of the workload model to do a fair comparison. So in summary, um fairness is making the objective explicit when you do benchmarks. Um the assumptions should be transparent. Of course the approach needs to be reproducible and the data has to be public but not only the data because all the technical details and raw data not only some high level um charts or aggregations to have it as fair as it can be these days. So thank you all for uh attending the talk.

**[23:55](https://www.youtube.com/watch?v=_aR4V7ima2Y&t=1435s)** If you're interested more around the database performance topics, uh happy to connect or um also feel free to have a look at our newsletter where we uh continuously publish some insights from our latest studies. So, thanks again and I'm happy to take questions if there are any. >> [applause and cheering]
