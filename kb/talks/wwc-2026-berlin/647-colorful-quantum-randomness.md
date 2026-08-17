---
id: 647
title: "Colorful quantum randomness"
slug: colorful-quantum-randomness
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Emerging Technologies"
type: "Keynote/Talk"
stage: "Stage 2"
tags: ["AWS", "IBM", "Quantum"]
speakers: ["Jakub Gaj"]
speaker_companies: ["Danske Bank"]
day: 2
starts_at: 2026-07-10T09:40:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=kWqi4mY3YfU
video_id: kWqi4mY3YfU
session_page: https://app.wearedevelopers.com/events/16/session/647
transcript: true
---

# Colorful quantum randomness

**Jakub Gaj (Cloud Solution Architect — Danske Bank)**

`Track: Emerging Technologies` · `Type: Keynote/Talk` · `Stage: Stage 2`

`#AWS` `#IBM` `#Quantum`

[Watch the recording](https://www.youtube.com/watch?v=kWqi4mY3YfU) · [Session page](https://app.wearedevelopers.com/events/16/session/647)

## Abstract

Experience the power of quantum superposition through this visual hands-on demo to generate truly random colors using actual quantum computers.

See how quantum randomness can supercharge real-world applications in cryptography, material science simulation, and optimization problems that classical computers struggle to solve efficiently.

Showcase of quantum algorithm development using OpenQASM and Qiskit frameworks, running on IBM Quantum and Amazon Braket platforms. No prior quantum physics knowledge required, just bring your curiosity for emerging technologies!

## Speakers

### Jakub Gaj

*Cloud Solution Architect — Danske Bank*

I've been building cool stuff on the Internet since 1999. Trigram tech enthusiast (IBM, AWS).

I help enterprise companies navigate their digital transformation journeys, specializing in data center migrations, cloud migrations & modernizations, as well as cloud-native development.

When I'm offline, you can find me chasing the Endless Summer with my family, exploring surf spots around the world.

Currently based in Copenhagen, Denmark.

## Transcript

*3,787 words · source: yt (en)*

**[0:18](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=18s)** Hello everyone. Good morning to all of you. I hope everyone is having an awesome time at the conference today. So before um So the next topic for us is colorful quantum randomness. So if you have been interested in quantum superposition or randomness but are also interested into the visuals and the technology part of it I think today we'll get to know about this from Jacob who is a cloud solution architect at Danske Bank. Uh before I welcome him, just a few notes. If you have any questions, uh just feel free to post them over the app so that if you have any time towards the end, we could go over them or else we will take

**[1:05](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=65s)** them offline. So before any further ado, let me welcome Jacob to the stage. Please give a warm hand of applause. >> [applause] >> Hello everyone. Um can you hear me? Okay. Can you hear me? >> Yes. >> I need to I need to scream, I think. All right. Hello. My name is Jacob Guy. I'm a cloud solution architect at Danske Bank. I'm ex-ballerina. I live in Copenhagen right now. And today I want to talk about just scratching the surface of quantum computing and available platforms which you can actually experiment with. And I

**[1:52](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=112s)** will try to run a short demo. Uh and yeah, let's dive deeper into it. All right, so um what does randomness mean in general in in our IT world and in in uh what we use nowadays is mostly a pseudo random, right? So, it's a math formula which only looks random. So, it's very complex math for Okay. Is it better now? Okay. Uh I can't run demo over there one hand, but um we'll see. Um yes, so pseudo randomness is a base of our modern encryption, right? And it's a very complex math which only looks random. It's actually not really random. Then we have some true random number

**[2:41](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=161s)** generators which use some massive physics like lava lamps and other liquids. Uh and also we have a quantum random number generators which I'm going to talk about a bit later. Uh but basically they measure a quantum state which is in principle uh impossible to predict, right? But what what are quantum computers? Have you ever heard of quantum computers? Uh even President Trump has heard about them, so I'm pretty sure I I'm pretty sure you have. Um so we figure out that a certain uh certain our nature and the world we live in actually runs on quantum mechanics and it's super hard to simulate certain things.

**[3:27](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=207s)** Um so we had to invent some computing capabilities to basically speak the native language of nature, right? Like uh simulating molecules and so on. But we are very early in in those uh developments, so there's a quantum computing race happening, I would say. A lot of companies are competing for this, IBM, Google, Amazon, um Microsoft and so on. Um we are in like 1940s, 50s of classical computing, but uh the evolution happens much quicker, I would say. There are already available products, uh commercial products, uh which uh you can experiment with, or you can actually purchase, like IBM is is providing them. And a lot of industries are

**[4:14](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=254s)** experimenting with even messy and noisy machines, you can still experiment some with with certain certain industries. In Germany, that's automotive, which is doing a lot of material research for EV batteries. You can um you have pharma in Denmark, for example, doing the drug discovery. Finance institutions, Monte Carlo simulations, risk assessment, and so on. And IBM predicts that the quantum advantage, so um solving certain real problems with uh quantum computers or hybrid computing, um they predict it might happen by the end of this year. Quantum resilience is probably a hot

**[5:02](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=302s)** topic you have heard about uh in the news, and this relates to this math we use for generating cryptography. So, Peter Shor, uh professor of MIT, in 1994, uh he designed a encryption sorry, not encryption the algorithm actually um uh calculate the the the the prime numbers much quicker using quantum computing. And this this was only theoretical, but if we have enough qubits, uh and we're years ahead of that yet, uh then potentially that could break certain encryption algorithms like RSA, for example. So, the threat is there already, and it's called uh harvest now, decrypt later, which basically means that you

**[5:50](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=350s)** can um still can encrypt the data, and even though it is encrypted, you can still decrypt it in years ahead from now. So, it's it's really important for like historical data, financial data, um personal data, medical data, and so on. The fix is already there, and it's actually not running on quantum computers. It's actually classical computers using more advanced math. And And we generally call it uh quantum-safe cryptography or post-quantum cryptography, right? And NIST, uh this American institution for standards, has already finalized some standards, and they included them um in, for example, TLS 1.3 already includes those standards. And different companies, cloud providers, SaaS

**[6:40](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=400s)** providers, software providers already doing the upgrades on their stack uh for so-called quantum-safe cryptography years ahead of time, right? So, uh preparation like Y2K, I had a chance to actually work uh before Y2K. It also required a lot of preparation, and basically nothing major has happened. Uh so, this is what is happening right now, preparation for this um so-called Q-day, so the day where actually quantum computers can be used for um cracking some um encryption algorithms. All right, let's talk about quantum basics. I'm not sure if you have ever heard of how quantum computers work, so I will just scratch the surface, basically. So, if you can imagine a coin, and you

**[7:27](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=447s)** flip it, and you snap it, [snorts] it's either heads or tails, right? A zero or one. And this is what we have we what what we use in uh classical bits now. Our digital world is just zeros and ones. The qubit is a special kind of coin which you can actually spin and that spinning state is called superposition. So it can be zero, one, or both at the same time. So that gives us massive improvements in calculations for certain problems, not all of them, but for certain problems. Um So measurement of the superposition is basically catching the coin and the coin has to choose it's either zero or one. So in a in a perfect state you have actually 50/50 chance

**[8:16](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=496s)** to be zero or one. All right. So I will use this superposition to actually to demo something and I will try to run it with one hand. I'll we'll see. Um so I'm going to I'm going to generate colors and as you as you probably know um each each uh each color requires like 20 for random bits. Three channels which form one color. Uh so I will use eight qubits and a term called shots. So that's a circuit execution, kind of think of as a loop. So I will run it three times to get 24 bits. So a um eight bit for each color. I could also run it on 24 qubits to and

**[9:05](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=545s)** one shot to get the same or one qubit with 24 shots. I just chose to to use eight second show it on a on actual demo. And most of the accessible quantum computers right now publicly accessible computers run in hundreds of qubits, 150 I think. Uh so so it's absolutely fine to run 24 qubits at the same time. So I need to run my circuit um about three times and 3,000 times to get thousand colors, right? So, this is how my quantum circuit looks like. It's represented by this kind of graphical interface, but also by Qiskit, which is Python library for interacting with for designing the the circuits, but also

**[9:53](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=593s)** with interacting with different platforms. And it it's becoming a standard, so it's a open-source framework. But, what you can see on the left-hand side is the eight qubits and a so-called Hadamard gate, which is putting into super-superposition every single qubit, and then I measure each one of them, and that fails into classical registers. So, I will have exactly zeros and ones. So, the output of my quantum computing job will be just bunch of zeros and ones, which I have to convert into something. So, I'll use a hybrid job using Python and this Qiskit to actually represent some ANSI colors on on a console. IBM Quantum Platform is one of those platforms where you can actually have

**[10:42](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=642s)** some free tier open plan to actually experiment with quantum computing. I'll be using Qiskit SDK from my laptop, and Qiskit runtime is is running on the on the IBM Quantum Platform. Instance is this billing entity, so I can define users, I can define certain credits. Um all the bill billing parts and and the payments behind running the jobs, and they are calculated in seconds. Um And IBM provides like 10 minutes for free every month, so so you can experiment. And they expose you to different quantum computers. Um and to some simulators as well. So, you can have a local simulator, or you can have a actual physical hardware in One is Some of them are in Frankfurt,

**[11:32](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=692s)** some of them are in in Washington. Amazon Bracket is um is a service from AWS. I'm I'm very working very closely with I AWS, so uh this is close to my heart, I would say. Amazon does not provide you uh their own hardware. They actually expose different vendors at different providers, so they have a um secure connections with different uh provider labs or data centers, and they expose you certain services and simulators, and you can actually build uh some um SageMaker notebooks actually integrated with other AWS services, and you can schedule jobs to run to specific providers. Um I will try to show it on a console how it looks like on on both IBM

**[12:21](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=741s)** platform and on AWS. All right. Let's uh dive into demo. I'll try to Mhm. Is it visible? All right. So, this is this is IBM IBM Quantum Platform. As you can see, I was running some jobs uh before. Um I have access to a couple of uh quantum computing um units. So, those are the available for me quantum

**[13:08](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=788s)** computers. As you can see, they they have like 100 something qubits. And they are running on a previous the ones I have access to, they running on a previous generation of quantum computers. You can actually see some details about the computer itself, and topology of the qubits, so the the between the qubits. And some measurements results and so on. Um there's a new processor from IBM called Nighthawk, and it has a slightly different topology, so you can you can see the differences between them. I have run some workloads already, but um the real cool part of the the platform is actually composer, so you can compose and it's loading

**[13:57](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=837s)** um a bit slow. You can actually compose your own circuits in a visual way, and that would generate you some some code for it. So you can actually learn and uh produce some um produce some uh circuits for you. So you can drag and drop things like this. So if I need to build my my computer, I need to define quantum register and and and and a classic register, and I need to create eight qubits and eight classical bits. And I need to populate that on the whole register. Then I need to grab a measurement. I can just type it. And I can measure. And this is my

**[14:47](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=887s)** circuit. Um as you can see, this is the open QASM, which is more like a assembler level, and you have a Qiskit as well. I can also try to run it. I will not, but I will it will just tell me which um which hardware it actually runs, uh which are online, which are not in maintenance, and I can actually schedule a job. I will try to run it from the script itself. Um in a second. On AWS, as you can see, you can have access to different devices. So it just shows you which are online. There There different ways of uh creating cubits as well. So, every vendor is creating the slightly different topology. We can also see some retired devices. They don't provide access anymore, too. So, there's a bunch of vendors, as you can see, Rigetti,

**[15:35](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=935s)** IBMQ, IonQ, um D-Wave, and so on. Uh they also provide some simulators. So, you can run against the simulator. Um simulator is more to test your um circuit space circuit, right? So, so you can you can uh you can make sure that the circuit um will execute correctly. This is a very simple case circuit, so there's no um there's no rocket science in it, to be honest. Uh but for more complex ones, you of course want to run it first on a simulator to optimize it before you run it in a real hardware, where you actually have to pay for it. All right, so I have a couple of scripts. I'll try to run them. Um So, one of them is Sorry, I was not planning to do that

**[16:30](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=990s)** with one hand. Um so, I have I I wrote some couple of scripts which interact with this platforms. So, as you can see, I can see just a bunch of information from the what I showed in the console, and it can identify some least busy backends for me. So, I have access to three quantum computers. I can as you can see, there are some jobs queued. I can try to run it, see if that finishes within few seconds. If not, uh um I will cancel that. Um but I can run it on simulator. So, my script basically creates um run It will just ask me how many colors I they to use, and that will convert into number

**[17:18](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1038s)** of shots and it will basically get some measurement and from measurement it will create um the colors. Um I can also use a fake provider, so KissKit provides this option to actually download a snapshot of the quantum computer state. Uh so you can simulate noise and other um things and like topology of the specific hardware. So I can actually use IBM Berlin, which is based in Frankfurt, but it's just named this way. And it will generate me some shots based on on this fake provider. So this is the idea behind the as you can see those are very beautiful, very random colors. Uh but I can also run it on a real QPU and we'll see

**[18:06](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1086s)** if they works. Let's Let's run a hundred. And that will show me some work loss. It should show me some job I was scheduled. As you can see and it's actually scheduling some job to a quantum computer and uh yeah, we're just spinning the qubits and making a measurement out of it. So nothing nothing fancy. It should take two one or two seconds, but of course we have to wait in a queue because I'm just using open plan, so it's it's it's a free plan.

**[18:53](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1133s)** So I need to wait for a queue to um to finish. As you can see it finished. The job has finished on a real quantum computer super exciting and this is the my read reading just 100 or 300 of zeros and ones which I just converted into um into colors. So, this is actual job from quantum computer um absolutely random zeros and ones converted into ANSI colors. And that's uh that's the whole point of of the demo just to show you that you can actually schedule a quantum jobs uh design them and uh play around with them. All right.

**[19:50](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1190s)** All right. So, as you can see, um classical So, yeah. Some of the key takeaways I wanted you to take. So, um classical computers just fake this randomness uh this pseudo randomness which we know about, and uh it's a well-known problem. Uh but they're very good at it, and uh we use very complex maths to actually fake it. Uh that's why we can use it for a modern uh encryption. But quantum computers are actually random by the nature of quantum physics, right? So, quantum num random random num- number generators already exist. There are some products like chipsets which are based on photonic um photonic qubits. So, they can be very small, and they can work in a room temperature. And but it basically uses the same

**[20:38](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1238s)** principle as I showed you. Superposition and measurement. Additionally, it does some cleanup on because the real hardware will have some noise. I did not take it this into consideration completely. I just wanted to have a random colors, so I didn't care about that. But normally, there's um there's some error correction which you have to take into consideration when you're designing your um your circuits uh to actually give you the the the best results. And the number of shots you run is basically uh a way of um figure out if you actually having the right results you you want to. Um you can try that even tonight. I know it's Friday, but like it's a weekend project. You can you can actually learn about the quantum computing and circuits and Qiskit and a bunch of other

**[21:28](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1288s)** frameworks. Um which every company is actually um creating, but IBM is uh providing this open-source Qiskit, which is the factor like a standard in in in the quantum computing. Uh so, Bracket, um Microsoft, IonQ, they give you some access to paid plans. So, you can pay um it's not super cheap, but it's also very quite affordable, I would say. IBM is giving you some open plans you can play around and test. And um definitely we go through certain tutorials, you will hear about Bell state, Grover, Shor. Those are the algorithms which you can actually try to understand and how quantum computers actually speed up certain things. Like Shor, as I said, is for factoring prime

**[22:16](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1336s)** numbers. Uh Grover is a search algorithm, and Bell state is a entanglement, which is uh yet another concept of uh quantum physics. And um yeah, those are the resources I highly recommend if you want to um have them and also the scripts which I was using. Feel free to grab my repo uh from GitHub, and you have some scripts in you have some links to the different documentation. So, IBM Quantum Learning is super super nice. Um they have some free courses, free education. Microsoft Learn is very good. Uh those are very specific to IBM or my Microsoft platforms. Um Black Opal is a paid option, but it's more generic on quantum computing and quantum physics. And you have a bunch of frameworks. As I said, Qiskit is one of

**[23:05](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1385s)** the most popular one. Microsoft has so-called quantum development kit and they're using language called Q#, which is based more on C#. If that's more your boat, then Qiskit is Python. QDK is more C# Q#. Google is providing their own. Nvidia is providing some some frameworks as well. IBM is developing some MCP servers. Also, they have this IBM Bob coding assistance, which is also trained very well on on Qiskit and quantum computing. And if you want to have some specific LLMs trained for Qiskit and development of quantum computing, you can find them on on a on a hugging face. And

**[23:57](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1437s)** Yeah, so feel free to feel free to grab a repo code. And I think we have some minutes for questions if you have any, but Yeah. >> [applause] >> Thank you so much, Yacoub, for this enlightening session. Uh We have three questions. I think we have some time. First one is from Ali Salman. Can quantum safe encryption be broken by another technology? Even if it's only theoretical now. >> Um

**[24:43](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1483s)** I would say that So, the Shor algorithm is one of the examples where you can actually um theoretically break RSA encryption, but that requires hundreds of thousands of qubits. Um physical qubits and logical qubits, which is a kind of I don't want to dive too deep into it, but um we are saying that we're still far away from this as a as a different technologies um are trying to achieve more and more qubits. Um but there's a there's very speedy development in that field. So, we have to be aware of that that at some point um quantum computers or hybrid computing can can break uh certain encryption algorithms has been offered. As as of now, it's not possible because we don't have enough.

**[25:38](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1538s)** Okay. >> Okay. >> So, thank you. >> Yeah. >> Yes, so the quantum safe So, well, post-quantum cryptography is is taking into consideration potential breaks of quantum uh by using quantum computers. Um uh but yeah, it's it's based on certain assumptions, right? So, so we we we I I think it will be ongoing process of uh quantum safe cryptography in general. Um and uh other emerging technologies which can also come out of it, right? Like a hybrid computing uh with GPUs and QPUs.

**[26:26](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1586s)** >> Thank you. Uh the next question from Kristoff, "Could quantum randomness be attacked by sneakily using entanglement?" >> Uh that's a good question. To be honest, I don't know. >> Surely >> Um I don't think so by the nature of entanglement um which is uh I don't think so, but I'm not a quantum physicist, and I know there are some sessions over about quantum computing here, and led by a couple of other guys. So, I can I can get back to you on this, but I don't I don't think so, but I'm not sure. >> Thank you.

**[27:15](https://www.youtube.com/watch?v=kWqi4mY3YfU&t=1635s)** Uh next one is from Karim Shehab. How reliable are Okay. So, I think we are out of time right now, but we uh Yakub is still available for some questions if you are if you want to take with him offline. Thank you so much, Yakub, for your time today. >> Thank you so much. Thank you, everyone. >> Thank you.
