# Mechanic Card 04 - Safari Extension Bundled With Groupon App
*Source: PayPal Honey via PayPal iOS app - plus trust-positive variant | 2026-04-21*

## What it is

The Groupon iOS app ships with a Safari Web Extension pre-installed. Users do not separately install the extension - it arrives silently during a regular Groupon app update. Activation requires one user action inside the Groupon app: tap "Deals" tab -> tap "Enable Safari extension" -> grant the iOS permission prompt. Once enabled, the Groupon extension surfaces at retailer checkouts automatically.

Honey's implementation inside the PayPal app is the reference [Data - help.joinhoney.com, paypal.com/us/cshelp/article/593; High]. Works in 10 countries (US, CA, UK, AU, DE, FR, NL, IT, ES, IN). Capital One Shopping also does this with Safari extension #2 Top Free Shopping app ranking [Data - Apple Community July 2025; Medium].

## Why it works

- **Zero-friction distribution.** Users don't install Groupon's extension deliberately - they install the Groupon app deliberately, and the extension comes with it.
- **Uses Apple's permission model.** iOS Safari Web Extensions are a native Apple product since iOS 15. Distribution via parent app is an Apple-sanctioned pattern.
- **Insulated from Chrome-style exodus.** Chrome users can uninstall a browser extension in one click. Safari iOS extensions are buried in Settings, and users who got them via app bundling often don't know they have them. This is why Honey's Chrome user count fell from 20M to 12M in 12 months while iOS user count has not visibly cratered [Opinion - high confidence, public tracking asymmetry].
- **Leverages Groupon's existing 30M+ app installs with 84% iOS share.** [Data - Groupon internal; High] That's ~25M iOS installs = addressable activation pool.
- **Defensible moat.** Once activated, the extension is always there at checkout. It becomes part of the user's shopping infrastructure, not a website they choose to visit.

## Critical design choice: the trust-positive variant

Honey's version of this has a **bundle-lock**: users cannot uninstall Honey independently of the PayPal wallet. They must uninstall PayPal entirely. German press (heise.de) has flagged this as a dark pattern, and it has been the subject of multiple Apple Community complaints. [Data - heise.de, discussions.apple.com; High]

**Groupon must build the trust-positive variant:** Safari extension bundled by default, but **independently removable**. Add a "Remove Safari extension" button inside Groupon app settings. This:
- Avoids heise.de-style dark-pattern criticism
- Protects Groupon from possible future App Store policy changes on tying
- Is actually a marketing asset ("unlike Honey, we let you remove it")
- Costs Groupon almost nothing - users who uninstall the extension were unlikely to use it anyway

## Activation rate assumption

**Publicly undisclosed by Honey, Rakuten, and Capital One Shopping.** Groupon sizing should assume **10-30% of app users activate** until we have our own data. [Estimate, Low confidence]

- Lower bound (10%): 2.5M active Safari extension users from 25M iOS installs.
- Upper bound (30%): 7.5M active Safari extension users.
- Middle (20%): 5M active Safari extension users.

Even the lower bound is larger than Genie's current ~981 installs. The order-of-magnitude difference is what makes this worth the investment.

## Rollout sequence

**Phase 1 - Minimum viable MVP (6-8 weeks):**
- US only
- 3-5 launch merchants (e.g. major retailers with existing Groupon coupon deals)
- Extension does ONE thing: auto-apply best coupon code at checkout, with on-screen confirmation "Groupon applied [code]"
- Optional: report to user whether they earned Bucks on the purchase
- NO silent cookie overwrites, NO private-code scraping, NO merchant-paid code suppression (per Honey class action)

**Phase 2 (Q3):**
- Expand merchant list to 500+
- Add Bucks earn surface in the extension
- Add a "Groupon is earning affiliate commission from this purchase; we pay it back as Bucks" disclosure banner (the trust-positive version of Honey's attribution hijacking)

**Phase 3 (Q4+):**
- Country expansion (CA, UK initially; match Honey's 10-country footprint over 12-18 months)
- Price comparison alerts (Capital One Shopping's universal-credit hook, Card 05)
- Droplist / watchlist (Honey's best uncontroversial feature)

## Specifically do NOT copy (from Honey)

- **Silent cookie overwrites / last-click hijack at checkout.** This is the criminal mechanic in the Honey class action. Groupon extension must NEVER overwrite an affiliate cookie it did not originate.
- **Merchant-paid coupon suppression.** If Groupon has a merchant agreement that restricts code visibility, disclose it inline at the point of use.
- **Scraping user-typed private codes.** MegaLag Part 2 allegation. Design the code database to accept only codes from verified merchant feeds or affiliate network feeds.
- **Bundle-lock (cannot uninstall extension without uninstalling app).** Per above - ship with independent removal.
- **Aggressive creator sponsorships as primary acquisition channel.** YouTube creators are now Honey's class-action plaintiffs. Diversify before scaling.

## Merchant coverage strategy

Honey's vulnerability in MegaLag Part 2: 181,000 stores listed in the extension, only 35,000 with actual affiliate partnerships. The rest were listed without merchant consent. This is structurally fragile and legally exposed.

**Groupon's better model:** only list merchants Groupon has active affiliate or direct relationships with. Groupon's network is narrower than Honey's (by design) but fully contracted. Lean into this as a trust differentiator: "every merchant in the Groupon extension has a legitimate affiliate or direct relationship with Groupon."

## Effort

- iOS Safari Web Extension build: **6-8 weeks** (mobile eng team, first time through)
- Groupon app integration + activation prompt UI: ~1 sprint
- Attribution + Bucks earn plumbing: ~1 sprint (reuses Bucks ledger from Card 02)
- App Store resubmission + review cycle: 2-4 weeks
- Launch merchants coupon sync: ~2 sprints

**Total: ~10-14 weeks to US MVP.**

## Success metrics

- **Install → activate conversion** in first 30 days after app update (target: 15-25% Phase 1)
- **Monthly active extension users** (ratio vs app MAU)
- **% of retailer checkouts where extension surfaces a code** (target: >60%)
- **Extension-assisted conversion rate lift** (extension users vs non-extension users)
- **Bucks earned per extension user per month**
- **Uninstall rate after first 30 days** (target: <15%; if higher, UX is broken)

## Risks

- **App Store policy evolution.** Apple could restrict Safari extensions in parent app bundles at any time. Mitigate by offering standalone extension as well.
- **EU Digital Markets Act.** Possible tying concerns. Mitigate with independent-removal button.
- **Merchant pushback.** If extension is seen as hijacking, merchants cut affiliate deals (as they did with Honey). Mitigate with clear attribution, no overwrites, public policy on code sourcing.
- **Registration / identity dependency.** Extension needs to know who the user is to credit Bucks. Anonymous coupons users must be onboarded into the loyalty identity layer first. This is the critical blocker for Q2.

## Related

- Mechanic Card 01 - Quarterly Payout Ritual (Bucks earned via extension drop quarterly)
- Mechanic Card 02 - Soft Currency 1:1 (Bucks is what the extension earns)
- Mechanic Card 05 - Trust Floor (guaranteed minimum Bucks per purchase)
- Mechanic Card 06 - Trust + Transparency (extension is the highest-scrutiny surface)
