---
id: 999
title: "The LLM Evolution: From Sequence Imitation to Verifiable Reasoning"
slug: the-llm-evolution-from-sequence-imitation-to-verifiable
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Engineering"
type: "Keynote/Talk"
stage: "Stage 6 - powered by Microsoft"
tags: ["AI Models", "Large Language Models (LLMs)", "AGI (Artificial General Intelligence)", "AI Coding Assistants", "Agentic AI"]
speakers: ["Kamen Petroff"]
speaker_companies: ["ATOS"]
day: 2
starts_at: 2026-07-10T13:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=6Sb2eAm3oiE
video_id: 6Sb2eAm3oiE
session_page: https://app.wearedevelopers.com/events/16/session/999
transcript: true
---

# The LLM Evolution: From Sequence Imitation to Verifiable Reasoning

**Kamen Petroff (Software Developer — ATOS)**

`Track: AI Engineering` · `Type: Keynote/Talk` · `Stage: Stage 6 - powered by Microsoft`

`#AI Models` `#Large Language Models (LLMs)` `#AGI (Artificial General Intelligence)` `#AI Coding Assistants` `#Agentic AI`

[Watch the recording](https://www.youtube.com/watch?v=6Sb2eAm3oiE) · [Session page](https://app.wearedevelopers.com/events/16/session/999)

## Abstract

For the last decade, the recipe for AI was simple: more data, bigger models. By feeding neural networks the entire internet, we taught them to imitate human language with startling accuracy. But as we exhaust the world's high-quality text data, a new question arises: How do we scale intelligence when there is nothing left to imitate?

In this talk, we trace the evolution of Language Modeling — from counting words with n-grams, through Word2Vec and the Transformer, to the reasoning paradigm sparked by OpenAI o1 and DeepSeek R1. This "Data Wall" is real — but it ends imitation, not progress: the industry is pivoting from System 1 (fast imitation) to System 2 (deliberate reasoning), opening test-time compute as a second scaling axis where models "think" before they answer.

Following the AlphaGo Zero precedent, we'll see how reinforcement learning with verifiable rewards lets models keep improving without new human data, and how coding agents like Claude Code, Codex, and Cursor point that same propose–verify loop at your codebase. Along the way, Verifier's Law and the  "jagged edge" of intelligence will tell us which tasks AI will master next — and which it won't.

This session is for any developer who wants to understand where this is heading — and how our role evolves from writing syntax to architecting the specs, tests, and feedback loops that guide AI reasoning.

## Speakers

### Kamen Petroff

*Software Developer — ATOS*

Software Developer at cycos AG (an Atos company) since 2001, specializing in real-time media streaming, web conferencing, and IVR solutions. Shifted focus to Applied AI in 2017, working on research projects in the fields of Natural Language Processing and Deep Learning. Creator of `kpe/bert-for-tf2`, one of the pioneering implementations of the Transformer architecture for TensorFlow 2, dedicated to bridging the gap between cutting-edge AI research and practical software engineering.

## Transcript

*3,241 words · source: yt (en)*

**[0:14](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=14s)** All right, welcome back for the penultimate time. Um, but still great content coming up this Friday afternoon. Next up is Carmen Petro. Uh, he'll talk to us about the evolution of language modeling. Some great stuff coming up. Um and so that's without any further ado, let's welcome to the stage Carmen Petro. Welcome Carmen. >> Okay, thank you Christian. Hello together. Hello everyone. Thank you for being here today. For the last decade decade, the recipe for building AI was uh very simple. Get more data, big bigger models. And after feeding those models the entire internet um and teaching them to imitate human language, they developed some incredible capabilities.

**[1:03](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=63s)** But today we have mostly depleted our reserves of high quality text. And this brings up the question, how can we keep how can we keep scaling intelligence when there is nothing left to imitate? So hello, my name is um Kam Petro and um I'm a software developer at Cyos which is part of um ATOSS and traditionally I worked on realtime media streaming and IVR IV those um chat bots which nobody likes talking to in the call center. So this led me 2017 to natural language understanding and this time timing was quite um good because just year or two

**[1:54](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=114s)** later the first um transformer models came out and started the AI revolution we see today. So here is our plan for today. We'll start with um and with the statistic statistic language modeling with word embeddings, neural networks, attention transformers and move up to uh reinforcement learning from human feedback and chat GPT and at that point we will hit the data scarcity wall and we'll discover test time compute and verifiable reasoning as a way forward. So we will also talk about the jack of intelligence and the verifiers wall and

**[2:42](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=162s)** how this affect us as our data day-to-day job as software developers. So let's start with some basics first. What is a language model? Language model is just predicting the ne next token in a sequence. You can think of it uh just simply as um input completion or if you're into math you can think of it as a conditional probability predicting the next stock given the previous tokens and um if for us as software developers we can think even as a software as a function signature where you pass in the previous tokens and get as a result a probability distribution of the next token from your dictionary to how likely is it in the given context? And um keep in mind this is just an

**[3:33](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=213s)** interface but a very generic one and it does not constrain um how your implementation could look like. So let's take a look at what it takes to be good at this um at this uh completion game. So water boil set. You may need some fctional knowledge and um the sum of integers from one to 100 some basic math some transitive logic and this this all of this is not limited to a single word. Of course you can let the model generate word by word to get uh much larger answers. And as a general um pattern you can basically encode because of the expressivity of the human language you

**[4:22](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=262s)** can encode basically every cognitive task as a question and expect some well-written answer. So uh so for how do we implement such uh language models for very long time the predominant architecture or the predominant um concept was um engrams which is basically counting cocc occurrences of words and this is quite simple and interpretable and in fact they powered um Google translate up to 2016 before they get replaced by recurrent neural networks. But before we look at recurrent neural networks, we should take a look at one probably the most iconic idea in modern

**[5:09](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=309s)** AI, which is the beta lesson by Rich Saturn. And he put it roughly like this. General methods that leverage computations are ultimately the most effective. And Rich Saturn talked about two such general methods. one is learning like uh learning to imitate human text and the other one is search which we see in the second half of the talk in reinforcement learning and our agentic loop. So with that just to give you an example why human cleverness human engineered cleverness alone is not enough. Imagine you need to implement uh image classifier without data just with a rule-based approach. And while we talk about datadriven

**[5:57](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=357s)** algorithms, just a two sentence recap on neural networks. Think about neural networks as a ma mathematical function with which is parameterized and can transform some bunch of numbers input vector into some output vector and you can tweak the [clears throat] weights so that you get the answer you need. Once you learn those weights you can reuse them over and over again to transform the input to the output you care about. So how can we use uh this neural networks for language? In 2003, uh Benju uh Benju and team Joshua Benju and uh team um they were the first to represent words as dense vectors, bunch of numbers and

**[6:48](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=408s)** use them together with a neural network to jointly train them on text and on a on the language task. However, it took 10 years uh before this concept was scaled uh employed at scale at um Google by this work to vec method and uh this is the first time we showed that those word embedded can decode semantic meaning into the geometry of the embedding space. Now word to vec is just for single words represent single words as um vectors and to move further to be able to represent

**[7:36](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=456s)** full sequences like uh sentences. We move to recurrent neural networks. Those recurrent neural networks they leave uh read the text left to right and they have something like a running summary which is this um hidden state and that's a bottleneck because you because it's a fixed size and you cannot represent long range long range uh histories. This was solved by the attention mechanism which as you see here is a way to let the model dynamically learn which inputs are important and which are not. So the model attendents it looks at the full sequence. It attends only to the

**[8:24](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=504s)** input positions which are important for the current output position. And uh this attention was fully employed in 2000 2017 in the attention all you is all you need paper which introduced the transformer architecture. And the main point here it was uh extremely uh very well scalable. You can process the inputs in parallel which unlocked usage of um GPUs and TPUs and basically unlocked everything that follow. This is the scalability that unlocks uh most of the things we see today. So um this idea the transform architecture was uh then um one year later used for language modeling in the GPT and bird

**[9:14](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=554s)** models and the main concept it's a paradigm shift from for pre-training the model on large amounts of text and then use this pre-trained model to fine-tune on specific tasks. So to give you example on some specific tasks um you have classification may maybe summarization similarity between sentences you see the green part the transformer that's um learned during pre-training and then you fine-tune the final head for each specific task and this was the state of the at state-of-the-art at the time but um then OpenAI realized If you scale the model, you no longer need to do task

**[10:04](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=604s)** specific fine-tuning. So with GP2, a larger model, they figured out if you if you just prompt the model in a appropriate way like uh it can it can um do some task like translation or summarization without having been specifically fine-tuned on that. And with the next model which was um 100 times bigger GPT3 they showed also this uh in context learning capability which is you put in your context example of the task and the model picks up and starts being able to solve it without pri prior fine-tuning. So this is quite important for what we see today.

**[10:55](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=655s)** And then uh also OpenAI experimented in 2021 with uh fine-tuning GPT3 on data from uh GitHub and they notice of course if you give it the we know that if you give it uh documentation of a function it starts being able to generate the implementation or if you give it the implementation it get generate the documentation and more importantly they noticed is that it's not only good on generate generating code but this code fine-tuning also improved the general reasoning capabilities of the model. So that's something we see later. However, text completion and input

**[11:46](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=706s)** completion was not enough to move a step further. For example, if you ask GP3 a question, it might as well output or generate additional questions. That's usually not what you need, what you want. And to move further, um, researchers at Google took a lot of different NLP task, nature language processing understanding task and reformatted them as instruction answer pairs. So they give the instruction a different task, they answer and they fine-tune the model on this um data set and they noticed that the model generalizes and start being able following instructions on tasks it never

**[12:34](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=754s)** saw before. And the second idea was reinforcement learning from human feedback where you first train a reward model which can great uh the outputs of the model and then use this signal to fine-tune the model further to reinforce to rewards the best answers. This is AOHF reinforcement learning from human feedback and using this recipe uh OpenAI released CH GPT in November 22. So, so it was quite successful in um modeling human preferences and you can see this is the actually the

**[13:24](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=804s)** recipe pre-training supervised instruction fine-tuning followed by arrowf and it's you notice that um pre-training is basically uses all of the compute and it's important that this is the phase pre-training is where those capabilities of the model get developed. They they get forged. While the other stages supervised by tuning, rewards modeling, they don't build new capabilities. They just elicit what's already there from the pre-training phase. Uh in this sense, pre-training sets the ceiling and pre-training is limited by the data. So how much data do we need?

**[14:13](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=853s)** This has been answered by the scaling walls. So they are surprisingly precise in predicting the model capability based on um the amount of compute the amount the data size you have and the parame parameter count of the model. But there is some optimality point where for a given compute budget you can calculate for this parameter size how much uh data you need. And this is done by this uh Chinua paper and it says for each parameter in the model we need 20 tokens and using best estimates of today we could say that we are we have almost depleted the usable text data we have or nearly so. So here's the question again.

**[15:03](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=903s)** How do we keep scaling intelligence when there is nothing left to imitate? And the answer is to stop imitating and start verifying. So this idea first start showing uh so maybe we can look at this um paradigm in three different ways. System one to system two thinking. Um Daniel Canniman thinking fast and slow [snorts] like transition from learning to search or transition from um training on verifiable rewards instead of human preferences human preference alone. So this um what enabled this was this chain of thought idea. So what the researchers

**[15:53](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=953s)** just observed that by simply asking the model to let's think step by step including this in your prompt the model started generated longer answers and this longer answer is like compute budget the model can use to find the final answer. So so that's why it improved the final answer. This idea was employed um by OpenAI in their 01 model which was a huge step on some reasoning task like competitive coding, competitive math or PhD level questions. Um

**[16:43](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1003s)** so 01 basically established test time compute as a new scaling access where you can buy capability with test time inference compute budget otherwise they didn't um disclosed much but just a few months later just a few months later different model show up To understand it, we should first look at how reinforcement learning solved u the game of go. In 2016, Alpha Go model built by um Deep Mind was able to beat the best professional player in Go, Lisa Do. And at the time this was quite unexpected and surprising because even

**[17:32](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1052s)** the best um uh go programs at the time were far weaker than human players. So how they did it? They first um used the human data like 30 million um professional game records um bootstrap it bootstrapped the model from that and then optimized further with reinforcement learning uh with selfplay and one year later they threw out the human data and uh this new model which was trained from scratch from scratch just using the game uh the rules of the without human data or this new model was able to beat the previous one 100 to

**[18:21](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1101s)** zero. And um this demonstrates the new paradigm which is a cheap objective verifier can beat human data. and uh language models they had their alpha go model uh about five months after 01 with this deepseick air10 model which was trained without supervised fine-tuning um data without rewards human preference rewards but entirely using reinforcement learning with verification with verification on

**[19:11](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1151s)** tasks like math and code. So you give the model some um math and code problem and let it generate and you just verify the final answer. Researchers noted that the length of the responses they increased over training because the model figured out longer thinking tokens uh uh bring better outcome and and so so this was this is kind of the new recipe. You sample different outputs from the model, use a verifier and reward the best outputs. For this you need um verifier, right?

**[20:03](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1203s)** And this result by10 it was uh quickly reproduced by the community. Um the details does not matter much m much much maybe uh example more recent example was this um VIP tinker 3B which was just from last month and it's a very small model but shows capability similar to GLM5 and Gemini drive 3 pro it was also trained uh from um on code and math and science and science basically all verifiable domains And while it's not so good at broader knowledge a task that require broader knowledge

**[20:50](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1250s)** um we can we can uh argue that the reasoning can be compressed into a core without the need for much parameters. So the conclusion is we are not data limited on reasoning [snorts] and this brings us to the verifiers war which is formulated by Jason way who is the first author of the chain of thought paper. He put it roughly like this. The easier task is to verify the easier is to train AI to do it. And a task is easy to verify if you have uh objective truth of of what counts as a good solution. If those candidate solution they can be

**[21:40](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1300s)** checked quickly and in parallel so you can scale and this this verification uh results into a low noise continuous signal. So this also um translates to software development where we see that AI is good on verifiable specs but is much less good on things like grading an essay or open-ended design. And this is also known as the jacked age of intelligence where you see superhuman performance on some tasks and uh very

**[22:31](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1351s)** well performance on others. Now to see how we use this um today we should we should first look into uh the react architecture. So the recipe here is you take a model and you need to connect it with the outside world. So you give it tools like search, maybe some sort of executing different tasks, uh, API access, whatever. And this loop of reasoning, act, observe basically turns your chat model into an agent. And that this is what we also see in the

**[23:19](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1399s)** today's coding agents like open code, cloud code, anti-gravity, CLI, codex, all of them they are what they do they can plan, read files, code and repeat until they find the solution. So what this means for us is that our um our job levels up. We don't need to write the code ourself. So we our leverage lives on writing the specs and acceptance criteria and let the agent optimize on those generate the

**[24:08](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1448s)** code itself. So what I'm almost uh done. So quick summary what we saw until now in the first phase imitation we had u statistical language modeling neural networks word embeddings RNN um and instruction fine-tuning. Then we hit the data wall, the data scarcity wall. And to move further, we discovered verification as a new scaling axis. So this bring to bring it all together. This data w is real but only for the kind of imitation algorithms we used for LLM

**[24:57](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1497s)** pre-training. verification is a new scaling access and it needs no human data, no human text. The upshot for this room is um making the make this test pass is something that gets automated quickly and first. But deciding what to build and defining what correct even means. This is a task no verifier can solve. So taste has no key has no answer key. And one honest uh caveat, the frontier keeps moving fast. better verifiers keep turning what was uh unverifiable

**[25:45](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1545s)** yesterday into something that might be verifiable tomorrow. So this all this is about the order of automation. It's not a permanent mode. So that's all. Thank you for your attention. >> Thank you K. >> Very good talk. Thank you very much. If you have questions for common um he'll be on the side stage. ready to answer all of them. I actually I have one. So, so you mentioned that the role will change, developers role will change. So, what what's your assessment? Will every developer role change to that? Will roles become obsolete or will be new extra additional roles? I think um coding itself I mean software development is uh so huge and coding maybe takes a lot of this time

**[26:34](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1594s)** traditionally but actually it's only small part of what else should be done and I really believe our leverage is not so much into coding the syntax but much more into designing this verification loop which enables AI without the AI we don't have this amplification so we need to concentrate on um building exactly those stuff the specification and the verification to close the loop and only when this loop works only then we have an effective leverage. >> Okay, thank you. Thank you very much. Still make sure there's one more talk to go. We have one more highlight session today. So make sure that you return at 20 past the hour and until then give it up once again for Kam Petra for this great talk. Thank you very much.

**[27:22](https://www.youtube.com/watch?v=6Sb2eAm3oiE&t=1642s)** [applause] Thank you.
