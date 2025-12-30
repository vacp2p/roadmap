---
title: 2025q4 Nimble
tags:
  - 2025q4
  - nim
  - ift
draft: false
description: Nimble development.
---

`vac:nim:ift:2025q4-nimble`

## Description

This commitment comprises advancing Nimble as a robust replacement for Nimbus build system while enhancing its overall functionality.
We will focus on three key milestones:

* implementing declarative parsing
* expanding the feature set
* establishing a local-by-default approach.

Our primary objective is to streamline the development process by improving IDE integration,
making Nimble more user-friendly and efficient.
We'll prioritize these enhancements to bring Nimble closer to its 1.0 release, ensuring it becomes a more powerful and versatile tool for our developers.
By the end of this quarter, we aim to have made significant progress on these fronts, setting the stage for Nimble to become the go-to package manager in IFT projects.


## Task List

### Nimble 1.0.0

* fully qualified name: `vac:nim:ift:2025q4-nimble:nimble-1.0.0`
* owner: jmgomez
* status: done
* start-date: 2025/10/01
* end-date: 2025/12/30

#### Description

All the relevant information can be found in [this GitHub issue](https://github.com/nim-lang/nimble/issues/1449).

#### Deliverables
- [Fixes Infinite Reading official package list](https://github.com/nim-lang/nimble/pull/1545)
- [Filter declarative parser warnings to solution packages only](https://github.com/nim-lang/nimble/pull/1544)
- [Adds paths to nimble.nim.cfg to circunvent skipParentConfig when bootstrapping](https://github.com/nim-lang/nimble/pull/1543)
- [Nim is added by default to the lock file](https://github.com/nim-lang/nimble/pull/1538)
- [Track git errors during package discovery and show them](https://github.com/nim-lang/nimble/pull/1542)
- [Nim special version can be used in requires](https://github.com/nim-lang/nimble/pull/1539)
- [Fixes #1495 ^= version operator yields warning](https://github.com/nim-lang/nimble/pull/1530)
- [Cleans up dep logs. Fixes #1487](https://github.com/nim-lang/nimble/pull/1529)
- [Package downloads improvements](https://github.com/nim-lang/nimble/pull/1526)
- [Use releases.json as source of truth for nim binaries](https://github.com/nim-lang/nimble/pull/1525)
- [Simplifies install dir bottleneck #1520](https://github.com/nim-lang/nimble/pull/1520)
- [Add nim-chronos v4.0.4 as submodule #1518](https://github.com/nim-lang/nimble/pull/1518)
- [Atomic parser fallback #1517](https://github.com/nim-lang/nimble/pull/1517)
- [Use Nim binaries when no system is present for bootstrap nim #1516](https://github.com/nim-lang/nimble/pull/1516)
- [Fix before install to keep hook execution graph #1515](https://github.com/nim-lang/nimble/pull/1515)
- [Refactor Nim bin parametrization and bootstrap fixes #1514](https://github.com/nim-lang/nimble/pull/1514)
- [Fixes nimble add assertion defect #1512](https://github.com/nim-lang/nimble/pull/1512)
- [Adds call tree to instrumentation #1511](https://github.com/nim-lang/nimble/pull/1511)
- [optimizes some nimblesat funcs #1507](https://github.com/nim-lang/nimble/pull/1507)
- [Adds instrument tools #1506](https://github.com/nim-lang/nimble/pull/1506)
- [Always build installed deps #1505](https://github.com/nim-lang/nimble/pull/1505)
- [Run setup for every action the solver is ran #1503](https://github.com/nim-lang/nimble/pull/1503)
- [Adds support for deps in `vnext` Fixes #1496](https://github.com/nim-lang/nimble/pull/1499)
