---
title: Status QA Mobile
tags:
  - "2026q4"
  - "qa"
  - "status"
draft: false
description: Support Status Mobile releases, maintain reliable automation, and expand coverage, framework capabilities, and performance testing.
---

`ift-ts:qa:status:2026q4-status-qa-mobile`

## Description

Support ongoing Status Mobile releases, including at least 2.40 and 2.41, and test the new features in each release.
Keep nightly automation and the per-PR gate reliable, add coverage for existing features, and improve the test harness.
Maintain the performance suite and extend measurements to a loaded existing account.

## Task List

### Release testing

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-mobile:release-testing`
* owner: magnus
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Support ongoing Status Mobile releases, including at least 2.40 and 2.41.
Perform exploratory and regression testing, test new features in each release, and report issues and release risks.

#### Deliverables

- Release test reports and tracked issues for Status Mobile 2.40, 2.41, and other releases tested during Q4.

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-mobile:maintenance`
* owner: magnus
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Investigate and fix failing nightly tests and keep the per-PR gate running as a trusted regression signal.
Address flaky tests and assist developers with test changes in pull requests as the app evolves.

#### Deliverables

- PRs fixing nightly failures, flaky tests, and per-PR gate issues.
- Test updates for application changes and tracked product or framework defects.

### Coverage for existing features

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-mobile:coverage`
* owner: magnus
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Add automated tests for existing Status Mobile features that lack coverage.
Prioritize gaps with the Status team based on user impact and the feasibility of reliable device-level automation.

#### Deliverables

- PRs covering previously untested existing features.
- Tracked coverage gaps and any constraints preventing automation.

### Framework improvements

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-mobile:framework`
* owner: magnus
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Improve the mobile test harness in the following areas:
- iOS build and execution support.
- Repeatable setup and reuse of a loaded existing account.
- Accessibility properties that provide stable locators and assertions.
- App/backend binding checks that detect missing or changed backend methods.
- Backend-peer support for messaging scenarios with a headless second participant.

#### Deliverables

- PRs implementing harness improvements and contract checks.
- Setup and usage documentation for iOS, loaded accounts, and backend-peer scenarios.

### Performance

* fully qualified name: `ift-ts:qa:status:2026q4-status-qa-mobile:performance`
* owner: magnus
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Maintain the mobile performance suite and add a loaded-account scenario using the account setup provided by the framework task.
Keep measurements useful for comparing releases and identifying performance regressions.

#### Deliverables

- PRs maintaining the performance suite and adding loaded-account measurements.
- Performance reports and tracked regressions.
