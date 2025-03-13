---
title: Staking Protocol Refinement
tags:
  - "2025q1"
  - "sc"
  - "status"
draft: false
description: Refinement of the staking protocol, revisiting features that didn't make it in previous iterations.
---

`vac:sc:status:2025q1-staking-protocol-refinement`

Revisit, research and implement features that didn't make it in the previous quarter. 

## Description

After building a first version of the SNT staking protocol for Status Network, we will now revisit some of the features that we didn't implement in the previous iteration.

This includes

- Researching and implementing a way to allow users to add funds to an existing staking vault
- Researching and implementing the possibility for users to lock their funds multiple times
- Implementing minimal proxy clones for stake vaults to make vault creation as cheap as possible
- Fixing bugs that were found in the previous iteration
- Refactoring parts of the code we thing needs adjustment for maintainability

## Task List


### Fixing bugs
* fully qualified name: `2025q1-staking-protocol-refinement:fixing-bugs`
* owner: r4bbit
* status: done
* start-date: 2025/01/01
* end-date: 2025/03/31

#### Description

To make sure the staking protocol works as intended,
we need to fix any bugs we encounter during the refinement phase.
This task is about tracking and addressing issues that come up.

#### Deliverables

- [x] [Re-implementation of MP compound mechanism](https://github.com/vacp2p/staking-reward-streamer/pull/136)

### Refactoring
* fully qualified name: `2025q1-staking-protocol-refinement:refactoring`
* owner: 
* status: in progress
* start-date: 2025/01/01
* end-date: 2025/03/31

#### Description

While the protocol is largely functional,
we want to ensure it's composability and maintainability over time.
Therefore,
some work items related to refactoring the existing codebase might be requrred.
This task is about tracking and addressing these.

#### Deliverables

- [x] [Update terminology used in contracts](https://github.com/vacp2p/staking-reward-streamer/pull/97)
- [x] [Isolating MP math](https://github.com/vacp2p/staking-reward-streamer/pull/109)
- [x] [Storage gap implementation](https://github.com/vacp2p/staking-reward-streamer/pull/149)

### Adding funds to existing vaults

* fully qualified name: `2025q1-staking-protocol-refinement:adding-funds-to-existing-vaults`
* owner: gravityblast
* status: in progress (80%)
* start-date: 2025/01/01
* end-date: 2025/01/21

#### Description

Due to historic reasons that can't be recalled, we didn't implement the possibility for users to add funds to an existing vault.
This is a feature that we'd like to have in the protocol,
as it allows for a more flexible user experience.

Part of this task is to research how adding funds to an already funded vault affects the multiplier points generation and inherintely the XP token rewards.
If it turns out to be feasible,
implementation should follow.

#### Deliverables

- [] Implementation of `stake()` function that allows for adding funds to an existing vault 
- [] Tests proving its functionality
- [] If necessary, additional rules for the formal verification
- [] Updated documentation


### Locking funds multiple times

* fully qualified name: `2025q1-staking-protocol-refinement:locking-funds-multiple-times`
* owner: 3esmit
* status: done 
* start-date: 2025/01/01
* end-date: 2025/01/21

#### Description

To keep the protocol simple and consistent,
just like we currently don't allow for adding funds to an existing vault that already has funds,
we don't allow for locking staked funds more than once.
This is also to ensure that we don't run into scenarios where users will lock their stake for an amount of time that is not beneficial to the amount of XP they'll earn.

In this iteration, 
we want to revisit this functionality and ideally allow for users to lock their funds multiple times.

Example:

- User stakes funds
- User locks funds for 3 months
- 3 months pass
- User locks funds again
- Repeat (as long as it makes sense)

Due to the token economics,
there's an upper limit on how long locking up funds can be incentivized.
This is something that needs to be researched and implemented.


#### Deliverables

- [x] [Implementation of `lock()` function that allows for locking stake multiple times](https://github.com/vacp2p/staking-reward-streamer/pull/162)
- [x] [Tests proving its functionality](https://github.com/vacp2p/staking-reward-streamer/pull/162)

### Optimize gas costs for vault creation

* fully qualified name: `2025q1-staking-protocol-refinement:stakes-vaults-proxy-clones`
* owner: r4bbit
* status: done
* start-date: 2025/01/01
* end-date: 2025/01/21

#### Description

While the contract size of `StakeVault` is already fairly limited,
we can still squeeze out some more bytes implementing a pattern that is known as "Minimal Proxy Clones".

The idea is to,
instead of creating and deploying copies of `StakeVault`,
deploy just a single template `StakeVault` and clone proxies instead.

Part of this task is to research if this pattern is feasible and if it is,
implement it.

#### Deliverables

- [x] [Implementation of `StakeVault` minimal proxy clones](https://github.com/vacp2p/staking-reward-streamer/commit/18fb16bcc67fa9d0647accf7f6377376a23b1525)
- [x] [Integration tests to ensure it works](https://github.com/vacp2p/staking-reward-streamer/commit/18fb16bcc67fa9d0647accf7f6377376a23b1525#diff-9fba913da43564473980fc4cabf095465fcaf84f425e08d6a6d807c0e8b745c0)
- [x] [Updated deployment scripts](https://github.com/vacp2p/staking-reward-streamer/commit/18fb16bcc67fa9d0647accf7f6377376a23b1525#diff-a86f9f3c1b97ab54108b58c44e3e721fae338da4bb2b5578b175c29160cb4b66)

### Deployment on Status Network testnet

* fully qualified name: `2025q1-staking-protocol-refinement:status-network-testnet-deployment`
* owner: r4bbit
* status: done
* start-date: 2025/01/01
* end-date: 2025/03/31

#### Description

Status aims to have the staking protocol deployed on a testnet in April 2025,
however,
if they manage to put out a Status Network testnet before,
then we'll deploy the system earlier. 

#### Deliverables

- [x] [Contract addresses of the deployed system on testnet](https://www.notion.so/Contract-Deployment-Addresses-d6dd98b1b4f6461d82eec6ab18b852c8?pvs=4#1ac8f96fb65c80cc9f1adf389a575d3f)
