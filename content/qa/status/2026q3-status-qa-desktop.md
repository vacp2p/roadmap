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
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Ongoing maintenance of Status Desktop tests.
- Update tests for changes in Status Desktop, address regressions, investigate failures, and implement minor framework improvements needed to keep the suite reliable.

#### Deliverables
- PRs / Issues / Reports

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
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Support Q3 desktop releases with test planning, exploratory testing, regression execution, and issue reporting.
- Manually test Status Desktop 2.39 and 2.40.
- Track release risks and bugs found during manual release validation.

#### Deliverables
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
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Add more tests to track in-app performance for the desktop application on Windows from the UI side.
- Improve coverage for the main performance-sensitive user flows and make the measurements useful for regression tracking.

#### Deliverables
- PRs / Issues

### Battery, CPU, and RAM usage

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:battery-cpu-ram-usage`
* owner: nastya
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Investigate battery, CPU, and RAM usage for Status Desktop and define useful QA validation around resource consumption.
- Use [status-im/status-app#21249](https://github.com/status-im/status-app/issues/21249) as the reference issue for scope and follow-up.

#### Deliverables
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

