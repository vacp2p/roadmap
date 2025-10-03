---
title: Nescience Consulting
tags:
  - "2025q3"
  - "acz"
  - "nes"
draft: false
description: "Creating research documents and specifications 
for Nescience architecture"

---

`vac:acz:nes:2025q3-nescience-consulting`

Creating research documents and specifications 
for Nescience architecture
## Description

ACZ offers review consulting services to Nescience, 
acting as a bridge between Nescience researchers and engineers, 
facilitating faster and more efficient communication between the two groups.

By utilizing the Nescience Consulting commitment, 

we will reinforce the Conduit of Expertise narrative by:
* The Nescience specifications will be reviewed and refined from an engineering perspective.
* Addressing any potential gaps in the architecture, whether theoretical or practical, 
if any are identified
* Improve communication between Nescience researchers and developers.

We will also strengthen the Premier Research Destination narrative by: 
* This will enable the Nescience project to be more effectively integrated 
and introduced into the ecosystem.

## Task List

### zkVM Benchmark and Survey
* fully qualified name: `vac:acz:nes:2025q3-nescience-consulting:zkvm-benchmark`
* owner: Marvin
* status: done
* start-date: 2025/07/01
* end-date: 2025/07/18

### Description

The [zkVM benchmarks](https://github.com/vacp2p/nescience-zkvm-testing) consisted on basic arithmetic tests.
However, this is not reflective on common computations that the transaction kernel circuits use.
In this task, we extend these tests to include the following benchmarks:

- Elliptic curve arithmetic (scalar multiplication and group addition)
    - jubjub, secp256k1, pallas, vesta, bn254 and bls12-381
- Merkle proof verification
    - Used for non-membership (nullifiers) and membership (UTXO commitments)
- Nullifier generation

Additionally, more zkVMs have been developed and released since Nescience’s initial survey. 
We should analyze a selection of new zkVMs (e.g., zisk and Secret VM) in terms of their usage in NSSA.

**Changes to task:** Nescience’s reaffirmed selection of Risc0 negates the necessity of non-Risc0 tests. Additionally, surveys for additionally zkVMs are not needed.

### Deliverables
* A notion doc to the Nescience notion workspace
* A PR to the [vacp2p/nescience-zkvm-testing](https://github.com/vacp2p/nescience-zkvm-testing) repo

### Alternative UTXO commitment
* fully qualified name: `vac:acz:nes:2025q3-nescience-consulting:alt-utxo`
* owner: Marvin
* status: done
* start-date: 2025/07/11
* end-date: 2025/07/18

### Description

In the [zkVM benchmarks](https://github.com/vacp2p/nescience-zkvm-testing) we determined that
Pedersen commitments are not practical within Risc0. This is a critical issue that must be mitigated.
In this task, we propose an alternate commitment scheme for UTXOs.
Additionally, we demonstrate that this proposal is practical within Risc0 by writing an appropriate guest program.

### Deliverables
* A notion doc to the Nescience notion workspace that describing replacement for UTXO commitment scheme.
* A PR to the [vacp2p/nescience-zkvm-testing](https://github.com/vacp2p/nescience-zkvm-testing) repo

### NSSA feasibility as L2 on Cosmos
* fully qualified name: `vac:acz:nes:2025q3-nescience-consulting:cosmos-l2-feasibility`
* owner: Marvin
* status: done
* start-date: 2025/07/15
* end-date: 2025/07/25

### Description

Nescience’s state seperation architecture (NSSA) is designed to function as a L1 and as a L2.
In this task, we will examine the requirements for running NSSA as a L2 on Cosmos.

### Deliverables
* [A notion doc](https://www.notion.so/NSSA-as-a-Cosmos-Zone-2388f96fb65c8042ad4ae1e805fcc604) to the Nescience notion workspace 

### Privacy Projects Analysis
* fully qualified name: `vac:acz:nes:2025q3-nescience-consulting:privacy-projects-analysis`
* owner: Marvin
* status: done 
* start-date: 2025/08/25
* end-date: 2025/08/08

### Description

This task entails to investigate and analyse existing similar projects.
This deep dive into other projects make it concrete how Nescience sets itself out from each one.
Basically analyse:
    - Privacy claims (and if possible, reality of these claims)
    - Techniques used (e.g., consensus, snarks, etc)

### Deliverables
* [A notion doc](https://www.notion.so/Draft-WIP-2538f96fb65c80ff83afcad4fd3ca2f9) to the Nescience notion workspace 

### Specs for Key Protocols
* fully qualified name: `vac:acz:nes:2025q3-nescience-consulting:key-protocol-spec`
* owner: Marvin
* status: done
* start-date: 2025/08/05
* end-date: 2025/08/19

### Description

This task entails to reparing a document that defines the concrete specifications for key-related hash function digests.
The current key protocol specifications do not explicitly define the digest format for each hash function invocation.
This task aims to formalize the byte-level construction of these digests,
similar to how protocols like Zcash and Iron Fish document their hash inputs and outputs in detail.

Providing precise digest specifications will reduce engineering and implementation overhead,
enable robust versioning and tracking for NSSA key formats, and ensure fixed-length digests that prevent key collision risks.

### Deliverables
* [A notion doc](https://www.notion.so/Concrete-key-protocol-specifications-23b8f96fb65c8011b488c8fe0d2f87ae?source=copy_link#23f8f96fb65c80388d89d6cca9d8ef3d) to the Nescience notion workspace 

### Fee Mechanism
* fully qualified name: `vac:acz:nes:2025q3-nescience-consulting:fee-mechanism`
* owner: Marvin
* status: deprecated 
* start-date: 
* end-date: 

### Description

This task entails conducting preliminary research on existing survey fee mechanisms,
with a focus on models that involve interactions between light users and service nodes.
The goal is to identify viable approaches that could be integrated into the current architecture.
This task may also help streamline responsibilities across the team by potentially reallocating
workload depending on the findings.

### Deliverables
* A notion doc to the Nescience notion workspace 

### DEX Research
* fully qualified name: `vac:acz:nes:2025q3-nescience-consulting:dex-research`
* owner: Marvin
* status: done 
* start-date: 
* end-date: 

### Description

This task involves a high-level comparative analysis of existing privacy-focused projects to Nescience.
Since newcomers to privacy and Web3 may find the claims of these projects difficult to navigate,
the analysis should clarify how Nescience differs, with a focus on DEX users.
It should explain why a decentralized exchange would be built on NSSA
and what advantages exist for migrating an existing DEX to NSSA.
The analysis should consider both private and public DEX scenarios.
By the end of this task, we should have a clear understanding
of how Nescience compares to other projects from a user perspective.

### Deliverables
* [A notion doc](https://www.notion.so/DEX-on-NSSA-25a8f96fb65c807496c0c0aadd16d56e) to the Nescience notion workspace that summarizes existing projects
from a user perspective, notes their roadmap progress, and compares each to NSSA.

### Regulatory Positioning
* fully qualified name: `vac:acz:nes:2025q3-nescience-consulting:regulatory-positioning`
* owner: Marvin
* status: deprecated
* start-date: 
* end-date: 

### Description

Prepare an internal reference document that outlines
how Nescience aligns with general regulatory expectations.
The document should synthesize core protocol principles
with relevant considerations and include a brief rationale
for how NSSA avoids classification under certain regulatory categories.

### Deliverables
* A notion doc to the Nescience notion workspace.


### Nomos Deep Dive
* fully qualified name: `vac:acz:nes:2025q3-nescience-consulting:nomos-deep-dive`
* owner: Marvin
* status: done
* start-date: 2025/07/31
* end-date: 2025/08/08

### Description
Nescience’s architecture is designed to function as a L1 and as a L2. Nomos’ infrastructure is designed to allow a network in blockchains to exist in a single ecosystem sharing the same storage (and in some instances, the same consensus). Nomos supports application-specific blockchains in two ways: zones and sovereign rollups. In this task, we deep dive into Nomos’ infrastructure to determine the best fit and potential changes for NSSA’s deployment in Nomos.

### Deliverables: 
[A document ](https://www.notion.so/Nescience-in-Nomos-2488f96fb65c801c8d10ef6d6f3d87ed)that:
* provides an overview of Nomos infrastructure
* provides an overview of Zone and sovereign rollup requirements
* Conclusion on the best fit for NSSA in Nomos

### Specs compatibility
* fully qualified name: `vac:acz:nes:2025q3-nescience-consulting:specs-compat`
* owner: Marvin
* status: done
* start-date:
* end-date:
 
### Description
Nescience's architecture has been specified for NSSAv.01 and portions implemented within Q3. This task, ACZ will examine the compatibility
of the specifications and implementation. Additionally, will audit the specifications and implementations for any potential vulnerabilities. 

### Deliverables: 
[A document](https://www.notion.so/NSSAv0-1-compatibility-and-security-2658f96fb65c80fb997fcb60be80d19a) that:
* provides a brief security analysis of specifications
* notes on any differences between code and specifications
* examination of theoretical attack models against specifications
* examination of attacks against code implementation
