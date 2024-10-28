---
title: Staking Protocol (v1)
tags:
  - "2024q4"
  - "sc"
  - "status"
draft: false
description: Delivery of a first version of the SNT staking protocol for testnet deployment.
---

`vac:sc:status:staking-protocol-v1`

Delivery of a first version of the SNT staking protocol for testnet deployment.

## Description

In collaboration with Status, we are building a staking protocol that enables holders of SNT to stake their tokens to ultimately earn non-transferable "XP" tokens, 
which can later be used to participate in community-driven governance, such as voting apps, and to get access to premium features in the Status app.

We're aiming to have a first version of the staking protocol ready for deployment on an EVM based test network of Status' choice by the end of Q4 2024.
This will give us the opportunity to test the system in a distributed environment.
Future commitments will allow us to refine the system and add additional features as required by Status.

Here are the main features and requirements of the first version of the staking protocol:

- Users can stake SNT tokens and accumulate "multiplier points" in return (multiplier points are later used to determine the amount of XP tokens a user has access to)
- Multiplier points are generated at an at least 1:1 ratio with the amount of SNT staked, at the time of staking
- Users can lock their SNT tokens for a certain period of time (e.g. 3 months - 4 years) to earn additional multiplier points, at the time of staking
- Users can unstake their SNT tokens at any time (unless locked)
- Multiplier points accrue as a function of time and the amount of SNT staked
- Staking protocol should be upgradable
- Users should be able to opt out of upgrades

We've already implemented two different staking algorithms,
so we can leverage this work to finalize a first version of the protocol.

## Task List

### Merging existing solutions

* fully qualified name: `vac:sc:status:staking-protocol-v1:merging-existing-solutions`
* owner: ricardo
* status: in progress (75%)
* start-date: 2024/10/07
* end-date: 2024/10/18

#### Description

After we've implemented two different staking solutions,
it's time for us to compose them into something that uses the best properties of both worlds.

Right now there's [logos-co/staking](https://github.com/logos-co/staking) and [vacp2p/staking-reward-streamer](https://github.com/vacp2p/staking-reward-streamer). 
We've reached consensus that the latter is the better solution for the problem at hand, as it allows for real-time balance updates in the protocol. 

However, the former comes with a few architectural benefits that we'd like to leverage as well.
Namely the composition of `StakeVault` and `StakeManager` and its whitelisting capabilities.

This bigger task is putting together a codebase that makes use of the `StakeVault` <-> `StakeManager` architecture, while also implementing the multiplier point system from the `staking-reward-streamer` solution.

See [this GitHub issue](https://github.com/vacp2p/staking-reward-streamer/issues/13) for more details.

#### Deliverables

- [ ] `StakeVault` and `StakeManager` implementation leveraging reward streamer

### Upgradeability

* fully qualified name: `vac:sc:status:staking-protocol-v1:upgradeability`
* owner: ricardo
* status: in progress (5%)
* start-date: 2024/10/14
* end-date: 2024/10/18

#### Description

Make the system upgradable, ideally using battle tested and standardized upgrade patterns.

See [this GitHub issue](https://github.com/vacp2p/staking-reward-streamer/issues/20) for more details.

#### Deliverables

- [ ] Implementation of upgradeable staking contract
- [ ] Test suite for upgradeable staking contract

### Testing

* fully qualified name: `vac:sc:status:staking-protocol-v1:testing`
* owner: r4bbit 
* status: in progress (80%)
* start-date: 2024/10/07
* end-date: 2024/10/18

#### Description

Create comprehensive test suite that ensure correctness and security of the staking protocol.
Many of those exist already, so we don't have to start from scratch here.

See [this GitHub issue](https://github.com/vacp2p/staking-reward-streamer/issues/17) for more details.

#### Deliverables

- [ ] Test suites as described in the GitHub issue

### Formal verification

* fully qualified name: `vac:sc:status:staking-protocol-v1:formal-verification`
* owner: r4bbit
* status: in progress (70%)
* start-date: 2024/10/07
* end-date: 2024/10/18

#### Description

Formally verify the staking protocol and ensure its correctness and security.
See [this GitHub issue](https://github.com/vacp2p/staking-reward-streamer/issues/19) for more details.


#### Deliverables

- [ ] Certora spec files containing rules listed in the GitHub issue
- [ ] Review of the rules by Certora

### Documentation

* fully qualified name: `vac:sc:status:staking-protocol-v1:documentation`
* owner: r4bbit
* status: in progress (10%)
* start-date: 2024/12/02
* end-date: 2024/12/13

#### Description

Document the overall system and underying algorithms of the staking protocol.
This includes a high level overview of the components and how they are connected,
an explanation of the underlying algorithm and its fundamental math,
and various user stories as examples to illustrate how the protocol behaves.

See [this GitHub issue](https://github.com/vacp2p/staking-reward-streamer/issues/21) for more details.


#### Deliverables

The following documents should be created in the project's repository inside of a `docs` folder:

- [ ] Overview of the staking protocol components
- [ ] Math and algorithm explanation
- [ ] Multiplier points explainer
- [ ] Examples (User stories)

All documents should be written in markdown and contain illustrations as necessary.
