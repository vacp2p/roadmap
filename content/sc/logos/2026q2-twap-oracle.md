---
title: TWAP Oracle
tags:
  - "2026q2"
  - "sc"
  - "logos"
draft: false
description: Design and implement TWAP oracle support for Logos LEZ programs.
---

`ift-ts:sc:logos:2026q2-twap-oracle`

## Description

Research, design, and implement TWAP oracle support for LEZ programs, including
price-account design, tick recording, current-tick calculation, and follow-up
design alternatives for sampling price ticks over time.

## Task List

### TWAP oracle

* fully qualified name: `ift-ts:sc:logos:2026q2-twap-oracle`
* owner: r4bbit
* status: in progress (90%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

Track TWAP oracle research and implementation work for LEZ programs, including
oracle price design, PublishPrice, RecordTick, and current-tick refactors.

#### Deliverables
- [logos-blockchain/lez-programs#195](https://github.com/logos-blockchain/lez-programs/pull/195) test(twap): cover CreateOraclePriceAccount and PublishPrice end-to-end
- [logos-blockchain/lez-programs#196](https://github.com/logos-blockchain/lez-programs/pull/196) feat(amm): create TWAP oracle price account on behalf of the pool
- [logos-blockchain/lez-programs#193](https://github.com/logos-blockchain/lez-programs/pull/193) test(twap): cover RecordTick end-to-end and add zkVM cycle benchmark
- [logos-blockchain/lez-programs#137](https://github.com/logos-blockchain/lez-programs/pull/137) feat(twap-oracle): implement PublishPrice with real tick-to-price conversion
- [TWAP Oracle account design research](https://notes.status.im/4PlwprLaQEWW4Q_SDT36zw)
- [logos-blockchain/lez-programs#138](https://github.com/logos-blockchain/lez-programs/issues/138) Alternative cascading solution for sampling price ticks over time
- [logos-blockchain/lez-programs#143](https://github.com/logos-blockchain/lez-programs/pull/143) fix(twap_oracle): validate clock account
- [logos-blockchain/lez-programs#128](https://github.com/logos-blockchain/lez-programs/pull/128) feat(twap-oracle): implement create_price_feed instruction
- [logos-blockchain/lez-programs#130](https://github.com/logos-blockchain/lez-programs/pull/130) feat(twap-oracle): implement CreateOraclePriceAccount instruction
- [logos-blockchain/lez-programs#131](https://github.com/logos-blockchain/lez-programs/pull/131) feat(twap-oracle): implement CreateCurrentTickAccount and UpdateCurre…
- [logos-blockchain/lez-programs#136](https://github.com/logos-blockchain/lez-programs/pull/136) feat(twap-oracle): implement RecordTick instruction
- [logos-blockchain/lez-programs#145](https://github.com/logos-blockchain/lez-programs/pull/145) fix(idl): update idl
- [logos-blockchain/lez-programs#147](https://github.com/logos-blockchain/lez-programs/pull/147) feat(amm): add Initialize instruction with config-gated chained calls
- [logos-blockchain/lez-programs#148](https://github.com/logos-blockchain/lez-programs/pull/148) feat(amm): create TWAP price observations on behalf of the pool
- [logos-blockchain/lez-programs#149](https://github.com/logos-blockchain/lez-programs/pull/149) feat(amm): bootstrap pool TWAP current-tick account at pool creation
- [logos-blockchain/lez-programs#150](https://github.com/logos-blockchain/lez-programs/pull/150) feat(amm): refresh TWAP current tick on add/remove liquidity
- [logos-blockchain/lez-programs#151](https://github.com/logos-blockchain/lez-programs/pull/151) feat(amm): add admin authority and UpdateConfig instruction
