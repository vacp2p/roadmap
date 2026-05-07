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
* status: in progress (20%)
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
    - [vacp2p/nim-libp2p#2336](https://github.com/vacp2p/nim-libp2p/issues/2336) TCP connection handling in nim-libp2p
    - [vacp2p/nim-libp2p#2335](https://github.com/vacp2p/nim-libp2p/issues/2335) CPU starvation issue in nim-libp2p
- Reports:


### nim-lsquic benchmark

* fully qualified name: `ift-ts:dst:ift:2026q2-libp2p-evaluation:nim-lsquic-benchmark`
* owner: Mamoutou
* status: in progress (85%)
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
    - [vacp2p/dst-nim-lsquic-test](https://github.com/vacp2p/dst-nim-lsquic-test)
    - [mamoutoudiarra/nim-libp2p-test:v1.1](https://hub.docker.com/repository/docker/mamoutoudiarra/nim-libp2p-test/tags/v1.1/sha256-8d71e4851734fdee37b6b87cda3f0d560336e4e05767c9d28db9640210f99942) Docker image with exposed GossipSub parameters
- Reports:
    - [LSQUIC RAW Benchmark in vaclab](https://www.notion.so/LSQUIC-RAW-Benchmark-in-vaclab-33c8f96fb65c802480baf186f3fa2fcf)
    - [NimLibp2p Random Delay Spikes when using QUIC](https://www.notion.so/NimLibp2p-Random-Delay-Spikes-when-using-QUIC-3478f96fb65c80e3af66fa0e999dc975)
    - [Experiments with Gossip parameters](https://www.notion.so/NimLibp2p-Random-Delay-Spikes-when-using-QUIC-3478f96fb65c80e3af66fa0e999dc975?source=copy_link#34f8f96fb65c80699751d64dcbc69ec7)
    - [Nim-libp2p Gossipsub Delivery Delay with LSQUIC Muxer](https://www.notion.so/Nim-libp2p-Gossipsub-Delivery-Delay-with-LSQUIC-Muxer-3558f96fb65c80cdb386dc4957b258e5)


### priority queues

* fully qualified name: `ift-ts:dst:ift:2026q2-libp2p-evaluation:priority-queues`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Help validating new changes around priority queues and slow peer behavbior in nim-libp2p introduced in
https://github.com/vacp2p/nim-libp2p/pull/2269
https://github.com/vacp2p/nim-libp2p/pull/2241
Check that control message and subscriptions traffic remains reliable, Queues behave as expected, 
that the slow peer penalty is applied and decays overtime, and that the values selected for `slowPeerPenaltyWeight`, 
`slowPeerPenaltyThreshold` and `slowPeerPenaltyDecay` are not too aggressive, and that there are not regressions.


#### Deliverables
- Code:
- Reports:


### connection manager

* fully qualified name: `ift-ts:dst:ift:2026q2-libp2p-evaluation:connection-manager`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Switch builder now has an option for pruning behavior, and connection manager has ephemeral tag mechanisms. More info:
https://github.com/vacp2p/nim-libp2p/blob/master/examples/tutorial_5_connmanager.nim
Help validating cahnges of watermark mode as well as connection scoring mechanism.
Provide feedback if examples are not clear, and create scenarios to validate the behavior and impact of this new changes.


#### Deliverables
- Code:
- Reports: