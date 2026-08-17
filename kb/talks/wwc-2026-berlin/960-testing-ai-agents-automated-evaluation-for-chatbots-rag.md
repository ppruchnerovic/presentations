---
id: 960
title: "Testing AI Agents: Automated Evaluation for Chatbots & RAG Systems"
slug: testing-ai-agents-automated-evaluation-for-chatbots-rag
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Agents"
type: "Keynote/Talk"
stage: "Stage 6 - powered by Microsoft"
tags: ["AI Models", "AI Standards", "Agentic AI", "Fine-Tuning", "PyTest", "Python", "Retrieval-Augmented Generation (RAG)", "Unit Testing"]
speakers: ["Sebastian Messingfeld"]
speaker_companies: ["Eurowings Digital"]
day: 2
starts_at: 2026-07-10T12:20:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=hbShI0crCOg
video_id: hbShI0crCOg
session_page: https://app.wearedevelopers.com/events/16/session/960
transcript: true
---

# Testing AI Agents: Automated Evaluation for Chatbots & RAG Systems

**Sebastian Messingfeld (Staff Engineer — Eurowings Digital)**

`Track: AI Agents` · `Type: Keynote/Talk` · `Stage: Stage 6 - powered by Microsoft`

`#AI Models` `#AI Standards` `#Agentic AI` `#Fine-Tuning` `#PyTest` `#Python` `#Retrieval-Augmented Generation (RAG)` `#Unit Testing`

