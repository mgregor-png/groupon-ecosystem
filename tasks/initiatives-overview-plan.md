# Coupons Initiatives Overview - Plan

## Context

From Rebecca 1:1 (Apr 14): Adam wants ALL initiatives listed with mandates and estimated revenue impact. Rebecca agreed to create the "top layer" herself, with Martin providing numbers. This document supports her and also serves as Adam's requested view.

**Key framing from Rebecca:**
- "We need to go back up a layer and explain how the initiatives split"
- "This is where we need to explain how the initiatives split"
- Two distinct problems: (1) low app retention, (2) not fully leveraging existing traffic

**Relationship to Safari report:**
- Safari report = standalone deep-dive (DONE, v5 on GitHub Pages)
- This = the umbrella that shows all initiatives side by side
- Rebecca: "Keep [Safari] as its own piece, and then this is the top layer"

---

## Proposed Structure

### 1. The Two Problems

Frame upfront that coupons can address two distinct challenges:

**Problem A: App retention** (Groupon app has 5% DAU/MAU, 66% buy once)
- Safari extension solves this by creating off-platform presence
- This is the big strategic bet

**Problem B: Underleveraged traffic** (29.6M sessions, declining 17% YoY)
- We have significant web traffic generating $12.6M but it's declining
- Multiple initiatives to extract more value from what we have

### 2. Initiative Map

For each initiative: What it is | What problem it solves | Effort | Revenue estimate | Status | Dependencies

#### Category 1: Monetize Existing Traffic More (Problem B)
**What:** Add revenue-generating elements to existing coupons pages
- Promote Groupon deals on coupons pages
- Display advertising on non-monetized sessions
- Cross-promote app deals to web visitors

**Data:** 29.6M sessions/yr. CTR 50.1%. Non-monetized sessions = opportunity.
**Effort:** Low engineering (banner placement, feed integration)
**Revenue:** TBD - Rebecca said she has some basic numbers
**Status:** Some already in place (deal promotion exists), room to expand

#### Category 2: Drive Registrations from Existing Web Traffic (Problem B)
**What:** Gate rewards behind Groupon registration on coupons pages
- A/B test on non-monetized pages
- Convert anonymous visitors to registered users

**Data:**
- 540K registrations/yr currently
- $3.83 value per registration ($31.88 LTV at 12% conversion)
- +1,247% sign-up uplift from rewards gating (tested)
- Revenue potential: $2.1-4.6M/yr (at 2x-3x current rate)

**Effort:** Low-medium (A/B test, registration flow changes)
**Status:** Planned
**Dependencies:** None - can execute independently

#### Category 3: Increase Impressions - Existing App Base (Problem A)
**What:** Safari extension bundled inside the Groupon app
- Captures users off-platform while shopping in Safari
- Bridges back to app via Groupon Bucks

**Data:**
- 8-10M MAU, 84% iPhone (confirmed Tableau)
- $4-25M revenue potential
- Full analysis: [link to Safari report]

**Effort:** High (2-week spike to validate, then 12-week build)
**Status:** Proposal stage - needs iOS spike approval
**Dependencies:** 2-week iOS engineering spike

#### Category 4: Increase Impressions - New Base (Problem B)
**What:** Genie desktop Chrome extension + rewards integration
- Desktop companion to Safari (covers the 39% desktop traffic)
- Proves unit economics for Safari model

**Data:**
- 981 installs currently, $6/user/yr (CJ actuals)
- With rewards: projected 8-18K installs/month
- With Bucks cross-sell: $9.81/user/yr
- Revenue potential: Scale-dependent

**Effort:** Medium (34 MD eng + 4 MD design for rewards integration)
**Status:** Planned (Q2 rewards integration)
**Dependencies:** Engineering capacity

#### Category 5: Create More Content - Cashback (Supports A + B)
**What:** Cashback infrastructure on top of Groupon Bucks
- Creates offers on popular merchants without relying on merchant-issued codes
- Content lever that enhances both extension and web

**Data:** Harder to size independently - enables other initiatives
**Effort:** Medium-high (Bucks infrastructure + merchant integrations)
**Status:** Scoping
**Dependencies:** Groupon Bucks platform

### 3. Comparison Table

| Initiative | Problem | Effort | Revenue Est | Timeline | Eng Dependency |
|---|---|---|---|---|---|
| Monetize traffic | B | Low | TBD | Weeks | Minimal |
| Registrations | B | Low-Med | $2.1-4.6M/yr | Weeks | Minimal |
| Safari extension | A | High | $4-25M/yr | 14 weeks | iOS spike |
| Genie + rewards | B | Medium | Scale-dep | Q2 | 34 MD |
| Cashback infra | A+B | Med-High | Enables others | TBD | Bucks platform |

### 4. Recommended Sequencing

Phase 1 (Now): Monetize traffic + Registrations (low effort, immediate value)
Phase 2 (Q2): Genie rewards + Safari spike (medium effort, validates model)
Phase 3 (Q3): Safari build + Cashback (high effort, big payoff)

### 5. The Ask

- For Adam: This is the full initiative map with effort/revenue
- The Safari extension is the strategic bet (separate deep-dive available)
- Registration and traffic monetization are quick wins we can start now

---

## What Rebecca Needs from Martin

- [ ] Numbers for "monetize existing traffic" - how many non-monetized sessions? What's the CPM/CPC potential?
- [ ] Confirm registration numbers are still current (540K, $3.83)
- [ ] Genie LTV model numbers (already have these)
- [ ] Safari report link on GitHub Pages
- [ ] Any other data she requests

## Format

HTML single-page, similar style to Safari report but lighter:
- No prototype needed
- Simple table/cards for the initiative comparison
- Link out to Safari report for the deep-dive
- Focus on the comparison view Adam wants

## Execution

Rebecca said she'd do the first draft. Martin provides numbers and reviews.
If Rebecca needs help building it, use the same HTML template as the Safari report.
