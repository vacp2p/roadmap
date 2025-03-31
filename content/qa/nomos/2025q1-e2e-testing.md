---
title: Nomos E2E Testing for Nomos Node
tags:
  - "2025q1"
  - "qa"
  - "nomos"  
draft: false  
description: Maintain and ensure the reliability of Nomos e2e tests.
---

`vac:qa:nomos:2025q1-e2e-testing`

## Description
Maintain and ensure the continued reliability of the Nomos end to end testing framework. 
This includes addressing regressions, adapting code in `nomos-e2e-tests` and `nomos-node`, 
adapting to other changes in `nomos-node`, 
and performing minor improvements to keep the framework functional and effective.

**Alignment with VAC Narratives:**

* The VAC QA team supports internal collaboration and efficiency by maintaining the quality and reliability of the Nomos E2E framework.

## Task List

### Maintenance

* fully qualified name: `vac:qa:nomos:2025q1-e2e-testing:maintenance`
* owner: romanzac
* status: done
* start-date: 2025/01/01
* end-date: 2025/03/31

#### Description
Ongoing maintenance of Nomos E2E tests and changes in Nomos Node repository related to Nomos E2E testing. 
This includes updating tests for changes in `nomos-node`, addressing regressions, 
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.

#### Deliverables
* [Two node cluster start automation](https://github.com/logos-co/nomos-e2e-tests/pull/1)
* [fix: Temporarily downgrade cargo-binstall to 1.10.19](https://github.com/logos-co/nomos-node/pull/983)
* [chore: Add LogOutput and LogLevel property to Cfgsync config](https://github.com/logos-co/nomos-node/pull/978)
* [chore: Add reconstruct command to nomos-cli](https://github.com/logos-co/nomos-node/pull/994)
* Consensus is working reported to Risc0 project. Issues with failing tests to be resolved with Nomos devs once Risc0 v1.3 is released.
* [chore: Update nomos-cli reconstruct to work with DaBlob](https://github.com/logos-co/nomos-node/pull/1080)
* [chore: Collect more insight for data dispersal](https://github.com/logos-co/nomos-e2e-tests/pull/6)
* [chore: Add dispersal mempool strategy to cfgsync template](https://github.com/logos-co/nomos-e2e-tests/pull/10)
* [chore: Improve error handling](https://github.com/logos-co/nomos-e2e-tests/pull/11)
