---
title: Status Network Native Bridge Yield Bearing Module
tags:
  - "2025q2"
  - "sc"
  - "status"
draft: false
description: Design and implement architecture to enable yield generation in the Status Network native bridge.
---

`vac:sc:status:2025q2-sn-native-bridge-yield-bearing-module`

Design and implement architecture to enable yield generation in the Status Network native bridge.

## Description

The native bridge of Status Network needs to be extended,
such that it allows for generating yield on the bridged assets.
The general idea is that users lock their assets in the L1 bridge contract and the bridge deposits them to yield-bearing protocols.
The yield is then regularly harvested and distributed on the L2.
This commitment is about laying the groundwork for this feature,
by designing and implementing the necessary interfaces and base contracts.

**Linea has decided to take over the work of building the yield-bearing bridge, due to an internal roadmap change.**

## Task List


### Research and Design
* fully qualified name: `2025q2-sn-native-bridge-yield-bearing-module:research-design`
* owner: r4bbit
* status: done
* start-date: 2025/04/01
* end-date: 2025/04/30

#### Description

This task is about researching the existing bridge protocol to get a better understanding of how it works and how it can and should be extended to allow for yield generation.
In addition,
we need to collaborate with the Linea team to understand what their requirements are.
The goal is to have a clear plan on how to implement the fundamental architecture.

#### Deliverables

- [x] [Design document explaining how the yield-bearing module will be integrated into the bridge protocol](https://www.notion.so/Native-yield-bearing-bridge-on-Linea-shared-1d98f96fb65c80edbfbde3d83746c187)
- [x] [StatusL2 Yield Management](https://www.notion.so/Yield-management-on-Status-Network-shared-2168f96fb65c80fc9596dedeef903a74)

### Fundamental Architecture Implementation

* fully qualified name: `2025q2-sn-native-bridge-yield-bearing-module:implementation`
* owner: andrea
* status: done
* start-date: 2025/05/01
* end-date: 2025/05/30

#### Description

After we've created a proper plan on how to implement the basic architecture and interfaces,
the next step is to actually implement it.
Testing and verification of its functionality is also part of this task and will happen as the fundamentals are implemented.

**After this task was done, Linea has decided to take over the work of building the yield-bearking bridge, due to an internal roadmap change.**

#### Deliverables

- [x] [PR #21](https://github.com/vacp2p/linea-monorepo/pull/21)
- [x] [PR #22](https://github.com/vacp2p/linea-monorepo/pull/22)
- [x] [PR #23](https://github.com/vacp2p/linea-monorepo/pull/23)
- [x] [PR #25](https://github.com/vacp2p/linea-monorepo/pull/25)

### Status Networtk Devnet Deployment
* fully qualified name: `2025q2-sn-native-bridge-yield-bearing-module:devnet-deployment`
* owner: andrea
* status: cancelled
* start-date: 2025/06/01
* end-date: 2025/06/31

#### Description

Once the fundamental architecture is implemented, we will deploy it on the Status Network devnet for further testing.
We should spend a significant amount of time testing the module with other team members to ensure that it works as expected.

**Linea has decided to take over the work of building the yield-bearking bridge, due to an internal roadmap change.**

#### Deliverables

- [ ] Deployment of base architecture on Status Network devnet
