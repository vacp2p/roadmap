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
  - [nim-lang/nimble#1550](https://github.com/nim-lang/nimble/pull/1550) Fix isRoot flag being loaded from cache causing wrong root package selection
  - [nim-lang/nimble#1548](https://github.com/nim-lang/nimble/pull/1548) Improve local Docker
  - [nim-lang/nimble#1547](https://github.com/nim-lang/nimble/pull/1547) Load package version table from cache on startup
  - [nim-lang/nimble#1546](https://github.com/nim-lang/nimble/pull/1546) Prefer tagged versions over #head and remove maxTaggedVersions
- Releases:
  - Released `setup-nimble-action`
