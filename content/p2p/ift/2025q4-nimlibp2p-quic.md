---

title: Quic Stabilization and removal of runtime dependencies
tags:
  - "2025q4"
  - "p2p"
  - "ift"
draft: false
description: Stabilize Quic so it can be used effectively by Nimbus and Waku and remove OpenSSL Support

---

`vac:p2p:ift:2025q4-nimlibp2p-quic`

Maintain nim-libp2p through improvements, bug fixes, and user support

## Description

In Q3 we discovered critical deficiencies in nim-quic, including runtime instability and excessive memory use during testing. As a result, we cannot safely deploy quic in production. in parallel, we identified OpenSSL as a long-term liability and will migrate to AWS-LC or Boringssl to reduce dependencies and improve maintainability.

## Task List

### Quic Stabilization

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-quic:stabilization`
* owner: vlado/rramos
* status: in progress (60%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Resolve runtime crashes, race conditions and excessive memory use in nim-quic. Target outcome is that quic can be enabled and run stably in both nimbus and waku test environments.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- [feat: optimize send loop for release mode](https://github.com/vacp2p/nim-lsquic/pull/19)
- [chore(many_queue): get() raises CancelledError](https://github.com/vacp2p/nim-lsquic/pull/17)
- [fix(quic): muxer handling](https://github.com/vacp2p/nim-libp2p/pull/1885)
- [chore(config.nims): add errors](https://github.com/vacp2p/nim-lsquic/pull/16)
- [chore(many_queue): add test and new()](https://github.com/vacp2p/nim-lsquic/pull/15)
- [test(transports): fix muxer handling](https://github.com/vacp2p/nim-libp2p/pull/1884)
- [test: split tests](https://github.com/vacp2p/nim-lsquic/pull/13)
- [feat: add ManyQueue](https://github.com/vacp2p/nim-lsquic/pull/12)
- [vacp2p/nim-libp2p#1877: QuicMuxer is created without upgrader](https://github.com/vacp2p/nim-libp2p/pull/1877)
- [vacp2p/nim-lsquic#8: perf tests and fix: pin connections and streams](https://github.com/vacp2p/nim-lsquic/pull/8)
- [vacp2p/nim-lsquic#7: fix TODOs](https://github.com/vacp2p/nim-lsquic/pull/7)
- [vacp2p/nim-lsquic#6: feat stream write](https://github.com/vacp2p/nim-lsquic/pull/6)
- [vacp2p/nim-lsquic#5: feat stream read](https://github.com/vacp2p/nim-lsquic/pull/5)
- [vacp2p/nim-lsquic#4: feat close / abort stream](https://github.com/vacp2p/nim-lsquic/pull/4)
- [vacp2p/nim-lsquic#3: feat stream lifecycle - creation](https://github.com/vacp2p/nim-lsquic/pull/3)
- [vacp2p/nim-lsquic#2: feat connections](https://github.com/vacp2p/nim-lsquic/pull/2)
- [vacp2p/nim-lsquic#1: chore test github actions](https://github.com/vacp2p/nim-lsquic/pull/1)
- [vacp2p/nim-libp2p#1846: use negotiated protocol in pubsub connection lookups](https://github.com/vacp2p/nim-libp2p/pull/1846)
- [vacp2p/nim-libp2p#1844: quic wildcard resolver fixes](https://github.com/vacp2p/nim-libp2p/pull/1844)
- [vacp2p/nim-libp2p#1839: quic EOF handling fixes](https://github.com/vacp2p/nim-libp2p/pull/1839)
- [PR 175: fix timeout handling](https://github.com/vacp2p/nim-quic/pull/175)
- [PR 174: refactor send pipeline](https://github.com/vacp2p/nim-quic/pull/174)
- [PR 167: fix blocked streams](https://github.com/vacp2p/nim-quic/pull/167)
- [PR 162: acknowledge packets faster](https://github.com/vacp2p/nim-quic/pull/162)
- [PR 163: fix no-defects handling](https://github.com/vacp2p/nim-quic/pull/163)


### Replace OpenSSL by AWS-LC / BoringSSL

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-quic:openssl-replacement`
* owner: rramos
* status: done
* start-date: 2025/10/01
* end-date: 2025/10/15

#### Description
Replace the openssl dependency in nim-quic and related libraries with BoringSSL or AWS-LC. The goal is to reduce the need of runtime dependencies by statically linking any of these libraries

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- [vacp2p/nim-ngtcp2#22](https://github.com/vacp2p/nim-ngtcp2/pull/22) feat: compile boringssl using assembly files (except windows)
- [vacp2p/nim-ngtcp2#21](https://github.com/vacp2p/nim-ngtcp2/pull/21) feat: replace picotls by BoringSSL
- [vacp2p/nim-quic#140](https://github.com/vacp2p/nim-quic/pull/140) feat: use BoringSSL
- [vacp2p/nim-libp2p#1782](https://github.com/vacp2p/nim-libp2p/pull/1782) chore: remove libp2p_quic_support compile flag, and openssl dependency
- [vacp2p/nim-libp2p#1761](https://github.com/vacp2p/nim-libp2p/pull/1761) feat: use BoringSSL for certificate ops
