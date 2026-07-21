---

title: Logos Core Learning Materials
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Create tutorials, examples, and toy projects for nim-libp2p through Logos Core

---

`ift-ts:p2p:ift:2026q3-logos-core-learning-materials`

Create learning material for using nim-libp2p through Logos Core, including
tutorials, practical examples, and small toy projects.

## Description

As Logos Core integration grows, downstream developers need a clear path for
learning how to use libp2p features without first understanding all nim-libp2p
internals. This commitment creates a Q3 set of tutorials and examples around
common Logos Core workflows.

The material should focus on practical usage: creating a node, configuring
transports, connecting peers, using service discovery, using Kademlia, handling
custom protocols where available, and debugging common setup problems.

## Task List

### Plan

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-core-learning-materials:plan`
* owner: Vlado
* status: in progress (10%)
* start-date: 2026/07/01
* end-date: 2026/07/05

#### Description
Define the tutorial and example set for Q3, prioritizing workflows that Logos
Delivery, Anoncomms, and Logos Core developers are expected to use.

#### Deliverables
- [logos-co/logos-web#110](https://github.com/logos-co/logos-web/issues/110) some text have really small font size
- [logos-co/logos-web#112](https://github.com/logos-co/logos-web/issues/112) Install Basecamp is throught web wrongly implemented
- [logos-co/logos-basecamp#268](https://github.com/logos-co/logos-basecamp/issues/268) bug: hide/show is not working after second click
- [logos-co/logos-basecamp#269](https://github.com/logos-co/logos-basecamp/issues/269) feat: make text selectable on Settings screen
- Tutorial outline for Q3 Logos Core libp2p material
- Decision on which examples should be executable tests


### Tutorials

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-core-learning-materials:tutorials`
* owner: Vlado
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Write step-by-step tutorials for using nim-libp2p through Logos Core. The
tutorials should be concise, runnable where practical, and aligned with the
current Logos libp2p module API.

#### Deliverables
- [logos-co/logos-docs#398](https://github.com/logos-co/logos-docs/pull/398) fix command
- [logos-co/logos-docs#397](https://github.com/logos-co/logos-docs/pull/397) add libp2p module
- Tutorial for creating and starting a libp2p node through Logos Core
- Tutorial for peer discovery and Kademlia usage
- Tutorial for connecting peers and exchanging protocol data
- Troubleshooting notes for common setup and runtime issues


### Toy Projects And Examples

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-core-learning-materials:toy-projects`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Create small toy projects or executable examples that demonstrate common
workflows end to end. Examples should be easy to run locally and should serve as
regression checks where possible.

#### Deliverables
- Minimal peer discovery example
- Minimal custom protocol or stream example, if custom protocol support is available
- Example project documentation and validation notes
