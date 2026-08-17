---
id: 598
title: "Building Trust Through Private and Verifiable AI"
slug: building-trust-through-private-and-verifiable-ai
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Security & Privacy"
type: "Keynote/Talk"
stage: "Stage 10 - powered by TikTok"
tags: ["Privacy", "Security"]
speakers: ["Mingshen Sun"]
speaker_companies: ["TikTok"]
day: 1
starts_at: 2026-07-09T08:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=JVtWw3mZz2o
video_id: JVtWw3mZz2o
session_page: https://app.wearedevelopers.com/events/16/session/598
transcript: true
---

# Building Trust Through Private and Verifiable AI

**Mingshen Sun (Research and Engineering Lead — TikTok)**

`Track: Security & Privacy` · `Type: Keynote/Talk` · `Stage: Stage 10 - powered by TikTok`

`#Privacy` `#Security`

[Watch the recording](https://www.youtube.com/watch?v=JVtWw3mZz2o) · [Session page](https://app.wearedevelopers.com/events/16/session/598)

## Abstract

AI has transformed how people learn, work and live - automating complex tasks and extracting insight from massive datasets. But most powerful AI today (especially large language models) runs on server-class hardware, which typically means user prompts and context must be visible to the service provider to be processed. While acceptable for some cases, it is still challenging with highly sensitive data where users expect similar protections as end-to-end encryption. Private Verifiable Compute (Project PVC) is an open source project that can enable users to initiate a request to a private and verifiable environment for context-aware AI processing with sensitive data, where no one, including service providers, can access them. With PVC in the cloud environment, it unleashes full potentials of AI hardware in the data center for complex AI tasks, such as large language models (LLMs), generative AI and beyond, while guaranteeing user privacy and verifiable transparency.

## Speakers

### Mingshen Sun

*Research and Engineering Lead — TikTok*

Mingshen is leading application and innovations of the trusted/confidential computing technologies at TikTok. Previously, Mingshen worked on multiple projects towards building safe, secure and trustworthy systems. Notably, he was fortunate to initiate the Apache Teaclave open-source project. Mingshen got his PhD from the Chinese University of Hong Kong, and has broad research experience on topics at the intersection of privacy and security, operating systems, and programming languages. He also serves on Technical Advisory Council of Confidential Computing Consortium.

## Transcript

*2,817 words · source: yt (en)*

**[0:00](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=0s)** So, ladies and gentlemen, let's give a round of applause to our speaker for today at 10:10 section building trust through private and verifiable AI by TikTok. Our speaker is Kam Ming Shawn Sun. Let's give him a round of applause. >> Um this is my third time in the WeAreDevelopers World Congress in Berlin. It was a great experience in the last 2 years and I hope you enjoy today's talk in this year. So, today I'm going to bring you a topic uh how we have to build the trust through a private and verifiable AI. I'll start with background of why we need that and then I will talk a little bit about how we are achieving this and uh

**[0:49](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=49s)** I think we have time to have a a little demo. You will see how it works and have a hands-on experience of how the private AI shows in the demo. So, let's get started. So, we have seen that AI has transformed how people learn, work, and live. It helps us to automate complex tasks and extracting insights from massive massive data sets. If you follow recent news, companies introduces new health-related features in one of the reports saying health is one of the most common ways people use GBT based on their

**[1:38](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=98s)** the identified analysis of the conversation over over 230 million people globally ask health and wellness-related questions. So, to understand what is a personal health looks like and how to do the treatment, for example. So, uh people are sharing personal and sensitive health information with the service providers. Um the questions comes to our users, how to safeguard how to ensure the safeguarding of the life cycle of the health data, sensitive data I rest in transit and in processing. So, this is a very challenging industry problem and uh because we know uh the most powerful AI today, especially large

**[2:30](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=150s)** language models, uh it runs on server-side uh class uh hardwares, uh but not our cell phone, right? So, which basically means uh your prompts, your health uh information, sensitive data will be transferred to the uh cloud service provider, to the service provider who have the powerful GPUs can process your data. Uh well, sometimes uh acceptable for for some use cases, but uh for the sensitive sensitive data, it is still very challenge uh very challenging uh with this data, um which uh we all expect a similar protection uh as end-to-end encryption. So, um uh these uh questions we like to answer

**[3:20](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=200s)** with uh private verifiable uh project project. Okay, uh uh we have some background of how uh AI works, but here's a typical workflow uh how how how AI agent uh work today. Uh let's use a health uh care questions as an example. A user we uh we usually on the client side on the device uh uh ask questions, the palm prompts. Uh for example, I'm not feeling well uh of my legs, and what should I do? And uh some relevant context you already maybe we put our medical records, uh some physical exam reports, and uh then uh the

**[4:09](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=249s)** uh information, the data, and the context will be sent to the remote servers. And uh uh the remote server will process the prompt and the context together to help user to uh diagnose the sick symptoms. Uh during the process, uh there are multiple places that uh your uh sensitive information might be leaked or misused. For example, uh the administrator with higher privilege uh um uh in the server side, uh they have ability to access the data in the cluster, uh and uh the algorithm and uh model owners uh uh sometimes they need to debug and the uh may might misuse the data for other purpose. Uh even though um

**[4:57](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=297s)** we have term of service, right? Uh and user concerned, so you you don't know, and you want to know whether the service provider uh uh enforce the uh policy or I intentionally misuse the data. So, uh our ask is is there any technical solution to guarantee that uh the user data uh cannot be seen, uh cannot be accessed by service providers, and uh also uh they can provide third party uh uh verifiable uh proof um that can be remotely attested um the privacy and the security claims are guaranteed uh during the process.

**[5:46](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=346s)** Um so, we uh uh in this project we are leveraging concept of a technology called trusted computing something sometimes also called confidential computing. Um the underlying technology is trusted execution environment to protect the data process data in use. So, um The trusted execution environment is hardware based isolation technology provided by the hardware and it can protect the data processed in the server in CPU and GPU so that the infrastructure providers the employees SREs cannot access the data in use.

**[6:35](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=395s)** Uh besides that the good the nice part is the uh the chip vendors the trusted execution environments can issue a hardware signed remote attestation report to prove that the data is processed by inside the trusted execution environment and there's data protection mechanism in place in the software. So, that's the that's that's why trusted execution environment is a key technology we are leveraging here. So, uh in in specifically I feel if you interview of computing computer architecture there's a special unit

**[7:24](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=444s)** in the processor both CPU and the GPU called memory encryption agent. Uh for every data fetched from memory and emit to the memory the data will be encrypted and decrypted inside the chip. So, uh no one can look uh look at the mem- By looking at the memory, no one can access the data. Uh so, the data is only visible to the processor during the computation in silicon. Um and uh also for the remote attestation uh mechanism, uh the trusted execution environment uh the chip vendor will uh measure the software uh and the data processed in the environment, and uh prove its software identity, and the hardware

**[8:13](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=493s)** execution environment status, proving that this is a secure environment, and the identity is uh trusted software. So, so they so that they can provide uh software transparency, uh auditabilities, and uh assure certain uh privacy and the security properties of the software. Okay, so with that, uh this uh prompt will be encrypted, and uh uh the uh the prompt will be encrypted, and there's no access from employee, and there'll be a attestation report. So, the in high level uh when we design this project, we will Our goal is we still

**[9:02](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=542s)** want to use the powerful cloud AI on sensitive data. Uh we want to make sure uh no one uh not even the platform provider can see our uh what you are uh sent and what I in processed. So, we want to provide provide uh data accessing and processing, and anonymize your identity is separated from the request, and uh verify ability. So, you don't uh you don't have to uh provide the software, and uh but uh the auditor can remote attested the identity of the software in the remote server. So, um, uh, this is, uh, the some of the, uh, technical guarantees we uh, put in place in this

**[9:50](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=590s)** project. Uh, mainly, uh, in three part: private processing, private storage, and the verifiable, uh, transparency. So, for private processing, we, uh, define these data security guarantees, uh, price, uh, comprehensive security practices, uh, to protect the confidentiality, integrity, uh, of, uh, the complete data life cycle from the end to end. So, uh, include data at rest, data in transit, and data in use. And, uh, privacy-preserving, uh, meaning, uh, in addition to, uh, the uh, the general security protection, we apply comprehensive, uh, uh, privacy-enhancing technologies to ensure, uh, traffic anonymity and, uh, privacy-preserving debuggability and

**[10:38](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=638s)** operations. Uh, enforce, uh, enforce, uh, enforcement guarantees, uh, that basically means, uh, not only we have the process guarantees, we also enforce in, uh, the technical ways, because we are leveraging the, uh, trusted execution environments. Uh, it can help us to ensure only authorized and the cryptographically measured software will be loaded inside the environment and the, uh, and the execute with uh, user data. And the last one, uh, in private processing is called no privilege access. Uh, we, uh, we provide a hardened, uh, operating system in the confidential VM. We ensure no, um, uh, privileged interface, uh, that might enable the, uh, uh,

**[11:28](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=688s)** administrator access. Uh, so, that's the three, uh, main, uh security guarantees we provide in uh in pro- in processing. And for private storage, we uh we understand that there's uh uh some use cases. For example, you want to uh use your user context to uh uh and the prompt as well to do some AI uh tasks. Uh uh Healthcare example, you might provide the physical exam uh reports. So we want to store this uh user uploaded uh context data uh and uh when do processing uh and the data is uh processing such trusted execution environment. But when

**[12:15](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=735s)** uh as storage, we use a user-controlled key to encrypt the data and to make sure no one else no one can access the data uh at uh rest. And last one is verifiable transparency, which is uh uh a key uh feature that uh the whole projects provide uh because uh the question uh in the first I I raised, how can we prove that uh uh your data is processing remote but cannot be accessed. So because we uh we have the code transparency and the assurance to making uh uh to enabling third-party auditing and uh maintain the uh highest level of software assurance and uh supply chain assurance. And uh secondly, uh

**[13:05](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=785s)** verifiable transparency. So we want to make sure all the privacy guarantees, the security guarantees are verifiable uh by third parties. Uh How we achieve through remote attestation. So because the code and the its execution environment uh can be remotely attested by uh the remote attestation mechanism. And because of because the mechanism is provided by the hardware vendors, so uh that's that basically means third party can verify this property independently without trusting the service provider. Um so this is a very general diagram uh we are uh deploying uh and designing uh in this project. Uh you can see uh

**[13:54](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=834s)** anonymous authentication authentication and routing, private private processing and the storage, transparency release, and the verifiable transparency. So uh for each component, there are uh a lot of details. Uh I'll pick several things as an example. For anonymous routing, we are using oblivious HTTP protocols to make sure uh the anonymity of the traffic. And uh uh for uh like private storage, I have already mentioned is user user-controlled encryption keys. And for trusted uh for the transparency release, we apply trusted building systems to make sure this IC pipeline is uh uh trusted. And uh we also apply a

**[14:43](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=883s)** reproducible build to make sure the supply chain uh assurance and the security. And that's uh part of the work we have already done. And the last one is verifiable transparency. Uh uh it's will I'll talk about that later. Um now don't we are not only uh uh deploy the uh system in trusted execution environment, we also open source the software. So you can build by yourself and uh test by yourself. Okay. So we uh we have a look at the some of details of the technical guarantees, but from users and business perspective, what this project bring us. Uh first, it helps us to build

**[15:32](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=932s)** trust because the PV C the private viable compute project leverages the privacy enhancing technology, for example, confidential computing. With nature of privacy, transparency, and auditability, it showcases our commitment maintaining the technical advancement in PET in private AI processing. And the secondly, it can help us to mitigate risks. Because of the design, the security design, the privacy designs by default, the sensitive data is not visible even to the service providers. And additionally, it can be a remotely tested independently. And last one, unblock some business innovations because the AI features and the most powerful models deployed on the

**[16:23](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=983s)** cloud. This kind of security and privacy or design features can help us to unblock new business features and innovations. Um Yeah, that's the high-level propositions. At last, as I mentioned, this is this project is an open-source project. It has been published in December 2025. And we we we have a very comprehensive document to guide you through to try local deployment with a mini cube. So, you don't have to use any like confidential computing environment just to to experience the how it works. And

**[17:14](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=1034s)** secondly, if you really want to use, we also uh provide uh several deployment deployment uh like measures. So, you can deploy on on the cloud or on premise and uh hybrid uh as well. And uh also we uh have a document talk you through how to do the reproducible build uh and uh we have a transparent code release. So, if you are interested, you can uh uh look at the the website and uh the code as well. So, last uh as I promised, we will have a short live demo. So, before that, I will uh go through what you will see uh in the demo. And

**[18:03](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=1083s)** uh firstly, we will we use uh very general AI chat box uh chat agent as example. So, you will uh talk with an agent uh deployed in a remote in the uh trusted execution environment and uh with this private uh uh anonymization uh routings and private processing uh and the uh private storage uh as I mentioned. Then uh uh what I will show you in the demo as well is the remote attestation. So, how people uh the end user can see the remote attestation report and uh there's a lot of details uh I think uh in the demo, you probably cannot look in the details, but I can uh have a a simple

**[18:54](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=1134s)** explain of what it is. So, you will see uh the CPU attestation report and GPU attestation report. Uh in uh both of them contain the uh uh execution environment status whether it is uh vulnerable status vulnerable environment or whether it is a secure environment. And also, you will see some measurements. And the measurements means the software deployed at the wrong time. Let's take an example. We use a model and we use like VLLM to serve the model and the measurement will contains

**[19:41](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=1181s)** the model hash and the software the image of the VLLM hash. And as well as the operating system in the confidential VM. So, the demo will be very quick. So, if you you want to see details, of course, you can you can check online to try by yourself. Okay, next slide. Okay, start. Okay, so uh So, here this is a website. You can see this a green bar. I just want to show this is confidential computing environment and uh

**[20:27](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=1227s)** I'm asking a question, what is confidential computing? It can process in the cloud and give the output and the reasoning process. And then I inspect the traffic between the client and the server. So, reload the page and if you see the network, there's a test station endpoint. And if you see the response of this test station, you'll see a lot of details of the remote environment. The CPU means CPU attestation and GPU GPU attestation. So, uh you can see a lot of details of the measurement, uh the policies,

**[21:15](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=1275s)** uh the uh TCB meaning uh trusted computing base version, uh meaning the like full mirror version whether it is updated or not. And uh all the information will be uh included inside and designed by uh Intel because we are using the Intel CPU uh in this use case. And here uh we are using NVIDIA GPU in this use case, you see all the NVIDIA attestation report as well. Uh so, you can also upload any uh contacts uh and they will encrypted by the user key. So, yes, that's uh the uh short demo of the private viable viable compute project. Uh you can always deploy this demo uh in a cloud uh environment like

**[22:03](https://www.youtube.com/watch?v=JVtWw3mZz2o&t=1323s)** GCP and and others. Uh uh I think that's wrap up my talk. Thanks so much and uh if you have any questions, I'll be in the booth uh in in the back. Uh you will see our yogurt uh uh food truck and you can enjoy the yogurt and ask questions. I'll be there. Thank you so much.
