---

title: Logos Core Node Management UI
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Build a Logos Core UI for managing a nim-libp2p node

---

`ift-ts:p2p:ift:2026q3-logos-core-node-management-ui`

Build a UI for managing a nim-libp2p node from Logos Core, exposing useful
controls, status information, and diagnostics for local node operation.

## Description

The Logos Core libp2p module should provide a usable node management interface
The UI should help operators and developers inspect node identity, listen addresses, 
connected peers, protocols, discovery state, and selected runtime controls without 
requiring direct access to nim-libp2p internals.

## Task List

### UI Requirements And Mock Review

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-core-node-management-ui:requirements`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/03

#### Description
Turn the existing UI mocks into an implementable UI specification with screen inventory, 
required fields, node actions, API dependencies, and explicitly deferred diagnostics or 
operator tooling.

#### Deliverables
- Reviewed mock set and selected UI direction
- Node management screen scope
- Required data and control APIs identified


### Node Status And Control APIs

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-core-node-management-ui:status-control-apis`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Expose the node status and control information needed by the UI through Logos
Core. Initial scope should include node identity, peer id, listen addresses,
advertised addresses, connected peers, mounted protocols, discovery status,
transport state, and start/stop controls where supported.

#### Deliverables
- Logos Core APIs for node status and basic node controls


### Management UI Implementation

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-core-node-management-ui:ui-implementation`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Implement the node management UI using the agreed Q3 scope and Logos Core APIs.
The UI should prioritize operational clarity over broad feature coverage.

#### Deliverables
- Node management UI screen in Logos Core
- Display of node identity, addresses, peers, protocols, and discovery state
- Basic controls wired to supported node operations
- Manual validation notes or automated UI coverage if possible
