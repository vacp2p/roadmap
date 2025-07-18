---
title: Waku Evaluation
tags:
  - "2025q2"
  - "dst"
  - "waku"
draft: false
description: "Test Waku on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:waku:2025q2-waku-evaluation`

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

### Message latency

* fully qualified name: `vac:dst:waku:2025q2-waku-evaluation:message-latency`
* owner: Alberto
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

Investigate situations where a message
takes up to 2 seconds to arrive to all nodes.
Analyze if this is dependant on number of nodes,
if the messages that take longer have a correlation
with being the latest injected, and so on.
Determine what can be the causes,
and report findings.

#### Deliverables
- Reports:
- Related PRs if apply:

### Regression testing (recurring)

* fully qualified name: `vac:dst:waku:2025q2-waku-evaluation:regression-testing`
* owner: Pearson
* status: recurring
* start-date: 2025-04-01
* end-date: 2025-06-30

#### Description
Run different scenarios
and collect evidence and data
of Waku's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
- Reports:
  - [Notion: nWaku v0.36](https://www.notion.so/Waku-regression-testing-v0-36-21c8f96fb65c804dab04d676c2a6121e)
  - [Notion: nWaku v0.36 notes](https://www.notion.so/Experiments-for-nWaku-v36-0-21e8f96fb65c801e9ffcd25cf0d88370)
- Related PRs if apply:
  - [Github Commit: Cript to generate input for log scraping](https://github.com/vacp2p/10ksim/commit/5ae2a3ca6faf2b6c8d0cb750c37c7c2afaa23e66)