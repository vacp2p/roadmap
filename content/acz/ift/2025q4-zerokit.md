---
title: Zerokit
tags:
  - "2025q4"
  - "acz"
  - "ift"
draft: false
description: "Maintaining and improving Zerokit, including the release of version v1.0.0,
which supports BE and improved FFI, lastly researching new ZK proof techniques"

---

`vac:acz:ift:2025q4-zerokit`
## Description

This commitment entails developing and maintaining Zerokit
including Zerokit v1 release by advancing the next version, such as
big-endian support, research on faster proving methods,
lastly improved FFI feature and new ZK proofs research. 

### Background

[Zerokit](https://github.com/vacp2p/zerokit) is a collection of Zero Knowledge modules
that focus on RLN, developed in Rust, is intended for integration with various system programming environments.

In 2025q3, we released Zerokit v0.9.0, which supports improved CI, optimized, partially BE support and research on FFI improvements. 

### Narratives

By utilizing the zerokit commitment, we will reinforce the Conduit of Expertise narrative by:
* Delivers an optimized version for IFT projects utilizing Zerokit, 
including [nwaku](https://github.com/waku-org/nwaku)and [js-rln](https://github.com/waku-org/js-rln)
and [Status L2](https://docs.status.network/).

We will also strengthen the Premier Research Destination narrative by:
* Offers a Rust crate that serves as a more efficient open-source development tool for users looking to integrate RLN into their projects. 
* Verifying the existing ZK framework by integrating zerokit. 

## Task List

### Zerokit maintaining

* fully qualified name: `vac:acz:ift:2025q4-zerokit:zerokit-maintaining`
* owner: Ekaterina
* status: in progress (%30)
* start-date: 2025/10/01
* end-date: 2025/12/30

#### Description
This task encompasses all maintenance updates for Zerokit, including CI updates and the creation of future issues.

#### Deliverables
A set of PRs and issues to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/). 

### FFI re-work

* fully qualified name: `vac:acz:ift:2025q4-zerokit:ffi-rework`
* owner: Vinh
* status: in progress (80%)
* start-date: 2025/10/01
* end-date: 2025/11/01

#### Description
The due date of this task is expanded to 11/01 due to the bugs and test requirements.

This task entails reworking Zerokit’s FFI (Foreign Function Interface) to support passing data in Big Endian format,
and to transition from a manual byte-based serialization approach to a safer and more maintainable opaque-struct model.
Currently, FFI functions require developers to manually allocate buffers, serialize arguments,
and handle deserialization within Rust, which introduces overhead, performance loss, fragile data handling
and complex documentation requirements.
Additionally, maintaining separate implementations for different endianness formats
and managing numerous byte-to-struct conversions adds unnecessary complexity.

The proposed solution is to adopt an opaque struct pattern managed by Rust,
allowing C code to manipulate only pointers through a defined API, leveraging the safer_ffi crate
to automatically generate C headers, ensure memory safety, and remove unsafe code, 
as in planned in [this zerokit/discussion](https://github.com/vacp2p/zerokit/discussions/336).

This change aims to simplify the FFI layer, improve performance, reduce maintenance effort,
and make the system more resilient to data format changes while easing integration with languages like C and Nim.

This task is complete when a proof of concept demonstrating RLN proof generation
and verification through the new FFI model is implemented and validated
for memory safety and Big Endian compatibility.

#### Deliverables
A set of PRs and issues to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/). 

### Release v1

* fully qualified name: `vac:acz:ift:2025q4-zerokit:release`
* owner: Ekaterina
* status: not started 
* start-date: 2025/12/15
* end-date: 2025/12/30

#### Description
The new version of the Zerokit v1.0.0.

#### Deliverables
A set of PRs to vacp2p/zerokit repository with [tag v1.0.0](https://github.com/vacp2p/zerokit/releases/tag/v1.0.0)