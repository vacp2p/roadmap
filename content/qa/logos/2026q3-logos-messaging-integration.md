---
title: Logos Messaging Integration Testing
tags:
  - "2026q3"
  - "qa"
  - "logos"
draft: false
description: Validate Logos Messaging module integration inside Logos Core through the REST API exposed by Logos Messaging.
---

`ift-ts:qa:logos:2026q3-logos-messaging-integration`

## Description
Validate the integration of the Logos Messaging module inside the Logos Core platform through the REST API exposed by Logos Messaging.

## Task List

### Group chat

* fully qualified name: `ift-ts:qa:logos:2026q3-logos-messaging-integration:group-chat`
* owner: egor
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/10

#### Description
- Implement a smoke suite for group messaging using the same framework and REST API integration path.
- Validate the core group messaging flows needed to confirm the Logos Messaging module works correctly inside Logos Core.

#### Deliverables
- PRs with group messaging smoke tests.
- Test report with covered scenarios and follow-up issues.

### Logos Delivery module E2E testing and CI integration

* fully qualified name: `ift-ts:qa:logos:2026q3-logos-messaging-integration:delivery-module-e2e`
* owner: egor
* status: in progress (75%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Move the Delivery module E2E tests into the `logos-delivery-module` repository.
- Extend the Python E2E suite that drives the Delivery module over RPC and integrate it into CI.

#### Deliverables
- [logos-messaging/logos-delivery#4077](https://github.com/logos-messaging/logos-delivery/pull/4077) test(e2e): port remaining wrapper tests from the interop repo
- [logos-messaging/logos-delivery#4109](https://github.com/logos-messaging/logos-delivery/pull/4109) fix(persistency): own Persistency per node instead of a process-global singleton
- [logos-messaging/logos-delivery#4103](https://github.com/logos-messaging/logos-delivery/issues/4103) bug:SIGSEGV during node shutdown after restoring persisted reliable-channel state
- [logos-co/logos-delivery-module#51](https://github.com/logos-co/logos-delivery-module/pull/51) test: add Python e2e suite driving delivery_module over RPC
- [logos-messaging/logos-delivery#4052](https://github.com/logos-messaging/logos-delivery/pull/4052) ci: run docker subset of the API/e2e wrapper tests
- [logos-messaging/logos-delivery#4027](https://github.com/logos-messaging/logos-delivery/pull/4027) Add in-repo API/e2e test suite (tests-e2e)
- [logos-co/logos-delivery-module#58](https://github.com/logos-co/logos-delivery-module/issues/58) delivery_module `start` hangs depending on the build.
