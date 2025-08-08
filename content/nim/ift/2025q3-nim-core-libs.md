---
title: nim core libraries
tags:
  - 2025q3
  - nim
  - ift
draft: false
description:
---

`vac:nim:ift:2025q3-nim-core-libs`

## Description

## Task List

### Add cbor support to json: [https://github.com/status-im/nim-json-serialization](https://github.com/status-im/nim-json-serialization "https://github.com/status-im/nim-json-serialization")

(info: cbor is needed for QT at compile time)

fully qualified name: `vac:nim:ift:2025q3-nim-core-libs:add-cbor-supoort-to-json`
* owner: Esteban
* status:
* start-date: 2025/07/01
* end-date: 2025/09/30

### Compile time support for json and cbor

fully qualified name: `vac:nim:ift:2025q3-nim-core-libs:compile-time-support-for-json-and-cbor`
* owner: Esteban
* status:
* start-date: 2025/07/01
* end-date: 2025/09/30

### Create Standalone CPU Integer Library

fully qualified name: `vac:nim:ift:2025q3-nim-core-libs:extract-and-set-up-an-integer-library`
* owner: Arnaud
* status:
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description

- Extract low-level, hardware- and compiler-specific primitives from [`stint/private/primitives`](https://github.com/status-im/nim-stint/tree/master/stint/private/primitives) and turn them into a reusable, standalone library for CPU-sized integers. Model the design after [Rust’s integer intrinsics](https://github.com/rust-lang/rust/issues/85532), [`nim-stew` PR #187](https://github.com/status-im/nim-stew/pull/187), and [Constantine’s arithmetic core](https://github.com/mratsim/constantine/tree/master/constantine/math_arbitrary_precision/arithmetic), with clean abstractions, cross-platform support, and a minimal, well-documented API. The resulting library should serve as a foundational building block for bigint and cryptographic libraries like Stint and Constantine.