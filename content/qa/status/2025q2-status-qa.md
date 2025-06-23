---
title: Status QA
tags:
  - "2025q2"
  - "qa"
  - "status"
draft: false
description: Status QA
---

`vac:qa:status:2025q2-status-qa`

## Description
This commitment includes continuing the Status QA work to ensure a seamless transition of service to Status after QA moved from Status into Vac,
up until the release of version 2.34.
It also covers ongoing support for Status after the release, for the remainder of this quarter.
QA work for Status for Q3 will be defined in follow up commitments.

## Task List

### Maintenance

* fully qualified name: `vac:qa:status:2025q2-status-qa:v2-34`
* owner: nastya,tetiana,magnus
* status: in progress (70%)
* start-date: 2025/05/20
* end-date: 2025/06/10

#### Description

#### Deliverables
- finished the main round testing for mobile 2.34, the full report is [here](https://www.notion.so/2-34-Mobile-Release-Coordination-1f88f96fb65c80589326d087cfc6f0f5)
- retested several fixes, reported 12 issues [here](https://www.notion.so/2-34-Mobile-Release-Coordination-1f88f96fb65c80589326d087cfc6f0f5)
- logged a couple of issues for desktop (including the results of e2e):
  - https://github.com/status-im/status-desktop/issues/18053
  - https://github.com/status-im/status-desktop/issues/18043
  - https://github.com/status-im/status-desktop/issues/18018
  - https://github.com/status-im/status-desktop/issues/18063
- opened a PR to partially remove unused code and merge 2 tests of similar functionality in 1 https://github.com/status-im/status-desktop/pull/18052
- started fixing tests to fit them into qt 6.9 app (in scope of https://github.com/status-im/status-desktop/pull/18019)
- Research and shared findings regarding opening RC testing to community
- Tested fix of 2 blockers
- Tested new feature required for 2.34
- Tested a fix for [18063](https://github.com/status-im/status-desktop/issues/18063)
