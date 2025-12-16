---
title: Keycard Website
tags:
  - "2025q4"
  - "web"
  - "keycard"
draft: false
description: "Development of comprehensive website content and documentation for Keycard and Keycard Shell products to educate users and developers about hardware wallet security and integration capabilities."
---

`vac:web:keycard:2025q4-keycard-website`

## Description

This commitment involves developing comprehensive website content and documentation for both Keycard and Keycard Shell products to educate users and developers about hardware wallet security, integration capabilities, and usage. The content will serve as the primary educational resource for understanding these innovative hardware wallet solutions.

The Keycard website's content will support IFT's strategic objectives by:
- **User Education**: Providing clear, accessible information about Keycard's security features and benefits
- **Developer Onboarding**: Creating comprehensive documentation for developers to integrate Keycard into their applications
- **Product Showcase**: Highlighting the unique features of both Keycard and the new Keycard Shell product
- **Security Awareness**: Educating users about best practices in hardware wallet security and usage

**Key Product Features to Highlight:**
- **Keycard**: Lightweight, card-shaped hardware wallet with EAL6+ certified secure element, non-extractable keys, and seamless Status integration
- **Keycard Shell**: Air-gapped, stateless device supporting infinite Keycard backups with QR code transaction signing
- **Security Features**: Common Criteria EAL6+ certification, counterfeit protection, and fully open-source design
- **Integration Support**: Works with Status, MetaMask, Rabby, imToken, Bitget, UniSat, Sparrow, Specter, and Nunchuk
- **Use Cases**: Vault storage, backup solutions, memecoin trading, and custom branded cards

**Educational Content Areas:**
- **Internationalization (i18n)**: Multi-language support for global user accessibility
- **Help Documentation**: Comprehensive help system covering setup, usage, and troubleshooting
- **Start Guide**: Step-by-step onboarding process for new users and developers
- **Integration Guides**: Developer documentation for wallet and dApp integration
- **Security Best Practices**: Educational content about hardware wallet security and key management

## Task List

### i18n

* fully qualified name: `vac:web:keycard:2025q4-keycard-website:i18n`
* owner: felicio 
* status: done
* start-date: 2025/10/01
* end-date: 2025/11/04

#### Description
Localize the Keycard site and docs so core pages ship in the priority languages for launch.

#### Deliverables
- [Update footer with i18n support](https://github.com/keycard-tech/keycard-website/pull/123)
- [Wallets page localisation](https://github.com/keycard-tech/keycard-website/pull/116)

### Help

* fully qualified name: `vac:web:keycard:2025q4-keycard-website:help`
* owner: jkbktl
* status: in progress (40%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Author the help center covering setup, troubleshooting, and FAQs for both Keycard and Shell devices.

#### Deliverables
- [Deploy articles in the documentation](https://github.com/keycard-tech/keycard-website/pull/132)
- [PR 116: wallets page layout and filtering](https://github.com/keycard-tech/keycard-website/pull/116).
- [Make repository public](https://github.com/keycard-tech/keycard-website/issues/130)

### Start Guide

* fully qualified name: `vac:web:keycard:2025q4-keycard-website:start-guide`
* owner: jkbktl
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Create a step-by-step getting started guide that walks new users through secure activation and first use.

#### Deliverables
- PRs/Issues/Docs/Reports

### Maintenance

* fully qualified name: `vac:web:keycard:2025q4-keycard-website:maintenance`
* owner: Jakub
* status: in progress (60%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Handle routine upkeep, security fixes, and content updates for the Keycard site.

#### Deliverables
- [keycard-tech/keycard-website#153](https://github.com/keycard-tech/keycard-website/pull/153) upgrade Next.js for critical patches
