---
title: Libp2p Evaluation
tags:
  - "2025q3"
  - "dst"
  - "vac"
draft: false
description: "Test libp2p on each new version or feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:vac:2025q3-libp2p-evaluation`


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

* fully qualified name: `vac:dst:vac:2025q3-libp2p-evaluation:regression-testing`
* owner: Alberto
* status: recurring
* start-date: 2025-07-01
* end-date: 2025-09-30

#### Description
Run different scenarios
and collect evidence and data
of libp2p's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
* Analysis done
  * [Notion: Nim-libp2p 1.12.0 (WIP)](https://www.notion.so/Nim-libp2p-v1-12-0-regression-testing-August-2025-WIP-2468f96fb65c8071b0a4dbf6f5807e94)
* Report published with all relevant details
* RFC's GitHub issue updated
  with links to the analysis and results.


### Universal connectivity

* fully qualified name: `vac:dst:vac:2025q3-libp2p-evaluation:universal-connectivity`
* owner: Alberto
* status: -
* start-date: -
* end-date: -

#### Description
Help p2p team running scenarios with universal connectivity app
and checking functionality with other libp2p implementations.

#### Deliverables
* PRs:
* Report:


### Evaluate Quic v0.2.9

* fully qualified name: `vac:dst:vac:2025q3-libp2p-evaluation:evaluate-quic-v0.2.9`
* owner: Alberto
* status: 50%
* start-date: 2025/07/30
* end-date: 2025/08/08

#### Description

Re-evaluate Quic in nimlibp2p with regression tests, to see if there is a difference with report [Notion: Nim-libp2p 1.11.0](https://www.notion.so/Nim-libp2p-v1-11-0-regression-testing-June-2025-2118f96fb65c802ca1b7c4233271ca26).

#### Deliverables
* PRs:
* Report:


### Mix re-evaluation

* fully qualified name: `vac:dst:vac:2025q3-libp2p-evaluation:mix-re-evaluation`
* owner: Alberto
* status: 0%
* start-date: 2025/07/30
* end-date: 2025/08/08

#### Description

Perform experiments with mix protocol current state to check:
- Message time propagation in and outside mix
- Confirm correct message routing
Compare results with the initial ones in [Notion: Mix report extended](https://www.notion.so/Nim-libp2p-Mix-May-2025-1f38f96fb65c800a8466f68472e799db?source=copy_link#2188f96fb65c8096a18ceba3d1c3fea8).

#### Deliverables
* PRs:
* Report:
