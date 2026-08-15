---
id: 713
title: "Trust Issues: Because Zero-Trust Isn’t Optional Anymore"
slug: trust-issues-because-zero-trust-isnt-optional-anymore
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Security & Privacy"
type: "Keynote/Talk"
stage: "Stage 9"
tags: ["Cloud Security", "Docker", "Infrastructure", "JavaScript", "Security"]
speakers: ["Jan Peer Stöcklmair"]
speaker_companies: ["Sentry"]
day: 1
starts_at: 2026-07-09T12:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=ltSozoarGbI
video_id: ltSozoarGbI
session_page: https://app.wearedevelopers.com/events/16/session/713
transcript: false
---

# Trust Issues: Because Zero-Trust Isn’t Optional Anymore

**Jan Peer Stöcklmair (Senior Software Engineer — Sentry)**

`Track: Security & Privacy` · `Type: Keynote/Talk` · `Stage: Stage 9`

`#Cloud Security` `#Docker` `#Infrastructure` `#JavaScript` `#Security`

[Watch the recording](https://www.youtube.com/watch?v=ltSozoarGbI) · [Session page](https://app.wearedevelopers.com/events/16/session/713)

## Abstract

“Just ship it” doesn’t cut it anymore, everything in our stack is connected, exposed, and talking to things it probably shouldn’t. Modern applications don’t just benefit from Zero-Trust principles; they depend on them. And yet… our frontends trust too much, our backends trust too much, and our infrastructure trusts everything by default. With attacks like React2Shell emerging from seemingly harmless origins, we need to be prepared to minimize the impact of inevitable vulnerabilities.

In this talk, I break down Zero-Trust in a practical, full stack way - from the browser all the way down to the infrastructure.

The talk starts at the Frontend, where simple changes like strong CSPs, proper handling of CSRF tokens, secure cookies, and escaping strategies can prevent entire classes of attacks before they ever reach your server. Then we move into the Backend, exploring security patterns that make your services resilient even when assumptions fail, because they will. This includes approaches like mounting secrets via files instead of environment variables, enforcing permission-based API access, and more.

Finally, we zoom out to the Infrastructure layer, where Zero-Trust becomes real: mTLS for identity, distroless and unprivileged containers to shrink the attack surface, network cuts and segmentation to isolate blast zones, and other future-proof operational patterns that keep your system secure even when (not if) something goes sideways.

By the end of the talk, the audience walks away with a practical, full-stack security playbook everyone can apply immediately: from browser headers to Docker containers. Just the tools you need to build systems that don’t rely on trust, assumptions, or wishful thinking.

Zero-Trust isn’t optional anymore. But with the right patterns, it also doesn’t have to be painful.

## Speakers

### Jan Peer Stöcklmair

*Senior Software Engineer — Sentry*

I’m a software engineer working at Sentry and Pebblebyte, where I focus on frontend, DevOps, and making sure observability is everywhere. When I’m not deep in code, you’ll probably find me kitesurfing, road biking, swimming, or hanging off a rock wall. Whether I’m debugging or chasing wind, I’m always looking for that perfect flow.
