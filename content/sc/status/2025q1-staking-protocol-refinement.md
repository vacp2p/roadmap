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

## Task List

### Adding funds to existing vaults

* fully qualified name: `2025q1-staking-protocol-refinement:adding-funds-to-existing-vaults`
* owner: 
* status: not started
* start-date: 2024/01/01
* end-date: 2024/01/21

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
* owner: 
* status: not started
* start-date: 2024/01/01
* end-date: 2024/01/21

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

- [] Implementation of `lock()` function that allows for locking stake multiple times
- [] Tests proving its functionality
- [] If necessary, additional rules for the formal verification
- [] Updated documentation

### Optimize gas costs for vault creation

* fully qualified name: `2025q1-staking-protocol-refinement:stakes-vaults-proxy-clones`
* owner: 
* status: not started
* start-date: 2024/01/01
* end-date: 2024/01/21

#### Description

While the contract size of `StakeVault` is already fairly limited,
we can still squeeze out some more bytes implementing a pattern that is known as "Minimal Proxy Clones".

The idea is to,
instead of creating and deploying copies of `StakeVault`,
deploy just a single template `StakeVault` and clone proxies instead.

Part of this task is to research if this pattern is feasible and if it is,
implement it.

#### Deliverables

- [] Implementation of `StakeVault` minimal proxy clones
- [] Integration tests to ensure it works
- [] Updated deployment scripts
- [] Updated documentation

### Deployment on Status Network testnet

* fully qualified name: `2025q1-staking-protocol-refinement:status-network-testnet-deployment`
* owner: 
* status: not started
* start-date: 2025/01/01
* end-date: 2025/03/31

#### Description

Status aims to have the staking protocol deployed on a testnet in April 2025,
however,
if they manage to put out a Status Network testnet before,
then we'll deploy the system earlier. 

#### Deliverables

- [] Contract addresses of the deployed system on testnet
