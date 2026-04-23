# Save Everywhere - Master Context for Final Output

Last updated: April 9, 2026
Purpose: Single source of truth for iterating on the MBR recommendation output

---

## The Core Message

"Coupons content provides a mechanism for Groupon to be part of our customers' shopping experience across thousands of brands and millions of checkouts. By delivering coupons content through a Safari extension within the Groupon app, we can extend Groupon's reach to deliver value for our customers across all their shopping experiences."

"This captures users off-platform and through Groupon Bucks brings them back into the Groupon app."

---

## Rebecca's Structure (Apr 9 - this is THE structure to follow)

1. The Premise (coupons as mechanism for being in every checkout)
2. How It Works (5 points - see below)
3. The Numbers
4. Unknowns
5. Why We Need All Three (extension + cashback/Bucks + coupons in app)
6. Then: The Coupons Space (organic decline, registration, Genie rewards)

---

## How It Works (Rebecca's 5 points)

1. "A Safari extension is added to the Groupon app. When a user downloads the app and enables the extension, Groupon will pop up when they shop at leading retailers on their phone."

2. "Coupons content is strengthened by cashback offers which upsell into Groupon Bucks - leading the user back to Groupon."

3. "Rather than the Genie extension which only works on desktop, this works on mobile - where our customers shop!"

4. "As an extension of the app, acquisition is supercharged using the existing app base."

5. "Integrating data from users' off-Groupon shopping experience into their Groupon profile enhances opportunity for personalisation."

---

## Why We Need All Three (Rebecca's framing)

"Rather than a standalone extension with just coupons content, we believe the real value of this feature would be based on the extension + cashback/Bucks + coupons account/app integration."

**Safari Extension = Reach**
- Distribution channel. Every Groupon app install becomes a Safari extension.
- Works on mobile (61% of traffic) where Genie can't reach.

**Cashback / Groupon Bucks = Value Creation**
- "The cashback element gives us a way of creating valuable content for the user without being reliant on codes issued by merchants."
- "Most importantly, cashback also opens the doorway to an upsell into Groupon Bucks."
- Bucks pull users back into the app to spend on local deals.

**Coupons in the App = Personalisation**
- "Coupons integration into the account opens the way for more personalisation and messaging - allow customers to follow their favourite brands for alerts when coupons/cashback offers are available."

---

## The User Flow (linear - NOT a flywheel)

User shops on Nike.com in Safari -> Groupon extension popup appears -> shows codes + cashback -> user applies code, earns Bucks -> push notification about Bucks balance -> user opens Groupon app -> sees Bucks balance + local deals -> books a deal using Bucks -> earns more Bucks

This is off-platform CAPTURE leading to in-app ENGAGEMENT.

---

## Key Feedback from Meetings (Apr 9)

### Product Catch-up (James, Rebecca, Mark)
- Safari extension confirmed as primary MBR solution
- Rebecca: quickly pivot to the solution, more visuals, position Safari as hero
- Registration and Genie rewards can be owned internally - Safari needs core team support
- Need mockups and customer perspectives
- Main incentive for conversion is rewards
- Need to validate if app submission process changes due to extension
- Need monthly app install/update rates from BI for Safari calculation
- Need a dedicated coupons content section in the app

### Rebecca 1:1
- "Proceed with building and measuring without waiting for explicit 100% sign-off"
- "Stack up projects, start cashback, Genie rewards, push hard"
- "Present to Dusan for advice not approval"
- Lead with "big idea front and center" + supporting efforts underneath
- Core message: driving more users to the core Groupon mobile app
- Safari solves reach + leverages existing content + is on critical mobile platform
- Need 5-sec visual demo (popup with cashback on Nike)
- "The main contribution the coupons team can make is extending the app into big-brand, day-to-day shopping"
- If presentation doesn't address everything Adam wants, Rebecca will intervene
- Compensation: 3.3% increase, 20% bonus

---

## BQ-Verified Data (source: prj-grp-coupons-prod-8892.rep.01_management_dashboard)

### US Coupons Traffic
| Period | Sessions | Clicks | Commission | CTR | RPS |
|--------|----------|--------|------------|-----|-----|
| 2024 | 35,764,927 | 18,721,697 | $14,680,358 | 52.3% | $0.41 |
| 2025 | 29,623,110 | 14,828,450 | $12,583,967 | 50.1% | $0.43 |
| 2026 Q1 | 5,884,965 | 2,190,195 | $2,212,548 | 37.2% | $0.38 |

Key: declining 17% YoY. Q1 2026 annualizes to ~$8.8M.

### Device Split (BQ, Apr 1)
- 61% mobile - unreachable by Chrome extension
- 39% desktop - Genie's addressable market
- Mobile popup CTR 1.80% vs desktop 0.81% (2.2x) - highest intent on mobile

### App Data (Tableau, Mar 25-Apr 7, MBNXT + Legacy combined)
- Daily active users: ~500K UDV
- 14-day unique users: ~7.2M
- Monthly unique users: ~8-10M (estimated)
- DAU/MAU: ~5%
- Visit frequency: 1.2x per 14 days
- Conversion: 5% (Orders/UDV)
- Revenue per visit: $3.72 (NOB/UDV)
- Daily app revenue: $1.9M (NOB)
- MBNXT share: 98.9% (legacy negligible)

### Registration Data (Behdad/BI)
- 540K annual registrations from coupons (Rebecca's ROI model)
- Registration rate: ~1.8% (45K/mo / 2.5M sessions)
- Registrant to purchaser (12mo): 12% (13.04% exact, 17M+ sample)
- 1Y LTV per converted registrant: $31.88 (discount cohort)
- Value per registration: $3.83
- Rewards gating test: +1,247% sign-up uplift (Rebecca's ROI model, NA)

### Genie Data (CJ actuals + MBR March 2026)
- 981 installs (as of Wk12, Mar 16)
- 388 transactions, $2,622 commission (23 weeks)
- $6.00/user/yr commission (actual)
- LP to install CVR: ~14% at scale
- Popup CTR: 1.45% (best promotional asset)
- GA4 active users: 205 (up from ~115)
- Current installs/month: ~304
- Rewards integration: 30 MD eng + 4 MD design (Q2)
- Projected with rewards: 8-18K installs/month (26-59x current)
- With Bucks + deals cross-sell: $9.81/user/yr (LTV model)

### Genie Rewards (Feb actuals)
- Transactions: 4,907
- Claim rate: 11%
- Clicks: 14,433
- Commission: $42,381
- Redeemed value: $10,110

---

## Revenue Potential

### Safari Extension (Primary)
- Addressable: 8-10M app MAU, ~55% iOS (EST - need from Radomir)
- Activation: 10-30% (TO TEST - Honey gets ~30%)
- Per user: $9.81/yr ($6 commission + $3.81 Bucks/deals)
- Revenue: $4.4-16.2M/yr
- Investment: 2-week iOS spike to validate, then MVP build

### Registration + Genie (Without Safari)
- Registration: $2.1-4.6M/yr ($3.83/reg, double rate to 3%)
- Genie + Rewards: scale dependent (8-18K installs/mo at $6-9.81/user)
- Combined: $4-7M/yr
- This is the fallback if Safari doesn't validate

### Combined
- $8-25M/yr for ~40 MD engineering total
- 33%+ uplift on current $12.6M base

---

## Competitor Data (from competitor-ecosystem-research-2026-04.md)

| Player | Users | Key Fact |
|--------|-------|----------|
| Honey (PayPal) | 13M (down from 20M) | Class action lawsuit, 33% code success rate. IN CRISIS. |
| Rakuten | 17M US members | $3.7B cashback paid. Quarterly payout = retention. |
| Capital One Shopping | 10M+ | #2 free Safari app. 4.9 stars. Bundled in banking app. |
| RetailMeNot | 18M visits/mo | Same model as us. 18% revenue decline. Added cashback. |
| Slickdeals | 12M MAU | 40% DAU/MAU from community. |
| Coupert | 8M | 73% code success (vs Honey 33%). Growing from Honey crisis. |
| Fetch | 12.5M | 34% DAU/MAU. $500M ARR. Receipt scanning habit. |

Key: Honey crisis = market window. All major players have Safari extensions. RetailMeNot declining = pure affiliate is dying.

---

## Unknowns / Open Items

- iOS App Store: can we bundle Safari extension inside the app? (2-week spike validates)
- Extension activation rate: 10-30% range, Honey gets ~30%
- iOS share of app users: estimated ~55%, need confirmed from Radomir
- Monthly app install/update rates: need from BI for activation modeling
- App Store submission process changes: does the extension require separate review?
- Gift card economics: $5 gift card exceeds $3.83 LTV per registration (need lower value or non-redemption rate assumption)

---

## Assets Built

| Asset | URL | Status |
|-------|-----|--------|
| Interactive Prototype (7 screens) | save-everywhere-prototype.html | Done, on GitHub Pages |
| Auto-playing Video Walkthrough (10 screens) | safari-extension-video.html | Done, on GitHub Pages |
| Competitor Research (7 players) | competitor-research-2026-04-08.html | Done, on GitHub Pages |
| Full Data Analysis (v1) | ecosystem-recommendation-2026-04-08.html | Done, on GitHub Pages |
| v2 Deck (dual problem) | ecosystem-recommendation-v2.html | Done, superseded |
| Becky's Version | ecosystem-recommendation-becky.html | Done, structure adopted |
| Final Premium | ecosystem-recommendation-final.html | Done, superseded |
| Save Everywhere v3 | save-everywhere-v3.html | Done, superseded |
| Save Everywhere Final | save-everywhere-final.html | Current working version |
| Genie LTV Model | genie-ltv-model.html | Done, on GitHub Pages |
| Screen Descriptions for AI UI Tool | In this conversation | Done |

---

## Engagement Hooks (Part B from original deck - KEEP these)

### A1: Follow Stores + Code Alerts (Low effort - RECOMMENDED)
Let users follow 10-20 favourite online retailers. Push when new code appears. "Nike just dropped a 25% off code." Every alert-driven app open exposes user to local deals.

### A2: Weekly Best Codes Digest (Low effort - RECOMMENDED)
Monday push: "This week's top codes: 30% off ASOS, 25% Nike, 20% Uber Eats + 3 more." Predictable cadence = habit. Flipp's playbook (weekly flyers, 10M+ downloads).

### A3: Code Expiry Countdown (Low effort)
"Your 30% off ASOS code expires tonight." Urgency + loss aversion. Nearly impossible to ignore. Just a notification trigger + UI treatment.

### A4: Web-to-App Bridge (Low-Med effort)
On groupon.com/coupons pages: "Save this code to the Groupon app" deep-link. Turn web visits into app installs.

### A5: Smart Code Recommendations (Medium effort)
Personalised codes based on shopping history. "Based on your shopping: Nike 20% off, Adidas 15%, Under Armour BOGO."

### A6: Affiliate Cashback via Extension (Medium effort)
Cashback on affiliate purchases via the extension. Earn Bucks without needing a promo code. Not reliant on merchant-issued codes.

---

## What's Next (ownership split)

**Already executing (no approval needed):**
- Genie rewards integration (34 MD eng + 4 MD design)
- Registration A/B test on non-monetized coupons pages
- Cashback scoping - building on Groupon Bucks infrastructure

**What we need from core team:**
- 2-week iOS engineering spike - validate Safari extension feasibility
- Alignment with Viktor's GROUPON LIFE personalization team

"We're presenting for direction - not asking approval on every sub-project. The one decision point is the iOS spike."

---

## Viktor's GROUPON LIFE (complementary, not competing)

Viktor focuses on IN-APP: personalization, feed, retention for 322K L4 high-affinity users.
We focus on OFF-PLATFORM: capture users when they're not in the app, bring them back via Bucks.

Viktor's key data (from his Gamma presentation):
- $166M marketing spend -> +15% new users -> +1% revenue growth
- 66% buy once and stop (7.3M users)
- Value ladder: $18 -> $36 -> $53 -> $70 -> $121
- 62% never click a deal, 53% gone in 10 seconds
- Search CVR 6.1% vs browse 1.38% (4.4x gap)
- 5.5x deep link conversion lift
- 88.5% have dominant L4 category
- 8 segments totaling $256M

NOTE: Viktor's data is about core app users, NOT coupons visitors. Don't mix them.

"Viktor fixes the bucket. We fill it with more water."

---

## Asana References

- Main task: https://app.asana.com/1/8437193015852/task/1213745471998935
- Jon's Safari test: https://app.asana.com/1/8437193015852/task/1213861645172479 (completed)
- New Platform bet: https://app.asana.com/1/8437193015852/task/1213786827282607

---

## Meeting Transcripts (saved in full)

- Product Catch-up Apr 9: projects/new platform/meetings/2026-04-09-product-catchup.md
- Rebecca 1:1 Apr 9: projects/groupon-ecosystem/meetings/2026-04-09-rebecca-1to1.md
- Product Catch-up Apr 7 (5 meetings): projects/new platform/meetings/2026-04-07-*.md

---

## Design Spec

Full spec at: docs/superpowers/specs/2026-04-09-save-everywhere-final-design.md

---

## Key Decisions Made

1. Original Save Everywhere brainstorm deck is the strongest foundation - enhance, don't rebuild
2. Strip Part A (core app ideas 1-10) - not our focus
3. Keep Part B (affiliate hooks A1-A6) - these are ours
4. No flywheel - the flow is LINEAR: Nike -> popup -> Bucks -> app -> deal
5. Safari is the hero, everything else supports it
6. Becky's structure is THE structure to follow
7. Data matters but customer perspective comes first
8. "Present for advice not approval"
9. Board framed around coupons content as mechanism, not internal metrics
10. Gross bet numbers exclude delivery discounts - 42% factor handles risk
11. US data only (rebased from global after BQ validation)
12. Light theme only, no toggles
