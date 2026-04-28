---
title: Messaging Testing
tags:
  - "2026q2"
  - "qa"
  - "logos"
draft: false
description: Maintain and ensure the reliability of messaging tests.
---

`ift-ts:qa:logos:2026q2-messaging-testing`

## Description
Ensure the ongoing reliability of the messaging by enhancing and maintaining existing testing frameworks.
This includes addressing regressions, adapting to changes in messaging components,
and applying minor improvements to keep the frameworks functional and effective.
The Q2 LogosDelivery E2E effort is tracked under [logos-messaging/logos-delivery-interop-tests#163](https://github.com/logos-messaging/logos-delivery-interop-tests/issues/163).

## Task List

### Maintenance

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:maintenance`
* owner: aya/roman
* status: in progress (60%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Ongoing maintenance of messaging testing frameworks.

#### Deliverables
- PRs / Issues / Reports
- [logos-messaging/logos-delivery-interop-tests#164](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/164) chore: Refactor RLN tests
- [logos-messaging/logos-delivery-interop-tests#177](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/177) Fix for wrong url of reports

### Python bindings

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:python-bindings`
* owner: aya
* status: in progress (10%)
* start-date: 2026/04/06
* end-date: 2026/04/24

#### Description
Continue the Python bindings work for the messaging test framework, including wrapper coverage, validation of the bindings in real test scenarios, and completion of the integration steps needed by the test repository.

#### Deliverables
- [logos-messaging/logos-delivery-python-bindings#4](https://github.com/logos-messaging/logos-delivery-python-bindings/pull/4) merged

### E2E testing LogosDelivery preparation

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:e2e-testing-logosdelivery-preparation`
* owner: aya
* status: in progress (10%)
* start-date: 2026/04/02
* end-date: 2026/04/08

#### Description
Configure the test environment with the necessary helpers and APIs before initiating LogosDelivery E2E tests.
Prepare the setup needed to execute the upcoming Send API scenarios and identify missing pieces that should be requested from the developers.

#### Deliverables
- [logos-messaging/logos-delivery#3800](https://github.com/logos-messaging/logos-delivery/issues/3800)
- [logos-messaging/logos-delivery-interop-tests#159](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/159) Prepare LogosDelivery E2E coverage

### Main tests of LogosDelivery part 1

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:logosdelivery-main-tests-part1`
* owner: egor
* status: in progress (40%)
* start-date: 2026/04/09
* end-date: 2026/04/25

#### Description
Cover the following E2E test scenarios for the Send API: `S02`, `S06`, `S07`, `S08`, `S09`, `S10`, `S12`, `S14`, and `S15`.

#### Deliverables
- [logos-messaging/logos-delivery-interop-tests#173](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/173) Add S06 relay-only test and fix wrapper helpers

### Main tests of LogosDelivery part 2

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:logosdelivery-main-tests-part2`
* owner: aya
* status: in progress (40%)
* start-date: 2026/04/09
* end-date: 2026/04/25

#### Description
Cover the following E2E test scenarios for the Send API: `S17`, `S19`, `S20`, `S21`, `S22`, `S23`, `S24`, `S26`, `S30`, and `S31`.

#### Deliverables
- [logos-messaging/logos-delivery#3827](https://github.com/logos-messaging/logos-delivery/issues/3827) Schema mismatch

### Waku.test RLN smoke suite

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:waku-test-rln-smoke`
* owner: aya
* status: not started
* start-date: 2026/04/27
* end-date: 2026/05/15

#### Description
Implement a smoke suite targeting the external Waku fleet `waku.test` where RLN is enabled.
The suite should perform RLN registration as part of the test flow and validate the main messaging scenarios needed to confirm the environment is usable end to end.

#### Deliverables
- PRs with smoke tests for `waku.test`.
- Test report covering RLN registration flow, execution results, and observed environment limitations.

### Messaging Sonda Tool extension

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:sonda-extension`
* owner: aya
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Extend Sonda tool to allow more advanced testing scenarios for the Store protocol, then add new advanced tests.

#### Deliverables
- PRs and issues
