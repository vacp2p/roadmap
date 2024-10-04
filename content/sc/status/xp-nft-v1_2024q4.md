---
title: XP NFT (v1)
tags:
  - "2024q4"
  - "sc"
  - "status"
draft: false
---

`vac:sc:status:xp-nft-v1_2024q4`

## Description

In addition to the non-transferable XP token,
Status wants also a non-transferable NFT which,
among other things,
will represent the XP token that a user has accrued via staking SNT and other onchain activities.

The NFT should be evolving in nature,
meaning that,
depending on the amount of XP an account has,
the visual attached to the NFT should change its appearance (currently unspecified how exactly that's going to look like).

We're aiming to have a first version of this XP NFT contract ready for deployment on an EVM based test network of Status' choice by the end of Q4 2024.

Here are the main features and requirements of the first version of this token:

- The token is ERC721 compliant but non-transferable
- The contract is upgradable, this is necessary to allow for future improvements and changes
- The token's metadata is partially retrieved from the XP token contract, allowing users to see their accumulated XP in a single place

## Task List

### Token implementation

* fully qualified name: `vac:sc:status:xp-nft-v1_2024q4:token-implementation`
* owner: 
* status: not started
* start-date: 2024/10/18
* end-date: 2024/10/25

#### Description

Implement the XP token contract according to the requirements outlined above.
For this version,
the contract will exclusively rely on the staking protocol's multiplier points estimation to determine the amount of XP tokens a user has access to.

See [this GitHub issue]() for more details.

#### Deliverables

- [ ] XP token contract implementation
- [ ] Tests proving its functionality (or lack thereof)

### Upgradeability

* fully qualified name: `vac:sc:status:xp-nft-v1_2024q4:upgradeability`
* owner: 
* status: not started
* start-date: 
* end-date: 

#### Description

Make use of battle tested upgradeability patterns to ensure the XP NFT contract can be upgraded in the future.

See [this GitHub issue]() for more details.

#### Deliverables

- [ ] Upgradeable XP NFT contract
- [ ] Tests proving its upgradeability

