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
* owner: Constantine
* status: done
* start-date: 2025/11/15
* end-date: 2025/12/31

#### Description
- Extract low-level, hardware- and compiler-specific primitives from [`stint/private/primitives`](https://github.com/status-im/nim-stint/tree/master/stint/private/primitives) and turn them into a reusable, standalone library for CPU-sized integers. Model the design after [Rust’s integer intrinsics](https://github.com/rust-lang/rust/issues/85532), [`nim-stew` PR #187](https://github.com/status-im/nim-stew/pull/187), and [Constantine’s arithmetic core](https://github.com/mratsim/constantine/tree/master/constantine/math_arbitrary_precision/arithmetic), with clean abstractions, cross-platform support, and a minimal, well-documented API. The resulting library should serve as a foundational building block for bigint and cryptographic libraries like Stint and Constantine.

#### Deliverables
- [vacp2p/nim-intops#9](https://github.com/vacp2p/nim-intops/pull/9)
- [vacp2p/nim-intops#8](https://github.com/vacp2p/nim-intops/pull/8)
- [vacp2p/nim-intops#7](https://github.com/vacp2p/nim-intops/pull/7)
- [vacp2p/nim-intops#2](https://github.com/vacp2p/nim-intops/pull/2)
- [Added 32-bit integer support and migrated tests to unittest2](https://github.com/vacp2p/nim-intops/pull/5)
- [Repository bootstrap with overflow/saturating arithmetic and tests](https://github.com/status-im/nim-intops)
- [API docs for nim-intops](https://vacp2p.github.io/nim-intops/apidocs/intops.html)
- [CI workflows for tests and docs](https://github.com/vacp2p/nim-intops/tree/develop/.github/workflows)

### Command line parsers

* fully qualified name: `vac:nim:ift:2025q4-nim-core-libs:command-line-parsers`
* owner: Esteban
* status: done
* start-date: 2025/11/15
* end-date: 2025/12/30

#### Description
Advance command-line parsing utilities (e.g. https://github.com/status-im/nim-confutils), covering new ergonomics and integration support for Nim projects.

#### Deliverables
- [status-im/nimbus-eth2#7826](https://github.com/status-im/nimbus-eth2/pull/7826) Use confutils obsolete for deprecated beacon node conf options
- [status-im/nim-confutils#140](https://github.com/status-im/nim-confutils/pull/140) Fix #50; support multiple subcommands in a case branch
- [nim-lang/Nim#25401](https://github.com/nim-lang/Nim/pull/25401) Add parseEnum support for triple-quoted and raw string enum values
- [status-im/nim-confutils#138](https://github.com/status-im/nim-confutils/pull/138) Fix #60; display default subcommand desc in help message
- [status-im/nim-confutils#136](https://github.com/status-im/nim-confutils/pull/136) Fix #62; add obsolete pragma
- [status-im/nim-confutils#135](https://github.com/status-im/nim-confutils/pull/135) Fix #74; envVarsPrefix app file name when not set
- [status-im/nim-confutils#134](https://github.com/status-im/nim-confutils/pull/134) Fix #87; support env var value list
- [status-im/nim-confutils#123](https://github.com/status-im/nim-confutils/pull/123) Fix #112; add results.Opt support
- [status-im/nim-confutils#132](https://github.com/status-im/nim-confutils/pull/132) Allow passing params to file decode
- [status-im/nim-confutils#131](https://github.com/status-im/nim-confutils/pull/131) Include debug arg in help desc only if used
- [status-im/nim-confutils#130](https://github.com/status-im/nim-confutils/pull/130) fix dispatch
- [status-im/nim-confutils#126](https://github.com/status-im/nim-confutils/pull/126) add debug tag for command line option
- [status-im/nim-confutils#129](https://github.com/status-im/nim-confutils/pull/129) documentation clean up
- [status-im/nim-confutils#127](https://github.com/status-im/nim-confutils/pull/127) fix #90; print help/version correctly
- [status-im/nim-confutils#128](https://github.com/status-im/nim-confutils/pull/128) fix #45; handle unsigned args
- [Argument alignment in --help](https://github.com/status-im/nim-confutils/pull/125)
- [Nested cmd config file test](https://github.com/status-im/nim-confutils/pull/124)
- [Fix #39; show case option in --help](https://github.com/status-im/nim-confutils/pull/122)
- [Fix #40; Help output regression tests](https://github.com/status-im/nim-confutils/pull/121)
- [Fix #15; show argument in --help](https://github.com/status-im/nim-confutils/pull/120)
- [fix #29; subcommand --help shows global options #119](https://github.com/status-im/nim-confutils/pull/119)
