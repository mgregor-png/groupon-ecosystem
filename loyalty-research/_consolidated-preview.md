# Loyalty Research - Consolidated Preview (2026-04-22)
*Generated 2026-04-22 for review. Combines final report + iteration outputs from Apr 21-22. Screenshots referenced below live in `competitor-mapping/` (upload folder separately to G Drive).*

---

## Table of contents

- Part 1 - Final merged report
- Part 2 - Retention uplift sizing model (shell)
- Part 3 - Fact-check v1 (load-bearing numbers vs primary sources)
- Part 4 - Competitor visual mapping - pattern analysis
- Part 5 - Competitor visual mapping - inventory
- Part 6 - Competitor visual mapping - gaps
- Part 7 - Signup-flow pre-auth captures
- Part 8 - Slickdeals partnership workstream
- Part 9 - Data gaps (internal + external asks)
- Part 10 - PostHog quick survey draft
- Part 11 - Daniel Rakuten ask draft
- Part 12 - AI funnel transparency appendix
- Part 13 - Mechanic cards (full detail)

---

## Part 1 - Final merged report

## Loyalty Mechanics Reverse Engineering for Groupon
### The $40M+ retention opportunity, delivered via Safari extension

*Prepared for: Adam Ward, Dusan, Rebecca, Groupon Product Leadership*
*Date: 2026-04-21 (rough-cut for Adam feedback, NOT final polish)*
*Authors: Martin Gregor with AI research assistance (see AI Funnel Appendix) + Rebecca's April 2026 draft*
*Classification: Confidential. Do NOT publish to public GitHub Pages.*

---

### Executive Summary

**The prize is not $4M in coupon commissions. It is $40M+ in retention uplift delivered as habit formation across coupons + core.** No team currently owns loyalty at Groupon, and every major competitor now has some form of cashback or rewards programme. This is the loyalty layer Groupon does not yet have, not a coupons-only Safari extension.

Six competitors were reverse-engineered for the mechanics that drive weekly habit: **Rakuten, Capital One Shopping, PayPal Honey** (deep), **Ibotta, RetailMeNot, Coupert** (scan). **Slickdeals** is treated as a separate partnership workstream, not a loyalty competitor. A Starbucks pure-loyalty benchmark was run and then dropped from the final recommendation because its habit engine (pre-loaded stored value plus mobile order) does not port to episodic, unpredictable-basket commerce - see §3.5 for the scope note. Key strategic findings:

1. **Stacking, not switching, is the dominant consumer behaviour.** [Rebecca §4.4] The four most-affiliated sites to groupon.com are RetailMeNot (affinity 1.000), Rakuten (0.924), Capital One Shopping (0.826), Honey (0.815) [Data - SimilarWeb Jan-Mar 2026 Worldwide; High confidence]. Groupon does not need to displace any of them. It needs to earn a place in the existing stack.
2. **Groupon's structural advantage is Bucks redeemable on local experiences.** [Rebecca §6.1] No cashback competitor can offer "earn from Nike, spend on a massage near you." This is unmatched and defensible.
3. **The PayPal Honey collapse (20M -> 12M Chrome users, 40% loss in 12 months) has created the largest acquisition window in category history.** [Data - 9to5Google Dec 31 2025; High] Three major affiliate networks (Rakuten Advertising, Impact.com, Awin) cut Honey off between Jan 12 and Jan 21, 2026. The vacuum is real and time-bound.
4. **Mechanics cluster into six cards worth copying, each with Groupon adoption cost.** The top four (quarterly payout ritual, 1:1 soft currency, Safari-extension-via-app-bundling, guaranteed floor) are load-bearing. Cards 5 and 6 (big visible cumulative earnings counter, trust-and-transparency discipline) govern how the first four are executed.
5. **The single biggest risk is trust collapse.** Honey's scandal chronology is a blueprint for what NOT to do. Every mechanic must be transparently user-positive. If a loyalty flywheel only works when users don't understand it, it is a liability waiting for a viral expose.

Recommended prioritisation ([largely validated by Rebecca's §6.4] and refined here):

- **Immediate (Q2 now):** Layer 1 monetisation, trust-floor mechanic (1% guaranteed back minimum), quarterly payout ritual + weekly anchor day (Mobile Monday / Free Mod Monday analogue). ~15 MD.
- **High conviction (Q2):** Genie rewards integration + Bucks (1:1 transparent soft currency, redeemable on local experiences). ~15-20 MD.
- **Strategic bet (Q2-Q3):** Safari extension bundled with Groupon iOS app (the Honey distribution playbook, minus the bundle-lock anti-pattern). Registration layer is a blocker. ~6-8 weeks.
- **Growth driver (Q3+):** Cashback PoC with merchant network depth as the differentiator. Tiered status for top 5% of spenders.

The rest of this document is the evidence, the mechanic cards, and the honest list of what Groupon cannot learn from this research (primary user interviews, internal crossover data, LTV uplift).

---

### 1. Market Context

Largely carried forward from Rebecca's draft with light edits. Skip ahead if already familiar.

#### 1.1 Market Size & Growth

- Global cashback apps market: ~$8-10B in 2024 [Data - growthmarketreports, credenceresearch; Rebecca refs 1, 2; High]
- Projected $22-23B by 2032-2033 at 9-12% CAGR [Data; Rebecca ref 1, 3; High]
- North America ~40% of global revenue; US alone ~$1.37B in 2025 [Data; Rebecca ref 3; Medium]
- 76% of shoppers prefer stores offering cashback or points [Data; Rebecca ref 16; Medium]
- Cashback platforms shown to increase repeat purchases by up to 40% [Data - industry aggregate; Rebecca ref 17; Medium-Low confidence on exact figure]

#### 1.2 Competitive Landscape Summary (2026 state)

Quick reference - full per-competitor detail in §3 and mechanic cards.

| Competitor | Est. User Base | Reward Currency | Payout Method | Sign-Up Bonus | Extension |
|---|---|---|---|---|---|
| **Rakuten** | 17M+ US members [Data, High] | Cash / Amex pts / Bilt pts | Quarterly (PayPal/cheque) | $50/$50 referral until Jun 30 2026 | Chrome, Safari, Firefox, Edge |
| **PayPal Honey** | 12M Chrome (down from 20M peak) [Data, High] | Honey Gold points | PayPal balance / gift cards | 500 Gold ($5) conditional | Chrome, Safari iOS bundled with PayPal app |
| **Capital One Shopping** | 6-10M [Data, Medium] | Shopping Credits (1:1 = $1) | Gift cards only (~50 retailers) | $40-80 install + 90-day retention, YMMV | Chrome, Safari, Firefox, Edge |
| **RetailMeNot** | 100M+ social reach | USD cashback (1% floor Feb 25 2026) | PayPal / Venmo, ~45 days | None standard | Mobile Safari only |
| **Ibotta** | 54M registered, 20.4M Q4 redeemers [Data, High] | USD cashback | PayPal / Venmo / gift cards, $20 min | $5-20 welcome | Browser ext, app, IPN (B2B2C) |
| **Coupert** | 8M weekly active claimed [Data, Medium] | Cash + Gold Coins | PayPal / gift cards / debit ($1 first) | $20 new user | Chrome, Edge, Firefox, Safari |

[Rebecca's ref indices: see §10. My additional refs: see §10 continuation.]

---

### 2. The Strategic Frame: Stacking, Not Switching

**This is the single most important strategic insight in the research, carried over from Rebecca §4.2-4.4.**

#### 2.1 The SimilarWeb Audience Affinity Data

[Rebecca's primary data from SimilarWeb Pro Similar Sites, Jan-Mar 2026, Worldwide, exported 20 April 2026]

All four cashback competitors profiled rank in Groupon's top 8 most-affiliated sites:

| # | Domain | Affinity | Note |
|---|---|---|---|
| 1 | retailmenot.com | 1.000 | Perfect overlap - same user base |
| 3 | rakuten.com | 0.924 | Deep overlap |
| 7 | capitaloneshopping.com | 0.826 | Strong overlap |
| 8 | joinhoney.com | 0.815 | Strong overlap |

Experiences cluster (TripAdvisor, Yelp, Expedia, Viator, Eventbrite) also appears in the top 20, validating the Bucks-on-experiences thesis. Walmart, Sam's Club, Costco in the top 20 confirm value-seeking mainstream mindset. Ibotta and Coupert do NOT appear in the top 37 - they serve partially different segments.

#### 2.2 The Stacking Pattern

Groupon's existing users are already visiting RetailMeNot, Rakuten, Capital One Shopping, and Honey. They are NOT choosing one. Multiple industry guides explicitly recommend running 2-3 extensions together [Data - WalletGrower 2026 guide, Rebecca ref 39]. 

Capital One Shopping shows 81% direct traffic and 7.8% referral share - users arrive via extension triggers and cross-platform referrals, not by searching "cashback apps" and choosing one [Data - SimilarWeb Mar 2026].

**Strategic implication**: Groupon does not need to displace a competitor. Groupon needs to be visible and valuable enough to earn a slot in the user's existing savings stack. The Safari extension bundled inside the Groupon app is positioned for this: zero friction install, no competing extension to displace, and a unique reward currency (Bucks redeemable on local experiences).

**Counter-nuance I'd add to Rebecca's framing**: stacking benefits Groupon only if Groupon's mechanic is additive to the existing stack. If Groupon's cashback rate is structurally below Rakuten's (and it will be - see §3.1.17), the cashback itself cannot be the hook. Bucks-on-local-experiences IS the additive value. The mechanic must be positioned as "earn Groupon Bucks from Nike, spend on a spa day" not "better cashback than Rakuten." [Opinion, High confidence]

---

### 3. Competitor Deep Dives

Structured as competitor -> mechanics -> habit drivers ranked -> weaknesses -> Groupon adoption.

#### 3.1 Rakuten - the category volume leader, but thin-margin and saturating

**Core state (2026):**
- 17M+ US members, $4.6B cumulative cashback paid since 1998 [Data - rakuten.com/about, Wikipedia; High]
- US rakuten.com global rank #237 (up from #251 three months prior) [Data - SimilarWeb Mar 2026; High]
- Traffic +15.39% MoM Mar 2026 [Data; High]
- Rakuten International segment FY2024: $2.04B revenue (+8.5% YoY), $48.5M op income = **2.4% operating margin** [Data - Rakuten Group Feb 14 2025 release; High]
- US Rewards revenue "flat" in FY2025 [Data - Rakuten Group Q3 FY2025 release Nov 13 2025; High]

**Mechanics that matter for Groupon:**

1. **Big Fat Check quarterly payout.** Fixed dates Feb/May/Aug/Nov 15. $5.01 minimum threshold. Methods: cheque, PayPal, Amex MR points (1:100), Bilt points (1:100 elite / 0.5:100 non-elite). [Data - rakuten.com/blog; High] The dopamine-anticipation engine.
2. **Mobile Monday.** Weekly boosted cashback in-app only. Forces weekly app open. [Data - rakuten.com/double-cash-back; High] This is the pull mechanic that drives WEEKLY habit - the single thing Capital One Shopping does NOT have, and the single thing Groupon needs.
3. **Double Cash Back flash events.** 24-hour to week-long promotional events between quarters. Creates sub-quarterly FOMO. [Data; High]
4. **$50/$50 symmetric referral bonus.** Both sides. Active until Jun 30 2026. Historical baseline $30. [Data - The Points Guy Apr 2026; High] This suggests viral CAC is their primary growth lever.
5. **Rakuten+ paid tier (launched Nov 12 2025).** $100/yr, invite-only, 10% cashback at premium/luxury stores (Sephora etc). **Too new to validate** - no adoption data disclosed. Likely a margin-defense move. [Data + Opinion; Medium] Skip until proven.

**Habit drivers ranked:**

| Rank | Driver | Copyability for Groupon |
|---|---|---|
| 1 | Quarterly "Big Fat Check" | HIGH - ~1 sprint |
| 2 | Mobile Monday weekly | HIGH - ~1 sprint + push |
| 3 | $50/$50 referral | HIGH - but expensive CAC |
| 4 | Cumulative earnings counter | HIGH - ~0.5 sprint |
| 5 | Double Cash Back events | HIGH - admin tooling |
| 6 | Points currency optionality (Amex/Bilt) | MEDIUM - partnership BD |
| 7 | Card-linked in-store | HIGH effort - PCI + network deals |
| 8 | Rakuten+ paid tier | LOW - skip |

**Rakuten's #1 weakness (surface aggressively): tracking reliability.** Every negative-review cluster on Trustpilot 4.6/5 with 5% 1-star (36,643 reviews), Reddit, ConsumerAffairs points to missed cashback on large purchases, denied pending balances, and no human customer-service escalation path. Active class action: **Oganesyan v. Rakuten USA, filed Feb 13 2025 (ND Cal)** [Data - Justia docket].

**Android is broken.** iOS 4.8/5 on 360K reviews vs Google Play 3.4/5 on 73K reviews - a 1.4-point gap [Data - app stores July 2025]. For Groupon (~84% iOS base) this matters less but is a cautionary signal.

**What Groupon should NOT copy from Rakuten:**
- Paid premium tier ($100/yr for 10%). Too new, unproven. Wait 12 months.
- Manual activation before every purchase. Honey's auto-apply wins on UX.
- Mailing address at signup (relic of paper-check era).
- $5.01 minimum payout threshold (anti-customer - see Coupert's $1 instead).
- Tolerating a 5-10% tracking failure rate (single biggest churn driver).
- Opaque "loop of articles" customer service.
- Android under-investment.

#### 3.2 Capital One Shopping - the soft-currency blueprint

**Core state (2026):**
- 6-10M users (6M+ Chrome, 10M+ total claimed) [Data - Chrome Web Store + company; Medium]
- 66.7M monthly visits to capitaloneshopping.com (+58% MoM Mar 2026) [Data - SimilarWeb; High]
- 81.76% direct traffic, 97.21% US, 60% female audience, age 25-34 [Data; High]
- #2 Top Free App (Shopping) on iOS [Data - Apple Community July 2025; Medium]
- 100,000+ retailers supported [Data; High]

**Mechanics that matter for Groupon:**

1. **Shopping Credits soft currency: 1 credit = $1.** 1:1 transparent. NO obfuscation. [Data - Capital One help center; High] This is the Bucks inspiration Dusan referenced. The clarity is load-bearing - the moment Groupon obfuscates the ratio ("1000 Bucks = ???"), trust erodes.
2. **The $45 install incentive is real but not fixed at $45.** It has fluctuated: $10 (2020) -> $200 (Dec 2023 peak, days only) -> $40-80 (2024-2026 norm). Current (Apr 2026) headline: **$80/$80 referral, both sides, with 90-day install-retention requirement** [Data - Doctor of Credit, Frequent Miler; High]. One documented variant: "$45 after $15 qualifying purchase within 90 days" [Data - PhatWallet]. US-only, heavily YMMV-targeted.
3. **90-day retention gate on the welcome bonus.** This is the more interesting LTV signal than the dollar amount. It converts bonus-hunters into habit-formed users.
4. **Gift-card-only redemption at 50+ rotating retailers.** NO cash-out, NO bank deposit, NO statement credit. [Data; High] Rotating inventory is intentional - Lowe's, Home Depot, Macy's, Walmart, Safeway have all been removed at various points. Currently available (Feb 2026): Marriott Bonvoy, eBay, Uber/Uber Eats, Petco, **Groupon**, Zappos, Nike, Kohl's.
5. **No paid tier, no banking tie-in required.** Standalone loyalty product by design - keeps it a clean acquisition funnel for Capital One's actual revenue product (credit cards). [Data; High]
6. **Price comparison universal credit.** On Amazon product pages, extension alerts "this is $15 cheaper at Walmart." Works even when no coupon/reward exists. [Data - Wikibuy DNA from 2014; High]
7. **Watchlist + price-drop alerts.** Pull-back-to-app mechanic. Email + push on price drops. [Data; High]

**Critical reframe of the $45 anchor (for Groupon's sizing model):**

The $45-80 payment is NOT per-user monetisation inside Capital One Shopping. It is an **acquisition bribe underwritten by Capital One Financial Corp's credit-card cross-sell LTV** (where real LTV is $500+). Capital One can afford it. Groupon's equivalent CAC tolerance depends on whether Groupon has an analogous downstream revenue product to cross-sell into. Without one, $45/install is a multi-year payback at ~$5-15/yr per user (6% affiliate commission on $8-25 monthly basket). [Opinion - Medium-High confidence]

**Capital One's critical gap for Groupon's goal: it is reactive-only.** The extension surfaces when you shop. No weekly habit loop. No streaks. No daily reveal. **If Groupon wants WEEKLY habit, Capital One's model is insufficient on its own.** Must add pull mechanics (weekly anchor day, daily deal reveal, time-bound challenges). This is where Rakuten's Mobile Monday becomes the reference.

**Capital One's weaknesses (surface aggressively):**
- Trustpilot 1.3/5 vs App Store 4.9/5 - power-user tracking-failure complaints vs prompt-timed "reward posted" reviews [Data; High]
- Post-confirmation reward denials (top churn driver)
- Phone-number conflict redemption bugs
- **$4M class-action settlement (Dec 2025 preliminary approval)** for affiliate cookie hijacking / silent last-click overwrite [Data - ABA Banking Journal, classaction.org; High]
- Rotating redemption inventory removing top brands (Walmart/Home Depot/Macy's/Lowe's)

#### 3.3 PayPal Honey - the Safari distribution playbook AND the cautionary tale

**Core state (2026):**
- Chrome users: **12M (Dec 31 2025), down from 20M peak late 2024 - 40% loss in 12 months** [Data - 9to5Google Dec 31 2025; High]
- iOS App Store: 4.8/5 on 2,400+ reviews [Data - App Store; High]
- Class action live: **In Re PayPal Honey Browser Extension Litigation, N.D. Cal. Judge Beth Labson Freeman.** Second Amended Consolidated Complaint filed Jan 5 2026, 101 pages, 10+ creator plaintiffs including MrBeast-adjacent properties [Data - Cohen Milstein, Orrick; High]
- **Jan 12-21 2026: three major affiliate networks cut Honey off.** Rakuten Advertising (full removal, ~2,000 partners cut), Impact.com (removed from Discovery Marketplace), Awin (payments suspended, blocked from new advertisers) [Data - ppc.land, Affiverse, hellopartner.com; High]
- PayPal public statement Jan 12 2026: "Problematic code in Honey, have disabled it" [Data - Wikipedia; High]

**The distribution playbook (copy this):**

1. User installs PayPal app on iPhone (for the wallet - PayPal has ~430M active accounts globally).
2. PayPal app contains the Honey Safari extension as a **bundled component** - installed silently during app update.
3. User opens PayPal app -> "Deals" tab -> is prompted to enable Honey Safari extension.
4. Enabling requires granting Safari extension permissions (access to all websites). This is the only user-action gate.
5. Once enabled, Honey auto-pops in Safari at supported retailer checkouts.
6. Available in 10 countries: US, CA, UK, AU, DE, FR, NL, IT, ES, IN.

**Why iOS is insulated from the Chrome exodus:** users who got Honey via PayPal app bundling often don't know they have it. They cannot easily "uninstall Honey" the way a Chrome user can with one click. [Opinion - high confidence] This is the asymmetry that matters for Groupon.

**Groupon implication:** Groupon app (~30M installs, 84% iOS) -> Safari extension pre-installed but not active -> explicit activation prompt in-app. This replicates the most defensible piece of Honey's moat. Groupon has the ADDITIONAL asset that Honey needs to manufacture: contracted direct merchant relationships (181K stores showed up in Honey but only 35K had affiliate partnerships - that's the structural fragility MegaLag Part 2 exposed [Data - MegaLag Dec 2025; High]).

**The cautionary tale (do NOT copy):**

MegaLag's Dec 2024 video exposed three mechanisms: (1) commission hijacking via last-click cookie overwrite at checkout, (2) merchant-paid suppression of better codes, (3) (from MegaLag Part 2 Dec 2025) scraping user-typed private codes and redistributing. Chrome exodus in 12 months: 20M -> 17M (Jan 3 2025, 3M lost in 2 weeks) -> 16M (Mar 2025) -> 14M (Jul 2025) -> 13M (Dec 22 2025) -> 12M (Dec 31 2025).

**The meta-lesson for Groupon:** every mechanic must be transparently user-positive. If a loyalty flywheel has a mechanic that only works when users don't understand it, that mechanic is a liability waiting for a viral expose. Specifically:

- NO silent cookie overwrites / last-click hijack
- NO merchant-paid code suppression
- NO scraping user-typed private codes
- NO bundle-lock (let users uninstall Safari extension independently of Groupon app - that is the trust-positive version of the bundle)
- NO 60-90 day pending windows (Coupert does 7-15 days and advertises the difference)
- NO 365-day inactivity forfeiture with silent expiration
- NO "not your property, not money, no value prior to redemption" T&C language

**What Honey still does well:** Droplist price tracking, referral simplicity ($5 cash per friend capped at $1,000), auto-pop at checkout UX, country breadth for Safari iOS, brand recognition (even post-collapse).

#### 3.4 Tier 2 scan - all three under structural pressure

Important cross-competitor pattern from the research: **Ibotta, RetailMeNot, and Coupert are all under structural pressure, not stable benchmarks.** Treat them as declining or niche, not as threats to match feature-for-feature.

**Ibotta** has pivoted from consumer app to B2B2C infrastructure. The IPN (Ibotta Performance Network) powers Walmart Cash, Dollar General, Family Dollar, Schnucks, Instacart (Nov 2024), DoorDash (Q2 2025). Q4 2025 revenue mix: 64% third-party publishers, 25% D2C. FY2025 revenue $342.4M, down 7% YoY. D2C revenue fell 25% to $139.9M. Redemption revenue per redemption $0.83, down 5% YoY - classic B2B2C dilution. [Data - Ibotta investor relations Q4 2025, Motley Fool transcript; High]

*Groupon lesson from Ibotta:* the B2B2C distribution pattern. Ibotta solved "stop begging for app installs" by embedding offer logic inside partners' owned wallets. Groupon could plug cashback into partner checkout flows rather than forcing users through the Groupon app - but this is a later-phase move, after Bucks are working inside Groupon's own surface.

**RetailMeNot's 1% guaranteed cashback floor (Feb 25 2026) is defensive, not innovative.** Ziff Davis Tech & Shopping segment revenue fell 18% in Q4 2025, with a $25M YoY drop in affiliate commissions attributed to AI-displaced search traffic. Management guided double-digit decline H1 2026. Stock fell 11-13% on Q4 miss. [Data - Ziff Davis Q4 2025 earnings Feb 2026; High] The 1% floor is buying back attribution from an eroding traffic base.

*Groupon lesson from RetailMeNot:* guaranteed floor as a trust primitive. "You will always get at least X% back" removes shopping-around from the consumer's decision tree. Cross-applied to Bucks, this becomes: "any purchase through Groupon always earns at least X Bucks, no matter what." This is a defensible positioning against competitors who have variable rates.

**Coupert** is a bootstrapped 8-11-person operation (Dover DE + Kowloon HK) with ~$1.2M revenue [Data - Latka; Estimate, single source]. Two mechanics matter: $1 withdrawal floor via Visa/Mastercard with 2% + $0.50 processing fee, and 72.92% claimed auto-apply success rate vs Honey's 33% (self-reported, not independently audited). [Data - Coupert research; Medium with integrity caveat] Trustpilot shows mixed reviews including $600+ unpaid-balance complaints.

*Groupon lesson from Coupert:* **the $1 floor as an activation trigger.** Let the user cash out at any amount with a small fee. Converts cashback from a distant future reward into an immediately usable one. Solves the "abandoned balance" trust problem that plagues every reward system. Elegant, cheap to implement.

**One data-gap flag:** the intake referenced "Honey shutdown" context for Coupert migration. Researched sources did NOT confirm a Honey shutdown - Honey's PayPal-era degradation is what sources describe. Re-verify before relying on this in exec messaging. [Data gap - flag from agent A4]

#### 3.5 Scope note - pure-loyalty benchmark deferred

A Starbucks teardown was run as a pure-loyalty benchmark (see `raw/tier2-scan-and-starbucks-benchmark.md` for audit trail). The honest finding: Starbucks' habit engine is **pre-loaded stored value + mobile order**, not stars, and it does NOT port to Groupon because coffee is a daily consumable with deterministic price while Groupon purchases are episodic and unpredictable. The benchmark has been **dropped from this final report** to keep the recommendation set focused on mechanics that actually apply. Marriott Bonvoy was excluded earlier for the same reason (wrong frequency cadence).

The generic mechanics that would have been derived from Starbucks (weekly anchor, time-bound challenges, tier status for top spenders) either remain in the recommendation set with different attribution (Rakuten's Mobile Monday for the weekly anchor) or are deferred to later phases.

---

### 4. Mechanic Cards - What to Copy, in What Order, at What Cost

Each mechanic has its own card in `mechanic-cards/` with fuller detail. Summary table here.

| # | Mechanic | Source | Why it works | Groupon cost | Priority |
|---|---|---|---|---|---|
| 1 | **Quarterly payout ritual** | Rakuten Big Fat Check | Dopamine anticipation 4x/yr; $5 soft-threshold drives breakage; builds brand ritual | LOW (~1 sprint) | Q2 now |
| 2 | **1:1 transparent soft currency (Bucks)** | Capital One Shopping Credits | Clarity = trust; gift-card-only preserves unit economics; 15-30% breakage | MED (~2 sprints + finance model) | Q2 |
| 3 | **Weekly anchor day** | Rakuten Mobile Monday | Forces weekly app-open habit | LOW (~1 sprint + push infra) | Q2 now |
| 4 | **Safari extension bundled with Groupon app** | Honey via PayPal app (with trust-positive variant: independent uninstall) | Zero-friction distribution; 84% iOS base insulated from Chrome exodus pattern | MED-HIGH (mobile eng + Safari ext build) | Q2-Q3 |
| 5 | **Trust floor (1% guaranteed back)** | RetailMeNot Feb 2026 + Coupert $1 withdrawal | Removes shopping-around; activates on first small purchase | LOW (~0.5 sprint + merchant margin tuning) | Q2 now |
| 6 | **Big visible cumulative earnings counter** | Rakuten ("You've earned $127.43") | Sunk-cost psychology; users return to protect/grow balance | LOW (~0.5 sprint) | Q2 |
| 7 | **Symmetric referral $X/$X** | Rakuten $50/$50 + Honey $5 cash | Viral CAC | MED (funded by growth budget) | Q2-Q3 |
| 8 | **Points-currency optionality** (partner with Amex/Chase/Bilt) | Rakuten | Locks in affluent users | HIGH (partnership BD) | Q4+ |
| 9 | **B2B2C cashback embedded in partner wallets** | Ibotta IPN | Zero app-install dependency | HIGH (BD + API) | 2027 |
| 10 | **Card-linked in-store cashback** | Rakuten RCLON | Cross-channel presence | HIGH (PCI + network deals) | 2027 |

**Not to copy (explicit):**
- Paid premium tier (Rakuten+ $100/yr) - unproven
- Bundle-lock that prevents independent uninstall (Honey) - anti-consumer
- Silent cookie overwrites / last-click hijack (Honey class action) - criminal mechanic
- Opaque merchant ranking / merchant-paid code suppression (Honey MegaLag Part 1)
- Scraping user-typed private codes (Honey MegaLag Part 2)
- 60-90 day pending windows (Honey) - Coupert does 7-15 days
- 365-day inactivity forfeiture silent expiration (Honey)
- "Not your property, not money, no value prior to redemption" T&C language (Honey)
- Aggressive mid-program devaluation of any established rate (general loyalty anti-pattern)
- $5+ minimum payout threshold (Rakuten $5.01 - anti-customer)
- Manual activation before every purchase (Rakuten) - auto-apply wins
- Opaque "loop of articles" customer service with no escalation (Rakuten)
- Android under-investment (Rakuten 1.4-point gap)
- Post-confirmation reward denials (Capital One top churn driver)

---

### 5. User Overlap, Switching Behaviour, and the Research Programme

**This section is essentially Rebecca §4.5, which is already investment-grade and should stand as-is. Summarising for continuity; full detail in Rebecca's original (see raw/rebecca-draft.md).**

Rebecca's recommended 5-phase research programme to move from directional evidence to investment-grade confidence:

- **Phase 1 (1-2 weeks, minimal cost):** Desk research. Semrush Audience Overlap dashboard ($289/mo or 7-day free trial), SimilarWeb Pro audience overlap, keyword gap analysis.
- **Phase 2 (3-4 weeks, $15-25K):** Quantitative survey of 1,000-2,000 Groupon coupons page visitors. Intercept via Qualtrics or Hotjar. Conjoint analysis on Bucks vs cash vs gift card.
- **Phase 3 (2-3 weeks, internal):** Behavioural analysis of existing data. Genie install-to-purchase analysis (981 Genie installs), coupons-to-deals cross-purchase analysis, Bloomreach email cohort test.
- **Phase 4 (4-6 weeks, $10-20K):** Qualitative depth interviews. 15-20 heavy cashback users (using 2+ platforms, earning $100+/yr).
- **Phase 5 (ongoing, built into PoC):** Live A/B testing. Extension activation incentives, stacking behaviour tracking, Bucks redemption funnel.

I'd add **Phase 1.5**: independent audit of at least one month's mystery-shopper activity to stress-test tracking reliability across Rakuten, Capital One Shopping, and Coupert. Tracking failure is the #1 churn driver across all three and Groupon must out-perform on this specific dimension from day one.

---

### 6. Executive Due Diligence Checklist

**Carried from Rebecca §5, selected high-leverage items with confidence ratings applied.**

#### 6.1 Is the market opportunity real and big enough?

- Global cashback market $8-10B in 2024 growing to $22-23B by 2033 [Data, High]
- 76% of shoppers prefer cashback-offering stores [Data - Rebecca ref 16, Medium]
- 84% of Groupon app users on iOS [Data - Groupon internal, High]
- Honey's 8M-user exodus = the largest category acquisition window in years [Data - 9to5Google, High]
- **Red flag to watch:** the underlying category is under pressure. Rakuten flat revenue FY2025, Ziff Davis Tech & Shopping -18%, Ibotta revenue per redemption falling -5% YoY. Growth comes from B2B2C distribution and displacement of declining players, not category expansion. [Opinion, Medium]

#### 6.2 Will users actually adopt this?

- Groupon users already stack 2-3 cashback extensions (affinity data) [Data, High]
- Bucks redeemable on local experiences is genuinely unique [Opinion, High]
- Safari extension bundled inside the Groupon app has a distribution path validated by Honey [Data, High]
- **BUT: activation rate of bundled Safari extensions is NOT publicly disclosed by Honey or Capital One Shopping.** We should assume moderate (10-30% of app users) until proven otherwise. [Data gap / Estimate, Low confidence]

#### 6.3 Do the unit economics work?

- **This is the largest open question.** [Data gap]
- Rakuten's 2.4% International operating margin suggests the free tier is near break-even. Rakuten+ $100/yr paid tier launched Nov 2025 is a signal even the category leader can't make enough on the free tier alone.
- Capital One Shopping almost certainly runs at break-even on Rewards P&L in isolation, making up the difference via credit-card cross-sell. Groupon's equivalent cross-sell product is Groupon deals/experiences.
- **Required internal data: average commission per click-out by merchant category, redemption rate vs breakage on Groupon Bucks (if any exist today), Genie retention curve, coupons-to-deals crossover rate.** See `data-gaps.md`.

#### 6.4 Can we actually build and ship this?

- Mobile eng for Safari extension: medium effort, ~6-8 weeks for iOS-first MVP
- Bucks ledger + redemption: medium effort, dependent on registration layer
- Safari extension bundling in Groupon app: requires App Store resubmit; US+IDN+EU rollout staggered
- **Critical dependency: identity / registration layer.** All loyalty mechanics require logged-in state. Current coupons page is largely anonymous. This is Phase 1 of the loyalty roadmap, not Phase 2.

#### 6.5 Competitive dynamics and timing risks

- Honey acquisition window is time-bound. Every month Groupon delays is a month Coupert, Capital One Shopping, and Rakuten absorb the displaced users. [Opinion, High]
- AI-assistant displacement of shopping search (RetailMeNot Q4 2025 -18%) is a category-wide risk. Groupon's merchant direct relationships are the buffer - no one can replace a Local deal at a specific restaurant.
- Rakuten+ paid tier, if it proves traction (public data due early 2026), may reshape the economics of the free tier.

#### 6.6 How do we measure success?

Leading indicators (weekly):
- Safari extension activation rate (installed -> active)
- Weekly active users with a Bucks balance > $0
- Mobile Monday opt-in cadence
- Bucks earned per active user per week

Lagging indicators (monthly/quarterly):
- Coupons-to-deals conversion lift (Bucks-bridge hypothesis)
- Retention curve delta (cohort with Bucks vs cohort without)
- Quarterly payout event transaction spike
- 90-day-post-install retention (matching Capital One Shopping's gate)

#### 6.7 Internal data to pull immediately

Carried forward verbatim from Rebecca §5.7 plus my additions. See `data-gaps.md` for the consolidated list and owners.

---

### 7. Implications for Groupon's Strategy

#### 7.1 Groupon's unique position

Unlike every competitor analysed, Groupon is the only platform that can bridge online coupons to local, in-person experiences. Rakuten bridges coupons to retail rewards. Ibotta bridges receipts to cashback. Only Groupon can offer "Earn Bucks from Nike, spend them on a massage near you." This is an unmatched strategic moat. [Rebecca §6.1]

#### 7.2 Validation of proposed initiatives

**Layer 1 - Monetise (Immediate, Q2 now).** Every competitor monetises coupon traffic through multiple channels. Groupon's 30M annual sessions are an under-monetised asset. ~8 MD. Zero dependencies. [Rebecca §6.2]

**Layer 2 - Genie + Rewards (High conviction, Q2).** Extension users are demonstrably the highest-value segment. Capital One's $45-80 acquisition cost, Rakuten's $50 referral, and Honey's $235 per-user PayPal acquisition price (at peak) all confirm high extension-user LTV. Honey's scandal has created a unique acquisition window. ~15 MD. [Rebecca §6.2]

**Layer 3 - Safari Extension bundled with Groupon app (Strategic bet, Q2-Q3).** Honey and Rakuten both operate iOS Safari extensions today, confirming App Store feasibility. With 84% of Groupon app users on iOS, this is the largest untapped engagement channel. 2-week spike + registration layer. [Rebecca §6.2]

**Cashback / Bucks PoC (Growth driver, Q3+).** Every major competitor now operates cashback. Not having it is a competitive disadvantage. Groupon Bucks redeemable on local experiences is structurally advantaged. Requires registration layer first. [Rebecca §6.2]

#### 7.3 Risks and considerations

- **Regulatory scrutiny of extensions.** Honey scandal led to Chrome Web Store policy change (Mar 2025) and multiple class actions. Design with transparent affiliate practices from day one. [Rebecca §6.3]
- **User extension fatigue.** Bundling Safari inside the Groupon app (as proposed) removes this friction. [Rebecca §6.3]
- **Payout economics.** Competitors paying cash face ongoing cost pressure. Groupon Bucks, redeemable only in-app against deals, offer structurally lower cost-of-reward while driving core business. [Rebecca §6.3]
- **Competitive response.** If Groupon's Safari extension gains traction, expect Rakuten and Honey to pursue deeper app integrations. Speed of execution matters. [Rebecca §6.3]
- **Trust-collapse risk.** Every mechanic must be transparently user-positive. The Honey chronology is the cautionary tale. If Groupon adopts ANY mechanic that only works when users don't understand it, instrument it honestly and publicly before launch. [My addition - High priority]

#### 7.4 Recommended prioritisation

| Timing | Initiative | Effort | Rationale |
|---|---|---|---|
| **Immediate (Q2 now)** | Layer 1 monetisation (display ads, deal cross-sell, Genie CTA) + 1% trust floor + Mobile Monday / weekly anchor | ~8 MD + ~3 MD | Zero dependencies. Every competitor does this. Trust floor is cheap and differentiates. |
| **Q2** | Genie rewards integration + Bucks 1:1 soft currency + quarterly payout ritual + registration layer | ~15-20 MD | Honey window closing. Cross-channel rewards data shows +110% revenue uplift for extension+rewards users. [Rebecca §6.4] |
| **Q2-Q3** | Safari extension bundled with Groupon iOS app + $X/$X referral | 6-8 weeks + growth budget | 84% iOS base, validated by Honey/Cap One feasibility. Registration layer must land first. |
| **Q3** | Tier structure (top 5% spenders) + challenge engine + symmetric referral | 10-15 MD | Retention of top cohort. Short-horizon pull between quarterly payouts. |
| **Q3+** | Cashback PoC at scale + Double Cash Back flash events | 20+ MD | Groupon's Bucks-on-local-experiences differentiator. |
| **Q4+** | Points currency partnership (Amex/Chase) | Partnership BD | Lock-in for affluent users. Long lead time. |
| **2027** | B2B2C distribution (Ibotta IPN model) + in-store card-linked offers | Strategic bet | After Bucks flywheel is proven. |

---

### 8. Slickdeals - Separate Partnership Workstream

**Slickdeals is NOT a loyalty competitor. It is a UGC deal-hunting community that Dusan has flagged as a potential partner for replacing Goods on core Groupon. This section summarises the standalone feasibility analysis at `partnership-feasibility-slickdeals.md`.**

#### 8.1 Recommendation: Conditional Go on Option B (90-day embedded pilot), NOT full Goods replacement

**Dusan's thesis that Slickdeals is the #1 partner candidate is defensible IF the goal is "fill the Goods surface with credible physical-goods deals fast." But the framing "replace Goods" misdiagnoses the problem.**

- Goods failed on inventory/fulfilment economics, not on curation.
- A UGC feed solves demand-side deal discovery, which is a different problem.
- The community belongs to slickdeals.net. If the partnership ends, Groupon has zero residual audience - that's the DEAL BREAKER from the brief.

#### 8.2 Core facts (2026 state)

- **Ownership:** Goldman Sachs Merchant Banking + Hearst since June 2018 ($500M deal). 8-year hold suggests exit within 12-24 months. Possible buyers: Amazon (owns Woot), Ziff Davis, Rakuten. [Data - Bloomberg, PR Newswire, Fried Frank; High]
- **Revenue:** $35-50M estimated 2025; working range $45-55M for 2026. [Data/Estimate, Medium]
- **Traffic:** 12M MAU, 40% DAU/MAU (excellent), 25M monthly visitors, +5% MoM Mar 2026. [Data - SimilarWeb; High]
- **Audience:** 63% male, 70% aged 18-44, higher income, US-only. **Inverse gender skew vs Groupon.** [Data - Slickdeals corp, SimilarWeb; High]
- **Economics:** Affiliate commissions 1-8.5% of GMV; SD holds negotiating leverage in any deal. [Data - enactsoft, HBS case; Medium-High]
- **AI shipping velocity:** March 2025 iOS redesign, AWS SageMaker personalisation rolled out (7% merchant click lift at re:Invent 2025). [Data - AWS re:Invent 2025 SMB206; High]

#### 8.3 Five honest findings

1. **No public precedent for a white-label SD feed on a retail partner's core site.** Either strategic whitespace or a signal that partners prefer direct affiliate networks.
2. **The community is non-transferable.** Rent, not own. If partnership ends, the inventory ends.
3. **SD's upper-funnel pivot shifts incentives away from maximising affiliate click-out.** Neville Crawley's stated strategy is to convert MAU to DAU and go brand-advertising heavy. Partner incentives may diverge from Groupon's.
4. **Dusan's framing misdiagnoses the Goods problem.** Fulfilment, not curation.
5. **Amazon (owns Woot) is the most likely SD buyer.** Change-of-control risk is real.

#### 8.4 Partnership conditions (must all be true)

- Pilot scope: 90 days, single Goods sub-category (e.g. consumer electronics), <5% of Goods surface
- 30-day termination clause, no exclusivity
- Change-of-control right to terminate on SD acquisition
- 24-month commission rate protection
- Light co-branding only ("Powered by Slickdeals"), not full SD takeover
- Groupon-side moderation filter (only deals with >N community votes, no expired)
- Metric gate: minimum $X revenue/mo + Y% CTR lift for renewal
- Parallel in-house "Groupon Deals Feed" project as alternative

#### 8.5 Do not

- Sign a co-branded storefront (Option C) before Option B pilot succeeds.
- Acquire - Groupon market cap ~$600M-$900M; SD likely commands $700M-$1.2B+. Transformative capital commitment without strategic rationale.
- Let "replace Goods" framing drive the contract structure.

---

### 9. Data Gaps, Red Flags, Yellow Flags

#### 9.1 Data gaps (consolidated from all agents + Rebecca + my additions)

Internal gaps → owner → path to fill. See `data-gaps.md` for the operational list.

- **Groupon coupons page visitors ↔ Groupon deal purchasers crossover** → Mark Brenda → Internal BI (2-3 days work)
- **Groupon Bucks (if any today) issuance, redemption, breakage, time-to-redeem** → Finance/loyalty data owner → existing systems
- **84% iOS user base retention curve, purchase frequency, LTV uplift for Genie installs** → Ernesto's team → Genie analytics + internal BI
- **Push opt-in rate + engagement on current app** → Mobile analytics owner → push platform
- **Non-monetised session rate (% of coupons sessions with zero commission)** → Internal BI → direct query
- **Web rewards programme data (redemption rate, avg reward cost, ROI by channel)** → Rewards platform owner → existing data

External gaps I could not close with public research:
- Rakuten+ paid tier adoption (launched Nov 2025 - needs 12 months of data)
- Rakuten Rewards US standalone P&L (hidden in Rakuten Group International segment)
- iOS Safari extension activation rate for Honey / Rakuten / Capital One Shopping (not publicly disclosed)
- Ibotta IPN publisher take-rate split (not disclosed)
- Honey iOS Safari user count trajectory (no tracking series exists like Chrome Web Store)
- Coupert founder identity, audited revenue, actual Honey-migration numbers
- SD 2026 revenue, exact DAU, employee count, white-label precedent (private company)

#### 9.2 Red flags (issues that could undermine the analysis or the business)

- **Trust-collapse vulnerability.** Every loyalty mechanic that is not transparently user-positive is a time-bomb. The Honey chronology is a 12-month loss of 40% of Chrome users. Groupon must architect the mechanic with transparency from day one - retrofitting trust after a MegaLag-equivalent expose is impossible.
- **Category saturation.** Rakuten revenue flat FY2025, Ziff Davis Tech & Shopping -18% Q4 2025, Ibotta revenue-per-redemption -5% YoY. The cashback extension market is not growing - it is consolidating. Groupon's entry must be additive (Bucks on local experiences) not substitutive (better cashback).
- **Time-bound acquisition window.** Honey's displaced users are being absorbed by Coupert / Capital One Shopping / Rakuten weekly. The longer Groupon delays, the smaller the available pool.
- **Regulatory escalation.** Rakuten Advertising, Impact.com, and Awin cut Honey off over five days in Jan 2026. The affiliate ecosystem is rewriting what is acceptable. Groupon's affiliate mechanic must meet the new standard, not the 2024 standard.

#### 9.3 Yellow flags (monitor, not blockers)

- **"Honey shutdown" narrative may be inaccurate.** Sources describe degradation, user exodus, and affiliate-network termination - not a full shutdown. The PayPal wallet still runs Honey. Re-verify before exec messaging.
- **$45 Capital One Shopping anchor is an order of magnitude, not a fixed CAC.** Recent observed range is $40-80, with 90-day retention gate. Update the sizing model accordingly.
- **iOS Safari extension activation rates are undisclosed by all competitors.** Groupon sizing must assume 10-30% activation until we have our own data.
- **SD PE exit clock.** GS has held 8 years. If Amazon buys SD, any Groupon partnership would likely be killed or radically shifted. Change-of-control terms are non-negotiable.

---

### 10. Source Reference Index

#### Rebecca's original references [1]-[60]

See `raw/rebecca-draft.md` for the full list. Citations in this merged document use Rebecca's numbering when referencing her-originated data, and my-side references [M1]-[M70] for mine.

#### My additional references [M1]-[M70]

**Rakuten [M1]-[M27]:** rakuten.com/blog (Big Fat Check schedule), rakuten.com/help (welcome bonus terms, how Rakuten works, Safari iOS walkthrough), Rakuten Group FY2024 Financial Results Feb 14 2025 (press release), Rakuten Group Q3 FY2025 Results Nov 13 2025, SimilarWeb rakuten.com Mar 2026, Trustpilot (36,643 reviews 4.6 stars), Dollar Sprout Rakuten Review 2025, CNBC Select Rakuten Review 2025, Rakuten+ launch WWD / Retail TouchPoints Nov 12 2025, Bilt Newsroom Rakuten partnership, Statista Rakuten quarterly US GMS, Justia Oganesyan v Rakuten USA docket 4:2025cv01534, PhatWallet Big Fat Check bounce thread Mar 2024.

**Capital One Shopping [M28]-[M48]:** capitaloneshopping.com help center, CNBC Wikibuy acquisition Nov 2018, PR Newswire class action settlement announcement Sep 2025, ABA Banking Journal Dec 2025 preliminary approval, classaction.org Capital One influencer lawsuit, SimilarWeb capitaloneshopping.com Mar 2026, Apple Community Safari #2 ranking July 2025, Doctor of Credit referral bonus history, Frequent Miler $80 referral + gift card redemption options, Trustpilot capitaloneshopping.com (1.3 stars, 305 reviews), Milestalk "I'm done with Capital One Shopping", PhatWallet $45-bonus thread, Chrome Web Store Capital One Shopping 6M+ users.

**PayPal Honey [M49]-[M70]:** 9to5Google Honey tracking series (Jan 3 2025, Mar 31 2025, May 23 2025, Jul 7 2025, Dec 22 2025, Dec 31 2025), ppc.land Rakuten Advertising termination Jan 2026, ppc.land Impact.com removal, ppc.land Awin suspension, Affiverse MegaLag Part 2 coverage, Cohen Milstein case page In Re PayPal Honey Browser Extension Litigation, Orrick Dec 2025 dismissal coverage, Ben Edelman benedelman.org Honey breaches analysis, heise.de Honey Safari iOS bundling flag, PayPal Q4 2025 earnings release Feb 3 2026, help.joinhoney.com (Gold program, Safari extension, Droplist), joinhoney.com/terms, PayPal Gold Program T&Cs (paypalobjects.com PDF), MegaLag YouTube Part 1 and Part 2, TechCrunch $4B acquisition Nov 2019, Wikipedia PayPal Honey (policy changes and lawsuits section).

**Tier 2 [M71]-[M84]:** Ibotta investor relations Q4 2025 + Q3 2025, Motley Fool Ibotta Q4 2025 earnings call transcript, IPN website, Grocery Dive DoorDash + Instacart partnerships, RetailMeNot 1% floor announcement Feb 25 2026, Ziff Davis Q4 2025 earnings Feb 2026, A Media Operator Ziff Davis affiliate drop, Dollar Sprout Coupert review, Coupert vs Honey 2025 test, Latka Coupert revenue, Crunchbase Coupert profile, Trustpilot coupert.com.

*Starbucks references (initially [M85]-[M96]) removed with scope pruning; Starbucks raw research preserved at `raw/tier2-scan-and-starbucks-benchmark.md` for audit trail.*

**Slickdeals [M97]-[M110]:** Slickdeals corporate / sales pages, Warburg Pincus to Goldman Sachs sale 2018 (PR Newswire, Bloomberg, Fried Frank), Groupon Q3 2025 results (investor.groupon.com), LA Business Journal Slickdeals upper-funnel pivot, AWS re:Invent 2025 SMB206 (Slickdeals AI with SageMaker), SimilarWeb slickdeals.net + SD vs Groupon comparison, HBS Digital Innovation case studies (Slickdeals Monetizing Frugality / Treasure Hunting), Awin publisher spotlight, Kevel customers case, Seeger Weiss Honey/Cap One class action.

---

### 11. Appendix

#### 11.1 AI funnel transparency (Adam's Apr 20 requirement)

See `ai-funnel-appendix.md`. Summary: 5 parallel research subagents (Opus 4.7, 1M context) ran 2-6 WebSearch rounds each. Rebecca's Google Doc fetched via `gws docs documents get` CLI (direct API, no copy-paste). Every claim labelled [Data] / [Estimate] / [Opinion] / [Assumption] with High/Medium/Low confidence. Data gaps declared explicitly rather than filled with guesses. Raw per-agent outputs preserved in `raw/` for audit trail.

#### 11.2 Glossary

- **Buck** - Groupon's proposed 1:1 soft currency. 1 Buck = 1 dollar of redemption value.
- **Big Fat Check** - Rakuten's marketing name for its quarterly cashback payout.
- **Breakage** - % of earned rewards users never redeem (typically 15-30% industry-wide).
- **CAC** - Customer Acquisition Cost.
- **DAU/MAU** - Daily Active Users divided by Monthly Active Users. A stickiness proxy.
- **Genie** - Groupon's existing browser extension (Chrome).
- **IPN** - Ibotta Performance Network (B2B2C distribution).
- **LTV** - Lifetime Value per user.
- **MegaLag** - YouTube investigative channel whose Dec 2024 and Dec 2025 videos triggered Honey's trust collapse.
- **RCLON** - Rakuten Card Linked Offer Network (in-store cashback via linked card).
- **Safari Web Extension** - Apple's iOS extension API, bundled with the parent iOS app.
- **YMMV** - Your Mileage May Vary (used in credit card / cashback communities for targeted offers).

#### 11.3 Deltas from Rebecca's April 2026 draft (for audit transparency)

**What this document adds beyond Rebecca's:**
- Explicit $40M+ retention frame replacing $4M commission frame in the opening
- Per-mechanic cards (6 mechanics) with Groupon adoption cost and priority
- Deeper forensics on Honey class action and Jan 2026 affiliate network terminations
- Capital One Shopping $45 anchor reframed as "$40-80 with 90-day retention gate, YMMV" rather than flat signal
- Rakuten's 2.4% operating margin as the category-economics ceiling
- Slickdeals partnership workstream (deliberately excluded from Rebecca's loyalty doc)
- Confidence ratings on every major claim
- Data gap honesty (internal data asks + external gaps I couldn't close)
- AI funnel transparency appendix (Adam Apr 20 requirement)

**What Rebecca's draft brings that this does NOT duplicate:**
- SimilarWeb audience affinity data (primary data, 37-domain export)
- The "stacking not switching" strategic frame (the sharpest insight in either doc)
- 5-phase research programme with cost estimates
- Honey Chrome decline monthly timeline table (I use it verbatim)
- Internal data requests organised by system/source (§5.7)
- Initial source index [1]-[60] - my [M1]-[M110] extend it

**What remains to be done (both docs):**
- Run Phase 1 of Rebecca's research programme (Semrush audience overlap, keyword gap)
- Pull the 8 internal data items in §5.7
- Mystery-shop one month of tracking reliability across Rakuten/Capital One/Coupert
- Re-verify the "Honey shutdown" narrative (likely: "degraded and de-networked", not shut down)
- Build the mechanic prototypes and A/B test incentive levels per Phase 5


---

## Part 2 - Retention uplift sizing model (shell)

## Retention Uplift Sizing Model - $40M+ 3-Scenario Sensitivity
*Subtask #2 | Martin kickoff, Rebecca to review + contribute | Draft v0.1 | 2026-04-22*

### Purpose
Anchor the $40M+ retention headline currently sitting in the exec summary without visible math. Build a transparent sensitivity model that shows which inputs drive the range, labels every assumption, and makes it trivial to swap in better internal data when it lands.

### The formula

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

### Input table (labelled - all [DATA GAP] items need internal pulls)

| Input | Conservative | Base | Aggressive | Source | Confidence |
|---|---|---|---|---|---|
| **addressable_MAU** (Groupon app + coupons web users, US) | [DATA GAP] | [DATA GAP] | [DATA GAP] | BQ / Tableau mobile app perf dashboard | High once pulled |
| **loyalty_adoption_rate** (% of MAU who activate Bucks / extension) | 10% | 20% | 35% | Cap One #2 Safari app + Honey bundle activation (undisclosed by both; our Estimate 10-30%) | Low - [Estimate] |
| **incremental_orders_per_year** (extra purchases vs no-loyalty baseline) | 0.4 | 1.0 | 2.0 | Industry proxies: Amazon Prime +2x tx, Starbucks Rewards +3x visits (but wrong cadence), general loyalty lit 15-25% frequency lift | [Estimate / Assumption] |
| **AOV** (avg order value, Groupon, US) | [DATA GAP] | [DATA GAP] | [DATA GAP] | BQ / Tableau | High once pulled |
| **take_rate** (Groupon net revenue % of GMV, blended) | [DATA GAP] | [DATA GAP] | [DATA GAP] | Groupon IR / 10-K segment data + internal finance | High once pulled |
| **avg_bucks_earned_per_year** (cashback paid per adopted user) | $15 | $30 | $60 | Rakuten avg $10/yr cumulative; Ibotta $256/yr; Cap One spread | [Estimate] |
| **breakage_rate** (% of Bucks issued, never redeemed) | 15% | 25% | 35% | Industry 15-30%; Starbucks $207M breakage on $1.78B stored value ~12%; compounding if gift-card-only adds 3-10% more | [Estimate] |

### Scenario math (placeholders - need internal data to compute)

#### Conservative
- Adopted users = MAU x 10%
- Incremental revenue per adopted user = 0.4 orders x AOV x take_rate = $[TBD]
- Cashback cost = $15 x (1 - 0.15) = $12.75 per adopted user
- Net per user = incremental revenue - $12.75
- **Scenario total = Adopted users x Net per user**

#### Base
- Adopted users = MAU x 20%
- Incremental revenue per adopted user = 1.0 orders x AOV x take_rate = $[TBD]
- Cashback cost = $30 x (1 - 0.25) = $22.50 per adopted user
- Net per user = incremental revenue - $22.50
- **Scenario total = Adopted users x Net per user**

#### Aggressive
- Adopted users = MAU x 35%
- Incremental revenue per adopted user = 2.0 orders x AOV x take_rate = $[TBD]
- Cashback cost = $60 x (1 - 0.35) = $39.00 per adopted user
- Net per user = incremental revenue - $39.00
- **Scenario total = Adopted users x Net per user**

### What drives the range (sensitivity narrative)

Three inputs dominate uncertainty. Every review conversation should focus on them:

1. **loyalty_adoption_rate** - 10% vs 35% is a 3.5x swing. Most defensible anchor: Capital One Shopping ranks #2 Top Free Shopping on iOS (real discovery channel, unknown activation rate) and Honey-via-PayPal bundling distribution playbook. Groupon's 84% iOS base is the ceiling.
2. **incremental_orders_per_year** - 0.4 vs 2.0 is the biggest lever. Loyalty programs reliably produce 15-25% frequency lift in general retail; Prime and Starbucks sit far higher but are different business models. Our base of 1.0 is the canonical "one extra purchase per year per adopted user" benchmark.
3. **take_rate** - Groupon-specific. Until this internal number lands, the model cannot produce a credible point estimate. Flag to Ernesto / finance.

Four secondary inputs:

4. **addressable_MAU** - scales linearly. Base case assumes Groupon coupons + app US; a broader definition (global, all verticals) would lift all scenarios.
5. **AOV** - internal, scales linearly.
6. **avg_bucks_earned_per_year** - depends on earn rate design. If Groupon commits to 1-5% base, the upper end is $60+ per active user. Needs merchant economic modelling.
7. **breakage_rate** - shifts cashback cost up or down 20-50% of headline earned. Meaningful to margin, not to topline revenue.

### Why this is load-bearing

The exec summary in `loyalty-mechanics-final.md` opens with "The prize is not $4M in coupon commissions. It is $40M+ in retention uplift." Without a visible model, that line is a thesis statement, not a quantified claim. This document is the math Adam / Dusan can stress-test.

### What this model does NOT include (honest scope)

- **Cannibalisation.** If adopted users shift existing purchases to Bucks-earning channel but don't add incremental orders, the "incremental_orders_per_year" term is zero and the whole thing collapses. Base case of 1.0 assumes TRUE incremental, not rebadged.
- **Cross-vertical bridge.** Dusan's coupons-to-deals-buyer crossover question (subtask for Mark Brenda). If crossover is zero, the unified loyalty proposition weakens and the scenarios need a per-vertical split.
- **Churn offset.** A loyalty program can also REDUCE churn. That's not in this model; it would widen the uplift estimate. Add once we have retention-curve data from Ernesto.
- **Fixed + variable program cost.** Eng build (~10-15 sprints per our mechanic cards), ops, fraud, customer service. Not in the incremental-revenue model. Needs a separate OpEx view for an honest NPV.
- **Time ramp.** Year 1 adoption is lower than steady state. Base case represents post-ramp (Year 2+). A real NPV needs a 3-year ramp.

### Inputs to request (ordered)

Top 3 to ask Ernesto / finance / BI this week:

1. **Addressable MAU** - Groupon app + coupons web, US, current MAU
2. **AOV** - blended, Groupon US
3. **Take rate** - Groupon net revenue % of GMV, blended US

These three alone, at [Data] confidence, collapse the scenario range from a 10x spread to ~3x.

Secondary (Rebecca's funded survey + Mark Neary track):

4. **Expected loyalty_adoption_rate** - conjoint willingness from survey
5. **Incremental orders per year** - the Phase 3 behavioural analysis of Genie users (coupons-to-deals crossover) is the closest internal proxy

### Process

- **Today (Apr 22):** Martin shares this shell + input requests to Ernesto + finance + Rebecca. Rebecca reviews methodology.
- **Wed (Apr 23):** ideally Ernesto returns MAU / AOV / take_rate. Martin plugs in, produces three point estimates.
- **Thu (Apr 24):** Rebecca reviews the populated model. Both agree on how to present the range to Adam (single number or range; we recommend range with base case highlighted).
- **Fri (Apr 24 1pm CET):** model ships as an appendix to the final doc, alongside a 2-sentence "how to read this" for Adam.

### Presentation recommendation to Adam

**Don't present a single $40M number.** Present a range with the base case highlighted:

> *Conservative $X M / **Base $Y M** / Aggressive $Z M annual net revenue uplift. The single biggest lever is incremental-orders-per-year; internal data on coupons-to-deals crossover (Mark Brenda, pending) would narrow this range significantly.*

This is honest to Adam's transparency rule and surfaces the one number that would change the recommendation (crossover rate).

---

### Changelog

- v0.1 (2026-04-22) - initial shell, all internal inputs as [DATA GAP], all external inputs as [Estimate] with sources.
- *v0.2 (pending Ernesto / finance data pull)*
- *v0.3 (pending Rebecca methodology review)*


---

## Part 3 - Fact-check v1 (load-bearing numbers vs primary sources)

## Fact-Check v1 - Load-Bearing Numbers vs Primary Sources
*Subtask #3 | Due Apr 22 | Fact-checked 2026-04-22*

### Purpose
Replace aggregator citations (sidehustlenation, millennialmoney, expandedramblings, financebuzz, marketersmedia) with primary sources for the 5 most load-bearing numbers in the loyalty research deliverable. Aggregator-sourced numbers undermine Adam's Apr 20 transparency rule; anything that cannot be verified primary gets downgraded to [Estimate].

### Summary table

| # | Claim | Verdict | Primary source | Confidence |
|---|---|---|---|---|
| 1 | Rakuten 17M+ US members AND $4.6B cumulative cashback | **PARTIAL: $4.6B confirmed; 17M not found on primary** | rakuten.com (cashback number) | $4.6B High; 17M Low |
| 2 | Capital One Shopping $45 install incentive | **UPDATE: not a fixed number** | capitaloneshopping.com live landing page (no public $45 visible); Doctor of Credit + Frequent Miler track referral range | Low on $45 specifically; Medium on "$40-80 YMMV referral + 90-day retention gate" framing |
| 3 | Coupert 8M+ weekly active users | **CONFIRMED as company claim, unaudited** | Coupert corp + Marketers Media press release Oct 2025 | Medium (company self-report) |
| 4 | Ibotta 54M registered / 18.2M redeemers / $342M FY2025 revenue | **CONFIRMED** | Ibotta investor relations, FY2025 10-K filed Feb 2026, BusinessWire release | High |
| 5 | PayPal Honey 12-13M Chrome users | **CONFIRMED at Dec 2025; no Apr 2026 update found** | 9to5Google tracking series Dec 31 2025 | High on Dec 2025; Medium-Low on Apr 2026 currency |

---

### Claim 1 - Rakuten 17M+ US members AND $4.6B cumulative cashback

- **Original source in report:** sidehustlenation.com (aggregator), Wikipedia (for 17M members), rakuten.com corp overview
- **Primary source found:** rakuten.com (corp page confirms "$4.6 Billion in Cash Back since 1999")
- **Verdict:**
  - **$4.6B cumulative cashback: CONFIRMED** as Rakuten's own public claim. Date baseline: 1999.
  - **17M+ US members: UNVERIFIED via primary source.** Rakuten.com search does not surface the number. Rakuten Group Q3 FY2025 Nov 13 2025 press release (prior research) discusses segment financials, not US membership count. This number may be cumulative signups ever (most likely) rather than active members, but Rakuten does not break this out publicly.
- **Current number (April 2026):**
  - $4.6B+ cumulative since 1999 [confirmed]
  - 17M+ [not publicly sourced primary; downgrade to [Estimate]]
- **Confidence:** High on $4.6B, Low on 17M
- **Recommended action:** Keep $4.6B as [Data]. Change "17M+ US members" to "**17M+ cumulative US signups since 1999 [Estimate - not broken out in public Rakuten IR; active member count undisclosed]**" throughout the final report.

Sources:
- [Rakuten Help - Coupons, Promo Codes & Cash Back](https://www.rakuten.com/help/article/company-overview-360002116927) - cumulative $4.6B
- [Rakuten American Express Card Expands Cash Back Benefits](https://global.rakuten.com/corp/innovation/rnn/2025/2509_001/) - corporate press release
- [Get 10% Cash Back with Rakuten+](https://www.rakuten.com/rp/member/join)

---

### Claim 2 - Capital One Shopping $45 install incentive

- **Original source in report:** millennialmoney.com (aggregator), with "also referenced in Groupon internal strategic documents" caveat
- **Primary source found:** capitaloneshopping.com current homepage (per agent capture 2026-04-22: **no dollar signup bonus visible on public landing page**)
- **Verdict:** **UPDATE - not a fixed $45.** The $45 specifically is not a current public headline. Historical range $10 (2020) -> $200 (Dec 2023 peak) -> $40-80 (2024-2026 norm). Current public offer: $80/$80 referral, both sides, 90-day retention requirement, referral-gated (not homepage-visible). iOS Safari extension App Store copy mentions a separate "$10 in 21 days" bonus.
- **Current number (April 2026):** **$80/$80 referral with 90-day retention gate, YMMV-targeted, US-only, referral-link-gated (not visible on homepage)**
- **Confidence:** Medium on "$40-80 range + retention gate" framing; Low if anyone tries to quote a single $45 number
- **Recommended action:** Replace every "$45" in the final report with "**$40-80, referral-gated, with 90-day retention requirement, YMMV-targeted (current Apr 2026 headline: $80/$80 both-sides)**". Flag that the retention gate is the more interesting LTV signal than the dollar amount. Update mechanic card 02 accordingly.

Sources:
- [Capital One Shopping homepage](https://capitaloneshopping.com/) - no visible $45 offer
- Doctor of Credit, Frequent Miler referral bonus coverage (per prior agent research; Tier 2 secondary but deals-community primary)
- `raw/capital-one-shopping-mechanics.md` (prior deep dive)

---

### Claim 3 - Coupert 8M+ weekly active users

- **Original source in report:** marketersmedia.com (press release wire service)
- **Primary source found:** company's own corp page + Marketers Media Oct 2025 press release issued BY Coupert
- **Verdict:** **CONFIRMED as Coupert's self-reported company claim.** Also appears on coupert.com ("Coupert helps 8M+ users save more online") and in Coupert's own blog content benchmarking vs Honey. **Unaudited self-report**, not independently verified.
- **Current number (April 2026):** 8M+ weekly active (Coupert claim, Oct 2025)
- **Confidence:** Medium - company-issued but not independently audited
- **Recommended action:** Keep "8M+ weekly active" in the final report but **add the provenance caveat**: "8M+ weekly active users [Data - Coupert self-reported Oct 2025 via company press release; unaudited]." Do NOT promote to high-confidence primary.

Caveat worth flagging: **This claim is weirdly inconsistent with the rest of Coupert's profile.** An 8-11 person bootstrapped company with ~$1.2M revenue claiming 8M weekly active users is implausible unless "weekly active" is being measured very loosely (e.g. extension installs, not users who actually engaged). Worth questioning in the Dusan conversation.

Sources:
- [Coupert Reaches 8 Million Weekly Users - Marketers Media press release](https://news.marketersmedia.com/coupert-reaches-8-million-weekly-users-as-global-leader-in-coupon-and-cashback-extensions/89172029) - company-issued
- [Coupert homepage](https://www.coupert.com/) - confirms 8M+ framing
- [Coupert vs Honey 2025 research](https://www.coupert.com/research/coupert-vs-honey-which-coupon-extension-performs-best-in-2025)

---

### Claim 4 - Ibotta 54M registered / 18.2M redeemers / $342M FY2025 revenue

- **Original source in report:** expandedramblings.com (aggregator)
- **Primary source found:** Ibotta investor relations FY2025 press release + 10-K filing Feb 2026
- **Verdict:** **CONFIRMED** - all three numbers corroborated directly from Ibotta IR.
- **Current number (April 2026):**
  - FY2025 revenue: $342.4M [Data, High]
  - Registered users: 54M+ [Data, High]
  - Redeemers 2025: **18.2M (average, +24% YoY from 14.7M in 2024)** [Data, High]
- **Confidence:** High
- **Recommended action:** Swap the expandedramblings citation for the Ibotta IR press release and 10-K in the reference index.

Sources:
- [Ibotta Reports Q4 and Full Year 2025 Financial Results - investors.ibotta.com](https://investors.ibotta.com/news-events/press-releases/detail/138/ibotta-reports-fourth-quarter-and-full-year-2025-financial-results)
- [BusinessWire mirror, Feb 25 2026](https://www.businesswire.com/news/home/20260225755258/en/Ibotta-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results)
- [Ibotta 10-K Feb 2026 - last10k.com](https://last10k.com/sec-filings/ibta/0001628280-26-011838.htm)

---

### Claim 5 - PayPal Honey 12-13M Chrome users

- **Original source in report:** 9to5Google tracking series (already Tier 2, reasonably primary for this metric)
- **Primary source found:** Chrome Web Store is the ultimate primary source; 9to5Google is the tracker. No April 2026 update article located in search.
- **Verdict:** **CONFIRMED as of Dec 31 2025** (12M Chrome users, down from 20M peak). **April 2026 specific number not found in public reporting.**
- **Current number (April 2026):**
  - Dec 31 2025: 12M [Data, High]
  - Apr 2026: [Data gap] - no public 9to5Google update between Jan and Apr 2026. The Chrome Web Store live count is the primary source; needs direct check.
- **Confidence:** High on Dec 2025 number; Medium-Low on currency for April 2026.
- **Recommended action:** **Update the final report** to say "12M Chrome users as of Dec 31 2025 [Data]; April 2026 live count not independently confirmed, check Chrome Web Store directly before final send." Martin or Daniel should screenshot the Chrome Web Store listing for the final Friday package.

Sources:
- [Honey has lost 8 million Chrome users in the past year - 9to5Google Dec 31 2025](https://9to5google.com/2025/12/31/honey-chrome-users-fraud/)
- [Chrome Web Store - Honey extension](https://chromewebstore.google.com/detail/honey-automatic-coupons-r/bmnlcjabgnpnenekpadlanbbkooimhnj) (live count - needs direct check)
- [PayPal Honey - Wikipedia](https://en.wikipedia.org/wiki/PayPal_Honey)

---

### Action items for the final report

1. **Rakuten:** soften "17M+ US members" to "17M+ cumulative US signups since 1999 [Estimate]" across mentions. Keep $4.6B as confirmed primary.
2. **Capital One Shopping:** replace every "$45 install incentive" with "$40-80 referral-gated with 90-day retention requirement (current Apr 2026: $80/$80)".
3. **Coupert:** add "unaudited self-report" caveat to the 8M figure; flag the implausibility-vs-company-size tension for Dusan.
4. **Ibotta:** trivial citation swap from expandedramblings to investors.ibotta.com + 10-K.
5. **Honey:** update 12M (Dec 2025) with a note that April 2026 live count is a dependency for the Friday final send; pair with Chrome Web Store screenshot.

### What I did not fact-check here (explicit scope)

- Rebecca's SimilarWeb audience affinity data [1.000, 0.924, 0.826, 0.815] - primary data from her own SimilarWeb Pro export, already confirmed
- Global cashback market $8-10B growing to $22-23B - multiple analyst citations, not one load-bearing aggregator
- Starbucks data points - irrelevant, Starbucks was removed from the final report in the Apr 21 scope prune
- Rakuten 2.4% operating margin - Rakuten Group IR filing, primary already

### What to ask Martin to do manually

- Screenshot Chrome Web Store Honey listing (Apr 22 2026 count) for the Friday package
- Confirm that the Cap One $80/$80 referral is still the current public offer when signing up for the real account this week
- Screenshot the current Rakuten welcome bonus landing page (Daniel US-side if available) for the $50/$50 referral through Jun 30 2026


---

## Part 4 - Competitor visual mapping - pattern analysis

## Cross-Competitor Pattern Analysis
*Source: automated captures 2026-04-22 from CZ IP | See `README.md` for provenance*

This is the analytic layer on top of the screenshot set. Every pattern below cites at least one PNG file in the `competitor-mapping/` folder; the raw evidence lives next to the claim.

---

### Headline patterns (what becomes obvious when you see all 7 side by side)

#### 1. Safari is the battleground - "Add to Safari, It's Free" is the new default CTA

Honey landing (`honey/01-landing-fold.png`) and Coupert landing (`coupert/01-landing-fold.png`) both use **identical primary CTA wording: "Add to Safari - It's Free"**. This is a competitive convergence - both compete for the same post-Chrome-exodus cohort and both have picked Safari as the wedge. Rakuten keeps the Safari push a step down (under the hero CTA) but still invests heavily in an iOS Safari extension bundled with the app (`rakuten/08-ios-app-store-fold.png`). Capital One Shopping has a dedicated App Store listing for the Safari extension as a separate product from the main app (`capital-one-shopping/07-ios-safari-extension-fold.png`).

**Implication for Groupon:** Safari-first is no longer a differentiator - it is table stakes. Groupon's Genie + iOS Safari extension thesis is validated by the convergence, but the "we're on Safari" claim alone will not cut through. The differentiator will be WHAT the extension earns (Bucks redeemable on local experiences).

#### 2. Social-proof arms race is in the hero

Every landing page uses a large member count or dollar count in the fold:
- Honey: "17 million members and counting" + "141,786 Chrome Store reviews" (`honey/01-landing-fold.png`)
- Ibotta: "$2.3B cash back paid" + "4.7 app store rating" + "3K+ retailers" (`ibotta/01-landing-fold.png`)
- Rakuten iOS App Store: "Join 17M members earning Cash Back" + "Earn $500+ a year on average" (`rakuten/08-ios-app-store-fold.png`)
- Coupert: "Trusted by 8M+ users and 70,000+ shoppers on Trustpilot" (`coupert/01-landing-fold.png`)

Honey's continued 17M member claim is notable - they are still marketing the peak-brand number in April 2026 despite having lost 40% of Chrome users. This is a willful optimism that a sophisticated user would see through, but marketing-wise it is consistent with PayPal's "no public admission the brand is damaged" posture.

**Implication for Groupon:** Social proof in the hero is table stakes. Groupon has the option to anchor on "30M app installs" or "X million Groupon deals purchased" - this will need to be decided and landed in the final mock.

#### 3. Three distinct signup-friction postures

Each competitor has a different strategy for converting landing-page visitors to registered users:

- **Capital One Shopping - aggressive modal interrupt** (`capital-one-shopping/01-landing-fold.png`): a full-screen signup modal appears over the landing content almost immediately. Message: "It's kinda genius, join now for free." Email + password + Continue, with "Create account later" as a de-emphasized escape hatch. Content behind the modal is visible but greyed out. **This is a forcing function** - user either signs up or explicitly declines.
- **Honey - passive hero CTA** (`honey/01-landing-fold.png`): no modal, no email capture on landing. Just a prominent "Add to Safari - It's Free" button. Signup happens after installing the extension.
- **Ibotta - app-store routing** (`ibotta/01-landing-fold.png`): no signup on the web at all. Landing hero pushes you to Apple App Store / Google Play buttons. The entire signup funnel is delegated to the mobile app.
- **Coupert - passive hero CTA + social proof** (`coupert/01-landing-fold.png`): similar to Honey; "Add to Safari - It's Free" button with Trustpilot trust signal immediately underneath.
- **Rakuten - hard geoblock** (`rakuten/01-landing-fold.png`): no signup flow available at all from EU IP. Users are routed to country chooser (FR/DE/ES).
- **RetailMeNot - GDPR consent wall** (`retailmenot/01-landing-fold.png`): signup is available but the content and CTAs are partly obscured by a cookie/tracking consent overlay.

**Implication for Groupon:**
- Aggressive signup-modal interrupt (Cap One pattern) drives account creation but is increasingly viewed as user-hostile
- The app-routing pattern (Ibotta) is right if the web surface is primarily an acquisition marketing page
- The passive-CTA + extension-led signup (Honey, Coupert) matches what our Safari extension strategy actually implies - signup is mid-funnel, not at landing
- Recommended for Groupon: Honey/Coupert pattern (passive landing CTA, extension installs first, account creation at first value-earning event)

#### 4. Currency clarity splits the category

Honey Gold page (`honey/03-features-gold-fold.png`):
- "Get Honey Gold rewards on eligible items when you shop at participating stores. Once you have enough Gold, redeem it for a gift card."
- "Keep in mind, you can only earn Gold from participating stores based in certain countries."
- **No rate disclosed on the page** - no "1000 Gold = $10" public message, no "X% earn rate" headline
- Links: "Terms and exclusions apply"

This is deliberate obfuscation - a user cannot tell what Honey Gold is worth from reading the public mechanic page.

Coupert cashback help (`coupert/03-cashback-help-fold.png`):
- Clear structure: sidebar with 12 articles - "How Cash Back Works", "Meaning of Cash Back Status", "Avg Confirmation Time", "How is Cash Back Rate Calculated", "How to Report Missing Cash Back", "Coupert Cash Back Terms"
- Rate is disclosed on the page with a live TEMU example: "8.3% Cash Back"
- Transparent and process-documented

Ibotta IPN page (`ibotta/03-ipn-performance-network-fold.png`):
- "Pay-per-sale efficiency"
- Chobani example shows "$1.00 back" as a real number next to the "Add to cart" button
- Transparent at the offer level

**Implication for Groupon:** Coupert + Ibotta demonstrate that transparent-rate presentation is compatible with the business model. Honey's obfuscation is a choice, not a requirement. Groupon's 1:1 Bucks design should lean Coupert-style: rate visible at the point of use. This matches mechanic card 02 already.

#### 5. Ibotta's B2B2C pivot is visible in the public surface

Ibotta IPN page (`ibotta/03-ipn-performance-network-fold.png`): hero speaks directly to **brands**, not consumers. "As the leading promotions network in the U.S., the Ibotta Performance Network helps brands maximize incremental return utilizing pay-per-sale efficiency and AI-driven optimization while delivering digital promotions at unprecedented scale." The main nav bar has a dedicated "Business solutions" entry alongside consumer-facing "Cash back" (`ibotta/01-landing-fold.png`).

This confirms the research finding that Ibotta has pivoted from consumer app to B2B2C distribution infrastructure. Compare to Rakuten, Honey, Cap One Shopping - none of which feature a brand-facing pitch in their primary nav.

**Implication for Groupon:** Ibotta's B2B2C model is a 2027 option for Groupon (per mechanic card table row 9), not a current-quarter play. But the fact that they're investing in brand-facing marketing so publicly means the opportunity is well-claimed - Groupon's window to compete on this dimension is narrower than it was 18 months ago.

#### 6. Ibotta is the only serious app-first competitor

All other Tier-1 and Tier-2 competitors (Rakuten, Honey, Cap One, Coupert, RetailMeNot) lead with an **extension** CTA or a signup form on the web. **Ibotta is app-only** in presentation (`ibotta/01-landing-fold.png` - only App Store + Google Play download buttons in the hero, no web-side account creation or extension link).

This reflects Ibotta's receipt-scan mechanic, which is app-mandatory (cameras, OCR, push for alerts). It's a structural UX difference, not just a marketing choice.

**Implication for Groupon:** If Groupon's loyalty layer is genuinely app-primary (Genie + Safari extension bundled), Ibotta's landing pattern is the closer analogue than the Honey/Rakuten extension-led pattern. Worth testing in A/B. For the Friday doc, worth showing both patterns as candidate UX inspirations.

#### 7. Geographic gating is asymmetric and meaningful

| Competitor | From CZ IP | What this means for Groupon's EU play |
|---|---|---|
| **Rakuten** | Hard-blocked to EU regional chooser (FR/DE/ES only; `rakuten/01-landing-fold.png` and all /* pages) | **Rakuten is absent from CZ and most EU markets.** Groupon's EU loyalty play has no incumbent cashback competitor outside FR/DE/ES. |
| **Capital One Shopping** | Fully accessible, content English, US-flavoured (`capital-one-shopping/01-landing-fold.png`) | Cap One does not geo-gate but also does not localise. US brands + $ currency - EU users can browse but the utility is thin outside US |
| **Honey** | Fully accessible, no geo-gate | Honey claims 10-country availability for mobile Safari, but web-side is borderless |
| **Ibotta** | Accessible but US-focused | US-only utility |
| **RetailMeNot** | Accessible with GDPR consent wall (`retailmenot/01-landing-fold.png`) | GDPR-compliant, so EU users can transact if they accept |
| **Coupert** | Fully accessible (`coupert/01-landing-fold.png`) | HK-based, no geo-gate |
| **Slickdeals** | Cloudflare bot challenge blocks even landing (`slickdeals/01-landing-fold.png`) | US-only community, hard to validate for a European partnership BD team |

**Implication for Groupon:** **Rakuten's EU absence is the single most actionable finding in this capture set.** If Groupon launches a loyalty layer in CZ, PL, or most EU markets (excluding FR/DE/ES), Rakuten is not a competitor at all. This is a material input to the EU rollout sequencing decision and has not been sized in the retention uplift model. Worth sharing with Dusan.

#### 8. Post-scandal posture: Honey has no visible trust-recovery messaging

Honey landing (`honey/01-landing-fold.png`), Honey Gold page (`honey/03-features-gold-fold.png`), Honey terms (`honey/04-terms-fold.png` - fold shows only cookie banner), PayPal help593 page (`honey/07-paypal-help-bundled-extension-fold.png`): **no mention of the scandal, no affiliate-attribution disclosure, no acknowledgement of the 40% Chrome user loss**. The PayPal Help article reads as if late-2024 never happened.

Compare to the MegaLag-era press coverage and the class action (Cohen Milstein, Jan 5 2026 101-page amended complaint). Honey's PUBLIC posture is "nothing to see here" - legal silence is the strategy.

**Implication for Groupon:** This is the anti-pattern. Proactive affiliate-attribution disclosure at the point of cashback (per mechanic card 06) is a direct differentiator against the current Honey posture. Users who have read the MegaLag coverage and land on Honey will see continuity, not repair - Groupon can win on visible repair-first design.

#### 9. The signup-friction-vs-trust tradeoff is live

Looking at the patterns together:
- **Lowest signup friction:** Honey, Coupert (passive "Add to Safari" - no email on landing)
- **Highest signup friction:** Cap One (aggressive modal interrupts landing)
- **No web signup:** Ibotta (app-only)

Cap One's aggressive modal is interesting because Cap One has the **most conservative trust posture** of the group (no paid tier, no points obfuscation, 1:1 currency, no banking tie-in required). They appear to be trading immediate conversion for account-creation-first - the user commits to a relationship before seeing the details.

**Implication for Groupon:** There's a clean A/B hypothesis here - does aggressive signup-modal conversion win vs passive-CTA + extension-first? Worth testing on the new-UI coupons pages once registration layer lands.

#### 10. Slickdeals is invisible to automation (and thus to AI pattern analysis)

Slickdeals landing (`slickdeals/01-landing-fold.png`) is a Cloudflare "verify you are human" challenge. No public-page scraping possible. Agent-era AI tools cannot do competitive intelligence on Slickdeals without human-authenticated sessions.

**Implication for Groupon:** this is an under-commented advantage for Slickdeals as a partner. Their Cloudflare posture means competitors (and AI-based ones especially) cannot easily reverse-engineer their community dynamics. It is one real reason the community moat is durable - you cannot scrape it.

---

### Pattern matrix (fast reference)

| Dimension | Rakuten | Cap One Shopping | Honey | Ibotta | RetailMeNot | Coupert | Slickdeals |
|---|---|---|---|---|---|---|---|
| Primary CTA | N/A (geoblocked) | Signup modal | Add to Safari | Get app | Browse deals | Add to Safari | (bot-blocked) |
| Signup friction on landing | N/A | High (modal) | Low (extension-led) | Low (app-led) | Medium (GDPR wall) | Low (extension-led) | Cloudflare |
| Currency clarity on public page | $ + points optionality | 1:1 Credits ($1 = 1) | Honey Gold (rate hidden) | $ direct | $ + 1% floor | $ + 8.3% example | N/A |
| Social-proof hero flex | "17M members trust" (app only) | None on landing (modal) | "17M members", "141K reviews" | "$2.3B", "4.7 stars", "3K+ retailers" | N/A (GDPR) | "8M+ users" | N/A |
| Geographic accessibility from CZ | Hard-blocked (EU chooser) | Full | Full | Full (US-utility) | Full (GDPR wall) | Full | Bot-blocked |
| Post-scandal / trust messaging | N/A | Standard | **Absent** | Standard | Standard | "Trusted" on hero | N/A |
| Public affiliate-attribution disclosure | None visible | None visible | None visible | IPN page talks to brands, not consumers | None visible | None visible | N/A |
| App store rating (where visible) | 4.8/147K+ (iOS, `rakuten/08`) | 4.9/1.6M (iOS, prior research) | Not captured (consent wall) | 4.7 (landing) | Not read | Not captured | N/A |

---

### The single most actionable finding

**Rakuten is absent from most EU markets.** Confirmed visually on capture day - rakuten.com from CZ IP offers only France/Germany/Spain, with no path to join a US Rakuten account without a US IP.

Consequence: Groupon's EU loyalty rollout operates in a market with no incumbent cashback extension competitor of scale. Honey is diminished, Capital One Shopping is US-brand-heavy and not localised, Coupert is HK/global but small. **The EU is a first-mover opening for Groupon** that the retention uplift model currently does not size separately.

Recommend adding a Phase 2 to the sizing model: US market (where Groupon competes with Rakuten + Cap One + Honey) vs EU market (where Groupon essentially competes with nobody at the loyalty-layer scale).

---

### Where the screenshots do NOT tell the full story

- **Logged-in user experience** - absent by design (human-only per subtask #1)
- **Safari extension in action on Nike.com** - absent (needs Martin or Daniel)
- **Chrome Web Store live install counts** - Google consent wall blocks automated capture from CZ IP; needs authenticated human session
- **Actual welcome email content** - requires real signup
- **Mobile Safari rendering** - this capture was desktop-viewport only; mobile Safari may present differently

See `gaps.md` for the full list and the path to close each.

---

### Sources (every pattern here traces to at least one PNG)

Every claim in this file is linked to a specific fold PNG above. For each competitor, the full-page PNG (non-fold version, same filename without `-fold` suffix) shows below-the-fold content that adds nuance - worth browsing manually when preparing the Friday package.


---

## Part 5 - Competitor visual mapping - inventory

## Competitor Visual Mapping - Inventory & Provenance
*Captured 2026-04-22 | Source: automated Playwright capture from Martin's Czech Republic IP*

### What this is

Headless-Chromium captures of 7 competitors' public pre-authentication surfaces (landing pages, signup forms, help center mechanic pages, Chrome Web Store listings, iOS App Store listings). Intended as:
1. Visual evidence backing the loyalty-mechanics-final.md report
2. Pattern-analysis input (see `pattern-analysis.md`)
3. Primary-source screenshots for Friday's Adam package (upload this folder to G Drive Shared Drive -> Product -> Cashback research -> loyalty-research/competitor-mapping/)

### Capture provenance

- **Date:** 2026-04-22
- **Tool:** Playwright 1.58.0 + Chromium 1208
- **Script:** `_capture.py` (initial run, 41 URLs) + `_retry.py` (Ibotta + RetailMeNot retries with less strict load strategy)
- **User agent:** Safari 17.5 on macOS Sonoma (desktop)
- **Viewport:** 1440x900 (desktop at typical laptop resolution)
- **Location:** Czech Republic (EU) IP - affects results for Rakuten (hard geoblock), RetailMeNot (GDPR cookie wall), Slickdeals (Cloudflare bot challenge), Chrome Web Store (Google consent wall)
- **Output:** full-page PNG + fold (above-the-fold) PNG per URL = 82 total PNGs
- **Inventory file:** `_inventory.json` (per-URL metadata: http status, final URL, page title, byte counts, errors)

### Competitor coverage

| Competitor | URLs captured | Key captures that worked | Known limitations from CZ IP |
|---|---|---|---|
| Rakuten | 9 | EU geoblock landing, iOS App Store (US content), referral, Big Fat Check FAQ (geoblocked too) | rakuten.com and every transactional path auto-redirect to an EU regional chooser (FR/DE/ES only). Rakuten US is effectively closed to EU residents - a competitive opening for Groupon in EU. Daniel dependency confirmed critical. |
| Capital One Shopping | 7 | Landing (with aggressive signup modal), iOS App Store, Safari extension App Store, rewards page | /how-it-works returns 404; the URL structure has changed. Chrome Web Store needs Google cookie acceptance. |
| PayPal Honey | 8 | Landing, Honey Gold features, Droplist, terms, PayPal help593 bundled-extension article | Chrome Web Store needs Google consent. Terms page cookie banner blocked fold capture. |
| Ibotta | 5 | Landing, IPN B2B2C page, iOS App Store, investor relations | /how-it-works path returns 404; footer uses different URL |
| RetailMeNot | 3 | Landing (GDPR consent overlay), cashback, iOS App Store | GDPR consent overlay blocks content above the fold; second-pass capture still shows overlay |
| Coupert | 5 | Landing, welcome, Chrome Web Store (blocked), cashback help center, Coupert-vs-Honey blog | Google consent wall on Chrome Web Store |
| Slickdeals | 4 | API sales page, advertising audience page | **slickdeals.net hard-walls with Cloudflare bot challenge** - no landing-page capture possible via automated browsing. Partnership BD will need to access via authenticated human session. |

### File structure

```
competitor-mapping/
├── README.md                           # this file
├── pattern-analysis.md                 # cross-competitor pattern findings
├── gaps.md                             # what's missing and how to close it
├── _capture.py                         # reproducible capture script
├── _retry.py                           # retry script for font-load + JS-redirect failures
├── _inventory.json                     # JSON metadata per URL
├── _errors.log                         # errors from first capture pass
├── rakuten/                            # 18 PNGs (9 URLs x 2 formats)
├── capital-one-shopping/               # 14 PNGs (7 URLs x 2)
├── honey/                              # 16 PNGs (8 URLs x 2)
├── ibotta/                             # 10 PNGs (5 URLs x 2)
├── retailmenot/                        # 6 PNGs (3 URLs x 2)
├── coupert/                            # 10 PNGs (5 URLs x 2)
└── slickdeals/                         # 8 PNGs (4 URLs x 2)
```

### File naming convention

Within each competitor folder:
- `NN-slug.png` = full-page screenshot
- `NN-slug-fold.png` = above-the-fold (viewport-sized, 1440x900) screenshot
- `NN` (01, 02, ...) = capture order within the competitor, corresponds to `_capture.py` TARGETS list

### How to re-run

```bash
cd projects/groupon-ecosystem/loyalty-research/competitor-mapping
python3 _capture.py   # full run
## or
python3 _retry.py     # just the failed targets
```

Requires `pip install --user playwright && python -m playwright install chromium` one-time setup.

### Reproducibility notes

- Screenshots reflect the **public pre-auth experience from a CZ IP** at the captured moment. US-visible content (behind Rakuten geoblock) is different and requires Daniel's US capture.
- Cookie / GDPR / bot-protection overlays visible in several fold captures are genuine pre-auth friction that matters for the analysis, not just capture artifacts.
- Automated capture cannot reproduce mouse-hover states, modal interactions, or authenticated flows. Those are the human-capture portion of subtask #1.

### Provenance for Adam's package

Every claim in `pattern-analysis.md` is traceable to a specific PNG file in this folder. When the Friday package includes a competitor mechanic claim, the PNG lives here as evidence. This is what Adam's Apr 20 transparency rule translates to at the visual level.


---

## Part 6 - Competitor visual mapping - gaps

## Competitor Mapping - Gaps and Follow-Up Actions
*2026-04-22 | Inventory of what the automated capture could NOT get, with mitigation*

### Priority-ordered gap list

#### P1 - Required for Friday package

| Gap | Owner | Mitigation path | Blocker? |
|---|---|---|---|
| **Chrome Web Store live install counts (Honey, Rakuten, Cap One Shopping, Coupert)** - Google consent wall blocks automated capture from CZ IP | Martin | Screenshot manually in a logged-in-to-Google session; takes 5 minutes, save to `competitor-mapping/<slug>/05-chrome-web-store-manual.png` | No (fast fix) |
| **Rakuten US web flows (signup form, welcome bonus page, Big Fat Check FAQ, Safari install walkthrough)** - geoblocked from CZ IP, redirects to EU chooser | Daniel (US content team) | Per existing subtask #6 - 10-min screen recording + screenshots from US IP | **YES - high risk if Daniel doesn't respond** |
| **Slickdeals landing / corporate pages** - Cloudflare bot challenge blocks automated capture | Martin | Screenshot manually in normal browser session with Cloudflare challenge solved; 5 min | No |
| **Honey terms page content** (to verify "not your property, not money, no value" language or its removal) | Martin | Scroll past cookie banner manually and capture | No |
| **Current Chrome install count for Honey** - 12M at Dec 2025, April 2026 number not publicly disclosed | Martin | Chrome Web Store manual screenshot; dovetails with the Chrome Web Store consent-wall gap above | No |

#### P2 - Strengthens the package but not blocking

| Gap | Owner | Mitigation path |
|---|---|---|
| **Logged-in user experience** for Rakuten, Cap One, Honey, Coupert (welcome email, bonus-progress UI, first merchant offer, extension activation) | Martin | Real signups per subtask #1; burner emails and + aliases recommended |
| **Safari extension in action on Nike.com** (Rebecca's canonical test case) | Martin (Cap One, Honey, Coupert) + Daniel (Rakuten US) | Screen recordings; subtask #1 |
| **Mobile Safari rendering** of each landing page | Martin | Open on phone, screenshot; optional - desktop captures are sufficient for most pattern analysis |
| **Ibotta how-it-works page** - /how-it-works is 404, correct URL is in the footer nav | Anyone | Click the footer link, update `_capture.py` with correct URL, re-run for that one target |
| **Cap One Shopping how-it-works page** - /how-it-works is 404 | Anyone | Find the right URL via site search; same low-effort fix |
| **Ibotta investor relations latest filing / 10-K PDFs** - IR page captured but the actual 10-K content is on a linked PDF | Anyone | Download 10-K PDF separately if we need to cite specific passages |

#### P3 - Nice to have, not critical

| Gap | Owner | Mitigation path |
|---|---|---|
| Below-the-fold content of all landing pages (testimonials, FAQ, footer) | Anyone | Full-page PNG already captured (non-fold versions). Just browse them manually when preparing the Friday slides. |
| RetailMeNot with GDPR consent accepted | Anyone | Click "Accept All" and re-capture one page; 2 min |
| **Ibotta vs RetailMeNot merchant-overlap comparison** - both show partial merchant grids on landing; could cross-reference | Rebecca (she has the Florence scrape) | Her existing subtask covers RetailMeNot + Cap One merchant overlap; Ibotta can fold in |

---

### Known structural limits of automated capture

These cannot be closed by tooling alone - documenting for context:

1. **Authenticated experience** is out of scope for this approach. Headless Chromium does not create accounts; it captures what an anonymous visitor sees. Any claim about "after signing up, the user sees X" requires a human session.
2. **Interactive states** (hover tooltips, dropdown menus, multi-step modals, video autoplay) are not captured by static PNG snapshots. Where a competitor's signup form has dynamic validation or conditional fields (Cap One, Rakuten likely), only the initial state is visible in the capture.
3. **Geographic content variation** is captured from one IP only. For every competitor except Rakuten, the CZ-IP version appears identical to what a US visitor would see (per spot-checks via US proxies in prior research). Rakuten is the exception.
4. **Dynamic content personalisation** (e.g. Amazon-style "recommended for you") doesn't apply to pre-auth captures but does apply to logged-in captures. Noting for completeness.

---

### Recommended next actions (next 24h)

1. **Martin, today EOD:** Open Chrome Web Store (logged into Google) and screenshot Honey, Rakuten, Cap One Shopping, Coupert extension pages. Save as `competitor-mapping/<slug>/05-chrome-web-store-manual.png`. Update `pattern-analysis.md` currency-clarity table with the live install counts.
2. **Martin, today EOD:** Screenshot Slickdeals landing in a normal browser (solve the Cloudflare challenge once). Save as `competitor-mapping/slickdeals/01-landing-manual.png`.
3. **Martin, today EOD:** Open Honey T&Cs in a normal browser, dismiss the cookie banner, capture the "your account" / "your property" / "expiration" / "redemption" sections. Save as `competitor-mapping/honey/04-terms-manual.png`. This is where the legal language for the final report's trust section is verified.
4. **Daniel (per subtask #6):** 10-min screen recording of Rakuten US. Save to G Drive or Slack back to Martin.
5. **Optional (Martin or anyone):** Find correct /how-it-works URLs for Cap One Shopping and Ibotta, re-run the capture script for those two URLs only.

---

### What NOT to spend time on

- Do not re-run the full capture script. It ran clean 82/82 screenshot files, 7/7 competitors covered. Only re-run individual failing targets.
- Do not attempt to automate around Cloudflare (Slickdeals). Human screenshot is fine, and Slickdeals is a partnership workstream, not the primary loyalty competitor.
- Do not attempt to automate signup flows. Burner signups by a human with a new email are faster and produce richer artefacts (welcome emails, activation screens) that automated tools would miss anyway.
- Do not invest in higher-resolution captures. 1440x900 is the standard laptop viewport; desktop 2560x1440 captures make for larger files without meaningful new information.

---

### Handoff for the Friday package

The inventory here fits Adam's Apr 20 transparency rule directly: every pattern claim in `pattern-analysis.md` has a PNG file. The G Drive upload path is one step:

```
Upload: projects/groupon-ecosystem/loyalty-research/competitor-mapping/
To:     Shared Drive -> Product -> Cashback research -> loyalty-research/competitor-mapping/
```

Total folder size: ~30 MB. 82 PNGs + 3 markdown docs + 2 Python scripts + 1 JSON inventory + 1 error log. Uploads in under a minute.


---

## Part 7 - Signup-flow pre-auth captures

### rakuten-preauth

#### Rakuten - Public Pre-Auth Capture
*Captured 2026-04-22 via public web, no account created. Access from CZ (EU) IP; all rakuten.com root-level URLs auto-redirect to an EU regional chooser, so US-site content was captured via mirror sources (help.rakuten.com articles which do render content, plus reviewer screenshots dated 2025-2026 and Rakuten's own App Store listing).*

---

##### 1. Landing page

**Source:** rakuten.com (US homepage), per search snippets 2026-04-22. Direct fetch from CZ IP returns the EU regional chooser, not the US homepage (see section 5 - Geography).

- **Title tag / meta:** "Promo Codes, Coupons & Cash Back | Shop 3,500+ Stores!" [Data; source: Google SERP title for rakuten.com, 2026-04-22]
- **Hero tagline:** "Shop. Get Cash Back. Repeat." [Data; source: visible even on EU redirect page rendering of rakuten.com, 2026-04-22]
- **Social-proof headline:** "Since 1999, Rakuten has paid members over $3.6 billion in cash back" [Data; source: homepage copy as quoted by multiple reviewer sites 2025-2026; >12 months old for exact figure - flag staleness, likely higher now]
- **Store count:** "3,500+ stores" (both on homepage and App Store listing) [Data]
- **Category nav (top-level):** All Categories, Clothing, Accessories, Travel & Vacations, Beauty & Wellness, Shoes, Electronics, Home & Garden, Home Improvement, Pets, Auto & Tires, Baby & Toddler, Toys & Games, Sports/Outdoors & Fitness, Food/Drinks & Restaurants, Books/Music & Media, Flowers, Business Supplies & Services, Events & Entertainment, Gifts [Data; reviewer aggregations 2025-2026]
- **Hero callouts rotation** (typical, reviewer screenshots): featured-store tiles with live %-cash-back badge (e.g. "10% Cash Back"), "Double Cash Back" banners on select merchants, a "Daily Double" carousel [Inference from reviewer screenshots; freshness ~6-9 months]

##### 2. Signup funnel (fields + CTAs)

Rakuten's signup is minimal and famously frictionless - that is itself the positioning.

**Required fields (initial signup):**
- Email address [Data; multiple reviewer confirmations]
- Password (>=8 chars, must include a letter + number or special char) [Data; help.rakuten.com + reviewer confirmations]

**Social signup options:**
- Sign up with Google [Data]
- Sign up with Facebook [Data]
- Sign up with Apple [Data]

**NOT required at signup (deferred to first-payout time):**
- Name
- Mailing address
- Payment method (PayPal / Big Fat Check / Amex Membership Rewards / Bilt)
- Phone number
- No credit card, no bank account [Data; reviewer confirmations 2025-2026]

**Key CTA on landing / hero:** "Join Now" button, plus a secondary "Sign In" link [Data; reviewer screenshots]
**Join-page URL:** rakuten.com/join (and referral-coded variants `rakuten.com/r/<code>`) [Data]

**Friction analysis [Opinion]:** Email + password only is as low-friction as cashback signup gets. Honey and Capital One Shopping are comparable. Groupon Coupons signup currently asks for email + password too; Rakuten's differentiator is the deferred address/payment capture - users get to browse the logged-in experience and accumulate pending cash back before being asked for any PII beyond email.

##### 3. Welcome bonus + referral

###### Welcome bonus (current as of 2026-04-22)

- **Amount:** $50 cash back (or 5,000 Amex Membership Rewards points, or 5,000 Bilt points - user's choice set in account preferences) [Data; multiple reviewer sources Feb-Apr 2026]
- **Qualifying spend:** $50 in eligible Rakuten-tracked purchases within 90 days of signup [Data]
- **Offer window:** April 1, 2026 - June 30, 2026 (extended from a prior March 31, 2026 deadline) [Data; awardwallet.com + doctorofcredit.com 2026]
- **Must sign up via referral link** - direct rakuten.com signup without a referral code typically shows a lower bonus or none [Data; multiple reviewer confirmations]
- **Payout:** bonus credited to next quarterly payment cycle, typically within 60 days of the qualifying purchase clearing [Data]
- **Geography:** 50 US states + DC only (resident AND physically located) [Data; help.ebates.com terms]

###### Referral program (evergreen)

- **Structure:** double-sided $50 / $50 (referrer + referee both earn $50) [Data; aligned with current welcome bonus structure]
- **Referee qualifying condition:** same as welcome bonus ($50 spend in 90 days)
- **Referrer payout:** credited within 60 days of referee's qualifying purchase, added to next quarterly Big Fat Check
- **Share channels:** unique referral link shareable via text, email, social media - Rakuten generates a personalized URL
- **Cap:** "You may qualify for a Referral Bonus more than one time" - no stated maximum [Data]
- **Source:** rakuten.com/referral/default.do + help.ebates.com Refer-A-Friend Program Terms

###### The "Big Fat Check" (payment mechanic)

- **What it is:** Rakuten's brand name for the physical paper check mailed to members every quarter. Now one of four payout options (others: PayPal, Amex MR transfer, Bilt transfer). [Data]
- **Payment calendar (quarterly):**
  - **Feb 15:** earnings from Oct 1 - Dec 31
  - **May 15:** earnings from Jan 1 - Mar 31
  - **Aug 15:** earnings from Apr 1 - Jun 30
  - **Nov 15:** earnings from Jul 1 - Sep 30
- **Minimum threshold:** $5.01 confirmed cash back as of the payment-date cutoff [Data]
- **Marketing tone:** The "Big Fat Check" is arguably Rakuten's most distinctive brand asset - a playful, physical artifact that turns a pedestrian ACH/PayPal payout into an unboxing moment. It has its own dedicated blog content and social posts. [Opinion]

##### 4. How it works + Safari extension

###### "How it works" - pre-auth framing (3 steps)

Per rakuten.com/blog/rakuten-explained and consistent across help-center and reviewer recaps:

1. **Sign up** (free, email + password)
2. **Shop through Rakuten** (website, app, or browser extension - "always start your shopping trip through Rakuten so the visit is tracked")
3. **Get Cash Back** (quarterly payout via Big Fat Check, PayPal, Amex MR, or Bilt)

Reinforcing "why this works" paragraph: "Stores pay Rakuten for sending them shoppers, and Rakuten shares that money with its members as Cash Back."

###### Safari mobile extension - install page copy

**Page:** rakuten.com/help/article/safari-mobile-extension-faq-24111151607059

**Positioning sentence:** "Activate Cash Back directly on store sites, right from your mobile device" (also finds and applies coupons).

**Install steps (exact copy):**
1. Install the latest Rakuten iOS App (extension is bundled with the app - no separate download)
2. Open Safari
3. Tap the `aA` icon in the bottom-left of the address bar
4. Tap **Manage Extensions**
5. Turn on the toggle next to **Rakuten**, tap **Done**
6. Review permissions by tapping **Review** in the top right
7. Tap **Always Allow** for the first permission
8. Tap **Always Allow on Every Website** for the second permission

**Bundling note (verbatim):** "The Safari extension is powered by the Rakuten App. They are bundled together in one download."

**Android:** No Safari equivalent; Rakuten explicitly states the mobile extension "isn't available for Android yet" and directs Android users to the app.

**Post-install UX:** Rakuten shows an activation bubble on merchant domains when the user lands there in Safari; user taps to activate cash back for that session.

###### iOS App Store listing (rakuten.com/ios linked to id723134859)

- **App Store headline:** "Earn rewards & find coupons"
- **Rating:** 4.8 / 5 across 361K ratings [Data]
- **Size:** 147 MB
- **Min iOS:** 18.0+
- **Age rating:** 16+
- **Feature bullets:** stack cashback with sales/coupons/shipping/loyalty; auto-apply coupons at checkout; in-store + dining cashback (location-based); unlimited referral bonuses; multiple payout options (PayPal, check, gift card); detailed cashback status + payment tracking

##### 5. Pre-auth copy / positioning themes

Distilled themes the prospective user absorbs before they ever log in:

1. **"Shop. Get Cash Back. Repeat."** - three-word loop tagline. Reinforces habit-forming behavior (the flywheel is the brand).
2. **Scale + trust:** "$3.6B paid to members since 1999," "3,500+ stores" - numeric legitimacy.
3. **Free + simple:** reviewers universally lead with "it's free, it's simple." Signup = email + password only. No cards to link.
4. **Multiple payout currencies:** cash (PayPal / check) OR Amex MR OR Bilt - the travel/points crowd is explicitly courted. This is a meaningful differentiator vs. Honey and Capital One Shopping.
5. **Big Fat Check as brand artifact:** physical check mailer is a retention and word-of-mouth asset (literal photos of checks on social).
6. **Mobile-first + Safari extension:** Rakuten is the only major cashback player with a working iOS Safari Web Extension in the App Store ecosystem as of Apr 2026. Honey has an iOS app but no Safari extension parity; Capital One Shopping ships a Safari extension via their app too. [Inference; confirmed independently by the Safari Extension Competitors reference in Martin's memory.]
7. **Non-disclosure of the welcome bonus on the unauth homepage:** The $50 bonus is primarily surfaced through referral landing pages, blog posts, and points-blog marketing - not the cold homepage hero. [Inference from reviewer screenshots] This is a deliberate choice: Rakuten wants users to come in via a referral link so the referrer earns, OR to sign up cold and THEN see the bonus. Worth noting.

##### 6. Notes for Martin's manual capture (what to look for once logged in)

Please capture, ideally with screenshots, the following that only a logged-in user can see:

1. **Welcome email subject line + body:** exact copy, CTAs, any initial merchant recommendations, any cross-sell to the Safari extension, any "complete your profile" prompt for address/payment.
2. **First logged-in home dashboard:** is the $50 bonus counter visible? Does it show "$0 / $50 to unlock your bonus" progress UI?
3. **First merchant click UX:** what happens when you click a merchant tile from the logged-in homepage? In-app WebView? Redirect to Safari? Do they interstitial with "your cash back is now activated" before the merchant loads?
4. **Address + payment-method prompts:** when does Rakuten ask for these? At signup? At first purchase? At first payout threshold? This is the critical friction-timing question.
5. **Extension install nudge flow:** logged-in users on desktop reportedly see a "Install Button for free" banner. What's the exact copy and placement? Does it appear on mobile Safari or only desktop?
6. **Safari extension on Nike.com (or any eligible merchant):** activation bubble copy, visual treatment, how many taps to activate, does it auto-apply coupons or just surface them, what's the "your cash back is active" confirmation state.
7. **Account settings payment options UI:** how are Big Fat Check / PayPal / Amex MR / Bilt presented? Default? Upsell framing for points?
8. **Referral share UI:** does the share CTA show your unique URL and a "copy" button? Any prefilled text for SMS/email share?
9. **Any geo-gate once logged in from CZ:** does the logged-in experience work from a CZ IP, or does it soft-block merchant redirects?
10. **Cookie banner:** from a CZ IP on any subpage (not just rakuten.com root), does GDPR/cookie consent banner appear? What categories are presented?

##### 7. Data gaps (what is human-only)

Items in this report that could NOT be validated from public pre-auth sources and NEED manual capture:

- Exact welcome-email content (subject, body, CTA buttons)
- Logged-in home dashboard screenshot + bonus progress UI
- Exact copy of the "install the extension" in-product nudge
- Whether the Safari extension respects Safari's privacy mode / Intelligent Tracking Prevention quirks
- First-merchant activation UX specifics (interstitial? toast? redirect?)
- Time-to-first-payout-prompt (how long until Rakuten asks for address/payment method)
- A/B variants: Rakuten runs extensive homepage tests; this capture represents a single temporal snapshot of public copy and may not match what US users currently see
- Visual design / color / typography specifics for the logged-in experience

##### 5b. Geography gate (supplementary)

**Critical finding:** From a Czech Republic (EU) IP, `rakuten.com`, `rakuten.com/join`, `rakuten.com/referral/default.do`, and `rakuten.com/blog/*` all return the same minimal **EU regional chooser page**, NOT the US site. The chooser shows:
- Tagline "Shop. Get Cash Back. Repeat."
- Question: "I live in Europe. Where can I use Rakuten?"
- Three country links: **France, Germany, Spain**
- "Member Services" help link

**What this means for Groupon competitive analysis:**
- Rakuten US is effectively **closed to EU-resident users**. Czech users cannot sign up even via VPN without address verification failing.
- The EU Rakuten properties (rakuten.fr, rakuten.de, rakuten.es) are *separately branded / separately operated* cashback + marketplace businesses, not a unified rakuten.com experience.
- For Groupon's Coupons vertical, this is a competitive *opening* in EU markets - Rakuten US's referral + Big Fat Check brand equity does not transfer.
- Help-center articles (help.rakuten.com/*) and blog articles (rakuten.com/blog/*) ARE accessible content-wise via some paths but the transactional pages are not.

[Data; direct test from CZ IP 2026-04-22 via WebFetch, multiple URLs tested]

##### 8. Sources

All accessed 2026-04-22 unless noted. Freshness flagged where staleness is material.

**Rakuten-owned pages:**
- https://www.rakuten.com/ - Homepage (EU redirect from our IP; US content inferred from SERP title + reviewer snapshots)
- https://www.rakuten.com/join - Join page (EU redirect from our IP)
- https://www.rakuten.com/referral/default.do - Referral landing (EU redirect from our IP)
- https://www.rakuten.com/help/article/the-rakuten-welcome-bonus-new-member-faqs-360002117247 - Welcome bonus FAQ
- https://www.rakuten.com/help/article/safari-mobile-extension-faq-24111151607059 - Safari extension install steps
- https://www.rakuten.com/help/article/when-will-i-get-paid-360002117667 - Payment schedule
- https://www.rakuten.com/help/article/signing-into-my-account-115009256128 - Signin fields reference
- https://www.rakuten.com/blog/rakuten-big-fat-check-schedule-faqs/ - Big Fat Check schedule (EU redirect from our IP)
- https://www.rakuten.com/blog/refer-a-friend/ - Refer a Friend (EU redirect from our IP)
- https://www.rakuten.com/blog/rakuten-explained-how-it-works-every-way-you-can-shop/ - How it works
- https://apps.apple.com/us/app/rakuten-cash-back-deals/id723134859 - iOS App Store listing
- https://help.ebates.com/hc/en-us/articles/46542221812115-Rakuten-Card-Referral-Bonus-Terms - Referral program terms

**Third-party reviewer sources (for US-site content inaccessible from EU):**
- https://awardwallet.com/shopping/rakuten-rewards/ - Feb 2026 $50 bonus confirmation
- https://onemileatatime.com/deals/rakuten-new-member-bonus/ - Bonus deadline tracking
- https://thepointsguy.com/news/rakuten-referral-bonus-online-shopping/ - $50 bonus mechanic
- https://20somethingfinance.com/rakuten-40-referral-bonus-promo/ - Historical bonus tracking
- https://20somethingfinance.com/rakuten-50-bonus/ - Feb 2026 bonus terms
- https://www.doctorofcredit.com/rakuten-50-5000-referral-bonus-highest-ever/ - Deal community confirmation
- https://financebuzz.com/rakuten-review - 2026 review, updated Aug 2025
- https://millennialmoney.com/rakuten-review/ - 2026 review
- https://upgradedpoints.com/travel/rakuten-ebates-review/ - Signup walkthrough
- https://www.rakuten.ca/button/safari/walkthrough - Safari install walkthrough (CA site, same UX)

**Privacy / GDPR context:**
- https://www.rakuten.com/help/article/privacy-policy - US privacy policy
- https://global.rakuten.com/corp/cookie_policy/ - Corporate cookie policy
- https://rakuteninternational.com/privacy-policy - EMEA-scoped policy

**Cross-reference (Martin's memory):**
- reference_safari_extension_competitors.md - prior iOS Safari Web Extension competitive context


---

### capital-one-shopping-preauth

#### Capital One Shopping - Public Pre-Auth User Experience

*AI-captured pre-authentication evidence for Groupon competitive intelligence*
*Access date: 2026-04-22 (fetched 2026-04-21 from CZ IP, Prague)*
*Scope: Public pages only - no account creation, no logged-in session*
*Companion docs: `raw/capital-one-shopping-mechanics.md` (deep teardown), `raw/signup-evidence/capone/public-capture.md` (prior capture, superseded in part by this file)*

---

##### 1. Executive Summary - what pre-auth users see

**The single biggest headline:** The current (Apr 2026) sign-in flow is **passwordless / magic-link by default**. The sign-in page shows "Send me a sign in link" as the primary CTA, with "Sign in a different way" as a secondary option. This is a structural change from the "email + password" model captured in prior rounds. [Data, High - direct WebFetch 2026-04-21]

**The second biggest headline:** There is **no dollar-amount signup bonus on the pre-auth homepage hero**. The $80/$80 referral program exists but is only reachable via a referral link, not via organic visits. A different "$10 spend in 21 days" bonus appears only on the iOS App Store listing, not on the web homepage. [Data, High]

**The third headline:** The "1 Credit = $1" soft-currency mechanic, the ~50 gift card retailer list, and all redemption catalog details are **auth-gated**. Pre-auth prospects see "Rewards" framing with implied dollar equivalence (e.g. "+2% back at Target", "up to 16.5% back at DoorDash") but no explicit currency explanation. [Data, High]

**Trust posture:** Despite the Dec 2025 $4M affiliate-commission class action (preliminary approval Dec 18, 2025; final hearing Jun 10, 2026; claim deadline Apr 17, 2026 - 5 days before this capture), Cap One has **not added explicit post-settlement affiliate-disclosure language** to the consumer-facing Terms of Service (effective Nov 19, 2025) or Privacy Policy (effective Feb 18, 2026). The ombudsman + compliance review commitments live only in legal filings. [Opinion, High - based on direct fetch + settlement documents]

---

##### 2. Per-Dimension Findings

###### 2.1 Current headline install incentive (April 2026)

**Web pre-auth homepage:** No dollar-amount signup bonus visible in the hero. Homepage copy focuses on "daily offers", auto-applied coupons, and per-merchant reward percentages. [Data, High - WebFetch 2026-04-21, https://capitaloneshopping.com/]

**Referral program (gated behind referral link):** $80 for referrer + $80 for new user. Requires extension install within 7 days of account creation, full permissions, on a device that has never had the extension installed before. Retention gate: use the extension for 90 days. Referrer cap: $1,900 (up from $500 earlier in 2024). US-only, 18+, new users only. [Data, High - Doctor of Credit Feb 24 2026, Frequent Miler, Thrifty Traveler Mar 30 2026, Upgraded Points Apr 2026, corroborated via April 2026 WebSearch round]

**Separate iOS Safari extension bonus:** App Store description states "add the Safari Shopping extension, allow access on all sites, create or log in to your account, verify your email and **spend $10 in 21 days** to be eligible for your bonus" with rewards "issued within 30 days". Dollar amount not disclosed in the App Store copy. [Data, High - WebFetch apps.apple.com 2026-04-21]

**Historical $45 reference:** The "$45" figure Dusan anchors to does NOT appear in Doctor of Credit's verified historical list (which tracks $30/$40/$50/$60/$75/$80/$200 variants). The closest documented variant was "$40 bonus after spending $15 within 90 days" from a Dec 2024 public link. The "$45" figure appears primarily in SEO blog content (Saint Augustine's, Martins Flooring) of uncertain authority. [Data, High - cross-verified]

**YMMV nature:** All historical amounts are targeted/YMMV - many users cannot access any referral bonus on any given day. [Data, High]

**Recommendation for Groupon sizing:** Reframe from "$45 anchor" to **"$40-$80 range with 90-day retention gate, US-only, YMMV"**. The retention mechanic is more strategically interesting than the dollar amount. [Opinion, High]

###### 2.2 Signup form fields

**Current state (2026-04-21):** The sign-in page at `capitaloneshopping.com/sign-in` is passwordless by default. [Data, High]

Verbatim:
> "Welcome back"
> "Sign in to continue saving"
> "Send me a sign in link"
> "We'll email you a secure link to sign in instantly - no password needed."
> "Sign in a different way" (secondary link)
> "Create Account" (new user path)

Fields visible pre-auth: **email only** for the magic-link flow. No password field, no phone number, no date-of-birth, no age verification, no US-residency toggle, no T&C checkbox visible on the sign-in widget. No social login (Google, Apple, Facebook) shown. [Data, High]

**Homepage inline widget:** The homepage displays a smaller signup widget that collects email, then prompts "Next step please add a password" / "Continue" on a subsequent screen. This suggests the web flow still supports a password alternative if users choose "Sign in a different way". [Data, High - WebFetch homepage 2026-04-21]

**DATA GAP:** Cannot verify whether the full signup flow post-email collects additional fields (age, location, payment method) without creating an account. [Gap, High]

###### 2.3 "How it works" messaging

**No dedicated /how-it-works page exists.** WebFetch to `capitaloneshopping.com/how-it-works` returns 404. [Data, High - verified in prior round, still 404]

The value proposition is conveyed via:

1. **Homepage hero:** "Save with your daily offers!" / "It's kinda genius, join now for free." [Data, High - prior capture, still live]
2. **Homepage value-prop block (verbatim):**
   > "Capital One Shopping gets you better offers, automatically applies coupon codes at checkout, and lets you know when prices drop on products you've viewed and purchased."
3. **Capital One editorial page** (`capitalone.com/learn-grow/money-management/capital-one-shopping/`) - this is the closest thing to a "how it works" explanation, with section headings: What is Capital One Shopping / Is there a fee / How does Capital One Shopping work / Coupon codes / Price comparisons / Price-drop notifications / Rewards / How to redeem / Do Rewards expire. [Data, High]

**Implicit 3-step messaging** (inferred from the combination of hero, offer cards, and editorial page):
- Step 1: Install the extension / download the app
- Step 2: Shop normally - coupons apply automatically, prices are compared cross-retailer
- Step 3: Earn Rewards redeemable for gift cards

Cap One does NOT present this as a numbered "how it works" flow on the pre-auth homepage. [Data, High] This is a structural design choice: the homepage is offer-led, not mechanic-led.

###### 2.4 Shopping Credits explanation pre-auth

**"1 Credit = $1" is NOT visible on any Cap One pre-auth public page.** [Data, High - verified across /, /help, /rewards (404), /gift-cards (404), /our-terms/, and editorial]

The editorial page uses "Rewards" consistently. The ToS states users must accumulate "a minimum balance of $1.00 worth" of Rewards to redeem, and caps redemption at "$500.00 worth of Shopping Rewards in any single transaction" - but does not define a "credit" unit. [Data, High - direct ToS fetch]

The "1 Credit = $1" framing comes from third-party review content (Frequent Miler, Upgraded Points, The Points Guy, FinanceBuzz). It is **Groupon-internal research framing**, not Cap One marketing language. [Data, High]

**Implication:** Groupon's "Bucks" soft-currency concept should not assume prospects understand a "1 unit = $1" frame from Cap One precedent. Cap One hides the mechanic behind "Rewards" until account creation. [Opinion, High]

###### 2.5 Redemption catalog messaging

**The gift-card-only constraint is NOT explicitly shown pre-auth.** The `/rewards` and `/gift-cards` pages both return 404 to unauthenticated visitors. [Data, High - verified in prior round]

Pre-auth users see only the outbound-shopping offer cards (e.g. "+2% back at Target") which create an implicit cashback expectation. The fact that Rewards can ONLY be redeemed as digital gift cards (no cash-out, no statement credit, no bank deposit) is auth-gated. [Data, High]

The Capital One editorial page uses the phrase "redeem your Capital One Shopping Rewards for digital gift cards from dozens of retailers" - "dozens" is the specific hedge language; no explicit "50+ retailers" number is published. [Data, High]

**Implication:** Cap One is strategically quiet about the gift-card-only constraint pre-auth. This is a retention-hostile mechanic that would hurt signup conversion if disclosed. [Opinion, High]

###### 2.6 Safari extension install page copy

**iOS main app listing** (`apps.apple.com/us/app/capital-one-shopping-save-now/id1089294040`):
- Star rating: **4.9 stars** [Data, High]
- Ratings count: **1.6M ratings** [Data, High - April 2026 refresh]
- Developer: **Wikibuy, LLC** (legacy branding) [Data, High]
- Version: **2.127.0** [Data, High]
- Last update: **4 days ago** (2026-04-17) [Data, High]
- Size: 161.5 MB [Data, High]
- Age rating: 4+ [Data, High]
- Category: Shopping [Data, High]
- Ranking: "#2 in Shopping Top Free Apps" claim from prior research rounds is **not directly displayed on the current App Store page** - likely valid but not primary-source verified this round. [Inference from prior research, Medium confidence]

**Verbatim app description (signup bonus):**
> "Add the Safari Shopping extension, allow access on all sites, create or log in to your account, verify your email and spend $10 in 21 days to be eligible for your bonus. 100% free for everyone - no Capital One bank or credit card account required!"

**Verbatim value prop:**
> "Automatically applies coupons and promo codes at checkout"
> "Earns rewards redeemable for gift cards"
> "Compares prices including shipping"
> "Notifies of price drops"

**Privacy disclosures:** App collects identifiers, purchase history, contact info, search/browsing history, payment information, and usage data for advertising, analytics, and personalization purposes. [Data, High - direct fetch]

**Dedicated iOS Safari extension SKU** (`id1477110326`): This separate listing exists but has **no aggregated rating** displayed ("This app hasn't received enough ratings or reviews"). Usage is concentrated in the main app, not the standalone extension SKU. [Data, High - prior capture]

###### 2.7 Chrome Web Store listing

**DATA GAP - CZ IP blocks Chrome Web Store directly.** EU consent redirect intercepts the fetch. chrome-stats.com mirror returned 403. [Gap, High]

**Indirect evidence (April 2026 WebSearch):**
- User count: "over 6 million users" (consistently cited across review sites April 2026) [Data, Medium-High]
- Review count: "over 10,000 reviews" (review-site citation); one source reports 91,392 ratings [Data, Medium - discrepancy unresolved]
- Star rating: 4.5 / 5 (most cited); one source says 4.7 [Data, Medium - discrepancy unresolved]
- Last updated: **April 20, 2026** (within 2 days of capture - indicates active maintenance) [Data, High]

**Recommendation:** US-IP verification needed to resolve review-count discrepancy. [Gap, High - carried forward from prior round]

###### 2.8 iOS App Store listing refresh

- **Current rating (2026-04-21):** 4.9 stars, 1.6M ratings [Data, High]
- **Prior research anchor:** 4.9 / 960K historical [Data, from prior rounds]
- **Growth:** ~66% growth in ratings count over recent period (960K -> 1.6M). This is a strong retention / usage signal. [Inference, High]
- **Update cadence:** 3-4 days between releases (v2.127.0 released 2026-04-17) [Data, High]
- **What's New text:** "Performance improvements" - no feature-launch signaling in public release notes [Data, High]

###### 2.9 Trust / privacy messaging (especially post-Dec 2025 class action)

**Class action status:** $4M settlement, preliminary approval Dec 18 2025, claim deadline **Apr 17 2026** (5 days before this capture), final approval hearing **Jun 10 2026**. Covers affiliate commissions allegedly diverted from content creators. [Data, High - ABA Banking Journal, classaction.org, InfluencerMarketingClaims.com]

**Consumer-facing pages - no post-settlement update language:**
- **Terms of Service** (`/our-terms/terms-of-service`): Effective **Nov 19, 2025** (predates preliminary approval by 1 month). Contains: `"We earn a commission when you make eligible purchases from certain Merchants using the Shopping Browser Companion or Mobile App and we may share those commissions with you as Rewards."` Class action waiver is **merchant-scoped only**, not user-scoped. [Data, High]
- **Privacy Policy** (`/our-terms/privacy-policy`): Effective **Feb 18, 2026** (post-settlement). Contains: `"Capital One Shopping does NOT sell your personal information to any third party for the third party's own marketing purposes"` and `"we exchange lists of user email addresses with other Capital One affiliates located in the United States, Canada, and the UK"`. **Does NOT contain** explicit post-settlement language about last-click attribution or competing-extension cookie behavior. [Data, High]

**Homepage affiliate disclosure (visible pre-auth):**
> "Capital One Shopping earns a commission when you make eligible purchases from merchants and we may share those commissions with you as rewards."

This line appears in homepage footer context. It is the standard commission-disclosure frame, not post-settlement transparency. [Data, High]

**The ombudsman + compliance-review commitments live in the settlement filing, not in consumer pages.** This is a material gap: Cap One's legal-side commitments are not yet reflected in marketing-facing trust language. [Opinion, High]

**Implication for Groupon:** Groupon can pre-empt this gap by adding clean, consumer-facing affiliate-disclosure language (e.g. "We respect the affiliate link you clicked first") from day 1 - differentiation without regulatory pressure. [Opinion, High]

###### 2.10 Capital One bank tie-in messaging

**Editorial page verbatim:**
> "It's free for everyone, even people who aren't already Capital One customers."

**iOS App Store description verbatim:**
> "100% free for everyone - no Capital One bank or credit card account required!"

**Homepage:** No Capital One bank account promo visible. No "Apply for a Cap One card" upsell on pre-auth pages. [Data, High]

**Strategic observation:** Cap One Shopping is positioned as **standalone acquisition funnel**, NOT as a Cap One banking tie-in. This is consistent with Walt Coon's original Wikibuy DNA (acquired 2018, ~$2M users at acquisition). [Opinion, High]

**Backend monetization (not disclosed pre-auth):** Cap One uses Cap One Shopping's first-party data via Rakuten Advertising's Audience Engine for credit-card customer acquisition targeting. This is the real monetization but is not visible pre-auth. [Data, Medium-High - Rakuten case study]

---

##### 3. Material Changes vs Prior Capture (2026-04-21 prior round)

1. **Sign-in flow is now passwordless-first.** Prior capture noted "Email + Password" as the form-field default. Current fetch (2026-04-21) shows "Send me a sign in link" as primary, password as secondary. This is a structural change within the past ~24 hours of capture time or was missed in prior capture. [Data, High - verify against prior screenshot if available]

2. **iOS main app ratings grew from 960K (prior research anchor) to 1.6M (current).** ~66% growth. Indicates sustained usage / install velocity. [Data, High]

3. **Chrome Web Store extension updated 2026-04-20** (2 days before fetch). Active maintenance signal. [Data, High]

4. **Class action claim deadline just passed (Apr 17, 2026).** Cap One has not yet propagated settlement language to consumer pages. Watch Jun 10, 2026 final hearing. [Opinion, High]

---

##### 4. Data Gaps (carried forward + new)

| Gap | Severity | Recommendation |
|---|---|---|
| Chrome Web Store user count / review count / rating (CZ IP blocked) | High | US-IP fetch or reviewer screenshot |
| Full signup flow post-email (age, location, payment? collected?) | Medium | Human-in-the-loop signup capture |
| Exact dollar amount for "$10 in 21 days" iOS extension bonus | Medium | Human signup - disclosure appears post-install |
| Gift card retailer list (auth-gated) | High | Human logged-in capture |
| Welcome email cadence + copy | High | Human signup - email inbox |
| "#2 in Shopping Top Free Apps" ranking verification | Low | App Store ranking snapshot service |
| 91K vs 10K Chrome review-count discrepancy | Low | US-IP fetch |

---

##### 5. Recommendations for Groupon

###### 5.1 Rebase the $45 anchor
[Opinion, High] Drop "$45" as a fixed reference. Use **"$40-$80 range with 90-day retention gate, US-only, YMMV-targeted"**. The retention gate is the strategically interesting design element - it converts bonus-hunters into habit-formed users. An A/B between retention-gated ($80) and spend-gated ($10 in 21 days) would be informative.

###### 5.2 Don't market "soft currency transparency"
[Opinion, High] Cap One hides "1 Credit = $1" behind auth. The pre-auth hook is "daily offers + coupons + price match", not currency mechanics. Groupon's Bucks pre-auth marketing should mirror this: lead with dollar savings on offers, not with soft-currency transparency.

###### 5.3 Consider passwordless as a default
[Opinion, Medium] Cap One's current sign-in flow is magic-link-first. This lowers activation friction. Groupon should evaluate this against the "commitment tax" argument (making users invest in a password may improve day-7 retention).

###### 5.4 Pre-empt affiliate-disclosure regulation
[Opinion, High] Cap One's consumer pages do NOT reflect settlement commitments. Groupon can ship clean affiliate-disclosure language from day 1 - a differentiator.

###### 5.5 Bundle, don't fragment SKUs
[Opinion, High] Cap One's standalone iOS Safari extension SKU has zero ratings; all reviews are in the main iOS app (4.9 / 1.6M). Groupon's iOS Safari extension should be bundled inside a primary Groupon app, not a standalone SKU.

###### 5.6 Auth-gate the redemption catalog
[Opinion, Medium-High] Cap One does not show the 50+ gift card list pre-auth. This is a commitment tax: users install + authenticate before discovering the redemption constraint. Groupon should consider the same posture.

###### 5.7 Two parallel activation gates exist
[Data, High] Web referral: 90-day retention, no purchase required. iOS extension: $10 spend in 21 days. Groupon should A/B test both structures - they attract different user populations.

---

##### 6. Sources (all fetched / verified 2026-04-21 or April 2026)

###### Primary (direct fetch)
1. `https://capitaloneshopping.com/` - homepage [2026-04-21]
2. `https://capitaloneshopping.com/sign-in` - sign-in / signup [2026-04-21] - **key change: passwordless default**
3. `https://capitaloneshopping.com/our-terms/terms-of-service` - ToS effective Nov 19, 2025 [2026-04-21]
4. `https://capitaloneshopping.com/our-terms/privacy-policy` - Privacy Policy effective Feb 18, 2026 [2026-04-21]
5. `https://capitaloneshopping.com/help` - help center (structural only; articles not accessible via WebFetch)
6. `https://apps.apple.com/us/app/capital-one-shopping-save-now/id1089294040` - iOS main app [2026-04-21]
7. `https://apps.apple.com/us/app/capital-one-shopping-extension/id1477110326` - iOS Safari extension SKU (prior round, no aggregated rating)
8. `https://www.capitalone.com/learn-grow/money-management/capital-one-shopping/` - editorial

###### Third-party corroboration (April 2026)
9. `https://www.doctorofcredit.com/join-capital-one-shopping-get-10-after-spending-10/` - Feb 24, 2026 updated
10. `https://frequentmiler.com/capital-one-shopping-offering-80-referral-bonus-for-both-sides/` - $80/$80 + $1,900 cap
11. `https://thriftytraveler.com/deals/credit-card/capital-one-shopping-referral-offer/` - Mar 30, 2026
12. `https://upgradedpoints.com/news/capital-one-shopping-referral/` - new links April 2026
13. `https://dannydealguru.com/capital-one-shopping-signup-bonus/` - signup bonus Apr 2026
14. `https://monkeymiles.boardingarea.com/capital-one-shopping/` - $80 referral April 2026
15. `https://www.biblemoneymatters.com/capital-one-shopping-review/` - Chrome Web Store stats 2026
16. `https://financebuzz.com/capital-one-shopping-review` - reviews 2026
17. `https://millennialmoney.com/capital-one-shopping/` - review 2026
18. `https://www.thepennyhoarder.com/save-money/capital-one-shopping-review/` - reviews
19. `https://bold.org/resources/capital-one-shopping-review/` - reviews
20. `https://cleverlyfrugal.com/capital-one-shopping-review/` - uneven tracking review 2026

###### Class action / legal
21. `https://www.influencermarketingclaims.com/` - settlement site
22. `https://www.prnewswire.com/news-releases/if-you-advertised-online-with-merchants-and-affiliate-networks-who-partnered-with-capital-one-shopping-...` - settlement notice
23. `https://www.classaction.org/news/capital-one-settlement-ends-affiliate-marketing-commission-class-action-lawsuit` - settlement
24. `https://bankingjournal.aba.com/2026/01/virginia-district-court-grants-preliminary-approval-for-settlement-in-influencer-lawsuit-against-capital-one/` - ABA Jan 2026
25. `https://openclassactions.com/settlements/capital-one-shopping-affiliate-settlement.php` - settlement details
26. `https://topclassactions.com/lawsuit-settlements/lawsuit-news/capital-one-hit-with-class-action-over-allegedly-unpaid-cashback-rewards/` - secondary suit (unpaid cashback)

###### Web Store (indirect, CZ IP blocked)
27. `https://chromewebstore.google.com/detail/capital-one-shopping-save/nenlahapcbofgnanklpelkaejcehkggg` - blocked, via third-party mirror

---

##### 7. Confidence Summary

| Finding | Confidence | Basis |
|---|---|---|
| Passwordless sign-in is current default | High | Direct fetch 2026-04-21 |
| No dollar signup bonus on homepage hero | High | Direct fetch |
| $80/$80 referral with 90-day retention is current structural offer | High | 5+ third-party sources April 2026 |
| iOS Safari extension uses $10-in-21-days gate separately | High | Direct App Store fetch |
| "$45" is NOT a current headline | High | Doctor of Credit historical list |
| "1 Credit = $1" NOT visible pre-auth | High | Verified across all public pages |
| Retailer list auth-gated | High | /rewards and /gift-cards both 404 |
| iOS 4.9 / 1.6M ratings | High | Direct fetch 2026-04-21 |
| Chrome 6M+ users, 4.5-4.7 rating | Medium-High | Indirect - CZ IP blocked |
| Class action $4M, Apr 17 claim deadline, Jun 10 hearing | High | Multiple legal sources |
| No post-settlement consumer-page language | High | Direct fetch Privacy + ToS |
| Cap One banking tie-in NOT required or promoted pre-auth | High | Editorial + App Store + homepage |
| Standalone iOS Safari extension SKU has 0 aggregated ratings | High | Direct fetch prior round |

---

**END OF PRE-AUTH CAPTURE**


---

### honey-preauth

#### Honey - Public Pre-Auth Capture
*Captured 2026-04-22 via public web, no account created*

##### Headline (2 sentences)
PayPal Honey's public funnel continues to pitch a 17M+ member "find deals, earn cash back, compare prices" value prop at joinhoney.com, with a "Join" CTA and PayPal SSO as the primary signup path. The funnel shows no visible post-scandal trust-recovery messaging despite Rakuten/Impact.com/Awin terminations in Jan 2026 and the active class action filed Jan 5, 2026.

##### Landing + signup funnel
- [Data] Primary CTA: "Join" button top-right of joinhoney.com; auth flow at `joinhoney.com/auth`.
- [Data] Signup options surfaced pre-register: PayPal account (primary), plus email/Google/Apple (per standard PayPal-era Honey auth page). SSO is the pushed path - reduces form friction and ties Honey identity to PayPal wallet.
- [Data] Value prop copy: "automatically searches for and tests available coupon codes at checkout on 30,000+ popular sites."
- [Estimate] No cash welcome-offer banner surfaced in April 2026 search results (no "$5 welcome" or "$10 bonus" copy detected on landing). Honey historically has NOT used a SUB like Rakuten/Capital One - they rely on coupon-hunter value prop + Honey Gold accrual.
- [Data] Separate acquisition LP: `get.joinhoney.com/page/dr-us-simplified-yellow-general/` - direct-response variant, "simplified yellow" branding.

##### PayPal app bundle path
- [Data] help593 article (`paypal.com/us/cshelp/article/help593`) not directly surfaced in this search round, but `help.joinhoney.com/article/302` ("What does Honey joining PayPal mean for Members") confirms: users can "use their PayPal account to join Honey on Chrome, iOS, and Android."
- [Opinion] PayPal app bundling is the strongest remaining acquisition channel for Honey post-Chrome bleed - it bypasses Chrome Web Store trust signals entirely. Martin should manually capture the exact in-PayPal-app entry point (likely a "Rewards" or "Shop" tab).

##### Chrome / iOS listings (current counts)
- [Data] Chrome Web Store rating: 4.6 stars (listing: `bmnlcjabgnpnenekpadlanbbkooimhnj`).
- [Data] User-count trajectory: Honey lost ~8M Chrome users by end of 2025 per reporting - consistent with the 20M -> 12M claim in the brief.
- [Estimate] Current Chrome install count (April 2026): not surfaced in this search round; requires direct scrape of store listing - likely in 10-13M range given trajectory.
- [Data] iOS App Store: not surfaced in this search round. Martin should manually capture - the PayPal-branded iOS app is the bundled path.
- [Data] Firefox addon listed at addons.mozilla.org/en-US/firefox/addon/honey - also available on Safari, Edge, Opera.

##### Honey Gold + T&Cs flags
- [Data] Honey Gold has been rebranded/merged into "PayPal Rewards" points: "Members may earn points through PayPal Rewards just for shopping on participating sites, even if there isn't a coupon code available."
- [Estimate] The historical "not your property, not money, no value" T&C clause was not surfaced in this search round. Status unconfirmed - requires direct T&C scrape. Given the class action exposure, PayPal legal may have softened or re-located this language, but the points-are-not-cash framing is structurally unchanged (points, not dollars).
- [Opinion] The Honey Gold -> PayPal Rewards rebrand is itself a trust-recovery move: ties the liability to PayPal's balance-sheet-backed rewards program rather than a standalone Honey scrip.

##### Post-scandal posture
- [Data] No visible trust-recovery banner or FAQ update on joinhoney.com landing as of April 2026 searches. No "our response" page surfaced.
- [Data] PayPal publicly acknowledged (Jan 12, 2026) code designed to evade affiliate network detection, and stated it had been disabled (per hellopartner.com/2026/01/15 coverage).
- [Data] Removed from Rakuten (Jan 12, ~2000 retailers lost), Impact.com, Awin within weeks.
- [Opinion] Public-facing silence is the strategy - legal exposure from the Jan 5 amended complaint (10 named plaintiffs, specific Bergdorf contracts) makes any public statement discoverable.

##### Droplist feature page
- [Data] Droplist (price-drop watchlist) is the uncontroversial mechanic - not affiliate-commission-dependent, purely user-utility. Not surfaced as a standalone landing page in this search round; lives inside the extension UX post-install. Martin should manually capture the in-extension Droplist flow.

##### Notes for Martin's manual capture
1. Screenshot the PayPal mobile app "Shop"/"Rewards" tab - the bundled Honey entry point.
2. Screenshot the iOS App Store listing: rating, review count, top negative reviews (likely scandal-tagged).
3. Pull current Chrome Web Store install count (exact number) and skim the top 10 recent reviews for scandal references.
4. Scrape current joinhoney.com T&Cs - search for "not your property," "no cash value," and "PayPal Rewards" clauses.
5. Capture the Droplist in-extension flow - it's the defensible mechanic Honey could double down on.
6. Check if any "our commitment" / "what we've changed" page exists at `help.joinhoney.com` post-Jan 2026.

##### Sources (URLs)
- https://www.joinhoney.com/auth (access 2026-04-22)
- https://help.joinhoney.com/article/39-what-is-the-honey-extension-and-how-do-i-get-it (access 2026-04-22)
- https://help.joinhoney.com/article/302-what-does-honey-joining-paypal-mean-for-members (access 2026-04-22)
- https://chromewebstore.google.com/detail/honey-automated-coupons-r/bmnlcjabgnpnenekpadlanbbkooimhnj (access 2026-04-22)
- https://www.paypal.com/us/digital-wallet/ways-to-pay/paypal-honey (access 2026-04-22)
- https://get.joinhoney.com/page/dr-us-simplified-yellow-general/ (access 2026-04-22)
- https://en.wikipedia.org/wiki/PayPal_Honey (access 2026-04-22)
- https://addons.mozilla.org/en-US/firefox/addon/honey/ (access 2026-04-22)
- https://ppc.land/honey-loses-access-to-2-000-clients-after-rakuten-network-termination/ (access 2026-04-22)
- https://hellopartner.com/2026/01/15/paypal-responds-to-honey-stand-down-allegations-and-rakuten-removal/ (access 2026-04-22)
- https://www.lieffcabraser.com/consumer/honey-paypal/ (access 2026-04-22)
- https://allaboutlawyer.com/paypal-securities-fraud-honey-class-action-lawsuit-2026/ (access 2026-04-22)
- https://thepma.org/key-takeaways-from-honey-browser-lawsuit-dismissal/ (access 2026-04-22)
- paypal.com/us/cshelp/article/help593 - referenced in brief, not directly retrieved this round


---

## Part 8 - Slickdeals partnership workstream

## Slickdeals - Partnership Feasibility for Goods Replacement
*Standalone workstream | 2026-04-21 | Prepared for Dusan, Rebecca, Adam, Groupon Product Leadership*

### TL;DR

**Conditional Go - as a 90-day embedded Featured Deals pilot (Option B), NOT as a Goods replacement owner.**

Dusan's thesis that Slickdeals is the #1 partner for replacing Goods on Groupon core is defensible IF the goal is "refill the Goods surface with credible physical-goods deals fast." But the framing "replace Goods" misdiagnoses the problem:

1. Goods failed on inventory / fulfilment economics, not on curation.
2. A UGC feed solves demand-side deal discovery, which is a different problem.
3. The community lives on slickdeals.net. If the partnership ends, Groupon has zero residual audience. That is the DEAL BREAKER flagged in the original brief.

Slickdeals can plausibly power an **affiliate storefront** embedded into Groupon, but cannot provide a **curated owned merchandising surface**, and cannot transfer its community moat. Any contract must reflect that.

---

### Core facts (2026 state)

| Fact | Value | Source | Confidence |
|---|---|---|---|
| Ownership | Goldman Sachs Merchant Banking + Hearst Corp | Since June 2018, $500M deal; Bloomberg, PR Newswire, Fried Frank 2018 | High |
| PE hold length | ~8 years, unusually long | Same | High |
| Revenue 2025/2026 | $35-50M (working range $45-55M 2026) | enactsoft, martini.ai, secondary press | Medium |
| Commission rate range | 1-8.5% of GMV, retailer-specific up to 15% | HBS case, enactsoft | Medium-High |
| MAU | 12M | Slickdeals corp | High |
| DAU/MAU ratio | 40% (excellent for consumer apps) | LA Business Journal 2024 | High |
| Monthly visitors | 25M / >1B annual | SimilarWeb via corp | High |
| Mobile installs | 5M+ iOS + Android combined | Slickdeals corp | High |
| Employee count | ~200-220 | Prior research, not re-confirmed 2026 | Medium |
| Audience gender | 62.6% male / 37.4% female | SimilarWeb | High |
| Audience age | 70% aged 18-44, largest cohort 25-34 | Slickdeals corp | High |
| Geography | US-concentrated, top 100 US sites | SimilarWeb | High |
| AI product signal | AWS SageMaker personalisation shipped 2025, +7% merchant outbound click lift | AWS re:Invent 2025 SMB206 | High |
| March 2025 iOS redesign | Shipped | Slickdeals forum 2025-03-27 | High |
| Leadership direction | CEO Neville Crawley pivoting upper-funnel brand advertising | LA Business Journal 2024 | High |

---

### Strategic assessment

#### 1. Audience overlap with Groupon - compatible, not cannibalising

- **Gender skew is inverted.** Slickdeals is male-heavy (63%); Groupon is female-heavy. [Data, High]
- Age overlap exists in the 25-44 band. Slickdeals' core is younger tech/CE; Groupon's is older value-conscious local.
- **Intent is different:** SD users hunt one-off product bargains; Groupon users buy repeatable local services + coupon codes.
- **Cannibalisation risk is LOW for local/coupons, MODERATE for Goods/physical.** Since Groupon is exiting first-party Goods anyway, cannibalising a winding-down vertical is not a real cost.
- **Incrementality potential:** SD brings male, tech/electronics demand that Groupon under-serves today.

Verdict: compatible, not cannibalising. Partnership likely brings incremental audience Groupon does not capture today. [Opinion, High]

#### 2. What UGC adds that Groupon cannot build in-house

**What UGC genuinely adds:**
- Deal velocity at zero merchandising cost (thousands of deals per day)
- Community trust signals (votes, comments, thread discussion)
- Long-tail discovery (price errors, stacking, regional deals)
- Power-user economy: ~5% of users drive ~20% of revenue [Data - HBS case; High] - a moat that took 20 years to build

**What UGC cannot give Groupon:**
- **Moderation liability transfer.** If Groupon embeds the feed, Groupon absorbs content-risk exposure.
- **An owned moat.** Community stays on slickdeals.net forever. Partnership ends = inventory ends.
- **Direct merchant relationships.** Groupon's merchant network is deeper (direct contracts, negotiated discounts). A SD feed collapses Groupon from a merchant platform to an affiliate distributor.

**Build vs partner honest take:** In-house UGC would take 2-3 years and $10-20M to reach 10% of SD's scale, with high failure risk. A partnership buys time. But it is rented time.

#### 3. Precedent

- Slickdeals has shipped affiliate network integrations (Awin, ShareASale, FlexOffers), API Sales program (>10,000 merchants), Kevel retail-media ad platform partnership, Perplexity AI + PayPal integration (Nov 2025). [Data, High]
- **No public evidence of a white-label SD feed licensed to another retail brand's core site.** [Data gap] Either strategic whitespace or a signal that retailers prefer direct affiliate networks.
- No public partnership between SD and Rakuten / Honey / RetailMeNot. Competitive norm in deals ecosystem.

---

### Partnership options

| Option | Description | Pros | Cons |
|---|---|---|---|
| A | Affiliate-only via SD API | Zero risk, fast, reversible | Tiny economics; does not "refill Goods" |
| **B** | **Embedded Featured Deals feed on Groupon Goods surface** | **Fastest way to refill Goods; still piloting** | **Brand dilution; Groupon becomes SD distribution channel; moderation liability** |
| C | Co-branded storefront "Groupon Goods by Slickdeals" | Highest engagement; clearest value exchange | Commits Groupon surface to non-owned brand; hard to unwind; exit risk |
| D | White-label API, community hidden | Control of UX; no brand dilution | Lose the moat; commodity feed only |
| E | Acquisition / equity | Owns the moat permanently | Transformative capital commitment; valuation math likely breaks for Groupon |

**Recommended: Option B, pilot scope, with unwind clauses.**

---

### Partnership conditions (all must be true)

1. **Pilot scope:** 90 days, single Goods sub-category (e.g. consumer electronics), <5% of Goods surface.
2. **Clean unwind:** 30-day termination clause, no exclusivity.
3. **Change-of-control:** right to terminate on SD acquisition (GS has held 8 years - sale within 12-24 months is likely).
4. **Rate lock:** 24-month commission rate protection.
5. **Branding:** light co-branding only ("Powered by Slickdeals"), not full SD takeover.
6. **Moderation:** Groupon-side safety filter (only deals with >N community votes, no expired, no known scam sellers).
7. **Metrics gate for renewal:** minimum $X revenue/mo + Y% CTR lift.
8. **Parallel in-house track:** commission a "Groupon Deals Feed" project as alternative, so we are not single-sourced.

---

### Do NOT

- **Do not sign a co-branded storefront (Option C) before Option B pilot succeeds.**
- **Do not acquire.** Groupon market cap in the $600-900M range; SD likely commands $700M-$1.2B+. Without a dedicated strategic rationale and investor buy-in, valuation math breaks.
- **Do not let "replace Goods" framing drive the contract structure.** SD cannot replace Goods because Goods was not a community. It was a merchandising surface with inventory and fulfilment dependencies a UGC feed does not solve.

---

### Economics

#### Base affiliate economics

- Merchants pay SD 3-15% of GMV via affiliate networks.
- SD keeps ~100% of that today (minus affiliate network cut ~10-20%).
- Net SD take-rate: ~2.5-12% of GMV. [Estimate]

#### Likely Groupon-SD split (Option B)

- If SD provides the inventory feed and Groupon drives the clicks, the split is likely 50/50 to 70/30 in SD's favour. [Estimate / Assumption]
- On a $100 order at 5% merchant commission ($5 gross), Groupon might net $1.50-$2.50 per order. [Estimate]
- Volume math: 10M clicks/mo at 2% conversion + $50 AOV = 200k orders/mo at $2 net = **~$400k/mo = ~$5M/yr to Groupon.** [Estimate, assumption-heavy]
- Small relative to Groupon revenue, but non-trivial if current Goods contribution is near-zero.

#### Warning

SD has leverage. Profitable, growing, has a moat, doesn't need Groupon. Expect Groupon to end up as the weaker side of the negotiation. [Opinion]

---

### Alternatives to Slickdeals

Ranked by fit for "refilling the Goods surface", not by size:

#### Tier 1 - Most fit
1. **Amazon Associates API + curated storefront** - deepest catalog, best affiliate infra; razor-thin commissions (1-4%).
2. **Walmart / Target affiliate feeds directly** - no middleman; Groupon builds curation.
3. **Direct merchant marketplace model** (Goods -> 3P marketplace) - path Groupon is already on. SD would be ADDITIVE, not replacement.

#### Tier 2 - Community-layer alternatives
4. **DealNews** - smaller, editorial-driven. 7M monthly visits vs SD's 25M. Viable cheaper alt.
5. **Brad's Deals / DealsPlus / 1Sale** - smaller SD-alikes.
6. **Woot (Amazon-owned)** - not realistic as partner (conflict of interest).

#### Tier 3 - Leapfrog moves
7. Build in-house UGC community. 2-3 years, $10-20M, high failure risk, owned moat.
8. Reddit r/deals + r/frugal partnership / content syndication. Cheap. No moat.
9. AI-curated feed across multiple affiliate networks. Skip the UGC layer entirely.

**The right question is not "SD vs build." It's "what is Goods supposed to BE?"**
- Curated physical-goods affiliate storefront? SD is one of 5+ viable partners.
- UGC community? SD is best partner but also overkill.
- Real revenue line again? Neither SD nor any alternative solves fulfilment/inventory. That's a separate strategic question.

---

### Strategic risks

- **Non-owned moat (DEAL BREAKER).** Rent, not own. Mitigate with surface-level integration and 30-60 day unwind.
- **SD gets sold to competitor.** GS exit likely in 1-2 years. Amazon (owns Woot) is plausible buyer - would likely kill the partnership. Mitigate with change-of-control termination.
- **Moderation and brand safety.** SD content occasionally has bait-and-switch, expired coupons, price errors. On Groupon's surface these become Groupon's brand problem. Mitigate with Groupon-side safety filter.
- **Audience leak.** Strong SD branding drives users to slickdeals.net. Mitigate by keeping users in Groupon's surface/session, minimise SD branding.
- **Rate ratchet.** SD history of raising rates as leverage grows. Mitigate with multi-year lock.
- **Regulatory exposure.** Honey + Capital One Shopping class actions on commission theft signal rising scrutiny. Mitigate with clear disclosure, legal review of attribution model.
- **Rented-moat opportunity cost.** Engineering cycles on SD integration are cycles not building Groupon-owned community. Mitigate with explicit 90-day review gate.

---

### Data gaps

1. Slickdeals 2026 revenue - last hard data is 2023-2024.
2. Exact DAU number - 40% DAU/MAU implies ~4.8M DAU, not directly confirmed.
3. "Storefront program" specifics - not a clearly-named public product. Ask SD BD directly.
4. 2026 employee count - not re-confirmed.
5. **Precedent white-label deployment** - no public example found. Ask SD for NDA references.
6. Ziff Davis or other buyer rumours 2025-2026 - no public evidence. Speculation only.
7. Groupon internal economics of current Goods surface - need Groupon-internal revenue-per-session and CTR to size the pilot gate.
8. Chrome extension usage trajectory - launched 2019, recent growth unclear.
9. SD AI personalisation external licensability - 7% lift was on SD's own site; unclear if portable to partners.
10. Groupon ↔ SD audience cross-visitation - would need Comscore / SimilarWeb panel.

---

### Red flags / Yellow flags

#### Red flags
- No precedent for the deal Dusan is proposing (white-label UGC feed into partner's core site).
- SD leverage > Groupon leverage. Expect SD to dictate terms.
- PE exit clock. 12-24 months.
- Audience skew mismatch (male-tech vs Groupon's female-local base).

#### Yellow flags
- iPhone/Android survey data from 2018 - dated, do not over-use.
- Traffic +5% MoM is good but not spectacular. Mature cash-flow asset, not hyper-growth.
- Moderation liability - occasional bad posts slip through.
- Upper-funnel brand-advertising strategy - pulls SD incentives away from maximising partner click-out over time.
- Strategic fit with Groupon's local-services pivot is weak. SD is a physical-goods play.

#### Green flags
- Active AI investment (SageMaker, 7% click lift) - healthy engineering culture.
- iOS redesign shipped 2025 - product velocity real.
- 40% DAU/MAU - community is sticky.
- Traffic still growing in 2026 - not declining.

---

### Recommendation to leadership (1 paragraph)

Start a 90-day Option B pilot: Slickdeals-provided Featured Deals feed embedded in one Goods sub-category (consumer electronics), <5% of Goods surface, light co-branding ("Powered by Slickdeals"), Groupon-side safety filter on >N community votes. 30-day unwind, 24-month commission rate lock, change-of-control termination. Parallel in-house "Groupon Deals Feed" project runs alongside as the single-sourcing insurance policy. Success gate for renewal: minimum revenue threshold + CTR lift (define with Dusan's team). **Explicitly reject** any framing of Slickdeals as a Goods replacement - Goods failed on fulfilment and inventory economics, which a UGC feed does not solve.

Human ownership: Dusan to sponsor, Goods product lead to drive contract, Rebecca / Martin to handle competitive comms.


---

## Part 9 - Data gaps (internal + external asks)

## Data Gaps - What We Still Need to Make an Investment-Grade Decision
*Consolidated from competitor research + Rebecca's April 2026 draft §5.7 | 2026-04-21*

### Purpose

Every loyalty investment decision requires internal evidence that competitive research alone cannot provide. This document lists what we still need to pull, who owns it, the approximate effort, and why it matters.

**Rule followed in the research: declare gaps, do not invent numbers.** This document is the honest list.

---

### 1. Internal data asks (no external spend, 1-5 working days each)

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

### 2. External gaps I could not close with public research

These require primary research (interviews, surveys, mystery shop) or commercial data (SimilarWeb Pro, Semrush, SensorTower, data.ai).

#### Competitor-specific gaps

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

#### Category-level gaps

| # | Question | Path to fill |
|---|---|---|
| 21 | **Average iOS Safari extension activation rate across category** | Apple does not disclose. Would need a panel or primary data. |
| 22 | **Breakage rate for cashback in a 1:1 soft-currency model** | Industry range 15-30%; Groupon-specific needs a pilot cohort. |
| 23 | **Post-Honey-collapse user migration destinations** | Rakuten / Capital One Shopping / Coupert public disclosures do not explicitly attribute inflow to Honey exodus. Pattern is likely diffuse (many users going cold rather than switching). |
| 24 | **Groupon audience ↔ RetailMeNot / Rakuten / Honey / Cap One Shopping cross-visitation sizes** | Rebecca's Phase 1 research programme: SimilarWeb Pro Audience Overlap dashboard, or Semrush Audience Overlap add-on ($289/mo). |

---

### 3. Primary research asks (funded, non-trivial spend)

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

### 4. Status tracker

| # | Item | Status | Owner | Requested | Due |
|---|---|---|---|---|---|
| 1-11 | Internal data asks | Not started | TBD | TBD | Target: pull within 1 week |
| 12-24 | External gaps | Flagged in final report | n/a | n/a | Some resolve with time |
| 25-30 | Primary research | Pending prioritisation | TBD | TBD | Phase 1 can start this week |

---

### 5. Priority to request this week

Top 3 for immediate pull (highest value, lowest cost):

1. **Item 1 - Coupons ↔ deals crossover.** Chase Mark Brenda for status. This is the single most decision-critical number.
2. **Item 6 - Non-monetised session rate.** Frames Layer 1 opportunity. Internal BI query, <1 day.
3. **Item 25 - Semrush Audience Overlap (7-day trial).** No cost, confirms Rebecca's SimilarWeb affinity data with independent second source.

### 6. Principle - do not invent what we can measure

Every number in the final report is labelled [Data] / [Estimate] / [Opinion] / [Assumption]. When any of these gaps close with real data, the corresponding claim should be promoted from [Estimate] to [Data] and the confidence rating revised.

No number in the final report is load-bearing in the "we would change the decision if wrong" sense without a data source. The explicit gaps above are the known unknowns.


---

## Part 10 - PostHog quick survey draft

## PostHog Quick Survey - Draft Wording (subtask #4)
*Target: new-UI coupons pages | Non-incentivized | Directional signal only | Apr 22 2026*

### Survey configuration

- **Placement:** new-UI coupons pages only (not legacy)
- **Trigger:** after 10 seconds on page OR on scroll-depth 40%, once per user per 30 days
- **Max length:** 3 questions, no free-text (to protect response rate with no incentive)
- **Incentive:** none (deeper + incentivized version lives in Mark Neary's funded survey track)
- **Est. response rate:** 2-5% unincentivized is realistic; below 2% means the UX is wrong

### The 3 questions

#### Q1 - Current tool usage
> **Do you use cashback or coupon tools when shopping online?**
>
> - Yes, regularly
> - Sometimes
> - No
> - Not sure what those are

Response-shape choice rationale: 4 options (not 3) adds the "not sure" path. If a meaningful share picks "not sure", the category education gap is material to Groupon's positioning.

#### Q2 - Which tools
> **Which do you currently use? (select all that apply)**
>
> - Rakuten
> - PayPal Honey
> - Capital One Shopping
> - Ibotta
> - RetailMeNot
> - Coupert
> - Other (no free text, just flagged)
> - None
>
> *Conditional logic: only show if Q1 = "Yes, regularly" or "Sometimes"*

Response-shape rationale: the 6 names map directly to our competitive scope. Order is deliberate (by category scale). "Other" captured without free-text to stay single-click.

#### Q3 - Willingness to add Groupon
> **Would you use a Groupon cashback tool alongside what you use today?**
>
> - Yes, definitely
> - Probably
> - Maybe
> - Probably not
> - No
>
> *Shown to all respondents, regardless of Q1*

Response-shape rationale: 5-point is more informative than 3-point yes/no/maybe. Lets us separate "yes definitely" (high conviction) from "maybe" (soft positive).

### Important framing choices

- **"Cashback or coupon tools"** (not just "cashback") - captures Honey / RetailMeNot users who may not self-identify as cashback-savvy. If we say only "cashback", response rate drops because Honey users say "I don't do cashback".
- **"Alongside what you use today"** in Q3 - anchors on Rebecca's stacking thesis. We're NOT asking them to switch; we're measuring slot availability in the existing stack. Critical framing.
- **Groupon not Groupon Bucks** in Q3 - don't introduce new terminology in the question. "Bucks" means nothing to users yet.

### What we'll learn (and what we won't)

**Will learn:**
- Rough share of coupons-page users who already use any cashback tool
- Concentration of competitor usage inside the coupons-page audience
- Raw willingness-to-stack signal

**Won't learn (this needs the Mark Neary funded version):**
- Stacking vs switching behaviour
- Rate sensitivity (conjoint: $5 Bucks vs $5 PayPal vs $5 gift card)
- Frustrations with current tools
- Trigger points for adding or removing a tool
- Demographic cuts (survey of this length can't capture it honestly)

### Launch checklist

- [ ] PostHog survey configured on new-UI coupons pages only (not legacy)
- [ ] 30-day once-per-user cap set
- [ ] Trigger: 10 seconds on page OR 40% scroll depth
- [ ] Skip option visible on every question
- [ ] Funnel instrumented: impression -> response -> question-1-answer -> question-2-answer -> question-3-answer
- [ ] Target: n=500-1000 responses before drawing conclusions
- [ ] Review after 2 weeks; extend or retire

### Analysis cut pre-registered (to avoid p-hacking)

Before the survey runs, the primary cut is:
1. **Q2 stacked bar** showing competitor-usage concentration inside coupons-page audience (calibrates Rebecca's affinity-data thesis).
2. **Q3 net positive** ("definitely" + "probably" as single bucket) as a go/no-go directional signal for the Bucks extension investment.

Everything else is secondary / exploratory.


---

## Part 11 - Daniel Rakuten ask draft

## Gchat Ask - Daniel (US Content Team) - Rakuten US Access
*Draft for Martin | Subtask #6 [Blocker] | Due Apr 22*

### The task context
CZ VPN does not reliably get into Rakuten's US flows (App Store regionalisation + Rakuten-specific geoblocks). The loyalty research deliverable to Adam Friday 1pm CET needs live-capture evidence of Rakuten's signup + Safari extension UX on Nike.com. Daniel on the US content team is the fallback per the Apr 20 debrief plan. Martin is chasing directly (not routed through Rebecca / Zoe).

---

### Option A - Quick ask (recommended)

> Hey Daniel - got a loyalty research deliverable going to Adam Friday and I need US-side capture of Rakuten that our CZ VPN can't reach reliably. Can you spare ~15 min this week to do a quick screen recording for me?
>
> Specifically:
> 1. Rakuten US signup flow from rakuten.com - just walk through the form, do NOT actually create an account (we can see fields + CTAs without committing)
> 2. Safari extension install + activation from rakuten.com/button/safari
> 3. Test the extension on Nike.com (add a product to bag, go to checkout, show whether Rakuten pops) - Rebecca's canonical test case
>
> Screen recording preferred (QuickTime or Loom, whatever is easiest). Notes on what surprised you welcome but optional.
>
> Deadline: Thu Apr 23 EOD would be perfect; absolute-latest is Fri Apr 24 09:00 CET.
>
> Upload to the Shared Drive -> Product -> Cashback research -> loyalty-research folder, or just Slack it to me and I'll file it.
>
> If you can't fit it in this week, no worries - I'll flag the Rakuten section as a data gap in the final doc. Just let me know either way by EOD today?
>
> Thanks!

### Option B - If Daniel is slammed (shorter)

> Hey Daniel - quick ask. Any chance you can do a ~10-min screen recording of Rakuten.com from a US IP this week? Specifically: (1) signup flow walk-through (don't actually sign up), (2) Safari extension install, (3) test on Nike.com checkout. Going into Adam's Friday loyalty deliverable. If you can't, I'll flag as a data gap - no worries. Yes / no by EOD today if possible. Thanks!

### If Daniel doesn't respond by EOD today

Fallback actions (documented for Thursday):
1. Post in a US-team Slack channel (if Martin has access) - "anyone have a free 10 min for a US-only screen recording?"
2. Post in a general Groupon Slack - same ask, wider net
3. If still nothing by Thu EOD, the Rakuten section in the final doc gets this note: *"Rakuten US signup flow + Safari extension UX: not captured in live-human session for this iteration (US IP not available from Martin's CZ location; US content team ask unanswered). Dependency flagged in data-gaps.md. Public pre-auth capture in `signup-flow/rakuten-preauth.md` covers the landing + marketing copy portion; logged-in + Nike-test still pending."*

### Things to NOT ask Daniel for
- Do NOT ask Daniel to sign up with his real email and keep receiving Rakuten emails afterwards (unfair ask; use a + alias or burner if any real signup is needed, but we aren't asking for that here)
- Do NOT ask for interpretation / analysis - Daniel is capturing, not analysing. Analysis stays with Martin.
- Do NOT ask for anything on Honey or Cap One - those are capturable from CZ per the research brief.

---

**Send via:** Google Chat DM to Daniel (US content team). If Martin doesn't have direct DM already, ping Zoe once for an intro and use Option A with "Zoe suggested I reach out" prefix.

**Track:** Mark subtask 1214151611001947 in-progress once sent; complete when recording received or gap flagged Thu EOD.


---

## Part 12 - AI funnel transparency appendix

## AI Funnel Transparency Appendix
*Loyalty Mechanics Reverse Engineering for Groupon | 2026-04-21*
*Per Adam's 2026-04-20 request: prompts used, raw data, what AI did, iteration log.*

---

### 1. What AI did (in plain English)

I used Claude Code (Opus 4.7, 1M context) to:
1. Fetch Rebecca's Google Doc research directly from Drive via the `gws docs documents get` CLI (no copy-paste, direct API). Result: 4.5MB JSON, parsed to 69K of clean markdown.
2. Spawn **5 parallel research subagents**, each with an independent WebSearch tool. Each agent ran 2-6 search rounds on a specific competitor or theme, wrote findings to a `raw/*.md` file, and returned a 300-word summary.
3. Read both Rebecca's draft and all 5 raw files, then synthesised a merged final report (this document's companion).
4. Applied a strict honesty protocol: label every claim `[Data]` / `[Estimate]` / `[Assumption]` / `[Opinion]`, date everything, flag confidence High / Medium / Low, declare data gaps rather than guess.

I did NOT use AI to generate numbers, invent statistics, or produce polished prose from thin air. Where a number isn't cited to a source, it's labelled `[Estimate]` or listed as a data gap.

### 2. Why this structure (and not a single all-in-one agent)

Three reasons for parallel specialist agents over one generalist:
- **Depth**: 6 search rounds per competitor beats a single scan. Rakuten's Big Fat Check mechanics and Capital One's $45 install trigger needed separate drill-downs.
- **Context hygiene**: Each agent returns a 300-word summary, not its full transcript. The main session stays uncluttered, which matters for the merge step.
- **Honest audit trail**: Separate `raw/*.md` files per agent make it trivial to trace any claim in the final report back to its research origin.

### 3. Agent roster and scope

| Agent | Competitor / Theme | Search rounds | Output file |
| --- | --- | --- | --- |
| A1 | Rakuten loyalty mechanics | 5-6 deep | `raw/rakuten-mechanics.md` |
| A2 | Capital One Shopping mechanics | 5-6 deep | `raw/capital-one-shopping-mechanics.md` |
| A3 | PayPal Honey mechanics + trust collapse | 5-6 deep | `raw/honey-mechanics-and-cautionary-tale.md` |
| A4 | Tier-2 scan (Ibotta, RetailMeNot, Coupert) + Starbucks pure-loyalty benchmark (later dropped from final) | 2-3 scan + 3-4 Starbucks | `raw/tier2-scan-and-starbucks-benchmark.md` |
| A5 | Slickdeals partnership feasibility (NOT loyalty) | 4-5 | `raw/slickdeals-partnership-feasibility.md` |

### 4. Prompts (verbatim, trimmed for length)

Full prompts are in the session transcript. Core instructions common to all five:

> - Label every claim: `[Data]` / `[Estimate]` / `[Assumption]` / `[Opinion]`
> - Rate confidence: High / Medium / Low
> - Date every data point. Flag anything >12 months old.
> - NO em-dashes, use plain hyphens.
> - Do not fabricate numbers. "DATA GAP: could not find X" is always better than a guess.
> - Be honest about weaknesses. If users complain, surface the complaints.
> - 5-6 search rounds minimum (Tier 1) / 2-3 rounds (Tier 2 / partnership)

Per-agent focus:
- **A1 (Rakuten):** quarterly payout mechanics (Big Fat Check), Rakuten+ paid tier, Amex/Bilt partnerships, in-store linked card, LTV signals from Rakuten Group filings, Safari iOS extension UX. See 20-point research brief in prompt.
- **A2 (Capital One Shopping):** the $45 install incentive triggers and conditions, Shopping Credits soft-currency economics (earn rate, breakage, gift-card-only redemption), App Store 4.9 / 960K reviews authenticity, Safari #2 ranking, is Capital One investing or in maintenance mode.
- **A3 (Honey):** MegaLag scandal chronology (Dec 2024 first video, Dec 2025 second), class-action status, PayPal app bundling activation flow, Chrome user loss month-by-month, what Honey still does well post-scandal, primary lesson for Groupon on trust.
- **A4 (Tier-2 + Starbucks):** where April-2026 surface doc is THIN (Ibotta IPN B2B2C, RetailMeNot Feb-2026 1% floor, Coupert post-Honey migration), plus Starbucks stars + tiering + mobile pre-load as pure-loyalty benchmark. Starbucks was subsequently dropped from the final report after the agent's honest "does not port" finding was accepted.
- **A5 (Slickdeals):** partnership economics for Goods replacement, audience overlap with Groupon, UGC moat Groupon can't build in-house, precedent partnerships, challenge the Dusan thesis honestly.

### 5. Iteration log

| Step | What changed, why |
| --- | --- |
| Initial intake | User brief gave me asymmetric tier structure (Tier 1 deep, Tier 2 scan, Tier 3 partnership) and an open question on pure-loyalty benchmark. |
| Research depth | Scored 8/9 on the startup-competitors skill's matrix (Deep), but deviated to Deep+scan+partnership mix rather than uniform Deep. Honest because the brief was asymmetric. |
| Starbucks vs Bonvoy | Recommended Starbucks over Marriott Bonvoy. Reason: Starbucks is daily/weekly frequency (matches habit goal), Bonvoy is low-frequency travel (wrong cadence). |
| Starbucks dropped | After research, Starbucks was removed from the final report. Honest finding from agent A4: the habit driver is pre-loaded stored value + mobile order, which does not port to Groupon (episodic, unpredictable-basket commerce). Raw research preserved in `raw/` for audit trail; benchmark removed from recommendation set. |
| Output shape pivot | Default skill produces battle cards. Switched to mechanic cards because Groupon isn't selling against Rakuten's sales team — we're learning from them. Battle cards would have been the wrong artifact. |
| Rebecca merge discovery | After fetching Rebecca's doc, found it was much richer than the brief implied (full report structure, 60+ cited sources, stacking-vs-switching thesis). Merge strategy shifted from "use her as draft input" to "use her structure as the skeleton, add depth/benchmark/partnership." |
| Honesty hits | Agents were instructed to surface competitor STRENGTHS and churn signals, not just weaknesses. Cherry-picking weaknesses would have been bad competitive intelligence. |

### 6. What AI is NOT good at here (transparency)

- **Primary customer research.** AI cannot replace the Phase 2 (survey) and Phase 4 (depth interviews) in Rebecca's research programme. Mechanics can be reverse engineered from public data; *why users feel loyal* cannot.
- **Internal data access.** AI cannot see Groupon's BI. Section 5.7 of Rebecca's doc (8 internal data requests) is unchanged by this AI pass.
- **Future-casting.** The Tier-1 teardowns reflect public mechanics in market today. If Rakuten launches a new tier next month, this report will be out of date.
- **Negotiation and politics.** Slickdeals partnership feasibility assesses whether it's the right *kind* of deal; the actual deal terms will be negotiated, not reverse engineered.

### 7. Raw research files (audit trail)

All raw outputs preserved in `raw/`:
- `rebecca-draft.md` — extracted from Rebecca's Google Doc via gws CLI
- `rakuten-mechanics.md` — agent A1
- `capital-one-shopping-mechanics.md` — agent A2
- `honey-mechanics-and-cautionary-tale.md` — agent A3
- `tier2-scan-and-starbucks-benchmark.md` — agent A4
- `slickdeals-partnership-feasibility.md` — agent A5

Every claim in the final report traces to one of these six files plus Rebecca's original citations [1]-[60].

### 8. Reproducibility

This research can be re-run by any team member:
1. `gws docs documents get --params '{"documentId":"1tck7N5UlkSWeSSNKpg-tWb2-VrUVeipEJR9XBLRxfUY"}'` — fetch Rebecca's doc
2. Replay the five agent prompts (above) in any Claude Code session with WebSearch enabled
3. Diff new raw files vs existing ones to see what changed in the market

The prompts are the actual audit; the document is the synthesis.


---

## Part 13 - Mechanic cards (full detail)

### 01-quarterly-payout-ritual

#### Mechanic Card 01 - Quarterly Payout Ritual
*Source: Rakuten "Big Fat Check" | 2026-04-21*

##### What it is

Four fixed payout dates per year where accumulated cashback lands as a visible, anticipated payment. Rakuten pays on **Feb 15, May 15, Aug 15, Nov 15** - always the 15th. Methods: cheque, PayPal, Amex MR points (1:100), Bilt points. Minimum threshold: **$5.01**. [Data - rakuten.com/blog; High]

##### Why it works as a habit driver

- **Dopamine anticipation 4x/year.** Users check back approaching each date to see their balance.
- **Brand ritual.** "Big Fat Check" has its own name, schedule, FAQ page, marketing moments. It becomes a thing users talk about.
- **Soft lock drives breakage.** Sub-threshold balances ($5.01 min) roll forward. Many users forget or abandon. Unredeemed cashback = margin.
- **Forces sub-quarterly engagement.** Users visit to accrue toward the next payout.

##### Evidence this works

- Rakuten's rakuten.com has 63% direct traffic [Data - SimilarWeb Mar 2026] - users bookmark / type in. Strong repeat usage.
- 17M+ cumulative US members, $4.6B cumulative cashback paid since 1998 [Data; High]
- The mechanic has survived 27 years unchanged. That is the strongest survival signal in the category.

##### Groupon adoption

**Copy the ritual. Skip the anti-customer details.**

- **Quarterly cadence:** pay on Feb 15 / May 15 / Aug 15 / Nov 15 (or Groupon-branded alternative - e.g. "Bucks Drop Day" with its own monthly-15th anchor).
- **Payout methods:** PayPal, Venmo, Groupon credit, OR cash-out to linked debit card at $1 minimum (Coupert-style, see card 04).
- **Brand the ritual.** Give it a name, a page, a push notification campaign, a homepage takeover.
- **Cumulative earnings counter** prominently on the home screen ("You've earned $127.43 this year; next payout Aug 15").

##### Specifically do NOT copy

- **$5.01 minimum payout threshold** - anti-customer. Use $1 instead (per Coupert). Accept the small UX cost; trade for trust.
- **Pending-balance denials** - Rakuten aggressively invalidates pending balances. For Groupon, reserve-and-release, never confirm-and-revoke.
- **Bounced cheques** - PhatWallet reports of Big Fat Check bouncing [Data - PhatWallet Mar 2024]. If Groupon pays, it pays.

##### Effort

- Backend ledger: ~1 sprint to build accumulating Bucks ledger per user.
- Cadence + payout job: ~0.5 sprint.
- Marketing / brand: ~1 sprint for the first "Bucks Drop Day" campaign.
- Cumulative counter UX: ~0.5 sprint.

**Total: ~2-3 engineering sprints + design + marketing.**

##### Success metrics

- % of users with a positive Bucks balance on payout day
- Push open rate on "Bucks Drop" notification
- Visits-per-user in the 14 days prior to payout date (should spike)
- Payout redemption rate (target >70%; anything <50% means either UX friction or distrust)
- Breakage rate (aim for 15-25% steady state - above 30% means users are losing trust)

##### Risks

- If Groupon cannot fund the cashback (Rakuten's 2.4% op margin is the category ceiling), the ritual reveals weak economics. Pilot at small scale before scaling.
- If Groupon cuts the rate after launch, the ritual amplifies the damage (rate cuts on established loyalty programmes are a well-documented backlash trigger across categories). Commit to 24 months of stable rate minimum before ever adjusting.

##### Related

- Mechanic Card 02 - Soft Currency 1:1 (the thing being accumulated)
- Mechanic Card 03 - Weekly Anchor Day (fills sub-quarterly engagement gaps)
- Mechanic Card 05 - Trust Floor (guaranteed minimum back)


---

### 02-soft-currency-1-to-1

#### Mechanic Card 02 - 1:1 Transparent Soft Currency (Groupon Bucks)
*Source: Capital One Shopping Credits | 2026-04-21*

##### What it is

A branded soft currency where **1 unit = 1 dollar of redemption value**, with NO obfuscation. Users earn "Bucks" per purchase. Bucks redeem against Groupon deals, gift cards, or select partner retailers. Clarity is the load-bearing design choice.

Capital One Shopping's implementation: 1 credit = $1 USD (transparent), gift-card-only redemption at 50+ rotating retailers, no cash-out, no bank deposit, no statement credit, no Capital One banking account required. [Data - Capital One help center; High]

##### Why 1:1 beats points systems

- **Clarity = trust.** Every time a user sees "1,000 points = ???", they have to do math. Honey does this (100 points = $1.00). Rakuten partially does this (cashback in $ but Amex transfer at 1:100). Capital One Shopping's 1:1 is the clean variant.
- **No devaluation gaming.** Points programs allow issuer to secretly devalue by changing redemption rates. High-profile examples across multiple loyalty categories have triggered customer backlash when long-held earn rates are silently cut. A 1:1 ratio makes devaluation impossible without a visible change users will notice.
- **Balance sheet elegance.** Bucks are a liability on the books, not a cash outflow. Breakage converts liability to profit.

##### Breakage economics

- Industry benchmark: 15-30% of earned rewards never redeem [Estimate - multiple sources]
- Gift-card-only redemption adds a second layer of breakage (3-10% industry) [Estimate]
- Compounding: issue Bucks -> ~25% never redeemed -> of redeemed, ~5-10% of gift card value never spent -> real cash cost to issuer is 60-80% of headline "earned" [Opinion]

**For Groupon, breakage on Bucks could plausibly be the difference between 2% and 8% margin on the loyalty program. Pilot before scaling.**

##### Redemption options (ranked by Groupon fit)

| Redemption | User appeal | Groupon margin | Recommendation |
|---|---|---|---|
| **Local experience on Groupon** (spa, restaurant, activity) | High - unique value | High (merchant relationships) | Primary path. Headline message. |
| **Groupon deal (any vertical)** | High | High | Secondary path |
| **Partner gift card** (Target, Amazon, Uber etc) | Medium (substitutable) | Medium | Optional, smaller catalog |
| **Cash-out to PayPal / Venmo** | Very high | Negative | Last resort, $1 minimum with processing fee |
| **Statement credit / bank deposit** | High | Negative | Do NOT offer - cannibalises Groupon spend |

Lean heavily toward the top two. They are what makes Bucks structurally better than a Capital One Shopping credit (gift card) - users get LOCAL experiences, which no competitor can match.

##### Groupon adoption

**Copy:**
- **1:1 transparent earn rate.** 1 Buck = 1 dollar. Never obfuscate.
- **No paid tier, no banking / Groupon+ tie-in required.** Keep the loyalty layer standalone.
- **Earn rate 1-10% by merchant** (matches Capital One Shopping), with boosted rates on promotional events.
- **Clear on-screen balance + countdown to next payout.**
- **90-day retention gate on the welcome bonus** (Capital One Shopping's best idea - converts bonus-hunters into habit-formed users).

**Critical Groupon variant:**
- **Bucks redemption prioritises Groupon deals and local experiences** over external gift cards. This is Rebecca's "Bucks bridge" insight and it is the thing that makes Groupon's loyalty layer different from every other cashback app.
- **Unique positioning:** "Earn Bucks from Nike, spend on a massage near you."

##### Specifically do NOT copy

- **Rotating redemption inventory that removes top brands** (Capital One removed Walmart, Home Depot, Macy's, Lowe's). Users lose trust when "my Target gift card" disappears. Lock in stable top-5 redemption partners with multi-year contracts.
- **Post-confirmation reward denials** (Capital One's top churn driver). Reserve-and-release architecture, not confirm-and-revoke.
- **Phone-number conflict redemption bugs** (Capital One operational failure). Test redemption end-to-end before GA.
- **"Wait 1 year before we investigate" customer service scripts** (Capital One). Target 30-day dispute SLA.
- **Gift-card-only redemption as the sole path.** Combine with cash-out at $1 (Coupert) and Groupon-deal redemption as primary.

##### Effort

- Bucks ledger + issuance: ~2 sprints
- Redemption UX + gift card provider integration: ~2 sprints
- Merchant-side earn-rate config: ~1 sprint
- Finance model + breakage forecasting: ~1 sprint (analyst-led)
- Legal T&Cs (NO "not your property, not money" language per Honey): ~1 week legal

**Total: ~6 sprints eng + legal + finance.**

##### Success metrics

- % of eligible sessions that earn Bucks
- Avg Bucks earned per active user per week
- Redemption rate by path (Groupon deal vs gift card vs cash-out)
- Breakage rate (target 15-25% steady)
- Bucks-driven Groupon deal purchase lift (Bucks bridge hypothesis)

##### Risks

- Breakage model wrong => margin erosion. Pilot with bounded cohort first.
- Too generous earn rate => unit economics don't work. Benchmark against Rakuten's ~3% average and Capital One's variable 1-10%.
- Regulatory: any points / currency program may trigger state escheatment laws (unclaimed property). Legal review early.

##### Related

- Mechanic Card 01 - Quarterly Payout Ritual (how Bucks are paid)
- Mechanic Card 04 - $1 Cashout Floor (escape valve)
- Mechanic Card 06 - Trust + Transparency (legal language, disclosure)


---

### 03-weekly-anchor-day

#### Mechanic Card 03 - Weekly Anchor Day
*Source: Rakuten Mobile Monday | 2026-04-21*

##### What it is

A weekly recurring event on a specific weekday that rewards opening the app / extension / website that day.

**Rakuten Mobile Monday**: every Monday, in-app only, boosted cashback rates. Drives weekly app open. [Data - rakuten.com/double-cash-back; High] Rakuten has maintained this mechanic for multiple years, making it one of the longest-running weekly anchors in the cashback category.

##### Why it works as a habit driver

- **Deterministic weekly hook.** Users learn "Monday = Groupon day" over 4-6 weeks of consistent pattern.
- **Low effort to participate.** Opening an app is trivial compared to purchasing.
- **Fills gap between quarterly payouts.** Without a sub-quarterly mechanic, the Big Fat Check cycle is 13 weeks between dopamine moments. Weekly anchor compresses this to 1 week.
- **Creates pushing surface.** Every Sunday night / Monday morning is a legitimate push notification opportunity without feeling spammy.

##### Evidence this works

- Rakuten direct traffic 63% [Data - SimilarWeb Mar 2026]. Suggests strong habit-formation.
- Rakuten has maintained Mobile Monday as a standing program for multiple years. Survival = evidence.
- Category pattern: committed weekly anchors are present across multiple loyalty categories, not just cashback. The mechanic is generic and well-validated.

##### Groupon adoption

**Monday is the obvious choice** (consistent with competitors, start of workweek mindset). Alternatives considered:

| Weekday | Argument | Verdict |
|---|---|---|
| **Monday** | Rakuten precedent; start-of-week; workweek-planning mindset | **Recommended** |
| Tuesday | Taco Tuesday / food-deal pairing | Alt - test if Monday saturates |
| Wednesday | Hump day optimism | Weak |
| Thursday | Pre-weekend ("Thirsty Thursday") | Weak |
| Friday | Weekend launch | Too late for "habit" framing |
| Weekend | Leisure browsing | Counter: users are distracted, conversion lower |

**Concrete Groupon pattern:**
- **Bucks Monday** - 2x Bucks earned on all qualifying purchases via app / extension every Monday.
- **Monday push notification** - 8am local time, "Your Monday Bucks are live."
- **Monday homepage takeover** - banner, boosted deals, curated "Monday-only" deals.
- **Monday-only deals** as a bonus surface - exclusive deals that only appear Mondays.

##### Specifically do NOT copy

- **Daily reveal / streak-based mechanic.** Daily streaks are designed for daily-frequency products. Groupon's cadence is weekly-to-monthly. A daily streak would punish users for not visiting Groupon every day, which is not realistic. Weekly anchor is the right frequency.
- **Calendar complexity.** Keep it one day, same day every week. Rakuten has occasionally overloaded with "Double Cash Back Days" which dilutes the Monday signal.

##### Interaction with other mechanics

- **Quarterly payout ritual (Card 01):** Monday feeds the Bucks balance that gets paid out quarterly. Clear narrative - "earn on Mondays, get paid on the 15th of Feb/May/Aug/Nov."
- **Challenge engine (separate card, planned Q3):** weekly challenges expire Sunday night - users rush to complete Mondays. Synergistic.
- **Push strategy:** Monday becomes the one confident-positive push day. Other days, push only for transactional or high-relevance events.

##### Effort

- Merchant config for boosted Monday rate: ~0.5 sprint
- Push scheduling infrastructure: ~0.5 sprint (if not already in place - else ~0.1)
- Homepage Monday takeover UX: ~0.5 sprint
- Monday-only deal curation tooling: ~1 sprint (optional)

**Total: ~1.5-2.5 sprints.**

##### Success metrics

- **App opens on Monday vs average weekday** (target: +40% Monday lift sustained over 8 weeks)
- **Push open rate** on Bucks Monday notification (target: 25-40%)
- **Conversion rate Monday vs average weekday** (target: Monday >= baseline; not significantly worse)
- **Repeat-visitor rate Monday** (same-user Mondays over 4 weeks; target: >= 30% return at least 3 of 4 Mondays after week 6)

##### Risks

- **Saturation / tuning out.** If Monday is the only push day, users grow immune. Rotate creative, vary deals, occasional surprise boosts.
- **Merchant fatigue.** If Monday is always 2x rate, merchants may push back on margin. Alternative: 1.5x everyone, 2x-3x on rotating featured merchants.
- **Holiday Mondays** (Memorial Day, Labor Day etc in the US). Plan around: either skip, or go 3x for holiday Mondays as a "super Monday" brand beat.

##### Related

- Mechanic Card 01 - Quarterly Payout Ritual (the longer-term flywheel)
- Mechanic Card 06 - Trust + Transparency (Monday is a good place to practice "here is why we are doing this" messaging)


---

### 04-safari-extension-bundling

#### Mechanic Card 04 - Safari Extension Bundled With Groupon App
*Source: PayPal Honey via PayPal iOS app - plus trust-positive variant | 2026-04-21*

##### What it is

The Groupon iOS app ships with a Safari Web Extension pre-installed. Users do not separately install the extension - it arrives silently during a regular Groupon app update. Activation requires one user action inside the Groupon app: tap "Deals" tab -> tap "Enable Safari extension" -> grant the iOS permission prompt. Once enabled, the Groupon extension surfaces at retailer checkouts automatically.

Honey's implementation inside the PayPal app is the reference [Data - help.joinhoney.com, paypal.com/us/cshelp/article/593; High]. Works in 10 countries (US, CA, UK, AU, DE, FR, NL, IT, ES, IN). Capital One Shopping also does this with Safari extension #2 Top Free Shopping app ranking [Data - Apple Community July 2025; Medium].

##### Why it works

- **Zero-friction distribution.** Users don't install Groupon's extension deliberately - they install the Groupon app deliberately, and the extension comes with it.
- **Uses Apple's permission model.** iOS Safari Web Extensions are a native Apple product since iOS 15. Distribution via parent app is an Apple-sanctioned pattern.
- **Insulated from Chrome-style exodus.** Chrome users can uninstall a browser extension in one click. Safari iOS extensions are buried in Settings, and users who got them via app bundling often don't know they have them. This is why Honey's Chrome user count fell from 20M to 12M in 12 months while iOS user count has not visibly cratered [Opinion - high confidence, public tracking asymmetry].
- **Leverages Groupon's existing 30M+ app installs with 84% iOS share.** [Data - Groupon internal; High] That's ~25M iOS installs = addressable activation pool.
- **Defensible moat.** Once activated, the extension is always there at checkout. It becomes part of the user's shopping infrastructure, not a website they choose to visit.

##### Critical design choice: the trust-positive variant

Honey's version of this has a **bundle-lock**: users cannot uninstall Honey independently of the PayPal wallet. They must uninstall PayPal entirely. German press (heise.de) has flagged this as a dark pattern, and it has been the subject of multiple Apple Community complaints. [Data - heise.de, discussions.apple.com; High]

**Groupon must build the trust-positive variant:** Safari extension bundled by default, but **independently removable**. Add a "Remove Safari extension" button inside Groupon app settings. This:
- Avoids heise.de-style dark-pattern criticism
- Protects Groupon from possible future App Store policy changes on tying
- Is actually a marketing asset ("unlike Honey, we let you remove it")
- Costs Groupon almost nothing - users who uninstall the extension were unlikely to use it anyway

##### Activation rate assumption

**Publicly undisclosed by Honey, Rakuten, and Capital One Shopping.** Groupon sizing should assume **10-30% of app users activate** until we have our own data. [Estimate, Low confidence]

- Lower bound (10%): 2.5M active Safari extension users from 25M iOS installs.
- Upper bound (30%): 7.5M active Safari extension users.
- Middle (20%): 5M active Safari extension users.

Even the lower bound is larger than Genie's current ~981 installs. The order-of-magnitude difference is what makes this worth the investment.

##### Rollout sequence

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

##### Specifically do NOT copy (from Honey)

- **Silent cookie overwrites / last-click hijack at checkout.** This is the criminal mechanic in the Honey class action. Groupon extension must NEVER overwrite an affiliate cookie it did not originate.
- **Merchant-paid coupon suppression.** If Groupon has a merchant agreement that restricts code visibility, disclose it inline at the point of use.
- **Scraping user-typed private codes.** MegaLag Part 2 allegation. Design the code database to accept only codes from verified merchant feeds or affiliate network feeds.
- **Bundle-lock (cannot uninstall extension without uninstalling app).** Per above - ship with independent removal.
- **Aggressive creator sponsorships as primary acquisition channel.** YouTube creators are now Honey's class-action plaintiffs. Diversify before scaling.

##### Merchant coverage strategy

Honey's vulnerability in MegaLag Part 2: 181,000 stores listed in the extension, only 35,000 with actual affiliate partnerships. The rest were listed without merchant consent. This is structurally fragile and legally exposed.

**Groupon's better model:** only list merchants Groupon has active affiliate or direct relationships with. Groupon's network is narrower than Honey's (by design) but fully contracted. Lean into this as a trust differentiator: "every merchant in the Groupon extension has a legitimate affiliate or direct relationship with Groupon."

##### Effort

- iOS Safari Web Extension build: **6-8 weeks** (mobile eng team, first time through)
- Groupon app integration + activation prompt UI: ~1 sprint
- Attribution + Bucks earn plumbing: ~1 sprint (reuses Bucks ledger from Card 02)
- App Store resubmission + review cycle: 2-4 weeks
- Launch merchants coupon sync: ~2 sprints

**Total: ~10-14 weeks to US MVP.**

##### Success metrics

- **Install → activate conversion** in first 30 days after app update (target: 15-25% Phase 1)
- **Monthly active extension users** (ratio vs app MAU)
- **% of retailer checkouts where extension surfaces a code** (target: >60%)
- **Extension-assisted conversion rate lift** (extension users vs non-extension users)
- **Bucks earned per extension user per month**
- **Uninstall rate after first 30 days** (target: <15%; if higher, UX is broken)

##### Risks

- **App Store policy evolution.** Apple could restrict Safari extensions in parent app bundles at any time. Mitigate by offering standalone extension as well.
- **EU Digital Markets Act.** Possible tying concerns. Mitigate with independent-removal button.
- **Merchant pushback.** If extension is seen as hijacking, merchants cut affiliate deals (as they did with Honey). Mitigate with clear attribution, no overwrites, public policy on code sourcing.
- **Registration / identity dependency.** Extension needs to know who the user is to credit Bucks. Anonymous coupons users must be onboarded into the loyalty identity layer first. This is the critical blocker for Q2.

##### Related

- Mechanic Card 01 - Quarterly Payout Ritual (Bucks earned via extension drop quarterly)
- Mechanic Card 02 - Soft Currency 1:1 (Bucks is what the extension earns)
- Mechanic Card 05 - Trust Floor (guaranteed minimum Bucks per purchase)
- Mechanic Card 06 - Trust + Transparency (extension is the highest-scrutiny surface)


---

### 05-trust-floor

#### Mechanic Card 05 - Trust Floor (Guaranteed Minimum + $1 Cashout)
*Sources: RetailMeNot 1% guaranteed floor (Feb 25, 2026) + Coupert $1 withdrawal | 2026-04-21*

##### What it is

Two complementary trust primitives:

1. **Guaranteed minimum rate.** Every qualifying purchase through Groupon earns AT LEAST X% back, regardless of merchant-specific rate. RetailMeNot's version: 1% floor across 4,000+ retailers launched Feb 25 2026 [Data - retailmenot.mediaroom.com; High].
2. **$1 cashout floor.** Users can withdraw any balance over $1 (with a small processing fee). Coupert's version: $1 min via Visa/Mastercard with 2% + $0.50 fee [Data - Coupert help center; High].

Together these reframe cashback from "a future promise I may never collect" to "real money I could take out tomorrow if I wanted."

##### Why each works

###### The guaranteed floor
- **Removes shopping-around from the decision tree.** If every purchase earns at least 1%, users stop comparing rates across tools. Groupon becomes the default.
- **Turns variable rates into brand certainty.** Users don't need to know what each merchant pays; they know the minimum.
- **Works as a trust primitive, not a loyalty mechanic per se.** It's not designed to drive habit; it's designed to make the app trustable.

###### The $1 cashout floor
- **Validates the system works on the first small purchase.** A new user earns 47 cents, cashes it out, gets a Venmo notification - the trust is cemented immediately.
- **Breaks the "abandoned balance" anti-pattern** that haunts Honey (1,000 points min = $10), Rakuten ($5.01 min), and Capital One Shopping (gift-card-only, ~$5+ values). Those thresholds silently favour the issuer.
- **Counter-intuitively, aligning with user incentive builds more habit.** Users who have cashed out once are more likely to come back than users who still haven't hit the threshold to redeem.

##### Why both together

Individually, either is thin. Combined they become: "You will earn at least X% back on every purchase, and you can pull it out as real money for $1." That is a rational-default framing that no competitor currently has.

##### Evidence

- RetailMeNot launched the 1% floor as a defensive move amid 18% segment revenue decline [Data - Ziff Davis Q4 2025 earnings Feb 2026]. The fact that they chose THIS as the differentiator suggests it is the mechanic that most resists AI-search displacement.
- Coupert's $1 floor appears prominently in every review and comparison of the tool. It is the one mechanic users mention unprompted.
- Both mechanics are LOW engineering cost and LOW margin impact at small scale. The value is brand/positioning, not unit economics.

##### Groupon adoption

**Copy both, integrate with Bucks:**

- **Floor: every qualifying Bucks-earning purchase earns minimum 1 Buck per $100** spent, even if the merchant pays <1% commission. Groupon makes up the difference. [Cost: negligible at pilot scale; needs finance model at full scale]
- **Cashout: any Bucks balance >$1 can be withdrawn** to PayPal, Venmo, or linked debit card. Processing fee: 2% + $0.50 (matches Coupert). [Small processing cost, offset by trust value]

##### Communication framing

**Don't bury this in FAQ.** Put it on the homepage and extension UX:

- "Every purchase earns at least 1% back. Guaranteed."
- "Cash out any Bucks balance above $1 - your money, anytime."

##### Specifically do NOT copy

- **Hidden floor caveats.** If the floor has exceptions, disclose them up front. RetailMeNot's fine print excludes some categories; any Groupon version must be clearly enumerated.
- **Cashout fees hidden in T&Cs.** If the fee is 2% + $0.50, say so at the withdrawal confirmation screen. Don't let users be surprised.
- **Minimum thresholds disguised as floors.** Rakuten's $5.01 is called a "minimum payout threshold", which is a soft lock. Coupert's $1 is called a "minimum withdrawal", which is a genuine escape valve. Language matters.

##### Interaction with other mechanics

- **Quarterly payout ritual (Card 01):** The floor sets the baseline; quarterly payouts are the ceremony. Users know they'll always get something each quarter because of the floor.
- **Soft currency 1:1 (Card 02):** Floor applies to Bucks earning rate; cashout is an alternative redemption path alongside Groupon-deal and gift-card redemption.
- **Safari extension (Card 04):** Floor is the headline feature on the extension's post-checkout "you earned Bucks" screen.

##### Effort

- **Floor implementation:** ~0.5 sprint (merchant config logic - floor applies if merchant-specific rate < 1%)
- **$1 cashout:** ~1-2 sprints (payment-rail integration; partnership or payment processor required)
- **T&Cs + disclosure UX:** ~1 week legal + design

**Total: ~2-3 sprints.**

##### Success metrics

- % of purchases where the floor boosts the base rate (tells us how often it fires; lower is fine - it's a safety net)
- **First-month cashout rate** for new users (target: 20-40% cash out at least once in first 30 days - proves the mechanic is trusted)
- Avg cashout size (Coupert reports users cash out ~$5-10 on average; smaller avg is better trust signal than larger)
- User-reported trust metrics in survey data (NPS on "I trust I will get paid" category)

##### Risks

- **Floor cost at scale.** If Groupon scales to 10M Buck-earning users, even a 1% floor on $10/user/month = $1M/month of Groupon subsidy. Pilot with cohort before scaling, and design the floor to be tunable (1% default, configurable to 0.5% if margin pressure).
- **Cashout rate higher than expected.** If users cash out aggressively, Groupon loses the redeem-against-deals flywheel. Monitor closely; if >40% of Bucks are cashed out vs spent on Groupon deals, the mechanic needs revisiting.
- **Regulatory.** Payment processor rules, state money-transmitter laws. Legal review. Likely handled via existing Groupon payment infrastructure if PayPal/Venmo are rails.

##### Related

- Mechanic Card 01 - Quarterly Payout Ritual (the headline payout; floor is the baseline)
- Mechanic Card 02 - Soft Currency 1:1 (Bucks itself)
- Mechanic Card 06 - Trust + Transparency (the floor is a trust primitive; the cashout is the proof)


---

### 06-trust-and-transparency

#### Mechanic Card 06 - Trust and Transparency (The Anti-Honey Checklist)
*Source: Forensic reverse engineering of PayPal Honey 2024-2026 trust collapse | 2026-04-21*

##### What it is

Not a single mechanic. A **design discipline** that governs every other mechanic. The discipline is simple: every loyalty mechanic must be transparently user-positive. If a mechanic only works when users don't understand it, it is a liability waiting for a viral expose.

This card exists because PayPal Honey lost 40% of Chrome users (20M -> 12M) in 12 months after a YouTube video explained how Honey actually worked. Three major affiliate networks cut Honey off over five days in Jan 2026. A 101-page class action is active. The failure mode is specific, documented, and entirely avoidable.

##### The Honey failure-mode catalog

From MegaLag Part 1 (Dec 2024), Part 2 (Dec 2025), class action complaint, affiliate network statements:

1. **Silent cookie overwrites at checkout.** Honey's popup at checkout would overwrite the creator's affiliate cookie with Honey's. User got "no better code found" but the click hijacked the commission. MegaLag's smoking gun: $35 NordVPN commission rerouted from a creator to Honey while user got $0.89 Honey Gold back.
2. **Merchant-paid code suppression.** Honey had contractual agreements with some merchants to NOT surface codes better than a merchant-approved default. Users saw "no better code found" when RetailMeNot had obviously better codes one click away.
3. **Private-code scraping (MegaLag Part 2).** Honey scraped codes users manually typed (employee codes, refund codes, retention-offer codes) and rebroadcast them to all Honey users. Merchants asked for takedown; Honey refused unless they became paying partners.
4. **Bundle-lock.** Honey iOS extension cannot be uninstalled independently of the PayPal wallet app. Users who want to remove Honey must remove PayPal.
5. **Long pending windows (60-90 days)** combined with **365-day inactivity forfeiture**, combined with **$10 minimum redemption threshold**, combined with **account-closure forfeiture of all points**. Each looks reasonable individually; together they form a breakage-optimisation machine.
6. **"Not your property, not money, no value prior to redemption" T&C language.** Standard for points programs, but this language becomes the legal team's nightmare in a class action.
7. **Creator sponsorships as primary acquisition channel.** YouTube creators, once the marketing engine, became the named plaintiffs.
8. **PayPal's defence ("industry standard", "legacy code").** This framing made the situation worse - it conceded the practices while shifting blame backwards. Never rely on "everyone does it" as defence.

##### The Groupon checklist

Every mechanic card in this research has a "specifically do NOT copy" section derived from this failure-mode catalog. Consolidating:

###### Design principles (non-negotiable)

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

###### Proactive disclosure UX

Things Groupon should build because Honey didn't:

- **Attribution banner in Safari extension.** "Groupon is earning affiliate commission on this purchase. We pay it back to you as Bucks." Shown once per merchant per session, not on every transaction.
- **Code provenance display.** When the extension applies a code, show where the code came from: "Code verified from [Merchant direct partnership / Affiliate network / Public aggregator]."
- **Explicit merchant partnership list.** Public page listing every merchant Groupon has an active affiliate / direct partnership with. Nothing else appears in the extension.
- **User dashboard for earned Bucks.** Full transaction log - when earned, what purchase, what merchant, what rate, when payable, when expired. Every Buck's provenance visible.
- **Change log for T&C updates.** Any change to rewards terms is published 30 days in advance with a summary of what changed.

###### What trust looks like in marketing

- "Every merchant in the Groupon extension has a legitimate partnership with Groupon." (vs Honey's 146K/181K stores without consent)
- "You can remove the Safari extension anytime, independently from the app." (vs Honey's bundle-lock)
- "Your Bucks are yours. No silent expiration, no account-closure forfeiture, no fine print." (vs Honey's T&Cs)
- "You can cash out any balance above $1. It's your money." (vs Rakuten's $5.01 threshold)
- "Codes we apply come from verified merchant partnerships. We never scrape codes you type." (vs Honey's MegaLag Part 2 allegations)

##### Why this matters economically

Trust is not a soft value. It has hard dollar consequences:

- Honey lost 8M Chrome users in 12 months. At Honey's peak valuation implied $235 per user acquisition cost [Data - $4B PayPal acquisition / 17M MAU], that's $1.88B of destroyed acquisition value. PayPal's 2025 public statements and the class action quantify the damage.
- Three affiliate networks (Rakuten, Impact.com, Awin) terminated Honey in 5 days. Each of those relationships took years to build.
- The class action is live, not dismissed. Honey's failure mode is now quantified in litigation.

For Groupon: the incremental cost of the trust-positive variant of each mechanic is tiny (~10-15% extra eng work on each card). The benefit is avoiding the Honey trajectory.

##### Governance

- **Pre-launch review gate.** Before any loyalty mechanic ships, a named reviewer (legal + PM + Adam) confirms it passes the checklist above.
- **Quarterly T&C audit.** A dedicated PM owns the loyalty T&Cs and reviews them every quarter for language drift. Any change requires Adam + legal sign-off.
- **Annual mystery-shopper test.** External contractor uses Groupon's cashback system end-to-end; publishes findings. Groupon acts on findings within 30 days. This is the public-trust proof.
- **Transparent metrics publication.** Annually publish: % of earned Bucks actually paid out, % of merchants with direct / affiliate relationships vs listed, average tracking accuracy rate. Numbers are the anti-MegaLag vaccine.

##### Success metrics

- **NPS on trust categories** ("I trust I will get paid", "The rewards are clear and fair") - target: top quartile of consumer finance apps
- **Class actions filed against Groupon re: loyalty program** - target: zero
- **Affiliate network terminations / warnings** - target: zero
- **External mystery-shopper audit pass rate** - target: >95%

##### Risks

- **Over-engineering trust at the expense of speed.** If every mechanic goes through a 6-week review cycle, Groupon ships nothing. Mitigate with a default-approve checklist that 80% of decisions don't need senior review for.
- **Competitors under-invest in trust and ship faster.** Possible. Counter-argument: Honey's 12-month exodus is why trust is the moat. Speed without trust is how you become Honey.
- **Regulatory ambiguity.** "Industry standard" is a moving target. Stay ahead of it.

##### Related

- **Every mechanic card references this one.** This card is the discipline that governs the others.


---
