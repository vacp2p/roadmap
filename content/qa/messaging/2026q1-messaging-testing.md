---
title: Messaging Testing
tags:
  - "2026q1"
  - "qa"
  - "messaging"  
draft: false  
description: Maintain and ensure the reliability of messaging tests.
---

`ift-ts:qa:messaging:2026q1-messaging-testing`

## Description
Ensure the ongoing reliability of the messaging by enhancing and maintaining existing testing frameworks.  
This includes addressing regressions, adapting to changes in messaging components,  
and applying minor improvements to keep the frameworks functional and effective.

## Task List

### Messaging Extended E2E Network Conditions Tests

* fully qualified name: `ift-ts:qa:messaging:2026q1-messaging-testing:network-conditions`
* owner: aya
* status: in progress (90%)
* start date: 2026/01/01
* end date: 2026/02/15

#### Description
Extend messaging end-to-end tests with network condition scenarios (high latency, low bandwidth, packet loss) for up to 7 nodes.

#### Deliverables
- [logos-messaging/logos-messaging-interop-tests#151](https://github.com/logos-messaging/logos-messaging-interop-tests/pull/151) Network conditions tests
- [logos-messaging/logos-messaging-interop-tests#155](https://github.com/logos-messaging/logos-messaging-interop-tests/pull/155) Network conditions improvements

### Maintenance

* fully qualified name: `ift-ts:qa:messaging:2026q1-messaging-testing:maintenance`
* owner: aya
* status: in progress (10%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Ongoing maintenance of messaging testing frameworks. 

#### Deliverables
- PRs and issues
  - [logos-messaging/logos-messaging-interop-tests#156](https://github.com/logos-messaging/logos-messaging-interop-tests/pull/156) Lightpush and metrics test fixes


### Python bindings

* fully qualified name: `ift-ts:qa:messaging:2026q1-messaging-testing:python-bindings`
* owner: aya
* status: in progress (30%)
* start-date: 2026/02/16
* end-date: 2026/03/31

#### Description
Build and validate Python bindings usage in the messaging test framework, including wrapper coverage and integration steps for the test repo.

#### Deliverables
- PRs and issues

### Messaging Sonda Tool extension

* fully qualified name: `ift-ts:qa:messaging:2026q1-messaging-testing:sonda-extension`
* owner: aya
* status: not started
* start date: 2026/02/15
* end date: 2026/03/31

#### Description
Extend Sonda tool to allow more advanced testing scenarios for the Store protocol, then add new advanced tests.

#### Deliverables
- PRs and issues
