---
id: 618
title: "Scaling GraphRAG: Efficient Knowledge Retrieval for AI"
slug: scaling-graphrag-efficient-knowledge-retrieval-for-ai
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Engineering"
type: "Keynote/Talk"
stage: "Stage 1"
tags: ["Agentic AI", "Retrieval-Augmented Generation (RAG)"]
speakers: ["Gal Shubeli"]
speaker_companies: ["FalkorDB"]
day: 1
starts_at: 2026-07-09T08:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=W5k-Rbou4t4
video_id: W5k-Rbou4t4
session_page: https://app.wearedevelopers.com/events/16/session/618
transcript: true
---

# Scaling GraphRAG: Efficient Knowledge Retrieval for AI

**Gal Shubeli (AI Engineer — FalkorDB)**

`Track: AI Engineering` · `Type: Keynote/Talk` · `Stage: Stage 1`

`#Agentic AI` `#Retrieval-Augmented Generation (RAG)`

[Watch the recording](https://www.youtube.com/watch?v=W5k-Rbou4t4) · [Session page](https://app.wearedevelopers.com/events/16/session/618)

## Abstract

This talk focuses on GraphRAG, an advanced Retrieval-Augmented Generation method that represents knowledge as interconnected nodes. We'll get into its architecture, implementation challenges, and performance gains in multi-hop reasoning tasks. Learn how GraphRAG is transforming knowledge management for large language models, improving accuracy and coherence in complex inference scenarios.

The talk is ideal for AI engineers, ML researchers, and developers working on knowledge-intensive NLP tasks, chatbots, question-answering systems, or any application requiring complex reasoning and factual accuracy from LLMs.

## Speakers

### Gal Shubeli

*AI Engineer — FalkorDB*

Gal Shubeli is a Software and AI Engineer at FalkorDB, building graph-powered retrieval systems for AI. He works on GraphRAG, modeling knowledge as interconnected nodes so LLMs can reason across multiple hops with greater accuracy and coherence. With experience developing machine learning and computer vision systems for medical ultrasound, and an MSc in Electrical Engineering from Ben-Gurion University, Gal is passionate about transforming cutting-edge AI research into practical, real-world applications.

## Transcript

*2,816 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=3s)** Pleasure to be here. All right. Good morning. You came here today for scanning graph rag efficient knowledge retrieval for AI. And it will be. I promise. We will get to the meat and potatoes. But before efficiency, I want to talk with you about accuracy. Cuz we all know how important it is. So we will we will do it backwards. First, how accurate graph rag is. Then, how efficient it is. I am Gaetano Bellini. I am an AI engineer at Falco DB. And I build knowledge graphs for AI. And it's not working.

**[0:58](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=58s)** >> [laughter] >> Yeah, thank you. Look at this number, 95%. That's the share of enterprise generative AI pilots that, according to MIT 2025 report, deliver no measurable return. 95% never get into production. And when you dig into why, it's almost never the model's fault. The models are extraordinary. The problem is the context we hand them. Ungrounded, disconnected, half relevant. One confident hallucination in front of a customer, and the pilot is shut down. The fixed isn't a bigger model.

**[1:48](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=108s)** It's a better retrieval. This drawing is basically the whole talk. Garbage in, garbage out. If you fed a rag system unconnected [clears throat] disorganized data, you get a garbage answer. Hallucinations, wrong facts, missing context. The machine isn't broken. The data you are feeding it is a mess. So, you can't fix this with a bigger model. You fix it by giving the data structure. Remember that 95%? Here's a system that doesn't fail. On a public graph rag benchmark, our graph rag SDK is number one.

**[2:39](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=159s)** Almost 82 overall accuracy. Compare it to the vector rag with only 55 overall accuracy. That's 26 points gap just from adding a graph. 26 points is the difference between a demo and something you actually ship. Here's a question, a real one. Which of my customers are in a city where I have an office? To you, that's easy. To a normal rag system, it's a trap and it will fail it because there is no single chunk of text anywhere that say this. Your customer location live lives in one document.

**[3:28](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=208s)** Your office locations lives in another. Vector cells are nothing to match and that's exactly the a gap a graph closes. We will come to this question later. Almost everyone here has shipped a rag pipeline and almost every one of them at some point confidentially made something up. So, we know the loop. Chunk your documents, embed them, and store them in a vector database. And at query time, pull back the top K chunks that looks like your question. But, look at what you get. A pile of chunk. A flat list. Nothing connects fact A in chunk three

**[4:18](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=258s)** to fact B in chunk 47. So, where this system broke breaks? I want to talk about four points. The first The first one is about multi-hop reasoning. If your question require multi-hop multi-hop knowledge, for example, people to people to event to a job, we need to extract the knowledge that leaves behind similarity. And the flat list can do that. If you're talking about concepts, like if you search about girl or any one of you or like this event, there is no grounding in vector search. So, your

**[5:08](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=308s)** concept is across the documents, and you need to find all the concept and to understand if it's relevant to your question or not. When you add documents, you only add more and more vectors. So, you add noise, and you need to find the relevant concept that with with database that doesn't scale. And when you eventually get to the ask the question, you only extract K chunks. And you don't know if your uh relevant information it it is in the K plus one chunk. I'm sure most of you already know this. But just in case,

