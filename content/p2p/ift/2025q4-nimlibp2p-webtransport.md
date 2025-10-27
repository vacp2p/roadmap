---

title: nim-libp2p Webtransport
tags:
  - "2025q4"
  - "ift"
draft: false
description: Add webtransport support to nim-libp2p

---

`vac:p2p:ift:2025q4-nimlibp2p-webtransport`

Add webtransport support to nim-libp2p

## Description

Extend the number of transports supported by nim-libp2p via the developent of Webtransport,
which would allow browsers to establish bidirectional stream connections to nim-libp2p servers
This deliverable continues the work started in 2025q2

## Task List

### Wrapping nghttp3

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-webtransport:nghttp3-wrapping`
* owner: vlado
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Create wrapper around the [nghttp3](https://github.com/ngtcp2/nghttp3) C library for Nim.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- add nghttp3 wrapping with futhark [nim-nghttp3 #1](https://github.com/vacp2p/nim-nghttp3/pull/1)
- ci: add ci for linux and mac [nim-nghttp3 #2](https://github.com/vacp2p/nim-nghttp3/pull/2)

### HTTP/3 Client

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-webtransport:http3-client`
* owner: vlado
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Implement HTTP/3 Client following [draft-ietf-webtrans-http3-02](https://www.ietf.org/archive/id/draft-ietf-webtrans-http3-02.html) specification.
This should be done as part of the [nim-quic](https://github.com/vacp2p/nim-quic) module.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs/Issues/Docs/Reports


### HTTP/3 Server

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-webtransport:http3-server`
* owner: vlado
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Implement HTTP/3 Server following [draft-ietf-webtrans-http3-02](https://www.ietf.org/archive/id/draft-ietf-webtrans-http3-02.html) specification.
This should be done as part of the [nim-quic](https://github.com/vacp2p/nim-quic) module.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs/Issues/Docs/Reports


### HTTP/3 Maintenance

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-webtransport:http3-maintenance`
* owner: vlado
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Final improvements, code polishing and interoperability testing after Client and Server are merged.


Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs/Issues/Docs/Reports


### Certificate generation

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-webtransport:certificate`
* owner: vlado
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Certificate generation according to libp2p webtransport [specification](https://github.com/libp2p/specs/tree/master/webtransport)

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs/Issues/Docs/Reports


### Key components implementation

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-webtransport:key-components`
* owner: vlado
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Implement webtransport key components: Client, Server, Session

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs/Issues/Docs/Reports


### Noise handshake and certificate validation

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-webtransport:handshake-and-cert-validation`
* owner: vlado
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
 1.3. Noise handshake and certificate validtion according to libp2p webtransport [specification](https://github.com/libp2p/specs/tree/master/webtransport)

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs/Issues/Docs/Reports

