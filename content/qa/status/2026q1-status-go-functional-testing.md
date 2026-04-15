---
title: Status Go Functional Testing
tags:
  - "2026q1"
  - "qa"
  - "status"  
draft: false  
description: Enhance functional and e2e testing for status-go features by implementing tests using status-backend.
---

`ift-ts:qa:status:2026q1-status-go-functional-testing`

## Description
Modernize the functional/e2e testing stack for status-go by cleaning up fixtures, 
improving the Python SDK, and expanding test coverage as defined [here](https://github.com/orgs/status-im/projects/166/views/4).

## Task List

### Remove direct usage of Anvil pre-generated accounts

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7086`
* owner: egor
* status: not started
* start-date: 2026/01/19
* end-date: 2026/01/30

#### Description
Eliminate hardcoded Anvil accounts and switch to dynamically managed identities.

#### Deliverables
- PRs and/or Issues

### Deploy contracts as part of `docker compose` pre-requisite

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7087`
* owner: egor
* status: done
* start-date: 2026/02/02
* end-date: 2026/02/13

#### Description
Bundle contract deployment into the compose bootstrap to simplify test setup.

#### Deliverables
- https://github.com/status-im/status-go/pull/7289

### Introduce `asyncio` into Python SDK

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7090`
* owner: egor
* status: done
* start-date: 2026/01/01
* end-date: 2026/01/16

#### Description
Add asyncio primitives to the Python SDK to enable async test flows.

#### Deliverables
- [test: simplify signal client](https://github.com/status-im/status-go/pull/7270)

### Simplify `SignalClient`

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7091`
* owner: egor
* status: done
* start-date: 2026/01/19
* end-date: 2026/01/30

#### Description
Reduce complexity in `SignalClient` to improve reliability and readability.

#### Deliverables
- [test: simplify signal client](https://github.com/status-im/status-go/pull/7270)

### Remove test classes inheritance to MessengerSteps

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7098`
* owner: egor
* status: not started
* start-date: 2026/02/02
* end-date: 2026/02/13

#### Description
Uncouple tests from MessengerSteps inheritance to simplify fixtures and setup.

#### Deliverables
- PRs and/or Issues

### Cleanup and simplify Python SDK

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7084`
* owner: egor
* status: done
* start-date: 2026/02/16
* end-date: 2026/02/27

#### Description
Perform broader cleanup of the Python SDK to reduce flakiness and maintenance overhead.

#### Deliverables
- PRs and/or Issues

### Community Owner Token Functional Test

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7128`
* owner: Roman
* status: done
* start-date: 2026/01/19
* end-date: 2026/03/24

#### Description
Validate ownership flows for community owner tokens.

#### Deliverables
- [status-im/status-go#7215](https://github.com/status-im/status-go/pull/7215) test: Token gated communities - TC 7128
- [status-im/status-go#7286](https://github.com/status-im/status-go/issues/7286) Owner token contract deployment reverts
- [status-im/status-go#7338](https://github.com/status-im/status-go/pull/7338) refactor: Add community token deployer overrides
- [status-im/status-go#7167](https://github.com/status-im/status-go/issues/7167) Community changes not visible to members after owner added the owner token

### Community Token Master Functional Test

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7129`
* owner: Roman
* status: done
* start-date: 2026/02/02
* end-date: 2026/02/13

#### Description
Cover token master responsibilities and guardrails.

#### Deliverables
- [status-im/status-go#7382](https://github.com/status-im/status-go/issues/7382) Unnecessary interaction with backend - storeDeployedOwnerToken
- [status-im/status-go#7258](https://github.com/status-im/status-go/issues/7258) Linux_arm64 is not supported by choosenim - docker build
- [status-im/status-go#7359](https://github.com/status-im/status-go/pull/7359) test: Token gated communities - TC 7129

### Community Admin Functional Test

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7130`
* owner: egor
* status: not started
* start-date: 2026/02/16
* end-date: 2026/02/27

#### Description
Ensure admin-level permissions behave as expected in communities.

#### Deliverables
- PRs and/or Issues

### Community Ownership Transfer Functional Test

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7131`
* owner: egor
* status: not started
* start-date: 2026/03/02
* end-date: 2026/03/13

#### Description
Test community ownership transfer workflows and state transitions.

#### Deliverables
- PRs and/or Issues

### Community Control Node Transfer Functional Test

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7132`
* owner: egor
* status: not started
* start-date: 2026/03/16
* end-date: 2026/03/27

#### Description
Verify control node transfer procedures for communities.

#### Deliverables
- PRs and/or Issues

### Community-Level Permissions Functional Test

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7133`
* owner: egor
* status: not started
* start-date: 2026/03/09
* end-date: 2026/03/20

#### Description
Validate community-level permission rules and enforcement.

#### Deliverables
- PRs and/or Issues

### Community Channel-Level Permissions Functional Test

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7134`
* owner: egor
* status: not started
* start-date: 2026/03/18
* end-date: 2026/03/28

#### Description
Test permissions at the channel level within communities.

#### Deliverables
- PRs and/or Issues

### Implement ENS functional tests

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7093`
* owner: egor
* status: done
* start-date: 2026/01/12
* end-date: 2026/03/31

#### Description
Create functional coverage for ENS integration paths.

#### Deliverables
- PRs and/or Issues

### Expand nightly benchmarks

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7094`
* owner: egor
* status: not started
* start-date: 2026/02/02
* end-date: 2026/02/13

#### Description
Broaden nightly benchmark scenarios to track performance and regressions.

#### Deliverables
- PRs and/or Issues

### Implement local notifications functional tests

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:7095`
* owner: egor
* status: not started
* start-date: 2026/02/23
* end-date: 2026/03/06

#### Description
Add functional tests for local notification flows.

#### Deliverables
- PRs and/or Issues

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q1-status-go-functional-testing:maintenance`
* owner: egor
* status: done
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Ongoing maintenance of Status Functional tests. 
This includes updating tests for changes in `status-go`, addressing regressions, 
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.

#### Deliverables
- [status-im/status-go#7376](https://github.com/status-im/status-go/pull/7376) Enable parallel backend teardown in functional tests
- [status-im/status-go#7358](https://github.com/status-im/status-go/pull/7358) Add ENS support to functional tests and implement ENS registration test
- [status-im/status-go#7352](https://github.com/status-im/status-go/pull/7352) remove direct usage of Anvil pre-generated accounts
- [status-im/status-go#7341](https://github.com/status-im/status-go/pull/7341) fix signal race conditions in send-all-then-verify-all patterns and rewrite `join_community` as robust state machine
- [status-im/status-go#7098](https://github.com/status-im/status-go/issues/7098) Remove test classes inheritance to MessengerSteps
- [status-im/status-go#7321](https://github.com/status-im/status-go/pull/7321) fix flaky tests on dev's PR
- [status-im/status-go#7289](https://github.com/status-im/status-go/pull/7289) deploy contracts as part of docker compose pre requesite
- [status-im/status-go#7270](https://github.com/status-im/status-go/pull/7270) simplify signal client/Introduce asyncio into Python SDK
- [status-im/status-go#7295](https://github.com/status-im/status-go/pull/7295)
