---
id: 936
title: "Quantum DevOps - Enabling Industrial Engineering"
slug: quantum-devops-enabling-industrial-engineering
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Emerging Technologies"
type: "Lightning Talk"
stage: "Airstream 1"
tags: ["DevOps", "Integration", "NVIDIA", "Quantum", "Systems Programming"]
speakers: ["Ilie-Daniel Gheorghe-Pop"]
speaker_companies: ["Fraunhofer FOKUS"]
day: 2
starts_at: 2026-07-10T11:05:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=IYzsiPjS6i4
video_id: IYzsiPjS6i4
session_page: https://app.wearedevelopers.com/events/16/session/936
transcript: true
---

# Quantum DevOps - Enabling Industrial Engineering

**Ilie-Daniel Gheorghe-Pop (Researcher — Fraunhofer FOKUS)**

`Track: Emerging Technologies` · `Type: Lightning Talk` · `Stage: Airstream 1`

`#DevOps` `#Integration` `#NVIDIA` `#Quantum` `#Systems Programming`

[Watch the recording](https://www.youtube.com/watch?v=IYzsiPjS6i4) · [Session page](https://app.wearedevelopers.com/events/16/session/936)

## Abstract

An overview of the latest technological developments in Quantum Computing and with it the new possibilities for introducing quantum computing in the industrial automation field. This session outlines the key technological developments of the last year that bring forth the real possibilities of using quantum computing in industrial production processes. Furthermore it highlights the key areas where quantum computing may be successfully used in this field and what are the key technical aspects to be taken into consideration. Finally, it showcases a currently pursued practical use-case of developing quantum optimization algorithms for industrial chemical production using the Qrisp - powered by Eclipse high-level programming language.

## Speakers

### Ilie-Daniel Gheorghe-Pop

*Researcher — Fraunhofer FOKUS*

M.Sc in Computer Engineering, specialized in advanced computer architectures. Now researcher at Fraunhofer FOKUS in Quality Engineering for Quantum Computing. Works in several industry and research projects in the fields of quantum computing, artificial intelligence, IoT, IT security and telco. Main interest is researching efficient application development and implementation of algorithms especially in the quantum domain (Quantum DevOps). Other areas of interest are quantum computing, quantum networks, IoT, Industry 4.0, 5G/6G, AI, robots and the high-level quantum  programming language Qrisp.

## Transcript

*1,388 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=IYzsiPjS6i4&t=0s)** Hi everyone. My name is Daniel. I'm a researcher at the Fraunhofer Institute in Berlin here. And starting 2019, I think I joined the team that was doing research in quantum computing. It was a very exciting time. We had those days the quantum computing hype. And we started on our journey there. And today I want to bring you on this journey and tell you something about how we can bring quantum computing to industrial engineering. So, when you think about industrial engineering, you think about factories, really precise processes, um traceability, reliability first and first and foremost, and of course zero fault tolerance, and um very much deterministic in any way possible. You want to build a car, you have the parts, you source them, you assemble them in a very orderly and fashionable um mode. And by the end of

