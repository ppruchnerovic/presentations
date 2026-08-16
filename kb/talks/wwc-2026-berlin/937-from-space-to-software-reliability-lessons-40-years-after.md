---
id: 937
title: "From Space to Software: Reliability Lessons 40 Years After Challenger"
slug: from-space-to-software-reliability-lessons-40-years-after
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Quality & Reliability"
type: "Lightning Talk"
stage: "Airstream 1"
tags: ["Developer Experience (DevEx)", "DevOps", "DevSecOps", "IBM", "Integration Testing", "People & Culture", "Reliability", "Site Reliability Engineering (SRE)"]
speakers: ["Robert Barron"]
speaker_companies: ["IBM"]
day: 2
starts_at: 2026-07-10T11:20:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=jSyv-XTGoK8
video_id: jSyv-XTGoK8
session_page: https://app.wearedevelopers.com/events/16/session/937
transcript: true
---

# From Space to Software: Reliability Lessons 40 Years After Challenger

**Robert Barron (SRE Architect — IBM)**

`Track: Quality & Reliability` · `Type: Lightning Talk` · `Stage: Airstream 1`

`#Developer Experience (DevEx)` `#DevOps` `#DevSecOps` `#IBM` `#Integration Testing` `#People & Culture` `#Reliability` `#Site Reliability Engineering (SRE)`

[Watch the recording](https://www.youtube.com/watch?v=jSyv-XTGoK8) · [Session page](https://app.wearedevelopers.com/events/16/session/937)

## Abstract

The Space Shuttle Challenger disaster is often explained as a technical failure, but the engineers knew something was wrong before launch. What failed was not their expertise - it was the system of decisions, incentives, and escalation paths that surrounded them.
This talk reframes Challenger as a leadership and management case study, highly relevant to today’s engineering managers. Modern software organizations operate systems that are fast-moving, distributed, and business‑critical, under constant pressure to deliver. In those conditions, reliability rarely fails because of a missing alert or a bad design - it fails because risk becomes normalized, concerns stop escalating, and “acceptable” tradeoffs quietly stack up.
By drawing deliberate parallels between NASA’s launch decisions and contemporary software organizations, this session examines how management structures, delivery metrics, and cultural signals shape technical outcomes. Attendees will explore how well‑intentioned decisions (schedule pressure, ownership ambiguity, optimistic reporting) create environments where teams do the “right thing” locally while producing system‑level failure.
The core argument is simple: reliability is not owned by operations or enforced by tooling. It is a leadership responsibility, expressed through priorities, incentives, and how managers act when tradeoffs appear.

## Speakers

### Robert Barron

*SRE Architect — IBM*

Robert works for IBM, helping clients improve their IT Operations. He is an SRE and AIOps evangelist who enjoys helping others solve problems even more than he enjoys solving them himself. Robert has over 20 years of experience in IT development & operations and is happiest when learning something new. He lives in Israel with his wonderful wife and two children. His hobbies include history, space exploration, and bird photography.

## Transcript

*1,547 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=jSyv-XTGoK8&t=0s)** Hello everyone. Thank you for being here. I'm very happy to be here with you at We Are Developers. This is my first time here. I'm very excited. I'm also excited to share with you one of my passions, which is space exploration. And in my day job at IBM, I am responsible for the reliability of the internal platforms at IBM. And I like to take lessons from what we can learn in how we got to space. And we can take these lessons for our modern-day IT operations and development. Sometimes these are lessons of what to do. Today, unfortunately, we're going to be talking about the Challenger disaster from 40 years ago, something about what not to do. And just for those of you who don't know, to remind you, Challenger was launched in January of 1986. A very successful launch. All the

