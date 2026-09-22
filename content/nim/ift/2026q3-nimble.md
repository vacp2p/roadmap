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
* status: in progress (90%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description

All the relevant information can be found in [this GitHub issue](https://github.com/nim-lang/nimble/issues/1449).
This remains the short-term roadmap for replacing pieces of the Nimbus build system bit by bit while improving Nimble overall.

#### Deliverables

- [nimble#1838](https://github.com/nim-lang/nimble/pull/1838) fix #1837: honor locked package URLs during installation
- [nimble#1834](https://github.com/nim-lang/nimble/pull/1834) Bridges PubGrub into nimble for error messages. When SAT fails PubGrub kicks in and explains the error.
- [nimble#1836](https://github.com/nim-lang/nimble/pull/1836) Fix dependency feature lists in declarative parser and SAT resolution (fixes #1832)
- [nim-lang/nimble#1830](https://github.com/nim-lang/nimble/pull/1830) Don't report a SAT search that ran out of budget as unsatisfiable
- [nim-lang/nimble#1828](https://github.com/nim-lang/nimble/pull/1828) Let `nimble list` filter versions by a version range
- [nim-lang/nimble#1826](https://github.com/nim-lang/nimble/pull/1826) Let `nimble list` look up packages by name
- [nim-lang/nimble#1824](https://github.com/nim-lang/nimble/pull/1824) Add standalone PubGrub version solver library.
- [nim-lang/nimble#1823](https://github.com/nim-lang/nimble/pull/1823) Keep lock upgrades consistent with the solution they merge into. Allow
- [nim-lang/nimble#1822](https://github.com/nim-lang/nimble/pull/1822) Fold `nimble upgrade` into `nimble lock --refresh`
- [nim-lang/nimble#1821](https://github.com/nim-lang/nimble/pull/1821) Adds `--refresh` flag
- [nim-lang/nimble#1820](https://github.com/nim-lang/nimble/pull/1820) Implements global refresh
- [nim-lang/nimble#1819](https://github.com/nim-lang/nimble/pull/1819) Refresh every globally known package with `nimble refresh -g`
- [nim-lang/nimble#1817](https://github.com/nim-lang/nimble/pull/1817) Fixes win ci
- [nim-lang/nimble#1813](https://github.com/nim-lang/nimble/pull/1813) Adds capabilities to `nimble refresh`
- [nim-lang/nimble#1811](https://github.com/nim-lang/nimble/pull/1811) Fix/unsatisfiable message crash
- [nim-lang/nimble#1810](https://github.com/nim-lang/nimble/pull/1810) Adds install deps. Fixes #1796
- [nim-lang/nimble#1809](https://github.com/nim-lang/nimble/pull/1809) Lock implies setup. Fixes #179
- [nim-lang/nimble#1798](https://github.com/nim-lang/nimble/pull/1798) Prefer the root's pinned special version when resolving a special-ver…
- [nim-lang/nimble#1788](https://github.com/nim-lang/nimble/pull/1788) Fixes #1738: collects user's info before opening gh session
- [nim-lang/nimble#1792](https://github.com/nim-lang/nimble/pull/1792) Makes it so special versions get a distinct cache key
- [nim-lang/nimble#1787](https://github.com/nim-lang/nimble/pull/1787) Same special version twice should not warn
- [nim-lang/nimble#1784](https://github.com/nim-lang/nimble/pull/1784) Fixes #1779
- [nim-lang/Nim#26011](https://github.com/nim-lang/Nim/pull/26011) Update Nimble Commit to version 0.24.1
- [nim-lang/nimble#1776](https://github.com/nim-lang/nimble/pull/1776) Bump 0.24.1
- [nim-lang/nimble#1774](https://github.com/nim-lang/nimble/pull/1774) Fixes #1768
- [nim-lang/nimble#1773](https://github.com/nim-lang/nimble/pull/1773) fix: SIGSEGV in version discovery under gcc-14 LTO on Nim <= 2.2 (#16…
- [nim-lang/nimble#1772](https://github.com/nim-lang/nimble/pull/1772) Moves sat-retry outside Except blog to avoid crash in old Nim versions
- [nim-lang/nimble#1771](https://github.com/nim-lang/nimble/pull/1771) fix: clear stale solvedPkgs in solveLocalPackages so withNimBinFallba…
- [nim-lang/nimble#1770](https://github.com/nim-lang/nimble/pull/1770) Use BearSSL only, drop OpenSSL dependency from the binary
- [nim-lang/nimble#1769](https://github.com/nim-lang/nimble/pull/1769) Fix #1717
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
- [nimble#1850](https://github.com/nim-lang/nimble/pull/1850) Point the init wizard's package-type link at the Nimble guide (#1835)
- [nimble#1852](https://github.com/nim-lang/nimble/pull/1852) Fix selective lock refresh to preserve compatible pins (fixes #1849)
- [nimble#1848](https://github.com/nim-lang/nimble/pull/1848) Don't abort the package-list refresh on the first unreachable mirror fixes #1845
- [nimble#1847](https://github.com/nim-lang/nimble/pull/1847) Fix lock checksum mismatches: skip Nim's bundled nimble, hash untrack…
- [nimble#1846](https://github.com/nim-lang/nimble/pull/1846) Bump chronos to 536169b4 to fix SIGSEGV on Windows i386 (fixes #1829)
- [nim-lang/nimble#1867](https://github.com/nim-lang/nimble/pull/1867) Bump version 0.26.0
- [nim-lang/nimble#1866](https://github.com/nim-lang/nimble/pull/1866) Stop tracking .claude/ local Claude Code config
- [nim-lang/nimble#1864](https://github.com/nim-lang/nimble/pull/1864) Explain missing packages, drop the duplicate resolution error
- [nim-lang/nimble#1863](https://github.com/nim-lang/nimble/pull/1863) Re-solve when a requirement moves onto a commit pin instead of keeping the old release
- [nim-lang/nimble#1861](https://github.com/nim-lang/nimble/pull/1861) Stop re-prompting to download a Nim that is already in the binaries dir (fixes #1855)
- [nim-lang/nimble#1859](https://github.com/nim-lang/nimble/pull/1859) Make `nimble dump` read-only: never install Nim (fixes #1857)
- [nim-lang/nimble#1858](https://github.com/nim-lang/nimble/pull/1858) Update copyright to new files introduced since the Nim team took over.

### Chronos HTTP downloads

* fully qualified name: `ift-ts:nim:ift:2026q3-nimble:chronos-http-downloads`
* owner: Constantine/Juan
* status: done
* start-date: 2026/07/01
* end-date: 2026/07/07

#### Description
- Migrate the remaining Nimble HTTP download paths to Chronos.
- Remove dependency on `asyncdispatch` / OpenSSL where possible so Nimble can run on Windows without requiring OpenSSL DLLs.

#### Deliverables

- [nim-chronos#728](https://github.com/status-im/nim-chronos/pull/728) Adds Win32 CI with test bug
- [nim-lang/nimble#1746](https://github.com/nim-lang/nimble/pull/1746) Replace asyncdispatch with Chronos
- [status-im/nim-chronos#698](https://github.com/status-im/nim-chronos/pull/698) perf(http): cut per-request allocs (buffer memset, header keys, empty tables
