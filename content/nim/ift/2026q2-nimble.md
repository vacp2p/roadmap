---
title: 2026q2 Nimble
tags:
  - 2026q2
  - nim
  - ift
draft: false
description: Nimble development.
---

`ift-ts:nim:ift:2026q2-nimble`

## Description

This commitment comprises advancing Nimble as a robust replacement for Nimbus build system while enhancing its overall functionality.
In Q2 we will focus on resolver improvements and solver architecture work that are also relevant for Logos package-manager efforts.
The emphasis is on improving correctness, maintainability, and user-facing error quality.

## Task List

### Nimble 1.0.0

* fully qualified name: `ift-ts:nim:ift:2026q2-nimble:nimble-1.0.0`
* owner: Juan
* status: in progress (10%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

All the relevant information can be found in [this GitHub issue](https://github.com/nim-lang/nimble/issues/1449).
This remains the short-term roadmap for replacing pieces of the Nimbus build system bit by bit while improving Nimble overall.

#### Deliverables
- [nim-lang/nimble#1680](https://github.com/nim-lang/nimble/pull/1680) Make async discovery the default
- [nim-lang/nimble#1679](https://github.com/nim-lang/nimble/pull/1679) Remove old sync version discovery path, add `--discovery:sync|async` flag
- [nim-lang/nimble#1676](https://github.com/nim-lang/nimble/pull/1676) Enable async parallel package version discovery
- [nim-lang/nimble#1668](https://github.com/nim-lang/nimble/pull/1668) Dissolve vnext
- [nim-lang/nimble#1667](https://github.com/nim-lang/nimble/pull/1667) Update version to 0.99.1
- [nim-lang/nimble#1665](https://github.com/nim-lang/nimble/pull/1665) refactor: extract version discovery into versiondiscovery.nim
- [nim-lang/nimble#1664](https://github.com/nim-lang/nimble/pull/1664) fix(#1663): use absolutePath for nimble dump to handle absolute paths
- [nim-lang/nimble#1662](https://github.com/nim-lang/nimble/pull/1662) fix(#1648): prefer installed package versions over cached ones in SAT solver
- [nim-lang/nimble#1661](https://github.com/nim-lang/nimble/pull/1661) Fixes #1650 use system temp dir so config.nims doesnt get leaked into
- [nim-lang/nimble#1660](https://github.com/nim-lang/nimble/pull/1660) adds an alias to to specify localdeps
- [nim-lang/nimble#1659](https://github.com/nim-lang/nimble/pull/1659) fix: feature resolution and SAT feature expansion for file:// URL
- [nim-lang/nimble#1654](https://github.com/nim-lang/nimble/pull/1654) refactor: unify getPkgInfo entry point

### Resolver Improvements

* fully qualified name: `ift-ts:nim:ift:2026q2-nimble:resolver-improvements`
* owner: Juan
* status: not started
* start-date: 2026/04/01
* end-date: 2026/05/15

#### Description
- Improve the current Nimble resolver implementation.
- Capture the relevant learnings that can inform work on the Logos package manager.
- Keep the work aligned with Nimble's short-term roadmap of replacing parts of the Nimbus build system incrementally.

#### Deliverables
- PRs/Issues/Docs/Reports

### SAT Solver Review and PubGrub Evaluation

* fully qualified name: `ift-ts:nim:ift:2026q2-nimble:sat-solver-pubgrub-evaluation`
* owner: Juan
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/15

#### Description
- Review the current SAT solver implementation and investigate replacing it with PubGrub, as used in Dart.
- The main motivation is to improve the quality of dependency-resolution errors, which are currently too hard to understand in practice.

#### Deliverables
- PRs/Issues/Docs/Reports

### MinVer Implementation for Version Extremity Testing

* fully qualified name: `ift-ts:nim:ift:2026q2-nimble:minver-version-extremity-testing`
* owner: Juan
* status: not started
* start-date: 2026/05/15
* end-date: 2026/06/15

#### Description
- Implement a MinVer-style capability for version extremity testing in Nimble.
- Support testing libraries against both the newest and oldest versions permitted by their `requires` ranges.
- This should make it easier to validate version-range behavior systematically instead of only testing the latest allowed dependency set.

#### Deliverables
- PRs/Issues/Docs/Reports

### Application Packaging Support

* fully qualified name: `ift-ts:nim:ift:2026q2-nimble:application-packaging`
* owner: Juan
* status: not started
* start-date: 2026/06/01
* end-date: 2026/06/30

#### Description
- Improve packaging support so Nimble applications can be distributed more easily as ready-made binaries and installers.
- Explore how to turn the ideas proven in Nora, Status Desktop, and related efforts into a more straightforward "packaging for dummies" workflow for Nim applications, including targets such as Android apps, AppImage, and NSIS installers.

#### Deliverables
- PRs/Issues/Docs/Reports
