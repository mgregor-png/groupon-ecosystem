# Mechanic Card 06 - Trust and Transparency (The Anti-Honey Checklist)
*Source: Forensic reverse engineering of PayPal Honey 2024-2026 trust collapse | 2026-04-21*

## What it is

Not a single mechanic. A **design discipline** that governs every other mechanic. The discipline is simple: every loyalty mechanic must be transparently user-positive. If a mechanic only works when users don't understand it, it is a liability waiting for a viral expose.

This card exists because PayPal Honey lost 40% of Chrome users (20M -> 12M) in 12 months after a YouTube video explained how Honey actually worked. Three major affiliate networks cut Honey off over five days in Jan 2026. A 101-page class action is active. The failure mode is specific, documented, and entirely avoidable.

## The Honey failure-mode catalog

From MegaLag Part 1 (Dec 2024), Part 2 (Dec 2025), class action complaint, affiliate network statements:

1. **Silent cookie overwrites at checkout.** Honey's popup at checkout would overwrite the creator's affiliate cookie with Honey's. User got "no better code found" but the click hijacked the commission. MegaLag's smoking gun: $35 NordVPN commission rerouted from a creator to Honey while user got $0.89 Honey Gold back.
2. **Merchant-paid code suppression.** Honey had contractual agreements with some merchants to NOT surface codes better than a merchant-approved default. Users saw "no better code found" when RetailMeNot had obviously better codes one click away.
3. **Private-code scraping (MegaLag Part 2).** Honey scraped codes users manually typed (employee codes, refund codes, retention-offer codes) and rebroadcast them to all Honey users. Merchants asked for takedown; Honey refused unless they became paying partners.
4. **Bundle-lock.** Honey iOS extension cannot be uninstalled independently of the PayPal wallet app. Users who want to remove Honey must remove PayPal.
5. **Long pending windows (60-90 days)** combined with **365-day inactivity forfeiture**, combined with **$10 minimum redemption threshold**, combined with **account-closure forfeiture of all points**. Each looks reasonable individually; together they form a breakage-optimisation machine.
6. **"Not your property, not money, no value prior to redemption" T&C language.** Standard for points programs, but this language becomes the legal team's nightmare in a class action.
7. **Creator sponsorships as primary acquisition channel.** YouTube creators, once the marketing engine, became the named plaintiffs.
8. **PayPal's defence ("industry standard", "legacy code").** This framing made the situation worse - it conceded the practices while shifting blame backwards. Never rely on "everyone does it" as defence.

## The Groupon checklist

Every mechanic card in this research has a "specifically do NOT copy" section derived from this failure-mode catalog. Consolidating:

### Design principles (non-negotiable)

1. **No silent cookie overwrites.** Groupon's extension must NEVER overwrite an affiliate cookie it did not originate.
2. **No merchant-paid code suppression.** If Groupon has merchant agreements that restrict code visibility, disclose them inline at the point of use.
3. **No private-code scraping.** Code database accepts only codes from verified merchant feeds or affiliate network feeds.
4. **Independent uninstall.** Groupon's Safari extension must be removable from Groupon app settings without uninstalling the Groupon app.
5. **Short pending windows.** 7-15 days max (matching Coupert), not 60-90 (Honey).
6. **No silent expiration.** Any Buck expiration requires 30/60/90-day warning email cadence and a clear in-app countdown.
7. **Account closure does not forfeit earned Bucks.** Closed accounts get a final redemption window.
8. **$1 cashout floor** (per Card 05). No artificial minimum thresholds disguised as "minimums."
9. **Legal T&Cs in plain language.** No "not your property, not money, no value" phrasing. Every sentence should read cleanly in front of a jury.
10. **Diverse acquisition channels from day one.** Don't concentrate on creator sponsorships. Paid social, app-store organic, partnerships, referral, content - broad mix.

### Proactive disclosure UX

Things Groupon should build because Honey didn't:

- **Attribution banner in Safari extension.** "Groupon is earning affiliate commission on this purchase. We pay it back to you as Bucks." Shown once per merchant per session, not on every transaction.
- **Code provenance display.** When the extension applies a code, show where the code came from: "Code verified from [Merchant direct partnership / Affiliate network / Public aggregator]."
- **Explicit merchant partnership list.** Public page listing every merchant Groupon has an active affiliate / direct partnership with. Nothing else appears in the extension.
- **User dashboard for earned Bucks.** Full transaction log - when earned, what purchase, what merchant, what rate, when payable, when expired. Every Buck's provenance visible.
- **Change log for T&C updates.** Any change to rewards terms is published 30 days in advance with a summary of what changed.

### What trust looks like in marketing

- "Every merchant in the Groupon extension has a legitimate partnership with Groupon." (vs Honey's 146K/181K stores without consent)
- "You can remove the Safari extension anytime, independently from the app." (vs Honey's bundle-lock)
- "Your Bucks are yours. No silent expiration, no account-closure forfeiture, no fine print." (vs Honey's T&Cs)
- "You can cash out any balance above $1. It's your money." (vs Rakuten's $5.01 threshold)
- "Codes we apply come from verified merchant partnerships. We never scrape codes you type." (vs Honey's MegaLag Part 2 allegations)

## Why this matters economically

Trust is not a soft value. It has hard dollar consequences:

- Honey lost 8M Chrome users in 12 months. At Honey's peak valuation implied $235 per user acquisition cost [Data - $4B PayPal acquisition / 17M MAU], that's $1.88B of destroyed acquisition value. PayPal's 2025 public statements and the class action quantify the damage.
- Three affiliate networks (Rakuten, Impact.com, Awin) terminated Honey in 5 days. Each of those relationships took years to build.
- The class action is live, not dismissed. Honey's failure mode is now quantified in litigation.

For Groupon: the incremental cost of the trust-positive variant of each mechanic is tiny (~10-15% extra eng work on each card). The benefit is avoiding the Honey trajectory.

## Governance

- **Pre-launch review gate.** Before any loyalty mechanic ships, a named reviewer (legal + PM + Adam) confirms it passes the checklist above.
- **Quarterly T&C audit.** A dedicated PM owns the loyalty T&Cs and reviews them every quarter for language drift. Any change requires Adam + legal sign-off.
- **Annual mystery-shopper test.** External contractor uses Groupon's cashback system end-to-end; publishes findings. Groupon acts on findings within 30 days. This is the public-trust proof.
- **Transparent metrics publication.** Annually publish: % of earned Bucks actually paid out, % of merchants with direct / affiliate relationships vs listed, average tracking accuracy rate. Numbers are the anti-MegaLag vaccine.

## Success metrics

- **NPS on trust categories** ("I trust I will get paid", "The rewards are clear and fair") - target: top quartile of consumer finance apps
- **Class actions filed against Groupon re: loyalty program** - target: zero
- **Affiliate network terminations / warnings** - target: zero
- **External mystery-shopper audit pass rate** - target: >95%

## Risks

- **Over-engineering trust at the expense of speed.** If every mechanic goes through a 6-week review cycle, Groupon ships nothing. Mitigate with a default-approve checklist that 80% of decisions don't need senior review for.
- **Competitors under-invest in trust and ship faster.** Possible. Counter-argument: Honey's 12-month exodus is why trust is the moat. Speed without trust is how you become Honey.
- **Regulatory ambiguity.** "Industry standard" is a moving target. Stay ahead of it.

## Related

- **Every mechanic card references this one.** This card is the discipline that governs the others.
