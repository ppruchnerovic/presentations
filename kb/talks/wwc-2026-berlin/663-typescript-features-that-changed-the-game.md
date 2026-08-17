---
id: 663
title: "TypeScript Features That Changed the Game"
slug: typescript-features-that-changed-the-game
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Languages & Runtimes"
type: "Lightning Talk"
stage: "Stage 7"
tags: ["TypeScript"]
speakers: ["Dani Coll"]
speaker_companies: ["Dynatrace"]
day: 1
starts_at: 2026-07-09T10:50:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=mDBU6GbvrB8
video_id: mDBU6GbvrB8
session_page: https://app.wearedevelopers.com/events/16/session/663
transcript: true
---

# TypeScript Features That Changed the Game

**Dani Coll (Senior Developer Advocate — Dynatrace)**

`Track: Languages & Runtimes` · `Type: Lightning Talk` · `Stage: Stage 7`

`#TypeScript`

[Watch the recording](https://www.youtube.com/watch?v=mDBU6GbvrB8) · [Session page](https://app.wearedevelopers.com/events/16/session/663)

## Abstract

TypeScript emerged as a practical, editor-first extension of JavaScript to help teams scale JavaScript with a structural, gradual type system and better tooling.

This talk traces that origin story and highlights the features that "changed the game" from strict null checking and discriminated unions to advanced conditional/template literal types and recent compiler performance advances.

## Speakers

### Dani Coll

*Senior Developer Advocate — Dynatrace*

Dani began his tech journey at a startup 10 years ago as a mobile developer. Over the years, he worked at several consulting companies, gaining some experience across multiple stacks. Eventually, he specialized in frontend development and is now focused on advocating for the field by writing technical content, conducting workshops and giving talks.

## Transcript

*1,688 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=3s)** Hello everyone. I wasn't expecting so much people for a lightning talk. So, yeah, I'm Danny. I'm from Barcelona and I actually been working in TypeScript for the last 10 years. And I thought about doing this talk. And I can see some friends here that are not uh TypeScript developers. They are more like Java developers. So, thank you for coming. Uh this is going to be short, so you won't suffer much. And I just want to clarify that this is not just a feature tour. I did one claim that is that TypeScript changed the game. And I will show you three proofs about

**[0:52](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=52s)** that. But first of all, I want to show you where TypeScript came from. So, TypeScript was shipped in 2012 to solve one problem. JavaScript, as much as I love him so much, uh it came to a point that it it wasn't scaling anymore in large projects. So, TypeScript came to the rescue being editor first, so types could power the auto complete and go to definition. You could adopt it gradually, so you got you could use allow JS flag, typings, use the any type, so you were not forced to use the types all the

**[1:40](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=100s)** time. It was a super set of JavaScript, so every valid JavaScript file was also valid TypeScript file. And it had zero runtime cost because types were erased at build time. But, adding types was never the breakthrough. There were other frameworks, other libraries that were already adding types back in the time. What actually changed the game was the expressiveness, types that could compute. A type system powerful enough so you could encode your domain logic, not just types. So,

**[2:27](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=147s)** we have this Papa Smurf here holding a potato. And TypeScript was not just about adding some types on your models, like in this case. So, we have this uh Papa Smurf that has a name and is holding a potato, and it has some weight, could be dirty or not, but you are not checking actually if the weight could be negative. You are not checking if you can eat a dirty potato. So, TypeScript did not add just types. And let me show you the first reason, the first proof that TypeScript changed the game, and it was through discriminated unions, and this became the death of the Boolean

**[3:19](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=199s)** soup. What is the Boolean soup? This is the Boolean soup. Here, we can have an example of a typical network state where we have is loading, is error, the data we receive from the back end, and the error, if there was any. So, we have data and error that are uh that could be undefined, but these four states are four independent flags. So, you could have up to 16 different representations of this object, but actually valid ones may be four, because you cannot have is loading and is the error at the same time. You

**[4:07](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=247s)** cannot have data and error at the same time. So, this was a problem in early TypeScript times that you have these conflicting attributes. And this was solved through discriminated unions. And in here, the compiler in with the Boolean soup couldn't help, but there was a fix to model the states. So, thanks to discriminated unions, you could add status idle, status loading, status success. And only when the status is success, you actually have data. And only when the status is error, you actually have error. If you try to access

**[4:56](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=296s)** the error on a success status, you will have that is not possible and TypeScript will will complain. And let's see about it proof. Let's see it here in a in a real case scenario. So, status idle, you show a placeholder. Status loading, you show a spinner. Status success, you show the profile. Status errors, you show the error. And then you have this type never that this means that this apparently should never reach here. So, if you forget something like s.data in this default state that never should reach here, TypeScript also will complain.

