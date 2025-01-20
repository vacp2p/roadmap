---
title: Codex Base Capacity
tags:
  - "2025q1"
  - "dst"
  - "codex"
draft: false
description: "Provide base capacity for Codex and keep it reliable.
Study its behaviour in the process of supporting it."
---

`vac:dst:codex:2025q1-codex-base-capacity`


## Description

We will ensure Codex
has a reliable storage base capacity
and study its behavior during support.
To enable scalability,
we will test Codex with large deployments
of 100TB+ and various setups.


### Background


### Narratives

Our efforts will contribute
to the Conduit of Expertise narrative
by accelerating Codex development
through real-world testing,
improving the RFC process
with performance insights,
and simplifying post-mortem analysis
of RFC outcomes to enhance future improvements.
Additionally, 
we will support the Premier Research narrative
by helping Codex build 
a stable foundation
for further research 
and innovative use cases.

### Additional info

This commitment has been rescheduled
from 2024Q4 to 2025Q1
due to unforeseen circumstances, 
including an extended sick leave of a CC.


## Task List

### Production Quality Base Capacity

* fully qualified name: `vac:dst:codex:2025q1-codex-base-capacity:deploy-base-capacity`
* owner: Wings
* status: 100%
* start-date: 2025/01/01
* end-date: 2025/01/31

#### Description

We have deployed
a large set of base capacity
to the Codex testnet.
Now we need to keep it online,
stable and prevented from losing data where possible.

It consists of 50x nodes
with 10xTB of data each for now.

#### Deliverables

<!--
* Helm chart adapted to Vaclab and used to deploy the nodes.
* 50x nodes running and adopted into the testnet.
-->
* Downloads/uploads tested and working for at least 3 selected nodes.
* 🚧 Ongoing monitoring (not a one time thing)
* ✅ 500TB of overall capacity provided to the network
