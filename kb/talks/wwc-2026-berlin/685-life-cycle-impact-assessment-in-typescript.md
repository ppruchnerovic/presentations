---
id: 685
title: "Life Cycle Impact Assessment in TypeScript"
slug: life-cycle-impact-assessment-in-typescript
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Keynote/Talk"
stage: "Stage 1"
tags: ["APIs", "TypeScript"]
speakers: ["Corinna John"]
speaker_companies: ["adesso SE"]
day: 1
starts_at: 2026-07-09T11:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=6NC9laD5OHY
video_id: 6NC9laD5OHY
session_page: https://app.wearedevelopers.com/events/16/session/685
transcript: true
---

# Life Cycle Impact Assessment in TypeScript

**Corinna John (Principal Software Engineer — adesso SE)**

`Track: Frontend, Web & Mobile` · `Type: Keynote/Talk` · `Stage: Stage 1`

`#APIs` `#TypeScript`

[Watch the recording](https://www.youtube.com/watch?v=6NC9laD5OHY) · [Session page](https://app.wearedevelopers.com/events/16/session/685)

## Abstract

Life cycle assessment of hardware products is becoming more important, as sustainability is a thing. The common tool "OpenLCA" is designed for expert use - but there is a TypeScript API. It allows you to write a simple UI and automate calculations of life cycle assessments.
In this live session I present a simplified LCA study first in OpenLCA, then write a React frontend with the "olca-ipc" TypeScript library and perform the same calculation in a web browser.

## Speakers

### Corinna John

*Principal Software Engineer — adesso SE*

Corinna lives in Hannover and works in renewable energies, always trying to connect coding with sustainability ideas. She ues C# since the year 2002 and has recently jumped into TypeScript for an LCIA project.

## Transcript

*1,327 words · source: yt (de)*

**[0:04](https://www.youtube.com/watch?v=6NC9laD5OHY&t=4s)** [applaus] So, welcome to my talk. Today I want to give you a very short glimpse into the white and complex field of life cycle assessment and especially a library that allows you to write very simple userfriendly UI for this life cycle assessmented moral framework for assessing everything that flows into out of product over life cycle getting out usone management materials back materials l to the on

**[0:52](https://www.youtube.com/watch?v=6NC9laD5OHY&t=52s)** the beginning of every life cycle assessment is inventory analysis experts review everything that goes into your project from energy materials luse water and so on at every stage of the life cycle was management matycling. How do you know what flows into product? Of course, you can do your own measurements. That's what we call primary data. But very far more often we will have to rely on former studies by other people. suppliers

**[1:43](https://www.youtube.com/watch?v=6NC9laD5OHY&t=103s)** secondary data usually more important one in real life life life cycle assessment is app to big and complex products for example my latest customer the life cycle of wind power plans because in some countries required to present carbon footprint calculation producton made apple juice and water in plastic bottle so plastic bottle made of recycled plastic it takes water and okay apples

**[2:33](https://www.youtube.com/watch?v=6NC9laD5OHY&t=153s)** to produce apples you need those trees Fertilizer pesticides out tractor. Oh my god. Never end. So we need to define clear system boundaries. So first show you how to do this in the open source software open desktop UI. Pin write simple UI in typescript for you. So let's begin. Welcome to very small desktop UI does not scale open LCA. I prepared something for you. Hope the people in the first line can read it a

**[3:24](https://www.youtube.com/watch?v=6NC9laD5OHY&t=204s)** bit. [räuspern] It is product I call developer drink and contains of course apples p for the bottle and water transported to the customer l of apples to be transported to our factory another lor all been preomiled into so product K. What goes into it? Apples. What goes into apples? Apple production ist hier getting longer and longer and longer. But what really want to know what is the environmental impact of doing all?

**[4:15](https://www.youtube.com/watch?v=6NC9laD5OHY&t=255s)** Well, it depends depends on the size of business. For first example, let say small startup from farmer in the neighborhood 10 k away transport bottles only in city k maximuming 0.5 one part water one part apple juice calculate what do we cause our business calculate can take a while. The windfarm project I told you about calculated up to a minute. But this one is small. And now we should see a graph exactly

**[5:08](https://www.youtube.com/watch?v=6NC9laD5OHY&t=308s)** developer drink. Green means positive climate impact Apple production positive impact on climate because we are growing trees and so on the red line carbon emissions transport of bottles to the customer. Okay. But after all this number is not really readable from for you. negative number negative CO2 in business for climate but now let's assume our business is growing people love our product try to produce more new parameter set all parameters of our project

**[5:58](https://www.youtube.com/watch?v=6NC9laD5OHY&t=358s)** transport kilometers of apples farm the factory of bottles, factory to customer of water to juice. Okay, we are growing me to buy more apples from Farm Far away get apples from 500 km away. Sh in the whole country up to 1000 ket away. Oh, and save. Let's use less apple juice and more water. And now let's calculate the carbon impact of this same product biger business. So not baseline parameters go complicated way doing it in the open

**[6:52](https://www.youtube.com/watch?v=6NC9laD5OHY&t=412s)** LCA desktop. Und here we go. The positive impact is very very small and number is higher zero positive means bad carbon emission. Project not anymore. Ui [schnauben] usable for farmers sales people marketing simple user interface web browser fancy cards. Of course we can do this because possible to run this open LCA headless without UI and IPC server

**[7:41](https://www.youtube.com/watch?v=6NC9laD5OHY&t=461s)** IPC server H in the developer mode. So let's go for it and let's to typescript prepared something here. And what we want to do now is get the list of calculation methods and get the product systems predefined by our environmental experts impact methods. Okay. get first open IPC Open Life Cycle Assessment Interprocess communication name of the library that we are using here ist just

**[8:31](https://www.youtube.com/watch?v=6NC9laD5OHY&t=511s)** ja API calling the API auf der open ACA in desptal methods desptors of type impact method same when we want to get our product systems descriptors descriptors of product system now startet. Ja, H go. Okay, now it has recognized the product systems in my database and it's too much common user will not find

**[9:24](https://www.youtube.com/watch?v=6NC9laD5OHY&t=564s)** right method to apply. filter filter all in database predefined for actually use easy because [schnauben] filter list of names filterc [schnauben] Select IPCC method next problems system parameters scan database parameters

**[10:28](https://www.youtube.com/watch?v=6NC9laD5OHY&t=628s)** One exception is not called descriptors. Olka library actually get parameters auf product system parameters of product system of the system selected. developing. Ja parameter a name default value that was predefined in the model. Now we need to calculate it just like pressing the calculate button in desktop UI. So le few more steps. First we have to set up our calculation. So target system product system working

**[11:16](https://www.youtube.com/watch?v=6NC9laD5OHY&t=676s)** in impact calculation measure user selected target amount how many bottles to produce and of course parameters user entered start calculation first run in the background get only handleit until the calculation result handle and you can check finished doing ready finished because

**[12:05](https://www.youtube.com/watch?v=6NC9laD5OHY&t=725s)** quick one today okay so we can Yes, see numbers global warming potential okay number good number is global temperature change potential actually not sure what is the difference so will just show nice charts. Materialings open

**[12:53](https://www.youtube.com/watch?v=6NC9laD5OHY&t=773s)** user numbers really cool diag flow charts one lines library library con component expect very very similar in structure to what we get from our result so we can just request graph also a collection of vertices and edges usually work

**[13:48](https://www.youtube.com/watch?v=6NC9laD5OHY&t=828s)** calculate again get the full result including address take that long go now the red and green lines green for climate positive things. positive small businessal grow produce more botalistic for whatever values ulations

**[14:44](https://www.youtube.com/watch?v=6NC9laD5OHY&t=884s)** complex desktop UI compare val compare impacts so open one side for people actually Standard framework system inventory calcul assessment look what calcul cycleate the details and know when to stop so quick glimp

**[15:43](https://www.youtube.com/watch?v=6NC9laD5OHY&t=943s)** textbook.com com So any questions? I think I hope you enjoyed it a bit. [gelächter] No fashions. Das ist gut. [gelächter] No,

**[16:42](https://www.youtube.com/watch?v=6NC9laD5OHY&t=1002s)** any question anyone want to ask i can actually ask one in the third slide of your talk to the third slై of this one theந sl after thisஒ மோஸ் slை afterதி so you mention aboutதி trதி So can you scale it to that level like it's almost like a m like a micro detailing actually there are databases and scale to that level I can show you this in the open LCA take a look at this result graph

**[17:33](https://www.youtube.com/watch?v=6NC9laD5OHY&t=1053s)** it sc production luse market for diesel and when you go back to the model model the graph open it market for okay irrigation lens use phenoxy transport market raansport tractor it is already al defined in here global market for diesel global market for tractor for wheels tractor production Eent database databas

**[18:22](https://www.youtube.com/watch?v=6NC9laD5OHY&t=1102s)** smart people predefined all possible flows for all possible materials so look intoor production you get for Ampel Aluminium in the market for Aluminium treatment of aluminium again big market so connection of flows der predefine flows for kind of material and then of this flows into common products common goods and so on why do never do life cycle analysis completely on own databases Ai agent

**[19:20](https://www.youtube.com/watch?v=6NC9laD5OHY&t=1160s)** AI layer platform need calculations on numbers any AI [seufzt][japst] for informet en AI make experts maybe find secondary data find data so okay database because in the past it was done manually speaker

**[20:19](https://www.youtube.com/watch?v=6NC9laD5OHY&t=1219s)** Dank dir. [applaus]
