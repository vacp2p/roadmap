---
title: Status QA Desktop
tags:
  - "2026q4"
  - "qa"
  - "status"
draft: false
description: Support Status Desktop releases, maintain automated tests, and expand feature and performance coverage.
---

`ift-ts:qa:status:2026q4-status-qa-desktop`

## Description

Collaborate with the Status team on manual and automated QA for ongoing Desktop releases, including at least 2.40 and 2.41.
Maintain the existing test suite and expand coverage for new features as release scope becomes clear.
Keep feature automation flexible as priorities and delivery dates change; select concrete scenarios with the Status team as the automation backlog is clarified.
Continue Windows performance testing. macOS and Linux performance work remains tentative, subject to infrastructure availability and prioritization.

## Task List

### Release Testing

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-desktop:release-testing`
* owner: nastya
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Support ongoing Status Desktop releases, including at least 2.40 and 2.41, with exploratory testing, regression testing, and validation of new features.
Report bugs and release risks and verify fixes with the Status team.

#### Deliverables

- Release test reports and tracked issues for Status Desktop 2.40, 2.41, and other releases tested during Q4.

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-desktop:maintenance`
* owner: nastya
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Investigate and fix failing nightly tests, address flaky scenarios, and keep the suite compatible with Status Desktop changes.
Assist developers with test changes in pull requests.

#### Deliverables

- PRs fixing nightly failures and updating existing tests for application changes.
- Tracked product or framework issues found while maintaining the suite.

### Performance tests for desktop application on Windows

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-desktop:windows-performance-tests`
* owner: nastya
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Continue creating Windows performance tests for the main Status Desktop user flows.
Maintain useful measurements for comparing releases and detecting performance regressions.

#### Deliverables

- PRs extending Windows performance test coverage.
- Performance measurements and tracked regressions.

### New tests

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-desktop:new-tests`
* owner: nastya
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Add automated coverage for new Status Desktop features, including those delivered in 2.40 and 2.41.
Choose scenarios as feature scope and the automation backlog are clarified with the Status team, and adjust coverage when features are delayed or changed.

#### Deliverables

- PRs adding automated tests for new release features.
- Tracked coverage gaps or automation constraints for features under test.

### Performance tests for desktop application on Mac

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-desktop:mac-performance-tests`
* owner: nastya
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Tentative: confirm with Infra whether a supported environment for macOS performance testing can be provided.
If the infrastructure dependency is resolved and the work is prioritized, add performance tests for the main Status Desktop user flows on macOS.

#### Deliverables

- A documented infrastructure decision and any remaining constraints.
- Performance test PRs and measurements if the work proceeds.

### Performance tests for desktop application on Linux

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-desktop:linux-performance-tests`
* owner: nastya
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Tentative: confirm whether Linux performance testing remains a Q4 priority and identify the scenarios worth covering.
If prioritized, add performance tests for the main Status Desktop user flows on Linux.

#### Deliverables

- A documented scope and prioritization decision.
- Performance test PRs and measurements if the work proceeds.
