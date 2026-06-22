---

title: nim-libp2p TLS SNI Multiaddress Support
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Add TLS and SNI information support for multiaddresses

---

`ift-ts:p2p:ift:2026q3-nimlibp2p-tls-sni-multiaddr`

Add support for representing and handling TLS/SNI information in
multiaddresses.

## Description

Some peers need to connect through TLS endpoints where SNI controls certificate
selection or routing. nim-libp2p should be able to represent TLS/SNI
requirements in multiaddresses and pass that information to the appropriate
dialing and listening paths.

## Task List

### Multiaddress Representation

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-tls-sni-multiaddr:representation`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/31

#### Description
Define and implement the multiaddress representation for TLS and SNI
information, following upstream multiaddr conventions where they exist.

#### Deliverables
- TLS/SNI multiaddress parsing support
- TLS/SNI multiaddress construction support
- Validation for malformed or unsupported address combinations
- Compatibility notes against upstream multiaddr behavior


### Transport Wiring

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-tls-sni-multiaddr:transport-wiring`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/31

#### Description
Pass TLS/SNI information from multiaddresses into dialing and listening
transports that need it.

#### Deliverables
- Dial path uses SNI information when present
- Listener or advertised address handling preserves relevant TLS/SNI information
- Tests covering TLS/SNI address parsing and transport configuration
