---

title: nim-libp2p WASM Targets
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Add WebAssembly build support and an example app for nim-libp2p

---

`ift-ts:p2p:ift:2026q3-nimlibp2p-wasm-targets`

Add WebAssembly build support for nim-libp2p, including CI coverage and an
example app demonstrating basic usage.

## Description

WASM support would allow nim-libp2p functionality to be explored in browser or
WASM-hosted environments. The Q3 scope should start with feasibility and build
support, then provide a minimal example app that demonstrates the subset of
nim-libp2p functionality available under WASM constraints.

## Task List

### WASM Feasibility

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-wasm-targets:feasibility`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/15

#### Description
Assess which nim-libp2p functionality can reasonably build and run under WASM,
including transport limitations, async runtime constraints, crypto
dependencies, DNS behavior, and browser versus non-browser environments.

#### Deliverables
- WASM feasibility report
- Supported and unsupported feature list
- Build and dependency blockers identified


### WASM Build Support

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-wasm-targets:build-support`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/15
* end-date: 2026/09/30

#### Description
To be determined based on prev task

#### Deliverables
To be determined based on prev task


### Example App

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-wasm-targets:example-app`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/15
* end-date: 2026/09/30

#### Description
Create a small WASM example app demonstrating basic supported nim-libp2p usage.

#### Deliverables
- Minimal WASM example app
- Instructions for building and running the example
- Notes on feature limitations and follow-up work
`