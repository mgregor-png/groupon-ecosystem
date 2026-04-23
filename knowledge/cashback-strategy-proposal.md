# Cashback & Conversion Strategy Proposal

**Source:** [Google Doc](https://docs.google.com/document/d/1jlErXw8wozl3E6hLmJdlCS1r1ZLaQnxB5ooNqyE1A_U/edit)
**Fetched:** 2026-04-16

## Executive Summary

Groupon's .com coupons subdomain draws ~17M unique visitors/year, 84% via organic search. Only 4% open accounts, average repeat engagement is 1.6 coupons purchases p/a. AI-driven search snippets increasingly surface promo codes directly, threatening affiliate revenue.

Proposal: Layer a performance-based cashback programme plus a "boosted-value" conversion path into Groupon vouchers. Goal: transform one-off coupon seekers into logged-in, high-value Groupon customers while insulating from SEO volatility.

## Background & Challenge

| Metric | Current | Issue |
|--------|---------|-------|
| Annual uniques | ~17M | High traffic, low capture |
| Account creation | 4% | Missed CRM & cross-sell opportunities |
| Repeat purchase rate | 1.6 | Low engagement |
| Avg commission/txn | ~$5 | Limited monetisation |
| SEO dependency | 84% traffic | Vulnerable to AI search overviews |

## Opportunity

### Part 1: Cashback Offers
For selected Coupons merchants, negotiate elevated CPA rates using existing Coupons sales team and pass a share back to users. Set a $10 cash-out threshold to drive >=2 purchases (baseline 1.6 x $5 = $8).

### Part 2: Voucher Upsell
Allow users to convert balance into selected Groupon vouchers at a premium (e.g. $10 cash -> $12-$15 voucher), selected by margin and customer-value models.

### Customer Value Proposition
Positioning tagline: "Cashback that grows when you treat yourself." Users can either take the savings or amplify them into memorable experiences via Groupon.

Key differentiator: Unique "boost" into local experiences - no direct competitor blends cashback with local adventures.

## Objectives & Target KPIs (Year 1)

| Objective | Baseline | Target |
|-----------|----------|--------|
| Account registrations | 4% of visitors | 10% (+1M regs) |
| Repeat purchase rate (cashback cohort) | 1.6 | >=1.92 (+20%) |
| Purchases via cashback | 0% | 5% total orders |
| Net revenue per cashback user | - | +10% vs non-cashback |
| CRM/email share of Coupons traffic | 1.6% | 5% |

## Operating Model

- **Ownership:** Existing Coupons team (parallels reward offers)
- **Forecast & Launch:** Business casing for every merchant; live monitoring & optimisation
- **Levers we control:**
  - Negotiated commission (often > standard coupons CPA)
  - User cashback payout %
- **KPIs monitored:** Purchase frequency, claim/breakage rate, LTV uplift
- **Programme Policies:**
  - Minimum payout: $10 (industry bench: Rakuten $5)
  - Cashback expiry: 12 months inactivity

## Financial Impact (Illustrative, Year 1)

- +20% repeat orders within cashback cohort
- 5% of total coupon transactions via cashback
- +11% net incremental revenue after payouts
- +1M net new registered users
- First-purchase conversion uplift via voucher exchange (baseline TBD)

## AI Opportunities

1. **Automated programme management:** Evaluate CPA rates, conversion rates and claim rates to suggest/create offers, flag low-performing or costly cashback offers
2. **Personalised voucher upsell rates:** Data modeling to offer personalised voucher upsell opportunities based on expected customer value (location/demographic match to best Groupon profiles)

## Engineering Feedback

Cashback added onto groupon.com/coupons = estimated engineering effort ~40-50 man-days.

Jira ref: [VC-5884](https://groupondev.atlassian.net/browse/VC-5884?focusedCommentId=8797654)

## Key Comments from Doc

- **Jon Smith (merchant feedback):** General optimism that CPA could increase - comes down to individual negotiations. Full merchant feedback in [Asana task](https://app.asana.com/1/8437193015852/project/1207220980840322/task/1210430303353249)
- **Voucher upsell = "Groupon Bucks"** concept - could be selected deals with high margins if concern about bucks spent on low-margin deals
- **Minas confirmed:** Team could build inhouse, but need to decide payment solution (e.g. PayPal etc)
