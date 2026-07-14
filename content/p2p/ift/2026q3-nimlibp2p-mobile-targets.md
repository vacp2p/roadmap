---

title: nim-libp2p Mobile Targets
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Add Android and iOS build support for nim-libp2p

---

`ift-ts:p2p:ift:2026q3-nimlibp2p-mobile-targets`

Add support for compiling nim-libp2p for Android and iOS targets, including
Android `arm64-v8a`, Android `x86_64`, iOS `arm64`, and iOS simulator `arm64`.

## Description

nim-libp2p should be buildable for mobile targets so downstream teams can embed
libp2p functionality in Android and iOS applications. The Q3 scope is to make
cross-compilation repeatable, document the toolchains, add CI coverage where
practical, and provide a small example app or smoke-test integration.

CI coverage should be included for targets where build time and available
runners make it practical. If full CI is too expensive, the commitment should
still provide documented local build commands and at least one automated smoke
path.

## Task List

### Cross-Compilation Support

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-mobile-targets:cross-compilation`
* owner: Richard
* status: in progress (80%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Define the supported Android and iOS build matrix and document the toolchains,
Nim configuration, C toolchain flags, and dependency constraints needed for
mobile builds.

Add the build configuration and dependency fixes needed for nim-libp2p to
compile for the selected mobile targets.

#### Deliverables
- [vacp2p/nim-lsquic#98](https://github.com/vacp2p/nim-lsquic/pull/98) fix: android msg_iovlen type
- Android `arm64-v8a` build succeeds
- Android `x86_64` build succeeds
- iOS `arm64` build succeeds
- iOS simulator `arm64` build succeeds
- Platform-specific dependency issues documented or fixed


### CI And Example App

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-mobile-targets:ci-example`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30
#### Description
Add CI or smoke-build coverage for mobile targets and provide a small example
application or integration harness that proves nim-libp2p can be linked and
started on mobile.

#### Deliverables
- CI smoke builds for feasible Android and iOS targets
- Example app or minimal integration harness
- Documentation for running the example locally
