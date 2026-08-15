---
id: 605
title: "One Color to Rule Them All: Relative CSS Colors in Practice"
slug: one-color-to-rule-them-all-relative-css-colors-in-practice
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Lightning Talk"
stage: "Airstream 2"
tags: ["CSS", "Design Systems", "HTML", "Storybook", "UI/UX"]
speakers: ["Mert Akça"]
speaker_companies: ["SAP"]
day: 1
starts_at: 2026-07-09T08:25:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=HyKX9Yi8gQY
video_id: HyKX9Yi8gQY
session_page: https://app.wearedevelopers.com/events/16/session/605
transcript: true
---

# One Color to Rule Them All: Relative CSS Colors in Practice

**Mert Akça (Software Engineer — SAP)**

`Track: Frontend, Web & Mobile` · `Type: Lightning Talk` · `Stage: Airstream 2`

`#CSS` `#Design Systems` `#HTML` `#Storybook` `#UI/UX`

[Watch the recording](https://www.youtube.com/watch?v=HyKX9Yi8gQY) · [Session page](https://app.wearedevelopers.com/events/16/session/605)

## Abstract

Choosing separate colors for text, borders, hover states, active states, and backgrounds is one of the most repetitive—and unnecessary—parts of frontend work. Every new component means another round of “What should the hover color be?” or “Can design give us a darker shade?” Modern CSS gives us a better way.

In this talk, we’ll explore how relative CSS colors let you generate an entire color system from a single base value. Using color-mix(), OKLCH, and custom properties, you can derive hover, active, border, and subtle background colors automatically.

I'll walk through an example of building a fully interactive button with just one color token, then generating all its states directly in CSS. You’ll see how this approach improves consistency, simplifies theming, and dramatically speeds up collaboration between design and engineering.

You’ll leave with practical patterns you can drop into your design system today—and a new way of thinking about color on the web.

## Speakers

### Mert Akça

*Software Engineer — SAP*

Hi, I’m Mert! I’m a Software Engineer based in Berlin. I’m a "user-driven" engineer at heart, which means I care just as much about the human at the other end of the screen as I do about clean, type-safe code.

Whether I’m closely working with other engineers or designers, my goal is always the same: making the experience faster, more inclusive, and a little more fun. Beyond the day job, I love writing about tech—from deep dives into designs to the joys of programming—and I built a browser-based mystery game to explore the limits of interactive storytelling. I'm a big believer in "learning by doing" and love a good live-coding challenge!

## Transcript

*1,096 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=HyKX9Yi8gQY&t=0s)** Uh welcome. So, first of all, you could have gone another AI workshop. So, you chose to actually see a CSS topic in 2026. I appreciate it. Uh it is a simple topic, so I will cut half of my jokes and just go into the topic. Is it here? Yeah. So, what are the CSS colors? We have different types of CSS colors, which is RGB, you may have known, hex, and ACA HSL, and there is the new guy, OK uh OKLCH, which I would love to explain the difference between HSL, but it is basically the same, but algorithm is more developed for human eye by HSL is more on color theory. So, I will use OKLCH LCH when I was talking about the relative colors. And And what are the relative colors? They

**[1:07](https://www.youtube.com/watch?v=HyKX9Yi8gQY&t=67s)** are developed around 2024, and it is supported by 85% of the computers/browsers. So, the structure is like you write from your base color, then the channel inputs, and if you like, you can change the opacity. And you can use every color function in your base color, and it helps you to generate a color from another color instead of just writing from scratch. Uh for example, I picked a red color, and in the second card I reduce the lightness by 10% just set that L minus 0.51 10% less lightness and I make the half of the chroma so it is less vivid and I change the hue can I go back? Here. Here. Off. Off. It doesn't go back? Yeah, this one. So the hue is this color wheel which

**[2:14](https://www.youtube.com/watch?v=HyKX9Yi8gQY&t=134s)** from 0 to 360 it says the degrees. So you can change the actual colors by uh just changing the base color like plus 100 then it red becomes blue. And how does it help us? So we have design systems and design systems are built with thinking of scalability, consistency and maintainability and our design system components have a lot of components. These components have different variations, different states and different elements inside and our design system have different teams. That means a lot of color per component and per design system. For example, this snack bar has background, icon, text color our buttons have more depending on the team. It has different background colors text when when you hover different color, when it is active different color, when it is disabled different color

**[3:20](https://www.youtube.com/watch?v=HyKX9Yi8gQY&t=200s)** and we used to do it if it is blue, color this, color this, color this, border color, background color, text color, icon color. Just you set a lot of colors and if it changes, you change everything. When you add something, you need to check if you think about accessibility if the contrast is good enough for people to see or uh it is actually clear that when you hover, it is active. Uh I can't I will I cannot right now open the link, but let's go through verbally. So, instead of using normal way, you can use the relative colors when you implement buttons. What you need to do in the base class, you set for example, the background and you say my border is 20% darker than background, my text color is 80% contrast with

**[4:29](https://www.youtube.com/watch?v=HyKX9Yi8gQY&t=269s)** background, my hover is 20% lighter, when it is clicked, let's do 40% lighter. When it is disabled, just reduce the opacity based on the background color, which I picked as a base color. And when you need to add another variant, what you need to do is okay, this is my new and it is now red and all of the elements of this component will generate it automatically instead of setting everything from scratch. For example, your designer came to you say, "Oh my god, we are doing a design re- migration and now instead of darker, when you hover a button, it is lighter." And you need to change every color from the if you implement it uh the normal way, but instead, you can just change the base style from 20% darker to 20 20% lighter and that's it.

**[5:40](https://www.youtube.com/watch?v=HyKX9Yi8gQY&t=340s)** You just changed the whole design system. Uh so, what is the point? So, if your platform allows users to customize teams, like I don't know, Jira or Slack, maybe, and you they can just choose a brand their brand color or their base color, and you can generate all the remaining colors by yourself, instead of letting them control every single one. And you can easily extend your design system, change the exist existing elements, like snack bars, buttons, cards, not only with the design system, but you can also change your pages depending on the team, dark team, light team, super space team, whatever you like. And Oh no. Yeah. Thank you. And also, you don't need to think about if you are think if you are care about accessibility, you

**[6:46](https://www.youtube.com/watch?v=HyKX9Yi8gQY&t=406s)** don't need to think about contrast or other accessibility elements that is depending on color every time. When you set the rule that I want my text enough color, enough contrast in comparison to background, you just set the rule in the base, and then if the users change the color, if you add the another variant, it doesn't matter anymore. Your contrast always stays the same and compatible, whatever accessibility rule you have. And And Yeah. So, I said, maybe I didn't say that, but it it is a practical presentation. So, what to do? So, you can clap and cheer for this amazing topic in the age of AI at the end. And run to your designers, present this idea to them, check the support because it is important. Not everything in CSS you can just

**[7:54](https://www.youtube.com/watch?v=HyKX9Yi8gQY&t=474s)** uh implement immediately because it will crash in old browsers. Uh instead of agreeing every single color, just agree on the rules, like how dark you want, how light, how vivid you want your uh elements, the small property colors, instead of just setting colors everywhere. And if there is one single variant that doesn't meet the expectation and you need to override manually and you're ashamed to go to your designer again, hey this relative topic doesn't work. I let's change back, but you can't. Then it is CSS for you. It is always be exceptions unfortunately. And yeah. And that's it. If you want to if you want the slide or the link that is in the slide or have any questions you can find me after presentation. And thank you so much for coming.
