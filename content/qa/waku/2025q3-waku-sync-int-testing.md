---
title: Waku-sync Integration Testing
tags:
  - "2025q3"
  - "qa"
  - "waku"
draft: false
description: Continue Waku Sync Integration testing
---

`vac:qa:waku:2025q3-waku-sync-int-testing`

## Description

Continue Waku Sync Integration testing in `nwaku`. 

**Alignment with VAC Narratives:**

* The VAC QA team contributes to the robustness of the Waku protocol suite
  by ensuring correctness and completeness of newer components such as Waku Sync.
* By exposing edge cases and ensuring spec alignment,
  these tests enhance the RFC lifecycle and provide confidence to teams building on top of `nwaku`.

## Task List


### Waku Sync Integration Testing

* fully qualified name: `vac:qa:waku:2025q3-waku-sync-int-testing:integration`
* owner: aya
* status: in progress (50%)
* start-date: 2025/07/01
* end-date: 2025/08/15

#### Description

Develop integration tests that simulate full protocol interaction across multiple nodes. 
These tests will include real-world edge cases like:

- Multi-peer end-to-end synchronization
- Archive-driven message reconciliation
- Message transfer over delayed and lossy networks
- Handling cluster and shard mismatches

#### Deliverables
- bug: [“storedAt” column still referenced](https://github.com/waku-org/nwaku/issues/3479)
