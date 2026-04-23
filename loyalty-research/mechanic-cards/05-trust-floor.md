# Mechanic Card 05 - Trust Floor (Guaranteed Minimum + $1 Cashout)
*Sources: RetailMeNot 1% guaranteed floor (Feb 25, 2026) + Coupert $1 withdrawal | 2026-04-21*

## What it is

Two complementary trust primitives:

1. **Guaranteed minimum rate.** Every qualifying purchase through Groupon earns AT LEAST X% back, regardless of merchant-specific rate. RetailMeNot's version: 1% floor across 4,000+ retailers launched Feb 25 2026 [Data - retailmenot.mediaroom.com; High].
2. **$1 cashout floor.** Users can withdraw any balance over $1 (with a small processing fee). Coupert's version: $1 min via Visa/Mastercard with 2% + $0.50 fee [Data - Coupert help center; High].

Together these reframe cashback from "a future promise I may never collect" to "real money I could take out tomorrow if I wanted."

## Why each works

### The guaranteed floor
- **Removes shopping-around from the decision tree.** If every purchase earns at least 1%, users stop comparing rates across tools. Groupon becomes the default.
- **Turns variable rates into brand certainty.** Users don't need to know what each merchant pays; they know the minimum.
- **Works as a trust primitive, not a loyalty mechanic per se.** It's not designed to drive habit; it's designed to make the app trustable.

### The $1 cashout floor
- **Validates the system works on the first small purchase.** A new user earns 47 cents, cashes it out, gets a Venmo notification - the trust is cemented immediately.
- **Breaks the "abandoned balance" anti-pattern** that haunts Honey (1,000 points min = $10), Rakuten ($5.01 min), and Capital One Shopping (gift-card-only, ~$5+ values). Those thresholds silently favour the issuer.
- **Counter-intuitively, aligning with user incentive builds more habit.** Users who have cashed out once are more likely to come back than users who still haven't hit the threshold to redeem.

## Why both together

Individually, either is thin. Combined they become: "You will earn at least X% back on every purchase, and you can pull it out as real money for $1." That is a rational-default framing that no competitor currently has.

## Evidence

- RetailMeNot launched the 1% floor as a defensive move amid 18% segment revenue decline [Data - Ziff Davis Q4 2025 earnings Feb 2026]. The fact that they chose THIS as the differentiator suggests it is the mechanic that most resists AI-search displacement.
- Coupert's $1 floor appears prominently in every review and comparison of the tool. It is the one mechanic users mention unprompted.
- Both mechanics are LOW engineering cost and LOW margin impact at small scale. The value is brand/positioning, not unit economics.

## Groupon adoption

**Copy both, integrate with Bucks:**

- **Floor: every qualifying Bucks-earning purchase earns minimum 1 Buck per $100** spent, even if the merchant pays <1% commission. Groupon makes up the difference. [Cost: negligible at pilot scale; needs finance model at full scale]
- **Cashout: any Bucks balance >$1 can be withdrawn** to PayPal, Venmo, or linked debit card. Processing fee: 2% + $0.50 (matches Coupert). [Small processing cost, offset by trust value]

## Communication framing

**Don't bury this in FAQ.** Put it on the homepage and extension UX:

- "Every purchase earns at least 1% back. Guaranteed."
- "Cash out any Bucks balance above $1 - your money, anytime."

## Specifically do NOT copy

- **Hidden floor caveats.** If the floor has exceptions, disclose them up front. RetailMeNot's fine print excludes some categories; any Groupon version must be clearly enumerated.
- **Cashout fees hidden in T&Cs.** If the fee is 2% + $0.50, say so at the withdrawal confirmation screen. Don't let users be surprised.
- **Minimum thresholds disguised as floors.** Rakuten's $5.01 is called a "minimum payout threshold", which is a soft lock. Coupert's $1 is called a "minimum withdrawal", which is a genuine escape valve. Language matters.

## Interaction with other mechanics

- **Quarterly payout ritual (Card 01):** The floor sets the baseline; quarterly payouts are the ceremony. Users know they'll always get something each quarter because of the floor.
- **Soft currency 1:1 (Card 02):** Floor applies to Bucks earning rate; cashout is an alternative redemption path alongside Groupon-deal and gift-card redemption.
- **Safari extension (Card 04):** Floor is the headline feature on the extension's post-checkout "you earned Bucks" screen.

## Effort

- **Floor implementation:** ~0.5 sprint (merchant config logic - floor applies if merchant-specific rate < 1%)
- **$1 cashout:** ~1-2 sprints (payment-rail integration; partnership or payment processor required)
- **T&Cs + disclosure UX:** ~1 week legal + design

**Total: ~2-3 sprints.**

## Success metrics

- % of purchases where the floor boosts the base rate (tells us how often it fires; lower is fine - it's a safety net)
- **First-month cashout rate** for new users (target: 20-40% cash out at least once in first 30 days - proves the mechanic is trusted)
- Avg cashout size (Coupert reports users cash out ~$5-10 on average; smaller avg is better trust signal than larger)
- User-reported trust metrics in survey data (NPS on "I trust I will get paid" category)

## Risks

- **Floor cost at scale.** If Groupon scales to 10M Buck-earning users, even a 1% floor on $10/user/month = $1M/month of Groupon subsidy. Pilot with cohort before scaling, and design the floor to be tunable (1% default, configurable to 0.5% if margin pressure).
- **Cashout rate higher than expected.** If users cash out aggressively, Groupon loses the redeem-against-deals flywheel. Monitor closely; if >40% of Bucks are cashed out vs spent on Groupon deals, the mechanic needs revisiting.
- **Regulatory.** Payment processor rules, state money-transmitter laws. Legal review. Likely handled via existing Groupon payment infrastructure if PayPal/Venmo are rails.

## Related

- Mechanic Card 01 - Quarterly Payout Ritual (the headline payout; floor is the baseline)
- Mechanic Card 02 - Soft Currency 1:1 (Bucks itself)
- Mechanic Card 06 - Trust + Transparency (the floor is a trust primitive; the cashout is the proof)
