---
title: 2025q3 Nim Core Libraries
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

### Nim cbor serialization

(info: cbor is needed for QT at compile time)

fully qualified name: `vac:nim:ift:2025q3-nim-core-libs:nim-cbor-serialization`
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

### Add ABI Codec Support to nim-web3

fully qualified name: `vac:nim:ift:2025q3-nim-core-libs:add-abi-codec-support-to-nim-web3`
* owner: Arnaud
* status:
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description

- Add [ABI encoder](https://github.com/codex-storage/nim-contract-abi) and decoder support to [nim-web3](https://github.com/status-im/nim-web3), enabling serialization and deserialization of static and dynamic types (including nested tuples, strings, and arrays). This should be Integrated with the nim-serialization ecosystem and inspired by contractabi from Codex, but rewritten using nim-faststream for better performance. Good test coverage is a must.

### Create Standalone CPU Integer Library

fully qualified name: `vac:nim:ift:2025q3-nim-core-libs:extract-and-set-up-an-integer-library`
* owner: Arnaud
* status:
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description

- Extract low-level, hardware- and compiler-specific primitives from [`stint/private/primitives`](https://github.com/status-im/nim-stint/tree/master/stint/private/primitives) and turn them into a reusable, standalone library for CPU-sized integers. Model the design after [Rust’s integer intrinsics](https://github.com/rust-lang/rust/issues/85532), [`nim-stew` PR #187](https://github.com/status-im/nim-stew/pull/187), and [Constantine’s arithmetic core](https://github.com/mratsim/constantine/tree/master/constantine/math_arbitrary_precision/arithmetic), with clean abstractions, cross-platform support, and a minimal, well-documented API. The resulting library should serve as a foundational building block for bigint and cryptographic libraries like Stint and Constantine.