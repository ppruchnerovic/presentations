---
id: 701
title: "How One Developer Built the Back Office for 10 Million Companies"
slug: how-one-developer-built-the-back-office-for-10-million
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Strategy & Innovation"
type: "Startup Presentation"
stage: "Airstream 1"
tags: ["Design Systems", "Figma", "Software Architecture", "Startups", "UI/UX"]
speakers: ["Alija Nuredini"]
speaker_companies: ["Pistacio"]
day: 1
starts_at: 2026-07-09T11:45:00+00:00
duration_min: 5
recording_url: https://www.youtube.com/watch?v=erD447IIJ1A
video_id: erD447IIJ1A
session_page: https://app.wearedevelopers.com/events/16/session/701
transcript: true
---

# How One Developer Built the Back Office for 10 Million Companies

**Alija Nuredini (Founder and CEO — Pistacio)**

`Track: Strategy & Innovation` · `Type: Startup Presentation` · `Stage: Airstream 1`

`#Design Systems` `#Figma` `#Software Architecture` `#Startups` `#UI/UX`

[Watch the recording](https://www.youtube.com/watch?v=erD447IIJ1A) · [Session page](https://app.wearedevelopers.com/events/16/session/701)

## Abstract

EU just made time tracking legally mandatory for every employer in Europe. Nobody loves it, and most small businesses are stuck choosing between enterprise HR software they can't afford and free tools that fall apart the moment compliance is on the line. This talk is about building Pistacio, a full operations platform for companies under 200 people, as a solo engineer. I'll walk through the architecture decisions that let one person ship six production modules, how a shared foundation makes compliance structural rather than bolted on, and what it actually looks like to use AI as a force multiplier without letting the codebase turn into a mess.

## Speakers

### Alija Nuredini

*Founder and CEO — Pistacio*

Alija Nuredini is the Founder and CEO of Pistacio and DesignOps Lead at 8reasons Digital, a design agency. He built Pistacio to solve a problem he saw firsthand: service businesses juggling too many disconnected tools for time tracking, task management, expenses, and team coordination. Combining a founder's instinct with a builder's hands-on approach, he shipped a full operations platform serving real service teams. He has the scope decisions, dead ends, and lessons to prove it.

## Transcript

*975 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=erD447IIJ1A&t=0s)** Nice to be here. Um, just a quick clarification. Pistachio doesn't really mean anything. I really like pistachios and anything pistachio flavored. Therefore, the name. And I also tend to hate how companies tend to be in this startup naming phase when everything is with fi or with io and I was like, you know, pistachio sounds like a pretty reasonable name. So, let's quickly get into it what we do. So, um, I'm the only developer for pistachio. The font is not our font, sadly. I don't know why, but um, yeah. Closer? Better? Very good. Uh, so, I don't know if you if most of you know, but the EU made time tracking mandatory for every company. Doesn't matter if you're one, two, three employees, but time tracking time tracking is now completely mandatory in every country in the EU without any exceptions. No one really wanted this to be this specific, but here we are. Um, it's the law and we have to abide by it. Uh, every small business is stuck

**[1:01](https://www.youtube.com/watch?v=erD447IIJ1A&t=61s)** choosing between the big ones. So, you have SAP, you have Personio or yeah, com- apps that are used by really big companies or free tools, which are not really compliant. Let's put it that way. So, most of the free tools lack compliance in the sense of the owners, the CEOs or anyone who's doing operations has to manually make sure that it's compliant with with EU law, with GDPR as well, because that's also part of this for whatever reason. Um, yeah. Usually mid-audit something will break. Um, I built Pistachio for that. It started mostly as just time tracking, but then the more we used it internally for us, the more I realized that there's definitely more things that can be stacked upon it. Uh, it's a full operations platform for ideally companies under 200 people. More ideally, up to 50 people, because that's where it really thrives. Uh but up to 200 people is definitely very manageable. We have six modules. We

**[1:59](https://www.youtube.com/watch?v=erD447IIJ1A&t=119s)** have time tracking, we have tasks and leads, we have leave, well vacations expenses travel expenses, inventory, and CRM plus reporting. Um all of them live under the same framework. And because I tend to be very fast at developing or fixing things, not developing, um rapid update cycles are almost a guarantee. Um six modules are not six different apps, which is what I found the hard way. Uh we were using not six, but we're using four different apps plus spreadsheets plus emails for six things that should have been in the same place. So, the shared foundation for this is identity, uh permissions, audit trails, and exports. So, everything is linked to this. Uh and then the modules are stacked on top. So, you have uh I have the same modules that I that I mentioned before are all interconnected with the shared foundation, but also with each other. Um Compliance for me was an architecture decision, really. It started from the

**[2:56](https://www.youtube.com/watch?v=erD447IIJ1A&t=176s)** fact that it's now mandatory. And then once it was an architecture decision, I stopped seeing it as a feature. Everything that was that is in the app currently has to be compliant with EU laws, which are very specific. Uh yeah, and if if audit grade is structural, you are always ready to ship. On day one, you are ready to stand up to like to audits and be like, "Yeah, it's there." Um then definitely gave me speed. A, I made developing this significantly easier than I would have had to do it like six, seven years ago. Uh but it definitely my judgment and in general um the entire idea behind the product was what keep what kept it from turning into slop. So, it's really lean, it's really fast. And um now, especially, speed is not the constraint anymore. It's mostly the discipline to stay clean in how we build it and to stay clean in what we actually add new to the app to make sure that we

**[3:57](https://www.youtube.com/watch?v=erD447IIJ1A&t=237s)** don't diverge too far from what a small team would need instead of hiring someone to do operations full time. Yeah, and the design system really beats handcrafted screens. I know a lot of you have heard maybe some of you have done it something in cloud code or cloud design or lovable or any other vibe coding tool. I loved it in the beginning but then the more the more we grew the more the application grew by itself the more I realized that the design system is what's keeping together because no matter how much how many new things I liked to add to the tool because of the constraints that I had set with our design system it was always relatively on brand with just a a lot less tweaks than before. And all of the modules share the exact same library so nothing is there are no other dependencies on external libraries. Then the go to market is it's the law. There's no better there's no better

**[4:57](https://www.youtube.com/watch?v=erD447IIJ1A&t=297s)** reason to go to market when it becomes mandatory. Am I out of time? >> Yes. >> Sorry wow. >> 5 minutes it's the law that's a perfect ending for that. Thank you so much. So we have time for a couple questions. A one question from me to you. You're the founder of Pistachio. Do you ever dream about Pistachio? >> Yes. If you like pistachios come to our booth at the startups we have pistachio chocolates pistachios in general. >> Do [snorts] you log that time that you're dreaming about Pistachio in Pistachio? >> I have a separate workspace for that. >> Okay perfect. >> [laughter] >> So we have time. Give him a huge round of applause. >> Thank you. Thank you.
