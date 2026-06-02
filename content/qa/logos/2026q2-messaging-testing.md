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
* status: done
* start-date: 2026/04/01
* end-date: 2026/05/26

#### Description
Ongoing maintenance of messaging testing frameworks.

#### Deliverables
- PRs / Issues / Reports
- [logos-messaging/logos-delivery-interop-tests#164](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/164) chore: Refactor RLN tests
- [logos-messaging/logos-delivery-interop-tests#177](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/177) Fix for wrong url of reports
- [logos-messaging/logos-delivery#3846](https://github.com/logos-messaging/logos-delivery/issues/3846) RLN registration not working with latest docker image
- [logos-messaging/logos-delivery-interop-tests#185](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/185) fix: Enable RLN registration for fleet tests
- [logos-messaging/logos-delivery-interop-tests#187](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/187) chore: Change fleet tests to run once a week


### Python bindings

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:python-bindings`
* owner: aya
* status: in progress (25%)
* start-date: 2026/04/06
* end-date: 2026/04/24

#### Description
Continue the Python bindings work for the messaging test framework, including wrapper coverage, validation of the bindings in real test scenarios, and completion of the integration steps needed by the test repository.

#### Deliverables
- [logos-messaging/logos-delivery-python-bindings#4](https://github.com/logos-messaging/logos-delivery-python-bindings/pull/4) merged

### E2E testing LogosDelivery preparation

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:e2e-testing-logosdelivery-preparation`
* owner: aya
* status: in progress (75%)
* start-date: 2026/04/02
* end-date: 2026/04/08

#### Description
Configure the test environment with the necessary helpers and APIs before initiating LogosDelivery E2E tests.
Prepare the setup needed to execute the upcoming Send API scenarios and identify missing pieces that should be requested from the developers.

#### Deliverables
- [logos-messaging/logos-delivery#3800](https://github.com/logos-messaging/logos-delivery/issues/3800)
- [logos-messaging/logos-delivery-interop-tests#159](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/159) Prepare LogosDelivery E2E coverage
- [logos-messaging/logos-integration-test-framework](https://github.com/logos-messaging/logos-integration-test-framework) Logos integration test framework
- [logos-messaging/logos-integration-test-framework#5](https://github.com/logos-messaging/logos-integration-test-framework/pull/5) Update `logoscore` dependency to track upstream `master` branch
- [logos-messaging/logos-integration-test-framework#4](https://github.com/logos-messaging/logos-integration-test-framework/pull/4) Add support for Python 3.13 and 3.14 in CI workflows
- [logos-messaging/logos-integration-test-framework#3](https://github.com/logos-messaging/logos-integration-test-framework/pull/3) Add Apache 2.0 and MIT licenses to the repository, and update README
- [logos-co/logos-chat-module#24](https://github.com/logos-co/logos-chat-module/pull/24) Add two-user integration tests for chat-module

### Main tests of LogosDelivery part 1

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:logosdelivery-main-tests-part1`
* owner: egor
* status: in progress (75%)
* start-date: 2026/04/09
* end-date: 2026/04/25

#### Description
Cover the following E2E test scenarios for the Send API: `S02`, `S06`, `S07`, `S08`, `S09`, `S10`, `S12`, `S14`, and `S15`.

#### Deliverables
- [logos-messaging/logos-delivery-interop-tests#173](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/173) Add S06 relay-only test and fix wrapper helpers
- [logos-messaging/logos-delivery-interop-tests#176](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/176) Add S07 and S10 send API tests with event invariants helper
- [logos-messaging/logos-delivery-interop-tests#178](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/178) Add S14 and S15 send API tests
- [logos-messaging/logos-delivery-interop-tests#174](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/174) Add S02/S12 send API tests and PR CI pipeline
- [logos-messaging/logos-delivery-interop-tests#180](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/180) Add relay-to-lightpush fallback integration tests

### Main tests of LogosDelivery part 2

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:logosdelivery-main-tests-part2`
* owner: aya
* status: done
* start-date: 2026/04/09
* end-date: 2026/05/19

#### Description
Cover the following E2E test scenarios for the Send API: `S17`, `S19`, `S20`, `S21`, `S22`, `S23`, `S24`, `S26`, `S30`, and `S31`.

#### Deliverables
- [logos-messaging/logos-delivery#3827](https://github.com/logos-messaging/logos-delivery/issues/3827) Schema mismatch
- [logos-messaging/logos-delivery#3847](https://github.com/logos-messaging/logos-delivery/issues/3847) Test failures when the lightpushnode option is not used
- [logos-messaging/logos-delivery-interop-tests#179](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/179) e2e_part2
- [logos-messaging/logos-delivery#3848](https://github.com/logos-messaging/logos-delivery/issues/3848) Store validation fails when the store peer joins after propagation

### E2E tests for remaining LogosDelivery scenarios

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:logosdelivery-e2e-tests-part3`
* owner: aya
* status: done
* start-date: 2026/05/05
* end-date: 2026/05/26

#### Description
Cover the remaining E2E test scenarios for the Send API beyond the 19 scenarios completed in parts 1 and 2: `S01`, `S03`, `S04`, `S05`, `S11`, `S13`, `S16`, `S18`, `S25`, `S27`, `S28`, and `S29`.

#### Deliverables
- PRs with Send API E2E tests for the remaining LogosDelivery scenarios.
- Test report covering execution results, failures, and any follow-up issues.
- [logos-messaging/logos-delivery#3863](https://github.com/logos-messaging/logos-delivery/issues/3863) S01 follow-up issue identified during remaining scenario coverage
- [logos-messaging/logos-delivery-interop-tests#181](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/181) e2e part3
- [logos-messaging/logos-delivery-interop-tests#183](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/183) E2e s13 s16
- [logos-messaging/logos-delivery-interop-tests#184](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/184) Fix failing tests
- [logos-messaging/logos-delivery#3873](https://github.com/logos-messaging/logos-delivery/issues/3873) S01 destroyed handle follow-up
- [logos-messaging/logos-delivery#3887](https://github.com/logos-messaging/logos-delivery/issues/3887) S16 lightpush peer appears later follow-up
- [Test Report Summary](https://www.notion.so/E2E-testing-report-of-new-LogosDelivery-API-send-3678f96fb65c80d9a8e1eb8e0e9dd2e1?source=copy_link)
- [Test Structure Reference](https://www.notion.so/Wrapper-Tests-Structure-Overview-3678f96fb65c80408aedcd8cae439f0e?source=copy_link)

### LogosDelivery bindings maintenance

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:logosdelivery-bindings-maintenance`
* owner: aya
* status: in progress (20%)
* start-date: 2026/05/19
* end-date: 2026/06/30

#### Description
Maintain LogosDelivery bindings test coverage, including port tests, failure analysis,
and coordination of findings with developers.

#### Deliverables
- [logos-messaging/logos-delivery-interop-tests#186](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/186) Add port tests and analyze current failures

### Waku.test RLN smoke suite

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:waku-test-rln-smoke`
* owner: roman
* status: done
* start-date: 2026/04/27
* end-date: 2026/05/12

#### Description
Implement a smoke suite targeting the external Waku fleet `waku.test` where RLN is enabled.
The suite should perform RLN registration as part of the test flow and validate the main messaging scenarios needed to confirm the environment is usable end to end.

#### Deliverables
- PRs with smoke tests for `waku.test`.
- Test report covering RLN registration flow, execution results, and observed environment limitations.
- [logos-messaging/logos-delivery-interop-tests#175](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/175) chore: Test waku fleet

### Nim FFI E2E tests

* fully qualified name: `ift-ts:qa:logos:2026q2-messaging-testing:nim-ffi-e2e-tests`
* owner: aya
* status: not started
* start-date: 2026/05/30
* end-date: 2026/06/15

#### Description
Add end-to-end tests for the nim-ffi library ([logos-messaging/nim-ffi#13](https://github.com/logos-messaging/nim-ffi/issues/13)).
Tests are written in C/C++ and consume the built Nim library through the generated glue code.
The suite exercises the various types and structures passed over the FFI boundary.

#### Deliverables
- PRs with C/C++ E2E tests covering the generated glue code for the nim-ffi library.

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
