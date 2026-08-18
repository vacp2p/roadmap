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
* owner: Vlado
* status: done
* start-date: 2026/07/01
* end-date: 2026/08/18

#### Description
Implement the node management UI using the agreed Q3 scope and Logos Core APIs.
The UI should prioritize operational clarity over broad feature coverage.

#### Deliverables
- Node management UI screen in Logos Core
- Display of node identity, addresses, peers, protocols, and discovery state
- Basic controls wired to supported node operations
- Manual validation notes or automated UI coverage if possible
- [logos-co/logos-libp2p-ui#2](https://github.com/logos-co/logos-libp2p-ui/pull/2) feat: initial project code
- [logos-co/logos-libp2p-ui#3](https://github.com/logos-co/logos-libp2p-ui/pull/3) add license
- [logos-co/logos-libp2p-ui#4](https://github.com/logos-co/logos-libp2p-ui/pull/4) feat: gossipsub screen
- [logos-co/logos-libp2p-ui#5](https://github.com/logos-co/logos-libp2p-ui/pull/5) feat: screens with basic functionality
- [logos-co/logos-libp2p-ui#6](https://github.com/logos-co/logos-libp2p-ui/pull/6) feat: settings
- [logos-co/logos-libp2p-ui#12](https://github.com/logos-co/logos-libp2p-ui/pull/12) feat: save settings
- [logos-co/logos-libp2p-ui#11](https://github.com/logos-co/logos-libp2p-ui/pull/11) feat: dht improvments
- [logos-co/logos-libp2p-ui#10](https://github.com/logos-co/logos-libp2p-ui/pull/10) feat: input validation
- [logos-co/logos-libp2p-ui#7](https://github.com/logos-co/logos-libp2p-ui/pull/7) test: add swarm script
- [logos-co/logos-libp2p-ui#9](https://github.com/logos-co/logos-libp2p-ui/pull/9) feat: add TrafficScreen and more metrics
- [logos-co/logos-libp2p-module#102](https://github.com/logos-co/logos-libp2p-module/pull/102) chore: bump nim-libp2p
- [logos-co/logos-libp2p-ui#8](https://github.com/logos-co/logos-libp2p-ui/pull/8) fix: close with eof
- [vacp2p/nim-libp2p#2927](https://github.com/vacp2p/nim-libp2p/pull/2927) chore: adding more metrics
