---
title: Status QA Mobile
tags:
  - "2026q3"
  - "qa"
  - "status"
draft: false
description: Status QA Mobile
---

`ift-ts:qa:status:2026q3-status-qa-mobile`

## Description
Continue building mobile test automation for the Status app, with three priorities for Q3:
- make the per-PR gate a trustworthy signal again,
- close the wallet-send and keycard coverage gaps where users risk funds and keys,
- and move backend correctness (delivery, sync, sends) down to status-go functional tests so the mobile suite holds what only a real device proves.

The performance work is a priority as there is an intention to use performance metrics as part of the gate for future releases.

## Task List

### Performance and resource monitoring

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:performance`
* owner: magnus
* status: in progress (75%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Make the mobile performance pipeline run unattended and extend it from response times to resource usage. The response-time dashboard already covers around 39 app surfaces on a fresh account; the priority this quarter is measuring a loaded account, getting the nightly run reliable, and adding battery, CPU, and memory tracking.

#### Deliverables
- [status-im/status-app#21448](https://github.com/status-im/status-app/issues/21448) [QA - Android] Regression: Wallet Swap screen takes >1s to open (was ~0.7s)
- [status-im/status-app#21447](https://github.com/status-im/status-app/issues/21447) [QA - Android] Regression: Wallet Send screen takes >1s to open (was ~0.7s)
- [status-im/status-app#21430](https://github.com/status-im/status-app/issues/21430) [QA - Android] Communities directory takes 17–80s to load — latest check never loaded (120s+)
- [status-im/status-app#21429](https://github.com/status-im/status-app/issues/21429) [QA] Screens in the slow performance band (>1.0s) — optimization backlog
- [status-im/status-go#7614](https://github.com/status-im/status-go/issues/7614) Fresh light-client account downloads gigabytes of background data on login
- Loaded-account measurement column published to the status-app-benchmarks dashboard
- Unattended nightly run with failure alerting, proven over consecutive nights
- Battery, CPU, and memory findings linked to [status-im/status-app#21045](https://github.com/status-im/status-app/issues/21045)
- Second test device (Moto G55) added to the runs
- Tracks [status-im/status-app#21086](https://github.com/status-im/status-app/issues/21086)
- [Mobile performance docs](https://north661.gitbook.io/docs/performance/performance/mobile)

### Gate-health stabilisation

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:gate-health`
* owner: magnus
* status: in progress (75%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Restore the Android per-PR gate as a trustworthy signal. Re-triage expected-fail tests and rebalance the gate into a stable set covering onboarding, messaging, wallet, and settings journeys.

#### Deliverables
- [status-im/status-go#7610](https://github.com/status-im/status-go/issues/7610) QA: functional test for the history-reconcile fetch path (test removed during #7604 review)
- [status-im/status-go#7609](https://github.com/status-im/status-go/issues/7609) QA: verify that light clients recover messages missed while staying online (gap deferred from #7604)
- [status-im/status-go#7606](https://github.com/status-im/status-go/issues/7606) Android light clients can't resolve boot-node DNS → no Waku peers → can't publish
- Expected-fail messaging tests re-triaged and re-enabled or refiled
- A rebalanced gate marker covering onboarding, messaging, wallet, and settings journeys
- `prs-android` job passing reliably on the rebalanced set
- [status-im/status-app#21405](https://github.com/status-im/status-app/issues/21405) [QA - Android] Contact requests stop reaching the receiver after the 2026-07-02 status-go bump

### Accessibility testability contract

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:a11y-contract`
* owner: magnus
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Add accessibility properties (`objectName` / `Accessible.name`) on screens the tests currently cannot read, improving assertions and reducing brittle locators.

#### Deliverables
- [status-im/status-app#21392](https://github.com/status-im/status-app/pull/21392) fix: expose send-confirm values to accessibility
- An agreed `objectName` / `Accessible.name` convention, lint-checked warn-only on touched files
- The reply, pin, and members `objectName`s added
- Disabled chat-title, message-text, and synced-name checks converted to assertions as properties land
- [status-im/status-app#21368](https://github.com/status-im/status-app/pull/21368) fix: expose the edited-message indicator to accessibility

### Mobile binding contract test

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:binding-contract`
* owner: magnus
* status: in progress (10%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Add a fast Go test that checks every backend method the mobile app calls is still exposed by status-go, so renamed or removed methods fail in CI instead of surfacing only on device.

#### Deliverables
- A method-existence test in status-go's `mobile` package covering the `wakuext` namespace, running in CI
- The app's referenced method names enumerated from source
- Coverage extended to the `wallet` and `accounts` namespaces

### Backend-peer messaging gate

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:backend-peer-gate`
* owner: magnus
* status: in progress (15%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Replace flaky two-phone messaging checks with a headless status-backend acting as the second participant, while retaining the on-phone smoke as a backup.

#### Deliverables
- A headless status-backend second-participant harness
- 1:1 delivery and receipt asserted through the backend peer in CI without a device pair
- Transport decided for Pi/emulator and BrowserStack paths
- The on-phone delivery smoke retained as a backup pending a production-network check

### Wallet-send and community smokes

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:journey-smokes`
* owner: magnus
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Add smoke tests for critical journeys missing from the gate: wallet send and joining a community. Both join the gate once gate-health has stabilised it.

#### Deliverables
- [status-im/status-app#21420](https://github.com/status-im/status-app/pull/21420) test(e2e-mobile): wallet-send smoke
- A wallet-send smoke asserting recipient and amount through to signing, with a `send_modal` page object
- A community browse-and-join smoke, with community page objects
- [status-im/status-app#21383](https://github.com/status-im/status-app/issues/21383) [QA - Android] e2e smoke: wallet send reaches the signing step

### Keycard UI coverage

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:keycard-ui`
* owner: magnus
* status: in progress (10%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Cover the new keycard on-screen flows on mobile: PIN entry, PUK unblock, onboarding, and recovery. Dev may provide a keycard test mock that makes these flows automatable without a physical card.

#### Deliverables
- Keycard page objects and locators against the new screens
- Automated PIN, onboarding, and recovery flows once the mock is reachable in the mobile build
- Drafted keycard QA test plan for the new simulator-based stack
- Tracks [status-im/status-app#20305](https://github.com/status-im/status-app/issues/20305) and [status-im/status-app#20289](https://github.com/status-im/status-app/issues/20289)

### Communities groundwork

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:test-communities`
* owner: magnus
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Land community page objects and establish mobile-feasible test coverage. Community creation is desktop-only, so test environment setup will be investigated using the backend API directly.

#### Deliverables
- Investigation of backend API for community creation and test environment setup
- Community overview, channels, categories, and permissions page objects merged
- Browse and join community flow test on mobile
- Channel interaction test within a joined community
- Documented remaining gaps for permissions and categories

### Device sync onboarding

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:test-device-sync`
* owner: magnus
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Implement mobile login-via-sync-code test coverage. Sync code generation is desktop-only through the UI, so the backend API will be investigated for generating sync codes directly.

#### Deliverables
- Investigation of backend API for sync code generation
- `SyncCodeInputPage` page object for `LoginBySyncingPage`
- `SyncProgressPage` page object for sync progress, success, and failure states
- `test_mobile_sync_login.py` validating code entry, sync completion, and profile data sync
- 5 assertions matching desktop critical parity

### Quick wins

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:quick-wins`
* owner: magnus
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Close small assertion gaps that require minimal new infrastructure.

#### Deliverables
- Post-login user identity check in password change test
- Post-login user identity check in backup recovery test
- Backup seed banner visibility state validation

### iOS coverage expansion

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:ios-expansion`
* owner: magnus
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Get a working iOS test build into the automation so iOS coverage can be expanded later. The framework already supports iOS with one onboarding smoke, based on the Q1 feasibility work in [status-im/status-app#20049](https://github.com/status-im/status-app/pull/20049).

#### Deliverables
- A working iOS test build available to the Appium framework (TestFlight or BrowserStack)
- An assessment of the iOS CI job
- iOS coverage roadmap for follow-up work

### Maintenance

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:maintenance`
* owner: magnus
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Keep the framework healthy as the app changes: triage flaky tests, follow app refactors, continue locator migration, and continue rolling out test-traceability markers.

#### Deliverables
- Brittle xpath locators reduced in messaging and wallet locator files, toward `tid()` / `objectName`
- Test-traceability markers extended beyond messaging suites to wallet and onboarding tests
- [status-im/status-app#21367](https://github.com/status-im/status-app/pull/21367) fix(e2e_appium): context-menu and wallet account gate tests
- [status-im/status-app#21304](https://github.com/status-im/status-app/issues/21304) [Epic] test(e2e-mobile): maintenance

### Release testing

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-mobile:release-testing`
* owner: magnus
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Support release testing for the 2.39 and 2.40 mobile builds: exploratory testing, regression execution, and reporting issues found.

#### Deliverables
- Critical-path sign-off for the 2.39 and 2.40 mobile releases
- Bugs and follow-up issues filed during release testing
