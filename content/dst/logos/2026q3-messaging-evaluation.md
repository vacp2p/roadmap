---
title: Messaging Evaluation
tags:
  - "2026q3"
  - "dst"
  - "logos"
draft: false
description: "Test Messaging on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`ift-ts:dst:logos:2026q3-messaging-evaluation`

## Description
Test Messaging on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Messaging and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

## Task list

### Regression testing (recurring)

* fully qualified name: `ift-ts:dst:logos:2026q3-messaging-evaluation:regression-testing`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Run different scenarios
and collect evidence and data
of Messaging's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
- Code:
- Reports:


### load metric

* fully qualified name: `ift-ts:dst:logos:2026q3-messaging-evaluation:load-metric`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Include new metric (`event_loop_accumulated_lag_secs`) for load in logos-delivery experiments introduced in https://github.com/logos-messaging/logos-delivery/pull/3833

#### Deliverables
- Code:
- Reports:


### quic vs tcp

* fully qualified name: `ift-ts:dst:logos:2026q3-messaging-evaluation:quic-vs-tcp`
* owner: Pearson
* status: done
* start-date: 2026/07/08
* end-date: 2026/07/21

#### Description
Analyze logos messaging using quic from nimlibp2p and compare results with mplex/yamux.

#### Deliverables
- Code:
  - [QUIC connectivity fix branch](https://github.com/PearsonWhite/waku/commits/pwhite/quic_b778d16) and `pearsonwhite/nwaku:quic-b778d16` image
- Reports:
  - [DST Results Summary](https://app.notion.com/p/DST-Results-summary-d7f0381afba343c98f0d8b1ef0193044?source=copy_link#3aa8f96fb65c80d5bca0e7d4084b94e3)
  - [Waku quic vs yamux](https://app.notion.com/p/Waku-quic-vs-yamux-39b8f96fb65c806288b0e68544207b45)
  - [nWaku Regression Testing Notes](https://app.notion.com/p/nWaku-Regression-Testing-Notes-39e8f96fb65c80bea716f022bac100fa)

  
### Logos delivery node
* fully qualified name: `ift-ts:dst:logos:2026q3-messaging-evaluation:logos-delivery-node`
* owner: Pearson
* status: in progress (95%)
* start-date: 2026/07/28
* end-date: 2026/08/07

#### Description

Try new image provided by logos-messaging introduced in [this PR](https://github.com/logos-messaging/logos-delivery/pull/4059)
Note: [REST API interface](https://github.com/logos-messaging/logos-delivery-rest-api/pull/21)
Build image and reproduce some experiments to see if results match and if we need to do modifications in our framework. 

#### Deliverables
- Code:
- Reports:
  - [nWaku delivery node analysis](https://app.notion.com/p/nWaku-deliverynode-3b08f96fb65c80839c80d01484bab923?showMoveTo=true&saveParent=true)
  - Completed the reliability experiment matrix successfully and produced message-delay plots, with one clock-skew anomaly documented for follow-up.



### Scalable Data Sync
> *Note*: This needs more input from project
* fully qualified name: `ift-ts:dst:logos:2026q3-messaging-evaluation:scalable-data-sync`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description

TBD

#### Deliverables
- Code:
- Reports:


### Reliable Channel API — General Availability
> *Note*: This needs more input from project
* fully qualified name: `ift-ts:dst:logos:2026q3-messaging-evaluation:reliable-channel-api`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description

TBD

#### Deliverables
- Code:
- Reports:


### Chat Reliability
> *Note*: This needs more input from project
* fully qualified name: `ift-ts:dst:logos:2026q3-messaging-evaluation:chat-reliability`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description

TBD

#### Deliverables
- Code:
- Reports:


### RLN on Logos Blockchain
> *Note*: This needs more input from project
* fully qualified name: `ift-ts:dst:logos:2026q3-messaging-evaluation:rln-logos-blockchain`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description

TBD

#### Deliverables
- Code:
- Reports:
