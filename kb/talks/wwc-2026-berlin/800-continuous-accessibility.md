---
id: 800
title: "Continuous Accessibility"
slug: continuous-accessibility
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Frontend, Web & Mobile"
type: "Keynote/Talk"
stage: "Stage 1"
tags: ["Accessibility", "CI/CD", "Cypress", "Playwright", "Testing", "TypeScript"]
speakers: ["Jörg Jakoby"]
speaker_companies: ["Atos"]
day: 1
starts_at: 2026-07-09T15:30:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=RS4DmYTvHIo
video_id: RS4DmYTvHIo
session_page: https://app.wearedevelopers.com/events/16/session/800
transcript: true
---

# Continuous Accessibility

**Jörg Jakoby (Software Developer — Atos)**

`Track: Frontend, Web & Mobile` · `Type: Keynote/Talk` · `Stage: Stage 1`

`#Accessibility` `#CI/CD` `#Cypress` `#Playwright` `#Testing` `#TypeScript`

[Watch the recording](https://www.youtube.com/watch?v=RS4DmYTvHIo) · [Session page](https://app.wearedevelopers.com/events/16/session/800)

## Abstract

In this session, I will demonstrate how to move accessibility with low effort from an "afterthought" to a systematic verification process using fast unit checks (jasmine-axe, jest-axe, vitest-axe) and realistic E2E scans (Cypress, Playwright). Instead of manually checking accessibility shortly before release, we shift feedback to the left: components are validated in isolation during testing, and critical user flows are scanned in real browsers. This is not just about tools, but about robust routines: ensuring stable UI states before scanning, maintaining consistent WCAG tags/severity levels, generating actionable reporting in CI, and establishing clear gate rules ("build fails on serious/critical").
Furthermore, I will shed light on the practical side: how teams handle exceptions (with justification and expiration dates), how to choose the right scopes (e.g., scanning a dialog instead of the entire page), and why uniform guardrails across unit and E2E tests are crucial for making accessibility sustainable, scalable, and genuinely integrated into daily development.

## Speakers

### Jörg Jakoby

*Software Developer — Atos*

Experienced software developer with 17 years of experience in frontend development. Specialized in the development of web applications with Angular and extensive knowledge of JavaScript, HTML, and CSS.
Great emphasis on accessible web content and is an Atos Accessibility Champion as well as a Certified Professional in Web Accessibility (CPWA).
Successfully developed web-based user interfaces while considering the Web Content Accessibility Guidelines (WCAG) 2.2.
Leads frontend teams, plans, and implements microfrontend architectures, thus ensuring structured and modular development.

## Transcript

*1,612 words · source: kome (en)*

**[0:00](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=0s)** Jog Jakobi software engineeros. Please welcome the speaker. [applaus] Thank you for the introduction. Thanks for let start presentation called accessibility and the focus on shift left accessibility testing. Let's take a look at the table of cont about motivation of accessibility. PRC SC Gils accessibility process second point implement automated tests last point implement robust and continuous consistent routines in development workflow quick overview agenda first topic problem statement courses then we will take shift left principle

**[1:11](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=71s)** then we will take look accessibility scansore unit test and last point will take look how we can integrate scans in the end to end test how to impl consist okay first topic ofel man test no automation problem of planning Ja next definition of that means development knowing what exactly want to achieve development defel shift shivel er cost escalat life cycle ja topics first is the latest def issues higher expensive ist fixing up to expensive issues end of

**[2:26](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=146s)** development beginning of delays couldal issues to late creat regressions behavior in application maintainability easier lead better quality solutions thanks to shift left approach that is our next chapter let shift left accessibility first general shift left principle key messages first point prevention instead of remediation that means want to fix and find issues early instead of fixing issues later want automation of repetition that means we want to automate our test instead of doing the test always man and need shared responsibility so accessibility

**[3:44](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=224s)** need to be team effort everyone in the team should own feature product manager designer to tester developer that get quality efficiency performance in the next slide all that enabler development that means focus on coding instead ofing about how to fix issues laterus prog perfection process then we should implement layer testing our main topic so means checks in the unit test for our components checks in the end toend test to protect complex workflows and states and also man user shakes

**[5:00](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=300s)** additionally AI based scans. Trust verification only if run test in C proper C integration for our unit tests. Okay. Now let's take a look at the unit based accessibility tests. First point is why are unit accessibility test effective? Ja. First obvious point is detection is quite early usually find the issues already development of our component second point is we implement usually independent component tests unit tests that means debugging is easier the result objects that we get easier to

**[6:16](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=376s)** understand and we can follow the concept of atomic design our test infrastructure never much proper workflow prevention effective excibility issues proper implemented and some of them are missing labels missing alternative text area misuse and contrast issues and that some of the most common accessibility issues the last Positive point is speed and integration. The unit tests are very easy to integrate and also exp easy to integrate in the unit test and run very fast and effective. So usually take some seconds or less.

**[7:35](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=455s)** Okay, let's talk about integration key features best practice first front integration pluginilable for all test runners test tools like gest vtest and jment so all can used for all main frameworks like angular react and few then we can test realistic proper and states PR central rules test allo applications Okay, let's take a look at the code sample I decided to go the code example Vest X and Angular. So ja example of the button real world example

**[8:48](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=528s)** to demonstrate how it works. function X package pass element first parameter X function X object schat contains violations array all violations found scan example filter array for series and critical issues at the expectation that array isempty and critical issues other filtering could also use expectation toolation partest x library others SC function configure XV test X library options second parameter example run test attack exactly so all rules 22A enhance that other like aa okay I guess that's clear and you see

**[10:06](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=606s)** quite easy to implement it in the unit tests now let's go to the end toend accessibility scan first question is why are end to end accessibility test essential er the answer cap test complex workfowsend test in design cover complex workflows dynamic states advantage in m browsers browser compatibility test point because coverage for accessibility browsers otherse would have to do manual tests to compatibility last point is end to end test usually focus strategies that means end to end

**[11:20](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=680s)** tests cover all critical workflows combine accessibility scans make that most important workflows are covered accessibility scans. Okay, now let's take a look at different types of end to end test scans, die scoped scans and die full page scans. The full page scans means that scan the whole page complete of the application. leads to issues potential is issues execution time slow unstabley we have benefits of scope scan scope scans means restrict our test to one element only test advantage test

**[12:37](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=757s)** obviously faster because only small elemental check smaller of less stable but best setup is combine full page scan scoped scans. Yeah. Scope scans are usually interaction coupled that means for example if we want to share a dialog then we first of course need to open dialog so we need to implement interaction to open dialog and then run the scan on the open dialog that's also what will see in the practical example later the last point is scope scans could be

**[13:54](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=834s)** easier to maintain because focused on similar to the unit tests focused on one element object is easier Okay, now let's take a look minimal setup playor example play also could also use playr IBM equ other library but since play and XC is documented officially and easy to integrate I decided to show with this combination. Ja, first step is install dependencies command npm important instore play test package playest okay plugins required pipele. page edit button trigger on button

**[15:08](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=908s)** dialog create new object page to the X builder include function scan profile dialog element restrict scan v2a rules analation res unit tests expectation exactly same that seen unit test example okay to additional commands first seen already you can use also helper functions from play like to have accessible name to check that element proper accessible name also use match are snapshot that means check element proper accessibility clear up in play documentation res official reporter package export play

**[16:22](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=982s)** nice HTML report could deploy gitar playground for example you could use wick that reporter of play. Okay. Ja. So much about end to end tests and now let's take a look about how to handle that but let's see little bit more in detail. Ja rules and severity levels should be consistent main point. First need uniform criteria means criteria for unit testend test ofck test for the unit test around else make sense. Yeah. min moderate critical Last point central definition that means

**[17:40](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=1060s)** definition in the repository do that follow concept of trust acceptance that means development accepts criteria def management product management team okay example define global configuration playore to do that we just need to extend x fixture implement function called make x builder passage of page and here we can define our rules and can also exclude elements that don't want to shake because of issue that will be topic of the next chapter ja could of course also create extensions parameters SC

**[18:57](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=1137s)** test function in test call function as got x builder. Okay, now let's talk about exceptions and guard trails. Ja exceptions in most cases exceptions responsibly. Ja, first question exceptions most of the cases historical in third party legacy compon exception exceptions document exception create issue for the exception since defined in the definition of done and for each last point implement work around but instead implement proper solutions exceptions okay now let's take look at the gardils

**[20:08](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=1208s)** in the CICD pipeline. First topic is commit issues should be blocked that could be done lints or code quality shacks like son cube the next topic talk about the unit tests unit test in the cd pipeline unit test pipel build blocked pipeline blocked issue needs to be fixed before the pipeline continues last SC CD pipeline is pipel stop is fixed before pipeline continues and after sc enhan accessibility scans accessibility scans AI based accessibility scans. Okay. Ja. already the content of the

**[21:27](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=1287s)** presentation. Now let's give summary and mention the key learnings. Ja first talked about unit test based accessibil should be implemented because fast and cost effective good regression protection. Second point addend scans because secure real workflows capture dynamic states. Next important point is that we have consistent rules and reporting and that test run in die CICD plel based on the rules defined project management and the last point is that we have responsible exception management that

**[22:38](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=1358s)** means cre issues exceptions justification owner and expiration [applaus] am presentation about to testing crucial prodction deyம there is one question which is how can screen reader test be covered for example making sure the screen reader reads it correctly end unit test possible combine end test ai so aiit screen testouing on that kind of based in related to that in your testing pipelines you are you using any AI agents to do the end to end

**[23:50](https://www.youtube.com/watch?v=RS4DmYTvHIo&t=1430s)** tests or at least the unit like that write the unit test and also the test and report them. How do you mean that are done by are they done by directly by the AI any of the AI agent testen super further question so than you for the presentation let the speaker J. Ja. [applaus] Ja.
