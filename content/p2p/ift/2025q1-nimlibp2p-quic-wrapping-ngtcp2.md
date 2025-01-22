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

### Implement the full TLS handshake using nim-mbedtls

* fully qualified name: `vac:p2p:ift:2025q1-nimlibp2p-wrapping-ngtcp2:tls_handshake`
* owner: rramos
* status: 
* start-date: 
* end-date:

#### Description
Implement the full TLS handshake using nim-mbedtls as explained in https://docs.libp2p.io/concepts/transports/quic/ and https://github.com/libp2p/specs/blob/master/tls/tls.md.
The ngtcp2 library has crypto helper libraries that make this integration easier, but unfortunately, it doesn't support mbedtls.
It is necessary to find a way to make this integration using mbedtls.

#### Deliverables


### Implement certificate validation

* fully qualified name: `vac:p2p:ift:2025q1-nimlibp2p-wrapping-ngtcp2:certificate_validation`
* owner: rramos
* status: 
* start-date: 
* end-date:

#### Description
Validates certificates according to libp2p TLS 1.3 specs.

#### Deliverables


### Improve QUIC transport code

* fully qualified name: `vac:p2p:ift:2025q1-nimlibp2p-wrapping-ngtcp2:improve_quic`
* owner: rramos
* status: 
* start-date: 
* end-date:

#### Description
Prepare the transport code for production by performing the necessary refactors, implementing logging, and adding unit tests. This may also involve determining whether QUIC support for hole punching needs to be implemented.

#### Deliverables
