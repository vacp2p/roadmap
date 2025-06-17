---
title: Status Network Native Dex
tags:
  - "2025q2"
  - "sc"
  - "status"
draft: false
description: Implementing a native DEX for the Status Network.
---

`vac:sc:status:2025q2-sn-native-dex`

Implementing a native DEX for the Status Network.

**This commitment has been removed. The Status Network team has decided to outsource the work to a 3rd party team.**


## Description

The Status Network needs a decentralized exchange (DEX) to allow users to trade tokens in a trustless manner.
The idea is to fork Uniswap V2 and extend it with additional features that are useful for the Status Network.
The changes to the fork are minor,
as the only requested changes are,
that the transaction fee is adjusted and the generated profit is sent to a splitter contract.

## Task List

### Implementation
* fully qualified name: `2025q2-sn-native-dex:implementation`
* owner: 
* status: not started
* start-date: 2025/04/01
* end-date: 2025/04/30

#### Description

The goal is to fork Uniswap V2 and make the necessary changes to the contract.
The details of those changes need to be discussed with the Status Network team.

#### Deliverables

- [ ] Forked Uniswap V2 contract with the necessary changes and tests

### Status Network Testnet Deployment
* fully qualified name: `2025q2-sn-native-dex:testnet-deployment`
* owner: 
* status: not started
* start-date: 2025/05/01
* end-date: 2025/05/30

#### Description

Deployment of the Status Network native DEX on the testnet.

#### Deliverables

- [ ] Contract addresses of the deployed DEX on the testnet

### Status Networtk Mainnet Deployment
* fully qualified name: `2025q2-sn-native-dex:mainnet-deployment`
* owner: 
* status: not started
* start-date: 2025/06/31
* end-date: 2025/06/31

#### Description

After successful testing on the testnet, we will deploy the dex on the Status Network mainnet.

- [ ] Deployment of the dex on Status Network mainnet
