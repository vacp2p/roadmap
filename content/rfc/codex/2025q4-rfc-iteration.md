---
title: RFC Iteration
tags:
  - 2025q4
  - rfc
  - codex
draft: false
description: "Iteration commitments generally comprise: through discussion and curation, support the process of auditing raw, draft, mature selected RFCs."
---

`vac:rfc:codex:2025q4-rfc-iteration`

Iteration commitments generally comprise:
through discussion and curation,
support the process of auditing raw, draft, mature selected RFCs.

This commitment covers this process for the following Codex RFCs:
block exchange, Erasure coding,  Proving system

## Description

This commitment supports the process of the choosing which raw RFCs,
from the existing documentation to be put in pipeline to be written or updated. 

This commitment supports the audit of the following mature specifications,
which are either in draft or raw states:
- Slot builder
- Purchase module
- Block Exchange
- Erasure coding module
<!--
- Merkle tree
- Prover
- Codex
- Sales module
- Store module
- Community history service
-->

We will also include specification validation - 
editorial work through previous and future RFCs to improve them
(identify edge cases for example)

## Task List

### Slot Builder

- fully qualified name: `vac:rfc:codex:2025q4-rfc-iteration:slot-builder`
- owner: jimstir
- status: done
- start-date: 2025/10/01
- end-date: 2025/10/15

#### Description
Create the RFC for slot builder, updating design decisions and open questions.


#### Deliverables
- [New RFC: CODEX-SLOT-BUILDER](https://github.com/vacp2p/rfc-index/pull/209)

###  Erasure Coding Module

- fully qualified name: `vac:rfc:codex:2025q4-rfc-iteration:erasure-coding-module`
- owner: cofson
- status: not started
- start-date: 2025/10/15
- end-date: 2025/10/30

#### Description
Create the RFC for the erasure coding module that documents data availability behaviour.

#### Deliverables
- PRs/Issues/Docs/Reports

### Purchase Module

- fully qualified name: `vac:rfc:codex:2025q4-rfc-iteration:purchase-module`
- owner: cofson
- status: not started
- start-date: 2025/10/04
- end-date: 2025/10/19

#### Description
Create the RFC for the purchase module covering pricing, incentives, and settlement flows.

#### Deliverables
- PRs/Issues/Docs/Reports

### The Block Exchange

- fully qualified name: `vac:rfc:codex:2025q4-rfc-iteration:the-block-exchange`
- owner: cofson
- status: done
- start-date: 2025/10/04
- end-date: 2025/10/31

#### Description
Create the RFC for the block exchange defining peer interactions for trading Codex data.

#### Deliverables
- [Block exchange RFC draft](https://github.com/vacp2p/rfc-index/pull/211)

### Merkle Tree Specification

- fully qualified name: `vac:rfc:codex:2025q4-rfc-iteration:merkle-tree`
- owner: cofson
- status: done
- start-date: 2025/10/04
- end-date: 2025/11/10

#### Description
Document the Merkle tree component, clarifying hashing strategy, storage layout, and verifier expectations.

#### Deliverables
- [Created codex/raw/codex-merkle-tree.md file](https://github.com/vacp2p/rfc-index/pull/203)

### Prover Module

- fully qualified name: `vac:rfc:codex:2025q4-rfc-iteration:prover`
- owner: cofson
- status: done
- start-date: 2025/10/04
- end-date: 2025/11/10

#### Description
Capture the prover workflow, artefacts, and interface details to support Codex storage proofs.

#### Deliverables
- [Created codex/raw/codex-prover.md file](https://github.com/vacp2p/rfc-index/pull/205)

### Store Module

- fully qualified name: `vac:rfc:codex:2025q4-rfc-iteration:store`
- owner: cofson
- status: done
- start-date: 2025/10/04
- end-date: 2025/11/10

#### Description
Capture the prover workflow, artefacts, and interface details to support Codex store protocol.

#### Deliverables
- [Created codex/raw/codex-store.md file](https://github.com/vacp2p/rfc-index/pull/207)

### Marketplace Module

- fully qualified name: `vac:rfc:codex:2025q4-rfc-iteration:marketplace`
- owner: cofson
- status: done
- start-date: 2025/10/04
- end-date: 2025/11/10

#### Description
Capture the prover workflow, artefacts, and interface details to support Codex marketplace protocol.

#### Deliverables
- [CODEX-MARKETPLACE: New Raw RFC ](https://github.com/vacp2p/rfc-index/pull/36)

### Community History

- fully qualified name: `vac:rfc:codex:2025q4-rfc-iteration:community-history`
- owner: jimstir
- status: done
- start-date: 2025/11/05
- end-date: 2025/11/15

#### Description
Author the community history RFC.

#### Deliverables
- [Community history RFC draft](https://github.com/vacp2p/rfc-index/pull/214)
