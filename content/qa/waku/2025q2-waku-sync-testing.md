---
title: Waku-sync Testing
tags:
  - "2025q2"
  - "qa"
  - "waku"
draft: false
description: Expand protocol test coverage for Waku Sync protocol in nwaku
---

`vac:qa:waku:2025q2-waku-sync-testing`

## Description

Expand protocol test coverage for the Waku Sync protocol in `nwaku`. 
Focus is placed on both unit testing of core logic (e.g., range reconciliation, fingerprinting, transfer encoding) 
and integration testing involving multi-peer synchronization, message archival, and protocol robustness.

**Alignment with VAC Narratives:**

* The VAC QA team contributes to the robustness of the Waku protocol suite
  by ensuring correctness and completeness of newer components such as Waku Sync.
* By exposing edge cases and ensuring spec alignment,
  these tests enhance the RFC lifecycle and provide confidence to teams building on top of `nwaku`.

## Task List

### Waku Sync Unit Testing

* fully qualified name: `vac:qa:waku:2025q2-waku-sync-testing:unit`
* owner: aya
* status: done
* start-date: 2025/04/08
* end-date: 2025/04/28

#### Description

Add test coverage by implementing unit tests for the Waku Sync protocol logic. 
These tests aim to validate internal mechanics such as:

- Reconciliation entrypoint handling
- Range fingerprinting and splitting
- Range type transitions
- Delta encoding/decoding
- Transfer dispatch and protobuf encoding
- Sync termination conditions

#### Deliverables
- Prepared [sheet](https://docs.google.com/spreadsheets/d/1Qj5LMyWR-ILA2wqd4eGe7j_V311QonZJ0LqnaWAJxMM/edit?gid=293767216#gid=293767216)  with missing coverage for unit tests  
- [test: Add comprehensive reconciliation unit-tests for Waku Store Sync](https://github.com/waku-org/nwaku/pull/3388)
- [test: Waku sync tests part2](https://github.com/waku-org/nwaku/pull/3397)
- [fix: fix failed sync test](https://github.com/waku-org/nwaku/pull/3464)

### Waku Sync Integration Testing

* fully qualified name: `vac:qa:waku:2025q2-waku-sync-testing:integration`
* owner: aya
* status: done
* start-date: 2025/04/29
* end-date: 2025/05/19

#### Description

Develop integration tests that simulate full protocol interaction across multiple nodes. 
These tests will include real-world edge cases like:

- Multi-peer end-to-end synchronization
- Archive-driven message reconciliation
- Message transfer over delayed and lossy networks
- Handling cluster and shard mismatches

#### Deliverables
- Issue [3471](https://github.com/waku-org/nwaku/issues/3471)
- Issue [3479](https://github.com/waku-org/nwaku/issues/3479)
