---
title: Logos Messaging Integration Testing
tags:
  - "2026q2"
  - "qa"
  - "logos"
draft: false
description: Validate Logos Messaging module integration inside Logos Core through the REST API exposed by Logos Messaging.
---

`ift-ts:qa:logos:2026q2-logos-messaging-integration`

## Description
Validate the integration of the Logos Messaging module inside the Logos Core platform through the REST API exposed by Logos Messaging.
The work covers building the test framework needed for this integration layer and implementing initial smoke coverage for one-to-one and group messaging flows.

## Task List

### Messaging integration testing framework

* fully qualified name: `ift-ts:qa:logos:2026q2-logos-messaging-integration:framework`
* owner: egor
* status: done
* start-date: 2026/04/06
* end-date: 2026/04/24

#### Description
- Create the testing framework for exercising Logos Messaging module integration inside Logos Core via the REST API.
- Define the environment setup, fixtures, helper utilities, and execution model needed to run integration scenarios reliably.
- Ensure the framework is structured so additional messaging scenarios can be added incrementally.

#### Deliverables
- [logos-messaging/logos-integration-test-framework#5](https://github.com/logos-messaging/logos-integration-test-framework/pull/5) Update `logoscore` dependency to track upstream `master` branch.
- [logos-messaging/logos-integration-test-framework#4](https://github.com/logos-messaging/logos-integration-test-framework/pull/4) Add support for Python 3.13 and 3.14 in CI workflows
- [logos-messaging/logos-integration-test-framework#3](https://github.com/logos-messaging/logos-integration-test-framework/pull/3) Add Apache 2.0 and MIT licenses to the repository, and update README
- [logos-co/logos-logoscore-py#2](https://github.com/logos-co/logos-logoscore-py/pull/2) Add support for attaching daemon containers to caller-managed Docker
- [logos-messaging/logos-integration-test-framework#2](https://github.com/logos-messaging/logos-integration-test-framework/pull/2) Update README.md to reflect updated repository URL

### One-to-one messaging

* fully qualified name: `ift-ts:qa:logos:2026q2-logos-messaging-integration:one-to-one-messaging`
* owner: egor
* status: done
* start-date: 2026/04/27
* end-date: 2026/05/15

#### Description
- Implement a smoke suite for one-to-one messaging using the new integration framework and the Logos Messaging REST API.
- Cover the main happy-path behaviors needed to validate end-to-end module integration inside Logos Core.

#### Deliverables
- PRs with one-to-one smoke tests.
- Test report with covered scenarios and identified gaps.
- [logos-co/logos-chat-module#24](https://github.com/logos-co/logos-chat-module/pull/24) Add two-user integration tests for chat-module

### Group chat

* fully qualified name: `ift-ts:qa:logos:2026q2-logos-messaging-integration:group-chat`
* owner: egor
* status: not started
* start-date: 2026/05/18
* end-date: 2026/06/05

#### Description
- Implement a smoke suite for group messaging using the same framework and REST API integration path.
- Validate the core group messaging flows needed to confirm the Logos Messaging module works correctly inside Logos Core.

#### Deliverables
- PRs with group messaging smoke tests.
- Test report with covered scenarios and follow-up issues.

### Logos Delivery module e2e testing and CI integration

* fully qualified name: `ift-ts:qa:logos:2026q2-logos-messaging-integration:delivery-module-e2e`
* owner: egor
* status: started
* start-date: 2026/06/16
* end-date: 2026/06/30

#### Description
- Build a Python e2e suite that boots logoscore daemons in Docker, loads the Logos Delivery module, and drives it over RPC.
- Exercise the plugin-load, codegen, RPC, and two-node network-delivery paths that the in-process C++ tests cannot cover.
- Integrate the suite into CI as a dedicated e2e job so delivery module integration is validated on every run.

#### Deliverables
- PRs with tests.
- Test report with covered scenarios and follow-up issues.