**[1:03](https://www.youtube.com/watch?v=IYzsiPjS6i4&t=63s)** the process, you have a car. If there's a fault, you can trace that fault, find where the error was, what the system uh what was the system that caused it, and of course fix it so you have uh replicable results every time. On the other hand, we have quantum computing, this new emerging um scientific field, which is now still at an experimental and pilot stage, where by its nature the results of a quantum computing um process or application is probabilistic. It's not deterministic. So, you have to run the same experiment multiple times, tens, hundreds, thousands of times to get uh quality, how do they call it? Probability distribution that can help you understand which is actually the result of your calculation. And if we want to bridge these two worlds, you might say they're really not compatible with each other. On one hand,

**[2:09](https://www.youtube.com/watch?v=IYzsiPjS6i4&t=129s)** you have classical engineering culture where all the processes are are well-defined. You have reliability, predictability, audit traceability very low fault tolerances. And on the other hand, you have quantum computing where everything is experimental. There's really a lot of changes every month. There's new developments in quantum hardware. There's little to no standards. And you think this this is not going to happen. So, if you go to a process engineer and say, "Hey, we want to deploy a quantum computer on your factory floor to optimize your production system." He's going to say, "Okay, is it reliable?" And at that point, you might say, "Okay, the hardware is not there yet. It's not production ready. It's got some faults. It's got error rates that change every day depending on the calibration."

**[3:08](https://www.youtube.com/watch?v=IYzsiPjS6i4&t=188s)** But it's not only that because you have the hardware, of course, on on one side, but you also need something that in engineering we've been doing for the past tens of years. We have this really well-put-in-place processes. And I'm going to tell you again and remind you, of course, because you're here mostly developers that we can apply the same development processes and development cycles to quantum computing software, as well. And I think that will be able to bridge the gap between quantum computing and industrial engineering because once you can ensure people and convince a production engineer that this process is reliable and you can certify it and have a standard on it, then he might be able to trust you on it and and make it work. So, what happened in quantum computing

**[4:09](https://www.youtube.com/watch?v=IYzsiPjS6i4&t=249s)** before? I I have this talk yearly. Back in 2025, I was saying the Moore's law is coming to an end. So, some say it already did come to an end, but of course it suffered some transformation. There's now um uh Huang's law and there's also the new Tao law about folding chips and making them uh faster by reducing the time it takes for the information to to circulate around the transistors. And of course the the super uh chips from Nvidia have proven that they can actually uh be greater than than Moore's law in the last year. They actually tripled the the capacity. But leaving that aside, uh we have uh new developments in in quantum computing. Just the past months, I think there was uh uh proof from IBM showing a nice uh

**[5:10](https://www.youtube.com/watch?v=IYzsiPjS6i4&t=310s)** impossible classical calculation done on a on their 100-qubit uh machine that solves a specific problem in 200 seconds opposed from I don't know how many years on classical computers. We have error correction breakthroughs. I think it's Google Willow that proved that they can do error correction that scales with the number of qubits that they put on a chip. And of course we have some uh dual modality hardware where they try to combine different technologies for quantum computing, atom-based and gate-based computers to work together. And we have a lot of early pilots. so a lot of quantum applications for different optimization problems ranging from logistics, uh scheduling, shipping, and of course on the other side on material technology, developing new molecules for uh the pharmaceutical industry or developing new materials for the

**[6:11](https://www.youtube.com/watch?v=IYzsiPjS6i4&t=371s)** avionics uh industry to make like better products in the end. But still these are still early-stage pilots. We don't have an actual production-level quantum computer computing system. And of course we have some standards coming out like the ones for security because partly the quantum computing was made famous by Shor's algorithm, which proved it can break uh RSA encryption in a in a linear time. So now we have new security standards. We have this post-quantum cryptography and new uh cryptographic schemes being tested, deployed, standardized from US, EU, and being rolled out over the next years. I think until 2030 everything will be secured and hopefully uh quantum safe, so you can be happy that you're not going to lose all your banking account uh dollars or money on that. But still we're we're talking about quantum

**[7:13](https://www.youtube.com/watch?v=IYzsiPjS6i4&t=433s)** computing in industrial processes and in the industry. So we don't want to scare anybody. We're not going to to put a quantum computer do uh resource uh management or or operations management. We're just going to uh have it inside the process where you already have your resource planning, your production system, your uh operations optimizations, and in those just some sub problems, some specific problems can be handed over to quantum computers to do faster and better calculations. And of course, the results go back into the loop. And the current like blockers apart from the standardization issue, so trust established between between enterprises is a lack of IT personnel. Because you go to a factory and say, "Okay, we have this awesome quantum computer. It can help you speed up your development. It can help you increase production and

**[8:16](https://www.youtube.com/watch?v=IYzsiPjS6i4&t=496s)** reduce energy consumption." But you need to handle it yourself. So, he said, "Okay, I don't have enough engineers. I don't have quantum physicists on my team. So, what do we do?" Well, we try to do a really robust development processing cycle. And we need some programming languages to to help us make it more accessible for for engineers. And um I think if we applying the same discipline that we have been applying to classical computing and classical software development to quantum computing development, this is going to be achievable in the long run. So, we need to apply tests, automatic test generation, certification, um benchmarking experimentation and all the concepts we apply to to current production systems, we need to be apply them as well to quantum computing applications. And we at Fraunhofer believe strongly in

**[9:17](https://www.youtube.com/watch?v=IYzsiPjS6i4&t=557s)** that. We don't think that a new algorithm will magically change everything or a new programming language will will bring all the world into quantum. But, we do believe that quantum computing doing being done well will will help us reach that. And that's why we created Crisp, quantum high-level high-level programming language based on Python for helping developers join the field. And we also started standardizing this software stack across Europe using Sense and Alec and the German DIN spec. We have already published it and actively working on it. So, we highly encourage you to look out our website, check our tutorials, and join us. Because it's going to be exciting and I'm pretty sure it's going to be the next big thing. Thank you very much. >> [applause]
