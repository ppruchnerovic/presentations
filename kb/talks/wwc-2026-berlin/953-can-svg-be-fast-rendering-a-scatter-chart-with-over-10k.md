---
id: 953
title: "Can SVG be fast? Rendering a scatter chart with over 10k points"
slug: can-svg-be-fast-rendering-a-scatter-chart-with-over-10k
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Lightning Talk"
stage: "Airstream 1"
tags: ["JavaScript", "React", "TypeScript"]
speakers: ["Bernardo Belchior"]
speaker_companies: ["MUI"]
day: 2
starts_at: 2026-07-10T11:50:00+00:00
duration_min: 10
recording_url: https://www.youtube.com/watch?v=oYfhnQZH0lc
video_id: oYfhnQZH0lc
session_page: https://app.wearedevelopers.com/events/16/session/953
transcript: true
---

# Can SVG be fast? Rendering a scatter chart with over 10k points

**Bernardo Belchior (Software Engineer — MUI)**

`Track: Frontend, Web & Mobile` · `Type: Lightning Talk` · `Stage: Airstream 1`

`#JavaScript` `#React` `#TypeScript`

[Watch the recording](https://www.youtube.com/watch?v=oYfhnQZH0lc) · [Session page](https://app.wearedevelopers.com/events/16/session/953)

## Abstract

In this talk, we’ll explore the performance limits of SVG when rendering scatter charts with thousands of data points, based on our experience at MUI X Charts.

You’ll learn how to identify bottlenecks, performance measuring tricks, and the techniques we use to optimize rendering.

## Speakers

### Bernardo Belchior

*Software Engineer — MUI*

Bernardo is a software engineer working on the MUI X Charts team to build the next-generation of React charts. He likes performance work and data visualization in general (charts, maps, etc.) and is very excited to have the opportunity to improve the ecosystem of charting in the web.

## Transcript

*1,331 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=oYfhnQZH0lc&t=0s)** Well, hello everyone. Uh as I said, I'm Bernardo and I'm here to talk to you about charts and how we made them fast uh with SVG. So, we probably know Material UI, uh well-known library if you're working in the React ecosystem. I don't know if you know about Base UI. It's something that we just released recently and uh do you know Base UI? Show hands. Oh, just one person, too. Nice. But, do you know Shatsi and UI? Oh wow. More people. So, yeah, Base UI, as of last week, is now the default library behind Shatsi and UI. So, every next project that you create with Shatsi and we'll use Base UI, which is built with um which is built by MUI, where I work. But, yeah, enough about that. Let's go back to charts. So, this talk will be about uh my experience when I was working at the MUI X charts team, uh which is the charts library for for MUI.

