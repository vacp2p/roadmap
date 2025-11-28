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

`vac:dst:ift:2026q1-dst-tooling`

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

* fully qualified name: `vac:dst:ift:2026q1-dst-tooling:general-tooling`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Group of utilities that are added to the main repository.
Should be made general when possible.

#### Deliverables
- PRs:
- Documents:

### Expand deployment - Waku

* fully qualified name: `vac:dst:ift:2026q1-dst-tooling:expand-deployment-waku`
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

* fully qualified name: `vac:dst:ift:2026q1-dst-tooling:expand-deployment-nim-libp2p`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Adjust deployment builders to support nim-libp2p.

#### Deliverables
- PRs:
- Related Documents:

### Expand deployment - codex

* fully qualified name: `vac:dst:ift:2026q1-dst-tooling:expand-deployment-codex`
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

* fully qualified name: `vac:dst:ift:2026q1-dst-tooling:expand-deployment-nomos`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Adjust deployment builders to support nomos.

#### Deliverables
- PRs:
- Related Documents:

### Expand deployment - annoncoms

* fully qualified name: `vac:dst:ift:2026q1-dst-tooling:expand-deployment-annoncoms`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Adjust deployment builders to support provided annoncoms binaries.

#### Deliverables
- PRs:
- Related Documents:
