---

title: nim-libp2p Wrapping ngtcp2
tags:
  - "2025q1"
  - "p2p"
  - "ift"
draft: false
description: Wrap ngtcp2 in nim and integrate it as quic transport in nim-libp2p.

---

`vac:p2p:ift:2025q1-nimlibp2p-wrapping-ngtcp2`

Wrap ngtcp2 in nim and integrate it as quic transport in nim-libp2p.

## Description

This commitment involves two main objectives:

*  Completing a deployable version of nim-quic by wrapping ngtcp2
*  Integrating this nim-quic implementation as a QUIC transport in nim-libp2p

We are dedicated to developing this wrapped version of the QUIC transport to a production-ready state,
ensuring it can be seamlessly integrated into various projects.
The development of a native Nim implementation of QUIC will be addressed in a future commitment.

## Task List

### Implement the full TLS handshake using picotls

* fully qualified name: `vac:p2p:ift:2025q1-nimlibp2p-wrapping-ngtcp2:tls_handshake`
* owner: rramos
* status: done
* start-date: 2025/01/26
* end-date: 2025/03/31

#### Description
Implement the full TLS handshake using nim-mbedtls as explained in https://docs.libp2p.io/concepts/transports/quic/ and https://github.com/libp2p/specs/blob/master/tls/tls.md.
The ngtcp2 library has crypto helper libraries that make this integration easier, but unfortunately, it doesn't support mbedtls. PicoTLS will be used as a TLS backend for
ngtcp2

#### Deliverables
- [ ] PRs:
  - nim-ngtcp2 - wrap picotls: [PR](https://github.com/vacp2p/nim-ngtcp2/pull/10)
  - nim-quic
    - picotls integration [PR](https://github.com/vacp2p/nim-quic/pull/55)
    - feat: ALPN [PR](https://github.com/vacp2p/nim-quic/pull/59)  
    - fix: connection timeouts [PR](https://github.com/vacp2p/nim-quic/pull/62)
    - fix: handshake failures on client side [PR](https://github.com/vacp2p/nim-quic/pull/64)
    - fix: remove `noSideEffect` pragma [PR](https://github.com/vacp2p/nim-quic/pull/63)
    - feat: wait for handshake on incoming connection and get access to certificate chain [PR](https://github.com/vacp2p/nim-quic/pull/65)
  - nim-libp2p
    - quic (WIP) [PR](https://github.com/vacp2p/nim-libp2p/pull/1265)
    - use libp2p alpn, remove hardcoded port number and fix certificate generation [PR](https://github.com/vacp2p/nim-libp2p/pull/1283)
    - refactor: use openssl instead of mbedtls [PR](https://github.com/vacp2p/nim-libp2p/pull/1298)
    - feat: `withQuicTransport` [PR](https://github.com/vacp2p/nim-libp2p/pull/1301)
    -  fix: set peerId on incoming Quic connection [PR](https://github.com/vacp2p/nim-libp2p/pull/1302)

### Implement certificate validation

* fully qualified name: `vac:p2p:ift:2025q1-nimlibp2p-wrapping-ngtcp2:certificate_validation`
* owner: vlado
* status: done
* start-date: 2025/02/05
* end-date: 2025 /03/25

#### Description
Validates certificates according to libp2p [TLS 1.3 specs](https://github.com/libp2p/specs/blob/master/tls/tls.md). 
This work should be built based on [nim-libp2p#1209](https://github.com/vacp2p/nim-libp2p/pull/1209)

#### Deliverables
- [ ] PRs:
  - Generate and parse TLS 1.3 Certificate: [PR](https://github.com/vacp2p/nim-libp2p/pull/1209)
  - Implement custom certificate validators: [PR](https://github.com/vacp2p/nim-quic/pull#56)
  - X.509 certificate validation[PR](https://github.com/vacp2p/nim-libp2p/pull/1292)
  - Certificate cosmetics - [PR](https://github.com/vacp2p/nim-libp2p/pull/1293)
  - Add tests with invalid certs - [PR](https://github.com/vacp2p/nim-libp2p/pull/1297)
  - Set distinguishable issuer name with peer id - [PR](https://github.com/vacp2p/nim-libp2p/pull/1296) 
  - TLS Certificate Verify - [PR](https://github.com/vacp2p/nim-libp2p/pull/1295)
  - Add Date verification - [PR](https://github.com/vacp2p/nim-libp2p/pull/1299)
  - Update libp2p specs:
    - update specs test vectors [PR](https://github.com/libp2p/go-libp2p/pull/3242)
    - update nim-libp2p certificate test vectors [PR](https://github.com/vacp2p/nim-libp2p/pull/1294)
    - update go-libp2p certificate test vectors [PR](https://github.com/libp2p/specs/pull/665)

### Improve QUIC transport code

* fully qualified name: `vac:p2p:ift:2025q1-nimlibp2p-wrapping-ngtcp2:improve_quic`
* owner: rramos
* status: 30%
* start-date:  2025/03/17
* end-date: 2025/03/31

#### Description
Prepare the transport code for production by performing the necessary refactors, implementing logging, and adding unit tests. This may also involve determining whether QUIC support for hole punching needs to be implemented. For the first part, follow recomendations from [Status nim style guidelines](https://status-im.github.io/nim-style-guide/)

**Note**: this task does not stop the main commitment to be closed. Further improvements over the code will be handled as part of maintenance tasks for Q2

#### Deliverables
- [ ] PRs:
  - [nim-quic#60](https://github.com/vacp2p/nim-quic/pull/60) -  chore: use bearssl rng
  - [nim-quic#57](https://github.com/vacp2p/nim-quic/pull/57) - chore: `async: raises`

