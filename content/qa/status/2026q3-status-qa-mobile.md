---
title: Status QA Mobile
tags:
  - "2026q3"
  - "qa"
  - "status"
draft: false
description: Status QA Mobile
---

`ift-ts:qa:status:2026q3-status-qa-mobile`

## Description
Continue closing mobile automation coverage gaps in communities, device sync, iOS, and small parity wins while keeping the mobile test framework healthy through app changes.

## Task List

### Communities groundwork

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:test-communities`
* owner: magnus
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Land community page objects and establish mobile-feasible test coverage.
Community creation is desktop-only, so test environment setup will be investigated using the backend API directly.

#### Deliverables
- Investigation of backend API for community creation and test environment setup
- Community overview, channels, categories, and permissions page objects merged
- Browse and join community flow test on mobile
- Channel interaction test within a joined community
- Documented remaining gaps for permissions and categories

### Device sync onboarding

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:test-device-sync`
* owner: magnus
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

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

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:quick-wins`
* owner: magnus
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Close small assertion gaps that require minimal new infrastructure.

#### Deliverables
- Post-login user identity check in password change test
- Post-login user identity check in backup recovery test
- Backup seed banner visibility state validation

### iOS coverage expansion

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:ios-expansion`
* owner: magnus
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Extend the iOS POC beyond the single onboarding smoke test, informed by the Q1 feasibility assessment from PR `#20049`.

#### Deliverables
- Additional iOS smoke tests covering wallet and messaging critical paths
- iOS CI integration assessment
- iOS coverage roadmap for follow-up work

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:maintenance`
* owner: magnus
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Keep the framework healthy while the app changes.

#### Deliverables
- Stability of tests monitored and flaky tests triaged
- Tests maintained through Status app refactors
- Locator migration from `xpath` and `resource-id` to `accessibility_id` continued
- PRs / Issues / Reports
