---
title: Anoncomms Evaluation
tags:
  - "2026q1"
  - "dst"
  - "anoncomms"
draft: false
description: "Test new anoncomms binaries on each new version 
or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`ift-ts:dst:anoncomms:2026q1-anoncomms-evaluation`

## Description
Test Anoncomms protocols on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of anoncomms projects and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

## Task list

### Mix
> *Note*: This needs more input from project

* fully qualified name: `ift-ts:dst:anoncomms:2026q1-anoncomms-evaluation:mix`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
TBD

#### Deliverables
- Reports:
- Related PRs if apply:

### KAD-DHT

* fully qualified name: `ift-ts:dst:anoncomms:2026q1-anoncomms-evaluation:kad-dht`
* owner: Alberto
* status: in progress (95%)
* start-date: 2026/02/17
* end-date: 2026/03/05

#### Description
Create a node in nimlibp2p to evaluate KAD-DHT.

#### Deliverables
- [dst-libp2p-test-node #kad-dht](https://github.com/vacp2p/dst-libp2p-test-node/tree/Alberto/kad-dht/nim-test-node/kad-dht)
- Added utility to connect to bootstrap nodes
- Added working FIND_NODE operations for normal nodes and probe nodes
- Added the option to use KAD-DHT or extended KAD-DHT to the node
- [Notion: KAD-DHT planning](https://www.notion.so/KAD-DHT-planning-3098f96fb65c801eb80ccc0b3f395eb6#3098f96fb65c80cdac81cb510c471e84)
- Created a new nimlibp2p node to evaluate KAD-DHT and other discovery mechanisms
- Code:
  - [Github branch: KAD-DHT](https://github.com/vacp2p/dst-libp2p-test-node/tree/Alberto/kad-dht)
- Reports:
