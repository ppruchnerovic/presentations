---
id: 616
title: "Your Distributed System Just Got a Brain. Now What?"
slug: your-distributed-system-just-got-a-brain-now-what
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Software Architecture"
type: "Lightning Talk"
stage: "Airstream 2"
tags: ["AI Standards", "Cross-Platform", "Distributed Systems", "Large Language Models (LLMs)", "Microservices", "Scaling", "System Design"]
speakers: ["Marcin Makowski"]
speaker_companies: ["BeOne"]
day: 1
starts_at: 2026-07-09T08:40:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=VBDnbJx2EEE
video_id: VBDnbJx2EEE
session_page: https://app.wearedevelopers.com/events/16/session/616
transcript: true
---

# Your Distributed System Just Got a Brain. Now What?

**Marcin Makowski (CEO — BeOne)**

`Track: Software Architecture` · `Type: Lightning Talk` · `Stage: Airstream 2`

`#AI Standards` `#Cross-Platform` `#Distributed Systems` `#Large Language Models (LLMs)` `#Microservices` `#Scaling` `#System Design`

[Watch the recording](https://www.youtube.com/watch?v=VBDnbJx2EEE) · [Session page](https://app.wearedevelopers.com/events/16/session/616)

## Abstract

Distributed systems were designed around predictable behavior.

Retries assume idempotency. State transitions assume determinism. Consistency models assume repeatable outcomes.

Then we added AI.

Now:
- the same input may produce different outputs
- retries may change decisions
- context mutates state unpredictably
- model upgrades alter behavior silently
- deterministic workflows depend on probabilistic components

Your distributed system just got a brain.
And distributed systems don’t tolerate ambiguity.

In this session, we explore what really changes when AI becomes part of a distributed architecture.

We’ll cover:
- how probabilistic inference breaks retry semantics
- why idempotency assumptions fail with LLMs
- separating state from inference
- deterministic checkpoints in AI workflows
- replayable execution paths
- handling model version drift
- designing hybrid architectures where AI proposes - but systems enforce

AI doesn’t just add intelligence. It changes the fundamental assumptions of your system design.

If you treat AI as just another microservice, your architecture will eventually collapse.

## Speakers

### Marcin Makowski

*CEO — BeOne*

Marcin Makowski is CEO at BeOne and a software architect focused on building production-grade AI and orchestration platforms. With over 20 years of experience in distributed systems, enterprise automation, and large-scale process execution, he specializes in designing deterministic architectures in non-deterministic environments.
Marcin works at the intersection of AI infrastructure, workflow orchestration, and decision modeling. His recent focus includes LLM platform engineering, model gateways, hybrid retrieval architectures, and building reproducible AI systems with strong observability and auditability guarantees.
He is a strong advocate of open ecosystems and engineering-first approaches to AI adoption. Instead of treating AI as a feature, he designs it as a runtime component that must meet the same standards of reliability, scalability, and traceability as any other production system.
Marcin co-authored research on dynamic decision model generation for tax compliance (accepted at ISD 2025) and regularly speaks about distributed systems, AI platform design, and deterministic orchestration in intelligent systems.

## Transcript

*1,752 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=0s)** Okay, it was good morning everyone. I have you I hope you grab the your coffees now. I will I will tell you something about AI again but AI in this area is on the to have an attendance at this presentation not something we will talk about during the whole presentation so I I hope it will be also interesting for you. Oh, give me a second. So, Okay. So, we started to talk about AI but not about what AI can do. So, we would like to begin with a different question. What changes when probabilistic driven become becomes a part of distributed production system? During this talk I will show you three things. First, why AI breaks some of the reliability assumptions we have used for years. Second, how AI generated rules and processes can be governed before

**[1:09](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=69s)** they affect production. Third, why an open orchestration runtime matters. So, let's start about that. Have you heard about Camunda? For example, can you show us who who who knows Camunda? Or Nathan? Okay. So, I will talk about the a bit later so maybe you will recognize some things from this parts of uh uh IT. So, when we call a service it times out so we can call it again. When a deterministic service we expect the same command to produce the same result. In that world, retry is form of control. But in LLM, it's not a deterministic service. The same request with the same context may produce results A, B, or C. So, all three results may even sound reasonable. So, a timeout followed by the retry and or not simply repeat the operation. It may create new business decision. The

**[2:20](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=140s)** problem is not that the AI can be wrong. Um The deeper problem is that that AI can be definitely differently right. So, which is uh great during brainstorming, is slightly less great when the model is approving, for example, refu- refunds. This means determinism is not longer automatic. The surrounding architecture must restore it. And this is main topic of this uh of this presentation. Now, so the same input should lead to the same transition and to the same audit trial. This contract supports the reliability mechanism we use every day. Retry assumes the that repeating an operation repeats the same effect. Uh so, in in potency assumes that we can prevent duplicate outcomes. Replay assumes that we can reconstruct what happened and audit assumes what we can explain why the state changed. The mechanism work because the

**[3:29](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=209s)** executed step is sufficiently predictable. AI introduces the a probabilistic dependency into this deterministic architecture. We should not pretend the inference in is deterministic. Instead, we should control what happened around it. Um So, oops, next slide. Okay. So so So AI output should never mutate business state directly, as you can see. The AI proposed explicit business rules validate the proposal. The process decides whether the transition is allowed the checkpoint because the approved decision only then does the system commit the business state. The important decision is this then AI answer is not yet production decision. It's not It's only a proposal that must pass through a controlled path. We are not trying to make the model deterministic. We are restoring determinism around the model. Interference can vary. State must not.

**[4:34](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=274s)** Okay. So, uh Now you can see what we have before an in irre- irreversible action, we must freeze the exact decision that the system is allowed to execute. So, the sequence is important. First AI uh Uh okay, maybe I have different slide here. Okay. First, we need uh First, AI creates a proposal, the explicit rules validate it, and we create decision checkpoint now, and uh only after do we this Only after that uh do we execute the checkpoint stores the model version, prompt version, context reference, proposal validator version, and approved outcome. It's not just another lock line. It's the version contract the process is allowed to execute. So, tomorrow the model may change, the prompt may change, the supporting document may change, but yesterday decision must still have stable and versioned explanation. The

**[5:42](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=342s)** model may drift, the recorded decision must not. Okay. And But, the next change is much larger. We will not only execute task, AI will begin to generate the rules of execution. It can read document policies procedures prompts forms and events from this input. It can propose decision rules, DMN tables, BPMN processes, users, task forms, agent flows, and integration. This changes the role of AI. It's not longer just returning the answer, it's producing models that may define how the enterprise operates. But, generated logic is not executable logic. It's not yet. Before we run, it must become explicit, reviewable, testable, and approved. So, in next slide, we'll show it. Okay. We have an Imagine that AI reads a contract, for example. The contract says that orders above the 100,000 euros require CFO approval. It also

**[6:50](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=410s)** defines a payment terms and rules for such interest. First, it I extract the relevant facts. Then, proposes an explicit DMN decision table. That decision becomes a part of BPMN process. The process creates the appropriate approval task. It sends notification, updates the ERP system. It stores the evidence in the document repository. So, and it produces status report. This is no longer simple document extraction. Unstructured documents has become executable logic and uh that creates an important question. If AI generate the rules, who approve the contract that is now controlling production? AI generate business logic is useful, but it also is uh executable uh risk. So, we have an uh human in the loop, you can see. Governance become Governance become the the main problem. Generate that BPM BPM and DMN forms, AI agents, and

**[7:57](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=477s)** integration must not move directly into production. First, AI suggest possible models, then humans review, test, validate, and approve them. Every accepted model receives a version. Only the approved version is deployed to the runtime, and every execution is recorded. They give us a simple life cycle. Suggest, validate, version execute audit. Uh we must always be able to answer which document generated this rule, which version was approved, which process is used, and uh we can um reconstruct the the decision later. AI can suggest the model. Production needs the contract. So, what we prepared is uh it leads to the different way of building enterprise software. The model the element that's frequently changed that must remain visible. Processes are modeled in the BPMN, decisions are modeled in DMN, human interactions

**[9:02](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=542s)** modeled for forms, documents, evidence are represented as a context model. AI can and agent behavior represented as an explicit AI flows. These are not five unrelated editors. They are five views of the same executable business system. The benefit is that rule, process form content structure, or AI flow can evolve through without rebuilding the entire application. This does not mean modeling instead of coding. It means modeling what change and coding what differentiates. Okay. Okay. So, we prepared an environment at B1. This is the direction we are building. An open modeling environment that extends software development which with elements that should not always be hard hardcoded. LangFlow is used for AI flows and agent logic. Nathan connects API systems, events, and automation. Forms provide a human interactions. Alfresco stores documents, versions, content models, and evidence. Operate on

**[10:11](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=611s)** execute BPMNs, process and DMN decision. B1 connects this this open source building blocks into one governed environment. This is not closed local platform that replaces engineering. This is a model open model driven layer that work alongside the engineering because the components are open and reprocessable. Teams can evolve the architecture without tying every layer to one vendor roadmap. From coding only delivery we move toward model driven delivery. So, one component has specially responsibility. It turns approved model into durable enterprise execution. Operate on is not just another workflow engine. It's the open execution layer between generated business logic and the real enterprise state. BPMN, DMN rules, forms, and agent flows might be generated and or updated with AI, but only approved contracts should enter the runtime. Operate on creates task. It handles events. It evaluates

**[11:19](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=679s)** decisions, it maintains process state, and it represents the audit trail. For enterprise AI, the execution layer must be open, deterministic, inspectable, and auditable. So, it should also remain under the control of the engineering team. Some teams want a complete platform they must adapt to. Operate represents a different path and operate an open runtime foundation that teams can build around and own. AI generates possibilities to create and execute contracts. That's why the operating matters for enterprise AI. So, so far, oops. Okay. Uh this is developer conference, so I need to show something in Docker and the Maven. So, let me show what the operator looks like from a developer's perspective. Operate is a Java runtime that can be embedded in directly in in an application, integrates Spring Boot, Quarkus,

**[12:24](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=744s)** Jakarta. It also run independently in a Docker Kubernetes. It also supports all these models I mentioned. It is licensed under Apache 2.0. There are no license fees, no usage limits, no open core splits. For existing Camunda 7 users, Operate provides compatible for the REST APIs, database schemas, deployable models together with an open right migration path. Okay. So, the above the project follows an active delivery model with regular patches, feature releases, SBOM generation, and database upgrade testing. Operate is open not only modeling level. It's open all the way down to the runtime and source code. So, finally, um what I want to say, do not deploy a brain without a nervous system. Enterprise AI should not silently rewrite the rules of the enterprise. AI proposes systems and force orchestration remembers generated logic must remain

**[13:32](https://www.youtube.com/watch?v=VBDnbJx2EEE&t=812s)** explicit. Decision must be validated. Execution must be controlled and evidence must be preserved. The future of enterprise AI is not only a smarter chatbot, it's open, governed, executable, and auditable business logic. So, thank you very much. Apologize for the problem. >> [applause] >> HELLO. MARTIN, THANK YOU VERY MUCH FOR showing us this and well, technical problems can happen. Thank you. >> Okay. >> Lots of loud applause. >> Uh another note, if you want to join to our open source project operator, we have a free t-shirts for you. So enjoy. >> Cool. Great. Thank you.
