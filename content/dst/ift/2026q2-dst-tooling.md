---
title: DST Tooling
tags:
  - "2026q2"
  - "dst"
  - "ift"
draft: false
description: "Creating tools that allow
DST to easily work with other IFT projects.
This includes functionalities such as deployments,
monitoring, analysis, and control of aforementioned software's."
---

`ift-ts:dst:ift:2026q2-dst-tooling`

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

* fully qualified name: `ift-ts:dst:ift:2026q2-dst-tooling:general-tooling`
* owner: Pearson
* status: in progress (10%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Group of utilities that are added to the main repository.
Should be made general when possible.

#### Deliverables
- Code:
- Reports:
- Other:
  - Fixed `zerotesting-store` so it runs on k8s


### Dashboard

* fully qualified name: `ift-ts:dst:ift:2026q2-dst-tooling:dashboard`
* owner: Mamoutou
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Present DST reports automatically in a dashboard for other CCs.

#### Deliverables
- Code:
- Reports:


### Shadow

* fully qualified name: `ift-ts:dst:ift:2026q2-dst-tooling:shadow`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Shadow simulator is hardcoded at the moment in dst-libp2p-test-node for the nim version.
We want to abstract builders from the main repository to take into account shadow.
We want to be able to launch experiments on K8s, deciding if we want to use a realistic environment, or
shadow.
This needs to take into account further data analysis of the main pipeline. Can probably be split into
subtasks.

#### Deliverables
- Code:
- Reports: