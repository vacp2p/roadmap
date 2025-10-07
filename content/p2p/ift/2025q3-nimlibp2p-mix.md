---

title: Nim-libp2p Mix
tags:
  - "2025q3"
  - "p2p"
  - "ift"
draft: false
description: stabilize and upstream mix in nim-libp2p

---

`vac:p2p:ift:2025q3-nimlibp2p-mix`

Stabilize mix in nim-libp2p

## Description

Bring initial mix support in nim-libp2p to prototype status—clean codebase, enforce style/CI, prep for PoCs; concurrently, work with ACZ to upstream the specs.

## Task List

### Maintenance

* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-mix:mix-core`
* owner: rramos
* status: done
* start-date: 2025-07-16
* end-date: 2025-09-30

#### Description
Get the core mix functionality in nim-libp2p as Prototype / Unstable state, this will allow mix to be used in PoCs or experiments. Some rough edges and minor issues expected, not recommended for production and API and internal structure subject to changes. Implement any needed refactorings, code cleanup and style conformity, as well as setting up the repository so CI tasks for running test units and ensuring code formatting is applied, and master branch protection is enabled.

#### Deliverables
- From commit [273f047](https://github.com/vacp2p/nim-libp2p/commit/273f047efe2e91f76b7dbdffe09a51708599b851) onwards, mix is available in `master` branch of `nim-libp2p`.
- Code has been cleaned up comparing original repository and functionality included in nim-libp2p repository
- Original [repository](https://github.com/vacp2p/mix/) will be archived once Release v1.14.0 of nim-libp2p is published


### Specs

* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-mix:specs`
* owner: 
* status: not started
* start-date:
* end-date:

#### Description
Collaborate with ACZ team into upstreaming initial mix design and rationale to 
`libp2p/spec` as proposal or draft PR.


#### Deliverables

