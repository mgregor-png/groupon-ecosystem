# Retention Uplift Sizing Model - $40M+ 3-Scenario Sensitivity
*Subtask #2 | Martin kickoff, Rebecca to review + contribute | Draft v0.1 | 2026-04-22*

## Purpose
Anchor the $40M+ retention headline currently sitting in the exec summary without visible math. Build a transparent sensitivity model that shows which inputs drive the range, labels every assumption, and makes it trivial to swap in better internal data when it lands.

## The formula

```
Revenue uplift = MAU x engagement_rate x frequency_uplift x AOV x take_rate x (1 - reward_cost%)
```

Simplified for a loyalty program layered on top of existing traffic:

```
Annual incremental revenue =
    [addressable_MAU]                     (who this reaches)
  x [loyalty_adoption_rate]               (what share adopts)
  x [incremental_orders_per_year]         (what extra frequency it drives)
  x [AOV]                                 (what those orders are worth)
  x [take_rate]                           (what Groupon keeps)
  - [cashback_cost_per_user_per_year]     (what we give back in Bucks)
  x [adopted_users]
```

Clearer form:

```
Net annual uplift = (adopted_users x incremental_orders x AOV x take_rate)
                    - (adopted_users x avg_bucks_earned_per_year x (1 - breakage_rate))
```

## Input table (labelled - all [DATA GAP] items need internal pulls)

| Input | Conservative | Base | Aggressive | Source | Confidence |
|---|---|---|---|---|---|
| **addressable_MAU** (Groupon app + coupons web users, US) | [DATA GAP] | [DATA GAP] | [DATA GAP] | BQ / Tableau mobile app perf dashboard | High once pulled |
| **loyalty_adoption_rate** (% of MAU who activate Bucks / extension) | 10% | 20% | 35% | Cap One #2 Safari app + Honey bundle activation (undisclosed by both; our Estimate 10-30%) | Low - [Estimate] |
| **incremental_orders_per_year** (extra purchases vs no-loyalty baseline) | 0.4 | 1.0 | 2.0 | Industry proxies: Amazon Prime +2x tx, Starbucks Rewards +3x visits (but wrong cadence), general loyalty lit 15-25% frequency lift | [Estimate / Assumption] |
| **AOV** (avg order value, Groupon, US) | [DATA GAP] | [DATA GAP] | [DATA GAP] | BQ / Tableau | High once pulled |
| **take_rate** (Groupon net revenue % of GMV, blended) | [DATA GAP] | [DATA GAP] | [DATA GAP] | Groupon IR / 10-K segment data + internal finance | High once pulled |
| **avg_bucks_earned_per_year** (cashback paid per adopted user) | $15 | $30 | $60 | Rakuten avg $10/yr cumulative; Ibotta $256/yr; Cap One spread | [Estimate] |
| **breakage_rate** (% of Bucks issued, never redeemed) | 15% | 25% | 35% | Industry 15-30%; Starbucks $207M breakage on $1.78B stored value ~12%; compounding if gift-card-only adds 3-10% more | [Estimate] |

## Scenario math (placeholders - need internal data to compute)

### Conservative
- Adopted users = MAU x 10%
- Incremental revenue per adopted user = 0.4 orders x AOV x take_rate = $[TBD]
- Cashback cost = $15 x (1 - 0.15) = $12.75 per adopted user
- Net per user = incremental revenue - $12.75
- **Scenario total = Adopted users x Net per user**

### Base
- Adopted users = MAU x 20%
- Incremental revenue per adopted user = 1.0 orders x AOV x take_rate = $[TBD]
- Cashback cost = $30 x (1 - 0.25) = $22.50 per adopted user
- Net per user = incremental revenue - $22.50
- **Scenario total = Adopted users x Net per user**

### Aggressive
- Adopted users = MAU x 35%
- Incremental revenue per adopted user = 2.0 orders x AOV x take_rate = $[TBD]
- Cashback cost = $60 x (1 - 0.35) = $39.00 per adopted user
- Net per user = incremental revenue - $39.00
- **Scenario total = Adopted users x Net per user**

## What drives the range (sensitivity narrative)

Three inputs dominate uncertainty. Every review conversation should focus on them:

1. **loyalty_adoption_rate** - 10% vs 35% is a 3.5x swing. Most defensible anchor: Capital One Shopping ranks #2 Top Free Shopping on iOS (real discovery channel, unknown activation rate) and Honey-via-PayPal bundling distribution playbook. Groupon's 84% iOS base is the ceiling.
2. **incremental_orders_per_year** - 0.4 vs 2.0 is the biggest lever. Loyalty programs reliably produce 15-25% frequency lift in general retail; Prime and Starbucks sit far higher but are different business models. Our base of 1.0 is the canonical "one extra purchase per year per adopted user" benchmark.
3. **take_rate** - Groupon-specific. Until this internal number lands, the model cannot produce a credible point estimate. Flag to Ernesto / finance.

Four secondary inputs:

4. **addressable_MAU** - scales linearly. Base case assumes Groupon coupons + app US; a broader definition (global, all verticals) would lift all scenarios.
5. **AOV** - internal, scales linearly.
6. **avg_bucks_earned_per_year** - depends on earn rate design. If Groupon commits to 1-5% base, the upper end is $60+ per active user. Needs merchant economic modelling.
7. **breakage_rate** - shifts cashback cost up or down 20-50% of headline earned. Meaningful to margin, not to topline revenue.

## Why this is load-bearing

The exec summary in `loyalty-mechanics-final.md` opens with "The prize is not $4M in coupon commissions. It is $40M+ in retention uplift." Without a visible model, that line is a thesis statement, not a quantified claim. This document is the math Adam / Dusan can stress-test.

## What this model does NOT include (honest scope)

- **Cannibalisation.** If adopted users shift existing purchases to Bucks-earning channel but don't add incremental orders, the "incremental_orders_per_year" term is zero and the whole thing collapses. Base case of 1.0 assumes TRUE incremental, not rebadged.
- **Cross-vertical bridge.** Dusan's coupons-to-deals-buyer crossover question (subtask for Mark Brenda). If crossover is zero, the unified loyalty proposition weakens and the scenarios need a per-vertical split.
- **Churn offset.** A loyalty program can also REDUCE churn. That's not in this model; it would widen the uplift estimate. Add once we have retention-curve data from Ernesto.
- **Fixed + variable program cost.** Eng build (~10-15 sprints per our mechanic cards), ops, fraud, customer service. Not in the incremental-revenue model. Needs a separate OpEx view for an honest NPV.
- **Time ramp.** Year 1 adoption is lower than steady state. Base case represents post-ramp (Year 2+). A real NPV needs a 3-year ramp.

## Inputs to request (ordered)

Top 3 to ask Ernesto / finance / BI this week:

1. **Addressable MAU** - Groupon app + coupons web, US, current MAU
2. **AOV** - blended, Groupon US
3. **Take rate** - Groupon net revenue % of GMV, blended US

These three alone, at [Data] confidence, collapse the scenario range from a 10x spread to ~3x.

Secondary (Rebecca's funded survey + Mark Neary track):

4. **Expected loyalty_adoption_rate** - conjoint willingness from survey
5. **Incremental orders per year** - the Phase 3 behavioural analysis of Genie users (coupons-to-deals crossover) is the closest internal proxy

## Process

- **Today (Apr 22):** Martin shares this shell + input requests to Ernesto + finance + Rebecca. Rebecca reviews methodology.
- **Wed (Apr 23):** ideally Ernesto returns MAU / AOV / take_rate. Martin plugs in, produces three point estimates.
- **Thu (Apr 24):** Rebecca reviews the populated model. Both agree on how to present the range to Adam (single number or range; we recommend range with base case highlighted).
- **Fri (Apr 24 1pm CET):** model ships as an appendix to the final doc, alongside a 2-sentence "how to read this" for Adam.

## Presentation recommendation to Adam

**Don't present a single $40M number.** Present a range with the base case highlighted:

> *Conservative $X M / **Base $Y M** / Aggressive $Z M annual net revenue uplift. The single biggest lever is incremental-orders-per-year; internal data on coupons-to-deals crossover (Mark Brenda, pending) would narrow this range significantly.*

This is honest to Adam's transparency rule and surfaces the one number that would change the recommendation (crossover rate).

---

## Changelog

- v0.1 (2026-04-22) - initial shell, all internal inputs as [DATA GAP], all external inputs as [Estimate] with sources.
- *v0.2 (pending Ernesto / finance data pull)*
- *v0.3 (pending Rebecca methodology review)*
