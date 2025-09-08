---

title: RLN Status L2
tags:

- "2025q3"
- "acz"
- "ift"
draft: false
description: "Testing deployed RLN for the Status L2 architecture, including prover, verifier, deny list and RPC node"

---

`vac:acz:ift:2025q3-rln-status-l2`

## Description

This commitment entails testing and fine-tuning deployed RLN components 
for the gasless feature of the Status L2 architecture. 
Specifically, testing that all RLN components, such as prover, verifier, deny list, 
and RPC node, work fine with the Linea codebase securely and efficiently.

### Background

Status L2 is a rollup with Linea and builds a platform with the capacity 
to support SocialFi and GameFi apps, governance experiments, the Status voting system, 
and more, all while aiming to keep transaction costs low and throughput high. 
Status L2 will incorporate a gasless feature, necessitating an effective anti-spam mechanism. 
Rate-Limiting Nullifier (RLN) is a potential solution that could be deployed on 
Status L2 to prevent spam and support the gasless functionality.

In 2025q2, we released the RLN components such as prover, verifier, deny list, and RPC node.

### Narratives

By utilizing this commitment, we will reinforce the Conduit of Expertise narrative by:

- Continue sharing the RLN knowledge with the Status L2 team.
- Testing modified RLN design to make sure all components work seaminglessly.

We will also strengthen the Premier Research Destination narrative by:

- Offering a RLN use-case to the ecosystem that can be used for other gasless roll-up projects.

## Task List

### Maintain RLN Specification

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:rln-spec-maintain`
* owner: Ugur
* status: started (70%)
* start-date: 2025/07/01
* end-date: 2025/08/28

### Description

This task focuses on maintainin a specification of RLN deployment to the Status L2 network, 
based in the feedbacks and changes during testnet.

### Deliverables

* A Notion doc document that has implementation details. 

### Smart Contract Testing

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:sc-testing`
* owner: Sylvain
* status: done
* start-date: 2025/07/15
* end-date: 2025/07/31

### Description

This task focuses on testing the interaction between the prover and the smart contract developed by the SC team. Code
has been written (for both team) but never tested together.

### Deliverables

* A set of PRs and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).
    * [Test and fix smart contract interaction PR#24](https://github.com/vacp2p/status-rln-prover/pull/24)
    * [Update for new KarmaTiers smart contract PR#23](https://github.com/vacp2p/status-rln-prover/pull/23)

### Profiling

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:profiling`
* owner: Sylvain
* status: done
* start-date: 2025/07/15
* end-date: 2025/08/15

### Description

This task focuses on profiling and finding bottlenecks (memory allocations & cpu usage) for the prover module 
so that the module can be more performant.

### Deliverables

* A set of PRs and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).
    * [Add throughput measurement for prover benchmark PR#22 ](https://github.com/vacp2p/status-rln-prover/pull/22)
    * [Split unit tests PR#21](https://github.com/vacp2p/status-rln-prover/pull/21)

### Tracking and Monitoring 

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:track-and-monitor`
* owner: Sylvain
* status: done
* start-date: 2025/07/15
* end-date: 2025/08/15

### Description

Set up monitoring for the prover module using Prometheus to observe real-time performance metrics and identify 
potential overload conditions or bottlenecks. Also better tracing (using opentelemetry otlp protocol) should be done
and tested (using for example: Jaeger) in order to ensure that everything is correctly logged.

### Deliverables

* A set of PRs and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).
    * [Add histogram PR#20](https://github.com/vacp2p/status-rln-prover/pull/20)
    * [Initial code for tracing + oltp PR#19](https://github.com/vacp2p/status-rln-prover/pull/19)
    * [Initial Prometheus PR#18](https://github.com/vacp2p/status-rln-prover/pull/18)

### Researching decentralized architecture

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:research-decentralized`
* owner: Ugur
* status: started (50%)
* start-date: 2025/08/15
* end-date: 2025/09/25

### Description

This task focuses on researching more decentralized and applicable solutions to the Status L2 network, 
by minimize the prover and RLN centralization. 

### Deliverables

* A Notion doc document that has implementation details.

### E2E Prover module testing 

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:e2e-prover-testing`
* owner: Sylvain
* status: done
* start-date: 2025/07/01
* end-date: 2025/07/15

### Description

This task focuses on testing prover module with its edge cases before the testnet. 
The findings and feedbacks will be reflected to the RLN specification.

### Deliverables

* A set of PR to the [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover)
    * [PR#12 Tier Limit test](https://github.com/vacp2p/status-rln-prover/pull/12)
    * [PR#13 Unit tests](https://github.com/vacp2p/status-rln-prover/pull/13)
    * [PR#15 e2e gRPC test](https://github.com/vacp2p/status-rln-prover/pull/15)
    * [PR#17 More unit test](https://github.com/vacp2p/status-rln-prover/pull/17) 

### Stress test for prover module

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:stress-test`
* owner: Sylvain
* status: done
* start-date: 2025/08/18
* end-date: 2025/09/01

### Description

This task focuses on testing the prover module to measure maximum TPS (transactions per second)
by using dedicated machines. 

### Deliverables

* [A PR](https://github.com/vacp2p/status-rln-prover/pull/35) to the [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover)
* [A benchmark doc](https://www.notion.so/Prover-Benchmarks-25d8f96fb65c80a1bef2e317338f528b#25d8f96fb65c8078a6d4f6afde295b8c)

### Devnet testing 

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:devnet-testing`
* owner: Sylvain
* status: on-hold (5%)
* start-date: 2025/07/15
* end-date: 2025/09/15

### Description

This task is on-hold since devnet is not deployed yet.

This task focuses on testing internal devnet. 
The findings and feedbacks will be reflected to the RLN specification.

### Deliverables

* A Notion doc document that has implementation details.

### Prover Module maintaining

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:maintaining`
* owner: Sylvain
* status: started (50%)
* start-date: 2025/07/07
* end-date: 2025/09/25

#### Description
This task encompasses all maintenance updates for prover module, 
including CI updates and the creation of future issues.

#### Deliverables
A set of PRs and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).
    * [Extend testcase timeout to prevent panic, seperate anvil feature for testcase PR#28](https://github.com/vacp2p/status-rln-prover/pull/28)
    * [Add CI workflow, resolve clippy warning PR#29](https://github.com/vacp2p/status-rln-prover/pull/29)
    * [Use exact latest zerokit version, PR#30](https://github.com/vacp2p/status-rln-prover/pull/30)