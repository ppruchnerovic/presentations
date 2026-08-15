---
id: 729
title: "Rules, Heuristics, or LLMs? Lessons from Solving the Same Problem Twice"
slug: rules-heuristics-or-llms-lessons-from-solving-the-same
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "AI Engineering"
type: "Keynote/Talk"
stage: "Stage 6 - powered by Microsoft"
tags: ["AI Models", "Large Language Models (LLMs)", "Small Language Models (SLMs)", "Software Architecture", "System Design"]
speakers: ["Artur Naumenko"]
speaker_companies: ["Softeta"]
day: 1
starts_at: 2026-07-09T12:50:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=gAjwsmSvtIM
video_id: gAjwsmSvtIM
session_page: https://app.wearedevelopers.com/events/16/session/729
transcript: true
---

# Rules, Heuristics, or LLMs? Lessons from Solving the Same Problem Twice

**Artur Naumenko (Senior Software Engineer — Softeta)**

`Track: AI Engineering` · `Type: Keynote/Talk` · `Stage: Stage 6 - powered by Microsoft`

`#AI Models` `#Large Language Models (LLMs)` `#Small Language Models (SLMs)` `#Software Architecture` `#System Design`

[Watch the recording](https://www.youtube.com/watch?v=gAjwsmSvtIM) · [Session page](https://app.wearedevelopers.com/events/16/session/729)

## Abstract

Not every problem needs an LLM. But at the same time some problems are asking for LLMs as the solution. So, when to choose which?

I ran into this while working on a subjective text transformation problem. It’s hard to specify and hard to test. That made it into a brilliant grey zone. When the answer to the regular regular question "can it be done without LLM" is "yes, but...".

To understand the trade-offs, I built two solutions to the same problem. Both of them produce similar result, they just work in a very different way.

One is a "just code and math": rule-based stochastic system using Markov chains, edit-distance mutations and so on. The other is a LoRA fine tuned LLM trained on the examples.

In this talk, I'll share what I learned, so that you could build just one system, instead of two:

Where deterministic models offer better control
Where LLMs produce more natural results
How the results are different
Maintenance cost

As the problems sits in a grey zone and hard to properly measure, I will show a result of blind comparison between rule-based output and LLM output to determine whether LLM solution was necessary or overkill.

This is not a tutorial or an AI demo. You’ll leave with a practical way to understand and decide when the problem is LLM-worthy and when to stick to the good old code and algorithms.
It's a case study on how over-engineering once on purpose can save future effort and resources.

## Speakers

### Artur Naumenko

*Senior Software Engineer — Softeta*

I am a senior software engineer and consultant with 9+ years of experience working in banking, telecom, government, and enterprise domains.

A systems thinker and pragmatic generalist. Backend-first, infrastructure-aware and privacy-minded. Currently exploring applied AI direction.

Experienced mentor, speaker, and consultant, organizer of "summer academies" and different internal knowledge-sharing sessions with a strong focus on practical learning and software engineering reality.

## Transcript

*3,020 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=0s)** Hi. So, uh I'm Arthur. I'm a senior software engineer at Stoetta. And this whole talk started because one weekend I got honestly bored and instead of touching grass, I decided that I want to overengineer something on purpose. Take some maybe stupid, maybe small problem and uh make it suspiciously good. So, uh here's how it went. I solved the same problem twice. One time it was just with a regular Java roughly 520 lines of code and uh another time with a fine tuned LLM and both solutions work both produce convincing output and uh I had to choose choice to make uh which one to use which one is better because it can be uh which one works because they both genuinely do work and they produce very similar good results and uh I have to decide based on

**[1:02](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=62s)** something else which one wins and that's something else that's the talk. So I've got two tools on my table. Pure code. It is rules, math, algorithms. It is really unbeatable when you need to actually when you can to actually specify the thing what you're building, what results are you expecting examples or sorting the list, parsing some file or calculating with math like taxes. LLMs on the other hand can solve a more vague problem and you know roughly what is the input but you can't really program in a classic way the output for example translating Lithuanian to Japanese you can do it with code especially naturally or summarizing information like PDFs and uh if you need to soften the passive aggressive email well there's no if else statement for being passive aggressive so 11 can do that and there is a gray zone. Um, most