[Watch the recording](https://www.youtube.com/watch?v=hbShI0crCOg) · [Session page](https://app.wearedevelopers.com/events/16/session/960)

## Abstract

AI Agents, chatbots, and RAG systems are easy to prototype — but difficult to test reliably. Small changes to prompts, models, retrieval sources, or system instructions can silently change behavior, and classic assertions (string matching, snapshots) often fail to capture what actually matters: correctness, relevance, grounded answers, and consistent multi-turn dialogue.

In this talk, we’ll start with the common testing problems in real projects: “it worked yesterday”, hidden regressions, evaluation noise, and the challenge of aligning developers and stakeholders on what “good” means.

Then we’ll explore practical testing possibilities with evaluation frameworks like DeepEval: how to validate responses beyond keyword matching, how to structure test cases for both chatbots and retrieval-based assistants, how to define pragmatic quality gates, and how to run these checks continuously in suggests, then?

As a side topic, we’ll show how BDD/Gherkin can wrap these evaluations into human-readable scenarios (Given–When–Then), making expectations reviewable by non-developers while keeping the actual validation powered by automated evaluation metrics.

You’ll leave with a reusable blueprint for introducing automated AI evaluation into your development workflow — from local runs to CI pipelines with actionable reports.

## Speakers

### Sebastian Messingfeld

*Staff Engineer — Eurowings Digital*

Sebastian is a Staff Engineer at Eurowings Digital GmbH, building end-to-end solutions across the Eurowings website and mobile app. His current focus is the information experience on eurowings.com — including AI-powered chatbots, on-site search, and smarter contact flows — where he helps teams turn AI features into reliable, production-ready capabilities.

## Transcript

*1,610 words · source: yt (de)*

**[0:12](https://www.youtube.com/watch?v=hbShI0crCOg&t=12s)** Alr, welcome back on best stage today. So, next up Sebastian Messingfeld will talk about testing AI agents staff engineer for Eurowings Digital. Now I talk to him before there won't be a flight voucher for the best asked him today unfortunately but question please use the app might pick at the end still time without any furastian stage welcome ja hello welcome. Messingfeld work stuff engineer for the department optim flight operations flight may flight conference who maybe had a flight delay flight cancellation

**[1:03](https://www.youtube.com/watch?v=hbShI0crCOg&t=63s)** please put the question in the app and then we can talk about it. Ja, what will I talk today about? informers diverse customer rusters times customer fly once year somebody laptop help content page chat introduc also capture knowledge to customers

**[1:58](https://www.youtube.com/watch?v=hbShI0crCOg&t=118s)** of course initiated our customer support center and tech was a few challenges how testing chatbot first like always practical sessions all the slides all of the codes example code already grab gitaro so you can really relax sit down enjoy the talk think about the question you want to ask me so now pressure for you website chatbot integrate chatbard in search

**[2:48](https://www.youtube.com/watch?v=hbShI0crCOg&t=168s)** website combination touch points also extend our feature set not only asking question also rebook over ag and then you can think about what can what can go wrong in real chatot please not fingerinting happen to all of us bring awareness attack vectors over chats first example manipulation use case customer of car dealer could car

**[3:40](https://www.youtube.com/watch?v=hbShI0crCOg&t=220s)** GM luck sell also destructive chat systems overall for example AI calling tool delet database 4000 users and then covers try to cover even his action maybe would say it's chatbot later airlineability information getting chat trust for example Canada fair informationeray high priceed chatbard found a lot of isses

**[4:43](https://www.youtube.com/watch?v=hbShI0crCOg&t=283s)** Corona still website nobody no customer found interaction chatbot come up again problem that we have to come up how our chatbots chatbotsic systems coming now to general starting point of talk to what vectors do what points you have to look at it if you want to introduce chatbard afterwards how to test so as said chatbard changes behavior instead of only saying giving answer dedicated question actbooker

**[5:34](https://www.youtube.com/watch?v=hbShI0crCOg&t=334s)** my flight canceled me next customer also my boss expected Sebastian please impl new category of chatbot started here wiring our internal systems life systems knowledgeas may dedicated capability brings doma airline may have flight search booking maybe cancellation maybe book hotel over the website

**[6:24](https://www.youtube.com/watch?v=hbShI0crCOg&t=384s)** funels hotel flight one steps valid here point new moving syem usbehavi chat

**[7:14](https://www.youtube.com/watch?v=hbShI0crCOg&t=434s)** only proms combination of prompts at different parts of the system of course also guard value tools and so on but little bit out of the focus talk here I want to say every layer is a new place where you have to test it where this chat could fail and then it comes to the question how it fails and here directly see the failing point is prompt injection I think everyone knows what the prompt injection let me repeat instruction into following adduction

**[8:10](https://www.youtube.com/watch?v=hbShI0crCOg&t=490s)** lming life cycle of injection airline PDF PDF may content inside on us also think about bypassing also of internal security limiting

**[9:23](https://www.youtube.com/watch?v=hbShI0crCOg&t=563s)** % session ja always getting 10% losing money in the end hard to test and if you think about retriggering the persistent we really have to think about our tests like real user of may come agent test pyramid soft test software testing pyramid only other categories of course cheap tests expensive test cheap

**[10:19](https://www.youtube.com/watch?v=hbShI0crCOg&t=619s)** schema testing tool test on calling chatbot and checking the response it goes a little bit for the reference based test if you for example our chatbotings if it fix fix sent easy test case working easy assert in unit test also comes what is openended questions to ask

**[11:14](https://www.youtube.com/watch?v=hbShI0crCOg&t=674s)** business day correctly direction may synonym program introduce additional lmcks respmcks against parameters of on top of it always our human security team finally judging about our test cases daily working on chatbot may finishbody looks

**[12:03](https://www.youtube.com/watch?v=hbShI0crCOg&t=723s)** here only human vectors using example succeed sa never fall in the same direction but for this talk I want to concentrate on LM as a judge what is LML Judge LM judge AI AI against categories automatic quality reviewer you can think about

**[12:51](https://www.youtube.com/watch?v=hbShI0crCOg&t=771s)** requester reviewer checks what did you do well would you do it in a different way here also check which AI which model do use same as for example for pull request do you use the colle you best body with who always says yeah it's fine or do you really use somebody who also looks critical on on your output and here what the lm as a judge also brings not only the correct answer it also can look at other topics like tone like correctness formul scaling

**[13:46](https://www.youtube.com/watch?v=hbShI0crCOg&t=826s)** show slides code example scale question answer session with real chat in a way that not possible with other humans in the loop chat judge also having repetitive consistent test can checking system working judge only yes test case was correct false also can give you a score exp

**[14:49](https://www.youtube.com/watch?v=hbShI0crCOg&t=889s)** incorrect Berlin capital may obvly in airline expcorrects example knowledge base because updating knowledge base update test next point how do we use impract so we are using

**[15:38](https://www.youtube.com/watch?v=hbShI0crCOg&t=938s)** you maybe think about judge lml judge simple idea only need to put prompt against result and say okay is it correct or is it not correct not true deep evil python framework lm judge open source python framework test good one you have in test cases only in test so it may be once in the same level as currently end test unit test new environment magic deepil

**[16:39](https://www.youtube.com/watch?v=hbShI0crCOg&t=999s)** research back prompt scores answer in matrics brings also a lot of boiler plate code around like datet loading thres number exfulas coming

**[17:37](https://www.youtube.com/watch?v=hbShI0crCOg&t=1057s)** bi toxic buil functionality pick only means bringing deep evil prompt to you around may come In the beginning sentence how long refund for my flight take a real customer question and it should be coming from your product owner from your users that use chatbot wet team which tries to hack the AI

**[18:27](https://www.youtube.com/watch?v=hbShI0crCOg&t=1107s)** board and then you are really connecting your chatboard to your test cases. Here of course for this example I put fixed sentence but here you would connect to your chat GPT overwest RP overstream RP over websocket and really getting the answer back that is coming question then we already have a predefined set of context that chatbot also had and that you want to test context answer depending on use case you really see only

**[19:17](https://www.youtube.com/watch?v=hbShI0crCOg&t=1157s)** example context in the end element test case takes question takes the answer and also the context sofor last line is test against may matric what 07 matri decides what to check the decides how strict are you checking a metric is not black box a matric is really question inside the deep evil framework good defined prompt hier answer true to context could also ask is the answer

**[20:09](https://www.youtube.com/watch?v=hbShI0crCOg&t=1209s)** relevant to my question so different matrics you can take and then framework splits up also the answers into claims so it doesn't wipe the correctness it really separates the different claims that it found in the answer and twice to check it against provided context is supported by the context on invented and then it sums up if you have maybe 10 claims found and you have h in this example seven was supported by framework by the retriev context it 1.7 score

**[21:01](https://www.youtube.com/watch?v=hbShI0crCOg&t=1261s)** one zero higher the stricter and here you have really to calibrate it on own because can also come up claims totally fine maybe business day monday to frid maybe in set Next part

**[22:06](https://www.youtube.com/watch?v=hbShI0crCOg&t=1326s)** testes green only one time Boss cheaper modeling system getting may not so good results. Same goes with the knowledge base if we got reindex something changed. incorrecting memories users also memories developed maybe injection can

**[22:55](https://www.youtube.com/watch?v=hbShI0crCOg&t=1375s)** be happen so us important you can do unit test on every commit like schema is valid predefined anwers maybe cases sy content manager changed our content not aware of it so of course our tests fail so vor hier Ag break

**[23:49](https://www.youtube.com/watch?v=hbShI0crCOg&t=1429s)** so last part of presentation during the development of our AI agent we saw that not only tech guys not only tech team working on passengersit tonality pol standing aware engine tools memory plumping together in

**[24:43](https://www.youtube.com/watch?v=hbShI0crCOg&t=1483s)** reality product owner defin ites agent only developer can test here is solution what we did what would be if the tests not anym code tests also written extend testing may scenario flight

**[25:51](https://www.youtube.com/watch?v=hbShI0crCOg&t=1551s)** refund for situation will get test cases separated content editor new BDD test work on the syntax having end to end responsibility if I change something I have to do something over learn a lot of our knowledge base that we have wrong content on that missing content editor prodyton

**[26:41](https://www.youtube.com/watch?v=hbShI0crCOg&t=1601s)** code required up in my code example show link slide brings setup judge chatesten place potentius ja in chatbot what you take out aguture

**[27:30](https://www.youtube.com/watch?v=hbShI0crCOg&t=1650s)** expensively act use cases systems chat touch how can change maybe what offered simpleckwers exp schedule looking memory drift using testing user the quality that everybody can commit bd

**[28:22](https://www.youtube.com/watch?v=hbShI0crCOg&t=1702s)** test increases also in our company policy owners brings also more value and more stability to the chatpot so you also have to bring in people who define what good is not developer responsible not stuff engineer responsibility really to think as whole team what is a good chat for you also again slide Thank rec

**[29:26](https://www.youtube.com/watch?v=hbShI0crCOg&t=1766s)** LM website define our content editors knows content better stuff engineer Okay.

**[30:22](https://www.youtube.com/watch?v=hbShI0crCOg&t=1822s)** [applaus] M.