**[5:57](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=357s)** a knowledge graph is the simplest structure there is. Nodes are the entities, the things your data is about. People, places, products. Edges are the relationship between them, typed and directional. And the key idea, the fact, lives on the edge. Alice founded founded Falco DB isn't a sentence to be read every time. It's one edge. Alice founded Falco DB. Falco DB based in London. Falco DB builds graph right SDK. Same picture you sketch on a whiteboard,

**[6:47](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=407s)** except now it's queryable. And the SDK does this automatically. Yeah. Back to the question from earlier. To a human, easy. To vector search, a trap. Because the the two facts live in different chunks. Top K graphs, whatever looks like your the question. And the two facts that are relevant never ends up in the same context window. So, the model guesses. But a graph already has the joint built in. Customer to city, back to office. That's a path you can walk. Two hops,

**[7:34](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=454s)** one query. The answer isn't retrieved, it's traversed, and it's grounded. Because every step is a real edge. That's it. You don't throw anything away. Look at these two sides. On the left, your documents and their chunks. Only now they are connected. Chunks to chunks and to the source documents. On the right, you have the entities and relationship from the original chunks. The information is just with representation as a graph. Put them together and you can use this graph to walk from document to

**[8:21](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=501s)** chunk to entity to entity to entity and then to chunk. And you can connect two documents with same relationships that lives in them. So, how So, how do we build it? The first two steps are identical to vanilla rag. Take your documents, split them into chunks. Only now you need to extract entities. This is where the graph came come from. Extraction. We use an LLM to extract entities and and and relationships. Then, we need to resolve them uh in order to deduplicate the graph and

**[9:09](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=549s)** reduce the noise. At the end, we get a a full knowledge graph linked and embedded. And that's it. Same embedding as vector, same same chunks. Only now with connections and that we can traverse. How does text become a graph? It's an entity extraction We found out that using two models for extraction is more accurate and fast and faster. The first the first step is a is done doing done by local name entity entity recognition model, Gleaner. This model is optimized to extract entity based on a given ontology.

**[9:59](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=599s)** It's local, it's fast, run by milliseconds, and zero API cost. Free. At the output, we get entities. Alice, Faculty B, London. And then we are using LLM to verify those entities and extract relationship between them. The output is a complete knowledge graph. Now Alice connected to Faculty B with real edge. Faculty B connected to London with also a real edge. Now we have we have extracted entities. And sometimes we got duplications. For example, from documents we can get a

**[10:47](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=647s)** several men mentioning names like Nova, Novacorp, and Nova Inc. We want to deduplicate this this entities in order to get a single representation on our graph and to know that every time we when we search for concept, we return to a single representation. This is how it scales. And we're doing that but by taking these entities and created communities. A similar a similar semantic groups. For example, Nova and Novacorp in one group and Apple in another. Then we extract the entities that look similar on the graph and create batches.

**[11:35](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=695s)** Each batches we give to the LLM to decide if to merge these entities or not. At the end we get the the single representation and unified knowledge graph. This is how when you add documents and add same entities, they return and merge to the entities in the graph and we can add and add documents and the concept is single of the graph in the graph. By now, we know a little bit a bit how to build a graph and what is what is it look like. Let's talk about how we retrieve it. For example, when we query a question, we now can

**[12:24](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=744s)** take this question and find entry point in the graph. For example, Alice and London. And now we can use the graph that we built to do a multi-hop reasoning. We are the one hop to to walk out, then to base in, and expand it to other information that we want. Think what you can do with it when the agent can control the hops. Let's get more specific. When we query a question, we extract keywords and embed them. And now finding the entry point and the route between them. This is the power of graph. Only now we have the edges and the fact between

**[13:13](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=793s)** them. For example, Alice co-founded Faculty B in 2023 is a fact that live in your original chunks and now it's on the database connecting the two concepts, Alice and Faculty B. We extract this structure and re-rank it. And then give it give this complete context to the LLM. Every answer cited its source. The answer Alice works at Faculty B didn't come from nowhere. It resolved to the entity Alice, which as mentioned in this exact chunk, which is part of this document, company profile.md, for example.

**[14:02](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=842s)** So, when someone asks, "Why did the the system say that?" you show the trail. That's it. The score, the the source sentence, the file, that's the difference between black box and knowing exactly where your answer came from. Everything I'm showing you package and it's open source. Point uh the Graph Rag SDK is one simple API, point it at your documents, and you extract uh and you build the the knowledge graph, and then you can ask. It's built on Faculty B, including vector and full text index uh in one engine. Automatic extraction and reservation reso- resolution, every answer is

**[14:51](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=891s)** grounded and cited. Okay. Let [snorts] me show you a quick demo. Uh we uh built a demo of an application with this Graph Rag SDK, uh ingesting a document, and then ask the question from earlier. Um this is the first step. We ingest the documents, the all the steps of of uh creating the graph. Then we have extracted entities and relationship. The graph looks like this. We can see how the databases look like. We have a visual and then we can ask our question, go to the database, search, traverse, and we rank, and now we can build the question and