**[0:57](https://www.youtube.com/watch?v=oYfhnQZH0lc&t=57s)** Um it's SVG based and it can render like the the charts that you can see here on screen. You have line, scatter, stuff like that. Also, maps, candlesticks, Sankey, all that good stuff. However, in May 2024, we received a complaint by a user saying, "Well, your charts are slow when you have a lot of data points." They were like, "All right, cool. Let's investigate." And um the specific case they had was this line chart with these points that we call markers. And as soon as we asked them, "Well, can you disable them disable these markers these circles to see how it works?" They said, "Well, it works perfectly." So, okay. We realized that there was an issue with the markers and so we got to investigate. So, where do you see more markers than in a scatter chart? Pretty much the same thing, but many many more markers. And this is now an example from our docs, where we are showing 16,000 data points

**[1:56](https://www.youtube.com/watch?v=oYfhnQZH0lc&t=116s)** as a result of what we've done. And to show you that there's a real use case to have so many data points rendering in the browser. It's fully interactive, by the way, if you go to our docs. All right. So, let's go a bit about how our scatter plot is being rendered. You have You render the scatter plot component, and that will render a scatter marker component for every circle that you see on the screen, which will eventually render an SVG circle in the DOM. So, I don't know. Here we have maybe 31 30 circles, and we'll have 30 DOM elements. To profile this, we created I created a scatter chart with 10,000 data points. So, let's take a look at how how it handles it. And I'm not sure you can see this. I was a bit afraid. Yeah. So, I'll I'll just tell you. We were spending around 20 milliseconds

**[2:50](https://www.youtube.com/watch?v=oYfhnQZH0lc&t=170s)** just rendering the React render cycle, and then about 140 milliseconds creating the DOM elements, setting the attributes, and then much more time on the right. I don't know if you can see, but there's a bunch of purple bars and also green bars that are the work that's that's been done by the browser. And it's usually it can scale with with the number of DOM elements that you're rendering. So, from taking a look at this, we kind of found, well, maybe we're rendering too many DOM elements. Can we maybe work around this somehow? So, the approach we found, or the at least the initial approach, and what a lot of chart chart libraries do, is going for a canvas, which is pretty simple to solve our use case. You have one DOM element, which is a canvas, and then you just draw all circles as you see on the screen here. The benefit is obviously that you fix the issue, you no longer have a bunch of

**[3:49](https://www.youtube.com/watch?v=oYfhnQZH0lc&t=229s)** DOM elements, but then you have other issues. And if you're used to Material UI, we use CSS to style things, and if you're using canvas, you can't really apply some of these properties. For example, fill, stroke, stuff like that. You can no longer apply those to your circles or to your your markers, right? So, we wanted to find another solution that would allow you to style some things. Obviously, we had some trade-offs, but it would still keep you in the same state of mind when you're using Material UI. So, the way we did it is we created a batch SVG. And what this does is, unlike the previous solution, which is on the left, you have a circle element a circle uh SVG element for each circle that you see on the screen, we're actually using one path, and then inside the path we draw all the circles. The benefit of this is that you reduce

**[4:45](https://www.youtube.com/watch?v=oYfhnQZH0lc&t=285s)** by a lot the number of DOM DOM elements. You can decide, I don't know, I want 1,000 or 10,000 in each path, and you can tweak it, but you can still apply fill, you can still apply opacity, you can still apply stroke. You cannot apply things like, I don't know, if you try to scale it, it won't work well, right? But for most things that people are are going to use in a chart, it still works well. It's much more performant, as we'll see. So, just to see to show you the previous flame chart that we had, we were taking around 410 milliseconds for the whole rendering, the initial render. And now we're taking around 150 milliseconds to do the same thing. So, visually, it's the same thing, but we're spending much, much less time. So, in total, we got around almost three times faster initial render just with this improvement alone. This with four times CPU throttling. So, yeah, as I mentioned, we also had

**[5:44](https://www.youtube.com/watch?v=oYfhnQZH0lc&t=344s)** some trade-offs that we had to do. Uh one of them was the click event. Before, it was kind of trivial, just apply an on-click listener and you know where the click came from. But, now we had to have some kind of special spatial index that maps from the pixels back to the item that was clicked on. Um bit more madness that we need to do, but it was still it solves the problem, which I think is a good thing. Also highlighting uh it's a feature that we have that uh the basically, as you move the cursor around, the closest item will keep its its opacity at one, for example, and everything else will be slightly faded at opacity 30%. And uh for this, we need to find a work-around not to have to uh re-render the whole path for the dimmed uh the the faded elements. And the way we did it is that we just render a replica on top. So, if you have an

**[6:44](https://www.youtube.com/watch?v=oYfhnQZH0lc&t=404s)** opaque circle, you don't see any issue. Um but, you do see it if you have like a uh translucent one. And that's something that we also had to mention in the docs. Um the last trade-off is this one. Uh for some things, yeah, some things didn't work as you'd expect, so we had to document them. But, I think in the end, it was worth it for the around three times uh faster render that we that we found. >> [snorts] >> All right, that's that's it. It was much faster than I expected. Uh so, yeah. Uh if you want to see our work, you can see it at this repo. Uh it's open source. And also, you can find me on the socials. And if you'd like to um provide some feedback to the session, I'd appreciate it. And you can just uh scan that QR code and leave it there. And that's it. Thank you very much. >> [applause]
