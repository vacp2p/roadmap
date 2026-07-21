---
title: Status QA Desktop
tags:
  - "2026q3"
  - "qa"
  - "status"
draft: false
description: Status QA Desktop
---

`ift-ts:qa:status:2026q3-status-qa-desktop`

## Description
Collaborate with the Status team to keep Status Desktop releases covered through manual and automated QA.
Q3 focuses on release testing for 2.39 and 2.40, recurring maintenance, and targeted coverage for browser, privacy, and performance-related areas.

## Task List

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:maintenance`
* owner: nastya
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Ongoing maintenance of Status Desktop tests.
- Update tests for changes in Status Desktop, address regressions, investigate failures, and implement minor framework improvements needed to keep the suite reliable.

#### Deliverables
- [status-im/status-app#21476](https://github.com/status-im/status-app/issues/21476) Fix MacOS setup with Squish 9.2
- [status-im/status-app#21518](https://github.com/status-im/status-app/pull/21518) tests(@qml): add tests for custom order for assets in wallet
- [status-im/status-app#21517](https://github.com/status-im/status-app/issues/21517) Custom assets order from wallet settings is not applied to wallet
- [status-im/status-app#21423](https://github.com/status-im/status-app/pull/21423) chore(@e2e): fix Squish setup on macOS
- [status-im/status-go#7561](https://github.com/status-im/status-go/pull/7561) test(functional): use Docker-assigned ephemeral host ports

### New tests

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:new-tests`
* owner: nastya
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Add new automated tests from the existing backlog.
- Add or update tests for new Status Desktop features as they are planned and implemented.

#### Deliverables
- PRs / Issues / Reports

### Release Testing

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:release-testing`
* owner: nastya
* status: in progress (10%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Support Q3 desktop releases with test planning, exploratory testing, regression execution, and issue reporting.
- Manually test Status Desktop 2.39 and 2.40.
- Track release risks and bugs found during manual release validation.

#### Deliverables
- [status-im/status-app#21524](https://github.com/status-im/status-app/issues/21524) iOS app crashes on swipe-to-close action
- Bugs and follow-up issues found during 2.39 and 2.40 release testing.
- Release testing notes / reports.

### Privacy Mode

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:privacy-mode`
* owner: nastya
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Evaluate the current Privacy Mode behavior and determine what can be covered by automated tests.
- Add automated coverage where feasible, or document the constraints if the feature is not practical to automate.

#### Deliverables
- PRs / Issues
- Automation feasibility notes for Privacy Mode.

### Dapp Browser

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:dapp-browser`
* owner: nastya
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Support the Browser feature in tests after the 2.38 rework.
- Add automated scenarios and refresh existing coverage for the updated browser flows.

#### Deliverables
- PRs / Issues

### Performance tests for desktop application on Windows

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:windows-performance-tests`
* owner: nastya
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Add more tests to track in-app performance for the desktop application on Windows from the UI side.
- Improve coverage for the main performance-sensitive user flows and make the measurements useful for regression tracking.

#### Deliverables
- [status-im/status-app-benchmarks#16](https://github.com/status-im/status-app-benchmarks/pull/16) desktop: add wallet resource metrics and improve benchmark dashboard
- [status-im/status-app-benchmarks#15](https://github.com/status-im/status-app-benchmarks/pull/15) desktop: add baselines
- [status-im/status-app-benchmarks#13](https://github.com/status-im/status-app-benchmarks/pull/13) desktop: align benchmark charts with mobile layout and split by account variant
- [status-im/status-app#21509](https://github.com/status-im/status-app/pull/21509) chore(@e2e): add fresh-user variants to desktop benchmark tests
- [status-im/status-app-benchmarks#12](https://github.com/status-im/status-app-benchmarks/pull/12) desktop: add run spread bands and responsive Plotly charts for multi-run benchmarks
- [status-im/status-app#21493](https://github.com/status-im/status-app/pull/21493) chore(@ci): collect Windows system info in nightly benchmark push
- [status-im/status-app-benchmarks#11](https://github.com/status-im/status-app-benchmarks/pull/11) desktop: small refactoring
- [status-im/status-app-benchmarks#10](https://github.com/status-im/status-app-benchmarks/pull/10) desktop: add system info panel and --machine-info for Windows benchmarks
- PRs / Issues

### Battery, CPU, and RAM usage

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:battery-cpu-ram-usage`
* owner: nastya
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Investigate battery, CPU, and RAM usage for Status Desktop and define useful QA validation around resource consumption.
- Use [status-im/status-app#21249](https://github.com/status-im/status-app/issues/21249) as the reference issue for scope and follow-up.

#### Deliverables
- [status-im/status-app#21537](https://github.com/status-im/status-app/pull/21537) chore(@ci): fix benchmark job log path
- [status-im/status-app-benchmarks#17](https://github.com/status-im/status-app-benchmarks/pull/17) desktop: fix parser
- [status-im/status-app#21536](https://github.com/status-im/status-app/pull/21536) chore(@e2e): expand wallet performance benchmarks with CPU and RAM metrics
- [status-im/status-app-benchmarks#14](https://github.com/status-im/status-app-benchmarks/pull/14) desktop: align CPU and RAM charts with load-time chart style
- [status-im/status-app#21480](https://github.com/status-im/status-app/pull/21480) chore(@e2e): cpu data is 0 in benchmark reports
- [status-im/status-app#21475](https://github.com/status-im/status-app/pull/21475) chore(@e2e): cpu measurements fix
- PRs / Issues / Reports
- Resource usage findings linked to [status-im/status-app#21249](https://github.com/status-im/status-app/issues/21249).

### E2E tests for keycard with mock

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:e2e-kyecard-mock`
* owner: nastya
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Once keycard mock is ready (new implementation), bring back to life existing e2e tests if possible or create new ones, to cover main keycard interactions with desktop app
- Work with infra team (if needed) to build proper app (the one that will use keycard mock), including macOS

#### Deliverables
- PRs / Issues / Reports
