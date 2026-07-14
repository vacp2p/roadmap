---
title: 2026q3 Nimble
tags:
  - 2026q3
  - nim
  - ift
draft: false
description: Nimble development.
---

`ift-ts:nim:ift:2026q3-nimble`

## Description

This commitment comprises advancing Nimble as a robust replacement for Nimbus build system while enhancing its overall functionality.
In Q3 we will continue the Nimble 1.0.0 track and migrate remaining HTTP download paths toward Chronos.

## Task List

### Nimble 1.0.0

* fully qualified name: `ift-ts:nim:ift:2026q3-nimble:nimble-1.0.0`
* owner: Juan
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description

All the relevant information can be found in [this GitHub issue](https://github.com/nim-lang/nimble/issues/1449).
This remains the short-term roadmap for replacing pieces of the Nimbus build system bit by bit while improving Nimble overall.

#### Deliverables
- Released Nimble 0.24.0.
- [nim-lang/nimble#1766](https://github.com/nim-lang/nimble/pull/1766) Bump 0.24.0
- [nim-lang/nimble#1764](https://github.com/nim-lang/nimble/pull/1764) develop --with-dependencies vendors nim when the lock file pins it
- [nim-lang/nimble#1762](https://github.com/nim-lang/nimble/pull/1762) fixes nimble lock emitting empty url/checksum for develop dependencies
- [nim-lang/nimble#1761](https://github.com/nim-lang/nimble/pull/1761) fixes #1758: build Nim from source when the .tar.xz binary can't be extracted
- [nim-lang/nimble#1760](https://github.com/nim-lang/nimble/pull/1760) fixes #1757: detect system Nim on layouts without a nim.nimble
- [nim-lang/nimble#1759](https://github.com/nim-lang/nimble/pull/1759) Fix binary workflow
- [nim-lang/nimble#1757](https://github.com/nim-lang/nimble/issues/1757) Nimble won't detect system Nim
- [nim-lang/nimble#1758](https://github.com/nim-lang/nimble/issues/1758) `nimble install nim` should not require xz-utils
- [nim-lang/nimble#1755](https://github.com/nim-lang/nimble/pull/1755) fixes #1752 set psInstalled for packages read from pkgs2
- [nim-lang/nimble#1753](https://github.com/nim-lang/nimble/pull/1753) Adds semver pre-release version ordering and parsing support
- [nim-lang/nimble#1751](https://github.com/nim-lang/nimble/pull/1751) Introduces resolver:min|max version selection
- [nim-lang/nimble#1750](https://github.com/nim-lang/nimble/pull/1750) fix: extract Nim .tar.xz with tar when unxz is absent

### Chronos HTTP downloads

* fully qualified name: `ift-ts:nim:ift:2026q3-nimble:chronos-http-downloads`
* owner: Constantine
* status: done
* start-date: 2026/07/01
* end-date: 2026/07/07

#### Description
- Migrate the remaining Nimble HTTP download paths to Chronos.
- Remove dependency on `asyncdispatch` / OpenSSL where possible so Nimble can run on Windows without requiring OpenSSL DLLs.

#### Deliverables
- [nim-lang/nimble#1746](https://github.com/nim-lang/nimble/pull/1746) Replace asyncdispatch with Chronos
