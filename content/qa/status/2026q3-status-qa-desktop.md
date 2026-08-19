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
* status: in progress (92%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Ongoing maintenance of Status Desktop tests.
- Update tests for changes in Status Desktop, address regressions, investigate failures, and implement minor framework improvements needed to keep the suite reliable.

#### Deliverables
- [status-im/status-app#21992](https://github.com/status-im/status-app/pull/21992) chore(@e2e): check if biometrics popup is displayed when devices are synced (on Mac)
- [status-im/status-app#21968](https://github.com/status-im/status-app/pull/21968) chore(@e2e): fix aut shutdown on windows and make local waku fleet ports assignment cross platform
- [status-im/status-app#21864](https://github.com/status-im/status-app/pull/21864) chore(@e2e): fix pin and community link on mac
- [status-im/status-app#21868](https://github.com/status-im/status-app/issues/21868) Fix pin and and community link on Mac
- [status-im/status-app#21845](https://github.com/status-im/status-app/pull/21845) chore(@e2e): wait for geometry of button in onboarding screen
- [status-im/status-app#21752](https://github.com/status-im/status-app/issues/21752) Returning login: “Create profile” opens Log in page (NewAccountLoginPage) instead of Create profile
- [status-im/status-app#21797](https://github.com/status-im/status-app/pull/21797) chore(@e2e): fix for nightly failures
- [status-im/status-app#21757](https://github.com/status-im/status-app/pull/21757) chore(@e2e): missing import fix
- [status-im/status-app#21751](https://github.com/status-im/status-app/pull/21751) chore(@e2e): fix testnet popup reference in e2e
- [status-im/status-app#21731](https://github.com/status-im/status-app/pull/21731) chore(@e2e): fix seed import verification on onboarding
- [status-im/status-app#21719](https://github.com/status-im/status-app/pull/21719) chore(@e2e): fix token naming
- [status-im/status-app#21727](https://github.com/status-im/status-app/pull/21727) tests(@qml): port testnet popup tests from e2e to QML
- [status-im/status-app#21728](https://github.com/status-im/status-app/issues/21728) Port skipped network and testnet modal tests to QML
- [status-im/status-app#21679](https://github.com/status-im/status-app/pull/21679) chore(@e2e): fixes for tests
- [status-im/status-app#21578](https://github.com/status-im/status-app/pull/21578) chore(@e2e): screenshots helper
- [status-im/status-app#21476](https://github.com/status-im/status-app/issues/21476) Fix MacOS setup with Squish 9.2
- [status-im/status-app#21518](https://github.com/status-im/status-app/pull/21518) tests(@qml): add tests for custom order for assets in wallet
- [status-im/status-app#21517](https://github.com/status-im/status-app/issues/21517) Custom assets order from wallet settings is not applied to wallet
- [status-im/status-app#21423](https://github.com/status-im/status-app/pull/21423) chore(@e2e): fix Squish setup on macOS
- [status-im/status-go#7561](https://github.com/status-im/status-go/pull/7561) test(functional): use Docker-assigned ephemeral host ports

### New tests

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:new-tests`
* owner: nastya
* status: in progress (28%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Add new automated tests from the existing backlog.
- Add or update tests for new Status Desktop features as they are planned and implemented.

#### Deliverables
- [status-im/status-app#21961](https://github.com/status-im/status-app/pull/21961) tests(@e2e): get rid of toasts verifications in e2e
- [status-im/status-app#20806](https://github.com/status-im/status-app/pull/20806) tests(@e2e): send stickers in chat
- [status-im/status-app#21750](https://github.com/status-im/status-app/pull/21750) feat(@settings): checksum wallet address on settings
- [status-im/status-app#21727](https://github.com/status-im/status-app/pull/21727) tests(@qml): port testnet popup tests from e2e to QML
- [status-im/status-app#21728](https://github.com/status-im/status-app/issues/21728) Port skipped network and testnet modal tests to QML
- [status-im/status-app#17648](https://github.com/status-im/status-app/issues/17648) Wallet address is not checksumed in wallet settings
- [status-im/status-app#21545](https://github.com/status-im/status-app/pull/21545) tests(@qml): add wallet account reordering tests
- PRs / Issues / Reports

### Release Testing

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:release-testing`
* owner: nastya
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Support Q3 desktop releases with test planning, exploratory testing, regression execution, and issue reporting.
- Manually test Status Desktop 2.39 and 2.40.
- Track release risks and bugs found during manual release validation.

#### Deliverables
- [status-im/status-app#21778](https://github.com/status-im/status-app/issues/21778) Seed phrase input component is cut by popup if status app is not full screen
- [status-im/status-app#21758](https://github.com/status-im/status-app/pull/21758) Focus input fix
- [status-im/status-app#21756](https://github.com/status-im/status-app/issues/21756) Typing in the seed words in confirm dialog is extremely problematic
- [status-im/status-app#21781](https://github.com/status-im/status-app/issues/21781) No prices for NVDA token on Robinhood chain
- [status-im/status-app#15120](https://github.com/status-im/status-app/issues/15120) Windows assets (icons) are blurry (poor quality?)
- [status-im/status-app#19154](https://github.com/status-im/status-app/issues/19154) PCSC error on windows if card reader is not plugged in
- [status-im/status-app#21720](https://github.com/status-im/status-app/issues/21720) Can't mute community on mobile / tablet, extra menu is not shown
- [status-im/status-app#21733](https://github.com/status-im/status-app/issues/21733) Desktop: Change password hangs in Logout/statusNode.Stop. Restart stays disabled >60s
- [status-im/status-app#21730](https://github.com/status-im/status-app/issues/21730) OnboardingLayout crashes on null keychain during startup / restart (TypeError: Cannot read property 'loading' of null)
- [status-im/status-app#21694](https://github.com/status-im/status-app/issues/21694) Desktop: Assets loading for fresh account on cold start is taking about 15 seconds
- [status-im/status-app#21732](https://github.com/status-im/status-app/issues/21732) Desktop: opening empty collectibles tab (cold start, new user profile) takes ~ 16 seconds
- [status-im/status-app#21704](https://github.com/status-im/status-app/issues/21704) Changing network in Send modal crashes the app
- [status-im/status-app#21678](https://github.com/status-im/status-app/issues/21678) N/A on Asset details for balance
- [status-im/status-app#21524](https://github.com/status-im/status-app/issues/21524) iOS app crashes on swipe-to-close action
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
* status: in progress (75%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Add more tests to track in-app performance for the desktop application on Windows from the UI side.
- Improve coverage for the main performance-sensitive user flows and make the measurements useful for regression tracking.

#### Deliverables
- [status-im/github-comment-manager#29](https://github.com/status-im/github-comment-manager/pull/29) Map status-app-benchmarks URLs to prf / bar_chart
- [status-im/status-app#21980](https://github.com/status-im/status-app/pull/21980) feat(@ci): extend Windows benchmarks job to support PR and releases
- [status-im/status-app-benchmarks#28](https://github.com/status-im/status-app-benchmarks/pull/28) desktop: richer PR listing cards and channel badges
- [status-im/status-app-benchmarks#27](https://github.com/status-im/status-app-benchmarks/pull/27) desktop: isolate nightly, PR, and release benchmark channels
- [status-im/status-app-benchmarks#26](https://github.com/status-im/status-app-benchmarks/pull/26) desktop: add deep links and collapsible scenario charts
- [status-im/status-app-benchmarks#25](https://github.com/status-im/status-app-benchmarks/pull/25) desktop: fix the encoding error
- [status-im/status-app#21732](https://github.com/status-im/status-app/issues/21732) Desktop: opening empty collectibles tab (cold start, new user profile) takes ~ 16 seconds
- [status-im/status-app#21733](https://github.com/status-im/status-app/issues/21733) Desktop: Change password hangs in Logout/statusNode.Stop. Restart stays disabled >60s
- [status-im/status-app-benchmarks#24](https://github.com/status-im/status-app-benchmarks/pull/24) desktop: polish Flags badges and escalate chronic slows to Backlog
- [status-im/status-app-benchmarks#23](https://github.com/status-im/status-app-benchmarks/pull/23) desktop: rename regression report to Flags and link known tickets
- [status-im/status-app-benchmarks#22](https://github.com/status-im/status-app-benchmarks/pull/22) desktop: add missing test stats for asset first time opening
- [status-im/status-app#21594](https://github.com/status-im/status-app/pull/21594) chore(@e2e): fix for benchmarks test
- [status-im/status-app#21590](https://github.com/status-im/status-app/pull/21590) chore(@e2e): do not rely on is_visible property for empty activity list
- [status-im/status-app-benchmarks#21](https://github.com/status-im/status-app-benchmarks/pull/21) desktop: post regression report on the website as well
- [status-im/status-app-benchmarks#20](https://github.com/status-im/status-app-benchmarks/pull/20) desktop: update summary
- [status-im/status-app-benchmarks#19](https://github.com/status-im/status-app-benchmarks/pull/19) desktop: update dashboard profile stats and add colored profile chips
- [status-im/status-app#21566](https://github.com/status-im/status-app/pull/21566) chore(@e2e): update BD for benchmark profiles to store transactions data
- [status-im/status-app#21556](https://github.com/status-im/status-app/pull/21556) chore(@e2e): do not wait for balances for benchmark tests
- [status-im/status-app-benchmarks#18](https://github.com/status-im/status-app-benchmarks/pull/18) desktop: baseline for 2.38.0
- [status-im/status-app#21542](https://github.com/status-im/status-app/pull/21542) chore(@e2e): do not wait for collectibles to be loaded in benchmark test
- [status-im/status-app-benchmarks#16](https://github.com/status-im/status-app-benchmarks/pull/16) desktop: add wallet resource metrics and improve benchmark dashboard
- [status-im/status-app-benchmarks#15](https://github.com/status-im/status-app-benchmarks/pull/15) desktop: add baselines
- [status-im/status-app-benchmarks#13](https://github.com/status-im/status-app-benchmarks/pull/13) desktop: align benchmark charts with mobile layout and split by account variant
- [status-im/status-app#21509](https://github.com/status-im/status-app/pull/21509) chore(@e2e): add fresh-user variants to desktop benchmark tests
- [status-im/status-app-benchmarks#12](https://github.com/status-im/status-app-benchmarks/pull/12) desktop: add run spread bands and responsive Plotly charts for multi-run benchmarks
- [status-im/status-app#21493](https://github.com/status-im/status-app/pull/21493) chore(@ci): collect Windows system info in nightly benchmark push
- [status-im/status-app-benchmarks#11](https://github.com/status-im/status-app-benchmarks/pull/11) desktop: small refactoring
- [status-im/status-app-benchmarks#10](https://github.com/status-im/status-app-benchmarks/pull/10) desktop: add system info panel and --machine-info for Windows benchmarks
- PRs / Issues

### Battery, CPU, and RAM usage

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:battery-cpu-ram-usage`
* owner: nastya
* status: done
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Investigate battery, CPU, and RAM usage for Status Desktop and define useful QA validation around resource consumption.
- Use [status-im/status-app#21249](https://github.com/status-im/status-app/issues/21249) as the reference issue for scope and follow-up.

#### Deliverables
- [status-im/status-app#21537](https://github.com/status-im/status-app/pull/21537) chore(@ci): fix benchmark job log path
- [status-im/status-app-benchmarks#17](https://github.com/status-im/status-app-benchmarks/pull/17) desktop: fix parser
- [status-im/status-app#21536](https://github.com/status-im/status-app/pull/21536) chore(@e2e): expand wallet performance benchmarks with CPU and RAM metrics
- [status-im/status-app-benchmarks#14](https://github.com/status-im/status-app-benchmarks/pull/14) desktop: align CPU and RAM charts with load-time chart style
- [status-im/status-app#21480](https://github.com/status-im/status-app/pull/21480) chore(@e2e): cpu data is 0 in benchmark reports
- [status-im/status-app#21475](https://github.com/status-im/status-app/pull/21475) chore(@e2e): cpu measurements fix
- PRs / Issues / Reports
- Resource usage findings linked to [status-im/status-app#21249](https://github.com/status-im/status-app/issues/21249).

### E2E tests for keycard with mock

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:e2e-kyecard-mock`
* owner: nastya
* status: in progress (41%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Once keycard mock is ready (new implementation), bring back to life existing e2e tests if possible or create new ones, to cover main keycard interactions with desktop app
- Work with infra team (if needed) to build proper app (the one that will use keycard mock), including macOS

#### Deliverables
- [status-im/status-app#21944](https://github.com/status-im/status-app/pull/21944) tests(@qml): cover keycard login, management and re-auth UI states
- [status-im/status-app#21938](https://github.com/status-im/status-app/pull/21938) tests(@e2e): import known seed onto card and create profile with keycard simulator
- [status-im/status-app#21875](https://github.com/status-im/status-app/pull/21875) fix(keycard): make packaged simulator work on Linux and Windows
- [status-im/status-app#21871](https://github.com/status-im/status-app/issues/21871) Simulated keycard does not work in packaged build on Linux and Windows
- [status-im/status-app#21863](https://github.com/status-im/status-app/pull/21863) chore(@ci): allow launching keycard tests in manual job
- [status-im/status-app#21867](https://github.com/status-im/status-app/issues/21867) Update manual jenkins job to run keycard tests on demand
- [status-im/status-app#21665](https://github.com/status-im/status-app/pull/21665) tests(@e2e): keycard simulator infrastructure and onboarding scenario
- [status-im/status-app#21722](https://github.com/status-im/status-app/issues/21722) App crashes on login when creating account with keycard simulator
- [status-im/status-app#21667](https://github.com/status-im/status-app/issues/21667) Starting keycard simulator fails in packaged app — looks for vendor/ source tree
- [status-im/status-app#21680](https://github.com/status-im/status-app/issues/21680) Keycard Simulator Restart resets UI only, not keycard-qt simulated backend
- PRs / Issues / Reports

### Performance tests for desktop application on Linux

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:linux-performance-tests`
* owner: nastya
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Add tests to track in-app performance for the desktop application on Linux from the UI side.
- Improve coverage for the main performance-sensitive user flows and make the measurements useful for regression tracking.

#### Deliverables
- PRs / Issues

### Performance tests for desktop application on Mac

* fully qualified name: `ift-ts:qa:status:2026q3-status-qa-desktop:mac-performance-tests`
* owner: nastya
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Add tests to track in-app performance for the desktop application on Mac from the UI side.
- Improve coverage for the main performance-sensitive user flows and make the measurements useful for regression tracking.

#### Deliverables
- PRs / Issues
