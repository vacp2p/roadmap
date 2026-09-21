---
title: 2026q4 Nim Core Libraries
tags:
  - "2026q4"
  - "nim"
  - "ift"
draft: false
description: Maintain Nim core libraries, improve documentation, and integrate nimlangserver fixes with a consistent LSP protocol model.
---

`ift-ts:nim:ift:2026q4-nim-core-libs`

## Description

Maintain and document the foundational Nim libraries used by IFT teams.
Improve nimlangserver by reviewing and integrating applicable fixes from the recent fork and following the separation of protocol handling, JSON serialization, and protocol data models used by nim-web3.

## Task List

### Documentation Improvement

* fully qualified name: `ift-ts:nim:ift:2026q4-nim-core-libs:docs-improvement`
* owner: Constantine
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Continue improving documentation for Nim core libraries, including missing API guidance, runnable examples, and integration notes needed by downstream teams.
Improve documentation tooling where it helps keep package documentation accurate and maintainable.

#### Deliverables

- Documentation PRs covering identified gaps and downstream usage examples.
- Documentation tooling improvements and validation of the updated examples or builds.

### Maintenance

* fully qualified name: `ift-ts:nim:ift:2026q4-nim-core-libs:maintenance`
* owner: Constantine
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Provide ongoing maintenance and fixes across Nim core libraries.
Triage issues, address regressions and compatibility problems, support downstream consumers, and maintain tests and CI as dependencies and toolchains evolve.

#### Deliverables

- PRs fixing library defects and maintaining compatibility, tests, and CI.
- Tracked issues and verification results for downstream integration problems.

### Nimlangserver improvements

* fully qualified name: `ift-ts:nim:ift:2026q4-nim-core-libs:nimlangserver`
* owner: TBD
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Review the recent nimlangserver fork and cherry-pick applicable improvements and fixes into the team's maintained branch, adapting changes where needed.
Identify the fork URL, source commits, and target branch before selecting changes; these references remain to be specified.

Use the nim-web3 approach as the model for the LSP implementation:
- Keep JSON-RPC protocol handling in `nim-json-rpc`.
- Define an LSP-specific `nim-json-ser` flavor for interpreting and emitting protocol JSON, including null values, number formatting, and missing or extra fields.
- Represent the protocol data model with Nim objects that map directly to the [LSP 3.18 specification](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/), starting with the messages and structures used by nimlangserver today.
- Make additional protocol objects straightforward to add using the same model. Generating objects from the specification is optional; the task does not require implementing every LSP feature.
- Add regression tests for imported fixes and serialization tests for the supported protocol objects and edge cases.

#### Deliverables

- A fork review identifying source commits, target branch, selected fixes, and deferred changes.
- PRs integrating applicable fork fixes and improvements into the maintained branch.
- An LSP JSON serialization flavor and Nim protocol objects for the currently used messages and structures.
- Regression and serialization tests, plus guidance for adding further protocol objects.
