---
title: Waku Interop Testing
tags:
  - "2025q3"
  - "qa"
  - "waku"  
draft: false  
description: Maintain and ensure the reliability of Waku interop tests.
---

`vac:qa:waku:2025q3-interop-testing`

## Description
Maintain and ensure the continued reliability of the Waku interop testing framework. 
This includes addressing regressions, adapting to changes in `nwaku` and `gowaku`, 
and performing minor improvements to keep the framework functional and effective.

**Alignment with VAC Narratives:**

* The VAC QA team supports internal collaboration and efficiency
  by maintaining the quality and reliability of the Waku interop framework.

## Task List

### Maintenance

* fully qualified name: `vac:qa:waku:2025q3-interop-testing:maintenance`
* owner: fbarbu15
* status: in progress (10%)
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description
Ongoing maintenance of Waku interop tests. 
This includes updating tests for changes in `nwaku` or `js-waku`, addressing regressions, 
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.

#### Deliverables
- Adjust waku interop tests to latest [nwaku changes and fixes](https://github.com/waku-org/waku-interop-tests/pull/128)

### js-waku filter hardening

* fully qualified name: `vac:qa:waku:2025q3-interop-testing:jswaku-filter-hardening`
* owner: fbarbu15
* status: in progress (90%)
* start-date: 2025/07/01
* end-date: 2025/07/14

#### Description
Harden js-waku filter protocol by adding more advanced tests like:
- Sanity checks in terms of throughput of Waku messages of different sizes
- Sending/receiving thousands of messages in a short period of time

#### Deliverables
- [chore: add throughput reliability tests](https://github.com/waku-org/js-waku/pull/2444)
- [chore: network conditions tests](https://github.com/waku-org/js-waku/pull/2450)

### Lite protocol tester

* fully qualified name: `vac:qa:waku:2025q3-interop-testing:liteprotocoltester`
* owner: fbarbu15
* status: 
* start-date: 
* end-date: 

#### Description
Explore, fix and improve [waku lite protocol tester](https://github.com/waku-org/nwaku/tree/master/apps/liteprotocoltester) 
based on nwaku dev requirements

#### Deliverables
- PRs or Issues

### Waku cannary tool

* fully qualified name: `vac:qa:waku:2025q3-interop-testing:wakucannary`
* owner: aya
* status: in progress (30%)
* start-date: 2025/07/01
* end-date: 2025/07/30

#### Description
Explore, fix and improve [waku canary tool](https://github.com/waku-org/nwaku/tree/master/apps/wakucanary) 
based on nwaku dev requirements

#### Deliverables
- [bug: Canary app fails to connect to well-known Waku peers over all transports](https://github.com/waku-org/nwaku/issues/3518)

### 12H Longevity

* fully qualified name: `vac:qa:waku:2025q3-interop-testing:12hlongevity`
* owner: aya
* status: not started
* start-date: 2025/07/21
* end-date: 2025/08/15

#### Description
Create a github actions workflow that can run a 12 hour longevity test for waku go bindings.

#### Deliverables
- PR and CI run