**[0:58](https://www.youtube.com/watch?v=jSyv-XTGoK8&t=58s)** operations were successful. All the metrics were green. All the KPIs were successful. And suddenly, 73 seconds after launch, Challenger disintegrated. Why did this happen? Let's do a little bit of background to the space shuttle. Comparing the space shuttle or flying to space with the airplane shows that they are very different. 30 years after the first flight, we already had airliners. Flight was something natural. Flight was something that everyone was doing. 20 years after the face first flight into space, it was still primitive and it was still uh experimental. In 1953, 50 years after the first flight, 50 million people had already flown. Whereas in 1981, the space shuttle constantly became something that was difficult to operate. One of the things I'm proud about as an IBMer is IBM's rich history in space exploration. I have here a medallion that was minted by IBM and given to all IBMers who worked on the space program. It's operational, it says there. The

**[2:03](https://www.youtube.com/watch?v=jSyv-XTGoK8&t=123s)** declaration that the space shuttle was no longer in an experimental way of going to space, but a standard way, a safe way of going to space, little different between an airline. But the reality is that the shuttle was never standard. It was never simple, it was never easily deployed if we take it into uh into what we do in development. The first non-astronaut, the first regular person who was supposed to fly into space was a teacher, a high school social sciences teacher, and she was scheduled for July of 1985. But the flight was delayed. And the flight was delayed. And the flight was delayed. Now, if you take an airline and it tells you that you're scheduled for 1985, but you actually launch in 1986, you're going to say, "This is no good. I don't want this." There was a lot of pressure on NASA to fulfill the promise of the space shuttle, that spaceflight would be simple, would be easy, would be cheap,

**[3:10](https://www.youtube.com/watch?v=jSyv-XTGoK8&t=190s)** would be a commodity. And finally, January 1928, the space shuttle launched. By coincidence, it was the coldest launch ever for the space shuttle. It was just above 0° C, just above freezing. And because of that, 73 seconds after launch, the shuttle exploded. Now, why did the shuttle explode? Didn't they know that they couldn't launch when it was too cold? And why do they care about the temperature in any case? Well, if we look at the telemetry that came from the at the telemetry coming out, you can see a small spark coming out the side of the space shuttle. A small amount of hot gas escapes and reaches the fuel tank causing the explosion. What happened? We have it's called an O-ring. If you look at this pipe that's part of the rocket that helped launch the space shuttle, there's a rubber ring inside. The role of the rubber ring is to expand and contract as the shuttle flies. And if it can't do

**[4:17](https://www.youtube.com/watch?v=jSyv-XTGoK8&t=257s)** that, if it's frozen solid and can't move, that means that it's not keeping the seal and the gas is escaping. And that's what happened. The O-ring froze, the gas escaped, and it exploded. Now, the question is, this was not the first flight of the shuttle. We've already said the shuttle is operational. We know how to fly it. So, why did they make this mistake? Well, the engineers did complain. They did say, "We're flying at a too cold a temperature. We're not having tested this. We're not ready. We don't know what's going to happen. This is outside parameters." But then management said, "Well, show us the evidence." And they showed the evidence, and you can see in this graph that basically when the temperature is low, there's damage to O-rings. This is from previous flights. This is our previous experience. This is our previous tests. But, the engineers couldn't explain, for example, why we also have damage when

**[5:22](https://www.youtube.com/watch?v=jSyv-XTGoK8&t=322s)** the temperature is high. So, the managers go back and say, "Well, you haven't proved that low temperatures cause damage. You've just shown that there is damage sometimes, and it doesn't look like it depends on the temperature. So, we're going to fly anyway because you haven't shown us that there's a problem." Now, this isn't really the way to do it. You shouldn't be proving that there You be proving that it's safe, not having to prove that it's not safe. The other thing is these are only the flights that had damage. If we take more KPIs, more metrics from the flights that had no damage, we can suddenly see that the anomaly is not the cold temperature, but the anomaly is the damage at the high temperature. And if we take this new graph with all the data and not just the data that they

**[6:20](https://www.youtube.com/watch?v=jSyv-XTGoK8&t=380s)** originally connected and we extrapolate it to the real temperature of the launch, now we can see evidence of what the problem would be. So, this is what's called normalization of deviance. The shuttle had problems. It always had problems, but they got used to the problems. And when they decided that these problems were too severe, they could no longer explain why suddenly this little problem is actually a major problem. Because near misses get reclassified into business as usual. And I'm sure you all know from your own experience cases where you have near misses in production, but then you can't justify getting that into a change that will that will prevent the future problems. If we compare normalization of deviance for the Challenger, O-ring erosion can be AI code that no one fully understands. Launch pressure is ship faster. We've got deadlines. And we got it right last week, so why now would the AI suddenly decide to have

**[7:25](https://www.youtube.com/watch?v=jSyv-XTGoK8&t=445s)** bad code? And we've got all our tests in a row. We've got our tests, so why why now when it's green do we suddenly suspect? The fact that the engineer is suspicious is less important than the fact that all the test suite go goes through because that's something that can be easily easily measured. I'm going to contrast this a little bit with the planes and the space shuttle and computers. I'm very proud to be part of IBM where we've got a 115-year record of changing the way computers work and computers have become more and more of a commodity, more precise, faster, safer, and so on. The IBM computers were part were on the shuttle. Five computers working in parallel with redundancy. But a perfect computer which had no problems isn't enough to prevent disaster. The computer was fine. It said that everything was working, but reality is stronger than software. And reliability has to be part of our

**[8:30](https://www.youtube.com/watch?v=jSyv-XTGoK8&t=510s)** culture. We can't say the developer has to develop something reliable. We can't say that the SRE is responsible for reliability of the system. It has to be what happens when there are trade-offs, when there are priorities that we have to balance. What happens then? What happens when someone raises a signal, I can't deploy this safely. I know that there's a problem. How is that accepted in the culture of the organization? In NASA's case, it was not accepted. In our case, it should be accepted. So, we're flying a shuttle. It's not a shuttle like this, but it is our software shuttle. And you need to be careful that you don't fall into the problem of normalization of deviance yourselves, that the schedule pressure will override the concerns of your engineers. Look at safety, not avoid something going wrong, but safety is make sure that nothing can go wrong and everything goes right. So, you're going to have a lot of problems.

**[9:35](https://www.youtube.com/watch?v=jSyv-XTGoK8&t=575s)** It's going to be software. No one here, I presume, is working on the shuttle. But you have to make sure that the leaders know how to make the right decisions. You can build nearly flawless software. AI is not the magic bullet. Leadership is the magic bullet. So, thank you very much. If you like this, I have more articles, more contacts. This is a thank you from NASA to IBM after the second shuttle launch. This is one of my prized possessions, signed by the astronauts. And thank you very much for being here on my talk.
