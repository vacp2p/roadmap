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

- [ ] Design document explaining how the yield-bearing module will be integrated into the bridge protocol

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

#### Deliverables

- [ ] Implementation of agreed architecture and interfaces for eth bridging

### Status Networtk Devnet Deployment
* fully qualified name: `2025q2-sn-native-bridge-yield-bearing-module:devnet-deployment`
* owner: andrea
* status: done
* start-date: 2025/06/01
* end-date: 2025/06/31

#### Description

Once the fundamental architecture is implemented, we will deploy it on the Status Network devnet for further testing.
We should spend a significant amount of time testing the module with other team members to ensure that it works as expected.

#### Deliverables

- [ ] Deployment of base architecture on Status Network devnet
