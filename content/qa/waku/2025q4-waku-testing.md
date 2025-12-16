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
* owner: Florin
* status: in progress (80%)
* start-date: 2025/10/01
* end-date: 2025/12/30

#### Description
Ongoing maintenance of Waku testing frameworks. 

#### Deliverables
- [logos-messaging/logos-messaging-interop-tests#145](https://github.com/logos-messaging/logos-messaging-interop-tests/pull/145) chore/repo rename
- [logos-messaging/logos-messaging-interop-tests#144](https://github.com/logos-messaging/logos-messaging-interop-tests/pull/144) maint/postgres payload size bytes
- [logos-messaging/logos-messaging-interop-tests#143](https://github.com/logos-messaging/logos-messaging-interop-tests/pull/143) fix allure report link
- [chore: admin tests fix](https://github.com/waku-org/waku-interop-tests/pull/140)
- retested [fixed issue](https://github.com/waku-org/nwaku/issues/3572)
- [chore: fixes and adjustments](https://github.com/waku-org/waku-interop-tests/pull/139)
- Validated `harbor.status.im/wakuorg/nwaku:v0.37.0-rc.4` across interop regression suite.

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
