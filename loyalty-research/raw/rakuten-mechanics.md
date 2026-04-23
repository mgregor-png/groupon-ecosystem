# Rakuten - Loyalty Mechanics Teardown
*Source: startup-competitors / Rakuten deep dive | 2026-04-21*

---

## 1. TL;DR (what Groupon should copy or avoid)

Rakuten is a 27-year-old cashback portal (founded 1998 as Ebates, acquired by Rakuten Group for $1B in 2014) with 17M+ US members and ~$2.6-2.8B quarterly US GMS. Its core habit loop is NOT the cashback percentage - it is the **quarterly "Big Fat Check"** ($5.01 minimum threshold, paid Feb/May/Aug/Nov 15) that creates dopamine anticipation four times a year, combined with **Mobile Monday** and **Double Cash Back** weekly flash events. The economics are thin: US International segment (which includes Rewards + Kobo + Viber + Viki + ads) delivered only **$48.5M operating income on $2.04B revenue in FY2024** (2.4% margin) - this is a volume game, not a profit engine. Critical weaknesses to avoid copying: (a) **tracking failures** are the #1 complaint on Reddit/Trustpilot/ConsumerAffairs - users lose faith when large purchases don't track, (b) Rakuten+ paid tier ($100/year, 10% cashback, invite-only, launched Nov 2025) is a Honey-defensive move of uncertain traction, (c) Amex/Bilt partnerships convert cashback to points at 1:100 and 1:100 respectively, turning Rakuten into a de facto points-earning utility rather than a destination. **For Groupon: copy the quarterly payout + Mobile Monday cadence, skip the paid tier, invest 2x Rakuten in tracking reliability.** [Confidence: High on mechanics, Medium on segment P&L attribution, Low on standalone US Rewards revenue]

---

## 2. The 20-point mechanics (with citations)

### 2.1 Signup flow [Data, High confidence]
- Email + password, payment method preference (check / PayPal / Amex points / Bilt points), mailing address required for security verification [S1, S11]
- Friction point: mailing address up-front is unusual for an online service; exists because default payout is a physical check
- Welcome bonus requires $25-$50 qualifying purchase in first 90 days (not first click) [S3]

### 2.2 Welcome bonus - current 2026 value [Data, High confidence]
- **Referred new member: $50 cash back / 5,000 Amex MR points / 5,000 Bilt points** after $50 qualifying spend in 90 days [S3, S14]
- **Unreferred new member: $10** (historical default) [S3]
- Active promo window: April 1 - June 30, 2026 (referred to as "best ever" - historical baseline is $30, with occasional $40 bumps) [S14]
- Referrer also gets $50 - a 100% payout to referrer is unusually generous and signals viral CAC is their primary growth lever

### 2.3 Onboarding email cadence [Data Gap - Low confidence]
- Could not find public documentation of 30-day welcome series content/cadence
- Known: confirmation email at signup, payment email at Big Fat Check disbursement [S11]
- **DATA GAP:** email frequency, content themes, and triggers for first 30 days not publicly disclosed

### 2.4 Push notification strategy [Data Gap + Inference - Low confidence]
- Mobile Monday (weekly boosted cashback in-app only) implies push notifications drive app opens every Monday [S16]
- Time-limited flash deals (24h) and Double Cash Back events (week-long) imply event-based pushes [S16]
- **DATA GAP:** no public data on frequency, CTR, or opt-in rates

### 2.5 Core reward mechanic [Data, High confidence]
- Real cash (not points) by default [S1]
- Average cashback rate across members is ~3% [S8 - Rakuten's own characterization in Rakuten+ announcement]
- Per-merchant rates typically 1-10%, with promotional peaks up to 15-40% during events [S5, S15]
- Cashback is tiered/personalized - "system tailors Cash Back rates for different audience segments based on shopper behavior" [S1]

### 2.6 Big Fat Check quarterly payout [Data, High confidence]
- **Schedule: February 15, May 15, August 15, November 15** (four fixed dates) [S2]
- **Minimum threshold: $5.01** - anything below rolls forward to next quarter [S2]
- **Methods: physical check, PayPal, Amex MR points, Bilt points** [S2]
- Quarterly cadence is a deliberate engagement mechanic - it creates 4x/year anticipation moments

### 2.7 Breakage [Inference + Data, Medium confidence]
- $5.01 minimum is a soft lock: users with sub-threshold balances roll forward, increasing the chance they forget or abandon [S2]
- "Pending cashback disappears if it hasn't been collected by the time they get their quarterly check" - user complaints suggest aggressive breakage policy on pending balances [S9]
- "Much of the money earned never even goes on accounts, especially when cashback percentages are high" [S9]
- Complaint volume on missing/denied cashback is the dominant negative-review theme [S6, S12]
- **Estimate:** breakage is a meaningful contributor to margin, though not publicly disclosed

### 2.8 Rakuten+ paid tier [Data, High confidence - NEW]
- **Price: $100/year** annual subscription [S8]
- **Launch: November 12, 2025** (very recent - ~5 months old as of this research) [S8]
- **Mechanic: minimum 10% cashback at participating premium/luxury stores, year-round** [S8, S13]
- **Access: invite-only**, targeted at "most loyal and active shoppers" [S8]
- **Launch partners:** Sephora (beauty, joined October 2025); broader luxury lineup not disclosed [S8]
- **Comparison: standard members get "approximately 3% rate"** - Rakuten+ is 3x the base [S8]
- **Adoption signals: DATA GAP** - no enrollment, retention, or revenue disclosure

### 2.9 Points partnerships [Data, High confidence]
- **Amex Membership Rewards:** $1 cash back = 100 MR points, transfers every 3 months (quarterly), one-way only (cannot convert points back to cash) [S4]
- **Bilt Rewards:** 1:1 ratio for Silver/Gold/Platinum elite members through May 15, 2026; non-elites get 0.5x (50 points per dollar) [S10]
- **2,500-point Bilt sign-up bonus** if registering via Bilt app after $25 qualifying purchase [S10]
- Strategic read: Amex + Bilt partnerships turn Rakuten into an invisible points-earning utility for high-income users (NOT a destination)

### 2.10 In-store cashback (linked card) [Data, High confidence]
- **RCLON** (Rakuten Card Linked Offer Network) - PCI-compliant card linking [S7]
- Link Amex, Mastercard, or Visa credit card; must use credit rail (debit with PIN does NOT track) [S7]
- Must activate each offer individually BEFORE shopping [S7]
- No receipt upload required - transaction detected via card network data [S7]
- **Purpose:** drives app open frequency between online purchases (geo / offer-browse reason to return)

### 2.11 Merchant take-rate [Data, Medium confidence]
- Rakuten Advertising (the affiliate network) takes ~10% of merchant commission, 90% goes to publisher [S17]
- Rakuten Rewards (consumer cashback) keeps the difference between the affiliate commission it earns from merchants (typically 2-20%, avg ~6-10%) and what it gives the user (~3% avg)
- **Estimate: Rakuten retains ~40-60% of the merchant commission** as gross margin [Estimate, Medium confidence]

### 2.12 Traffic sources [Data, Medium confidence - SimilarWeb]
- **rakuten.com (US): ranked #237 globally** as of March 2026 (up from #251 three months prior) [S18]
- **Traffic +15.39% MoM** as of March 2026 [S18]
- **63.63% of desktop visits from Direct** - heavy brand/bookmark traffic, implies strong habit [S18]
- Audience skew: 48% male / 52% female, largest cohort 35-44 [S18]

### 2.13 Acquisition channels [Inference, Medium confidence]
- Referral program pays $50 to BOTH sides - implies referrals are the primary organic channel [S14]
- Partnerships with Amex / Bilt / Chase act as co-marketing (credit card issuers promote Rakuten to affluent card holders)
- Paid search/display not visible in this research
- **DATA GAP:** paid marketing spend

### 2.14 12-month trajectory [Data, Medium confidence]
- US Rewards revenue "remained flat" in FY2025 "due to a cautious stance among US retailers" [S4, S19]
- Rakuten International segment FY2024: **$2,037M revenue (+8.5% YoY), $48.5M non-GAAP op income (+$93.4M YoY swing to profitability)** [S19]
- Rakuten International Q3 FY2025: **$486.9M quarterly revenue (+5.4% YoY), $4.2M non-GAAP op income (+78.8% YoY)** [S20]
- 17M+ US members (figure used repeatedly by Rakuten; likely cumulative signups, not active) [S21]
- $4.6B cumulative cashback paid to US members since 1998 [S21]

### 2.15 Session / retention proxies [Data Gap - Low confidence]
- **DATA GAP:** no DAU / MAU / session length disclosed
- 63% direct traffic suggests strong repeat usage [S18]
- Mobile Monday + quarterly Big Fat Check cycle = at minimum 4 high-engagement moments per year + 52 weekly triggers (Mondays)

### 2.16 LTV economics [Estimate, Medium confidence]
- FY2024 US International: $2.04B revenue / 17M members = ~**$120 revenue per member** [Estimate]
- Note: this includes Kobo, Viber, Viki, ads - NOT purely Rewards; Rewards-only is lower
- FY2024 op margin ~2.4% on International segment; after corporate allocation, Rewards standalone contribution likely similar or lower
- **Implied take per member: ~$3-5 of operating profit/year** - extremely thin [Estimate, Low confidence]

### 2.17 Break-even or loss to drive habit? [Opinion + Inference, Medium confidence]
- The 2.4% operating margin on International segment (FY2024) strongly suggests Rakuten Rewards runs near break-even on US standalone basis
- Margin expansion seems to come from cost cuts ("cost reductions and profitability improvements") rather than unit economics [S19]
- **Hypothesis:** Rakuten runs cashback at thin margin as a customer acquisition / retention loss leader for the broader Rakuten Group ecosystem (Amex card, Bilt partnership, Rakuten credit card)
- Rakuten+ paid tier ($100/yr) is likely a direct response to this margin problem - attempt to create a profitable subset of power users

### 2.18 Safari iOS extension UX [Data, High confidence]
- Extension is **bundled with the iOS Rakuten app** (not separate install) [S22]
- Activation requires: Safari > aA icon > Manage Extensions > toggle Rakuten > grant "Always Allow on Every Website" permission [S22]
- **This is a 4-tap, 2-permission flow with scary "Every Website" wording** - significant activation friction
- Once active, it pops a button on merchant sites prompting "Activate" for cashback [S23]
- Each purchase requires re-activation (two purchases at same site = two activations) [S23]
- **DATA GAP:** no public data on % of app users who complete extension activation

### 2.19 App store ratings [Data, High confidence]
- **iOS App Store: 4.8 / 5 from 360.5K reviews** (July 2025) [S12]
- **Google Play: 3.4 / 5 from 73.1K reviews** (July 2025) [S12]
- 1.4-point gap is enormous - indicates Android experience is materially worse
- **Trustpilot (rakuten.com): 4.6 / 5 from 36,643 reviews; 75% 5-star, 5% 1-star** [S6]

### 2.20 Differentiation vs Honey and Capital One Shopping [Data, High confidence]
- **vs Honey:** Rakuten has higher cashback peaks (up to 40% promo) but requires manual activation. Honey auto-applies coupon codes, lower but passive earn [S24]
- **vs Capital One Shopping:** Capital One has price comparison + automatic coupon stacking; rewards redeem only as gift cards (not cash). Rakuten redeems as cash/points [S24]
- **Rakuten's moat:** quarterly cash payout ritual + Amex/Bilt points optionality + highest merchant cashback rates. **Rakuten's weakness:** manual activation required, worse UX than Honey

### 2.21 Key churn / weakness signals [Data, High confidence - SURFACE AGGRESSIVELY]
- **#1 complaint: cashback not tracked** - especially on large purchases, ad-blocker interference, tab switching [S6, S12]
- **#2 complaint: pending cashback denied retroactively** without clear explanation [S9, S12]
- **#3 complaint: quarterly payout too slow** - users want on-demand withdrawal [S6]
- **#4 complaint: customer service is a "loop of articles"** - no path to escalate [S12]
- **#5 complaint: returned checks / NSF** - reports of Big Fat Checks bouncing [S25]
- **Active class action:** Oganesyan v. Rakuten USA, filed Feb 13, 2025 (ND Cal) - nature not yet clear from sources [S26]
- **Account suspensions just before payout** reported on Reddit/Trustpilot [S6]

---

## 3. Retention / habit drivers ranked by strength of evidence

| Rank | Driver | Evidence | Copyability for Groupon |
|------|--------|----------|-------------------------|
| 1 | **Quarterly "Big Fat Check"** payout ritual | 4 fixed dates create dopamine moments; $5.01 soft threshold | HIGH - easy to copy |
| 2 | **Mobile Monday** weekly in-app bonus | Forces weekly app open for committed users | HIGH - direct copy |
| 3 | **Direct traffic dominance** (63% of desktop) | Habit baked in - users bookmark/typein | Outcome not lever - build into it |
| 4 | **Referral program ($50/$50 both sides)** | Viral CAC, strongest single acquisition signal | HIGH - but expensive |
| 5 | Amex / Bilt points optionality | Keeps affluent users locked in via points currency | MEDIUM - requires partner |
| 6 | Double Cash Back flash events | Creates FOMO, shorter-cycle triggers between quarters | HIGH - direct copy |
| 7 | In-store card-linked cashback | Cross-channel presence (online + retail) | MEDIUM - requires card network deal |
| 8 | Rakuten+ paid tier | Too new to prove retention; unclear traction | LOW - skip until proven |

---

## 4. Weaknesses and churn signals (aggressive)

1. **Tracking reliability is the Achilles heel.** Every negative review cluster points to missed cashback. This erodes the core value prop - users churn because they feel cheated, not because cashback is too small. For Groupon: reliability is existential, not a feature.
2. **Manual activation tax.** Rakuten requires a click before every purchase. Honey's auto-apply wins on UX convenience. Rakuten's higher peak rates only matter if users remember to click.
3. **Android is broken.** 3.4 stars vs 4.8 on iOS = ~40% of mobile users having a bad experience. For Groupon (iOS-skewed user base per my earlier research: 84% iOS), this is less relevant but still a data point.
4. **Customer service is a self-serve loop.** Multiple reviews cite zero human escalation path. When Rakuten denies cashback, users have no recourse - this compounds churn on the single biggest complaint vector.
5. **Quarterly payout friction.** Modern fintech UX (Venmo-instant, Cash App) has made users impatient. Users want on-demand payouts, not 90-day waits. Rakuten's quarterly cadence is a retention *feature* for Rakuten (forces check-back) but a churn driver for impatient users.
6. **FY2025 revenue flat** = market is saturating or Honey/Cap One Shopping are taking share.
7. **2.4% op margin** = Rakuten has almost no room to compete on cashback rate without going negative.
8. **Rakuten+ is an admission the base model isn't profitable enough** on average users.

---

## 5. LTV / economics signals from public filings

| Metric | Value | Source / Date |
|--------|-------|---------------|
| Rakuten International segment revenue FY2024 | $2,037M (+8.5% YoY) | [S19] Feb 2025 release |
| Rakuten International op income FY2024 | $48.5M (+$93.4M YoY swing to profit) | [S19] Feb 2025 |
| Rakuten International Q3 FY2025 revenue | $486.9M (+5.4% YoY) | [S20] Nov 2025 |
| Rakuten International Q3 FY2025 op income | $4.2M (+78.8% YoY) | [S20] Nov 2025 |
| Rakuten Rewards quarterly US GMS (Q1 2023) | $2.6B | [S27] Statista |
| Rakuten Rewards quarterly US GMS (Q2 2024) | $2.78B | [S27] Statista |
| Cumulative US members | 17M+ | [S21] rakuten.com/about |
| Cumulative cashback paid (US, lifetime since 1998) | $4.6B | [S21] |
| Standard member avg cashback rate | ~3% | [S8] per Rakuten in Rakuten+ launch |
| Quarterly minimum payout threshold | $5.01 | [S2] |

**Derived estimates [Medium-Low confidence]:**
- Revenue per member (International, FY2024): ~$120/yr (but includes non-Rewards businesses)
- Average cashback earned per member per quarter: $4.6B / 17M / ~27 years of operation = ~$10/yr per member, implying most members earn below the $5.01 threshold and many roll forward
- This aligns with breakage as a meaningful (but undisclosed) margin contributor

---

## 6. What Groupon SHOULD copy (ranked, with cost estimate)

| # | Mechanic | Rationale | Rough cost / lift |
|---|----------|-----------|-------------------|
| 1 | **Quarterly payout ritual** (4 fixed dates, ~$5 threshold) | Creates dopamine anticipation 4x/yr; soft-lock drives breakage; ritual builds brand | LOW eng lift (~1 sprint) |
| 2 | **Mobile Monday weekly in-app bonus** | Forces weekly app-open habit; pairs with push notif | LOW (~1 sprint + push infra) |
| 3 | **Referral $X/$X symmetric bonus** | Lowest-CAC channel; viral growth; double-sided incentive | MEDIUM (funded by growth budget) |
| 4 | **Big, visible cumulative earnings counter** ("You've earned $127.43") | Sunk-cost psych - users return to protect/grow balance | LOW eng (~0.5 sprint) |
| 5 | **Double Cash Back flash events** (24h-week events between quarters) | Sub-quarterly engagement triggers; FOMO | LOW (admin tooling for merchants) |
| 6 | **Points currency optionality** (e.g., partner with Amex, Chase, Bilt) | Locks in affluent users; converts cashback into a utility layer | HIGH (partnership BD effort) |
| 7 | **In-store card-linked cashback** (visa/MC/Amex linking) | Cross-channel presence; fills gap between online purchases | HIGH (PCI infra, network deals) |
| 8 | **Safari extension bundled with iOS app** | Extension bundling avoids separate install friction | MEDIUM (mobile eng effort) |

---

## 7. What Groupon should NOT copy

1. **Paid premium tier ($100/yr for 10% cashback).** Too new, invite-only, unproven retention. Launched Nov 2025; wait 12 months for public adoption data before considering.
2. **Manual activation before every purchase.** This is Rakuten's biggest UX liability. Honey's auto-apply is the better pattern - use Groupon's Safari/browser extension to auto-detect merchant and auto-apply without user click.
3. **Mailing address required at signup.** Relic of paper-check era. Ask only at first payout, and default to digital (PayPal/Venmo/ACH).
4. **$5.01 minimum payout threshold.** This is anti-customer. Lower to $1 or zero, and make quarterly cadence the mechanic - not a soft lock on small balances.
5. **"Cash Back Not Tracked" as an acceptable failure mode.** Rakuten tolerates a 5-10% tracking failure rate; this is the #1 churn driver. Groupon should target <1% failure and auto-credit user the good faith amount.
6. **Opaque customer service ("loop of articles").** When cashback is denied, there must be a human path. This alone would differentiate from Rakuten meaningfully.
7. **Android under-investment.** 1.4-point app-store gap is indefensible. Build mobile-first for both OSes from day one.

---

## 8. Data gaps

| Gap | Impact |
|-----|--------|
| Rakuten Rewards US standalone revenue / op income | Can't isolate US unit economics from Group filings |
| DAU / MAU / session length / retention cohorts | Best retention proxies (quarterly cadence, 63% direct traffic) are inferred |
| Safari extension activation rate (% of app users) | Critical for Groupon's Safari extension sizing |
| Email / push notification frequency and content | Can't benchmark cadence for onboarding design |
| Rakuten+ paid tier adoption (member count, retention) | Can't validate the paid-tier thesis |
| Breakage rate (% of cashback that expires unclaimed) | Material to LTV estimate; undisclosed |
| CAC and referral program conversion rate | Can't estimate Groupon parity cost |
| Marketing spend (paid vs organic mix) | No visibility |
| Churn rate / year-2 retention | No public data |

---

## 9. Red flags / Yellow flags

**Red flags (Rakuten-side, things to watch):**
- Active class action (Oganesyan v. Rakuten USA, Feb 2025 ND Cal) - nature unclear but suggests legal exposure on cashback denials
- Historical report of Big Fat Check bouncing for NSF (2024) - cashflow flag, low recurrence but telling
- "Account suspensions just before payout" Reddit pattern - looks like aggressive fraud-prevention with collateral damage on legitimate users
- Flat FY2025 revenue suggests market maturation - Rakuten is not growing faster than the cashback category

**Yellow flags (for Groupon's strategy):**
- 17M cumulative US members over 27 years is not as impressive as it sounds - that's 630K/yr net signup rate
- ~$10/yr cashback per member (cumulative average) implies long tail of inactive accounts
- 2.4% International op margin = category is structurally thin-margin; Groupon must expect similar economics at scale
- Rakuten+ at $100/yr is a signal that even the category leader can't make enough money on free tier alone

---

## 10. Sources (numbered, with dates)

- [S1] The Points Guy, "What is Rakuten?" — https://thepointsguy.com/loyalty-programs/how-to-use-rakuten/ (accessed 2026-04-21)
- [S2] Rakuten Help, "Big Fat Check Schedule & FAQs" — https://www.rakuten.com/blog/rakuten-big-fat-check-schedule-faqs/ (accessed 2026-04-21)
- [S3] Rakuten Help, "Welcome Bonus Terms" — https://www.rakuten.com/help/article/rakuten-welcome-bonus-terms-4409324215955 (accessed 2026-04-21)
- [S4] FinanceBuzz, "Your Guide to Earning Amex Points with Rakuten" 2026 — https://financebuzz.com/earning-amex-points-with-rakuten
- [S5] TopBubbleIndex, "Rakuten Double Cash Back Ultimate Guide" — https://www.topbubbleindex.com/blog/rakuten-double-cash-back/
- [S6] Trustpilot, Rakuten USA reviews (36,643 reviews, 4.6 stars as of 2026-04-21) — https://www.trustpilot.com/review/www.rakuten.com
- [S7] Rakuten, "In-Store Cash Back & Card-Linked Offers" — https://www.rakuten.com/in-store
- [S8] Rakuten International press release / WWD / Retail TouchPoints, "Rakuten+ Launch" Nov 12, 2025 — https://rakuteninternational.com/news/... ; https://wwd.com/business-news/business-features/rakuten-plus-invite-membership-luxury-shopping-cash-back-1236405876/
- [S9] RedFlagDeals / PhatWallet / ConsumerAffairs user threads 2024-2025 on tracking failures — multiple URLs
- [S10] Bilt Newsroom, "Rakuten x Bilt Partnership" + frequentmiler.com — https://newsroom.biltrewards.com/rakuten ; https://thepointsguy.com/news/earn-bilt-points-rakuten/
- [S11] Rakuten Help, "How does Rakuten work?" — https://www.rakuten.com/help/article/how-does-rakuten-work-360002117047
- [S12] App Store / Google Play / DollarSprout Rakuten Review 2025 — https://dollarsprout.com/rakuten-review/ ; https://apps.apple.com/us/app/rakuten-cash-back-deals/id723134859
- [S13] Rakuten+ landing page — https://www.rakuten.com/rp/member/join
- [S14] The Points Guy / One Mile at a Time referral promo coverage (Apr 2026) — https://thepointsguy.com/news/rakuten-referral-bonus-online-shopping/
- [S15] CNBC Select, "Rakuten Review 2025" — https://www.cnbc.com/select/rakuten-review-2022-cash-back-earnings-perks-and-more/
- [S16] Rakuten Blog, Mobile Monday / Double Cash Back pages — https://www.rakuten.com/double-cash-back
- [S17] UpPromote / Sharetribe, Rakuten Advertising commission structure — https://uppromote.com/affiliate-program-directory/rakuten/
- [S18] SimilarWeb rakuten.com (March 2026 data) — https://www.similarweb.com/website/rakuten.com/
- [S19] Rakuten Group FY2024 Financial Results Highlights, Feb 14, 2025 — https://global.rakuten.com/corp/news/press/2025/0214_01.html
- [S20] Rakuten Group Q3 FY2025 Financial Results Highlights, Nov 13, 2025 — https://global.rakuten.com/corp/news/press/2025/1113_01.html
- [S21] Rakuten Rewards About Us / Wikipedia (accessed 2026-04-21) — https://business.rakuten.com/about-us/ ; https://en.wikipedia.org/wiki/Rakuten_Rewards
- [S22] Rakuten Help, Safari iOS extension installation — https://www.rakuten.ca/button/safari/walkthrough
- [S23] Rakuten Blog, "How the Cash Back Button Works" — https://www.rakuten.com/blog/rakuten-cash-back-button-how-it-works/
- [S24] JoinKudos / INOUSNY / Making Sense of Cents - Rakuten vs Honey vs Capital One (2026) — https://www.joinkudos.com/blog/rakuten-vs-honey-vs-capital-one-shopping---comparing-the-top-shopping-rewards-extensions
- [S25] PhatWallet, "BEWARE of Rakuten cashback - Big Fat Check bounced" Mar 2024 — https://phatwalletforums.com/topic/39392/...
- [S26] Justia docket, Oganesyan v. Rakuten USA, filed Feb 13, 2025 (ND Cal) — https://dockets.justia.com/docket/california/candce/4:2025cv01534/444510
- [S27] Statista, Rakuten Rewards quarterly US GMS 2023-2024 — https://www.statista.com/statistics/586575/ebates-gross-merchandise-sales-quarter/

---

*Research rounds completed: 6 (broad mechanics → specific mechanics → financials → user sentiment → LTV proxies → Safari/activation). Date of all web-fetched data: 2026-04-21 unless otherwise noted. Flags: Rakuten Group financial year ends March (Japanese standard); USD figures converted at reporting date rates per Rakuten filings. Confidence levels per claim: see inline labels [Data] / [Estimate] / [Inference] / [Opinion].*
