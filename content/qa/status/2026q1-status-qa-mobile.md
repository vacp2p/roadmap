---

title: Status QA Mobile
tags:
- "2026q1"
- "qa"
- "status"
draft: false
description: Status QA Mobile

---

`ift-ts:qa:status:2026q1-status-qa-mobile`

## Description

Continue building mobile/tablet test automation coverage for the Status app.

**Areas for Q1:**
- Wallet test coverage (account editing, receive modal, settings)
- Messaging test suite (1x1 advanced features, group chat)
- Communities testing ground work
- iOS testing pilot

**Current Coverage (End of Q4 2025):**
- 7 tests
- 61/298 discrete features covered (20%)
- Multi-device infrastructure added (2-device validated)
- BrowserStack CI integration nearing completion

## Task List

### Wallet test expansion

- fully qualified name: `ift-ts:qa:status:2026q1-status-qa-mobile:test-wallet`
- owner: magnus
- status: in progress (5%)
- start-date: 2026/01/01
- end-date: 2026/02/15

#### Description

Round out wallet automation to cover account edit, restart, receive, and settings flows.

#### Deliverables

- Account rename + restart path automated in `test_wallet_accounts_basic.py`
- Receive modal page object with QR/address assertions
- `test_add_delete_account_from_settings.py` ported (settings navigation + details view)

### iOS testing pilot

- fully qualified name: `ift-ts:qa:status:2026q1-status-qa-mobile:ios-pilot`
- owner: magnus
- status: not started
- start-date: 2026/01/20
- end-date: 2026/02/15

#### Description

Investigate feasibility of adding iOS coverage to framework.

#### Deliverables

- Assessment for Q2 planning

### Messaging 1x1 additional features

- fully qualified name: `ift-ts:qa:status:2026q1-status-qa-mobile:test-messaging-1x1`
- owner: magnus
- status: not started
- start-date: 2026/02/01
- end-date: 2026/02/21

#### Description

Bring the 1x1 messaging test to desktop parity, including edit/reply/react, media, and history flows.

#### Deliverables

- Messaging context menu + reaction/emoji helpers
- Media/emoji/reaction coverage added to `test_messaging_1x1_chat.py`
- Edit, reply, delete, clear-history assertions implemented

### Messaging group chat

- fully qualified name: `ift-ts:qa:status:2026q1-status-qa-mobile:test-messaging-group`
- owner: magnus
- status: not started
- start-date: 2026/02/15
- end-date: 2026/03/15

#### Description

Stand up the first 3-device group chat test covering Activity Center acceptance, member management, and leave flows.

#### Deliverables

- Activity Center + group chat page objects
- `test_messaging_group_chat.py` ported with 3-device execution
- Member management, link preview, and leave-chat assertions validated

### Communities foundation

- fully qualified name: `ift-ts:qa:status:2026q1-status-qa-mobile:test-communities`
- owner: magnus
- status: not started
- start-date: 2026/03/01
- end-date: 2026/03/31

#### Description

Lay the groundwork for communities tests with page objects and a basic create/invite/join flow.

#### Deliverables

- Community overview/settings/channel page objects
- Smoke test covering create - invite - join (stretch goal)
- Documented gaps for permissions, categories, and pinning (Q2 follow-up)

### Maintenance

- fully qualified name: `ift-ts:qa:status:2026q1-status-qa-mobile:maintenance`
- owner: magnus
- status: in progress (5%)
- start-date: 2026/01/01
- end-date: 2026/03/31

#### Description

Keep the framework healthy while the app changes.

#### Deliverables

- Stability of tests monitored and flakey tests triaged
- Tests maintained through Status app refactors
- [status-im/status-app#19310](https://github.com/status-im/status-app/pull/19310) chore(StatusListItem): add accessible name for e2e test ids

### Release testing

- fully qualified name: `ift-ts:qa:status:2026q1-status-qa-mobile:release-testing`
- owner: magnus
- status: in progress (5%)
- start-date: 2026/01/01
- end-date: 2026/03/31

#### Description

Support mobile release testing efforts:
- Exploratory testing on mobile builds
- Regression test execution

#### Deliverables
PRs and Issues