**[15:39](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=939s)** connect it to the source chunks. Nothing's free. So, that be Let Let me be straight with you. Creating a graph is cost you an LLM tokens and a processing time. The extraction, the resolution, the incremental updates, the deduplication has its own processing time and it take tokens. But, at the end, you get a database that you can reuse. An accuracy and trust that vectors alone can give you. This is one graph that goes with you. It's multi-tenant, one graph per tenant,

**[16:29](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=989s)** how this relation. It's incremental, you update and delete. You don't rebuild it from scratch. It's efficient because you traverse and the relevant sub-graph, not the whole thing. And it's fast, sub-milliseconds queries on Faculty B. Add gra- Add data, add tenant, add traffic, the the graph keeps up. Okay. So, everything I've shown you until now runs on one engine, Faculty B, the graph database. It's including the vector search, the full text, like I told you, and all runs on Graph Blast and in milliseconds. Let me show you three more use cases that we at Faculty B built with AI to solve problems.

**[17:19](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=1039s)** Um The fifth use case is your own code base. Point code graph at any repo and it turns your code base into a knowledge graph. Modules, classes, functions connected by calls, inheritance, depends on. You can trace code, run impact analysis, and literally chat with your code base. And it ships an MCP server, so Cloud Code and Cursur can query it directly. Think of it. Your code base as an architecture of uh graph. Calls, functions, models. Query Weaver is is open source text to SQL. You ask your existing MySQL or Postgres

**[18:09](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=1089s)** database a question in plain English. The trick is graph semantic layer. We basically take your relational schema uh relational database schema and represent it as a semantic layer on the graph. What we can achieve with that that when you ask question, we can retrieve sub graph of your schema, give it to the LLM in order to create SQL query. For example, if you have table one and table two, and your question talking about this table, but in order to create complete SQL, you need a connection table that semantic not connecting uh or similar to your question. Only if if you have the route between this table, you can understand it.

**[18:55](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=1135s)** And you can use it without all schema. Maybe your schema is large and you can get it into the context window. And finally, memory to your agent. Agent forget anything between sessions. Give them graph memory and their memory becomes relationship instead of a flat text. Alice follows diet vegan. Alice lives in London. Now the agent can reason across facts, not just retrieve them. And it's sub-milliseconds. It plugs into Graphity, Cogney, Mem Zero, and LangChain. Okay, wrap it up. The system that I've shown you today leverages the powerful graph

**[19:44](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=1184s)** capabilities to solve problems with AI. All run on Faculty B, a graph engine, and the use cases are connected here in this uh slide. It's open source. Go try it. You can use it with Docker and run it and we you don't need to pay anything. Just use it without limitation. Thank you. This is the QR code for the Graph AI SDK. I will be around for your questions. >> [applause] >> Okay, just quick announcement for people

**[20:38](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=1238s)** who may have questions. In order for you to ask the questions, you have to submit them through the app. You will see a section where you can submit questions. But I have two questions for you. >> Yeah. >> So one is from Johan. He says, "I see vector databases are all are all over. What does Falcon do better?" >> I can answer it, but I want to do a selfie before. >> [laughter] >> With you. >> Yeah. >> Okay. Um What Faulko do better? So, vector vector database are simple. Uh it's cheap. You just put your documents, create vectors from each chunk, and

**[21:27](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=1287s)** simple to to run it. What Faulko DB brings and graph database brings is the connection between these chunks. Now, with graph, you can connect with entities, um and you you also connect the the chunks. The the simplest way is you connect the chunks. And now you can walk on the chunks. Um So, basically, Faulko DB brings the vector DB into graph. So, you have the vector uh index in them. And you can use the the edges For example, for example, about the Query Weaver, uh you can like store your schema as a vector DB. But let's say you want a table that has connection to a uh with with a business

**[22:17](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=1337s)** logic to other table or other information. Now, when you extract knowledge, it it came with the connection, and you can extract the knowledge to complete the information that LLM need uh needs to create the sequel. I hope that >> I hope that answered the question, too. So, the second question is from Thomas, and then he says, "How can graph handle restrict restricted information if not every user is allowed to access every document?" >> Can you repeat that? >> How can graph handle restricted information if not every user is allowed to access every document? >> Okay. Thomas. Um good question.

**[23:05](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=1385s)** Uh, yeah, Thomas. No, yeah, Thomas. Uh, you can uh, you can create user management and create different graphs to be different user and split like restrict usage between them. Uh, we at Faculty B have this ability. Uh, I will state with you, I didn't build it. Uh, but we have the ability to create restriction between graphs. Uh, single connection to Faculty B with single single database, you have multi-tenancy. So, you can create graphs and graphs and graphs and you can choose which graph is allowed to which users. Also, I saw uh, use cases when you namespacing and know a knowledge into the in the knowledge graph and when you retrieve

**[23:53](https://www.youtube.com/watch?v=W5k-Rbou4t4&t=1433s)** them, you filter it based on the on the user. But, we at Faculty B believe full isolation is the is the way to solve it.
