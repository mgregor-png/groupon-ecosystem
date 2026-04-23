Better Leveraging Anonymous Coupons Traffic - Raw Data & Sources
Prepared for Dusan / Adam / Rebecca | April 2026

EXECUTIVE SUMMARY
Proposal: Extract more value from 30M anonymous coupons sessions through 3 additive layers - quick monetisation wins, Genie rewards integration, and longer-term identity + extension infrastructure.
Layer 1 (now): ~$518-694K/yr from display ads, deal cross-sell, Genie CTA. ~8 MD, no dependencies.
Layer 2 (Q2): Genie + Rewards. ~15 MD, email-first, no external deps. +29-110% revenue per user.
Layer 3 (Q2-Q3+): Registration, Safari extension, Cashback. External deps, bigger investment.
This document contains the raw data sources supporting each claim.


1. COUPONS TRAFFIC BASELINE

Source: Coupons Tableau project
https://analytics.groupondev.com/#/projects/1332

~30M organic sessions/yr
$0.43/session blended
$12.6M commission/yr
14.8M clicks/yr
61% mobile traffic
1,606 monetised merchants (19.1M sessions/yr)
2,107 non-monetised merchants (8.2M sessions/yr)

BigQuery source: prj-grp-coupons-prod-8892.rep.01_management_dashboard
Period: US, Apr 2025 - Apr 2026


2. CROSS-SELL GROUPON DEALS

Sources:
Coupons sessions: prj-grp-coupons-prod-8892.rep.01_management_dashboard (US, last 12 months)
Deal page revenue/session: prj-grp-dataview-prod-1ff9.supply.unagi_monthly (US, all-time)
Cross-sell history: prj-grp-coupons-prod-8892.edw.dim_cross_sell_order
CTR data: Rebecca (Costco 19% actual, others estimated 10%)

Model A - Shared merchants (deals shown on matching coupons pages):

Costco:           542,818 sessions/yr | 19% CTR (actual) | $0.37 deal rev/s | $0.00 current | $38,160 incremental
Sam's Club:       131,681 sessions/yr | 10% CTR           | $0.77 deal rev/s | $0.47 current | $10,139 incremental
JCPenney:          62,048 sessions/yr | 10% CTR           | $1.24 deal rev/s | $0.17 current |  $7,694 incremental
Shutterfly:       112,345 sessions/yr | 10% CTR           | $0.58 deal rev/s | $1.45 current |  $6,516 incremental
Regal Cinemas:     54,080 sessions/yr | 10% CTR           | $0.38 deal rev/s | $0.00 current |  $2,055 incremental
Canvas On Demand:   7,021 sessions/yr | 10% CTR           | $1.91 deal rev/s | $0.45 current |  $1,341 incremental
TOTAL:            909,993 sessions/yr                                                          $65,906 incremental

Model B - Top deals promoted across all coupons pages (lower CTR, more sessions):

All pages:            27,346,180 sessions/yr | @ 1% CTR: $175,562 | @ 2% CTR: $351,125
Non-monetised only:    8,233,291 sessions/yr | @ 1% CTR:  $52,858 | @ 2% CTR: $105,715
Monetised only:       19,112,889 sessions/yr | @ 1% CTR: $122,705 | @ 2% CTR: $245,409

Avg deal rev/session: $0.64 (weighted from top 5 deals)
Combined A+B: $241-417K/yr

Costco CTR source: Rebecca Spurr - Costco coupons page, last 28 days: 28,887 sessions > 5,771 referrals = 19%
Six Flags reference: 3,489 sessions > 70 referrals = 2%

CTR sensitivity (Model A only, shared merchants):
At 5% CTR (all merchants incl. Costco): ~$21K/yr
At 10% CTR (used in model, Costco at 19%): ~$66K/yr
At 15% CTR (all merchants incl. Costco): ~$98K/yr
Note: Only 2 actual data points exist (Costco 19%, Six Flags 2%). The 10% assumption for non-Costco merchants is a midpoint estimate, not validated. The range between the two data points is 10x. Model B (all pages) uses 1-2% CTR which is more conservative.

CLTM downstream tracker:
https://analytics.groupondev.com/#/views/CLTMDownstreamTrackerV2/CLTMTrackerSegmentView?:iid=2


3. DISPLAY ADS

Source: Rebecca Spurr
Annual estimate: ~$276,750
Awaiting: Breakdown from Rebecca (CPM, fill rate, eligible inventory). Number is a top-line estimate without published formula.
Effort: 3-5 MD (2-3 MD with AI-first team)
Requires: New ad spec from Ads team, placeholder size and implementation
Engineering estimate source: VC team - 3-5 MD including testing ($2,750)
Note: This is the least verifiable number in the document. Treat as directional until Rebecca provides the underlying assumptions.


4. REGISTRATION

Source: Behdad Karimi (BI)
https://app.asana.com/1/8437193015852/project/1210682964756930/task/1213804728929738/comment/1213821285294140

Current registrations from coupons: 540K/yr
Registrant to 1Y conversion (1+ purchase): 13.04% (NA, Feb 2023 - Mar 2024)
1Y LTV per converted customer (discount cohort): $31.88
Per registration LTV: 13.04% x $31.88 = $3.83
Annual value: 540K x $3.83 = ~$2.07M/yr
Data vintage: Conversion rates from Feb 2023 - Mar 2024 registrant cohorts. LTV from Jan+Feb 2025 cohorts. No 2026 cohort data available yet - may differ given Groupon's recent trajectory.

Effort: ~15 MD + external deps (Core B2C for GraphQL auth, Bloomreach for delayed email registration)
NOT a quick win - coupons has no registration today. Full flow needed: GraphQL core auth integration, registration UI, delayed reg via email, reward gating logic, session identity handling.


5. GENIE - CURRENT STATE

Sources:
Genie LTV Model: https://mgregor-png.github.io/coupons-dashboards/genie-ltv-model.html
Raw data: https://docs.google.com/spreadsheets/d/1hzMz_Dj4dJjniGrC-_YPHLQYkXJRF0r_tbBKw7JiodY/edit
BigQuery: prj-grp-coupons-prod-8892.rep.genie_dashboard

Cumulative installs: 981 (as of Wk12, Mar 16, 2026)
Weekly active users: ~100-340
Total CJ commission: $2,622 (23 weeks)
Total transactions: 388
Commission/user/yr: $6.04 ~ $6.00
Caveat: Small sample (981 installs, 388 txns). Directional, not statistically robust.


6. GENIE + REWARDS

Sources:
Rewards Tableau: https://analytics.groupondev.com/#/views/07RewardsDashboard_17591580155130/Overview?:iid=2
Cross-channel analysis: Jarrett Sidaway consultant document (Nov 2025)
https://docs.google.com/document/d/1MjiHmyTFV2j2R-4vqdfKeJwPszpPD-am04_-SpHGwuE/edit
Genie LTV Model Scenario 2: https://mgregor-png.github.io/coupons-dashboards/genie-ltv-model.html

a) Rewards program economics (from Tableau, Jan-Oct 2025):
With rewards conversion (txn/click): 10.93%
Without rewards conversion: 6.29%
Uplift: +74%
Commission/txn with rewards: $15.82
Commission/click with rewards: $1.73 vs $0.84 without (+106%)
Reward cost/txn: $2.97
Reward ROI: 5.33x
Redemption rate (of claimed): 19.9%

b) Applied to Genie (LTV model Scenario 2):
Current: $6.00/user/yr
With rewards (2.06x uplift, net of $4.62 reward cost): $7.74/yr (+29%)
LTV with retention uplift: $19.34-22.28

c) Cross-channel data (Jarrett's analysis):
Extension users: 33% make 3+ purchases/yr (vs 5% web) = 6x more likely
Extension + Rewards revenue/user: $17.50/yr (vs $5.40 web, $8.30 ext without rewards)
Rewards lift on extension: +110% (highest of any channel)
Rewards lift on web: +41%, email: +80%, app: +75%

d) Auto-apply impact:
Revenue per user increase: ~20%
Driven by engagement/cookie volume, not checkout success rate

Effort: ~15 MD (AI-first team, L3+)
MVP is email-first, no login/registration dependency
Reuses existing web rewards infrastructure (Giftcloud)
Asana task: https://app.asana.com/1/8437193015852/project/1205603135602102/task/1212298912009523
Jira: https://groupondev.atlassian.net/browse/VC-7121


7. GENIE + DEALS CROSS-SELL

Source: Behdad Karimi (BI) + LTV Model Scenario 3
https://mgregor-png.github.io/coupons-dashboards/genie-ltv-model.html

Registrant to 1Y conversion: 13.04%
1Y LTV per converted customer (discount): $31.88
Assumption: 50% of installs register on Groupon (unvalidated - no data on Genie-to-Groupon registration rate exists yet)
Effective deals conversion per install: 6.5%
1Y deals LTV per install: $2.07
Total with rewards + deals: $9.81/user/yr

Effort: ~18 MD (AI-first)


8. SAFARI EXTENSION

Source: Save Everywhere report raw data doc (full detail)
https://docs.google.com/document/d/1Th5zbtT6lvxfGdev9DyCJIBKW9rNhwB_YZ2unDKuZNA/edit

Key numbers (reproduced here for standalone use):
14-day active app users (US): ~6-7M (Tableau, midpoint 6.5M)
iOS share: 84% (Tableau, Mar 15 - Apr 14)
Safari-addressable base: ~5.5M

Commission/user: $6.00 (Genie desktop actual - small sample: 981 installs, 388 txns)
Note: This is the same $6/user that anchors the Genie rewards model. The Safari revenue range is entirely dependent on this figure and on the activation rate assumption. Neither is validated at scale.

Activation rate: 10-30% (no verified benchmark)
Honey's PayPal app activation is estimated at ~30% but not publicly confirmed.

Revenue at $6/user:
5% activation (275K users): $1.1M/yr (not used in model - below floor)
10% activation (550K users): $3.5M/yr (conservative)
20% activation (1.1M users): $6.6M/yr (base)
30% activation (1.65M users): $9.9M/yr (optimistic)

Validation: Jon's Safari extension test confirmed iOS app bundling works technically.
https://app.asana.com/1/8437193015852/project/1208046402782685/task/1213861645172479


9. CASHBACK

Sources:
Strategy doc: https://docs.google.com/document/d/1jlErXw8wozl3E6hLmJdlCS1r1ZLaQnxB5ooNqyE1A_U/edit
Financial model: https://docs.google.com/spreadsheets/d/1NEeEws2Phld5M2TUFiVWsMUtOIY4gX0rnd3A_BC9ICI/edit
Full deck: https://docs.google.com/presentation/d/1teyJnZ-zrKWiJBjAQjBQrHwN0edrTPIP-m_B27jSFjU/edit

4 goals: user acquisition (registration gating), app upsell, retention, deal conversion

Funnel (from deck, 95M all sessions):
25% reg rate > 23M registrations > 5% cashback txns (1.1M) > 50% Bucks conversion > 2.8M annual Groupon purchases
Coupons organic is ~30M of those 95M sessions.

Financial model (middle scenario):
Purchasers: 195,000 (5% of total 2024 purchases)
Cashback commission rate: 6.74% (vs 4.21% standard, +60% negotiated)
65% of commission awarded to user
Cashback total commission: $3,883,816
Cashback payout: $1,640,912
Net after costs: $2,242,904
Cashback vs non-cashback profit margin: +$220,083 (+11%)
ROI: 136.69%

Three scenarios:
Worst: -$1,281,983 (-63%)
Middle: +$220,083 (+11%)
Best: +$3,074,688 (+152%)

Scope note: The funnel model (95M sessions, 23M registrations) covers ALL Groupon coupons traffic globally. Coupons organic (this proposal's scope) is ~30M of those 95M sessions. The financial model numbers above are based on the full 95M funnel, not the 30M coupons-only slice. A coupons-only model would be proportionally smaller (~32% of the totals). The $220K middle scenario for coupons-only would be roughly ~$70K. This needs to be properly re-modeled for the coupons scope if cashback is pursued.

Engineering: 40-50 MD (from strategy doc, eng feedback section)
AI-first estimate: ~20 MD + external deps (Core B2C, Bloomreach, Financial dept)

PoC scope: merchant page 4MD, offer type 2MD, registration 1MD, profile 5MD, Bucks conversion 2MD, withdrawal 1MD + coordination


10. AI-FIRST DEVELOPMENT ESTIMATES

Source: Minas Arustamyan - AI First Development Team presentation (March 2026)
https://docs.google.com/presentation/d/1Ey3d-5j2KIgL7RVDrOKd3n7mPXrD5bNqj6WYYNyxPfc/edit

Team: 8 engineers, 4 domains, 25 repositories, 7 tech stacks
AI maturity: L3+ ("Human directs, AI implements")
Meta-repository with 3-layer hierarchy (root > domain > repo)
Shared knowledge compounds across all engineers

Principle: AI compresses code-writing time (~30-35% reduction), NOT coordination, external deps, or validation. Biggest gains on FE-heavy work with existing patterns and designs.


---
REFERENCES
---

Better Leveraging Anonymous Coupons Traffic: https://mgregor-png.github.io/coupons-dashboards/coupons-initiatives-overview.html
Save Everywhere report: https://mgregor-png.github.io/coupons-dashboards/save-everywhere-report.html
Save Everywhere raw data: https://docs.google.com/document/d/1Th5zbtT6lvxfGdev9DyCJIBKW9rNhwB_YZ2unDKuZNA/edit
Genie LTV model: https://mgregor-png.github.io/coupons-dashboards/genie-ltv-model.html
Genie raw data: https://docs.google.com/spreadsheets/d/1hzMz_Dj4dJjniGrC-_YPHLQYkXJRF0r_tbBKw7JiodY/edit
Competitor research: https://mgregor-png.github.io/coupons-dashboards/competitor-research-2026-04-08.html
Cashback strategy: https://docs.google.com/document/d/1jlErXw8wozl3E6hLmJdlCS1r1ZLaQnxB5ooNqyE1A_U/edit
Cashback financial model: https://docs.google.com/spreadsheets/d/1NEeEws2Phld5M2TUFiVWsMUtOIY4gX0rnd3A_BC9ICI/edit
Cashback deck: https://docs.google.com/presentation/d/1teyJnZ-zrKWiJBjAQjBQrHwN0edrTPIP-m_B27jSFjU/edit
Consultant analysis (Jarrett): https://docs.google.com/document/d/1MjiHmyTFV2j2R-4vqdfKeJwPszpPD-am04_-SpHGwuE/edit
AI-first team: https://docs.google.com/presentation/d/1Ey3d-5j2KIgL7RVDrOKd3n7mPXrD5bNqj6WYYNyxPfc/edit
Viktor clickstream: https://gamma.app/docs/GROUPON-LIFE-u9tppglyxfzpu7j
Coupons Tableau: https://analytics.groupondev.com/#/projects/1332
App metrics Tableau: https://analytics.groupondev.com/#/views/MbnxtVs_LegacyPerformanceBQKeboola/BaseMetrics
Rewards Tableau: https://analytics.groupondev.com/#/views/07RewardsDashboard_17591580155130/Overview
CLTM tracker: https://analytics.groupondev.com/#/views/CLTMDownstreamTrackerV2/CLTMTrackerSegmentView
Behdad BI data: https://app.asana.com/1/8437193015852/project/1210682964756930/task/1213804728929738/comment/1213821285294140
Genie Rewards Asana: https://app.asana.com/1/8437193015852/project/1205603135602102/task/1212298912009523
Jon Safari test: https://app.asana.com/1/8437193015852/project/1208046402782685/task/1213861645172479
Figma designs: https://www.figma.com/design/CHEG2ocUJ6vhZXjph0aUhi/GC---Research---Development
