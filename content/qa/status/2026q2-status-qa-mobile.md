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
Continue building mobile/tablet test automation coverage for the Status app.

## Task List

### Messaging group chat

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:test-messaging-group`
* owner: magnus
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Stand up the first 3-device group chat test covering Activity Center acceptance, member management, and leave flows.

#### Deliverables
- Activity Center + group chat page objects
- `test_messaging_group_chat.py` ported with 3-device execution
- Member management, link preview, and leave-chat assertions validated

### Communities foundation

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:test-communities`
* owner: magnus
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Lay the groundwork for communities tests with page objects and a basic create/invite/join flow.

#### Deliverables
- Community overview/settings/channel page objects
- Smoke test covering create - invite - join (stretch goal)
- Documented gaps for permissions, categories, and pinning (Q2 follow-up)

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q2-status-qa-mobile:maintenance`
* owner: magnus
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Keep the framework healthy while the app changes.

#### Deliverables
- PRs / Issues / Reports

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
