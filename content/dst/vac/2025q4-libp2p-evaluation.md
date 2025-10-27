---
title: Libp2p Evaluation
tags:
  - "2025q4"
  - "dst"
  - "vac"
draft: false
description: "Test libp2p on each new version or feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:vac:2025q4-libp2p-evaluation`


## Description

Test libp2p on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Waku and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

The scope of this commitment depends on the P2P team
work and improvements, and it is subjected to change.

### Background

We want to learn specific, actionable information
about libp2p's behaviour
and how it is evolving over time
with each new release
and with each thing we are specifically asked to check and test.

We will use a combination of real world testing,
theoretical analysis and simulation
to determine and measure the success,
side effects and other factors of libp2p and its evolution.

### Narrative

We will support the Conduit of Expertise narrative directly
by analysing and evaluating new libp2p releases and their features,
both with regards to features they have today
and with regards to how that compares to past behaviour.

Additionally, these efforts will contribute
to the Premier Research destination narrative by
improving and strengthening our relationship with the libp2p team
and thus increasing the reach and influence of the IFT,
and improving the chances
that we successfully grow our ecosystem's products and collaborations
and especially those we want to work with externally.

### Additional info

## Task list

### Regression testing (recurring)

* fully qualified name: `vac:dst:vac:2025q4-libp2p-evaluation:regression-testing`
* owner: Alberto
* status: recurring
* start-date: 2025-10-01
* end-date: 2025-12-31

#### Description
Run different scenarios
and collect evidence and data
of libp2p's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
* Analysis:
  * [Notion: Nim-libp2p 1.14.0 Report](https://www.notion.so/Nim-libp2p-v1-14-0-regression-testing-October-2025-28d8f96fb65c803ba789ccdb73753cab)


### Universal connectivity

* fully qualified name: `vac:dst:vac:2025q4-libp2p-evaluation:universal-connectivity`
* owner: Alberto
* status: -
* start-date:
* end-date:

#### Description
Help p2p team running scenarios with universal connectivity app
and checking functionality with other libp2p implementations.

#### Deliverables
* PRs:
* Report:


### Quic-vs-tcp

* fully qualified name: `vac:dst:vac:2025q4-libp2p-evaluation:quic-vs-tcp`
* owner: TBD
* status: 0%
* start-date:
* end-date:

#### Description

Perform a comparison between nim-libp2p using quic and waku using mplex and yamux.

#### Deliverables
- Reports:
- Related PRs if apply:

### Interop framework

* fully qualified name: `vac:dst:vac:2025q4-libp2p-evaluation:interop-framework`
* owner: TBD
* status: 0%
* start-date:
* end-date:

#### Description

Perform a comparison between nim-libp2p using quic and waku using mplex and yamux.

#### Deliverables
- Reports:
- Related PRs if apply:


### Mix in nim-libp2p node

* fully qualified name: `vac:dst:ift:2025q4-libp2p-evaluation:mix-in-nim-libp2p-node`
* owner: Farooq
* status: 90%
* start-date: 2025/10/06
* end-date: 2025/10/17

#### Description
After refactor was done in `vac:dst:ift:2025q3-dst-tooling:nim-libp2p-dst-node-refactor`,
include mix to the configuration options of the node.

#### Deliverables
- PRs:
  - [Github PR: mix-integeration #7](https://github.com/vacp2p/dst-libp2p-test-node/pull/7)
- Related Documents:

### Go-libp2p node

* fully qualified name: `vac:dst:ift:2025q4-libp2p-evaluation:go-libp2p-node`
* owner: Farooq
* status: 100%
* start-date: 2025/10/06
* end-date: 2025/10/24

#### Description
Include go-libp2p node to the [dst node repository](https://github.com/vacp2p/dst-libp2p-test-node).
It should behave the same than the nim-libp2p node.
Create a small deployment with both implementations using the same publisher.
Report results of a single scenario (fixed parameters) using K8s and shadow.

#### Deliverables
- PRs:
  - [Github PR: go-libp2p-test-node #8](https://github.com/vacp2p/dst-libp2p-test-node/pull/8)
- Related Documents:

### Webtransport ?

### KAD-DHT ?

