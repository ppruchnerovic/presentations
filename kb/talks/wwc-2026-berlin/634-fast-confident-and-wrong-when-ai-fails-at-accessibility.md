---
id: 634
title: "Fast, Confident, and Wrong: When AI Fails at Accessibility"
slug: fast-confident-and-wrong-when-ai-fails-at-accessibility
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Lightning Talk"
stage: "Airstream 2"
tags: ["Accessibility", "AI Coding Assistants", "Testing", "Web Accessibility"]
speakers: ["Radostina (Ina) Tsvetkova"]
speaker_companies: ["NAV"]
day: 1
starts_at: 2026-07-09T09:10:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=IbSFnFhuLkQ
video_id: IbSFnFhuLkQ
session_page: https://app.wearedevelopers.com/events/16/session/634
transcript: true
---

# Fast, Confident, and Wrong: When AI Fails at Accessibility

**Radostina (Ina) Tsvetkova (Senior Advisor — NAV)**

`Track: Frontend, Web & Mobile` · `Type: Lightning Talk` · `Stage: Airstream 2`

`#Accessibility` `#AI Coding Assistants` `#Testing` `#Web Accessibility`

[Watch the recording](https://www.youtube.com/watch?v=IbSFnFhuLkQ) · [Session page](https://app.wearedevelopers.com/events/16/session/634)

## Abstract

You ask your AI assistant to fix an accessibility issue. It gives you code that looks perfect, runs without errors, and even cites WCAG success criteria. And you trust it. Why wouldn't you? It sounds so certain. You ship it. Then your QA team reports that keyboard users are now trapped in your navigation menu.

This lightning talk exposes the three most dangerous ways AI fails at accessibility work and shows developers how to build verification workflows that catch these failures before they reach production.

Attendees will learn why AI confidently invents WCAG success criteria that don't exist, how seemingly correct fixes can break assistive technology, and why verification is not optional when AI touches accessibility code.

AI is a productivity multiplier for developers who already understand accessibility fundamentals, it is not a replacement for learning them.
AI will help you move fast, but only verification keeps you from breaking accessibility. Trust, but verify!
And know exactly what to verify.

## Speakers

### Radostina (Ina) Tsvetkova

*Senior Advisor — NAV*

Radostina (Ina) Tsvetkova was recognized as one of Norway's top 50 Women in Tech in 2026. She is a Senior Advisor in Digital Accessibility and Inclusive Design at the Norwegian Directorate of Labour and Welfare (NAV). She is an Invited Expert in the W3C Accessibility Guidelines Working Group, a PhD candidate in Computer Science, a Certified Professional in Web Accessibility (CPWA), a DHS Trusted Tester, and an ISTQB Advanced Level Test Manager and Test Analyst.

Ina provides guidance on digital accessibility throughout the product development lifecycle, from early planning and design through development, testing, and procurement. She has participated in the development of two Norwegian standards on accessibility in procurement and accessibility in the workplace, as well as the European standard “Accessible Systems for Living Independently.”

Ina is a passionate advocate for an accessible and inclusive world for all, regardless of ability.

She has presented at conferences including Agile Testing Days 2025, a11yCamp 2025, a11yTO 2025, M-Enabling 2025, BdKCSE 2025, Social Media Days 2025, Web4All 2025, EuroSTAR 2024, Odin 2023, and Mangfold i Mai (Diversity in May) 2023 and 2025.

## Transcript

*1,114 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=0s)** Now okay. Uh thank you for being here. So, my presentation is about fast, confident, and wrong when AI fails at accessibility. And uh I have only 10 minutes, so I will just say that I work as a senior advisor in digital accessibility in Norwegian Directorate of Labor and Welfare. And this year I was recognized as one of the top 50 tech women in Norway. So, uh back to the presentation. But before we start, do you know what an accessibility digital product is? Um it's a digital product that could be usable in an easy and effective way by as many people as possible and including

**[1:03](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=63s)** those with disabilities. And why do we need accessible digital products? Because they're essential for creating an inclusive society where everyone can participate and has equal access to information, services, and opportunities. And I hope that you have heard about the WCAG. It's uh Web Content Accessibility Guidelines and they are published by the W3C. Uh they're standard and these guidelines explain how to make web content more accessible to people with disabilities. And a lot of countries have adopted these guidelines into their laws and regulations aiming to create inclusive digital society. And also another thing that we will mention after in in the presentation is area. It's

**[2:06](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=126s)** accessible rich internet application. It's also developed by W3C and is a set of rules and attributes that define ways to make web content and web applications more accessible to people with accessibility, especially those developed with JavaScript. And here the story. You ask your AI assistant to fix an accessibility issue. And it gives you code that looks perfect. Runs without errors and even sites one of these the weak access criteria. And you trusted it. It sounds so certain, specific, and confident. Of course you did. Why wouldn't you? And you accept the change. And here then it comes, the trap. Probably your QA team reports that keyboard users are now trapped into into your login or navigation menu. They can tap in but can't tap out.

**[3:20](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=200s)** And you know, you didn't have you didn't had any errors. Actually, all checks were passed. So, I can give you five key take takeaways from this presentation. First, AI could hallucinate these the weak access success criteria. Yes, the models are better now than it they were before, but it's always good to verify citations again official W3C documentation. AI fixes could create new accessibility problems. So, that's why it's important to test the full interaction, not just isolated issue. And um What Aim Uh they produced a report every year. It's a non-profit organization. So, they they produced a WebAIM Million, a report

**[4:21](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=261s)** on the accessibility of the top 1 million homepages. And according to this report this year, 95.9% of these homepages had detected WCAG 2.0 failures. And these numbers actually increased um from 94.8% from 2025. So, you know why? Because of the AI. Because the models that we are using, they are trained on this data, which is 95% inaccessible. And some of the more common failures that we can AI could create, and these failures actually can pass the automation checks. Because with automation, if you use automation tool, you can catch around 30-40% for the other things you need to do a manual testing. So, here I I list

**[5:25](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=325s)** It will be 10 different issues that probably could come into the code. So, div, spans, or other non-interactive elements with onclick handles um could be could be used instead of native button or a elements. And it's very common It's very common error. Um also, AI could add area attributes redundantly, incorrectly, or in way that conflict with native semantics. Also, we can get form inputs without labels, icon buttons without text alternatives, and landmarks without distinguishing names. We can also get unaccessible custom form controls, but without uh, without keyboard interaction, area roles, or state management. We can get components that handle mouse events, but does not add key- keyboard

**[6:30](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=390s)** equivalents. Another five, modal dialogues, expandable panels, and single page navigation that change the visual state of the page without moving keyboard focus to the new content. Also, form validation that displays error messages visually, but does not programmatically associate them with their fields. Unaccessible modal dialogues without a correct area role, without an accessible name, without focus trapping, and without an escape key handle. Also, UI components where meaning is communicated communicated exclusively through color. And also, unaccessible dynamic contact content updates. So, the third thing based on these common failures is we can, um, skip the verification, skip verification compounds into organizational debt. So,

**[7:31](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=451s)** if you if you have one of these components, um, in in one in one component that can be reused in several places, you actually create organizational debt. And the fourth one, AI multiplies expertise. It doesn't replace it. And this is my core message. AI is a productively multiplier for developers who already understand accessibility fundamentals. It is not replacement for learning them. Because without this fundamental knowledge, um you cannot evaluate whether you uh whether AI's output is correct. You cannot tell if the area row is misapplied. So use um So, you need foundational knowledge of accessibility principles to evaluate whether this AI-generated code is

**[8:33](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=513s)** correct. And expertise in accessibility and AI can give faster and better outcomes. But gaps in expertise and AI could give faster code, but bigger mistakes. So, fast, confident, and wrong. And the cost of being wrong in accessibility is exclusion. And it's about real users who cannot access your product. And more than 1 billion people have some sort of disabilities. And this is about the permanent one. Because we can also have temporary, like if you broke your uh hand, or situational, if you're holding a baby and you cannot use your hand um uh to to to to use the product. So, in this

**[9:35](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=575s)** case, verification is not optional when AI touches accessibility. Because accessibility is a civil and human right. And from fast, confident, and wrong, we need fast, verified, and accessible. So, AI will help you move fast, write code fast, but only verification keeps you from creating an exclusion. And the last one, trust, but verify, and know exactly what to verify. Thank you. >> [applause] >> And I hope I nearly managed with the time. And do you If you have any questions, please come find me. I'm really happy to to talk about accessibility. Thank you. >> Cool. Thank you. You managed time perfectly fine. Um a last round of

**[10:39](https://www.youtube.com/watch?v=IbSFnFhuLkQ&t=639s)** applause for Ina. Thank you. >> [applause]
