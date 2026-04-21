---
title: Status QA Mobile
tags:
  - "2026q2"
  - "qa"
  - "status"
draft: false
description: Status QA Mobile
---

`ift-ts:qa:status:2026q2-status-qa-mobile`

## Description
Close critical mobile test coverage gaps in group chat, communities, and device sync, while expanding platform support.

Areas for Q2:
- Group chat test stabilization and landing, carried from Q1
- 1x1 messaging completion to desktop critical parity
- Communities test groundwork using backend API for environment setup
- Device sync onboarding using backend API for sync code generation
- iOS coverage expansion

Current Coverage (End of Q1 2026):
- 13 test files, 32 test methods
- 52% of desktop critical assertions matched, 46/89
- Zero-coverage areas: group chat, communities, device sync
- iOS POC validated with a single onboarding test
- Multi-device infrastructure mature, with 2-device and 3-device setups validated
- Nightly and per-PR CI checks operational

Platform Constraints Identified in Q1:
- Community creation is desktop-only, `createCommunityEnabled: !isMobile`
- Sync code generation is desktop-only, `SetupSyncingPopup` is a desktop modal
- Ownership transfer and control node management are desktop-only
- Backend API needs to be investigated as an alternative for test environment setup

## Task List

### Messaging group chat

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:test-messaging-group`
* owner: magnus
* status: not started
* start-date: 2026/04/01
* end-date: 2026/05/15

#### Description
Stabilize and land 3-device group chat tests.
The tests were built in Q1 but reverted because of flakiness; the multi-device infrastructure is now ready and group chat creation is fully available on mobile.

#### Deliverables
- Activity Center and group chat page objects
- `test_messaging_group_chat.py` with 3-device execution
- Member management, link preview, and leave-chat assertions validated
- 11 assertions matching desktop critical parity
- First draft of the 3-device group chat suite covering 7 tests

### Messaging 1x1 completion

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:test-messaging-1x1`
* owner: magnus
* status: in progress (10%)
* start-date: 2026/04/01
* end-date: 2026/04/30

#### Description
Close the remaining 1x1 messaging gaps to reach full desktop critical parity.

#### Deliverables
- Message edit status, `isEdited`, assertion added
- Image attachment send and receive test
- Chat history clear and post-clear chat state assertions
- Receiver cannot-delete-sender's-message assertion
- 3 additional assertions bringing 1x1 messaging to 12/12 desktop parity

### Communities groundwork

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:test-communities`
* owner: magnus
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/30

#### Description
Land community page objects and establish mobile-feasible test coverage.
Community creation is desktop-only, so test environment setup will be investigated using the backend API directly.

#### Deliverables
- Investigation of backend API for community creation and test environment setup
- Community overview, channels, categories, and permissions page objects merged
- Browse and join community flow test on mobile
- Channel interaction test within a joined community
- Documented remaining gaps for permissions and categories, for Q3 follow-up if needed

### Device sync onboarding

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:test-device-sync`
* owner: magnus
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/15

#### Description
Implement mobile login-via-sync-code test coverage.
Sync code generation is desktop-only through the UI, so the backend API will be investigated for generating sync codes directly.

#### Deliverables
- Investigation of backend API for sync code generation
- `SyncCodeInputPage` page object for `LoginBySyncingPage`
- `SyncProgressPage` page object for sync progress, success, and failure states
- `test_mobile_sync_login.py` validating code entry, sync completion, and profile data sync
- 5 assertions matching desktop critical parity

### Quick wins

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:quick-wins`
* owner: magnus
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/30

#### Description
Close small assertion gaps that require minimal new infrastructure.

#### Deliverables
- Post-login user identity check in password change test
- Post-login user identity check in backup recovery test
- Backup seed banner visibility state validation

### iOS coverage expansion

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:ios-expansion`
* owner: magnus
* status: not started
* start-date: 2026/05/15
* end-date: 2026/06/30

#### Description
Extend the iOS POC beyond the single onboarding smoke test, informed by the Q1 feasibility assessment from PR `#20049`.

#### Deliverables
- Additional iOS smoke tests covering wallet and messaging critical paths
- iOS CI integration assessment
- iOS coverage roadmap for Q3

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:maintenance`
* owner: magnus
* status: in progress (10%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Keep the framework healthy while the app changes.

#### Deliverables
- Stability of tests monitored and flaky tests triaged
- Tests maintained through Status app refactors
- Locator migration from `xpath` and `resource-id` to `accessibility_id` continued
- [status-im/status-app#20308](https://github.com/status-im/status-app/pull/20308) fix(e2e_appium): improve test timing for light-client messaging
- [status-im/status-go#7393](https://github.com/status-im/status-go/issues/7393) Light clients can silently lose messages sent immediately after contact acceptance
- [status-im/status-app#20460](https://github.com/status-im/status-app/issues/20460) Android splash / grey content after backgrounding

### Release testing

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:release-testing`
* owner: magnus
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Support mobile release testing efforts:
- Exploratory testing on mobile builds
- Regression test execution

#### Deliverables
- PRs and Issues
- Manual 2.38 checks completed for 3 of 5 critical items, with notifications partially verified and one item blocked
