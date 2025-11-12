---
title: Status QA Desktop
tags:
  - "2025q4"
  - "qa"
  - "status"
draft: false
description: Status QA Desktop
---

`vac:qa:status:2025q4-status-qa-desktop`

## Description
Collaborate with Status team to ensure that the Status Desktop app behaves as expected.  
Add new automated tests to the existing e2e testing framework for new features.  
Oversee testing strategy around releases.

## Task List

### Maintenance

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:maintenance`
* owner: nastya
* status: in progress (70%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
- Ongoing maintenance of Status Desktop tests.  
  This includes updating tests for changes in status, addressing regressions,  
  investigating and resolving issues, and implementing minor improvements  
  to the testing framework as needed.

#### Deliverables
- [tests(@e2e): cover help us improve status dialog](https://github.com/status-im/status-desktop/pull/19217)
- [chore: update status-go](https://github.com/status-im/status-desktop/pull/19216)
- [tests: add test to change language](https://github.com/status-im/status-desktop/pull/19165)
- [bug: Can't mint tokens on Optimism Sepolia](https://github.com/status-im/status-desktop/issues/18954)
- [chore: Optimize code usage](https://github.com/status-im/status-desktop/pull/18980)
- [bug: Cover language selector in e2e](https://github.com/status-im/status-desktop/issues/18983)
- [issue: Account name resets when editing account in settings](https://github.com/status-im/status-desktop/issues/19174)
- [issue: Tests using an old data dir crash on login on latest master](https://github.com/status-im/status-desktop/issues/19176)
- [issue: Fix toplevel window usage](https://github.com/status-im/status-desktop/issues/19237)
- [issue: Run Squish 9.1.0 on mac arm](https://github.com/status-im/status-desktop/issues/19226)
- [issue: Add checks for Help us to improve Status info icon popup](https://github.com/status-im/status-desktop/issues/19173)
- [issue: Biometrics is not fully applied for created profile](https://github.com/status-im/status-desktop/issues/17450)
- [feat: replace old transfer detector](https://github.com/status-im/status-desktop/pull/18924)
- [chore(@e2e): improvement to object definition](https://github.com/status-im/status-desktop/pull/19047)
- [chore: remove TestRail usage from the project](https://github.com/status-im/status-desktop/pull/19100)
- [tests: enable syncing on Windows](https://github.com/status-im/status-desktop/pull/19123)
- [tests: fix Windows object references](https://github.com/status-im/status-desktop/pull/19125)
- [infra-ci issue 219: Windows test overlap with system window](https://github.com/status-im/infra-ci/issues/219)

---

### Release Testing

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:release-testing`
* owner: nastya
* status: in progress (5%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
- Support releases **2.36** and **2.37** with testing.

#### Deliverables
- [Tested: add withdraw flow fixes](https://github.com/status-im/status-desktop/pull/19180)
- [Tested: release patch set for PR #19227](https://github.com/status-im/status-desktop/pull/19227)
- [fix tests for new component](https://github.com/status-im/status-desktop/pull/19122)
- [issue: test bug fixes](https://github.com/status-im/status-desktop/issues/19152)
- [issue: opened bug follow-up](https://github.com/status-im/status-desktop/issues/19167)
- [fixed tests](https://github.com/status-im/status-desktop/pull/19171)
- [tested: Enter seed phrase component refactored according to new design](https://github.com/status-im/status-desktop/pull/19004)
- [bug: Application login is incredibly slow](https://github.com/status-im/status-desktop/issues/19019)
- [tested: chore: fix some undefined references](https://github.com/status-im/status-desktop/pull/19022)
- [tested: restore mobile release regression fixes](https://github.com/status-im/status-desktop/pull/19073)
- [bug: Traces missing for release testing](https://github.com/status-im/status-desktop/issues/19119)
- [bug: Investigate desktop login freeze](https://github.com/status-im/status-desktop/issues/19120)
- [bug: Follow-up on mobile build reliability](https://github.com/status-im/status-desktop/issues/19135)

---

### Measure app load time

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:app-load-time`
* owner: nastya
* status: not started
* start-date: 2025/10/01
* end-date: 2025/11/01

#### Description
- Track UI loading time of the desktop app wallet screens.

#### Deliverables
- PRs / Issues

---

### E2E Windows CI

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:e2e-windows`
* owner: nastya
* status: done
* start-date: 2025/10/07
* end-date: 2025/10/31

#### Description
- Work with infra team on initiative to run tests on Windows on CI.  
- Tweak tests if needed.

#### Deliverables
- [tests: add new test, updating old test](https://github.com/status-im/minimal-qt-squish-app/pull/4)
- [testing: WIP: feat(e2e): add windows pipeline](https://github.com/status-im/status-desktop/pull/18724)

---

### Qt6 Migration

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:qt6-migration`
* owner: nastya
* status: in progress (30%)
* start-date: 2025/10/01
* end-date: 2025/10/25

#### Description
- Work with developers and infra team.  
- Test Qt **6.9.2 update** and further updates.  
- Ensure tests are working and change them if needed.

#### Deliverables
- [bug: Qt 6.9.3: can't build app on newer Qt (ubuntu)](https://github.com/status-im/status-desktop/issues/18947)

---

### Privacy Mode

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:privacy-mode`
* owner: nastya
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
- Support new **Privacy Mode** feature in tests.  
- Add new tests and update existing ones.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs / Issues

---

### Dapp Browser

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:dapp-browser`
* owner: nastya
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
- Support Browser feature in tests.  
- Add new tests and update existing ones.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs / Issues

---

### Local Backup

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:local-backup`
* owner: nastya
* status: in progress (75%)
* start-date: 2025/10/07
* end-date: 2025/10/20

#### Description
- Maintenance for **Local Backup** feature.

#### Deliverables
- [fixed tests in the https://github.com/status-im/status-desktop/pull/18953]

---

### Local Backup Opt-in

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:local-backup-opt-in`
* owner: nastya
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
- Opt-in messages Local Backup feature support in tests.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs / Issues

---

### External Activity

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:external-activity`
* owner: nastya
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
- Support **Activity fetching** feature in tests.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs / Issues

---

### Emoji Reactions

* fully qualified name: `vac:qa:status:2025q4-status-qa-desktop:emoji-reactions`
* owner: nastya
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
- Maintenance for full emoji list in **Reactions** feature.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs / Issues
