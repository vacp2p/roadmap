---

title: Logos Messaging nim-ffi Integration
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Support logos-messaging usage of nim-ffi features in nim-libp2p

---

`ift-ts:p2p:ift:2026q3-logos-messaging-nim-ffi-integration`

Assist the logos-messaging team in implementing and using `nim-ffi` features
needed by nim-libp2p, with the goal of replacing the current C bindings path
with a cleaner Nim-based integration path where practical.

## Description

Logos Messaging is evolving `nim-ffi` to support safer and more ergonomic
cross-language integration. P2P should help align those capabilities with
nim-libp2p needs so downstream consumers can move away from custom C binding
surfaces over time.

This work continues the Q2 `nim-ffi` alignment and focuses on features required
to use nim-libp2p through the improved integration path.

## Task List

### Integration Support

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-messaging-nim-ffi-integration:integration-support`
* owner: gabe
* status: in progress (65%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Support implementation and testing of `nim-ffi` features that unblock
nim-libp2p usage. This may include reviewing designs, contributing fixes,
writing compatibility tests, or adapting nim-libp2p wrappers.

#### Deliverables
- [logos-messaging/nim-ffi#119](https://github.com/logos-messaging/nim-ffi/pull/119) feat: shrink the genbindings incantation
- [logos-messaging/nim-ffi#116](https://github.com/logos-messaging/nim-ffi/pull/116) feat(ffi): compile-time validation of --nimMainPrefix
- [logos-messaging/nim-ffi#117](https://github.com/logos-messaging/nim-ffi/pull/117) feat(nimble): actionable remediation message on stale-bindings check failure
- [logos-messaging/nim-ffi#121](https://github.com/logos-messaging/nim-ffi/pull/121) docs: complete the README workflow story
- [logos-messaging/nim-ffi#120](https://github.com/logos-messaging/nim-ffi/pull/120) feat(ffi): make the scalar-fast-path binding drop loud
- [logos-messaging/nim-ffi#115](https://github.com/logos-messaging/nim-ffi/pull/115) feat(ffi): async teardown hook for {.ffiDtor.}
- `nim-ffi` features or fixes needed by nim-libp2p
- Compatibility tests for selected nim-libp2p integration scenarios
- Migration notes comparing `nim-ffi` usage with existing C bindings
- [logos-messaging/nim-ffi#103](https://github.com/logos-messaging/nim-ffi/pull/103) fix(ffi): regenerate stale echo C++ bindings and guard them in check_bindings_cpp
- [logos-messaging/nim-ffi#104](https://github.com/logos-messaging/nim-ffi/pull/104) refactor(codegen): shared FFIType IR + single type parser for C/C++/Rust
- [logos-messaging/nim-ffi#106](https://github.com/logos-messaging/nim-ffi/pull/106) feat(ffi): CBOR-free scalar fast path for all-scalar `abi = c` procs
- [logos-messaging/nim-ffi#107](https://github.com/logos-messaging/nim-ffi/pull/107) feat(ffi): slab-allocate event payloads instead of c_malloc per dispatch
- [logos-messaging/nim-ffi#108](https://github.com/logos-messaging/nim-ffi/pull/108) feat(ffi): configurable per-request handler timeout with a finite default (#93)
- [logos-messaging/nim-ffi#109](https://github.com/logos-messaging/nim-ffi/pull/109) feat: CBOR-free abi=c C bindings (-d:targetLang=c_abi)
- [logos-messaging/nim-ffi#110](https://github.com/logos-messaging/nim-ffi/pull/110) feat: CBOR-free scalar fast path for abi=c procs
- [logos-messaging/nim-ffi#111](https://github.com/logos-messaging/nim-ffi/pull/111) feat(devx): derive ffiEvent wire name, guard genBindings ordering, real README


### Migration Path

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-messaging-nim-ffi-integration:migration-path`
* owner: gabe
* status: in progress (70%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Define how projects can migrate from the current C bindings to the cleaner
`nim-ffi` integration path without breaking existing users.

#### Deliverables
- [vacp2p/nim-libp2p#2775](https://github.com/vacp2p/nim-libp2p/pull/2775) chore(cbind): nim-ffi migration [4/9] — streams & custom protocols (+ echo example)
- [vacp2p/nim-libp2p#2774](https://github.com/vacp2p/nim-libp2p/pull/2774) chore(cbind): nim-ffi migration [3/9] — connectivity & identity
- [vacp2p/nim-libp2p#2773](https://github.com/vacp2p/nim-libp2p/pull/2773) chore(cbind): nim-ffi migration [2/9] — new-library scaffold + CI
- [vacp2p/nim-libp2p#2784](https://github.com/vacp2p/nim-libp2p/pull/2784) fix(ci): daily runnableExamples check skips vendored Nim compiler
- [vacp2p/nim-libp2p#2772](https://github.com/vacp2p/nim-libp2p/pull/2772) chore(cbind): nim-ffi migration [1/9] — deps + pinning scaffold
- Incremental migration plan for existing binding users
- Compatibility notes for APIs that must remain available
- Follow-up commitments or issues for work beyond Q3
- [logos-messaging/nim-ffi#102](https://github.com/logos-messaging/nim-ffi/pull/102) feat(codegen): C binding generator (-d:targetLang=c)