**[5:42](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=342s)** So, thanks to this never exhaustive mess, we made the compiler a state machine reviewer. So, why this change the game? This is the game because it's actually the model behind Redux Toolkit, thanks that query, status your reducer, and it did what Elm slogan um said. So, make impossible states impossible. So, uh thanks to TypeScript, it became the default mental model in front end. And

**[6:29](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=389s)** you stop asking what if data isn't defined here because you could know already at compile time. So, on the second case study, we have template literal types. And here we can see an example. So, the compiler is now able to compute over a string structure at compile time. So, not just check that something is a string, but also understand understand what's inside it. So, in here you have click, focus, blur, and the handler that is a modification of the event name. So, it already understands that you have the

**[7:18](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=438s)** handlers on click, on focus, and on blur. So, without manual listing or code generation, here we have one example real example that I really like a lot. So, we have the path params that is actually a beautiful recursive function in TypeScript that calls itself. And thanks to this template literal types, the network was no longer the the place where there was no typing at all. You could have You could get inferred the typings from the path, like in this case on the get, you can infer the ID and the post ID directly thanks to this path params parameter.

**[8:07](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=487s)** And you can say that user ID is not in this path params, so it will be a complaint by TypeScript. And why this change the game as well? Because it powers tRPC and TanStack Router. So the network boundary when where types began to die before, they are no longer there and they are safe function to call. And the final case study is that all this exhaustiveness in a small repo, it took seconds. But in a large repo, it took minutes. So all these new features that TypeScript

**[8:55](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=535s)** added, it was making the projects slower as more slow after updating to the new the newest version. So at the scale, the developer experience downgraded. So what did large code bases do? They used the minus minus incremental flag. So you could save the type graph into a TS built info file. And this just rechecks what actually changed. In this case, instead of checking everything, you just check the app.task script file. So you could change from 60 seconds to 3 seconds time. However, on call CI, it had no benefit. It only had benefit on local host.

**[9:45](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=585s)** Mitigation number two. Package B and package C were depending on package A. So, if you change something on package A source, nothing would change on package B on on package C. They were They could be skipped thanks to the project reference and the public type surface, this .d.ts, and this is what is used for every library right now. Mitigation number three, we have skip lib check file that it allows to uh skip all the type things on the node modules. So, you just check your code, and you might think this is dangerous, but you actually cannot do anything about the code that is not yours. So, anyway,

**[10:32](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=632s)** it makes sense, and this also save like 20 40%. And it's actually the the default one on byte, next js, and all the latest frameworks. What else? We have the import type. So, you could also use import type. So, the imports are erased entirely at at the mid, so zero JavaScript output. And there was no not more circular runtime dependencies. So, you got you could import type each other safely. Finally, we had mitigation number five. So, each file must be checkable without reading any other files. So, you could uh parallelize the compile by a

**[11:21](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=681s)** different worker checking different files at the same time. But, the final moment is what we have now. We have TS Go. TS Go is the new version of TypeScript, TypeScript 7, that will allow to be 10 times faster than before. And you can see from sources here from from Microsoft. They claim that VS Code takes 10 times faster to load, Playwright, TRPC, RxJS libraries. All 10 times faster. I have to say that um well, we have some complexity on our company. We haven't tried in all the apps that we currently use, but I've tried on

**[12:09](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=729s)** a side project that is a React JS game, and it was two times faster only. So, just bear in mind that on small on small code bases, this might be not that benefit as big as this one, but it's still uh great improvement. And if you are uh using TypeScript, consider updating and starting to try it. So, this changed the game because you finally can use TypeScript very easily, and it doesn't downgrade the developer experience. And can you use it today? So, in April, it was beta. Now, it's on release candidate, and I guess on July or August will be finally a stable. So,

**[12:59](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=779s)** um start testing it now on your own code base to surface migration issues. And I don't have more time, but there are so these are the breaking changes. And well, in the end, I did one claim, so I gave you three proofs. Discriminated unions, template literal types, and the rewrite of TypeScript in Go that make it made it 10 times faster. So, here you have some more extra features from TypeScript that satisfies the using and the pipe that is actually powering Zod, but in this lightning talk I did not have

**[13:45](https://www.youtube.com/watch?v=mDBU6GbvrB8&t=825s)** time to explain them. And all are the same idea, more precise modeling. So, I will end up my talk with this quote again, making possible states impossible. And thank you so much.
