---
id: 660
title: "Code Style in Practice: Balancing Preferences and Consistency"
slug: code-style-in-practice-balancing-preferences-and-consistency
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Developer Experience"
type: "Lightning Talk"
stage: "Airstream 1"
tags: ["Clean Code", "Developer Experience (DevEx)", "Legacy", "Motivation", "People & Culture"]
speakers: ["Angelika Shvets"]
speaker_companies: ["Global-e"]
day: 1
starts_at: 2026-07-09T10:10:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=RwSfrCDMdqo
video_id: RwSfrCDMdqo
session_page: https://app.wearedevelopers.com/events/16/session/660
transcript: true
---

# Code Style in Practice: Balancing Preferences and Consistency

**Angelika Shvets (Senior Software Engineer — Global-e)**

`Track: Developer Experience` · `Type: Lightning Talk` · `Stage: Airstream 1`

`#Clean Code` `#Developer Experience (DevEx)` `#Legacy` `#Motivation` `#People & Culture`

[Watch the recording](https://www.youtube.com/watch?v=RwSfrCDMdqo) · [Session page](https://app.wearedevelopers.com/events/16/session/660)

## Abstract

How often do we work with code where similar parts look different and are difficult to understand? The reasons are not always clear and are often related to personal preferences, missing standards, or historical decisions.

In this talk, we will discuss:
Is it better to follow an exciting coding style rather than introduce your own?
When and how is it appropriate to improve or change code style?
Can principles be used when formal standards do not exist?
How do code style and consistency impact readability, maintainability, and overall code quality?

This talk focuses on balancing personal preferences with shared team consistency and on making software projects easier and more enjoyable to work with.

## Speakers

### Angelika Shvets

*Senior Software Engineer — Global-e*

Angelika Shvets, a software developer based in Israel.
I've been in the IT industry since 2004.
Over the last 7 years, my work has primarily involved software development, encompassing research, implementation, integration, and testing of systems of varying complexity.
Prior to my current role, I spent 8 years as a full-stack web application developer.
In the early stages of my career, I gained a solid foundation with 5 years of experience as a system administrator.
I also served as a system administrator in the military.
I hold a Masters in Mathematics and Computer Engineering.

## Transcript

*1,308 words · source: yt (en)*

**[0:02](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=2s)** Hi everyone. My name is Angelika Schwetz. I'm a software engineer and I have been working in the IT industry for over 20 years. During my time, I have worked with different technologies, teams, and code bases from startups to large companies. I have built new projects from scratch and work on legacy systems. Today, [gasps] we have more ways than ever to create code. We can write it ourselves, reuse existing solution, or use AI tools. But no matter where the code comes from, we are still responsible for its quality. Writing new code is enjoyable, but most of our work is reading and changing existing systems. And what if the system is a legacy

**[0:51](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=51s)** monolith with years of history? Where is the line between improving the code and simply rewriting it in our own style? Today, I would like to talk about consistency, personal preferences, and how to find the right balance between them. So, let's start. And it's not work Oh. A few years ago, I had an interview with a company where is the interviewer was a big fan on linkin.net. For him, good code meant a compact code. Most of the interview focused on how well I could write link expressions. Please take a look at this at this example. It's compact, elegant, and in many situations, it's exactly the right solution. Now, please look at the

**[1:39](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=99s)** alternative implementation. It's [clears throat] longer, less expressive, and nobody wins programming competitions with code like this. >> [gasps] >> But what happened if you need to investigate production issue under time pressure and you have never seen this code before and you don't have tokens, I don't know. >> [snorts] >> Which implementation would you prefer to debug? I'm sorry. Sorry. Sorry. I'm sorry. Technical issues. Yes, unexpected situations. I'm I'm not saying that compact code is wrong code. But many In many situations, it's exactly right

**[2:27](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=147s)** choice. But code written once is edited, reviewed, debugged, and maintained many times. That's why readability is more often valuable than compactness. Let me Sorry. Let me share another example. Thank you. Um So time sometime sometime ago, my tech lead and I were reviewing a pull request. And we found that the property was being used in this in system, but we couldn't understand where the value comes from. We expected to find something like this. A simple property assignment. Instead of this >> [clears throat] >> I after some investigation, we discovered that another team was

**[3:16](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=196s)** populating the property using the reflection. The code worked correctly. There was no bug, but we wasted [clears throat] more time understanding the code than solving our task. Working code is not always understandable code. When behavior is hidden, every developer who work with the code pay later the price. Let me share one final example. During a code review, I saw change in the builder. Sorry. The builder already delegate all related logic to helper. With a new requirement the developer added new logic to directly to the builder. The code worked correctly, but now related logic to a

**[4:04](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=244s)** splitter between two different places. I think this would have been more consistent approach. The builder stays focused on building and helper keeps all the related logic. The behavior stays the same, but but design stays consistent. This example isn't really about builders or helpers. It's about respecting the existing design. Next one, it's refactoring. Most developers like refactoring, I definitely do. When we see code that we would write differently, the first instinct is often to improve it. And sometimes that's exactly the right thing to do. In my experience, I have noticed that

**[4:51](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=291s)** not every refactoring adds value. I have learned to stop and ask myself one simple question. Am I solving the real problem or I am just following my preferences? Because those are not always the same thing. If the refactoring improves readability, reduce complexity, removes duplication, or make debugger easier, it's probably adds value. But if the result that the code that looks like my own work, I'm not really improving the system and only changing it. And every change has a cost. It [snorts] increases the pull request size. It makes the review harder and it increase the risk of introducing new bugs. And it becomes more difficult to

**[5:37](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=337s)** understand what actually changed. My sorry. Good refactoring isn't about changing code. It's about improving it. The next one, let's talk about code reviews. How many of you have seen Sorry. Comments like this. Most programming problems have more than one valid solution. Code review is great opportunity to see different perspectives, but different doesn't automatically mean wrong. And the question is does the current implementation create What's happened here? I'm sorry. Doesn't Does the current implementation create a

**[6:29](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=389s)** real problem or it's simply different way from what would would write it? That's why I try to separate personal preferences from objective concerns. Every comment on the right side explains the problem, not the preferred solution. And whenever possible, I preferred asking questions instead of giving instructions. The goal of the code review isn't to prove that one solution is better. It's goal to help all team maintain consistent and understandable code. After all these examples, I would like to come back to the topic I mentioned in the beginning. It's consistency. When we hear consistency, we usually think about formatting, naming

**[7:17](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=437s)** conventions, or coding style. Those things are important, but consistency it's much more than that. It's about understanding the existing design before making changes. Following the patterns that already exist instead of introducing new ones. Keeping related logic together. And it's about making decisions that help to the whole team maintains the code that just not just ourselves. And opposite is also also true. When the related logic is scattered, when we make unnecessary architectural changes, or when the we change code simply because we prefer different style, a code base become become less consistent. And consistency doesn't mean that every

**[8:05](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=485s)** piece of code looks like exactly the same. It means that the code is predictable. So, many next developer can understand and work with with it more easily. One question I often hear is that if what if there are no standards? Not every team has coding guidelines. Sometimes standards exist, but nobody follows them. In those situation, we usually there usually isn't one perfect perfect answer. Over the years, I have found that a few simple principles help me to make better decision. None of them is new, and most of us already know them. The challenge is remembering them in our everyday

**[8:55](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=535s)** work. If the result is the code that easier to understand, it easier to change, and easier to maintain. The principle the principle those principle won't answer every question, but it can help create consistency even formal standards don't exist. And to summarize, there isn't one perfect coding style. At the beginning, I ask where is the where is the where is the line between improving the code and simply rewriting it in our own style. For me, it's simple answer is simple. >> [snorts] >> Improve the code to the next developer, and not your for your own preferences. Martin Fowler described refactoring as improving the internal structure of code

**[9:44](https://www.youtube.com/watch?v=RwSfrCDMdqo&t=584s)** without changing external behavior. I think it's important word, it's improving and not changing. And Boy Scout rule, it's remind us to leave code a little better that we found it. Thank you very much. Technology will continue to change and AI will continue change how we will write code, but someone will need to read it, review it, debug it, and maintain it. If our change makes the person's job easier, we probably made the right decision. Thank you for your attention and patience. Thank you.
