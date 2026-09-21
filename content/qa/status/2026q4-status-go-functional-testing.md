---
title: Status Go Functional Testing
tags:
  - "2026q4"
  - "qa"
  - "status"
draft: false
description: Maintain status-go functional tests and expand backend coverage through status-backend.
---

`ift-ts:qa:status:2026q4-status-go-functional-testing`

## Description

Continue backend functional testing through status-backend to support Status releases and catch regressions below the desktop and mobile UI layers.

Proposed Q4 scope: the planning discussion reserves one or two backend functional-testing tasks without specifying their details.
The maintenance and coverage tasks below continue the Q3 direction; concrete scenarios and ownership remain to be defined.

## Task List

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q4-status-go-functional-testing:maintenance`
* owner: TBD
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Maintain the status-go functional test suite as backend APIs and behavior evolve.
Investigate failing or flaky tests, update fixtures and the Python SDK where needed, and assist with test changes in pull requests.

#### Deliverables

- PRs fixing functional test failures and maintaining fixtures, SDK helpers, and CI execution.
- Tracked backend or test-framework defects found during maintenance.

### Functional test coverage

* fully qualified name: `ift-ts:qa:status:2026q4-status-go-functional-testing:coverage`
* owner: TBD
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Add functional tests for prioritized backend coverage gaps and new Status release behavior using status-backend.
Select concrete scenarios from the existing backlog and issues found during desktop and mobile testing, including delivery, synchronization, or send behavior where backend-level coverage is appropriate.

#### Deliverables

- PRs adding backend functional tests for selected scenarios and regressions.
- Tracked backend issues and remaining coverage gaps.
