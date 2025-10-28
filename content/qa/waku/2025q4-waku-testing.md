---
title: Waku Testing
tags:
  - "2025q4"
  - "qa"
  - "waku"  
draft: false  
description: Maintain and ensure the reliability of Waku tests.
---

`vac:qa:waku:2025q4-waku-testing`

## Description
Ensure the ongoing reliability of the Waku by enhancing and maintaining existing testing frameworks.  
This includes addressing regressions, adapting to changes in waku components,  
and applying minor improvements to keep the frameworks functional and effective.

**Alignment with VAC Narratives:**

* The VAC QA team enhances internal collaboration and efficiency 
  by maintaining the quality and reliability of the Waku testing frameworks.

## Task List

### Waku Canary Tool

* fully qualified name: `vac:qa:waku:2025q4-waku-testing:wakucanary`
* owner: aya
* status: not started
* start date: 2025/10/01
* end date: 2025/10/07

#### Description
Explore, fix, and improve the [Waku Canary tool](https://github.com/waku-org/nwaku/tree/master/apps/wakucanary) 
based on `nwaku` development requirements.  
The Q4 goal for this task is to retest open issues 
and close the current open PR with a full set of test scripts.

#### Deliverables
- PRs and issues

---

### 12H Longevity

* fully qualified name: `vac:qa:waku:2025q4-waku-testing:12hlongevity`
* owner: aya
* status: not started
* start date: 2025/10/08
* end date: 2025/10/15

#### Description
The Q4 goal for this task is to add the remaining tests to the 12-hour job, 
ensure there are no failures, and analyze CPU and memory performance.

#### Deliverables
- PRs and issues

---

### Waku Rendezvous Peer Discovery

* fully qualified name: `vac:qa:waku:2025q4-waku-testing:rendezvous`
* owner: aya
* status: in progress (20%)
* start date: 2025/10/16
* end date: 2025/10/26

#### Description
The Q4 goal for this task is to merge the current open PRs, 
add new tests, and ensure the existing open bugs are resolved.

#### Deliverables
- PRs and issues

---

### Waku Extended E2E Network Conditions Tests

* fully qualified name: `vac:qa:waku:2025q4-waku-testing:network-conditions`
* owner: aya
* status: not started
* start date: 2025/10/29
* end date: 2025/11/20

#### Description
Extend Waku end-to-end tests with network condition scenarios (high latency, low bandwidth, packet loss) for up to 7 nodes.

#### Deliverables
- PRs and issues

---

### Maintenance

* fully qualified name: `vac:qa:waku:2025q4-waku-testing:maintenance`
* owner: fbarbu15
* status: in progress(20%)
* start-date: 2025/10/01
* end-date: 2025/12/30

#### Description
Ongoing maintenance of Waku testing frameworks. 

#### Deliverables
- retested [fixed issue](https://github.com/waku-org/nwaku/issues/3572)
- [chore: fixes and adjustments](https://github.com/waku-org/waku-interop-tests/pull/139)

---

### Store sync updates

* fully qualified name: `vac:qa:waku:2025q4-waku-testing:store-sync-updates`
* owner: aya
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Update/enhance the waku store sync tests according to latest changes.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs and issues

---

### Waku Sonda Tool extension

* fully qualified name: `vac:qa:waku:2025q4-waku-testing:sonda-extension`
* owner: aya
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Extend Sonda tool to allow more advanced testing scenarios for the Store protocol, then add new advanced tests.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs and issues
