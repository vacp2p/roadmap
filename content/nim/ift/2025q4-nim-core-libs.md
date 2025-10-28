---
title: 2025q4 Nim Core Libraries
tags:
  - "2025q4"
  - "nim"
  - "ift"
draft: false
description: Continue evolving Nim core libraries.
---

`vac:nim:ift:2025q4-nim-core-libs`

## Description
Maintain and extend the foundational Nim libraries required by IFT teams, delivering portable CPU integer primitives and improved CLI parsing utilities.

## Task List

### Create Standalone CPU Integer Library

* fully qualified name: `vac:nim:ift:2025q4-nim-core-libs:cpu-integer-library`
* owner: Esteban
* status: not started
* start-date: 2025/11/15
* end-date: 2025/12/31

#### Description
- Extract low-level, hardware- and compiler-specific primitives from [`stint/private/primitives`](https://github.com/status-im/nim-stint/tree/master/stint/private/primitives) and turn them into a reusable, standalone library for CPU-sized integers. Model the design after [Rust’s integer intrinsics](https://github.com/rust-lang/rust/issues/85532), [`nim-stew` PR #187](https://github.com/status-im/nim-stew/pull/187), and [Constantine’s arithmetic core](https://github.com/mratsim/constantine/tree/master/constantine/math_arbitrary_precision/arithmetic), with clean abstractions, cross-platform support, and a minimal, well-documented API. The resulting library should serve as a foundational building block for bigint and cryptographic libraries like Stint and Constantine.

#### Deliverables
- PRs/Issues/Docs/Reports

### Command line parsers

* fully qualified name: `vac:nim:ift:2025q4-nim-core-libs:command-line-parsers`
* owner: Esteban
* status: not started
* start-date: 2025/11/15
* end-date: 2025/12/31

#### Description
Advance command-line parsing utilities (e.g. https://github.com/status-im/nim-confutils), covering new ergonomics and integration support for Nim projects.

#### Deliverables
- PRs/Issues/Docs/Reports
