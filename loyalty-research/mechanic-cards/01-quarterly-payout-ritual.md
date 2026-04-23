# Mechanic Card 01 - Quarterly Payout Ritual
*Source: Rakuten "Big Fat Check" | 2026-04-21*

## What it is

Four fixed payout dates per year where accumulated cashback lands as a visible, anticipated payment. Rakuten pays on **Feb 15, May 15, Aug 15, Nov 15** - always the 15th. Methods: cheque, PayPal, Amex MR points (1:100), Bilt points. Minimum threshold: **$5.01**. [Data - rakuten.com/blog; High]

## Why it works as a habit driver

- **Dopamine anticipation 4x/year.** Users check back approaching each date to see their balance.
- **Brand ritual.** "Big Fat Check" has its own name, schedule, FAQ page, marketing moments. It becomes a thing users talk about.
- **Soft lock drives breakage.** Sub-threshold balances ($5.01 min) roll forward. Many users forget or abandon. Unredeemed cashback = margin.
- **Forces sub-quarterly engagement.** Users visit to accrue toward the next payout.

## Evidence this works

- Rakuten's rakuten.com has 63% direct traffic [Data - SimilarWeb Mar 2026] - users bookmark / type in. Strong repeat usage.
- 17M+ cumulative US members, $4.6B cumulative cashback paid since 1998 [Data; High]
- The mechanic has survived 27 years unchanged. That is the strongest survival signal in the category.

## Groupon adoption

**Copy the ritual. Skip the anti-customer details.**

- **Quarterly cadence:** pay on Feb 15 / May 15 / Aug 15 / Nov 15 (or Groupon-branded alternative - e.g. "Bucks Drop Day" with its own monthly-15th anchor).
- **Payout methods:** PayPal, Venmo, Groupon credit, OR cash-out to linked debit card at $1 minimum (Coupert-style, see card 04).
- **Brand the ritual.** Give it a name, a page, a push notification campaign, a homepage takeover.
- **Cumulative earnings counter** prominently on the home screen ("You've earned $127.43 this year; next payout Aug 15").

## Specifically do NOT copy

- **$5.01 minimum payout threshold** - anti-customer. Use $1 instead (per Coupert). Accept the small UX cost; trade for trust.
- **Pending-balance denials** - Rakuten aggressively invalidates pending balances. For Groupon, reserve-and-release, never confirm-and-revoke.
- **Bounced cheques** - PhatWallet reports of Big Fat Check bouncing [Data - PhatWallet Mar 2024]. If Groupon pays, it pays.

## Effort

- Backend ledger: ~1 sprint to build accumulating Bucks ledger per user.
- Cadence + payout job: ~0.5 sprint.
- Marketing / brand: ~1 sprint for the first "Bucks Drop Day" campaign.
- Cumulative counter UX: ~0.5 sprint.

**Total: ~2-3 engineering sprints + design + marketing.**

## Success metrics

- % of users with a positive Bucks balance on payout day
- Push open rate on "Bucks Drop" notification
- Visits-per-user in the 14 days prior to payout date (should spike)
- Payout redemption rate (target >70%; anything <50% means either UX friction or distrust)
- Breakage rate (aim for 15-25% steady state - above 30% means users are losing trust)

## Risks

- If Groupon cannot fund the cashback (Rakuten's 2.4% op margin is the category ceiling), the ritual reveals weak economics. Pilot at small scale before scaling.
- If Groupon cuts the rate after launch, the ritual amplifies the damage (rate cuts on established loyalty programmes are a well-documented backlash trigger across categories). Commit to 24 months of stable rate minimum before ever adjusting.

## Related

- Mechanic Card 02 - Soft Currency 1:1 (the thing being accumulated)
- Mechanic Card 03 - Weekly Anchor Day (fills sub-quarterly engagement gaps)
- Mechanic Card 05 - Trust Floor (guaranteed minimum back)
