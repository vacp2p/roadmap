---
title: Base Chain Integration
tags:
  - "2025q1"
  - "sc"
  - "status"
draft: false
description: Creation and deployment of Status app smart contracts for Base chain.
---

`vac:sc:status:2025q1-base-chain-integration`

Creation and deployment of Status app smart contracts for Base chain.

## Description

Status aims to integrate with Base chain as another L2 solution to operate on.
To provide the same user experience and features as on Ethereum mainnet and other L2s they are supporting,
we need to deploy the Status app smart contracts on Base chain and ensure that there's a bridged SNT token availble for these apps.

## Task List

### Research and implement SNT bridge token 

* fully qualified name: `2025q1-base-chain-integration:snt-bridge-token`
* owner: r4bbit
* status: done
* start-date: 2025/01/01
* end-date: 2025/02/01

#### Description

Status would like to deploy liquidity pools on Base.
To make this happen,
some form of SNT token needs exist on the Base L2.
This task is about researching the best way to do this and implementing it.

There's also the question of whether Status needs an SNT version on Base chain that has the additional features that SNT has on Ethereum mainnet.
That decision will affect out implementation.

#### Deliverables

- [x] [SNT contract for Base chain and deployment address](https://basescan.org/address/0x662015EC830DF08C0FC45896FaB726542e8AC09E#code)
- [x] ~~Tests proving its functionality~~ (not needed, as this is Base's canonical implementation)

### Deployment of Status community contracts

* fully qualified name: `2025q1-base-chain-integration:communities-contracts-deployment`
* owner: r4bbit
* status: done
* start-date: 2025/01/01
* end-date: 2025/02/01

#### Description

Status community contracts are a set of smart contracts that allow users to create and manage access control for communities.
These contracts are currently deployed on Ethereum mainnet and other L2s.
This task is about deploying them on Base chain too.

#### Deliverables

- [x] [Deployment addresses of communities contracts](https://www.notion.so/Contract-Deployment-Addresses-d6dd98b1b4f6461d82eec6ab18b852c8?pvs=4#d14be5b1e9da45a59b8f9578eb80d756)
