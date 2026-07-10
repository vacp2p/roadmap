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
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Group of utilities that are added to the main repository.
Should be made general when possible.

#### Deliverables
- Code:
- Reports:

### Dashboard improvements

* fully qualified name: `ift-ts:dst:ift:2026q3-dst-tooling:dashboard-improvements`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Improve first approach delivered in Q2.

#### Deliverables
- Code:
- Reports:


### Slow proof analysis

* fully qualified name: `ift-ts:dst:ift:2026q3-dst-tooling:slow-proof-analysis`
* owner: Mamoutou
* status: not started
* start-date: 2026/07/09
* end-date: 2026/09/24

#### Description
RLN proofs in logos-delivery and blend proofs in logos-blockchain takes a suspiciously high amount of time.
Coordinate with CCs to get what are the estimations that should work, and check why in the lab these times are sometimes
x6 or even higher. 

#### Deliverables
- Code:
- Reports: