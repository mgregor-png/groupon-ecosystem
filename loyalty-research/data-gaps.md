# Data Gaps - What We Still Need to Make an Investment-Grade Decision
*Consolidated from competitor research + Rebecca's April 2026 draft §5.7 | 2026-04-21*

## Purpose

Every loyalty investment decision requires internal evidence that competitive research alone cannot provide. This document lists what we still need to pull, who owns it, the approximate effort, and why it matters.

**Rule followed in the research: declare gaps, do not invent numbers.** This document is the honest list.

---

## 1. Internal data asks (no external spend, 1-5 working days each)

Consolidated from Rebecca's §5.7 + my additions. Initiate immediately.

| # | Data request | System / source | Suggested owner | Why it matters | Confidence on availability |
|---|---|---|---|---|---|
| 1 | **Coupons page visitor ↔ deal purchaser crossover** - how many already do both? | Internal BI / user database | Mark Brenda (started per Apr 20 debrief) | Quantifies the existing organic crossover. Baseline Bucks must improve on. The #1 Dusan question from the Apr 20 debrief. | High |
| 2 | **Genie user cohort analysis** - retention curve, purchase frequency, avg commission vs non-Genie users | Genie analytics / internal BI | Ernesto's team | Validates the $6/user extension LTV figure. Tests whether extension users actually buy deals. | Medium - depends on Genie instrumentation |
| 3 | **Mobile vs desktop split for coupons traffic by merchant category** | GA / internal analytics | Analytics owner | Validates the 61% mobile figure. Identifies highest-impact categories for Safari extension. | High |
| 4 | **Push opt-in rate and engagement rate for existing app users** | App analytics / push platform | Mobile PM | Benchmark for Safari extension permission-granting willingness. | High |
| 5 | **App update adoption curve** - days to 50% / 80% adoption of new version | App Store Connect / Firebase | Mobile PM | Determines Safari extension rollout speed for existing iOS users. | High |
| 6 | **Non-monetised session rate** - % of coupons sessions with zero commission / click-out | Internal BI | Analytics owner | Sizes the Layer 1 monetisation opportunity directly. | High |
| 7 | **Web rewards programme data** - redemption rate, avg reward cost, ROI by channel | Rewards platform data | Rewards team | Validates 5.33x ROI and $2.97/txn cost figures in the business case. | Medium |
| 8 | **Groupon Bucks (if any exist today)** - issuance volume, redemption rate, breakage, avg time to redemption | Finance / loyalty data | Finance + rewards | Real breakage and redemption data for the Bucks financial model. | Medium - depends on current state |
| 9 | **iOS vs Android retention curve delta for Groupon app users** | Mobile analytics | Mobile PM | We claim 84% iOS - is iOS retention also stronger? | High |
| 10 | **Coupons → Local vertical conversion rate by merchant vertical** | Internal BI | Analytics owner | Which merchant partnerships drive the most cross-vertical spend? Affects which Bucks-earning merchants to prioritise. | Medium |
| 11 | **Ernesto's team data on retention uplift per added feature / segment** | Internal experimentation platform | Ernesto | The $40M+ retention frame needs Ernesto's model to validate. | Medium - may require new analysis |

---

## 2. External gaps I could not close with public research

These require primary research (interviews, surveys, mystery shop) or commercial data (SimilarWeb Pro, Semrush, SensorTower, data.ai).

### Competitor-specific gaps

| # | Question | Affected mechanic | Path to fill |
|---|---|---|---|
| 12 | **Rakuten+ paid tier adoption** (members, retention, revenue) | Whether to launch a paid Groupon tier | Wait 12 months for public disclosure (launched Nov 12 2025) |
| 13 | **Rakuten Rewards US standalone P&L** | Category-economics ceiling estimate | Hidden in Rakuten Group International segment. May appear in 2027 filings. |
| 14 | **iOS Safari extension activation rate** for Honey / Rakuten / Capital One Shopping | Safari extension sizing | Not publicly disclosed. Needs SensorTower or SimilarWeb panel + educated guesses. |
| 15 | **Ibotta IPN publisher take-rate split** | B2B2C distribution strategy (2027+) | Ask former Ibotta employees or Walmart Cash partners under NDA. |
| 16 | **Honey iOS Safari user count trajectory** | Whether iOS is insulated from Chrome exodus | No tracking series exists equivalent to 9to5Google's Chrome Web Store tracking. Estimate from PayPal app install data via SensorTower. |
| 17 | ~~Starbucks DAU/MAU and visit frequency~~ | ~~Pure-loyalty benchmark~~ | **Dropped: Starbucks benchmark removed from scope - habit engine does not port. Raw research preserved in `raw/`.** |
| 18 | **Coupert audited revenue, founder identity, Honey-migration numbers** | Tier 2 competitive threat sizing | Bootstrapped private company. Limited disclosure ever. |
| 19 | **Slickdeals 2026 revenue, exact DAU, white-label precedent customers** | Partnership economics and conditions | Private. Request under NDA during BD process. |
| 20 | ~~Post-March-2026 Starbucks retention data~~ | ~~Whether aggressive devaluation actually bites~~ | **Dropped with Starbucks scope change.** |

### Category-level gaps

| # | Question | Path to fill |
|---|---|---|
| 21 | **Average iOS Safari extension activation rate across category** | Apple does not disclose. Would need a panel or primary data. |
| 22 | **Breakage rate for cashback in a 1:1 soft-currency model** | Industry range 15-30%; Groupon-specific needs a pilot cohort. |
| 23 | **Post-Honey-collapse user migration destinations** | Rakuten / Capital One Shopping / Coupert public disclosures do not explicitly attribute inflow to Honey exodus. Pattern is likely diffuse (many users going cold rather than switching). |
| 24 | **Groupon audience ↔ RetailMeNot / Rakuten / Honey / Cap One Shopping cross-visitation sizes** | Rebecca's Phase 1 research programme: SimilarWeb Pro Audience Overlap dashboard, or Semrush Audience Overlap add-on ($289/mo). |

---

## 3. Primary research asks (funded, non-trivial spend)

Per Rebecca's §4.5 research programme:

| # | Research | Duration | Cost | Priority |
|---|---|---|---|---|
| 25 | **Phase 1: Desk research (Semrush Audience Overlap + SimilarWeb audience overlap + Semrush/Ahrefs keyword gap)** | 1-2 weeks | ~$300/mo Semrush add-on or 7-day trial | Start immediately |
| 26 | **Phase 2: Quantitative user survey of 1,000-2,000 Groupon coupons visitors** (including Bucks vs cash vs gift card conjoint) | 3-4 weeks | $15-25K | Q2 |
| 27 | **Phase 3: Behavioural analysis of existing Groupon data** (coupons-to-deals crossover, Genie install-to-purchase, Bloomreach cohort test) | 2-3 weeks | Internal | Q2 - overlaps with items 1-8 above |
| 28 | **Phase 4: Qualitative depth interviews with 15-20 heavy cashback users** | 4-6 weeks | $10-20K | Q2-Q3 |
| 29 | **Phase 5: Live A/B testing in PoC** (activation incentives, stacking tracking, Bucks redemption funnel) | Ongoing | Part of PoC build | Q3+ |
| 30 | **My addition: mystery-shop tracking reliability** across Rakuten / Capital One Shopping / Coupert for one month | 4 weeks | $2-5K | Q2 - critical for positioning |

---

## 4. Status tracker

| # | Item | Status | Owner | Requested | Due |
|---|---|---|---|---|---|
| 1-11 | Internal data asks | Not started | TBD | TBD | Target: pull within 1 week |
| 12-24 | External gaps | Flagged in final report | n/a | n/a | Some resolve with time |
| 25-30 | Primary research | Pending prioritisation | TBD | TBD | Phase 1 can start this week |

---

## 5. Priority to request this week

Top 3 for immediate pull (highest value, lowest cost):

1. **Item 1 - Coupons ↔ deals crossover.** Chase Mark Brenda for status. This is the single most decision-critical number.
2. **Item 6 - Non-monetised session rate.** Frames Layer 1 opportunity. Internal BI query, <1 day.
3. **Item 25 - Semrush Audience Overlap (7-day trial).** No cost, confirms Rebecca's SimilarWeb affinity data with independent second source.

## 6. Principle - do not invent what we can measure

Every number in the final report is labelled [Data] / [Estimate] / [Opinion] / [Assumption]. When any of these gaps close with real data, the corresponding claim should be promoted from [Estimate] to [Data] and the confidence rating revised.

No number in the final report is load-bearing in the "we would change the decision if wrong" sense without a data source. The explicit gaps above are the known unknowns.
