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
* status: in progress (90%)
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
    - [vacp2p/dst-libp2p-test-node#29](https://github.com/vacp2p/dst-libp2p-test-node/pull/29) Move regression node to its own folder
    - [vacp2p/dst-libp2p-test-node#30](https://github.com/vacp2p/dst-libp2p-test-node/pull/30) Remove mix from regression node
    - [vacp2p/dst-libp2p-test-node#32](https://github.com/vacp2p/dst-libp2p-test-node/pull/32) Update node to match v2.0.0
    - [vacp2p/dst-libp2p-test-node#33](https://github.com/vacp2p/dst-libp2p-test-node/pull/33) Ping in regression node
    - [vacp2p/10ksim#298](https://github.com/vacp2p/10ksim/pull/298) Use kad-dht discovery for nimlibp2p regression mesh
    - [vacp2p/dst-libp2p-test-node#37](https://github.com/vacp2p/dst-libp2p-test-node/pull/37) Form regression mesh via kad-dht instead of static connectTo
- Reports:
    - [Nim-libp2p v2.0.0 regression testing report](https://app.notion.com/p/Nim-libp2p-v2-0-0-regression-testing-June-2026-WIP-3758f96fb65c806ba584fc93f72c3762)

    - Updated the v2.1.0 results report with the new numbers and plots: [Nim-libp2p v2.1.0 Regression Testing with KAD-DHT](https://app.notion.com/p/3828f96fb65c8058a5dcd7258b2032d4).

### nim-lsquic benchmark

* fully qualified name: `ift-ts:dst:ift:2026q2-libp2p-evaluation:nim-lsquic-benchmark`
* owner: Mamoutou
* status: done
* start-date: 2026/04/01
* end-date: 2026/05/12

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
    - [Github branch: mamoutou/disable-lsquic-pacing](https://github.com/vacp2p/dst-libp2p-test-node/tree/mamoutou/disable-lsquic-pacing) LSQUIC performance test scenarios
- Reports:
    - [LSQUIC RAW Benchmark in vaclab](https://www.notion.so/LSQUIC-RAW-Benchmark-in-vaclab-33c8f96fb65c802480baf186f3fa2fcf)
    - [NimLibp2p Random Delay Spikes when using QUIC](https://www.notion.so/NimLibp2p-Random-Delay-Spikes-when-using-QUIC-3478f96fb65c80e3af66fa0e999dc975)
    - [Experiments with Gossip parameters](https://www.notion.so/NimLibp2p-Random-Delay-Spikes-when-using-QUIC-3478f96fb65c80e3af66fa0e999dc975?source=copy_link#34f8f96fb65c80699751d64dcbc69ec7)
    - [Nim-libp2p Gossipsub Delivery Delay with LSQUIC Muxer](https://www.notion.so/Nim-libp2p-Gossipsub-Delivery-Delay-with-LSQUIC-Muxer-3558f96fb65c80cdb386dc4957b258e5)


### priority queues

* fully qualified name: `ift-ts:dst:ift:2026q2-libp2p-evaluation:priority-queues`
* owner: Mamoutou
* status: done
* start-date: 2026/05/05
* end-date: 2026/06/02

#### Description
Help validating new changes around priority queues and slow peer behavbior in nim-libp2p introduced in
https://github.com/vacp2p/nim-libp2p/pull/2269
https://github.com/vacp2p/nim-libp2p/pull/2241
Check that control message and subscriptions traffic remains reliable, Queues behave as expected, 
that the slow peer penalty is applied and decays overtime, and that the values selected for `slowPeerPenaltyWeight`, 
`slowPeerPenaltyThreshold` and `slowPeerPenaltyDecay` are not too aggressive, and that there are not regressions.


#### Deliverables
- Code:
    - [vacp2p/dst-libp2p-test-node#25](https://github.com/vacp2p/dst-libp2p-test-node/pull/25) Add Node and Publisher for Priority Queues tests
    - [vacp2p/pod-api-requester#7](https://github.com/vacp2p/pod-api-requester/pull/7) Enable generic load tests for GossipSub queues
- Reports:
    - [Notion: Gossipsub Priority Queues Test](https://www.notion.so/Gossipsub-Priority-Queues-Test-3638f96fb65c80f69df4de8b27508371)
    - [Grafana Dashboard DEV: Gossipsub Queues - ALL](https://grafana.lab.vac.dev/d/ma8p7g5/gossipsub-queues-all?orgId=1&from=2026-05-17T22:55:52.208Z&to=2026-05-17T23:49:05.560Z&timezone=browser&var-namespace=libp2p-lab&var-pod=nim-quic-1&var-pod=nim-quic-10&var-pod=nim-quic-70&var-muxer=$__all)
    - [Grafana: New panels for H/M/L queues analysis](https://grafana.lab.vac.dev/d/ma8p7g5/gossipsub-queues-all?orgId=1&from=2026-05-24T11:24:01.380Z&to=2026-05-24T13:31:46.583Z&timezone=browser&var-namespace=libp2p-lab&var-pod=$__all&var-muxer=$__all&var-query0=&var-peer_id=12D3KooWAPY95zCGogURoa1E7HkV35xNZMPM9apFsXkWJRpee4Gw)


### connection manager

* fully qualified name: `ift-ts:dst:ift:2026q2-libp2p-evaluation:connection-manager`
* owner: Alan
* status: done
* start-date: 2026/05/05
* end-date: 2026/05/26

#### Description
Switch builder now has an option for pruning behavior, and connection manager has ephemeral tag mechanisms. More info:
https://github.com/vacp2p/nim-libp2p/blob/master/examples/tutorial_5_connmanager.nim
Help validating cahnges of watermark mode as well as connection scoring mechanism.
Provide feedback if examples are not clear, and create scenarios to validate the behavior and impact of this new changes.


#### Deliverables
- Code:
    - [Github branch: connection manager test node](https://github.com/vacp2p/dst-libp2p-test-node/tree/alan/connmanager/nim-test-node/connmanager)
    - [Github branch: connection manager experiment framework](https://github.com/vacp2p/10ksim/tree/alan/connmanager)
    - [vacp2p/dst-libp2p-test-node#24](https://github.com/vacp2p/dst-libp2p-test-node/pull/24) Add Connection Manager Experiment Node
    - [vacp2p/10ksim#267](https://github.com/vacp2p/10ksim/pull/267) Connection Manager Experiment Deployment
    - [vacp2p/10ksim#266](https://github.com/vacp2p/10ksim/pull/266) Add Connection Manager Experiment Analysis
- Reports:
    - [Notion: connection manager planning report](https://www.notion.so/3588f96fb65c8174b5a6e85f966b3976)
    - [Notion: connection manager results report](https://www.notion.so/3598f96fb65c81ea9dacd68f0450b296)
    - Automatic post-run analysis added for deployment, analysis, and plot generation.

  
### lsquic and queues to framework

* fully qualified name: `ift-ts:dst:ift:2026q2-libp2p-evaluation:lsquic-and-queues-to-framework`
* owner: Mamoutou
* status: in progress (99%)
* start-date: 2026/05/25
* end-date: 2026/06/12

#### Description
Add experiments realized in `priority-queues` and `nim-lsquic-benchmark` to the python framework.


#### Deliverables
- Code:
    - [Mamoutou/add_gossip_priority_queues_experiments branch](https://github.com/vacp2p/10ksim/tree/Mamoutou/add_gossip_priority_queues_experiments) Add priority-queue experiments to 10ksim
- Reports:
