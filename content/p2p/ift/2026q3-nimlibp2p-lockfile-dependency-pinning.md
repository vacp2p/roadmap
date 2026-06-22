---

title: nim-libp2p Lockfile Dependency Pinning
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Replace .pinned dependency handling with nimble lock file based pinning

---

`ift-ts:p2p:ift:2026q3-nimlibp2p-lockfile-dependency-pinning`

Replace the current `.pinned` file mechanism used by CI and interop with
dependency pinning based on Nimble lock files.

## Description

nim-libp2p uses `.pinned` files in some CI and interop flows to keep dependency
versions stable. This commitment migrates those flows to Nimble lock file based
pinning so dependency state is managed through the standard package workflow and
is easier for contributors and downstream projects to reproduce.

## Task List

### Lock File Migration

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-lockfile-dependency-pinning:lockfile-migration`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Determine the  `.pinned` usage in nim-libp2p, CI, docker, interop tests and scripts.
Replace `.pinned` driven dependency setup with Nimble lock file based installation
in the relevant workflows.

#### Deliverables
- Nimble lock file created or updated for nim-libp2p dependency pinning
- CI and interop scripts use lock file based dependency installation
- `.pinned` usage removed from active workflows
- Tests or CI runs proving dependency setup remains reproducible
