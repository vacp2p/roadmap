---

title: GossipSub Performance Improvements
tags:
  - "2025q1"
  - "p2p"
  - "ift"
draft: false
description: GossipSub Performance Improvements

---

`vac:p2p:ift:2025q1-gossipsub-perf-improvements`

## Description

This commitment focuses on improving the GossipSub protocol, as well as evaluating our improvements developed in previous reporting periods.
It comprises investigating, implementing, and testing various enhancements to optimize performance, scalability, and efficiency, while also comparing our approach to GossipSub 2.0 for potential future integration. This commitment includes finalizing the specification and getting it approved by the community for the message preamble and IAMRECEIVING message, which we introduced as improvements in the last reporting period. Actionable Description:

By the end of this quarter, we will:

*  Implement and test GossipSub enhancements in an Ethereum testnet
*  Complete a comparative analysis of our approach vs GossipSub 2.0
*  Test our improvements with Quic as a transport
*  Finalize and get community approval for the message preamble and IAMRECEIVING message specifications; including the combination of both approaches
*  Finalize the inclusion of our improvements in the official GossipSub protocol specifications

## Task List

(splitting into concrete tasks TBD)

* Investigate and implement the combination of staggering and IAMRECEIVING
  - Develop a Proof of Concept (PoC)
  - Experiment with protocol components to assess and optimize performance
  - Compare our approach with GossipSub 2.0
  - Investigate potential integration with GossipSub 2.0
  - evaluate QUIC transport vs TCP transport
* Evaluate in Ethereum testnet environment (Sepolia)
  - Design and execute comprehensive tests to evaluate real-world performance
  - Document test results and gather feedback for potential improvements
  - Compare testnet results with our simulation data
* Conduct libp2p implementation comparison:
  - Set up test environments for nim-libp2p, go-libp2p, rust-libp2p, and js-libp2p
  - Implement test nodes and add support for the shadow simulator across all implementations
  - Develop hooks to collect performance metrics and statistics
  - Analyze and compare the performance of all implementations
  - Compile findings into a comprehensive research blog post or technical report
* Finalize and integrate specifications:
  - Complete the specification for message preamble and IAMRECEIVING message
  - Present the specification to the community for review and approval
  - Actively engage with the commuity, drive the effort, and incorporate feedback and make necessary revisions
  - get the our parts included in the official GossipSub protocol specification

### TBD

* fully qualified name: `vac:p2p:ift:2025q1-gossipsub-perf-improvements`
* owner: farooq
* status: 10%
* start-date: 2025/01/13
* end-date: 2025/01/31

#### Description

#### Deliverables
