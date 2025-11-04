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
* status: in progress (37%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Maintain [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors and bug fixes.

#### Deliverables
- [PR 1831: move unittest tests into tools suite](https://github.com/vacp2p/nim-libp2p/pull/1831)
- [PR 1828: imports cleanup across test modules](https://github.com/vacp2p/nim-libp2p/pull/1828)
- [PR 1825: include dangling `testipaddr` file](https://github.com/vacp2p/nim-libp2p/pull/1825)
- [PR 1824: add trackers to test tools](https://github.com/vacp2p/nim-libp2p/pull/1824)
- [PR 1823: remove workaround in `runTest`](https://github.com/vacp2p/nim-libp2p/pull/1823)
- [PR 1819: add tools package to tests](https://github.com/vacp2p/nim-libp2p/pull/1819)
- [PR 1817: improve test logic](https://github.com/vacp2p/nim-libp2p/pull/1817)
- [PR 1812: bump chronos dependency](https://github.com/vacp2p/nim-libp2p/pull/1812)
- [PR 1810: fix CI Nim version matrix](https://github.com/vacp2p/nim-libp2p/pull/1810)
- [PR 1809: remove QUIC test variant](https://github.com/vacp2p/nim-libp2p/pull/1809)
- [PR 1808: temporarily split test-all task](https://github.com/vacp2p/nim-libp2p/pull/1808)
- [PR 1807: reduce global RNG usage](https://github.com/vacp2p/nim-libp2p/pull/1807)
- [PR 173: bump nim-quic to v0.5.1](https://github.com/vacp2p/nim-quic/pull/173)
- [PR 1685: enable QUIC transport in pubsub tests](https://github.com/vacp2p/nim-libp2p/pull/1685)
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
