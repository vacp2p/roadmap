---

title: Nim-libp2p maintenance
tags:
  - "2025q4"
  - "p2p"
  - "ift"
draft: false
description: Maintain nim-libp2p through improvements, bug fixes, and user support

---

`vac:p2p:ift:2025q4-nimlibp2p-maintenance`

Maintain nim-libp2p through improvements, bug fixes, and user support

## Description

Continue supporting and maintaining the nim-libp2p repository through ongoing improvements, refactoring, and bug fixes.
This includes a range of ad-hoc tasks critical to sustaining code quality, overall stability, correct functionality,
and performance of the project.
Additionally, it provides a platform for addressing small developer requests,
ensuring that nim-libp2p remains functional and usable for its primary users — Nimbus and Waku — helping to meet their evolving needs."

## Task List

### Maintenance

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-maintenance:maintenance`
* owner: rramos
* status: in progress (28%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Maintain [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors and bug fixes.

#### Deliverables
- [[Deliverable] Maintenance 2025Q4]
- [PR 1785: fix echo rendezvous regression](https://github.com/vacp2p/nim-libp2p/pull/1785)
- [PR 1781: release nim-libp2p 1.14.2](https://github.com/vacp2p/nim-libp2p/pull/1781)
- [PR 1790: add verbose output for test binaries](https://github.com/vacp2p/nim-libp2p/pull/1790)
- [PR 1791: increase message size for performance](https://github.com/vacp2p/nim-libp2p/pull/1791)
- [PR 1792: bump quic dependency to v0.5.0](https://github.com/vacp2p/nim-libp2p/pull/1792)
- [PR 168: bump nim-quic to v0.5.0](https://github.com/vacp2p/nim-quic/pull/168)
- [PR 154: increase connectionsCount with note](https://github.com/vacp2p/nim-quic/pull/154)


### Gossipsub Interop tests

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-maintenance:gossipsub-interop-tests`
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Integrate libp2p test plans' [GossipSub interop tests](https://github.com/libp2p/test-plans/tree/master/gossipsub-interop) as part of the CI tests executed on each PR 

#### Deliverables
- New github workflow: `Interoperability Tests / Run GossipSub interoperability tests`


### Fix flaky tests

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-maintenance:flaky-tests`
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Continue to systematically track flaky tests using CI logs and failure reports, 
and fix root causes where reproducible (e.g. race conditions, timeouts, dependency order)

#### Deliverables
- PRs/Issues/Docs/Reports
