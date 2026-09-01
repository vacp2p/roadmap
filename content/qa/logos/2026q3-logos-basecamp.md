---
title: Logos Basecamp QA
tags:
  - "2026q3"
  - "qa"
  - "logos"
draft: false
description: Validate Logos Basecamp release artifacts, module workflows, and desktop shell reliability.
---

`ift-ts:qa:logos:2026q3-logos-basecamp`

## Description
Validate [logos-co/logos-basecamp](https://github.com/logos-co/logos-basecamp) as the Logos desktop application shell.
Q3 QA should build on the existing smoke, UI, sandbox, and doctest coverage while focusing on release confidence and core module workflows.

## Task List

### Release validation

* fully qualified name: `ift-ts:qa:logos:2026q3-logos-basecamp:release-validation`
* owner: tbd
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Validate Basecamp release artifacts and confirm the app starts cleanly on supported platforms.

#### Deliverables
- Release validation notes / checklist.
- Issues for startup, packaging, or release regressions.

### Package and module workflows

* fully qualified name: `ift-ts:qa:logos:2026q3-logos-basecamp:package-and-module-workflows`
* owner: tbd
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Validate the main package manager and module workflows, including install, launch, update/reinstall, and module compatibility scenarios where feasible.

#### Deliverables
- PRs / Issues / Reports.
- Notes on package manager or module compatibility gaps.

### MCP tests

* fully qualified name: `ift-ts:qa:logos:2026q3-logos-basecamp:mcp-tests`
* owner: Roman
* status: in progress (20%)
* start-date: 2026/08/17
* end-date: 2026/09/30

#### Description

Add UI integration coverage for MCP preparation, installation navigation, and Basecamp workspace application lifecycle behavior.

#### Deliverables

- [logos-co/logos-basecamp#338](https://github.com/logos-co/logos-basecamp/pull/338) Test/MCP preparation UI tests
- [logos-co/logos-basecamp#342](https://github.com/logos-co/logos-basecamp/pull/342) Test/MCP UI welcome Install now navigates to Applications
- [logos-co/logos-basecamp#343](https://github.com/logos-co/logos-basecamp/pull/343) Test/pre-seed test_qml_only app for integration-test boot
- MCP preparation and installation UI coverage
- Workspace coverage for opening, closing, and reopening applications

### Test coverage and maintenance

* fully qualified name: `ift-ts:qa:logos:2026q3-logos-basecamp:maintenance`
* owner: Roman
* status: in progress (75%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Maintain and extend the existing Basecamp smoke, UI, sandbox, and doctest coverage as the project evolves.

#### Deliverables
- [logos-co/logos-basecamp#329](https://github.com/logos-co/logos-basecamp/pull/329) Test/module unload
- [logos-co/logos-basecamp#312](https://github.com/logos-co/logos-basecamp/pull/312) Test/missing dependencies
- [logos-co/logos-basecamp#317](https://github.com/logos-co/logos-basecamp/pull/317) Test/persistence portability
- [Logos Basecamp v0.2.3 release validation](https://github.com/logos-co/logos-basecamp/releases/tag/0.2.3), with 13 findings shared with developers.
- [logos-co/logos-basecamp#293](https://github.com/logos-co/logos-basecamp/pull/293) Chore/add coverage report
- [logos-co/logos-basecamp#298](https://github.com/logos-co/logos-basecamp/pull/298) Test/basecamp package lifecycle
- [logos-co/logos-basecamp#303](https://github.com/logos-co/logos-basecamp/pull/303) Fix/pin release test modules
- [logos-co/logos-basecamp#301](https://github.com/logos-co/logos-basecamp/issues/301) bug: Package Manager view unresponsive after package_manager_ui unload
- [logos-co/logos-basecamp#308](https://github.com/logos-co/logos-basecamp/issues/308) bug: uiPluginFileInstalled never emitted for QML-only packages
- [logos-co/logos-basecamp#286](https://github.com/logos-co/logos-basecamp/pull/286) Chore/add remaining tests to CI
- [logos-co/logos-basecamp#284](https://github.com/logos-co/logos-basecamp/pull/284) Fix/qml tests and references in flake file
- PRs extending or stabilizing tests.
- Issues for uncovered regressions or flaky scenarios.
