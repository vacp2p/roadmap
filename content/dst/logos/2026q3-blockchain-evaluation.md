---
title: Blockchain Evaluation
tags:
  - "2026q3"
  - "dst"
  - "logos"
draft: false
description: "Test Blockchain on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`ift-ts:dst:logos:2026q3-blockchain-evaluation`


## Description
> *Note*: This needs more input from project

Use real world testing,
theoretical analysis
and simulation
to determine and improve Blockchain's scaling properties.
Find the limits of Blockchain's capabilities
and measure them in different scenarios.

We will measure the real world speeds and latency of Blockchain' mixnet,
and what use cases it is therefore able to support.

The scope of this commitment depends on the Blockchain team
work and improvements, and it is subjected to change.

## Task List


### Devnets (recurring)
* fully qualified name: `ift-ts:dst:logos:2026q3-blockchain-evaluation:devnets`
* owner: Alberto
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description

Help blockchain team deploying nodes in the DST lab for each new release.
Help them measuring performance, memory, and other metrics that can be relevant, 
and document behaviors and findings.

#### Deliverables
- Code:
  - [vacp2p/10ksim#378](https://github.com/vacp2p/10ksim/pull/378) Files for logos-blokchain testnet
- Reports:


### Blend benchmarking
* fully qualified name: `ift-ts:dst:logos:2026q3-blockchain-evaluation:blendnet-benchmarking`
* owner: Mamoutou
* status: in progress (10%)
* start-date: 2026/08/04
* end-date: 2026/08/14

#### Description

Verifying the blend network timing assumptions.
Logos-blockchain has some very tight block dessimination budgets, if it turns out blend is much slower, 
they will need to increase block times.
This requires:

1. Distribution of how long it took for a block to propagate to nodes, the two datasets are:
    - block broadcast directly
    - block sent through blend and then broadcast

2. Frequency of reorgs observed at various block depths
    - For this, we have to extract the block tree, then pick the longest branch from the tree, treat that as canonical 
branch, then measure the length of every branch extending from this canonical branch

#### Deliverables
- Code:
- Reports:


### DA benchmarking
> *Note*: This was moved from previous quarter
> *Note*: This needs more input from project

* fully qualified name: `ift-ts:dst:logos:2026q3-blockchain-evaluation:da-benchmarking`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description

Measure Blockchain bandwidth usage in DA per node and entire network.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Code:
- Reports:
