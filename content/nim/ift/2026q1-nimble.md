---
title: 2026q1 Nimble
tags:
  - 2026q1
  - nim
  - ift
draft: false
description: Nimble development.
---

`ift-ts:nim:ift:2026q1-nimble`

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

* fully qualified name: `ift-ts:nim:ift:2026q1-nimble:nimble-1.0.0`
* owner: jmgomez
* status: in progress (10%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description

All the relevant information can be found in [this GitHub issue](https://github.com/nim-lang/nimble/issues/1449).

#### Deliverables
- PRs:
  - [nim-lang/nimble#1594](https://github.com/nim-lang/nimble/pull/1594) Update docs
  - [nim-lang/nimble#1593](https://github.com/nim-lang/nimble/pull/1593) Prevent submodule population in pkgcache, fetch only in buildtemp
  - [nim-lang/nimble#1591](https://github.com/nim-lang/nimble/pull/1591) Bumps sat "fix sat issue with mutating state"
  - [nim-lang/nimble#1590](https://github.com/nim-lang/nimble/pull/1590) Move develop pkgsToInstall redirect from runVNext into installPkgs
  - [nim-lang/nimble#1589](https://github.com/nim-lang/nimble/pull/1589) Skip setup after nimble shell
  - [nim-lang/nimble#1588](https://github.com/nim-lang/nimble/pull/1588) Fix develop --withDependencies generating empty nimble.paths in vnext
  - [nim-lang/nimble#1587](https://github.com/nim-lang/nimble/pull/1587) Allow -g flag to install packages globally even from a project directory
  - [nim-lang/nimble#1586](https://github.com/nim-lang/nimble/pull/1586) Fix async download: deduplicate parallel requirement processing
  - [nim-lang/nimble#1585](https://github.com/nim-lang/nimble/pull/1585) Deduplicate packages by checksum and fix assertion without nimble file
  - [nim-lang/nimble#1584](https://github.com/nim-lang/nimble/pull/1584) Show friendly error when running commands without nimble file
  - [nim-lang/nimble#1583](https://github.com/nim-lang/nimble/pull/1583) Fix multiple versions appearing in nimble.paths when using lock file
  - [nim-lang/nimble#1582](https://github.com/nim-lang/nimble/pull/1582) Fix lock file vcsRevision not being used during installation
  - [nim-lang/nimble#1581](https://github.com/nim-lang/nimble/pull/1581) Use vnext path for nimble add command
  - [nim-lang/nimble#1580](https://github.com/nim-lang/nimble/pull/1580) Use version-agnostic cache directories to avoid duplicate downloads
  - [nim-lang/nimble#1579](https://github.com/nim-lang/nimble/pull/1579) Lock preservation
  - [nim-lang/nimble#1578](https://github.com/nim-lang/nimble/pull/1578) Fix regression buildtemp
  - [nim-lang/nimble#1576](https://github.com/nim-lang/nimble/pull/1576) Recover from corrupted pkgcache directories during installation
  - [nim-lang/nimble#1575](https://github.com/nim-lang/nimble/pull/1575) Fixes #1572 Offline switch not honoured past 2.0.0
  - [nim-lang/nimble#1574](https://github.com/nim-lang/nimble/pull/1574) Fix dependency discovery when packages are loaded from cache
  - [nim-lang/nimble#1573](https://github.com/nim-lang/nimble/pull/1573) Isolate VM parser evaluation in temp dir to prevent pkgcache pollution
  - [nim-lang/nimble#1571](https://github.com/nim-lang/nimble/pull/1571) Strips # from directory names
  - [nim-lang/nimble#1570](https://github.com/nim-lang/nimble/pull/1570) Extend buildtemp flow to support before-install hooks for all packages
  - [nim-lang/nimble#1569](https://github.com/nim-lang/nimble/pull/1569) Refactor build pipeline
  - [nim-lang/nimble#1565](https://github.com/nim-lang/nimble/pull/1565) Fix develop packages being added twice in the lock
  - [nim-lang/nimble#1564](https://github.com/nim-lang/nimble/pull/1564) Make global the default (next release only)
  - [nim-lang/nimble#1561](https://github.com/nim-lang/nimble/pull/1561) Install nim from nimbinaries to pkgs2 for package consistency
  - [nim-lang/nimble#1559](https://github.com/nim-lang/nimble/pull/1559) Backwards compatibility with existing nim lock files
  - [nim-lang/nimble#1550](https://github.com/nim-lang/nimble/pull/1550) Fix isRoot flag being loaded from cache causing wrong root package selection
  - [nim-lang/nimble#1548](https://github.com/nim-lang/nimble/pull/1548) Improve local Docker
  - [nim-lang/nimble#1547](https://github.com/nim-lang/nimble/pull/1547) Load package version table from cache on startup
  - [nim-lang/nimble#1546](https://github.com/nim-lang/nimble/pull/1546) Prefer tagged versions over #head and remove maxTaggedVersions
  - [nim-lang/nimble#1552](https://github.com/nim-lang/nimble/pull/1552) Use git show for version enumeration with declarative parser fallback
  - [nim-lang/nimble#1553](https://github.com/nim-lang/nimble/pull/1553) Fix special versions replacing tagged versions in SAT solver
  - [nim-lang/nimble#1554](https://github.com/nim-lang/nimble/pull/1554) Fix nim requirements being filtered during SAT nim selection pass
  - [nim-lang/nimble#1555](https://github.com/nim-lang/nimble/pull/1555) Sets the nim url in the metadata for nim binaries
  - [nim-lang/nimble#1556](https://github.com/nim-lang/nimble/pull/1556) Compute nim checksum from stdlib
- Releases:
  - [nim-lang/nimble v0.22.0](https://github.com/nim-lang/nimble/releases/tag/v0.22.0)
  - Released `setup-nimble-action`
