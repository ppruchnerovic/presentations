---
id: 717
title: "Cryptographic agility for a post-quantum future: Falcon signatures in TypeScript"
slug: cryptographic-agility-for-a-post-quantum-future-falcon
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Security & Privacy"
type: "Keynote/Talk"
stage: "Stage 13"
tags: ["Cryptography", "Quantum", "TypeScript"]
speakers: ["Andrew Funk"]
speaker_companies: ["Algorand Foundation"]
day: 1
starts_at: 2026-07-09T12:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=MvuRFCtsicI
video_id: MvuRFCtsicI
session_page: https://app.wearedevelopers.com/events/16/session/717
transcript: true
---

# Cryptographic agility for a post-quantum future: Falcon signatures in TypeScript

**Andrew Funk (Integrations Lead — Algorand Foundation)**

`Track: Security & Privacy` · `Type: Keynote/Talk` · `Stage: Stage 13`

`#Cryptography` `#Quantum` `#TypeScript`

[Watch the recording](https://www.youtube.com/watch?v=MvuRFCtsicI) · [Session page](https://app.wearedevelopers.com/events/16/session/717)

## Abstract

Recent advancements in quantum computing are changing estimations of how soon classical cryptographic algorithms may be at risk. In this talk, we’ll explore the Falcon post-quantum signature scheme, how to apply it through a simple TypeScript library, and how Falcon signatures can be used to secure data today against tomorrow’s quantum attacks.

## Speakers

### Andrew Funk

*Integrations Lead — Algorand Foundation*

Andrew is Partner Integrations Lead at Algorand Foundation and has worked on the IT side of the payments industry for the past 20 years and has been an active builder in the Algorand ecosystem for the past 4 years. He has built several public-good products such as AlgoTools, FUNC Node Manager, and Lute Wallet. He now leads partner integrations for the Foundation.

## Transcript

*2,855 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=MvuRFCtsicI&t=3s)** cryptographic agility for a postquantum future. Um and so that is to say that we're going to talk about falcon signatures today but um broadly uh postquantum cryptography uh and implementations uh and uh going to be specific to the Algran blockchain uh because uh we have implemented those there and um so we're going to look at what that implementation looks like and how easy it is to uh sign in Typescript with these new uh cryptographic schemes. Uh I want to be clear that I'm not a cryptographer and so I'm just a developer that enjoys uh implementing these uh wonderful tools that are built by our brilliant engineers at Algrand. And um so I will be able to answer

