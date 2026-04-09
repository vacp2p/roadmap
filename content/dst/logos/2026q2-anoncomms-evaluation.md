---
title: Anoncomms Evaluation
tags:
  - "2026q2"
  - "dst"
  - "logos"
draft: false
description: "Test new anoncomms binaries on each new version 
or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`ift-ts:dst:logos:2026q2-anoncomms-evaluation`

## Description
Test Anoncomms protocols on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of anoncomms projects and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

## Task list

### Closeness score
* fully qualified name: `ift-ts:dst:logos:2026q2-anoncomms-evaluation:closeness-score`
* owner: Alan
* status: not started
* start-date: 2026/04/09
* end-date: 2026/04/24

#### Description
Design a way to obtain closeness score from KAD-DHT experiments.
If needed, the Kad-dht script in [libp2p-test-node](https://github.com/vacp2p/dst-libp2p-test-node)
repository can be modified, but shouldn't be necessary. PeerID is already exposed in the script already, so we need:
1. Deploy the experiment.
2. After the experiment is finished, scrape the logs of all PODs, searching for every PeerID in the network.
3. In the scripts for the KAD-DHT analysis, add this score as part of the analysis ifself.
4. Provide a way of visually represent this score.
For more information, refer to [this document](https://www.notion.so/KAD-DHT-planning-3098f96fb65c801eb80ccc0b3f395eb6?source=copy_link#3318f96fb65c80d8bf26fe0316691b0a).

#### Deliverables
- Code:
- Reports:

### Mix
> *Note*: This needs more input from project

* fully qualified name: `ift-ts:dst:logos:2026q2-anoncomms-evaluation:mix`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
TBD

#### Deliverables
- Code:
- Reports:

### Service discovery
> *Note*: This needs more input from project

* fully qualified name: `ift-ts:dst:logos:2026q2-anoncomms-evaluation:service-discovery`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Evaluate service-discovery protocol. Compare it against KAD-DHT or any other request that comes from anoncomms team.

#### Deliverables
- Code:
- Reports:


### De-MLS
> *Note*: This needs more input from project

* fully qualified name: `ift-ts:dst:logos:2026q2-anoncomms-evaluation:de-mls`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
TBD

#### Deliverables
- Code:
- Reports:
