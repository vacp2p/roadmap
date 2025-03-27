---
title: Status Network Native Bridge Yield Bearing Module
tags:
  - "2025q2"
  - "sc"
  - "status"
draft: false
description: Implementing a yield-bearing module for the Status Network Native Bridge.
---

`vac:sc:status:2025q2-sn-native-bridge-yield-bearing-module`

Implementing a yield-bearing module for the Status Network Native Bridge.

## Description

The native bridge of Status Network needs to be extended by a module that allows for generating yield on the bridged assets.
The general idea is that users lock their assets in the L1 bridge contract and the bridge module deposits them to yield-bearing protocols.
The yield is regularly harvested and distributed on the L2.

## Task List


### Research and Design
* fully qualified name: `2025q2-sn-native-bridge-yield-bearing-module:research-design`
* owner: 
* status: not started
* start-date: 2025/04/01
* end-date: 2025/04/30

#### Description

This task is about researching the existing bridge protocol to get a better understanding of how it works and how the yield-bearing module can be integrated.
In addition, we need to discuss with Linea if they want to implement the "modularity" of the bridge themselves,
or if that should also be done by us.
The goal is to have a clear plan on how to implement the yield-bearing module.

#### Deliverables

- [ ] Design document explaining how the yield-bearing module will be integrated into the bridge protocol

### Module implementation

* fully qualified name: `2025q2-sn-native-bridge-yield-bearing-module:implementation`
* owner: 
* status: not started
* start-date: 2025/05/01
* end-date: 2025/05/30

#### Description

After we've created a proper plan on how to implement the module extension for the bridge,
the next step is to actually implement it.
Here it's important that the module will be implemented upstream in the linea mono repository.
Testing and verification of its functionality is also part of this task and will happen in that repository as well.

#### Deliverables

- [ ] Yield-bearing module implementation (link to PR in Linea mono repository)

### Status Networtk Testnet Deployment
* fully qualified name: `2025q2-sn-native-bridge-yield-bearing-module:testnet-deployment`
* owner: 
* status: not started
* start-date: 2025/06/01
* end-date: 2025/06/31

#### Description

Once the module is implemented, we will deploy it on the Status Network testnet for further testing.
We should spend a significant amount of time testing the module with other team members to ensure that it works as expected.

#### Deliverables

- [ ] Deployment of the module on Status Network testnet

### Status Networtk Mainnet Deployment
* fully qualified name: `2025q2-sn-native-bridge-yield-bearing-module:mainnet-deployment`
* owner: 
* status: not started
* start-date: 2025/06/31
* end-date: 2025/06/31

#### Description

After successful testing on the testnet, we will deploy the yield-bearing module on the Status Network mainnet.

- [ ] Deployment of the module on Status Network mainnet
