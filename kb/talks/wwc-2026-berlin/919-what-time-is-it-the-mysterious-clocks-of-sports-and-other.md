---
id: 919
title: "What time is it? The mysterious clocks of sports and other things we do."
slug: what-time-is-it-the-mysterious-clocks-of-sports-and-other
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Data & Databases"
type: "Lightning Talk"
stage: "Airstream 1"
tags: ["Data", "Data Pipelines", "Data Science"]
speakers: ["Clemens Vasters"]
speaker_companies: ["Microsoft"]
day: 2
starts_at: 2026-07-10T10:20:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=959-8HEDzdc
video_id: 959-8HEDzdc
session_page: https://app.wearedevelopers.com/events/16/session/919
transcript: true
---

# What time is it? The mysterious clocks of sports and other things we do.

**Clemens Vasters (Principal Architect — Microsoft)**

`Track: Data & Databases` · `Type: Lightning Talk` · `Stage: Airstream 1`

`#Data` `#Data Pipelines` `#Data Science`

[Watch the recording](https://www.youtube.com/watch?v=959-8HEDzdc) · [Session page](https://app.wearedevelopers.com/events/16/session/919)

## Abstract

Most data analytics platforms and their temporal features make some assumptions about time and you might too. Time is what you see when you look at your watch and we use UTC timestamps.

Not so in football. Everyone knows at what minute in the match their team scored the deciding goal in a legendary match. Nobody cares what UTC clock moment that was, to the extent that it's practically impossible to find out what UTC moment that was. Also, pretty much each football match has the 45th minute twice! And if you do analysis on the match, you probably want to ignore injury periods or other occasions when the ball was out of play.

In motorsports and most other sports where it's a primary objective to "beat the clock", the clock is actually not a good x-axis for analytics since lap-to-lap times differ as a matter of principle and make data hard to compare.

In this session, we'll look at the clocks in sports and some other fields and how to make sense of them in data analytics.

## Speakers

### Clemens Vasters

*Principal Architect — Microsoft*

Clemens Vasters is Lead Architect in Microsoft’s Azure Messaging team that builds and operates a fleet of hyper-scale messaging services, including Event Grid, Service Bus, Event Hubs, Stream Analytics and Microsoft Fabric Eventstreams. Clemens represents Microsoft in messaging standardisation in OASIS (AMQP, MQTT) and CNCF (CloudEvents, xRegistry) and writes too much code for being an "Architect". He looks back at nearly 30 years in professional software development and has seen the same fashion come and go a few times.

## Transcript

*1,979 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=959-8HEDzdc&t=3s)** Hello everybody. My name is Clemens. I work for Microsoft. We don't have time for this. So, keep going. Um, I'm going to challenge your notion of time. I'm mostly about what is time in data analysis. I've done this talk for an audience of people who are not technician, not people interested in technology at all. So, now you are technology people. So, this is going to be interesting. Um, when we think about data analysis and we think about time data, time oriented data, we often use the wall clock, the clock on your wrist, um, and that time concept. And I wanted to talk about football, it's the World Cup, and I talk some other sports and how that actually ends up being super challenging to use the wall clock for

**[0:53](https://www.youtube.com/watch?v=959-8HEDzdc&t=53s)** analysis. Um, so we'll talk about time. How? Let's let's start with I want to analyze data that comes out of football game. I need to have a time for when the game starts. Nominally, this game starts at 15:30 in the afternoon. Well, turns out if you actually look at the data, it doesn't. So on time, so within really on the clock is only 9% of the games in the German Bundesliga. Um only uh 74% are within 15 seconds. So the the the the games don't start on time, which means you can't anchor any of the performance data, any of the things that you do on the wall clock.

**[1:42](https://www.youtube.com/watch?v=959-8HEDzdc&t=102s)** You need to run your own stopwatch to track the game. So now you're already decoupled from the clock. Then the clock you see on TV is not the game clock. In this example, um it's kind of hard to see. This is from the Merchin Gapa playing Cologne game uh in the last season. The clock on the TV started 7 seconds late. Um the latest I've seen so far is 18 seconds. that it started later because how is this operated? Someone is pushing a button. So the time is not synchronized with the whistle of the of the ref, but it's someone pressing a button. And as you have that in sports, especially in

**[2:30](https://www.youtube.com/watch?v=959-8HEDzdc&t=150s)** Bundesliga, there's actually numerous people who are push pushing buttons for when the data starts. Now the problem is if you want to have data that's synchronized and if you want to have you know data that's synchronized with the experience like you do overlays data overlays etc then you need to have precise alignment. One of the things that's actually kind of funny um a synchronization problem that's uh interesting. One of the things we want to do, um, by the way, I work for Microsoft and I'm also on the digital advisory board of Boris mentioning. Uh, for all you don't know, it's a football club, the best club in the world. Obviously, one of the things we do would like to do is we'd like to synchronize our own TV commentary or our radio commentary with

**[3:19](https://www.youtube.com/watch?v=959-8HEDzdc&t=199s)** TV pictures, but it's really hard because of the offset. So when you watch so for as we were um in the pre-digital age in the analog age you could listen to a football match or you can watch a football match on live TV and the delay would be 0.2 0.3 um seconds. It was instant. Now if you watch a match over the zone your delay is 25 seconds if you're lucky. and often uh 50 50 seconds. Um the fact that they're playing advertisements before a match when you look when you look at those matches kind of on your streaming service is not an

**[4:07](https://www.youtube.com/watch?v=959-8HEDzdc&t=247s)** accident because those uh ads are actually buffered on the on the machine and they're using that time when they play the play your uh the the ads to you to go and buffer the video signal. So also here in terms of time you can't rely on you know you have to understand where the data comes through you can't rely on on audio video signals and be naturally in sync you have to do synchronization work basically on all the steps data video audio all those things need to be synchronized which is super super difficult if you are trying to build an integrated experience as that exists for instance in prime competitor. Um, in Prime for the Champions League, they have a data overlay. And now Magenta in Germany also

**[4:55](https://www.youtube.com/watch?v=959-8HEDzdc&t=295s)** has a data overlay where you can go and see data out of the match being synchronized with the video. What you'll notice if you switch channels back and forth is that the data channel is lagging and it's lagging by 30 about 30 seconds because that's how much time they need to have to take the captured data and synchronize it with the video signal. So all of that is a lot of work to kind of deal with synchronization of time and of course football has its completely own world of time. This is the 43rd minute 1974 G Müller shooting the uh decisive goal in the World Cup final for Germany to become world champion. It is hard to find out but since this

**[5:47](https://www.youtube.com/watch?v=959-8HEDzdc&t=347s)** was in the first half it's half easy to find out when exactly that happened on the clock if we assume that that that match started at the sec right second of when the scheduled um uh time was now this goal Mario Guts 2014 the decisive goal against Argentina that actually happened didn't happened in the 113th second. This happened in the effectively in the 118th second because there was extra time in the first half, there was extra time in the second half. This is in the first half of the uh extra time. So, we kind of can piece together kind of when that was in match time, but when that was actually happening in real

**[6:36](https://www.youtube.com/watch?v=959-8HEDzdc&t=396s)** time on the real time clock is completely lost in history. You have to watch a video from start of the entire game including the break find one to actually find out where that was on the clock. The the time universe of football is completely decoupled from the watch. So that means that if you do data analysis in sports, you have to run your own clock. So what you do is you run an artificial match clock that has also has other um has other um nice advantages. So you create a clock that is January 1st 1970 is the first half. January 2nd 1970 is the second half. First time extra time third

**[7:24](https://www.youtube.com/watch?v=959-8HEDzdc&t=444s)** second half extra time is the fourth and the penalty shootouts happen on the fifth day. That gives you an an an artificial clock which also solves the problem that in each football game there's a 46th minute twice. one in the first half and one in the second half. So you have to go and and and split those apart. And the way you do this over multiple days. Why is it useful to do that over multiple days? Because if you do stream analytics on top of that live data that's streaming, you will have open data windows 5 minute aggregations, 15minute aggregations, one minute aggregations. And when the final whistle is at that match um or of a half, you want all those windows to close, right? You want to have all the all the stats need to go and close exactly at that moment. So

**[8:12](https://www.youtube.com/watch?v=959-8HEDzdc&t=492s)** what you do is you flip over to the next day that automatically clip clips all the windows because you now go go out of all the time windows and that automatically makes them roll over. So an artificial clock in football super useful and you still use the mechanisms that have you have the daytime time but you do not use the UTC clock you use you basically set null at the start of the event and then if you have logical breaks if you have logical segmentation in the match you will go and use this. Um, another fun thing you kind of have these timelines that you see on your sports pages or on TV where you have kind of first h first half second half and then you can have

**[9:00](https://www.youtube.com/watch?v=959-8HEDzdc&t=540s)** all these events like this is where the goal played. It's a fun thing to think about how you do pixel projection out of your out of your time scale because in football that stretches and contracts because each half has extra time which is unpredictable, right? And then the second half has that and the extra time has that. So as the game progresses, if you kind of render these these bars, you always need to kind of keep a clock system which projects out pixels into time and back where you have kind of these artificial. It's a pretty complicated calculation. Not not easy to go and build these pixel pieces. Um, in a football game there are only 58% of the time is the ball in play. 42% of

**[9:54](https://www.youtube.com/watch?v=959-8HEDzdc&t=594s)** the time in an average Bundesliga match the ball is out of play. Most less least uh um ball out of play is uh around 30% most over 50%. So you could say a little bit more than a third of the time you sit there and wait for the ball come back. Why is that significant? Because if you want to do analysis, performance analysis of players, um, and es especially when if you want to do real-time opponent analysis, it's important to understand when there's play action and when the players have time to rest because every player only has so much power in the tank. Like physiolog physiologically, um, they can only do like three sprints within 4 minutes. And you can tell, you

**[10:44](https://www.youtube.com/watch?v=959-8HEDzdc&t=644s)** can basically count that up and you can tell as an opponent, hey, that player is now needs rest. Go play around on that side if you have a clear understanding of what their physiological condition is. But before that, you need to understand when the ball is in in game and out of game. So you create a second clock, effectively a second clock model which is only for net playing time. And then sometimes the clock stops completely and when the stop clock stops completely that is when um everything breaks together as they say in German uh because that's then ultra challenging um from the perspective of you needing to have a clock system which can actually deal with interruptions.

**[11:32](https://www.youtube.com/watch?v=959-8HEDzdc&t=692s)** Finally, handball, basketball, ice. Okay, if you look at all these, none of these have a chaotic random uh system as football has. All of them have much more cleaned up, much more cleaned up time models. Um where they actually play on true time and not on random time as football does. You know, extra time in football is completely random randomized. [snorts] Um and then there is turnbased clock models where in baseball you run on innings, in darts you run on sets and legs. In tennis you run on sets and games. And also these are clocks, right? These are clock models that if you do data data anal analysis on them, you use that tact that clock model on your systems. And then at last point in motorsports and athletics,

**[12:24](https://www.youtube.com/watch?v=959-8HEDzdc&t=744s)** the clock is not the clock at all. The clock is distance. It's the length of the track in Formula 1 is your clock. Why? Because your objective is to shorten the time on which you drive. And to make the laps comparable, you need to have a fixed x-axis. The only way to create a fixed x-axis is by using distance as time. And that's it. >> Thank you very much, Clemens. [applause]
