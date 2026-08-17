---
id: 697
title: "Beyond authentication: an open-source trust model for the agentic web"
slug: beyond-authentication-an-open-source-trust-model-for-the
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Quality & Reliability"
type: "Keynote/Talk"
stage: "Stage 13"
tags: ["AI Standards", "Authentication", "AWS", "Agents", "Agentic AI", "Infrastructure", "Open Source", "Software Architecture"]
speakers: ["Alexander Günsche", "Sabrina Engling"]
speaker_companies: ["AWS", "Trusted Shops SE"]
day: 1
starts_at: 2026-07-09T11:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=5SWCbrxp8Z4
video_id: 5SWCbrxp8Z4
session_page: https://app.wearedevelopers.com/events/16/session/697
transcript: true
---

# Beyond authentication: an open-source trust model for the agentic web

**Alexander Günsche (Senior Solutions Architect — AWS), Sabrina Engling (AI Lead — Trusted Shops SE)**

`Track: Quality & Reliability` · `Type: Keynote/Talk` · `Stage: Stage 13`

`#AI Standards` `#Authentication` `#AWS` `#Agents` `#Agentic AI` `#Infrastructure` `#Open Source` `#Software Architecture`

[Watch the recording](https://www.youtube.com/watch?v=5SWCbrxp8Z4) · [Session page](https://app.wearedevelopers.com/events/16/session/697)

## Abstract

Authenticating an agent tells you who it is, but not whether to let it transact, access data, or act on a user's behalf. As autonomous agents begin crossing organisational boundaries, the systems they reach face a binary choice: block all agent traffic or accept it without verification - neither of which scales as agent traffic grows.

TSAI (Trust Signals for Agentic Interactions) is an open source protocol that fills this gap. Built on W3C Verifiable Credentials and Decentralised Identifiers (DIDs), it carries trust signals beyond identity - reputation, economic stake, authorization, and endorsements - in cryptographically signed credentials that any system can verify offline. Independent Trust Authorities issue them and agents present them when accessing a service, while receiving systems make their own access decisions based on the signals. Credentials describe the agent, not the user, which preserves user privacy and keeps existing user authentication unchanged.

In this talk, we walk through the architecture - the four-tier trust model that scales from offline verification at low risk to real-time checks at high stakes, the credential format and lifecycle, and how TSAI composes with agent protocols like MCP and A2A. TSAI is developed by AWS and Trusted Shops, combining agent infrastructure expertise with decades of online trust certification.

## Speakers

### Alexander Günsche

*Senior Solutions Architect — AWS*

Alex is a Senior Solutions Architect at AWS with 20 years of IT experience in expert and leadership roles. He is a strong advocate of agile and DevOps practices, and he enjoys seeing serverless, cloud-native and event-driven architectures deployed at scale. He has delivered large transformation projects and successfully developed own and customers’ businesses. As an international speaker, he has held advanced technology sessions at a wide range of events.

### Sabrina Engling

*AI Lead — Trusted Shops SE*

Sabrina Engling leads the AI Solutions Team at Trusted Shops and drives AI adoption and innovation across the entire company. Her focus is on scalable AI solutions, AI operations, and agentic commerce. She combines technical expertise with strategic business acumen, bringing together both perspectives - from the architecture of scalable AI systems to business value.

Beyond her corporate role, Sabrina is a dedicated advocate for tech education and serves as Chairwoman of the NGO TechLabs, helping thousands of people build digital skills. As an AWS Commmunity Builder for AI Engineering, alumna of the AWS She Builds mentoring program, a certified AI Manager, and a recent AI hackathon winner, she is committed to empowering more women to take the leap into AI and cloud technologies.

## Transcript

*1,633 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=3s)** This reputation mechanism in particular will work in practice. >> Exactly. Because also at Trusted Shops for 25 years we collect feedback and this is exactly also what we want to do here with the reputation feedback loop. So, reputation is a special category of trust signal because unlike others it is dynamic. So, the trust authority in this case, for example Trusted Shops, is not part of the direct interaction between the agent and the service provider. So, it's a neutral independent trust authority. But after the transaction is complete, the trust authority will accept feedback from both parties about their interaction because trust is always bidirectional.

**[0:51](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=51s)** So, the agent rates the service provider and the service provider rates the agent. And this two-sided feedback is very important because it allows the trust authority to mitigate bias and manipulation attempts. For example, one agent or one service provider could constantly provide bad feedback or constantly provide good feedback and then the trust authority can weigh that it probably against feedback from other actors. So, we have feedback from several service providers for the same agent and also from the from several agents for the same service provider. And so, we can also see if an AI agent or a service provider could arrange fake transaction and then give us positive

**[1:40](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=100s)** feedback so we would recognize this. And over the time we have a lot of feedback and an agent will build a reputation across multiple service providers. So, the behavior rating has two components. One is the average score, the other is the total number of interaction. And in in a more advanced stage, we also can say, "Hey, this agent is so trustworthy, we can guarantee it and also can offer an insurance and from the trust authority that this agent is trustworthy." And beyond those main actors of agentic trust landscape, so we already see and can also foresee other stakeholders entities because we have the trust authority, maybe also different trust authorities because it's an open source

**[2:28](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=148s)** protocol, but trusted shops one of them and the first one and several agent operators and service providers, but we also can see already different other stakeholder entities either because trust is important to them or they can contribute to increasing the level of trust for other parties. So, providing additional data about this agent behavior, for example, observability solutions record how agents behave in production and offer metrics as a service or firewalls and gateways enforce trust policies at the edge before requests reach the application, but also agent marketplaces list and distribute agents that users and businesses can adopt. Or even more important also for payment and agent

**[3:17](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=197s)** wallet, let agent hold funds and pay for the service they use. So, all for these for all of these stakeholder entities, it's important that we have a certain trust layer there. And we hope you enjoyed the talk. So, please scan this QR code with further materials and please do us a favor and also rate the talk and give us feedback via the feedback survey linked on the landing page and you also find the specs, the presentation, but also get in touch with us. So, we are happy to hear your thoughts or feedback, remarks, or if you want to contribute to this initiative. So, with that, thank you very much, and I think now it's time for questions if there are any. >> Thank you.

**[4:07](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=247s)** >> [applause] >> OKAY. THANK YOU GUYS. VERY INTERESTING. WE have 5 minutes for questions if someone has one. Yeah, we have one over there. I will hand you the microphone. >> In the meantime, take 30 seconds for a survey that would be very kind. >> You can also put your questions on the app. >> Thank you very much. That's quite insightful. I have a question around say you wanted to get it or your and public agent is not trustworthy or verified over a period of time. And the third party, right? You're not verifying the human and the third party then picks up this agent and you reuse this agent to continue transaction on behalf of the

**[4:56](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=296s)** user. Now, is there a way to detect this behavior or you completely trust the agent without considering everything outside of the agent circle? >> Sorry, which behavior do you mean? >> I stole some of the person's laptop and used the laptop. So, a third party that isn't in the loop, right? Are you completely forgetting about this or you're focusing on just the agent? So, the agent remains trustworthy throughout or there are cases where a user can invalidate the agent trust. He knows that the laptop is stolen. So, how can he invalidate that trust? >> Oh, that's a good question. So, the there is a revocation list. So, we didn't go into every little detail, but there is a revocation mechanism for the credentials. These credentials are short-lived anyway, 1 hour right now.

**[5:43](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=343s)** So, if you steal a credential and want to present it to somewhere else, then it will not last very long. But if you immediately inform a trust authority, they can upload a verification status. Ideally, for high-stakes transactions, the service provider would check that revocation list. But if a low-stake transaction, the question is always how big is the risk, how big is the damage. But yes, the mechanism exists for revocations. >> Yeah. And this is exactly the reason why we have this feedback loop, and this is also making this protocol so special and unique because this uh enables us to do this, right? So, if we only have identity, this is not possible because identity is yeah, kind of static, but reputation and behavior is dynamic, and then we can really revoke this trustworthiness or trust uh level from the agent.

**[6:32](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=392s)** >> Any more questions? >> question? Yeah, here. Have you handed over your Have you handed over your proposal to any standardization body already, and which one? It may >> Maybe. So, right now, this is driven as a collaboration here with an open-source approach, and we would be ready to hand over stewardship. It could be IETF, but as you've seen, most of those things are already standardized, and we don't want to reinvent the wheel or do a standards track just for our own ego. So, if we find out through that work that is worth to have a separate standard, it could be W3, or it could be IETF. Just after uh as a side note, there's a funny side note. There are two standards competing for verifiable credential standards. So,

**[7:21](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=441s)** there's one from W3, verifiable credentials, and there's one from IETF with this RFC 9901. Uh just in case you go and research, you might even even uh web pages discussing this, even agents having that knowledge, but they confuse the two of them. But it makes would would make sense to build on one of those ecosystems. Right now, it's IETF, but uh we see also make sense for W3. >> Okay, thank you. We have another questions over here. >> Uh Karl from Estonian Bank LHVB. I have a question about uh what's your take on credential delegation? >> Sorry? >> Credential delegation. No, it's it's a workload. We we we just give the workload and it may be

**[8:08](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=488s)** eventually delegated to some other agent. >> You mean like a multi-agent architecture? >> Yes. >> That makes sense. So, it would in in this scenario, you would invoke the other agent like a service provider. So, the other agent would offer its service, and of course, you can integrate this with HUA protocol. The digital token would be forward because in the end, it's a signing key. So, on the payload level, on the SD-JWT level, you can propagate that, but you cannot merge it with another one because that is of course part of that other agent's identity. So, in terms of disclosing that, yes. In terms of merging it, no, because in the end, the sub-agent would have to have its own identity. >> Have you considered any other token,

**[8:54](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=534s)** let's say Eclipse Biscuit Token, which is delegatable and it has third-party attributes and etc.? >> Can you maybe give an example? >> Uh do you know Eclipse Biscuit Token? No? It's a Biscuit Biscuit Token. It's Eclipse has a standard >> For Eclipse, the idea >> No, no, it's not this Eclipse is the foundation is owning it. Yeah, okay. It's a Biscuit Token which is delegatable. It's the same as it's a Macaroon Tokens which as well delegatable, but they're not that distributed. So, there are no it's all with hashing methods, but now there's no uh uh private private key infrastructure there which is makes it decentralized. >> Okay, I'm not sure. to I would have to look it up. >> Okay, thank you.

**[9:42](https://www.youtube.com/watch?v=5SWCbrxp8Z4&t=582s)** >> You need it? >> Okay, thank you. I think we have uh a bit less than a minute. Any more questions? No? Well, maybe I have a curiosity. It's why did you use the three dots as ASCII? It really looked like a hidden code block to me. >> I did not choose them or we did not choose them. As I mentioned, this is part of the 19901 RFC. And I myself I kind of researched it and then I saw these three dots and said, "What are they hiding? What What is there?" Until I realized it's literally three dots. That's the convention for them. >> Okay, thank you. >> It is what it is. >> Then, if we have no more questions, that's it. Thank you for coming. >> Thank you.
