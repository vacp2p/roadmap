---

title: nim-lsquic Per-Connection Certificate Validators
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Add per-connection certificate validator configuration to nim-lsquic

---

`ift-ts:p2p:ift:2026q3-nim-lsquic-per-connection-cert-validators`

Add support for configuring certificate validators on a per-connection basis in
`nim-lsquic`.

## Description

`nim-lsquic` should expose a safe API for setting certificate validators per 
connection, while preserving the default validator behavior for users that 
do not opt in. This is particularly useful for nim-libp2p as it would need
to validate that the peerId in the certificate is valid before connecting to
a peer, while right now, it connects to a peer first, but checks the certificate
peerId later.

## Task List


### Validator Implementation

* fully qualified name: `ift-ts:p2p:ift:2026q3-nim-lsquic-per-connection-cert-validators:validator`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/15
* end-date: 2026/09/30

#### Description
Design the per-connection validator API for `nim-lsquic`, including lifetime,
ownership, callback behavior, defaults, and interaction with existing TLS setup.
Implement the per-connection validator configuration and wire it into the
`nim-lsquic` connection setup path.

#### Deliverables
- Per-connection validator support implemented in `nim-lsquic`
- Existing default validation behavior preserved
- Tests for default, custom, accepted, and rejected certificate cases


### nim-libp2p Integration

* fully qualified name: `ift-ts:p2p:ift:2026q3-nim-lsquic-per-connection-cert-validators:nimlibp2p-integration`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/15
* end-date: 2026/09/30

#### Description
Use the new validator support from nim-libp2p where needed by QUIC
transport configuration.

#### Deliverables
- nim-libp2p QUIC transport can pass per-connection validators where required

