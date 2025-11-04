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
* status: in progress (37%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Resolve runtime crashes, race conditions and excessive memory use in nim-quic. Target outcome is that quic can be enabled and run stably in both nimbus and waku test environments.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
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
