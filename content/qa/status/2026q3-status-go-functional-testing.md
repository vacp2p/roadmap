---
title: Status Go Functional Testing
tags:
  - "2026q3"
  - "qa"
  - "status"
draft: false
description: Enhance functional and e2e testing for status-go features by implementing tests using status-backend.
---

`ift-ts:qa:status:2026q3-status-go-functional-testing`

## Description
Continue modernizing the functional/e2e testing stack for status-go by cleaning up fixtures,
improving the Python SDK, and expanding test coverage as defined [here](https://github.com/orgs/status-im/projects/166/views/4).

## Task List

### Remove test classes inheritance to MessengerSteps

* fully qualified name: `ift-ts:qa:status:2026q3-status-go-functional-testing:7098`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Uncouple tests from MessengerSteps inheritance to simplify fixtures and setup.

#### Deliverables
- PRs and/or Issues

### Cleanup and simplify Python SDK

* fully qualified name: `ift-ts:qa:status:2026q3-status-go-functional-testing:7084`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Perform broader cleanup of the Python SDK to reduce flakiness and maintenance overhead.

#### Deliverables
- PRs and/or Issues

### Community Control Node Transfer Functional Test

* fully qualified name: `ift-ts:qa:status:2026q3-status-go-functional-testing:7132`
* owner: Aya
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Verify control node transfer procedures for communities.

#### Deliverables
- [status-im/status-go#7619](https://github.com/status-im/status-go/issues/7619) Community update is not applied after paired control-node container pause/unpause
- [status-im/status-go#7615](https://github.com/status-im/status-go/issues/7615) bug: LoginAccount does not restore custom networks, causing token-gated community events to be dropped

### Community-Level Permissions Functional Test

* fully qualified name: `ift-ts:qa:status:2026q3-status-go-functional-testing:7133`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Validate community-level permission rules and enforcement.

#### Deliverables
- PRs and/or Issues

### Community Channel-Level Permissions Functional Test

* fully qualified name: `ift-ts:qa:status:2026q3-status-go-functional-testing:7134`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Test permissions at the channel level within communities.

#### Deliverables
- PRs and/or Issues

### Expand nightly benchmarks

* fully qualified name: `ift-ts:qa:status:2026q3-status-go-functional-testing:7094`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Broaden nightly benchmark scenarios to track performance and regressions.

#### Deliverables
- PRs and/or Issues

### Implement local notifications functional tests

* fully qualified name: `ift-ts:qa:status:2026q3-status-go-functional-testing:7095`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Add functional tests for local notification flows.

#### Deliverables
- PRs and/or Issues

### Keycard PUK Functional Testing

* fully qualified name: `ift-ts:qa:status:2026q3-status-go-functional-testing:keycard-puk`
* owner: magnus
* status: done
* start-date: 2026/08/10
* end-date: 2026/08/18

#### Description
Restore Status Go functional coverage for Keycard PUK flows, pairings, and mobile bindings.

#### Deliverables
- [status-im/status-go#7697](https://github.com/status-im/status-go/pull/7697) test(functional): restore keycard coverage in cold-wallet vocabulary
- [status-im/status-go#7696](https://github.com/status-im/status-go/pull/7696) test(wallet): cover keycard pairings file and mobile bindings

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q3-status-go-functional-testing:maintenance`
* owner: Egor
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Ongoing maintenance of Status Functional tests.
This includes updating tests for changes in `status-go`, addressing regressions,
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.

#### Deliverables
- [status-im/status-go#7716](https://github.com/status-im/status-go/issues/7716) messages.new not emitted for incoming 1:1 message on a chat created by the node's own contact request
- [status-im/status-go#7372](https://github.com/status-im/status-go/pull/7372) test: add ENS release, visibility, and verification functional tests
- [status-im/status-go#7365](https://github.com/status-im/status-go/pull/7365) test: add ENS management and validity tests to functional tests
- [status-im/status-go#7715](https://github.com/status-im/status-go/pull/7715) test(functional): drop stale strict xfail on post-reconnect delivery
- [status-im/status-go#7712](https://github.com/status-im/status-go/issues/7712) protocol: ENS name from ContactUpdate is never queued for verification
- [status-im/status-go#7713](https://github.com/status-im/status-go/issues/7713) protocol: ENS name is never sent on standard message paths, so automatic ENS verification never triggers
- [status-im/status-go#7714](https://github.com/status-im/status-go/issues/7714) wallet router sends ENS release/setPubkey transactions to the token contract instead of the registrar/resolver
- [status-im/status-go#7669](https://github.com/status-im/status-go/pull/7669) test(functional): stabilize reliability node-pause tests
- [status-im/status-go#7668](https://github.com/status-im/status-go/issues/7668) Historic sync delayed by up to 20s after reconnect: offline no-op attempts arm the min-interval
- [status-im/status-go#7648](https://github.com/status-im/status-go/pull/7648) test(functional): resolve backend host ports after joining bridge network
- [status-im/status-go#7633](https://github.com/status-im/status-go/pull/7633) test(functional): fix reliability ipv4 port publishing and skip ip-change on ipv6
- [status-im/status-go#7584](https://github.com/status-im/status-go/pull/7584) test(functional): add #7132 community control node transfer test
- [status-im/status-go#7612](https://github.com/status-im/status-go/pull/7612) test: skip light-client tests that are flaky under #7393
- [status-im/status-go#7582](https://github.com/status-im/status-go/pull/7582) ci(tests): report coverage to Codecov on PRs
