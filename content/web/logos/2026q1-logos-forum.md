---
title: Logos Forum
tags:
  - "2026q1"
  - "web"
  - "logos"
draft: false
description: "Optimization of the Logos Forum experience to reduce onboarding friction, enable seamless story submission, and improve community contribution workflows."
---

`vac:web:logos:2026q1-logos-forum`

> *note*: The `<` `>` mark places where information has to be filled in. Please do not copy the `<` and `>` characters into the actual commitment documents.

## Description

This commitment involves optimizing the Logos Forum experience to address critical bottlenecks that prevent community members from contributing their stories and engaging with the community. The current forum experience creates significant friction that causes potential contributors to drop off, requiring personal relationships and handholding to successfully onboard new users.

The Logos Forum optimization will support Logos' strategic objectives by:
- **Reduced Friction**: Eliminating barriers that prevent community members from contributing stories and pitches
- **Self-Service Onboarding**: Enabling users to contribute without requiring personal handholding
- **Community Growth**: Making it easier for new members to share their ideas and build with Logos
- **Story Onboarding**: Streamlining the process for community members to submit and share their stories

**Key Problem Areas:**
- **Email Domain Restrictions**: Forum doesn't accept custom domain names in email addresses
- **Spam Filter Cooldown**: 24-hour cooldown period prevents instant posting, even for legitimate contributors
- **First Post Complexity**: New users face barriers to posting their intro - category selection, multiple buttons, and unclear posting flow
- **Content Visibility Restrictions**: Content may be hidden based on user rank, preventing engagement from visitors and new users

## Task List

### Custom Domain Email Support

* fully qualified name: `vac:web:logos:2026q1-logos-forum:custom-domain-email-support`
* owner: <github/disord name of the CC responsible for this task>
* status: <not started or in progress (0%-99%) or done>
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

- Allow registration with custom domain email addresses

### Cooldown Bypass System

* fully qualified name: `vac:web:logos:2026q1-logos-forum:cooldown-bypass-system`
* owner: <github/disord name of the CC responsible for this task>
* status: <not started or in progress (0%-99%) or done>
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

- Implement referral code on signup to bypass 24-hour cooldown period
- If referral code system not possible, implement heart system that allows users to request bypassing the cooldown
- Maintain spam protection while enabling legitimate community members to post immediately

### First Post Intro Flow

* fully qualified name: `vac:web:logos:2026q1-logos-forum:first-post-intro-flow`
* owner: <github/disord name of the CC responsible for this task>
* status: <not started or in progress (0%-99%) or done>
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

- Enable new users to post their intro immediately, no matter what
- Automatic flow that brings new users directly to a text field where they can write their intro
- Single post button, no category choice required
- Very straightforward, simplified posting experience
- Remove 24-hour comment-only restriction for intro posts

### Content Visibility

* fully qualified name: `vac:web:logos:2026q1-logos-forum:content-visibility`
* owner: <github/disord name of the CC responsible for this task>
* status: <not started or in progress (0%-99%) or done>
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

- Allow anyone, including first-time visitors who are not signed up, to see all posts and comments
- Remove content restrictions based on user rank or registration status
- Enable public viewing to encourage engagement with community member posts

> https://github.com/acid-info/logos/issues/19