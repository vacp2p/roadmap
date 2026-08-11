---
title: Messaging Testing
tags:
  - "2026q3"
  - "qa"
  - "logos"
draft: false
description: Maintain and ensure the reliability of messaging tests.
---

`ift-ts:qa:logos:2026q3-messaging-testing`

## Description
Ensure the ongoing reliability of messaging by enhancing and maintaining existing testing frameworks.
This includes addressing regressions, adapting to changes in messaging components,
and applying minor improvements to keep the frameworks functional and effective.

## Task List

### Maintenance

* fully qualified name: `ift-ts:qa:logos:2026q3-messaging-testing:maintenance`
* owner: aya
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Ongoing maintenance of messaging testing frameworks.

#### Deliverables
- [logos-messaging/logos-delivery-interop-tests#206](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/206) chore(deps): bump urllib3 from 2.2.2 to 2.7.0
- [logos-messaging/logos-delivery-interop-tests#205](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/205) chore(deps): bump pytest from 8.0.2 to 9.0.3
- [logos-messaging/logos-delivery-interop-tests#204](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/204) chore(deps): bump idna from 3.7 to 3.15
- [logos-messaging/logos-delivery-interop-tests#210](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/210) update allure version to match the new pytest 9
- [logos-messaging/logos-delivery-interop-tests#201](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/201) chore(deps): bump setuptools from 70.0.0 to 83.0.0
- [logos-messaging/logos-delivery-interop-tests#211](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/211) chore(deps): bump virtualenv from 20.25.0 to 20.36.1
- [logos-messaging/logos-delivery-interop-tests#195](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/195) fix test s26
- [logos-messaging/logos-delivery#4003](https://github.com/logos-messaging/logos-delivery/issues/4003) portsShift double-applied: node advertises a port it isn't listening on
- [logos-messaging/logos-delivery-interop-tests#202](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/202) Fix CI issue [reports / flaky tests]
- [logos-messaging/logos-delivery-interop-tests#207](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/207) chore(deps): bump python-dotenv from 1.0.1 to 1.2.2

### RLN interaction with LEZ

* fully qualified name: `ift-ts:qa:logos:2026q3-messaging-testing:rln-lez-interaction`
* owner: roman
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Support QA for [RLN on Logos Blockchain](https://roadmap.logos.co/messaging/roadmap/milestones/2026-add-support-for-rln-on-lee).
Focus on library-level testing for the interaction between RLN and LEZ and report integration issues or missing coverage.

#### Deliverables
- PRs / Issues / Reports

### Reliable Channel API tests

* fully qualified name: `ift-ts:qa:logos:2026q3-messaging-testing:reliable-channel-api-tests`
* owner: aya
* status: in progress (90%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Support QA for [Reliable Channel API — General Availability](https://roadmap.logos.co/messaging/roadmap/milestones/2026-reliable-channel-api-general-availability).
Add API tests based on the [Reliable Channel API](https://github.com/logos-co/logos-lips/blob/master/docs/messaging/raw/reliable-channel-api.md), covering the main reliable-channel behavior exposed by the implementation.

#### Deliverables
- [logos-messaging/logos-delivery#4103](https://github.com/logos-messaging/logos-delivery/issues/4103) bug:SIGSEGV during node shutdown after restoring persisted reliable-channel state
- [logos-messaging/logos-delivery-interop-tests#200](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/200) remove some RC04 variants /add RC05/RC06
- [logos-messaging/logos-delivery#4065](https://github.com/logos-messaging/logos-delivery/issues/4065) bug: Channel still emits receive events after channel_close
- [logos-messaging/logos-delivery#4063](https://github.com/logos-messaging/logos-delivery/issues/4063) bug: Reliable Channel: received event reports receiver’s senderId
- [logos-messaging/logos-delivery-interop-tests#199](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/199) Channel api rc03 rc04 variants
- [logos-messaging/logos-delivery-interop-tests#197](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/197) Channel API RC01-RC02
- [logos-messaging/logos-delivery#4048](https://github.com/logos-messaging/logos-delivery/issues/4048) bug: Channel API A → B delivery does not produce a `channel_message_received` event on B
- [logos-messaging/logos-delivery-python-bindings#7](https://github.com/logos-messaging/logos-delivery-python-bindings/pull/7) Channel api wrappers

### Chat Developer Preview QA

* fully qualified name: `ift-ts:qa:logos:2026q3-messaging-testing:chat-developer-preview`
* owner: aya
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Support QA for [Chat — Developer Preview](https://roadmap.logos.co/messaging/roadmap/milestones/2026-chat-developer-preview).
Focus on library-level and module-level testing where feasible, including delivery module tests similar to the existing chat module coverage.

#### Deliverables
- PRs / Issues / Reports

### Messaging Sonda Tool extension

* fully qualified name: `ift-ts:qa:logos:2026q3-messaging-testing:sonda-extension`
* owner: aya
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Extend Sonda tool to allow more advanced testing scenarios for the Store protocol, then add new advanced tests.

#### Deliverables
- PRs and issues