**[0:52](https://www.youtube.com/watch?v=MvuRFCtsicI&t=52s)** questions in in terms of the implementations, but I can't go deep into how uh how all this stuff works. Just want to set that out there. Um I uh in my previous job I worked as a database engineer which means you know I kind of got kept in the basement uh and I didn't have to talk to many people. So this is a a new world for me getting on stage and uh very nervous. So uh bear with me. It it did help that uh I got delayed for 10 minutes though. All right. Um so for a little background uh Algarand when it was uh created was uh built on the Edwards curve uh which is um elliptic curve cryptography. It's used in a lot

**[1:42](https://www.youtube.com/watch?v=MvuRFCtsicI&t=102s)** of places uh all over the web and um for security purposes um you'll find this Edwards curve and uh the problem that we're dealing with is that with the advent of uh quantum computing um it threatens signatures and keys uh from elliptic curve cryptography. So we are at the Algrand Foundation working uh to get those uh replaced with post-quantum resilient uh methods such as uh lattisbased cryptography uh falcon scheme. Um one of the reasons that we chose uh Edwards curve in the first place is that it has very uh small footprint in terms of the size of the keys and the size of

**[2:30](https://www.youtube.com/watch?v=MvuRFCtsicI&t=150s)** the signatures. All of this uh size and computation is uh really important for blockchain purposes because you don't know the the hardware that uh these nodes that are uh supporting the chain is going to be running on. So you want to keep things as light as possible and as small as possible because you're trying to distribute a lot of data really quickly. Um it's kind of a fun area of computer science because you get to go back to a lot of these um really fundamentals of you know down to the bit level uh when you're when you're uh doing some of this this work which is kind of refreshing and fun. Um but uh that is to say that it's sensitive to to that level of stuff. And so when we're looking at uh making these more secure and coming up with a a good fit uh we we're are looking at size of

**[3:19](https://www.youtube.com/watch?v=MvuRFCtsicI&t=199s)** the keys and signatures very closely. That's why Falcon was chosen and has been developed uh by an in-house cryptographer that we have at the Agrarand Foundation by the name of Chris Pikert. uh and uh like I said a lot of the other engineers that are uh working to create uh the tooling around uh this and implement the op codes on chain that allow for signature um verification for these uh new schemes. As you can see uh Falcon signatures are much larger than the Edwards ones and right now we are uh working on Falcon 1024. Uh there will be a Falcon 512 implementation coming. Uh but and while that's smaller, it's considered uh slightly less secure. So, you know,

**[4:06](https://www.youtube.com/watch?v=MvuRFCtsicI&t=246s)** possibly for ephemeral uses, uh you might use something like Falcon 512. Uh the demo I'm going to be showing today is for Falcon 1024. Um in order to secure a blockchain, uh Algarand's taking this in sort of three phases that can be thought of. uh as the past, present and the future. Uh the in the the the past we have uh these state proofs that basically uh testify the state of the chain and record that as a proof uh as as the chain progresses. Every number of blocks you have one of these state proofs and so it prevents tampering with the history of the chain. That's been in place since 2022. And um those have been chugging along. We so we

**[4:55](https://www.youtube.com/watch?v=MvuRFCtsicI&t=295s)** have this historical security in place and have uh what we're working on now is the the present which is accounts and so that's what most people think of when they think of um blockchain or cryptocurrency are the the accounts that you have uh your funds in and that you uh sign with. That's what the demo is going to be today. And then looking forward into the future, uh we we're also going to be uh looking to implement these Falcon signatures into or or possibly some other method into the consensus mechanism that uh ensures uh random and fair uh choosing of who proposes the next block in the chain. Um here are some relevant repositories to Oh, I'm not going to be able to do

**[5:42](https://www.youtube.com/watch?v=MvuRFCtsicI&t=342s)** the demo. Um well these are the relevant repositories to uh what we're what [snorts] I was going to show you. Uh uh I suppose this will be recorded or you can take a photo here if you want to um have these uh the GitHub repos all this is open source. It's uh they're kind of in order here of um the dependencies. So uh first we have the falcon implementation in C which the web assembly and TypeScript bindings are built on. uh the Algrand SDK which sort of ties all of the uh Algarand specific uh stuff into the uh the TypeScript and WASM uh package there and all of that

**[6:33](https://www.youtube.com/watch?v=MvuRFCtsicI&t=393s)** implemented in a wallet uh which is actually a wallet that I built prior to joining the foundation uh sort of as a side project. Um, and that is something I could show you, but yeah, not not going to have access to all the demo which is on my other computer. Um, trying to think if there's any way to get to that. I don't suppose there is. So, unfortunately, this is going to be cut short a bit. Um, guess I'd like to open up to questions

**[7:22](https://www.youtube.com/watch?v=MvuRFCtsicI&t=442s)** given that I can't show the demo or the code. >> Sure. Um what I was going to do was uh spin up a um so I have we have development versions of the node uh which is the code that is all the nodes are running that um that supports uh the native uh Falcon accounts. So that's new and in development work and we have a development version of the SDK that is integrated into loot. And so it's all it's all uh very easy to create

**[8:11](https://www.youtube.com/watch?v=MvuRFCtsicI&t=491s)** these Falcon accounts within this uh crypto wallet and uh sign and transfer and then I would pull up the um uh those transactions from the chain and show that yes those signatures are quite large uh but it does work. uh they're small enough uh that that it works and the computation cost is also small enough that you can run those on a hardware wallet like a treasure. Um so that's the uh sort of postquantum future that we're looking at here and uh and building on Algrand. We um are leading the way in that regard. Um Brian may be working on uh

**[9:00](https://www.youtube.com/watch?v=MvuRFCtsicI&t=540s)** making this available. Any other questions? >> Yes. Uh a mic there. Yeah. >> Um if the new algorithms take more time decryting them like uh they are more complex. So is it um is the time for algorithms is more substantial than the previous ones. >> I'm sorry I'm I'm having trouble. >> I mean these are asynchronous um asymmetric algorithms right curves should be asymmetric right. So um from what I know that if the algorithm is more complex uh it will take more resource and time for decryting this algorithm in the back end right if I'm not wrong. um is is the question that it's more complex to process the

**[9:49](https://www.youtube.com/watch?v=MvuRFCtsicI&t=589s)** Falcon signatures than the Edwards ones. >> Yeah. >> Yes. Quite a bit. And and so that's why you know the the size of those uh of the signatures and the and the keys is very important and as well as the computational cost uh because yes the nodes have to be able to verify those transactions and like you said we don't know the hardware necessarily that uh the nodes are running on right now. uh many of the nodes on Algrand are running on people's home uh machines running off their home internet connections the uh the requirements are very low currently uh we'll see with with Falcon uh it if it does if the requirements do increase it wouldn't be much that's what that's what the the goal is is to keep those requirements very low for running nodes that's important for distribute uh you know keeping everything distributed uh

**[10:37](https://www.youtube.com/watch?v=MvuRFCtsicI&t=637s)** uh decentralized >> second Any other questions? Oh, cool. Uh, where do we have that? Oh, nice. Okay, we do get to see the demo after all. Okay. So, we go full screen. Oh, that's me. We go full screen.

**[11:28](https://www.youtube.com/watch?v=MvuRFCtsicI&t=688s)** Close. That's on their screen. That sidebar. So the first thing I'm going to do here is start up sandbox. Uh we have uh this uh basically is a local network of Algrand running just on this computer where I control all of the ALGO or the the native token on the on the chain. Uh we have really nice tooling to allow you to run local networks like that so that you don't have to just go straight to testn net in order to test things.

**[12:20](https://www.youtube.com/watch?v=MvuRFCtsicI&t=740s)** This is the wallet that I was mentioning. Uh it's a browser extension. So that's what we're looking at here is um and this is one of the accounts that gets uh funded with some of that initial ALGO from the uh test network that I just spun up. I'm going to send ALGO from that account to a Postquantum account that I have already set up in this wallet. That was a um an Edwards signature which we'll go back and look at in the ledger in just a second here. And then we will send you see that postquantum account now has 100 ALGO balance that I just sent there. We're going to send

**[13:08](https://www.youtube.com/watch?v=MvuRFCtsicI&t=788s)** ALGO back to that initial account. And this signature, you can see the fee is a little bit more expensive. There's a little bit more data going on there. Um, this signature will be one of these Falcon post quantum signatures and then we'll take a peek at the code that made all that possible. Uh, so if we go back here and look in ledger, if we look at the first block, we'll see this is what a typical uh transaction on Algarand looks like today. This is the signature. Oh, zoom in. All right. Uh in uh this is the signature in in base 64. Um there we go.

**[14:01](https://www.youtube.com/watch?v=MvuRFCtsicI&t=841s)** I may be zoomed in so much that when we look at the the Falcon Sig, you're not even going to be able to see all of it, but uh [laughter] we'll see. Uh they are quite large. Okay, so that was that that's a regular signature there. in B 64. So this is that Falcon transaction. We do have to send the prime the the the private key of the public key rather uh as part of the transaction because those aren't stored on the ledger like the traditional Edwards uh scheme. Uh and then this is so that the the large one at the top there was the the public key and this smaller one at the bottom is the signature. Um compared to other lattis based cryptographic

**[14:51](https://www.youtube.com/watch?v=MvuRFCtsicI&t=891s)** schemes, this is small and so that that's again that's why this uh scheme was chosen. Uh so we can take a peek at the code there which there's not going to be a ton to look at here because uh of the nice SDKs that we have. So this is uh the context of uh this curly here is we're inside a loop where we are signing all the transactions that have been submitted to the wallet. So, uh, if it's a from a Falcon account, we want to, uh, enter this. And, um, we have the seed for that Falcon account decrypted and stored in the wallet. So, first thing we do is see if we've decrypted it before for a previous transaction. If we

**[15:38](https://www.youtube.com/watch?v=MvuRFCtsicI&t=938s)** have, we can kind of skip this. If not, we need to decrypt that seed and uh, throw it in uh, this local buffer. And we that way we can reuse it if there are multiple transactions from the same account. Um once we have decrypted that with the password that was provided by the user, we can create a signing key and sign the transaction and push that signed transaction into the signed transaction array that will be eventually submitted to the chain. Um and that's about it. That's uh what I wanted to show you guys. Um how easy it can be to uh start building some uh postquantum

**[16:25](https://www.youtube.com/watch?v=MvuRFCtsicI&t=985s)** resilient uh SDKs and uh cryptographic wallets. [applause] Thank you. All right. Thank you, Andy. So, finally we made it. We had the demo. We had some uh you had some good colleagues that helped there. And do we have any more questions? We may have still a couple stack a couple of minutes. Yeah, one in the back coming. >> I think I can. >> Yeah, but in the recording they will not be able to hear it. >> Hey. Uh so do I understand this correctly? This is all happening on the account level then, right? So people would need new wallets to actually do

**[17:16](https://www.youtube.com/watch?v=MvuRFCtsicI&t=1036s)** this. >> Uh well the SDK would make it so that uh you know any wallet could implement this sort of thing. This is a a TypeScript implementation. Um the Loot like I said is a wallet that I built. Um I like to use it for stuff like this like you know getting out in front on bleeding edge of stuff and uh quick development. Um it's really a wallet that's more suited for developers. It's not super userfriendly uh but it really is uh light and gets stuff done. The the main wallet for the ecosystem is a mobile wallet uh that's now uh built on React Native. Um so that is going to be sort of the standard and and really uh as soon as all of this is generally available in the um in the

**[18:04](https://www.youtube.com/watch?v=MvuRFCtsicI&t=1084s)** node code and in the uh you know supporting uh SDKs it will be available in par wallet which like I said is the is the main wallet that uh folks use but uh yeah the idea is that every wallet would support it and and so we we work tightly to have uh standard ards so that we have interoperability. If you take your pneummonic from loot and restore it in parah, you have the same account because it's derived the same way. >> Thank you. We have another question over here. >> Uh thank you for your presentation. I wanted to ask on the kind of the [clears throat] state of a quantum as now of the quantum threat because the idea was that was kind of far ahead and like it's nothing to worry about. Now I think people are getting worry like getting much more worried about this >> uh kind of being in the midst of the

**[18:52](https://www.youtube.com/watch?v=MvuRFCtsicI&t=1132s)** things how far are we in terms of like what do we have now in terms of quantum computers what's kind of needed to actually break signatures what's kind of your take on like how far are we in terms not maybe not time but also uh progress needed to be done >> I' I'd want to uh answer that first by saying I'm not a cryptographer I think I'd mentioned that I I so I look to experts for for those sort of answers. I I think um you know Google has published a paper recently where they put out a date uh 2029. Uh I think there's some indication that it could come sooner than that. Um it's uh something that we're taking very seriously and and and preparing for as as quickly as we can. >> Okay.

**[19:42](https://www.youtube.com/watch?v=MvuRFCtsicI&t=1182s)** >> 2029 is really close. [laughter] Well, so no more questions then. Thank you, Andy. >> Thank you. >> Thank you, everyone. [applause]
