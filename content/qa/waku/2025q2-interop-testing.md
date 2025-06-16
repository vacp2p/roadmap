---
title: Waku Interop Testing
tags:
  - "2025q2"
  - "qa"
  - "waku"  
draft: false  
description: Maintain and ensure the reliability of Waku interop tests.
---

`vac:qa:waku:2025q2-interop-testing`

## Description
Maintain and ensure the continued reliability of the Waku interop testing framework. 
This includes addressing regressions, adapting to changes in `nwaku` and `gowaku`, 
and performing minor improvements to keep the framework functional and effective.

**Alignment with VAC Narratives:**

* The VAC QA team supports internal collaboration and efficiency
  by maintaining the quality and reliability of the Waku interop framework.

## Task List

### Maintenance

* fully qualified name: `vac:qa:waku:2025q2-interop-testing:maintenance`
* owner: fbarbu15
* status: done
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description
Ongoing maintenance of Waku interop tests. 
This includes updating tests for changes in `nwaku`,  `gowaku` or `js-waku`, addressing regressions, 
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.

#### Deliverables
- [Updated tests to no longer use deprecated pubsub flag](https://github.com/waku-org/waku-interop-tests/pull/111)
- [Enabled RLN tests](https://github.com/waku-org/waku-interop-tests/pull/112)
- [chore: add reconciliation metrics](https://github.com/waku-org/waku-interop-tests/pull/113)
- [test: Many tests fail on CI related to topics supscribtion](https://github.com/waku-org/nwaku/issues/3414)
- [chore: Remove go-waku from workflows](https://github.com/waku-org/waku-interop-tests/pull/117)
- [bug: node won’t start with RLN in on-chain dynamic mode 2](https://github.com/waku-org/nwaku/issues/3208)
- [bug: Raised issue related to relay fetch](https://github.com/waku-org/nwaku/issues/3444)
- [chore: Fixed failing tests](https://github.com/waku-org/waku-interop-tests/pull/121)
- [bug: node won't start with RLN in on-chain dynamic mode](https://github.com/waku-org/nwaku/issues/3208)

### js-waku filter hardening

* fully qualified name: `vac:qa:waku:2025q2-interop-testing:jswaku-filter-hardening`
* owner: fbarbu15
* status: in progress (30%)
* start-date: 2025/04/09
* end-date: 2025/04/30

#### Description
Moved to Q3! Could not be completed in Q2 because we were responsible for integrating status QA CCs into our team.
Harden js-waku filter protocol by adding more advanced tests like:
- Longevity test focused on sending/receiving messages continuously over a long duration (e.g., 6 hours)
- Sanity checks in terms of throughput of Waku messages of different sizes
- Sending/receiving thousands of messages in a short period of time

#### Deliverables
- [chore: add reliability tests package with longevity tests](https://github.com/waku-org/js-waku/pull/2361)
