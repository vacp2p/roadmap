---
title: DST Tooling
tags:
  - "2026q3"
  - "dst"
  - "ift"
draft: false
description: "Creating tools that allow
DST to easily work with other IFT projects.
This includes functionalities such as deployments,
monitoring, analysis, and control of aforementioned software's."
---

`ift-ts:dst:ift:2026q3-dst-tooling`

## Description

We will create tools to help DST efficiency.
These tools can be composed of utilities for Kubernetes,
or any other kind that fits the necessities of DST and other projects.
As projects might share common necessities, this tasks will be considered
as a scaffold for DST tools, adapting the tools for each project if it needs.
The primary focus will be on adapting the necessities of the Waku team for
the log parser tool. This will comprise retrieving information from a given
message id, history of discovered peers, subscriptions, while having good 
performance and supportability.
Additionally, the project will define workflows that facilitate the creation
and execution of specialized scenarios. These scenarios will assist in 
the analysis of libp2p and Gossipsub, supporting studies focused on 
adversarial conditions and control message behavior.


## Task list

### General tooling (recurring)

* fully qualified name: `ift-ts:dst:ift:2026q3-dst-tooling:general-tooling`
* owner: Mamoutou/Alan
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Group of utilities that are added to the main repository.
Should be made general when possible.

#### Deliverables
- Code:
  - [vacp2p/10ksim#308](https://github.com/vacp2p/10ksim/pull/308) Post run analysis
  - [vacp2p/10ksim#346](https://github.com/vacp2p/10ksim/pull/346) Kad-dht regression sweep across versions and muxers
  - [vacp2p/10ksim#354](https://github.com/vacp2p/10ksim/pull/354) Fix command add_args
  - [vacp2p/vaclab-2#42](https://github.com/vacp2p/vaclab-2/pull/42) Add namespace variable for nWaku
  - [vacp2p/10ksim#344](https://github.com/vacp2p/10ksim/pull/344) WakuExperiment: updates
  - [vacp2p/10ksim#369](https://github.com/vacp2p/10ksim/pull/369) Use local rng for parametrized logoscore test
  - [vacp2p/10ksim#365](https://github.com/vacp2p/10ksim/pull/365) Refactor metrics plotting to use grouped data paths
  - [vacp2p/10ksim#363](https://github.com/vacp2p/10ksim/pull/363) Allow non-primitive objects in ExpConfig CLI args
  - [vacp2p/10ksim#367](https://github.com/vacp2p/10ksim/pull/367) Add extra values to metadata for time intervals
- Reports:

### Dashboard improvements

* fully qualified name: `ift-ts:dst:ift:2026q3-dst-tooling:dashboard-improvements`
* owner: Mamoutou
* status: in progress (70%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Improve first approach delivered in Q2.

#### Deliverables
- Code:
  - [vacp2p/10ksim#376](https://github.com/vacp2p/10ksim/pull/376) Add Vaclab Nodes Resources and Topology to DST_DASHBOARD
- Reports:


### Slow proof analysis

* fully qualified name: `ift-ts:dst:ift:2026q3-dst-tooling:slow-proof-analysis`
* owner: Mamoutou
* status: in progress (92%)
* start-date: 2026/07/09
* end-date: 2026/09/24

#### Description
RLN proofs in logos-delivery and blend proofs in logos-blockchain takes a suspiciously high amount of time.
Coordinate with CCs to get what are the estimations that should work, and check why in the lab these times are sometimes
x6 or even higher. 

#### Deliverables
- Code:
  - [vacp2p/vaclab-2#47](https://github.com/vacp2p/vaclab-2/pull/47) Add RLN Proof Generation Time Panels
- Reports:
  - [High RLN Proof Generation Time Debugging](https://app.notion.com/p/High-RLN-Proof-Generation-Time-Debugging-3a08f96fb65c80e197a8dbe833df3097)
  - Enabled CPU pinning on `metal-01` and measured an average RLN proof-generation time of 195 ms, about 31% lower than without pinning.
  - Enabled static CPU Manager across VacLab nodes and CPU pinning on the running mix nodes.
  - [RLN generation and verification Grafana panels](https://grafana.lab.vac.dev/goto/cfve43sjymb5sb?orgId=1)
  - Found RLN proof-generation latency to be CPU-frequency-bound; node-02's higher frequency reduced p95 to about 242 ms versus about 400 ms on other nodes.
