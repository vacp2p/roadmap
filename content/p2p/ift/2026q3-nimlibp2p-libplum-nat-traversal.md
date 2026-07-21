---

title: nim-libp2p libplum NAT Traversal
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Replace nim-nat-traversal usage with nim-libplum when available

---

`ift-ts:p2p:ift:2026q3-nimlibp2p-libplum-nat-traversal`

Migrate NAT traversal functionality from `nim-nat-traversal` to `nim-libplum`
once `nim-libplum` becomes available.

## Description

nim-libp2p gained a NATService in Q2 that integrates reusable address setup and
port mapping behavior. Q3 should prepare and execute the migration from
`nim-nat-traversal` to `nim-libplum` if the new library is available and ready
for nim-libp2p usage.

The migration should simplify the NAT traversal stack without regressing
existing UPnP, NAT-PMP, explicit external IP, AutoNAT, or address announcement
behavior.

## Task List

### NATService Migration

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-libplum-nat-traversal:natservice-migration`
* owner: Gabe
* status: done
* start-date: 2026/07/01
* end-date: 2026/07/21

#### Description
Replace `nim-nat-traversal` usage in nim-libp2p NATService with
`nim-libplum`, preserving the public configuration and runtime behavior where
possible.

#### Deliverables
- [vacp2p/nim-libp2p#2821](https://github.com/vacp2p/nim-libp2p/pull/2821) chore(nat): replace nim-nat-traversal with nim-libplum
- NATService uses `nim-libplum` for supported port mapping behavior
- Existing NATService configuration remains source-compatible or has documented migration steps
- Tests updated for UPnP, NAT-PMP, explicit external IP, and disabled NAT setup
- Migration notes for downstream users if needed
