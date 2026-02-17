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
- status: done
- start-date: 2026/01/01
- end-date: 2026/02/10

#### Description

Round out wallet automation to cover account edit, restart, receive, and settings flows.

#### Deliverables

- [status-im/status-app#19770](https://github.com/status-im/status-app/issues/19770) [Epic] test(e2e-mobile): wallet test expansion
- [status-im/status-app#19795](https://github.com/status-im/status-app/pull/19795) test(e2e-mobile): Add wallet account rename
- [status-im/status-app#19802](https://github.com/status-im/status-app/pull/19802) test(e2e-mobile): Add app restart verification to wallet test
- [status-im/status-app#19862](https://github.com/status-im/status-app/pull/19862) test(e2e-mobile): wallet account settings
- [status-im/status-app#19860](https://github.com/status-im/status-app/pull/19860) test(e2e-mobile): wallet check for receive modal
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
- status: in progress (70%)
- start-date: 2026/02/01
- end-date: 2026/02/21

#### Description

Bring the 1x1 messaging test to desktop parity, including edit/reply/react, media, and history flows.

#### Deliverables

- [status-im/status-app#19888](https://github.com/status-im/status-app/pull/19888) Media and emoji coverage for messaging
- [status-im/status-app#19871](https://github.com/status-im/status-app/pull/19871) Message Context Menu and Emoji Picker locators
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

- [status-im/status-app#19908](https://github.com/status-im/status-app/pull/19908) finalize GitHub status in post block
- [status-im/status-app#19853](https://github.com/status-im/status-app/pull/19853) fix(e2e-mobile): stabilise 1x1 chat test and locators
- [status-im/status-app#19163](https://github.com/status-im/status-app/pull/19163) ci: add Jenkinsfile and config for e2e mobile tests
- [status-im/status-app#19239](https://github.com/status-im/status-app/pull/19239) E2E Appium 1x1 chat
- [status-im/infra-ci#222](https://github.com/status-im/infra-ci/issues/222) Configure job for mobile e2e tests
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
