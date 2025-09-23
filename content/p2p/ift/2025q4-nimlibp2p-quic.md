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
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date:

#### Description
Resolve runtime crashes, race conditions and excessive memory use in nim-quic. Target outcome is that quic can be enabled and run stably in both nimbus and waku test environments.

#### Deliverables



### Replace OpenSSL by AWS-LC / BoringSSL

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-quic:openssl-replacement`
* owner: 
* status: not started
* start-date: 2025/10/01
* end-date:

#### Description
Replace the openssl dependency in nim-quic and related libraries with BoringSSL or AWS-LC. The goal is to reduce the need of runtime dependencies by statically linking any of these libraries

#### Deliverables
