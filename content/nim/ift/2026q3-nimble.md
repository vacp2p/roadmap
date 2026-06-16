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
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description

All the relevant information can be found in [this GitHub issue](https://github.com/nim-lang/nimble/issues/1449).
This remains the short-term roadmap for replacing pieces of the Nimbus build system bit by bit while improving Nimble overall.

#### Deliverables
- PRs/Issues/Docs/Reports

### Chronos HTTP downloads

* fully qualified name: `ift-ts:nim:ift:2026q3-nimble:chronos-http-downloads`
* owner: moigagoo
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Migrate the remaining Nimble HTTP download paths to Chronos.
- Remove dependency on `asyncdispatch` / OpenSSL where possible so Nimble can run on Windows without requiring OpenSSL DLLs.

#### Deliverables
- PRs/Issues/Docs/Reports
