---
title: Logos LEZ Sequencing
tags:
  - "2026q3"
  - "qa"
  - "logos"
draft: false
description: Add automated test coverage for Logos Execution Zone sequencing.
---

`ift-ts:qa:logos:2026q3-lez-sequencing`

## Description

Add automated behavioral coverage for Logos Execution Zone sequencing as the sequencer implementation evolves.

## Task List

### Cucumber tests

* fully qualified name: `ift-ts:qa:logos:2026q3-lez-sequencing:cucumber-tests`
* owner: Roman
* status: in progress (20%)
* start-date: 2026/08/17
* end-date: 2026/09/30

#### Description

Add Cucumber scenarios covering LEZ sequencer registration behavior.

#### Deliverables
- Cucumber test coverage for LEZ sequencer registration
- [logos-execution-zone#854](https://github.com/logos-blockchain/logos-execution-zone/issues/854) Public actions, nonces and program image claims of a private transaction are not padded
- [logos-execution-zone#849](https://github.com/logos-blockchain/logos-execution-zone/issues/849) AMM derives the token program from a caller-supplied holding account and hands vault PDA authorization to it
- [logos-execution-zone#862](https://github.com/logos-blockchain/logos-execution-zone/issues/862) Token definition and account initialization write to any empty target without requiring authorization
- [logos-execution-zone#853](https://github.com/logos-blockchain/logos-execution-zone/issues/853) Init note view tag is derived only from the recipient's public keys
- [logos-execution-zone#852](https://github.com/logos-blockchain/logos-execution-zone/issues/852) Private note ciphertext length equals the fixed header plus the raw account encoding
- [logos-execution-zone#848](https://github.com/logos-blockchain/logos-execution-zone/issues/848) Wallet reveals the commitments it is about to spend to the sequencer via getProofsAndRoot
- [logos-execution-zone#868](https://github.com/logos-blockchain/logos-execution-zone/issues/868) Sequencer requeueCrossZoneDeadLetter is an unauthenticated state-mutating method on the public RPC port
- [logos-execution-zone#856](https://github.com/logos-blockchain/logos-execution-zone/issues/856) AMM remove_liquidity multiplies reserve and supply by a caller-chosen amount without checked arithmetic
- [logos-execution-zone#850](https://github.com/logos-blockchain/logos-execution-zone/issues/850) Wallet-created private accounts are seeded with identifier 0
- [logos-execution-zone#859](https://github.com/logos-blockchain/logos-execution-zone/issues/859) Private transactions are admitted to the mempool without a fee, proof verification, or deduplication
- [logos-execution-zone#857](https://github.com/logos-blockchain/logos-execution-zone/issues/857) Wallet stores decrypted note contents without checking that the recomputed commitment is in the transaction
- [logos-execution-zone#866](https://github.com/logos-blockchain/logos-execution-zone/issues/866) Indexer getBlocks materializes one block id and one RocksDB key per requested row before any lookup
- [logos-execution-zone#864](https://github.com/logos-blockchain/logos-execution-zone/issues/864) Publish failure after block building drops the mempool transactions included in the block
- [logos-execution-zone#867](https://github.com/logos-blockchain/logos-execution-zone/issues/867) Sequencer getProofsAndRoot and getAccountsNonces have no element cap and run under the chain lock; getBlockRange materializes up to 1024 blocks per call
- [logos-execution-zone#869](https://github.com/logos-blockchain/logos-execution-zone/issues/869) Program loader WriteSegment and CreateHeader accept any default target without requiring authorization
- [logos-execution-zone#865](https://github.com/logos-blockchain/logos-execution-zone/issues/865) Group invites are accepted without any sender authentication or group binding
- [logos-execution-zone#858](https://github.com/logos-blockchain/logos-execution-zone/issues/858) Wallet persists spending, authorization, viewing, group and sealing secrets as plaintext JSON and discards the password
- [logos-execution-zone#863](https://github.com/logos-blockchain/logos-execution-zone/issues/863) Block timestamp is chosen by the producer and only checked for agreement with the clock transaction
- [logos-execution-zone#861](https://github.com/logos-blockchain/logos-execution-zone/issues/861) Slash approvals sign only a domain, key and inscription and are not recorded once consumed
- [logos-execution-zone#855](https://github.com/logos-blockchain/logos-execution-zone/issues/855) Wallet and core code print or log decrypted account state and secret key material
