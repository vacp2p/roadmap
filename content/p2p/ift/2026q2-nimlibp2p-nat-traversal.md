---

title: nim-libp2p NAT Traversal
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: Add reusable NAT traversal address setup to nim-libp2p

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-nat-traversal`

Add reusable NAT traversal and public address setup support to nim-libp2p.

## Description

nim-libp2p has long tracked NAT traversal support in
[vacp2p/nim-libp2p#51](https://github.com/vacp2p/nim-libp2p/issues/51).
Downstream users already carry NAT address setup logic, including a configuration
option with `any`, `none`, `upnp`, `pmp`, and `extip:<IP>` modes,
and Nimbus code that calls `setupAddress(config.nat, ...)` for TCP and UDP
ports. This commitment extracts the reusable behavior into nim-libp2p so
applications can configure public address discovery and port mapping through
the library instead of duplicating efforts downstream.

## Task List

### NAT Address Setup API

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-nat-traversal:address-setup-api`
* owner: not assigned yet
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/30

#### Description
Provide a reusable nim-libp2p API and builder/config integration for NAT public
address setup. The API should support the downstream modes already used by
Logos and Nimbus: automatic discovery, disabled NAT setup, UPnP, NAT-PMP, and
explicit external IP configuration.

#### Deliverables
- Builder/config option for NAT address setup
- Support for `any`, `none`, `upnp`, `pmp`, and `extip:<IP>` modes or equivalent typed configuration
- Public address and mapped port results exposed to transport/listen address handling
- Tests for mode parsing, explicit external IP handling, and disabled NAT setup


### UPnP and NAT-PMP Integration

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-nat-traversal:upnp-pmp`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Integrate UPnP and NAT-PMP address mapping through existing Nim NAT traversal
libraries where possible, reusing the behavior already proven by downstream
projects. The implementation should work for nim-libp2p TCP usage and be
structured so UDP-capable transports can use the same setup path.

#### Deliverables
- UPnP and NAT-PMP mapping support available from nim-libp2p
- Address propagation into identify/listen address reporting where applicable
- Downstream migration guidance for Logos and Nimbus NAT configuration
- Tests or examples covering mapped TCP address advertisement
