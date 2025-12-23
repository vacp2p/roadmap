---
title: Status Wallet Extension
tags:
  - "2025q4"
  - "web"
  - "status"
draft: false
description: "Development of a browser wallet extension focused on trading and investor utility, featuring multi-chain swaps, portfolio management, and real-time token tracking with cost-optimized proxy services."
---

`vac:web:status:2025q4-status-wallet-extension`

## Description

This commitment involves developing a browser wallet extension that serves as a trading wallet and token price tracker for casual and meme coin traders and investors. The extension will be independent from the Status App project, focusing on revenue generation through trading activities while providing comprehensive portfolio management across multiple connected wallets.

The Status Wallet Extension will support Status' strategic objectives by:
- **Revenue Generation**: Creating a sustainable revenue stream through swap fees, bridge transactions, and wallet subscriptions
- **Market Expansion**: Reaching new user segments including casual traders and crypto enthusiasts (57.4M combined target audience)
- **Ecosystem Integration**: Leveraging existing services and providers to accelerate development and reduce costs
- **User Acquisition**: Attracting traders and investors through superior multi-chain trading capabilities

**Key Product Features:**
- **Multi-Chain Trading**: Extensive support for cross-chain swaps and bridge transactions
- **Portfolio Management**: Unified view of assets across connected hardware and software wallets
- **Real-Time Token Tracking**: Live token lists, price updates, and market data integration
- **Trading Center**: Token price lists, news, DEX screeners, favorites, and price alerts
- **Wallet Connection Hub**: Support for Ledger, Trezor, MetaMask, Trust Wallet, and Coinbase Wallet
- **Cost-Optimized Proxies**: Price and token proxy services to reduce external API costs

**Technical Implementation:**
- **Price Proxy**: Cost-effective price data aggregation and caching system
- **Token Proxy**: Token metadata and information management with reduced external dependencies
- **Status Proxy Extension**: Building upon existing Status Proxy infrastructure for enhanced data and usage
- **Integration-First Approach**: Leveraging existing services rather than building from scratch

**Target Audience:**
- **Meme-Driven Financial Revolutionaries**: Casual traders focused on meme coins and community-driven tokens
- **Crypto Enthusiasts**: Active investors seeking comprehensive trading tools and portfolio management

**Revenue Model:**
- Single and cross-chain swap transaction fees
- Bridge transaction fees
- Fiat-to-crypto onramp fees
- Premium wallet subscription services
- Future social features and community monetization

## Task List

### Price proxy

* fully qualified name: `vac:web:status:2025q4-status-wallet-extension:price-proxy`
* owner: jinhojang6
* status: done
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Stand up a price proxy service that aggregates token pricing data and exposes cached feeds to the extension.

#### Deliverables
- [Add Suspense and optimize token detail page loading](https://github.com/status-im/status-web/pull/869)
- [Implement proxies and production env vars](https://github.com/status-im/status-web/pull/860)
- [Improve tag width calculation for better chart label](https://github.com/status-im/status-web/pull/868)


### Token proxy

* fully qualified name: `vac:web:status:2025q4-status-wallet-extension:token-proxy`
* owner: jinhojang6
* status: done
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Build the token metadata proxy that supplies token lists, icons, and market data without relying on paid APIs.

#### Deliverables
- [Plan token proxy integration](https://github.com/status-im/status-web/issues/848)