**[2:08](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=128s)** problems land clearly in one bucket of clean code, clear code and another bucket of just used LLM at this point. But some problems live in the gray zone. Um, the gray zone is basically I could probably code it, but maybe LLM can just do it and do it better. And what would define the gray zone? uh roughly there are three uh categories let's go on that um there is first one there is no metric for good when you can't define it when you can't test that result is actually good uh it is subjective and uh it's already algorithm it's hard to do with just clear code another another one would be um the c the h cases never end uh there are some cases where the topic, the rule set is so broad that you just end up adding and

**[3:12](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=192s)** adding more and more rules and you still end up with some edge cases you need to tune. Once again, maybe LLM could handle it, maybe you're better with uh adding more more rules, but uh yeah, it's a graz and um interesting thing is that both ways generally do work. So now let me be precise because in the title I promised three things but so far I've been speaking about two things. So here's three things. The first one is uh pure code classic code. It is rules. You write yourself all branches. You define the rules. There are if else statement if else statements there are lookup tables. So uh the approach is very deterministic. You know what goes in, you know what goes out. It is testable works every time. Fantastic. Then there is heristics approach. This is where the

**[4:16](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=256s)** things already start to become interesting because you expect some kind of input and you roughly expect some kind of output but you don't really know what it is because what are you doing with heristics? You're already rolling the dice. And good example of that would be for example procedural world generation in games. You have rule sets how it should behave but the result every time is different or particle system simulation and physics also you have a define some kind of rule set but output every time is separate is different and then the LMS basically you handle it the data and it decides based on example what it should be and here's the part that matters the gray zone is Not between rules and LLM, not between clearly code and LLMs, but

**[5:16](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=316s)** between huristics and LLMs. The moment your problem is too weird or fuzzy for plain regular rules, you're already rolling the dice. And at this point, you might probably as well hand it to And now we approached the topic that I chose to overengineer on purpose. It's making your text sound dry. You take perfectly normal messages and corrupt them on purpose. And yes, really, but bear with me. It is actually a near perfect specimen because there is no metric for this text is drunk enough. You can only subjectively measure that. And um you can code it with pure code, but deterministic hardcoded typos look well well they look fake. We want real drunken text. or you can actually sit at 2:00 a.m. at night near your PC and send your friend direct messages. So then it appears as you have interesting life

**[6:21](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=381s)** but yeah both um both approaches work. You can roll the dice with horistics or you can handle it with them and I and I have built both. Now, not sure how it would work out, but do you have any ideas how to make text sound drunk with mouth? You can just shout out or >> Okay, so I will help you. Come again. Maybe repeat yourself. >> That's actually one. Yes, repeating yourself can be a corrupted text symptom. Do we have another opinion? Okay, then. So, there is a second and there's a third. And here's what I actually did. This looks terrible. uh that's roughly 500 lines of Java code turned into one formula. We don't want to look at that. Instead, this is more understandable approach. So with pure code, if you want

**[7:22](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=442s)** to do text operation, if you want to corrupt the text on purpose, there are a few ways to do that. And um u in this case, I'm rolling the dice because of horistics, it's probabilities. And I'm rolling the dice five times. One time it is mark of chain. Basically inserting random rumbling words. Another one is lemonstein edit distance. It is helps to produce realistic typos. You can tune it how severe the typo should be. There's also keyboard adjacency modeled to the querty keyboard. So uh you can model like uh when you haven't exactly pressed the key or your fat finger uh a couple of keys together. And I invented two more metrics. Uh one is sprinkle gating when you insert some random emojis or accidental punctuation and uh script injection injection. It is the case when

**[8:24](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=504s)** the next morning you look at your texts and wonder how could you even type Chinese or Arabic symbols. This one is just for fun and uh because I can tune the code. I control every variable. Here are the results. Here are the five levels of corruption. Five level of synthetic index into indexication as they call it. And you can watch it break down in front of you. And another one imple another implementation. It is the fine-tuned LM. This one becomes kind of more complex but not really because the way to do it is rather simple. You just need to have some kind of data set. Then you pick a model. The model in this case doesn't really matter. I picked Mistral 7B model. It's relatively smart, small and

**[9:23](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=563s)** easy model to work with. And uh what I did is Laura low rank adaptation. So I feed the examples. I had um sober text uncorrupted text in pairs and you do adaptation and the model learns what it needs to do by example. But here's the problem. Where do I get 22,000 drunk texts especially in pairs? because I don't I could probably gather 22,000 examples of random drunk text from the internet, but I also need uh the original text, what they actually meant. And I cheated a little bit. Remember the heristics engine? I use that to generate the examples because it's way easier to find 22,000 normal sentences on the internet and then run it through the engine and voila you have pairs and small result compar comparison on one side there is heristic approach

**[10:24](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=624s)** on another side there is LLM approach and they look different that's kind of expected But they both looks they look good they look realistic. So um heristic approach looks well believable and approach looks believable. In the third example, it's even learned what mark of chains is not algorithmically but by example some inserted also I swear promise inserted a random word but um that's why I why I was a little bit at unease. I had the synthetic data, not the real data. And um heristic approach was a little bit noisy. It's still rolling rolling a dice and sometimes um heristic approach with rules. Sometimes it produces nothing. You roll a dice and you come up with the same as it was before. Sometimes it overcorrupts into something completely unreadable. Just pure

**[11:24](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=684s)** sentence of noise. And uh turns out there is such thing as the noising we are averaging. I'm not a machine learning person. So I had to discover discover it by this example. But turns out it's no way decades at this point. But overall if one thing works the pure code works and LLM approach works then code wins right because well it's just Java. It run it can run on your old Windows XP. It can run on every potato you can imagine. And on the other side, LM you're either into beefy PC territory, you need GPU or or you're into cloud. So code should probably win. That was my thought too. But it gets more complicated than that. If we look under the hood, both are in essence uh weight tuning systems. Um the engine has 19 dials. I will show

**[12:28](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=748s)** you the whole table here. Um so it's it's a lot of stuff to tune by hand. When when you are programming it in horistic approach, you need to um ensure those probabilities exist and you you need to define what each probability is. So since it's not really a testable as I've mentioned there is no way of it is corrupted enough I actually invented a fake metric when I was trying to test that but um the perfect score on my metric was a completely unreadable sentence and even if we got 50% by my imaginary matrix of text corruption it could mean that half of the sentence is perfectly normal half of the sentence is completely garbage. So uh both are weight tuning systems. Yeah. And the difference is in code approach you tune them by hand and it is

**[13:31](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=811s)** quite fragile. In LLM you have 7 billion weights but you don't tune them by hand. That's the difference. Um and we have we approached to the trade-offs. LLM approach is more expensive to run. Code is obviously cheaper to run. But LLM approach is way more rigid. If I would like to change something, insert some some some new metrics, some new sprinkles, some new ways to corrupt the text, I would need to do retraining. It's not cheap. Depends on what you do, what what is the model, but generally it is not really cheap and takes some time. Code the other hand is quite flexible. You just open application application config tune a few a few weights and restart the application you're good to go but it is complex it is very complex I spend a lot of time a lot of evenings tuning

**[14:36](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=876s)** the code approach because when I was just shifting some probability by 0.1 I got really unpredictable results so everything just exploded and with lens it learned that way, some kind of way, and it stays the same. You can change it, but uh it is relatively easier uh to manage. I didn't put the easy slider on LM here all the way to the right because um there might be some complications in running the LLM itself. It's maybe still not that trivial, kind of easy, kind of not depends on your setup. And another trade-off is that LLM is data hungry. I needed 22,000 of examples to just make it happen. While the Java approach is just you you don't need anything. You start empty, you produce results. And I even trained the L based on those

