---

title: Nim-libp2p maintenance
tags:
  - "2025q3"
  - "p2p"
  - "ift"
draft: false
description: Maintain nim-libp2p through improvements, bug fixes, and user support

---

`vac:p2p:ift:2025q3-nimlibp2p-maintenance`

Maintain nim-libp2p through improvements, bug fixes, and user support

## Description

Continue supporting and maintaining the nim-libp2p repository through ongoing improvements, refactoring, and bug fixes.
This includes a range of ad-hoc tasks critical to sustaining code quality, overall stability, correct functionality,
and performance of the project.
Additionally, it provides a platform for addressing small developer requests,
ensuring that nim-libp2p remains functional and usable for its primary users — Nimbus and Waku — helping to meet their evolving needs."

## Task List

### Maintenance

* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-maintenance:maintenance`
* owner: rramos
* status: not started
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description
Maintain [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors and bug fixes.

#### Deliverables
- [[Deliverable] Maintenance 2025Q3](TODO)



### Remove go-libp2p daemon

* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-maintenance:go-libp2p-daemon`
* owner: 
* status: not started
* start-date:
* end-date:

#### Description
The overall goal is simplify the developer experience and reinforce the 
self-sufficiency of the nim-libp2p codebase. For this the following tasks must be implemented:
- Audit and remove the dependency on go-libp2p-daemon in examples and unit tests, 
  replacing it with native nim-libp2p components wherever feasible.
- Ensure all example code is runnable with a Nim-only toolchain.
- Update CI workflows to eliminate installation of go-libp2p-daemon;
  if removal is impractical, implement caching to reduce execution time


#### Deliverables



### Fix flaky tests

* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-maintenance:flaky-tests`
* owner: 
* status: not started
* start-date:
* end-date:

#### Description
Systematically track flaky tests using CI logs and failure reports, 
and fix root causes where reproducible (e.g. race conditions, timeouts, dependency order)

#### Deliverables
