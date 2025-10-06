---

title: nim-libp2p Test Coverage
tags:
  - "2025q3"
  - "p2p"
  - "vac"
draft: false
description: nim-libp2p Test Coverage

---

`vac:p2p:vac:2025q3-nimlibp2p-test-coverage`


nim-libp2p Improved Test Coverage

## Description
Work closely with the QA and DST teams to identify key areas for improvement in the release and testing of nim-libp2p,
ensuring better test coverage and reliability. 


## Task List

### Improve DST test node

* fully qualified name: `vac:p2p:vac:2025q3-test-coverage:dst-test-node`
* owner:
* status: not started
* start-date:
* end-date: 

#### Description
DST uses this [node](https://github.com/vacp2p/dst-gossipsub-test-node/blob/dockerized/main.nim) to do regression testing 
on each libp2p release. DST team has suggested that we collaborate in the refactoring of the node to allow custom test 
scenarios via specifying arguments/flags:
- Choose the multiplexer to use without having to recompile
- Number of nodes to connect to
- Message Ratio
- Message Weight
- Connection parameters (currently all nodes try to connect to other N nodes)
- External script for message injection instead of cron job

#### Deliverables



### QA Consulting over test coverage

* fully qualified name: `vac:p2p:vac:2025q3-test-coverage:qa-consulting`
* owner: vlado
* status: done
* start-date: 2025-07-01
* end-date: 2025-09-30

P2P provides consulting and support to QA by addressing queries, reviewing, formulating and designing strategies to test 
nim-libp2p more effectively, as well as offering guidance on resolving coding challenges that may arise during the 
development of the test units.

#### Deliverables