**[15:38](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=938s)** results. And so quality is a tie. And what does each one cost you on the real project? So the heristic version is cheaper to run, gives you knobs, dials for everything, and you can step through it when it breaks. It's also might be important if you need to audit your system because it's not a black box. You have access to every intermittent point if you're developing something more useful than corrupting the text. And uh it requires zero data. You start from nothing. But the price is it is fragile to tune. And uh the dice can misfire. Sometimes you produce something, sometimes you produce nothing and sometimes it is over complicated. And the LLM gives you the output that stays reliable and even in some cases it can selfcorrect. It never in my runs it

**[16:39](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=999s)** never tipped to pure noise or um there was no cases of no result. Um but the price is it is expensive to run. You can't really debug it. um if you need to filter out uh one bad word and it need thousands of examples to exist and so here are the four questions I would ask uh before reaching for an LLM. First is can you write down what good output actually means? Not the users like it but in actual rules. If you can do that that's deterministic and uh you can use code. If no, you're starting to drift drift off into the gray zone. Second, you also need to if you need to inspect, debug or override specific behaviors. If yes, then LLM will fight you. Cold wins in this one. Third one is uh if the input space is so wide you

**[17:44](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=1064s)** will be writing if statements forever different vocabulary context register then lm probably probably will save you at least time developing and getting to some kind of result and finally the one I learned the hard way um if you can't define the appropriate range of output explicitly um not what's just good but uh what is explicitly in bounds then um if you can do that training distribution does the work for you and it's not that easily reproduced by hand and the outcome is that the cheap one surprisingly was the hard one um I built this twice for fun majority of developers doesn't have that luxury at work in real projects. There's real deadlines probably someone above your head telling opinion about whether you should should AI, how to use it and when to use it.

**[18:46](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=1126s)** uh so you don't get to overengineer on purpose but doing it once on the right problem or just any problem early enough uh it is one of the most valuable thing you can do because in this example I did it both ways but uh I still needed the regular code approach to produce the LLM one and the cheap flexible handbuilt system was the hard one to make it work um LLM just learned the behavior instead of instead of me tuning 95 parameters by hand and uh personally evaluating run after change after run after run. Um and also there is a bonus to what I did. Uh it is actually a torture for autocorrect because if you think about it, it is autocorrect's job to fix that text uh back into the normal readable one. So if any autocorrect defs are here, hit me

**[19:51](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=1191s)** up. I have 22,000 examples and more to generate on demand. questions. [applause] All right. Thank you, Arthur. We do have a couple of questions uh in the app. First, how much did it cost to run the LLM and which hardware did you use? >> For this case, I used my own hardware. Uh I'm kind of a mazist because I used AMD back and back uh before the latest update. So technically it only cost me electricity and uh it's relatively small model that I chose. So it was easier to work with. You don't need very expensive hardware to use it. Cool. Um second question, can you tune the heristic approach with an LLM? This would allow you to have a cheap but well tuned approach.

**[20:48](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=1248s)** Yes. Um yeah. So can you tune the heristic approach? >> Yes, you can tune it but uh it is very fragile. Uh you have every dial exposed so you can modify every single one and uh basically it's the same thing what LLM does under the hood while learning but it is fragile. you have to go through iterations and you have to see the actual results of every change you send of every change you make in heristics approach. So uh yeah it's fragile because it can it can explode unexpectedly. >> Cool. Um any other questions from the audience? We have um roughly 8 minutes left. So uh feel free to raise your hand. Going once, going twice. All right. This the only experiment you did? >> Yeah, I'll hand you the mic. >> Did you do some other real world

**[21:52](https://www.youtube.com/watch?v=gAjwsmSvtIM&t=1312s)** examples um with this methodology comparing code versus LLMs? >> I probably did but in way less and way less significant approaches. But um yeah, the important thing is to experiment. Cool. Anybody else? All right. Uh thanks again, Arthur. That was great. Um another round of applause for him. [applause]
