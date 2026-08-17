---
id: 780
title: "Playing Pong on a shoulder press machine"
slug: playing-pong-on-a-shoulder-press-machine
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Emerging Technologies"
type: "Keynote/Talk"
stage: "Airstream 1"
tags: ["Internet of Things (IoT)"]
speakers: ["Daniel Meilak", "Enris Nogare von Tein"]
speaker_companies: ["EGYM"]
day: 1
starts_at: 2026-07-09T14:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=Uw1zFipBs1I
video_id: Uw1zFipBs1I
session_page: https://app.wearedevelopers.com/events/16/session/780
transcript: true
---

# Playing Pong on a shoulder press machine

**Daniel Meilak (Senior Software Engineer — EGYM), Enris Nogare von Tein (Team Lead — EGYM)**

`Track: Emerging Technologies` · `Type: Keynote/Talk` · `Stage: Airstream 1`

`#Internet of Things (IoT)`

[Watch the recording](https://www.youtube.com/watch?v=Uw1zFipBs1I) · [Session page](https://app.wearedevelopers.com/events/16/session/780)

## Abstract

What happens when you give a group of engineers a motor-controlled, high-tech strength machine and 24 hours of "Hack Day" freedom? You get a 300kg game of Pong.

In this session, we take you behind the scenes of EGYM’s ecosystem to show how we connect serious sports science and arcade nostalgia. We’ll walk you through the hardware and software stack of our Smart Strength machines, proving that with the right firmware and a bit of C++, any gym floor can become a playground.

What We’ll Cover:

- The anatomy of an EGYM Strength machine: a short introduction of our hardware, what makes a machine "smart" and how it differs from normal gym equipment
- Building the Frontend: using C++ and Qt to build a functional game UI
- The hardware part: we’ll explain how we utilize firmware-controlled motors to map lever positions to paddle movement, and how we use variable torque to create a customised feel
- Networking the gyms: a look at how our machines communicate with each other and our core backend to enable real-time, head-to-head multiplayer
- How to deploy: from a "buggy" demo to a polished release. showing our CI/CD pipeline, demonstrating how we push updates to machines in the field and swap GUIs on the fly (live coding/demo effect there)
- Beyond the hackdays: our journey to production, using Pong as an example, including the vital roles of testing, sports science validation, and fleet monitoring

## Speakers

### Daniel Meilak

*Senior Software Engineer — EGYM*

Dr Daniel Meilak is a Senior Software Engineer with a background in Computational Physics. After 9 years of grueling studies, he found that life became a lot more exciting when he was able to write bug ridden lines of C++ at EGYM

### Enris Nogare von Tein

*Team Lead — EGYM*

Born in Brazil, loving tech since very young!
Graduated in Computer Science and worked for ExxonMobil for a bit, afterwards came to Germany to work at e.Solutions and then finally at EGYM SE!
Magic the Gathering aficionado and hoping to lead bigger and bigger teams in the future!

## Transcript

*3,434 words · source: yt (en)*

**[0:02](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=2s)** Lovely to be here. Um, thank you very much for coming on such a beautiful day. Uh, my name is Daniel. This is Enris. Um, we're both from Egypt. And, uh, we'd like to tell you a little story about a hack day project that we worked on a few years ago. Um, I very much hope that it's going to be a little bit of a familiar story to other people in the audience. Um, and if not, something that will maybe inspire you to do something similar. Um, so it's going to be playing Pong on a shoulder press. >> Um, I won't go into too much detail because Andrew here is going to give you some nice background. >> Yeah. So, hello. Uh, I'm as Daniel said and we here at EIM. Uh, first of all, does that who here knows what EGM is? That's actually quite a lot of people. All right, this one I had to press the

**[0:50](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=50s)** button. Um yeah I mean Eim in here in EIM we are a fitness company which likes innovating a lot on the world of fitness and we have like more than a thousand people working for us already and we have two main product lines we have well pass who here knows about well pass or has it >> okay >> okay that's not a lot of people we need to expand a little bit more in Berlin um and we also have the strength machines the workout machines that we sell uh which who here has worked out on one of our machines. Not a lot of people. That's a bunch of nerds. That's fine. Uh to be expected here. Uh but yeah, I'll focus a little bit more on the strength machines. Um what are the EGM strength machines, right? So a regular machine is strength machine is where you go go to gym and

**[1:41](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=101s)** then you have to set it up, have to do this the stacking thing of the weights, you have to know how to do the the actual exercise. And the good thing about the aging machines is that you don't need to know most of that. Uh since it's an a digit digitized machine like fully digital uh with a motor inside uh we can kind of do almost all of that for you, right? So you go in, you log in with your uh RFID or or or something like that. And it already uh loads all the data from uh your account. So it sets the weights for you and it sets your training plans and all those things. uh automatically. So you don't have to change anything. It does all of that on the fly for you. And one of the good things about that is that we can also do training plans. So

**[2:29](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=149s)** if you for some reason don't have access to a personal trainer, you just get one of our training plans and that will help you work out, right? And that is as you can see on the small video that is playing. It is quite easy to use it. And we have I think the video is stopped right now, but that's fine. I think you guys saw saw it earlier. Uh even teaches you how to use the machine, how to properly use the exercise so you don't hurt yourself, right? Which is something that helps because me for example, before I started using the the the swing machines, I had no idea how to work out in a in a gym, right? Um and as I mentioned here at EGM, we like to innovate a lot, right? But how do we do innovation in the stack company

**[3:18](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=198s)** with all of our machines and all of our developers, right? And there are a couple of ways that we do that. Uh we do some workshops to share information. We do some uh uh developer conferences where we get everybody together to share what they're doing and what they're working on and what is the cool things they are seeing. Some learning days which we have about 10% of our days for just learning about about stuff. doesn't need to be work related, but usually is. And the coolest one that we do, the hack days, which is where we have some dedicated times, usually two or three or four days, uh, per year to basically break stuff, like try some new ideas, shake the pot a little bit, see what happens, and where we get like ideas for stuff like playing Pong or Doom, which dude, we should do

**[4:08](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=248s)** Doom next time. >> We can team up next year. >> Next year. Um so yeah uh the hacker were decided to do all these crazy weird projects and that time we decided to do pong. Everybody here know what's knows what pong is, right? Okay, good. And that game comes with a little bit of a challenge, right? Because how do we change our our strength machine using our fitness equipment into basically a game console? And how do we do that without killing anybody? Because we are working with a workout machine. So it can output a lot of weight, right? And if we don't do our um our safeguards correctly, we can hurt

**[4:58](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=298s)** people like um but don't worry uh the machines are safe. We have all the safeguards uh in place already. So you can work out uh in them without an issue uh and you will not hurt yourself but it can happen if you something up. And there also some other uh simpler challenges, right? So first of all the goal like how do we put Pong in a strength machine and how do we change the input? Because usually Pong is played with a joystick, right? or like a a lever of some sort. How do we change the input into an actual lever that's outputting like 200 kg of weight or something? And how do we actually show you Pong? And how do we make the machines talk to each other, right?

**[5:47](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=347s)** Well, to do that, we had to use all four parts of our stack, right? So, front end, back end, the normal stuff. I think everybody here knows about it. And for the 10% of you that are root uh firmware and hardware which we also do in Egyp because the machine is custom built right and yeah to explain a little bit more about how we are we solve this issue and solve this challenge I will switch over to my colleague Daniel. >> Thank you very much. All right let's talk a little bit about firmware and hardware. So okay um to get started with so you have we have roughly 20 different exercise machines and the basic idea is going to be the same on all of them right so you've got a lever that you're going to push or pull against um and that lever

**[6:36](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=396s)** in turn is going to be connected not to a weight stack like you would probably expect for most strength machines but actually to a motor and that motor can do I don't know about 300 kilos it depends on the kinematics the exact exercise of weight on whoever is working out. But the important thing is we can reduce it as as we like. Um, crucially, we can reduce it really quickly. I mean, well, wind's a bit loud. Um, we can, uh, adjust the speed, uh, adjust exactly how the lever feels. We can make it, um, for example, if you have want to have a weird like rumbling motion. Yeah, we can do all of that just by changing the firmware. So, obviously, okay, if you're going to be at a regular gym and you want to do normal workouts, then sure, you going to want to do some sort of

**[7:24](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=444s)** like nicely slow controlled reps. Um, the firmware is going to just ask for the weight to be consistent. Um, you know, you should really feel like you're just moving about a weight stack, right? But if instead we want to do something like pong, then we got to think about it a little bit because I mean, let's say you're trying to follow the ball around on the screen. Uh then you don't want turning around to be gargantuan effort. You don't want to just have holding the lever up in a constant position to be um too tiring. So we should make sure that the weight isn't too extreme and that the feeling is really responsive. That's all possible with the firmware. Um my gosh, what do I normally say next at this point? Um well, yeah, the firmware is going to basically help you to

**[8:11](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=491s)** achieve the feeling of Pong. So, we're going to try to like fool your senses into really thinking that you're just twiddling around with a little joystick and uh not using an actual strength work strength machine and doing a workout. So, if we manage to fool your senses, we need to fool your eyes as well, right? So, we need to make it look like Pong. So, I already talked about the lever on our machines. The other way that you interact with it is through a little touchcreen. I think you might have seen that in the video earlier, but you'll see it again later. That touch screen is, you know, uh, what's going to show you your exercise. You can follow the little training curve. It's also what's going to show you a bunch of useful information, how you can change the weight, choose your training program, whatever it is. For Pong, obviously, um,

**[8:59](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=539s)** we're going to want to show Pong. Now, we the the software stack for this is basically, um, C++ and cute QML. Um, I'm not going to say that we're doing some crazy hardcore processing that really needs a high performance programming language like C++, but we do have, you know, limited processing power. So, it does the job. Um, it's good enough for showing some static assets, a few animations here and there if you want to get fancy. Um, unfortunately, that's all we need for Pong, right? So, once you've got the design together, cool. You can write that all out in QML. Um you're going to need some logic, some simple collisions, um a point scoring system, um and uh as a C++ developer, I'd really

**[9:49](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=589s)** love to tell you at this point that this beautifully coded out in C++. Um but actually it wasn't JavaScript and QML because it was a hack day. Um I know, don't hate me, but um there are good reasons to do that, right? I'll remind you again, we're talking about a hack day here. you're going to have, you know, 1 to two days to get something from beginning to end. You know, you have nothing and by the end you should have something that looks pretty usable. And um in this case, QML has some really useful properties. I mean, it's got its own runtime. You can um basically edit it on the fly and get it to, you know, change design, change the behavior immediately. Um so that's going to be really important for this. But um to go a little bit deeper, I'll also talk about the other side of things that really

**[10:36](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=636s)** helped us to get you know from prototype to prototype to prototype for our hack day which was a rapid deployment system. So this is something that we're really happy with at Egyp. But we have machines you know all around the world and we deliver updates to them and this deployment system means that basically at you know I'm I'm exaggerating but it's really not that much more. at the push of a button. Then I can have a build with some local changes, you know, maybe a couple of bugs for fun and I can get that built um uploaded to the cloud and then with a simple assignment I can say, oh, I want it to be on that machine over there. And you know, within okay, from beginning to end, let's say 20 minutes, it's going to be right there waiting for me. So if you're in this kind of environment where you really need to rapidly develop, I highly

**[11:24](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=684s)** recommend that you very much take control of these kinds of tools. And if you don't have them, maybe hack day is the right place to start building something like that. Um I think it would be a great idea. So um at this point, let's see. We've got the design, we've got the logic. Um, we're starting to get some of the bugs out of the system. Uh, but it's still single player. I haven't talked about any multiplayer yet, have I? So, at this point in our hack day, we approached a few backend devs and we asked them, "Listen guys, um, so we've got one machine and it can play Pong. Uh, but we'd like it to broadcast to every other machine that it wants to play Pong with them. Um, can you do that for us?

**[12:14](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=734s)** And they said very politely, "No." Um, uh, the main reason being, to be fair, that if you're going to do be doing something like Pong, then the machines need to talk talk to each other constantly. You know, you need to be really live syncing the exact like state of the game. And, yep, fair enough. Our machines don't tend to absolutely blast the internet with communication of that kind. Um, so they said, "Can you try something else?" We said, "Okay." And uh then one of our developers, I wish it was me, but someone who had been at Egypt for a long much longer time, remembered that we have a little backup system in place. Um okay, this is going to be a bit hard to imagine for everyone, but um take yourself back in time and remember when maybe you're in a

**[13:02](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=782s)** gym and you try to connect to the internet and it's not very reliable. I know it's unheard of, especially in Germany. I I [clears throat] know. But um we built something that allows one machine to say in its local network um listen uh for example this user has just made an account he's got this name um he uh I don't know wants to wants to train with this training method and so that machine will broadcast that to the machines around it and cool he's just made a new account he can get up go over to the next machine sit down log in with his you know identifiable bracelet um and there you go they who he is even without any internet. And that's kind of perfect for Pong, right? We just say, "Okay, if you want to play Pong, then go to this page or, you know, screen." That

**[13:51](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=831s)** machine will start going, "Hey, um, this person wants to play Pong." And any machine around can connect to that and start syncing up. And the way we did it was, you know, one machine is going to be the the what's it called? like the head and it's going to send out all of the information and say like, you know, I know the game state and I'm telling you exactly how everything is changing. And so we did that and we tried it out and we got P working. So I'm going to talk over this, but these are two of my colleagues who very kindly offered to take this video. So, they're using the machine as would normally look basically and they're going to the settings and we add a little waiting room and they can join the waiting room and they'll see each other and then we can start our little hack of Pong.

**[14:40](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=880s)** So, we were very happy with the design overall. We tried to get some little retro assets in and uh you know theme it a little bit. And um it might not look like it yet, but once I zoom out, you can very clearly see that one person's on one of the paddles, another person's on the other. Um one thing that I will note is that when I I I kind of remade this for this talk to be perfectly honest, but when I put it on a real machine, it wasn't quite as fast as I thought it was. So, um maybe there's some some frames issues, but I promise, you know, you can't you can't tell that. It looks great, right? Um, but uh Oh, thanks video. But you got the gist. Um, we were very happy with how it came out and um afterwards they told us, would you guys mind just leaving this on a few machines so that the rest of the employees can come around and try this

**[15:27](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=927s)** out uh just for fun? But um I do have some bad news, which is um if you go to one of our machines today in a random gym anywhere um I'm afraid you won't be able to play Pong. I'm very sorry, but that isn't to say that none of the things that we came up with during this hack day three years ago didn't have any effect. So, I'm going to be an extra extra extra salesperson here for EIM and talk about this amazing feature that we made of 3 years agoish, two years ago, I think, called game day. Um, and it's oh, it's really cool. You can compete with your friends and um you can show off how strong you are. Now, the interesting part is you might notice on the right side there's a little leaderboard there. And as you do this exercise and, you

**[16:17](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=977s)** know, push out push around as much weight as you can, you'll go up the leaderboard. And even better, um, in certain gyms, as far as I'm aware, there'll even be a monitor separately for everything else. And depending on what exercises go, what exercises you are doing, you might show up on that exercise as the current leader on the leaderboard. And so, sure, we didn't quite get Pong to work. Um, you know, we didn't get it to production, but uh I'm pretty sure that this leaderboard idea came directly from that hack day. So, maybe some product manager somewhere was, you know, peeking through the windows or, um, seeing what we were doing. And I'm pretty happy because I think it's a really good idea to get people to be like, hey, I can I can move around more weight than you can. Um, so a nice result. I definitely think, you know, if you take anyway anything away

**[17:04](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=1024s)** from this talk, apart from, you know, how handsome both of us are, um, I think you should take away that hack days are really helpful. Um, and, uh, you can come up with some crazy ideas. You should definitely try them out. And, uh, who knows, you can literally like make some new product for your company by coming up with some crazy idea. So, yeah. Um, before we go, I'm going to hand it back to Enris to conclude. Um yeah, I hope we left you uh inspired to try some hack day projects of your own or maybe try them out in your company if you never did them. Uh and yeah, thank you very much for coming. Uh we have a booth at EIM uh at uh hall 2.2. >> Yeah, 2.2. Yeah. Yeah. >> B 48 between stage and three and four. And we are hiring. So, if any of you are interested to join in on this madness,

**[17:52](https://www.youtube.com/watch?v=Uw1zFipBs1I&t=1072s)** just let us know or scan the QR code or ask anybody with this QR code on their back. Um, and yeah, that's basically it. Oh, and unfortunately, you cannot play Pong on the machine we have here. We tried, marketing didn't let us, so sorry. >> It's also it's also harder to hide the bugs that are not in the build um at a booth, >> but you can do the other stuff. You can do game day. You can do game day for sure. That the one you can do. So yeah, thank you very much.
