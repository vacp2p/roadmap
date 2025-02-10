---
title: MDS Checker
tags:
  - "2025q1"
  - "acz"
  - "ift"
draft: false
description: "Creating the rust crate for MDS matrix security checker and a blogpost"

---

`vac:acz:ift:2025q1-mds-checker`

Creating the rust crate for MDS matrix security checker and a blogpost
## Description

This commitment entails releasing a Rust crate that verifies the security of any MDS matrix, 
along with a blog post that explains the underlying mathematics behind the crate.

### Background

[MDS matrices](https://en.wikipedia.org/wiki/MDS_matrix) are used in symmetric cryptography, 
such as hash functions and encryption schemes, to provide security against cryptanalysis. 
The security of MDS matrices can be verified using various methods. For example, 
the security of the Poseidon hash MDS matrix can be checked by
using this [algorithm](https://extgit.isec.tugraz.at/krypto/hadeshash/-/blob/master/code/generate_params_poseidon.sage). 
We propose a generic Rust crate that can verify the security of any matrix in any field. 
This crate can be used for in-code parameter checks or for custom hash functions operating in custom fields 
by the ecosystem.

### Narratives

By utilizing the MDS Checker commitment, we will reinforce the Conduit of Expertise narrative by:
* Delivers a Rust crate that we can use for security checks of MDS matrices 
in possible custom cryptographic primitives in the IFT projects.

We will also strengthen the Premier Research Destination narrative by:
* Offers a public Rust crate that is the first generic MDS matrix security checker in Rust, 
that any party can use on their projects
* Contribute to the ecosystem with the blog post that explains the mathematics behind the Rust crate.  

## Task List
 
### Releasing Rust Crate

* fully qualified name: `vac:acz:ift:2025q1-mds-checker:releasing-rust-crate`
* owner: Aleksei
* status: started (80%) 
* start-date: 2025/01/01
* end-date: 2025/02/12

#### Description

Releasing a Rust crate that checks the security of arbitrary MDS matrix with a new method 
based on the [report](https://notes.status.im/CVMoa6EcTmS2D4VPBCsH2w#). 
This crate will be open source and can be used by any project that requires generating in-code round parameters 
with an MDS matrix and checking the matrix security efficiently.

#### Deliverables

* PR to [rust-lang/crates.io](https://github.com/rust-lang/crates.io) repo with related crate 
* [A Report](https://notes.status.im/CVMoa6EcTmS2D4VPBCsH2w#) about the MDS security checker

### Blogpost MDS

* fully qualified name: `vac:acz:ift:2025q1-mds-checker:blogpost-mds`
* owner: Aleksei
* status: not started
* start-date: 2025/02/12
* end-date: 2025/02/28

#### Description

Writing a blog post that explains the security of MDS matrices 
and reviews existing methods for assessing their security. 
The post also introduces a new, efficient method for evaluating MDS matrix security 
and provides details about a Rust crate that automates these security checks 
based on the findings presented in the article.

#### Deliverables

A blogpost to [vac.dev/rlog/](https://vac.dev/rlog/)

