---
title: Waku Evaluation
tags:
  - "2025q4"
  - "dst"
  - "waku"
draft: false
description: "Test Waku on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:waku:2025q4-waku-evaluation`

## Description
Test Waku on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Waku and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

### Background

We want to learn specific, actionable information
about Waku's behaviour
and how it is evolving over time
with each new release
and with each thing we are specifically asked to check and test.

We will use a combination of real world testing,
theoretical analysis and simulation
to determine and measure the success,
side effects and other factors of Waku and its evolution.

## Task list

### Regression testing (recurring)

* fully qualified name: `vac:dst:waku:2025q4-waku-evaluation:regression-testing`
* owner: Alberto/Farooq
* status: in progress (70%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Run different scenarios
and collect evidence and data
of Waku's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Reports:
- [nwaku regression testing v0.37 findings](https://www.notion.so/nwaku-regression-testing-v0-37-October-2025-29c8f96fb65c80de9314c66dd3698b69)
- [Waku regression testing v0.37 – November 2025](https://www.notion.so/Waku-regression-testing-v0-37-November-2025-2b18f96fb65c80ec8f54d4eee93fabb7)
- Related PRs if apply:


### Quic-vs-tcp

* fully qualified name: `vac:dst:waku:2025q4-waku-evaluation:quic-vs-tcp`
* owner: Alberto
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description

Perform a comparison between Waku using quic and waku using mplex and yamux.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Reports:
- Related PRs if apply:


### nWaku API docker image

* fully qualified name: `vac:dst:waku:2025q4-waku-evaluation:nwaku-api-image`
* owner: TBD
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description

Merge all utilities from DST/nWaku into a single docker image.
This involves images that are used to interact with store, filter and lightpush protocols.
It should be investigated if adding the Waku publisher here is also a useful idea.
Documentation and code clarity is required, as this could be used by the waku team, or other projects.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Reports:
- Related PRs if apply:
