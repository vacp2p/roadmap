---
title: Status QA Desktop
tags:
  - "2026q2"
  - "qa"
  - "status"
draft: false
description: Status QA Desktop
---

`ift-ts:qa:status:2026q2-status-qa-desktop`

## Description
Collaborate with Status team to ensure that the Status Desktop app behaves as expected.
Add new automated tests to the existing e2e testing framework for new features.
Oversee testing strategy around releases.

## Task List

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:maintenance`
* owner: nastya
* status: in progress (89%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
- Ongoing maintenance of Status Desktop tests.
- Update tests for changes in Status Desktop, address regressions, investigate failures, and implement minor framework improvements needed to keep the suite reliable.

#### Deliverables
- [status-im/status-app#20527](https://github.com/status-im/status-app/pull/20527) chore(@e2e): community tests fixes
- [status-im/status-app#20545](https://github.com/status-im/status-app/issues/20545) Test Squish 9.2.2 for Qt 6.11 release on Windows and Linux
- [status-im/status-app#20526](https://github.com/status-im/status-app/issues/20526) Address nightly failures 20-04-2026
- [status-im/status-app#18543](https://github.com/status-im/status-app/issues/18543) Integrate custom waku fleets with e2e
- [status-im/status-app#17006](https://github.com/status-im/status-app/issues/17006) Increase automation coverage for smoke run
- [status-im/status-app#18274](https://github.com/status-im/status-app/issues/18274) Discover and join Communities
- [status-im/status-app#20352](https://github.com/status-im/status-app/issues/20352)
- [status-im/status-app#20386](https://github.com/status-im/status-app/pull/20386)
- [status-im/status-app#20373](https://github.com/status-im/status-app/pull/20373)
- [status-im/status-app#20356](https://github.com/status-im/status-app/pull/20356)
- [status-im/status-app#20468](https://github.com/status-im/status-app/pull/20468) fix(@e2e): better config to use local waku fleet for local test development
- [status-im/status-app#20431](https://github.com/status-im/status-app/pull/20431) tests(@e2e): add test to add community to profile showcase and verify it
- [status-im/status-app#20391](https://github.com/status-im/status-app/pull/20391) chore(@e2e): remove duplicated screenshots from allure
- [status-im/status-app#20271](https://github.com/status-im/status-app/issues/20271) Fix tests in 20214
- [status-im/status-app#19856](https://github.com/status-im/status-app/issues/19856) App login is super slow when internet connection is bad

### Release Testing

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:release-testing`
* owner: nastya
* status: in progress (30%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
- Support Q2 desktop releases with test planning, exploratory testing, regression execution, and issue reporting.

#### Deliverables
- [status-im/status-app#20581](https://github.com/status-im/status-app/issues/20581) Change password / Sign out and quit / Authenticate hang the app
- [status-im/status-app#20530](https://github.com/status-im/status-app/issues/20530) Browser: tabs are closed when navigating to home

### Privacy Mode

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:privacy-mode`
* owner: nastya
* status: not started
* start-date: 2026/04/06
* end-date: 2026/04/24

#### Description
- Support new **Privacy Mode** feature in tests.
- Add new automated coverage and update affected existing scenarios.

#### Deliverables
- PRs / Issues

### Dapp Browser

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:dapp-browser`
* owner: nastya
* status: not started
* start-date: 2026/04/27
* end-date: 2026/05/15

#### Description
- Support Browser feature in tests.
- Add automated scenarios and refresh existing coverage for the updated browser flows.

#### Deliverables
- PRs / Issues

### Local Backup Opt-in

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:local-backup-opt-in`
* owner: nastya
* status: not started
* start-date: 2026/05/04
* end-date: 2026/05/15

#### Description
- Add or update tests covering opt-in messaging and related flows for the Local Backup feature.

#### Deliverables
- PRs / Issues

### Standardized approach for Popups / Menus / Dropdowns

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:standardized-approach`
* owner: nastya
* status: not started
* start-date: 2026/05/18
* end-date: 2026/06/05

#### Description
- Support the **Standardized approach for Popups / Menus / Dropdowns** feature in tests.
- Update selectors, helpers, and relevant end-to-end scenarios to match the new shared UI behavior.

#### Deliverables
- PRs / Issues

### Private Transactions POC

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:private-transactions`
* owner: nastya
* status: not started
* start-date: 2026/05/18
* end-date: 2026/06/05

#### Description
- Support the **Private Transactions POC** feature in tests.
- Add focused test coverage for the initial private transaction flows and expected edge cases.

#### Deliverables
- PRs / Issues

### Activity Center & Notifications

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:activity-center-and-notifications`
* owner: nastya
* status: in progress (10%)
* start-date: 2026/06/01
* end-date: 2026/06/19

#### Description
- Support **Activity Center & Notifications - UX, Consistency and Responsive Improvements** in tests.
- Add or update scenarios covering the revised notification behavior, responsive layouts, and user interaction flows.

#### Deliverables
- [status-im/status-app#20267](https://github.com/status-im/status-app/pull/20267) test(ActivityCenter): add QML component tests for notification controls

### Backup feature improvements

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:backup-improvements`
* owner: nastya
* status: not started
* start-date: 2026/06/08
* end-date: 2026/06/26

#### Description
- Support **Backup feature improvements** in tests.
- Expand or adapt the desktop suite for the updated backup flows, messaging, and validation points.

#### Deliverables
- PRs / Issues

### Performance tests for desktop application on Windows

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:windows-performance-tests`
* owner: nastya
* status: not started
* start-date: 2026/04/13
* end-date: 2026/05/01

#### Description
- Add more tests to track in-app performance for the desktop application on Windows from the UI side.
- Improve coverage for the main performance-sensitive user flows and make the measurements useful for regression tracking.

#### Deliverables
- PRs / Issues

### Flatpak linux build support in tests

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-desktop:support-flatpak-build`
* owner: nastya
* status: not started
* start-date: 2026/06/08
* end-date: 2026/06/26

#### Description
- Support **Linux flatpak build type** in tests.

#### Deliverables
- PRs / Issues
