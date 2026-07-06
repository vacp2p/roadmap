---
title: Status Go Functional Testing
tags:
  - "2026q2"
  - "qa"
  - "status"
draft: false
description: Enhance functional and e2e testing for status-go features by implementing tests using status-backend.
---

`ift-ts:qa:status:2026q2-status-go-functional-testing`

## Description
Modernize the functional/e2e testing stack for status-go by cleaning up fixtures,
improving the Python SDK, and expanding test coverage as defined [here](https://github.com/orgs/status-im/projects/166/views/4).

## Task List

### Remove test classes inheritance to MessengerSteps

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7098`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Uncouple tests from MessengerSteps inheritance to simplify fixtures and setup.

#### Deliverables
- PRs and/or Issues

### Cleanup and simplify Python SDK

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7084`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Perform broader cleanup of the Python SDK to reduce flakiness and maintenance overhead.

#### Deliverables
- PRs and/or Issues

### Community Admin Functional Test

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7130`
* owner: Nastya
* status: done
* start-date: 2026/04/01
* end-date: 2026/06/02

#### Description
Ensure admin-level permissions behave as expected in communities.

#### Deliverables
- [status-im/status-app#20584](https://github.com/status-im/status-app/issues/20584) Can't get Admin privileges even UI says I am admin in community
- [status-im/status-go#7454](https://github.com/status-im/status-go/pull/7454) test: add test to check admin functionality in community

### Community Ownership Transfer Functional Test

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7131`
* owner: Aya
* status: done
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Test community ownership transfer workflows and state transitions.

#### Deliverables
- PRs and/or Issues

### Community Control Node Transfer Functional Test

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7132`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Verify control node transfer procedures for communities.

#### Deliverables
- PRs and/or Issues

### Community-Level Permissions Functional Test

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7133`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Validate community-level permission rules and enforcement.

#### Deliverables
- PRs and/or Issues

### Community Channel-Level Permissions Functional Test

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7134`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Test permissions at the channel level within communities.

#### Deliverables
- PRs and/or Issues

### Expand nightly benchmarks

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7094`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Broaden nightly benchmark scenarios to track performance and regressions.

#### Deliverables
- PRs and/or Issues

### Implement local notifications functional tests

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7095`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Add functional tests for local notification flows.

#### Deliverables
- PRs and/or Issues

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:maintenance`
* owner: Egor
* status: done
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Ongoing maintenance of Status Functional tests.
This includes updating tests for changes in `status-go`, addressing regressions,
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.

#### Deliverables
- PRs / Issues / Reports

### Add force reevaluation functionality for community tests

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7481`
* owner: Nastya
* status: done
* start-date: 2026/04/01
* end-date: 2026/06/02

#### Description
Add functionality to use force reevalutaion for community permission check

#### Deliverables
- [status-im/status-go#7481](https://github.com/status-im/status-go/issues/7481) Implement force reevaluation flag for functional tests
- [status-im/status-go#7488](https://github.com/status-im/status-go/pull/7488) Use force reevaluation for community tests

### Stabilise tests for light client

* fully qualified name: `ift-ts:qa:status:2026q2-status-go-functional-testing:7515`
* owner: Nastya
* status: done
* start-date: 2026/04/01
* end-date: 2026/06/09

#### Description
Make tests with light client stable

#### Deliverables
- [status-im/status-go#7519](https://github.com/status-im/status-go/pull/7519) Add small test improvements for light-client stability
