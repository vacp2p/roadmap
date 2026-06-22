---

title: Anoncomms Unified Networking
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Support Anoncomms unified networking module design and implementation

---

`ift-ts:p2p:ift:2026q3-anoncomms-unified-networking`

Support Anoncomms in designing and implementing a unified networking module that
packages libp2p, mix, and RLN-for-mix into a cohesive downstream component.

## Description

P2P provides consulting, design review, and implementation support for the
Anoncomms unified networking module. The exact scope is still expected to
change, so the first part of the commitment is to define module boundaries,
runtime responsibilities, configuration surfaces, and handoff points between
libp2p, mix, and RLN-for-mix.

This commitment should remain flexible while the Anoncomms team refines its
architecture, but it should still produce concrete module design and integration
artifacts during Q3.

## Task List

### Scope And Architecture

* fully qualified name: `ift-ts:p2p:ift:2026q3-anoncomms-unified-networking:scope-architecture`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/10

#### Description
Work with Anoncomms to define the responsibilities of the unified networking
module, including which functionality belongs in the module itself and which
functionality should remain in nim-libp2p, mix, RLN-for-mix, or downstream
application code.

#### Deliverables
- Initial module responsibility map
- Integration assumptions for libp2p, mix, and RLN-for-mix
- List of open design questions and required decisions

