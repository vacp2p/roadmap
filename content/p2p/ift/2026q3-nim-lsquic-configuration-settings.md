---

title: nim-lsquic Configuration Settings
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Expose and improve nim-lsquic configuration options

---

`ift-ts:p2p:ift:2026q3-nim-lsquic-configuration-settings`

Expose or improve configuration options for `nim-lsquic` so QUIC transport
behavior is easier to tune and align with nim-libp2p runtime needs.

## Description

nim-libp2p depends on `nim-lsquic` for QUIC behavior, but not all useful LSQUIC
settings are exposed clearly through the Nim wrapper or through nim-libp2p
transport configuration. This commitment identifies and exposes the settings
that matter for transport behavior, operational tuning, interop, and testing.

## Task List

### nim-lsquic Configuration API

* fully qualified name: `ift-ts:p2p:ift:2026q3-nim-lsquic-configuration-settings:nim-lsquic-api`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Expose selected settings through `nim-lsquic` with typed configuration and
safe defaults.

#### Deliverables
- Inventory of relevant LSQUIC settings and current wrapper support
- Typed `nim-lsquic` configuration API for selected settings
- Validation for invalid or unsupported setting values
- Tests covering defaults and custom setting application


### nim-libp2p QUIC Transport Wiring

* fully qualified name: `ift-ts:p2p:ift:2026q3-nim-lsquic-configuration-settings:nimlibp2p-wiring`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Expose the selected `nim-lsquic` settings through nim-libp2p QUIC transport
configuration where they are useful to applications.

#### Deliverables
- nim-libp2p QUIC transport accepts selected `nim-lsquic` settings
- Integration tests or examples for changed settings
