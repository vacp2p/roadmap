---
title: XP Token (v1)
tags:
  - "2024q4"
  - "sc"
  - "status"
draft: false
description: Development of a first version of the XP token contract for Status.
---

`vac:sc:status:xp-token-v1`

Development of a first version of the XP token contract for Status.

## Description

As part of a first version of the staking protocol we're working on and committing to deliver in Q4 2024,
we're aiming for implementing a first version of the XP token contract that complements the staking protocol as well.

The XP token (name of the token TBD) is a non transferable token that users earn by staking SNT tokens,
or by specified onchain activities on the Status Network.
These XP can then be used to participate in community-driven governance,
such as voting apps, and to get access to premium features in the Status app.

We're aiming for implementing a first version of this token and have it ready for deployment on an EVM based test network of Status' choice by the end of Q4 2024.

Here are the main features and requirements of the first version of this token:

- The token is ERC20 compliant but non-transferable
- The contract is upgradable, this is necessary to allow for future improvements and changes
- The token's balances leverage the internal accounting of the staking protocol, among other sources, to provide real-time values

## Task List

### Token implementation

* fully qualified name: `vac:sc:status:xp-token-v1:token-implementation`
* owner: Andrea
* status: in progress (30%)
* start-date: 2024/10/18
* end-date: 2024/10/25

#### Description

Implement the XP token contract according to the requirements outlined above.
For this version, the contract will exclusively rely on the staking protocol's multiplier points estimation to determine the amount of XP tokens a user has access to.

See [this GitHub issue](https://github.com/vacp2p/staking-reward-streamer/issues/34) for more details.

#### Deliverables

- [ ] XP token contract implementation
- [ ] Tests proving its functionality (or lack thereof)

### Formal verification

* fully qualified name: `vac:sc:status:xp-token-v1:formal-verification`
* owner: 
* status: not started
* start-date: 2024/10/21
* end-date: 2024/11/01

#### Description

Formally verify the functionality, correctness and security of the XP token contract.
See [this GitHub issue](https://github.com/vacp2p/staking-reward-streamer/issues/35) for more details.

#### Deliverables

- [ ] Certora spec files containing rules listed in the GitHub issue

### Documentation

* fully qualified name: `vac:sc:status:xp-token-v1:documentation`
* owner:
* status: not started
* start-date: 2024/11/18
* end-date: 2024/11/22

#### Description

Document the token contract and its functionality.

See [this GitHub issue](https://github.com/vacp2p/staking-reward-streamer/issues/36) for more details.


#### Deliverables

As this is a simple contract with few properties, providing documentation as part of the project's README might is sufficient.

- [ ] Comprehensive `README.md`

