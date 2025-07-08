---
title: Status evaluation
tags:
  - "2025q2"
  - "dst"
  - "status"
draft: false
description: "Test Status-go on each new version or feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:status:2025q2-status-go-evaluation`

## Description

Test Status-go on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Status-go and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

The scope of this commitment is expected to be updated based on input from Status.
work and improvements, and it is subjected to change.

### Background

We want to learn specific, actionable information
about Status-go's behaviour
and how it is evolving over time
with each new release
and with each thing we are specifically asked to check and test.

We will use a combination of real world testing,
theoretical analysis and simulation
to determine and measure the success,
side effects and other factors of Status-go and its evolution.

### Narratives

We will support the Conduit of Expertise narrative directly
by analysing and evaluating new Status-go releases and their features,
both with regards to features they have today
and with regards to how that compares to past behaviour.

Additionally, these efforts will contribute
to the Premier Research destination narrative by
improving and strengthening our relationship with the Status-go team
and thus increasing the reach and influence of the IFT,
and improving the chances
that we successfully grow our ecosystem's products and collaborations
and especially those we want to work with externally.

## Task list

### Regression testing (recurring)

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:regression-testing`
* owner: Alberto
* status: Recurring
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description

Run experiments on new or required status-go versions.
Maintain a report that can compare performance of new versions
with past ones. Make sure regressions are not happening,
or any other functionality specific request that can come from the status team.

#### Deliverables
* Reports:
* Related PRs if apply:
  - [Merged PR #1: Base-manifests](https://github.com/vacp2p/status-benchmarks/pull/1)
  - [To review PR #2: Controlbox](https://github.com/vacp2p/status-benchmarks/pull/2)
  - [To review PR #3: Status-Subscriber](https://github.com/vacp2p/status-benchmarks/pull/3)
  - [To review PR #4: Status-Init](https://github.com/vacp2p/status-benchmarks/pull/4)
  - [To review PR #5: Deployment Files](https://github.com/vacp2p/status-benchmarks/pull/5)
  - [To review PR #6: Logger](https://github.com/vacp2p/status-benchmarks/pull/6)
  - [To review PR #7: K8s Utils](https://github.com/vacp2p/status-benchmarks/pull/7)
  - [To review PR #8: RPC & Signal clients](https://github.com/vacp2p/status-benchmarks/pull/8)
  - [To review PR #9: Services](https://github.com/vacp2p/status-benchmarks/pull/9)
  - [To review PR #10: StatusBackend](https://github.com/vacp2p/status-benchmarks/pull/10)
  - [To review PR #11: Message Injection](https://github.com/vacp2p/status-benchmarks/pull/11)
  - [To review PR #12: Setup StatusBackend functions](https://github.com/vacp2p/status-benchmarks/pull/12)
