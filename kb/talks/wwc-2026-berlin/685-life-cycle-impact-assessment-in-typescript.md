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

*2,436 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=6NC9laD5OHY&t=0s)** [applaus] So, welcome to my talk. Today, I want to give you a very short glimpse into the wide and complex field of life cycle assessment and especially a library that allows you to write very simple, user-friendly you that you eyes for this. Well, life cycle assessment is a method or a framework for assessing everything that flows into or out of the product over its whole life cycle. From getting metals out of the earth until the usage of your maybe a mobile phone and even waste management. What can you do? Which materials can you get back? Which materials are lost to the air and so on. The beginning of every life cycle assessment is inventory analysis. Experts review everything that goes into your product, from energy, materials, land use, water and so on at every stage

**[1:10](https://www.youtube.com/watch?v=6NC9laD5OHY&t=70s)** of the life cycle until your formally final new product is treated by waste management. Maybe you get can get some material back by recycling. But how do you know what flows into your product? Of course, you can do your own measurements. That's what we call primary data. But very far more often we will have to rely on former studies by other people or on data sheets from your suppliers. This is secondary data, usually the more important one. Well, in the real life, life cycle assessment is applied to big and complex products. For example, my latest customer assesses the Life Cycle of Windkraftanlagen, die Kosten zum countries ja required to present a full carbon footprint calculation oder eben der Water or Land use footprint, vor der allow you to build a Windpark,

**[2:18](https://www.youtube.com/watch?v=6NC9laD5OHY&t=138s)** but for today lass du something simple, dass das analyse des Product von Lemonade mainly made of Apple Juice and Water in der Plastikflasche. So, wir haben eine Plastikflasche made of recycled Plastik, es takes Water and okay Apples. To produce Apples you need those trees or solar system a fertilizer pesticides brought out by a tractor or my God, was goes into a tractor, wenn der Bild it, you see this will never end, so we need to define clear system boundaries. So first, I will show you how to do this in der Open Source Software Open LCA, which has its own Desktop UI, you will see it's a really a pain and then I will write a simple UI in TypeScript for you. So, let's begin. Welcome to I know this is very small,

**[3:27](https://www.youtube.com/watch?v=6NC9laD5OHY&t=207s)** but the Desktop UI does not scale. Open LCA. I prepared something for you. I hope the people in the first line can read it a bit. [räuspern] It is a product I call developer drink and it contains of course Apples. PET for the bottle and tap water. It has to be transported to the customer with this lorry and of course the Apples have to be transported to our factory another lorry. So and all this has already been precompiled into a so called system. Which we can then watch here. What goes into it? Apples. What goes into apples? Apple production is here. We see it's getting longer and longer and longer. What what we really want to know is what is the environmental impact of doing all

**[4:33](https://www.youtube.com/watch?v=6NC9laD5OHY&t=273s)** this? Well, it depends. Depends on the size of our business. For this example, let's say we are small startup. We get apples from a farmer in the neighborhood, 10 kilometers away. We transport the bottles only in our city, 50 kilometers in maximum. And we are mixing a water to juice ratio of 0.5. So, one part water, one part apple juice. And let's calculate what do we cause with our business? Come on, calculate. This can take a while. The wind farm project I told you about is calculated up to a minute, but this one is small. And now we should see a graph, exactly. Our developer drink what goes into Green means positive climate impact. Apple production has a positive impact on climate because we are growing trees and

**[5:39](https://www.youtube.com/watch?v=6NC9laD5OHY&t=339s)** so on. And the red line with carbon emissions are the transport of our bottles to the customer. Okay. But after all, I know this number is not really readable from for you it is a negative number. Negative CO2 emissions mean we are good for climate. But now let's assume our business is growing growing. People love our product and we try to produce more. Let's do a new parameter set. Select all parameters of our project. That's transport kilometers of apples, farm to factory of bottles, factory to customer, and of course a mixing ratio water to juice. Okay, we are growing. This means we have to buy more apples from a farmer far away. So, let's assume we get apples from 500 kilometers away. We sell them in the whole country up to

**[6:48](https://www.youtube.com/watch?v=6NC9laD5OHY&t=408s)** 1000 kilometers away. Oh, and we have to save, let's use less apple juice. And more water. And now, let's calculate the carbon impact of this same project, but bigger business. So, now the baseline parameters are called the new would have called them rows. And let's go. So, this is a complicated way when doing it in the open LCA desktop. And here we go, the positive impact is very, very small, and number is higher than zero. So, we have a positive, that means bad carbon emission. Our project is not eco anymore. But you know, this UI [schnauben] is not really usable for farmers or sales people or people who do our marketing. So, we need to write something more simple. It would be so nice if this user interface would look like this, like a web browser with some fancy cards.

**[8:00](https://www.youtube.com/watch?v=6NC9laD5OHY&t=480s)** Of course, we can do this because it's possible to run this open LCA with headless, without this UI. And instead with an IPC server. I can start this IPC server here too in the developer mode. So, let's go for Und let's switch to TypeScript. I prepared something here. And what we want to do now is get the list of calculation methods and get the product systems that were predefined by our environmental experts. Impact methods. Okay. We could do it like this. I hope Is this readable? I can zoom into a little bit more. Let's get the descriptors. Oh, first I should tell you how it is called. OpenLCA IPC. Also, Open Life Cycle Assessment Interprocess Communication is the name of the library that we are

**[9:06](https://www.youtube.com/watch?v=6NC9laD5OHY&t=546s)** using here. It is just an ja, API, calling the API of the OpenLCA application. And nearly everything in here is a descriptor. So, when you get the calculation methods, get some descriptors. Of type impact method. Same when we want to get our product systems. Let's do We get some descriptors. Get descriptors of type product system. Let's see what is tension now. Ah, I should start it. Ja, here we go. Okay. Now it has recognized the product systems in my database and it's too much. Ähm, a common user will not find the right method to apply. So, we have to filter them. We have to filter all the methods that are in this database predefined for those that we actually want to use. This is easy because Ah, let's remove the dummy hier.

**[10:15](https://www.youtube.com/watch?v=6NC9laD5OHY&t=615s)** [schnauben] I can just filter the list. Like this. It's just an array of names and we can filter for IPCC measures which we will use here and maybe some others. [schnauben] Okay, here we go. We can now select the IPCC um method. And And now we have the next problem. Our system has parameters and we need to list them here. So let's scan the database for our parameters. This one exception is not called descriptors. Our library called it actually get parameters. Of Of product system we call it parameters of a product system. And of course the system we just selected. So now when we select our developer drink, yeah, every parameter has a name and a default value that was predefined in the model. And now we need to calculate it.

**[11:23](https://www.youtube.com/watch?v=6NC9laD5OHY&t=683s)** Just like pressing the calculate button in the desktop UI. But we would at least have a few more steps. So first we have to set up our calculation. So it needs a target system. This is the product system we are working in. The impact method was the calculation method that the user selected. Target amount. How many bottles do we want to produce and sell? And of course the parameters that the user just entered. And then we can start the calculation. Ja. Könnte gut ist das ein Weg Kalkulation mit Weg an das Ergebnis, was das Kalkulation kann ein Weil wir normalerweise in der Hintergrund. So ihr geht ein Handel Weg an das Kalkulation startet. Es gibt Resultat Handel. Und ihr kann checken, ob es fertig ist. Was wir sehen ist das Weg an das Resultat ist fertig, dann es ist fertig,

**[12:36](https://www.youtube.com/watch?v=6NC9laD5OHY&t=756s)** weil wir wissen es. Wir machen ein Weg heute. Okay, so wir kann starten unser Kalkulation. Es dauert ein Weil, aber hoffentlich nicht so lang. Ja. Wir kann sehen ein paar Nummern. Global Warming Potential, okay. Schlechte Nummer, gute Nummer ist Global Temperatur Potential. Eigentlich ich bin nicht sicher, was ist der Unterschied. So wir werden einfach ein paar schöne Charts wie wir kann jetzt sehen. Wir gehen durch unser Resultat und zeigen Pie Charts. Das ist Material UI Charts und wir mappen alle Resultate von Open LCA auf es. Es sieht besser aus für ein User als nur diese einfachen Nummern. Aber es wäre wirklich wirklich cool, wenn wir diese Sankey Diagramme für Flowcharts diese mit den drei Linien hier auch einfach, weil ich denke die meisten von euch, wenn ihr Typescript benutzt,

**[13:43](https://www.youtube.com/watch?v=6NC9laD5OHY&t=823s)** kennt die Recharts Library. Die Recharts Library enthält diese Sankey Komponente und es ist erwartet Import, das ist sehr sehr ähnlich in Struktur zu was wir bekommen von unserem Resultat. So wir kann das Request Sankey Graph, also. A collection of vertices and edges from our result set and then just map it to the input structure of Reed Sankey. And usually it should work. So let's calculate again, get the full result including the edges. It won't take that long. Here we go. And now we have the red and green lines, green for climate positive things. Red for climate. Negative things. And we still see. Yeah, a little little bit of climate positive, it's a small business. And now we can calculate our growth. Let's produce. More bottles. Transport them even further.

**[14:50](https://www.youtube.com/watch?v=6NC9laD5OHY&t=890s)** In the whole world. Okay, this is unrealistic. And calculate for whatever. Values we like. This is you. Understandable for a common user. It is scalable. For a small or big screen. And we get to the same calculations as we did before in the complex desktop UI. And then compare our values, compare our. Impacts. So this um. Open LCA, one side note for people who actually want to use this. Is actually a standard framework. And it always begins with a goal and scope definition. So this means you meet system boundaries, define exactly what you want to analyze. Find your eventually calculate the assessment look. What you calculated and it's a cycle. Do this and you iterate, you iterate every further to the. Details, die du sehen willst, und weißt, wann du aufhören musst. Das war mein kurzer Einblick in die

**[16:02](https://www.youtube.com/watch?v=6NC9laD5OHY&t=962s)** Lebenszyklusanalyse und wie man sie benutzerfreundlich gestalten Wenn Sie mit diesem Beispielprojekt spielen wollen, holen Sie es sich von Code Burger, und wenn Sie tiefer eintauchen wollen, gibt es ein sehr schönes Lehrbuch unter lcatextbook.com. Also, irgendwelche Fragen? Ich denke, ich hoffe, es hat Ihnen ein bisschen gefallen. [gelächter] Keine Fragen? Das ist gut. [gelächter] Nein nichts. Gibt es irgendwelche Fragen, wenn jemand etwas fragen möchte? Nein, dann kann ich tatsächlich eine Frage stellen. In der dritten Folie Ihres Vortrags Können Sie zur dritten Folie gehen? Diese? Äh, die nächste Folie nach dieser. Diese? Äh nein noch eine Folie. Nach dieser? Oh ja. Also, Sie haben dieses Traktor-Ding erwähnt. Können Sie es auf diese Ebene skalieren, wie äh äh, es ist fast wie eine winzige wie eine Mikrodetaillierung. Es gibt tatsächlich the LCA databases.

**[17:10](https://www.youtube.com/watch?v=6NC9laD5OHY&t=1030s)** And they scale to that level. I can show you this in the open LCA. When you take a look at this result graph. It scales the apple production. Okay, this is land use. Market for diesel. And when you go back to the model. Model of the graph. I had already opened it. Market for okay, irrigation land use and oxy transport. Market road transport tractor. And here it is already defined in here. Global market for diesel. Global market for tractor four wheels. Tractor production. And here is actually the whole material flow for the production of a tractor. Clearly defined in this eco invent database. Eco invent is one of many databases that you can

**[18:09](https://www.youtube.com/watch?v=6NC9laD5OHY&t=1089s)** buy. Smart people have um. Predefined all possible flows for all possible materials. So when this. Look into this tractor production. You get for example. Aluminum. In the market for aluminum. Treatment of aluminum. Oh, again a big big market. So this is just interconnection of flows. They are predefined flows for every kind of material and then. Of this flows into common products and common goods and so on. And this is why you do never do um. Life cycle analysis completely on your own. You buy those databases with predefined flows. And then just chain chain them and. Let the software And as a closing question, are there any AI agentic or like an AI layer or or on this platform? Actually, it is not needed, because we do exact calculations on known numbers.

**[19:17](https://www.youtube.com/watch?v=6NC9laD5OHY&t=1157s)** No need for any AI. [seufzt][japst] Not for the just for the a bit of like general like a reasoning ones. So you have an AI agent which can try to find the information, retrieve it from the knowledge base. Yes, of course, you you could enhance that with AI to make it easier for your LCA experts to maybe find secondary data, to find data sheets and so on. But okay, we have those databases, because in the past it was done manually, and I think when Ecoinvent and so on will produce the next generation of databases, they will in the background use R&D and so on to find more documents. Super. Thank you on that note, and let's thank the speaker again, Corina John. Thank you. [applaus]
