---
title: Anoncomms testing
tags:
  - "2026q1"
  - "qa"
  - "anoncomms"
draft: false
description: Expand QA coverage for anoncomms crypto and consensus components with negative-path and error-handling tests.
---

`ift-ts:qa:anoncomms:2026q1-anoncomms-testing`

## Description

Expand QA coverage for Zerokit RLN and hashgraph-like consensus by adding negative-path, error-handling, and regression tests, and by reviewing existing coverage for gaps.

Baseline test suites and file entry points for onboarding:
- Zerokit RLN tests: https://github.com/vacp2p/zerokit/tree/master/rln/tests (public.rs, protocol.rs, poseidon_tree.rs, ffi_utils.rs, ffi.rs, utils.rs).
- Zerokit Utils tests: https://github.com/vacp2p/zerokit/tree/master/utils/tests (poseidon_hash_test.rs, poseidon_constants.rs, merkle_tree.rs).
- Zerokit RLN-WASM tests: https://github.com/vacp2p/zerokit/tree/master/rln-wasm/tests (utils.rs, node.rs, browser.rs).
- Hashgraph-like consensus tests: https://github.com/vacp2p/hashgraph-like-consensus/tree/main/tests (concurrency_tests.rs, consensus_service_tests.rs, network_gossip_tests.rs, rfc_compliance_tests.rs, scope_config_tests.rs, storage_stream_tests.rs, threshold_tests.rs, vote_tests.rs, vote_validation_tests.rs).

## Task List

### Zerokit RLN negative-path hardening

* fully qualified name: `ift-ts:qa:anoncomms:2026q1-anoncomms-testing:rln-negative-paths`
* owner: Roman
* status: done
* start-date: 2026/01/01
* end-date: 2026/02/10

#### Description

- Review existing RLN coverage and document gaps.
- Add proof verification failure cases by mutating `external_nullifier`, `message_id`, `x`, and single `path_element` for `verify_rln_proof` and `verify_with_roots`.
- Add rate-limit validation tests for `RLNWitnessInput` (reject `message_id >= user_message_limit` and `limit = 0`).
- Add resource error tests for missing or wrong `rln_final.arkzkey` and `graph.bin`, plus mismatched tree depth.
- Add Merkle tree invalid proof tests (old root after update, wrong leaf index).
- Add tests for PM tree feature coverage.
- Baseline references:
  - https://github.com/vacp2p/zerokit/tree/master/rln/tests
  - public.rs, protocol.rs, poseidon_tree.rs, ffi_utils.rs, ffi.rs, utils.rs

#### Deliverables

- [vacp2p/zerokit#372](https://github.com/vacp2p/zerokit/pull/372) test: Improve coverage for protocol and circuit modules
- [vacp2p/zerokit#371](https://github.com/vacp2p/zerokit/pull/371) chore: Test coverage report for CI
- PR(s) with new RLN negative-path and resource error tests.
- Test report listing covered gaps and remaining risks.
- [vacp2p/zerokit#367](https://github.com/vacp2p/zerokit/pull/367) Test Merkle invalid proof and PM tree coverage tests
- [vacp2p/zerokit#365](https://github.com/vacp2p/zerokit/pull/365) Rate-limit validation and resource error tests
- [vacp2p/zerokit#363](https://github.com/vacp2p/zerokit/pull/363) Test RLN proof verification failure cases
- [vacp2p/zerokit#369](https://github.com/vacp2p/zerokit/issues/369) Unable to build with compression feature on for wasm32 target
- [vacp2p/zerokit#366](https://github.com/vacp2p/zerokit/issues/366) Unhandled error case mismatch between zkey_data and graph_data

### Zerokit serialization and FFI error handling

* fully qualified name: `ift-ts:qa:anoncomms:2026q1-anoncomms-testing:serialization-ffi-errors`
* owner: Roman
* status: in progress (90%)
* start-date: 2026/02/01
* end-date: 2026/03/15

#### Description

- Add truncated/extra-byte serialization tests for witness/proof values (Rust and FFI) and assert rejection.
- Extend C FFI coverage for out-of-bounds, bad depth, and invalid inputs to ensure `CResult.err` is returned.
- Add negative/invalid input tests for RLN-WASM bindings.
- Baseline references:
  - https://github.com/vacp2p/zerokit/tree/master/utils/tests
  - https://github.com/vacp2p/zerokit/tree/master/rln-wasm/tests

#### Deliverables

- [vacp2p/zerokit#383](https://github.com/vacp2p/zerokit/issues/383)
- PR(s) with serialization and FFI error-path tests.
- Test report describing validation behavior and coverage.

### Hashgraph-like consensus negative tests

* fully qualified name: `ift-ts:qa:anoncomms:2026q1-anoncomms-testing:hashgraph-negative-tests`
* owner: TBD
* status: not started
* start-date: 2026/02/15
* end-date: 2026/03/31

#### Description

- Add negative tests for proposal/vote lifecycle and timeout behavior.
- Validate consensus result calculations for both p2p and gossipsub networks.
- Expand invalid vote/proposal cases beyond happy-path coverage.
- Baseline references:
  - https://github.com/vacp2p/hashgraph-like-consensus/tree/main/tests
  - concurrency_tests.rs, consensus_service_tests.rs, network_gossip_tests.rs, rfc_compliance_tests.rs, scope_config_tests.rs, storage_stream_tests.rs, threshold_tests.rs, vote_tests.rs, vote_validation_tests.rs

#### Deliverables

- PR(s) with new negative-path consensus tests.
- Test report summarizing outcomes and open issues.
