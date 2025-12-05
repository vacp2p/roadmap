---

title: nim-libp2p c-bindings  
tags:  
  - "2026q1"  
  - "p2p"  
  - "ift"  
draft: false  
description: Provide c-bindings for nim-libp2p  

---

`vac:p2p:ift:2026q1-nimlibp2p-cbindings`

Expose nim-libp2p functionality via a c static library, enabling external projects (e.g. logoscore) to integrate without depending on nim toolchains. Implementation may leverage [nim-ffi](https://github.com/waku-org/nim-ffi) and/or [nim-library-template](https://github.com/logos-co/nim-library-template/) as well as previous learnings from building libwaku to simplify binding generation and library packaging.

## Description

Deliver a minimal set of c-bindings around nim-libp2p core. The bindings should cover basic node lifecycle, peer connectivity, and stream i/o. This enables downstream projects like logoscore to embed libp2p functionality directly. Stretch goals include exposing Gossipsub and custom protocol support, which may be deferred to 2026q1.

## Task List

TODO: move tasks that were not completed in 2025Q4 here