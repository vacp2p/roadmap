---
title: Karma RLN
tags:
  - "2025q2"
  - "sc"
  - "status"
draft: false
description: Implement RLN membership management and integration with the Karma protocol.
---

`vac:sc:status:2025q2-karma-rln`

Implement RLN membership management and integration with the Karma protocol.

## Description

Status Network aims to implement [gasless transactions by leveraging the RLN protocol](https://www.notion.so/Gasless-Transactions-for-Status-Network-using-RLN-shared-1d98f96fb65c809bb986dbf31276d7ad) as a means to offer different tiers to users based on their Karma balance.
The general idea is that users can send a certain amount of transactions within a certain time period without paying gas,
if they own a certain amount of Karma tokens.
The exact amount of transactions and the time periods are specified in tiers.
To make this a reality,
there has to be an RLN contract that allows a privileged actor to register users in the membership tree.
In addition,
there has to be a function to slash users.
In order to retrieve the available tiers,
another contract has to be deployed that provides the necessary data.

## Task List

### Karma slashing function

* fully qualified name: `2025q2-karma-rln:slash-karma`
* owner: r4bbit
* status: done
* start-date: 2025/05/21
* end-date: 2025/06/31

#### Description

Implement a function in the `Karma` contract allows privileged actors to slash a given account's Karma balance.
A first version of this should add a percentage value to the contract that can be configured by the privileged actor.
The `slash(account)` function should then slash the Karma balance of the given account by the percentage value.

#### Deliverables

- [ ] Commit that introduces slash functionality
- [ ] Unit tests for the slashing function
- [ ] Formal verification of the slashing function
- [ ] Documentation for the contract

### Implement KarmaTier contract

* fully qualified name: `2025q2-karma-rln:karma-tiers`
* owner: Ricardo
* status: not started
* start-date: 2025/05/21
* end-date: 2025/06/31

#### Description

Implement a contract that provides the available tiers for the gasless transactions system.
Tiers are currently defined in [this document](https://www.notion.so/Gasless-Transactions-for-Status-Network-using-RLN-shared-1d98f96fb65c809bb986dbf31276d7ad).
The owner of the contract should be able to update the tiers.
It should also be possible to add new tiers.

#### Deliverables

- [ ] Commit that introduces `KarmaTiers` contract
- [ ] Unit tests for updating and adding tiers
- [ ] Documentation for the contract

### Implement KarmaRLN contract

* fully qualified name: `2025q2-karma-rln:implementation`
* owner: Ricardo
* status: 80%
* start-date: 2025/05/21
* end-date: 2025/06/31

#### Description

Implement the RLN contract that allows for registering users and slashing their Karma.
We can likely take a lot of ideas from what the [WakuRLNV2](https://github.com/waku-org/waku-rlnv2-contract/blob/main/src/WakuRlnV2.sol#L4) contract does.

#### Deliverables

- [ ] Commits that introduce `KarmaRLN` contract
- [ ] Unit tests
- [ ] Documentation for the contract
