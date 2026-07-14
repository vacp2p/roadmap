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
* status: in progress (10%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Ongoing maintenance of messaging testing frameworks.

#### Deliverables
- [logos-messaging/logos-delivery-interop-tests#195](https://github.com/logos-messaging/logos-delivery-interop-tests/pull/195) fix test s26
- [logos-messaging/logos-delivery#4003](https://github.com/logos-messaging/logos-delivery/issues/4003) portsShift double-applied: node advertises a port it isn't listening on

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
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Support QA for [Reliable Channel API — General Availability](https://roadmap.logos.co/messaging/roadmap/milestones/2026-reliable-channel-api-general-availability).
Add API tests based on the [Reliable Channel API](https://github.com/logos-co/logos-lips/blob/master/docs/messaging/raw/reliable-channel-api.md), covering the main reliable-channel behavior exposed by the implementation.

#### Deliverables
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
