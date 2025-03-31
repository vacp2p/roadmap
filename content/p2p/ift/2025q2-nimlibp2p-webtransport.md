---

title: nim-libp2p Webtransport
tags:
  - "2025q2"
  - "p2p"
  - "ift"
draft: false
description: Add webtransport support to nim-libp2p

---

`vac:p2p:ift:2025q2-nimlibp2p-webtransport`

Add webtransport support to nim-libp2p

## Description

Extend the number of transports supported by nim-libp2p via the developent of Webtransport,
which would allow browsers to establish bidirectional stream connections to nim-libp2p servers.
This commitment will initiate in Q2, extending through Q3, this timeline reflects the 
substantial scope of work, which cannot be realistically completed within a single quarter.

## Task List

### HTTP/3 over Quic

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-webtransport:http3`
* owner: vlado
* status: not started
* start-date:
* end-date:

#### Description
Implement HTTP/3 over Quic following [draft-ietf-webtrans-http3-02](https://www.ietf.org/archive/id/draft-ietf-webtrans-http3-02.html) specification.
This should be done as part of the [nim-quic](https://github.com/vacp2p/nim-quic) module

#### Deliverables



### Certificate generation

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-webtransport:certificate`
* owner: vlado
* status: not started
* start-date:
* end-date:

#### Description
Certificate generation according to libp2p webtransport [specification](https://github.com/libp2p/specs/tree/master/webtransport)

#### Deliverables



### Key components implementation

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-webtransport:key-components`
* owner: vlado
* status: not started
* start-date:
* end-date:

#### Description
Implement webtransport key components: Client, Server, Session

#### Deliverables



### Noise handshake and certificate validation

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-webtransport:handshake-and-cert-validation`
* owner: vlado
* status: not started
* start-date:
* end-date:

#### Description
 1.3. Noise handshake and certificate validtion according to libp2p webtransport [specification](https://github.com/libp2p/specs/tree/master/webtransport)

#### Deliverables

