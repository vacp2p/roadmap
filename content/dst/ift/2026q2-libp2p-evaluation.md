---
title: Libp2p Evaluation
tags:
  - "2026q2"
  - "dst"
  - "ift"
draft: false
description: "Test libp2p on each new version or feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`ift-ts:dst:ift:2026q2-libp2p-evaluation`


## Description

Test libp2p on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Waku and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

The scope of this commitment depends on the P2P team
work and improvements, and it is subjected to change.

## Task list
> Schedule note: Dates reflect quarter bounds; update when actual timing is known.

### Regression testing (recurring)

* fully qualified name: `ift-ts:dst:ift:2026q2-libp2p-evaluation:regression-testing`
* owner: Pearson
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Run different scenarios
and collect evidence and data
of libp2p's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
- Code:
- Reports:


### nim-lsquic benchmark

* fully qualified name: `ift-ts:dst:ift:2026q2-libp2p-evaluation:nim-lsquic-benchmark`
* owner: Mamoutou
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Run the core part of quic in [nimlibp2p](https://github.com/vacp2p/nim-lsquic) in an isolated manner, instead
running the dst-test-node. We want to perform similar scenarios than the ones we are doing for regression experiments.
This means to set up a kubernetes deployment, and make the new scripts to have a similar behavior than the 
dst-test-node in terms of connections and throughput.
We need to study if the latencies reported by quic in the nim-libp2p regression experiments are caused by
this implementation or if there is another factor.

#### Deliverables
- Code:
- Reports: