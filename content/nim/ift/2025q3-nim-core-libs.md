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

### Extract and Set Up an Integer Library

fully qualified name: `vac:nim:ift:2025q3-nim-core-libs:extract-and-set-up-an-integer-library`
* owner: Esteban
* status:
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description

- Extract low-level primitives from [`stint/private/primitives`](https://github.com/status-im/nim-stint/tree/master/stint/private/primitives) to form a standalone library focused on CPU-sized integers, removing stint-specific dependencies and organizing the code into a clean, modular structure.

### Design Integer Library Architecture

fully qualified name: `vac:nim:ift:2025q3-nim-core-libs:design-integer-library-architecture`
* owner: Esteban
* status:
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description

- Design the library following inspirations from [Rust’s integer intrinsics discussion](https://github.com/rust-lang/rust/issues/85532), [`nim-stew` PR #187](https://github.com/status-im/nim-stew/pull/187), and Constantine’s arithmetic internals ([link](https://github.com/mratsim/constantine/tree/master/constantine/math_arbitrary_precision/arithmetic)), exposing a reusable low-level API with proper abstraction over platform- and compiler-specific differences.

### Finalize and Integrate Integer Library

fully qualified name: `vac:nim:ift:2025q3-nim-core-libs:finalize-and-integrate-integer-library`
* owner: Esteban
* status:
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description

- Ensure the library is testable, well-documented, and performant across platforms, with example integrations or adapters for projects like Stint, Constantine, or future bigint/cryptographic libraries with the goal of being reused in bigint and crypto projects.