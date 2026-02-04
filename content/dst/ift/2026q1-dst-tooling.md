---
title: DST Tooling
tags:
  - "2026q1"
  - "dst"
  - "ift"
draft: false
description: "Creating tools that allow
DST to easily work with other IFT projects.
This includes functionalities such as deployments,
monitoring, analysis, and control of aforementioned software's."
---

`ift-ts:dst:ift:2026q1-dst-tooling`

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

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-tooling:general-tooling`
* owner: Pearson
* status: in progress (10%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Group of utilities that are added to the main repository.
Should be made general when possible.

#### Deliverables
- PRs:
  - [vacp2p/10ksim#193](https://github.com/vacp2p/10ksim/pull/193) Add Waku functionality for pod_api_requester
  - [vacp2p/pod-api-requester#4](https://github.com/vacp2p/pod-api-requester/pull/4) Add Waku router with endpoint "waku/relay"
  - [vacp2p/10ksim#191](https://github.com/vacp2p/10ksim/pull/191) Add pod_api_requester
  - [vacp2p/10ksim#190](https://github.com/vacp2p/10ksim/pull/190) Allow base_experiment.deploy to directly take result from builders
  - [vacp2p/10ksim#189](https://github.com/vacp2p/10ksim/pull/189) Builders for building pods
  - [vacp2p/10ksim#188](https://github.com/vacp2p/10ksim/pull/188) namespace fixes for builders
  - [vacp2p/pod-api-requester#3](https://github.com/vacp2p/pod-api-requester/pull/3) Return better error info
  - [vacp2p/10ksim#187](https://github.com/vacp2p/10ksim/pull/187) Reorganize repo by feature
  - [vacp2p/10ksim#186](https://github.com/vacp2p/10ksim/pull/186) Add namespace param to VictoriaReaderBuilder query
- Documents:

### Expand deployment - Waku

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-tooling:expand-deployment-waku`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Waku is planning to deliver specific binaries with encapsulated configurations to DST
Adjust deployment builders to support these new binaries and be able to run
specific experiments with them.

#### Deliverables
- PRs:
- Related Documents:

### Expand deployment - nim-libp2p

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-tooling:expand-deployment-nim-libp2p`
* owner: Pearson
* status: in progress (80%)
* start-date: 2026/01/12
* end-date: 2026/01/23

#### Description
Adjust deployment builders to support nim-libp2p.

#### Deliverables
- PRs:
- Related Documents:
  - [Example deployment dummy.py](https://github.com/vacp2p/10ksim/blob/17b03f2ed49c889f10859a16ccb805b1a04950c2/deployments/experiments/dummy.py#L152)

### Expand deployment - codex

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-tooling:expand-deployment-codex`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Adjust deployment builders to support codex.

#### Deliverables
- PRs:
- Related Documents:

### Expand deployment - nomos

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-tooling:expand-deployment-nomos`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Adjust deployment builders to support nomos.

#### Deliverables
- PRs:
- Related Documents:

### Expand deployment - anoncomms

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-tooling:expand-deployment-anoncomms`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Adjust deployment builders to support provided anoncomms binaries.

#### Deliverables
- PRs:
- Related Documents:
