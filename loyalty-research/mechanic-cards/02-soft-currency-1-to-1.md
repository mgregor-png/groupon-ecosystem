# Mechanic Card 02 - 1:1 Transparent Soft Currency (Groupon Bucks)
*Source: Capital One Shopping Credits | 2026-04-21*

## What it is

A branded soft currency where **1 unit = 1 dollar of redemption value**, with NO obfuscation. Users earn "Bucks" per purchase. Bucks redeem against Groupon deals, gift cards, or select partner retailers. Clarity is the load-bearing design choice.

Capital One Shopping's implementation: 1 credit = $1 USD (transparent), gift-card-only redemption at 50+ rotating retailers, no cash-out, no bank deposit, no statement credit, no Capital One banking account required. [Data - Capital One help center; High]

## Why 1:1 beats points systems

- **Clarity = trust.** Every time a user sees "1,000 points = ???", they have to do math. Honey does this (100 points = $1.00). Rakuten partially does this (cashback in $ but Amex transfer at 1:100). Capital One Shopping's 1:1 is the clean variant.
- **No devaluation gaming.** Points programs allow issuer to secretly devalue by changing redemption rates. High-profile examples across multiple loyalty categories have triggered customer backlash when long-held earn rates are silently cut. A 1:1 ratio makes devaluation impossible without a visible change users will notice.
- **Balance sheet elegance.** Bucks are a liability on the books, not a cash outflow. Breakage converts liability to profit.

## Breakage economics

- Industry benchmark: 15-30% of earned rewards never redeem [Estimate - multiple sources]
- Gift-card-only redemption adds a second layer of breakage (3-10% industry) [Estimate]
- Compounding: issue Bucks -> ~25% never redeemed -> of redeemed, ~5-10% of gift card value never spent -> real cash cost to issuer is 60-80% of headline "earned" [Opinion]

**For Groupon, breakage on Bucks could plausibly be the difference between 2% and 8% margin on the loyalty program. Pilot before scaling.**

## Redemption options (ranked by Groupon fit)

| Redemption | User appeal | Groupon margin | Recommendation |
|---|---|---|---|
| **Local experience on Groupon** (spa, restaurant, activity) | High - unique value | High (merchant relationships) | Primary path. Headline message. |
| **Groupon deal (any vertical)** | High | High | Secondary path |
| **Partner gift card** (Target, Amazon, Uber etc) | Medium (substitutable) | Medium | Optional, smaller catalog |
| **Cash-out to PayPal / Venmo** | Very high | Negative | Last resort, $1 minimum with processing fee |
| **Statement credit / bank deposit** | High | Negative | Do NOT offer - cannibalises Groupon spend |

Lean heavily toward the top two. They are what makes Bucks structurally better than a Capital One Shopping credit (gift card) - users get LOCAL experiences, which no competitor can match.

## Groupon adoption

**Copy:**
- **1:1 transparent earn rate.** 1 Buck = 1 dollar. Never obfuscate.
- **No paid tier, no banking / Groupon+ tie-in required.** Keep the loyalty layer standalone.
- **Earn rate 1-10% by merchant** (matches Capital One Shopping), with boosted rates on promotional events.
- **Clear on-screen balance + countdown to next payout.**
- **90-day retention gate on the welcome bonus** (Capital One Shopping's best idea - converts bonus-hunters into habit-formed users).

**Critical Groupon variant:**
- **Bucks redemption prioritises Groupon deals and local experiences** over external gift cards. This is Rebecca's "Bucks bridge" insight and it is the thing that makes Groupon's loyalty layer different from every other cashback app.
- **Unique positioning:** "Earn Bucks from Nike, spend on a massage near you."

## Specifically do NOT copy

- **Rotating redemption inventory that removes top brands** (Capital One removed Walmart, Home Depot, Macy's, Lowe's). Users lose trust when "my Target gift card" disappears. Lock in stable top-5 redemption partners with multi-year contracts.
- **Post-confirmation reward denials** (Capital One's top churn driver). Reserve-and-release architecture, not confirm-and-revoke.
- **Phone-number conflict redemption bugs** (Capital One operational failure). Test redemption end-to-end before GA.
- **"Wait 1 year before we investigate" customer service scripts** (Capital One). Target 30-day dispute SLA.
- **Gift-card-only redemption as the sole path.** Combine with cash-out at $1 (Coupert) and Groupon-deal redemption as primary.

## Effort

- Bucks ledger + issuance: ~2 sprints
- Redemption UX + gift card provider integration: ~2 sprints
- Merchant-side earn-rate config: ~1 sprint
- Finance model + breakage forecasting: ~1 sprint (analyst-led)
- Legal T&Cs (NO "not your property, not money" language per Honey): ~1 week legal

**Total: ~6 sprints eng + legal + finance.**

## Success metrics

- % of eligible sessions that earn Bucks
- Avg Bucks earned per active user per week
- Redemption rate by path (Groupon deal vs gift card vs cash-out)
- Breakage rate (target 15-25% steady)
- Bucks-driven Groupon deal purchase lift (Bucks bridge hypothesis)

## Risks

- Breakage model wrong => margin erosion. Pilot with bounded cohort first.
- Too generous earn rate => unit economics don't work. Benchmark against Rakuten's ~3% average and Capital One's variable 1-10%.
- Regulatory: any points / currency program may trigger state escheatment laws (unclaimed property). Legal review early.

## Related

- Mechanic Card 01 - Quarterly Payout Ritual (how Bucks are paid)
- Mechanic Card 04 - $1 Cashout Floor (escape valve)
- Mechanic Card 06 - Trust + Transparency (legal language, disclosure)
