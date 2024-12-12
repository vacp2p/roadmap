---
title: XP NFT (v1)
tags:
  - "2024q4"
  - "sc"
  - "status"
draft: false
description: Development of a first version of the XP NFT contract for Status.
---

`vac:sc:status:2024q4-xp-nft-v1`

Development of a first version of the XP NFT contract for Status.

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

* fully qualified name: `2024q4-xp-nft-v1:token-implementation`
* owner: Andrea
* status: done
* start-date: 2024/10/07
* end-date: 2024/10/14

#### Description

Implement the XP token contract according to the requirements outlined above.
For this version,
the contract will exclusively rely on the staking protocol's multiplier points estimation to determine the amount of XP tokens a user has access to.

See [this GitHub issue](https://github.com/vacp2p/staking-reward-streamer/issues/37) for more details.

#### Deliverables

- [x] [XP token contract implementation](https://github.com/vacp2p/staking-reward-streamer/pull/12)
- [x] [Tests proving its functionality (or lack thereof)](https://github.com/vacp2p/staking-reward-streamer/pull/12)

### Upgradeability

* fully qualified name: `2024q4-xp-nft-v1:upgradeability`
* owner: Andrea
* status: done (100%)
* start-date: 2024/10/14
* end-date: 2024/10/25

#### Description

Make use of battle tested upgradeability patterns to ensure the XP NFT contract can be upgraded in the future.

See [this GitHub issue](https://github.com/vacp2p/staking-reward-streamer/issues/38) for more details.

#### Deliverables

- [x] [Upgradeable XP NFT contract](https://github.com/vacp2p/staking-reward-streamer/blob/main/src/XPNFTToken.sol) (Upgradeable via `setMetadataGenerator` function)
- [x] Tests proving its upgradeability (via [`setMetadataGenerator` function](https://github.com/vacp2p/staking-reward-streamer/blob/main/test/XPNFTToken.t.sol#L44-L51))

