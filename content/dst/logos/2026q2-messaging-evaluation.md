---
title: Messaging Evaluation
tags:
  - "2026q2"
  - "dst"
  - "logos"
draft: false
description: "Test Messaging on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`ift-ts:dst:logos:2026q2-messaging-evaluation`

## Description
Test Messaging on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Messaging and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

## Task list

### Regression testing (recurring)

* fully qualified name: `ift-ts:dst:logos:2026q2-messaging-evaluation:regression-testing`
* owner: Alberto
* status: in progress (10%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Run different scenarios
and collect evidence and data
of Messaging's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
- Code:
    - [vacp2p/10ksim#241](https://github.com/vacp2p/10ksim/pull/241) Update broken message_injector
- Reports:
    - [Notion: Logos-delivery regression testing - v0.38 - April 2026](https://www.notion.so/Logos-delivery-regression-testing-v0-38-April-2026-WIP-34a8f96fb65c806b8fd2c7c830ba4463)


### load metric

* fully qualified name: `ift-ts:dst:logos:2026q2-messaging-evaluation:load-metric`
* owner: Alberto
* status: not started
* start-date: 2026/04/27
* end-date: 2026/05/07

#### Description
Include new metric for load in logos-delivery experiments introduced in https://github.com/logos-messaging/logos-delivery/pull/3808

#### Deliverables
- Code:
- Reports:


### quic vs tcp

* fully qualified name: `ift-ts:dst:logos:2026q2-messaging-evaluation:quic-vs-tcp`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Analyze logos messaging using quic from nimlibp2p and compare results with mplex/yamux.

#### Deliverables
- Code:
- Reports:


### Scalable Data Sync
> *Note*: This needs more input from project
* fully qualified name: `ift-ts:dst:logos:2026q2-messaging-evaluation:scalable-data-sync`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

TBD

#### Deliverables
- Code:
- Reports:
