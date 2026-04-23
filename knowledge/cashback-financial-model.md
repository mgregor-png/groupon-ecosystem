# Cashback Financial Model & Scenarios

**Source:** [Google Sheet](https://docs.google.com/spreadsheets/d/1NEeEws2Phld5M2TUFiVWsMUtOIY4gX0rnd3A_BC9ICI/edit)
**Fetched:** 2026-04-16

## Proposed Model (Base Case)

| Metric | Value | Type |
|--------|-------|------|
| Purchasers (5% of total 2024 purchases) | 195,000 | |
| Avg purchase per visitor (no cashback) | 1.6 | |
| % Cashback uplift on avg purchase | 20% | *Metric to be monitored* |
| Avg purchase per visitor (with cashback) | 1.92 | |
| AOV | $154.00 | |
| Average commission rate | 4.21% | |
| % increase on commission rate for cashback | 60% | *Metric to be negotiated* |
| Cashback commission rate | 6.74% | |
| % of commission awarded to user | 65% | *Metric to be controlled* |
| Non-cashback total purchases | 312,000 | |
| Cashback total purchases | 374,400 | |
| Non-cashback total commission | $2,022,821 | |
| Cashback total commission | $3,883,816 | |
| Cashback claim rate ($10 threshold) | 65% | *Metric to be monitored* |
| Cashback payout | $1,640,912 | |
| Cashback total commission after costs | $2,242,904 | |
| **Cashback vs non-cashback profit margin** | **$220,083** | |
| Cashback vs non-cashback uplift | +11% | |
| Cashback ROI | 136.69% | |

## Three Scenarios

| Metric | Worst | Middle | Best |
|--------|-------|--------|------|
| Purchasers | 195,000 | 195,000 | 195,000 |
| % Cashback uplift on purchase freq | 9% | 20% | 50% |
| Avg purchase/visitor (with cashback) | 1.744 | 1.92 | 2.4 |
| % increase on commission rate | 20% | 60% | 100% |
| Cashback commission rate | 5.05% | 6.74% | 8.42% |
| % commission awarded to user | 90% | 65% | 40% |
| Cashback total purchases | 340,080 | 374,400 | 468,000 |
| Cashback total commission | $2,645,850 | $3,883,816 | $6,068,462 |
| Cashback claim rate | 80% | 65% | 40% |
| Cashback payout | $1,905,012 | $1,640,912 | $970,954 |
| Commission after costs | $740,838 | $2,242,904 | $5,097,508 |
| **Profit margin vs non-cashback** | **-$1,281,983** | **$220,083** | **$3,074,688** |
| Ratio vs non-cashback | -63% | +11% | +152% |
| Cashback ROI | 38.89% | 136.69% | 525.00% |

### Sensitivity Notes

- **Metrics we have less control over:** Purchase frequency uplift, claim rate - depends on UX & strength of cashback offers, not a quick lever
- **Metrics we control (medium):** Commission rate increase - depends on individual merchant negotiations & cashback offer mix
- **Metrics we control most:** % of commission paid to user - must be competitive with market (40-90% range)

### Long-Term Impact Adjustments

| Factor | Impact | Applied to all scenarios |
|--------|--------|------------------------|
| Google AI overview traffic erosion | -20% | Reduces non-cashback margin by $404,564 |
| Improved CPA over time | +5% | Adds $119K-$273K depending on scenario |
| **Long-term profit margin** | **-$758K / $799K / $3,752K** | worst/mid/best |
| Long-term ratio vs non-cashback | -47% / +49% / +232% | worst/mid/best |

## Rewards Users -> Deal Purchasers (BI Analysis)

**Source:** Asana task [1209680800265191](https://app.asana.com/1/8437193015852/project/1203832216598736/task/1209680800265191)

### Data Parameters
- **Region:** NA
- **Time Period:** PRE (Dec'23 - Jul'24, 8mon), POST (Aug'24 - Mar'25, 8mon)
- **Pre/post periods:** Determined based on subscription date
- **Subscribers:** Users who subscribed via "coupons" legal consent origin
- **Metrics measured:** From subscription date up to latest date (26th Mar'25)

### Key Findings

| Metric | PRE | POST | Change |
|--------|-----|------|--------|
| New Subscribers | 30K | 406K | +1,247% |
| % Purchasers | 22% | 86% | +64pp |
| Orders/NewSubs | 0.67 | 1.52 | +127% |
| GP/NewSubs | $8.74 | $23.58 | +170% |

**Bottom line:** Significant growth across all key metrics. Post-period coupons subscribers convert to deal purchasers at dramatically higher rates, with higher purchase frequency and increased spending.

## Engineering Work Breakdown (Sheet7)

Full breakdown: 21 work packages, detailed below.

| # | Work Package | Role(s) | Man-Days | Key Outputs |
|---|-------------|---------|----------|-------------|
| 1 | Discovery & functional spec | PM, Eng Lead, Data Lead | 10 | Signed PRD, sequence diagrams |
| 2 | High-level architecture & threat model | Eng Lead, Security | 8 | HLD, DFD, STRIDE review |
| 3 | Data-model & migrations | Backend | 6 | Liquibase migrations, ADR |
| 4 | Cashback Ledger micro-service | Backend (2) | 25 | CRUD APIs, unit tests, CI |
| 5 | Merchant rate & rule engine | Backend | 10 | Admin API + UI hooks |
| 6 | Order pipeline - click -> purchase attribution | Backend, Affiliate team | 12 | New message on Kafka, schema change |
| 7 | Settlement & payout batch jobs | Backend, DevOps | 15 | Step-Function, IAM, CloudWatch alerts |
| 8 | Payout gateway integration (PayPal + Stripe) | Backend (2) | 18 | OAuth, webhooks, idempotent retries |
| 9 | Voucher-Boost Service & voucher code API | Backend | 15 | Balance-to-voucher flow, id mapping |
| 10 | Groupon voucher inventory API bridge | Backend | 8 | Internal service contract |
| 11 | Web UI - coupon list badges & wallet | Front-end (React) | 20 | Responsive components, A/B flags |
| 12 | Wallet dashboard & settings page | Front-end | 12 | Historic transactions table |
| 13 | Checkout changes (apply boost) | Front-end + Backend | 12 | New step, validation |
| 14 | Mobile app parity (wallet, boost modal) | iOS, Android | 24 | GraphQL queries, UI tests |
| 15 | Auth funnel tweaks (cashback CTA) | Front-end | 6 | 2 new React screens |
| 16 | Notifications & CRM events | Backend, CRM | 8 | Braze templates, webhook |
| 17 | Fraud rules, rate-limiting & monitoring | Security, Backend | 10 | WAF rules, risk score |
| 18 | Observability & Looker/Grafana dashboards | Data Eng, DevOps | 8 | Metric specs, alerts |
| 19 | QA test-plan & execution (manual + automation) | QA (2) | 20 | Test cases, Cypress suites |
| 20 | UAT, bug-fix & hardening sprint | All | 10 | Release candidates |
| 21 | Launch/rollback playbook | SRE, PM | 5 | Run-books, incident drill |

**Total:** ~252 man-days (full build-out, not the 40-50 MD initial estimate)

Note: The 40-50 MD from Minas is likely the core cashback-on-coupons piece only. The 252 MD sheet covers the complete ecosystem (cashback + voucher boost + mobile + fraud + ops).

## ChatGPT Market Research (from sheet)

### Purchase Frequency Uplift Benchmarks
- Price-sensitive shoppers: 25-50% increase (baseline 2x/mo -> 2.5-3x/mo)
- Average customer: 10-30% increase (baseline 1x/mo -> 1.1-1.3x/mo)
- Loyal customers: <10% (marginal gain)

### Commission Pass-Through Benchmarks
| Type | % Passed to Users |
|------|------------------|
| Traditional (Rakuten) | 40-60% |
| Aggressive/Growth (TopCashback) | 70-90% (sometimes near 100%) |
| Fintech/Card-linked (Dosh) | 30-50% |
| Multi-feature wallets | 20-40% |

### Cashback Redemption Rate Benchmarks
| Program Type | Redemption Rate |
|-------------|----------------|
| Dedicated platforms (Rakuten, TopCashback) | 70-85% |
| Card-linked (Dosh, bank apps) | 60-80% |
| Retailer loyalty/rewards programs | 50-70% |
| Gamified/delayed cashback apps | 40-60% |

### Commission Rates: Cashback vs Coupon Sites
| Affiliate Type | Avg Commission (% of sale) |
|---------------|---------------------------|
| Cashback sites | 2-5% |
| Coupon/discount code sites | 1-4% |
