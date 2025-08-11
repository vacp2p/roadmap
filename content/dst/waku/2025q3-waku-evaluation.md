---
title: Waku Evaluation
tags:
  - "2025q3"
  - "dst"
  - "waku"
draft: false
description: "Test Waku on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:waku:2025q3-waku-evaluation`

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

### Narratives
We will support the Conduit of Expertise narrative directly
by analysing and evaluating new Waku releases and their features,
both with regards to features they have today
and with regards to how that compares to past behaviour.

We will:

* Enable improvements to Waku
  by allowing for repeatable, measureable
  and real world insights into Waku,
  all the way from theory to practice and back.
* Reduce the risk of a Waku regression
  making it into a new release of Waku.

Additionally, these efforts will contribute
to the Premier Research destination narrative by:

* Improving and strengthening our relationship with the Waku team
  and improving the quality and reputation of IFT's work, inside
  and outside of Waku.

### Additional info

## Task list

### Regression testing (recurring)

* fully qualified name: `vac:dst:waku:2025q3-waku-evaluation:regression-testing`
* owner: Alberto
* status: recurring
* start-date: 2025-07-01
* end-date: 2025-09-30

#### Description
Run different scenarios
and collect evidence and data
of Waku's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
- Reports:
- Related PRs if apply:

### Store dial failure

* fully qualified name: `vac:dst:waku:2025q3-waku-evaluation:store-dial-failure`
* owner: Pearson
* status: 100%
* start-date: 2025-07-07
* end-date: 2025-07-18

#### Description

Investigate `PEER_DIAL_FAILURE` error found in regression tests in nwaku v0.36, from the store protocol.

#### Deliverables
- Reports:
  - [Notion Notes](https://www.notion.so/Experiments-for-nWaku-v36-0-21e8f96fb65c801e9ffcd25cf0d88370#22d8f96fb65c807a8fe1d7c7496107a2)
  - [Extra notes](https://www.notion.so/Experiments-for-nWaku-v36-0-21e8f96fb65c801e9ffcd25cf0d88370#2328f96fb65c8008bb66cd46fb37662d)
- Related PRs if apply:

### Store dial failure followup

* fully qualified name: `vac:dst:waku:2025q3-waku-evaluation:store-dial-failure-followup`
* owner: Pearson
* status: 100%
* start-date: 2025-07-23
* end-date: 2025-08-01

#### Description

Investigate `PEER_DIAL_FAILURE` error found in regression tests in nwaku v0.36 in `vac:dst:waku:2025q3-waku-evaluation:store-dial-failure`.

#### Description

Try to reproduce `PEER_DIAL_FAILURE` in nWaku v0.34. Trace the peer_id from one of the failing logs 
to see what that node is doing. Also, reduce number of nodes in the scenario.

#### Deliverables
- Reports:
- Related PRs if apply:
  - [Github Issue](https://github.com/waku-org/nwaku/issues/3524)


### Discv5 feasibility comparison

* fully qualified name: `vac:dst:waku:2025q3-waku-evaluation:discv5-feasibility-comparison`
* owner: Pearson
* status: 100%
* start-date: 2025-07-21
* end-date: 2025-08-01

#### Description

Compare Discv5 bandwidth usage in regression tests to what we would expect from [Discv5 Feasibility Study](https://discuss.status.app/t/discv5-feasibility-study/1632)

#### Deliverables
- Reports:
  - [Notion Notes](https://www.notion.so/Waku-Discv5-analysis-over-time-2378f96fb65c80a5b60bc24d09b5de3a?showMoveTo=true&saveParent=true)
- Related PRs if apply:

### Quic-vs-tcp

* fully qualified name: `vac:dst:waku:2025q3-waku-evaluation:quic-vs-tcp`
* owner: Alberto
* status: 0%
* start-date: -
* end-date: -

#### Description

Perform a comparison between Waku using quic and waku using mplex and yamux.

#### Deliverables
- Reports:
- Related PRs if apply:

### JS waku

* fully qualified name: `vac:dst:waku:2025q3-waku-evaluation:js-waku`
* owner: Pearson
* status: 10%
* start-date: 2025-08-11
* end-date: 2025-08-22

#### Description

Start integrating js waku in DST experiments. Report js waku team any missing functionalities.

#### Deliverables
- Reports:
- Related PRs if apply: