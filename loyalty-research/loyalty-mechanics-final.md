# Loyalty Mechanics Reverse Engineering for Groupon
## The $40M+ retention opportunity, delivered via Safari extension

*Prepared for: Adam Ward, Dusan, Rebecca, Groupon Product Leadership*
*Date: 2026-04-21 (rough-cut for Adam feedback, NOT final polish)*
*Authors: Martin Gregor with AI research assistance (see AI Funnel Appendix) + Rebecca's April 2026 draft*
*Classification: Confidential. Do NOT publish to public GitHub Pages.*

---

## Executive Summary

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

## 1. Market Context

Largely carried forward from Rebecca's draft with light edits. Skip ahead if already familiar.

### 1.1 Market Size & Growth

- Global cashback apps market: ~$8-10B in 2024 [Data - growthmarketreports, credenceresearch; Rebecca refs 1, 2; High]
- Projected $22-23B by 2032-2033 at 9-12% CAGR [Data; Rebecca ref 1, 3; High]
- North America ~40% of global revenue; US alone ~$1.37B in 2025 [Data; Rebecca ref 3; Medium]
- 76% of shoppers prefer stores offering cashback or points [Data; Rebecca ref 16; Medium]
- Cashback platforms shown to increase repeat purchases by up to 40% [Data - industry aggregate; Rebecca ref 17; Medium-Low confidence on exact figure]

### 1.2 Competitive Landscape Summary (2026 state)

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

## 2. The Strategic Frame: Stacking, Not Switching

**This is the single most important strategic insight in the research, carried over from Rebecca §4.2-4.4.**

### 2.1 The SimilarWeb Audience Affinity Data

[Rebecca's primary data from SimilarWeb Pro Similar Sites, Jan-Mar 2026, Worldwide, exported 20 April 2026]

All four cashback competitors profiled rank in Groupon's top 8 most-affiliated sites:

| # | Domain | Affinity | Note |
|---|---|---|---|
| 1 | retailmenot.com | 1.000 | Perfect overlap - same user base |
| 3 | rakuten.com | 0.924 | Deep overlap |
| 7 | capitaloneshopping.com | 0.826 | Strong overlap |
| 8 | joinhoney.com | 0.815 | Strong overlap |

Experiences cluster (TripAdvisor, Yelp, Expedia, Viator, Eventbrite) also appears in the top 20, validating the Bucks-on-experiences thesis. Walmart, Sam's Club, Costco in the top 20 confirm value-seeking mainstream mindset. Ibotta and Coupert do NOT appear in the top 37 - they serve partially different segments.

### 2.2 The Stacking Pattern

Groupon's existing users are already visiting RetailMeNot, Rakuten, Capital One Shopping, and Honey. They are NOT choosing one. Multiple industry guides explicitly recommend running 2-3 extensions together [Data - WalletGrower 2026 guide, Rebecca ref 39]. 

Capital One Shopping shows 81% direct traffic and 7.8% referral share - users arrive via extension triggers and cross-platform referrals, not by searching "cashback apps" and choosing one [Data - SimilarWeb Mar 2026].

**Strategic implication**: Groupon does not need to displace a competitor. Groupon needs to be visible and valuable enough to earn a slot in the user's existing savings stack. The Safari extension bundled inside the Groupon app is positioned for this: zero friction install, no competing extension to displace, and a unique reward currency (Bucks redeemable on local experiences).

**Counter-nuance I'd add to Rebecca's framing**: stacking benefits Groupon only if Groupon's mechanic is additive to the existing stack. If Groupon's cashback rate is structurally below Rakuten's (and it will be - see §3.1.17), the cashback itself cannot be the hook. Bucks-on-local-experiences IS the additive value. The mechanic must be positioned as "earn Groupon Bucks from Nike, spend on a spa day" not "better cashback than Rakuten." [Opinion, High confidence]

---

## 3. Competitor Deep Dives

Structured as competitor -> mechanics -> habit drivers ranked -> weaknesses -> Groupon adoption.

### 3.1 Rakuten - the category volume leader, but thin-margin and saturating

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

### 3.2 Capital One Shopping - the soft-currency blueprint

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

### 3.3 PayPal Honey - the Safari distribution playbook AND the cautionary tale

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

### 3.4 Tier 2 scan - all three under structural pressure

Important cross-competitor pattern from the research: **Ibotta, RetailMeNot, and Coupert are all under structural pressure, not stable benchmarks.** Treat them as declining or niche, not as threats to match feature-for-feature.

**Ibotta** has pivoted from consumer app to B2B2C infrastructure. The IPN (Ibotta Performance Network) powers Walmart Cash, Dollar General, Family Dollar, Schnucks, Instacart (Nov 2024), DoorDash (Q2 2025). Q4 2025 revenue mix: 64% third-party publishers, 25% D2C. FY2025 revenue $342.4M, down 7% YoY. D2C revenue fell 25% to $139.9M. Redemption revenue per redemption $0.83, down 5% YoY - classic B2B2C dilution. [Data - Ibotta investor relations Q4 2025, Motley Fool transcript; High]

*Groupon lesson from Ibotta:* the B2B2C distribution pattern. Ibotta solved "stop begging for app installs" by embedding offer logic inside partners' owned wallets. Groupon could plug cashback into partner checkout flows rather than forcing users through the Groupon app - but this is a later-phase move, after Bucks are working inside Groupon's own surface.

**RetailMeNot's 1% guaranteed cashback floor (Feb 25 2026) is defensive, not innovative.** Ziff Davis Tech & Shopping segment revenue fell 18% in Q4 2025, with a $25M YoY drop in affiliate commissions attributed to AI-displaced search traffic. Management guided double-digit decline H1 2026. Stock fell 11-13% on Q4 miss. [Data - Ziff Davis Q4 2025 earnings Feb 2026; High] The 1% floor is buying back attribution from an eroding traffic base.

*Groupon lesson from RetailMeNot:* guaranteed floor as a trust primitive. "You will always get at least X% back" removes shopping-around from the consumer's decision tree. Cross-applied to Bucks, this becomes: "any purchase through Groupon always earns at least X Bucks, no matter what." This is a defensible positioning against competitors who have variable rates.

**Coupert** is a bootstrapped 8-11-person operation (Dover DE + Kowloon HK) with ~$1.2M revenue [Data - Latka; Estimate, single source]. Two mechanics matter: $1 withdrawal floor via Visa/Mastercard with 2% + $0.50 processing fee, and 72.92% claimed auto-apply success rate vs Honey's 33% (self-reported, not independently audited). [Data - Coupert research; Medium with integrity caveat] Trustpilot shows mixed reviews including $600+ unpaid-balance complaints.

*Groupon lesson from Coupert:* **the $1 floor as an activation trigger.** Let the user cash out at any amount with a small fee. Converts cashback from a distant future reward into an immediately usable one. Solves the "abandoned balance" trust problem that plagues every reward system. Elegant, cheap to implement.

**One data-gap flag:** the intake referenced "Honey shutdown" context for Coupert migration. Researched sources did NOT confirm a Honey shutdown - Honey's PayPal-era degradation is what sources describe. Re-verify before relying on this in exec messaging. [Data gap - flag from agent A4]

### 3.5 Scope note - pure-loyalty benchmark deferred

A Starbucks teardown was run as a pure-loyalty benchmark (see `raw/tier2-scan-and-starbucks-benchmark.md` for audit trail). The honest finding: Starbucks' habit engine is **pre-loaded stored value + mobile order**, not stars, and it does NOT port to Groupon because coffee is a daily consumable with deterministic price while Groupon purchases are episodic and unpredictable. The benchmark has been **dropped from this final report** to keep the recommendation set focused on mechanics that actually apply. Marriott Bonvoy was excluded earlier for the same reason (wrong frequency cadence).

The generic mechanics that would have been derived from Starbucks (weekly anchor, time-bound challenges, tier status for top spenders) either remain in the recommendation set with different attribution (Rakuten's Mobile Monday for the weekly anchor) or are deferred to later phases.

---

## 4. Mechanic Cards - What to Copy, in What Order, at What Cost

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

## 5. User Overlap, Switching Behaviour, and the Research Programme

**This section is essentially Rebecca §4.5, which is already investment-grade and should stand as-is. Summarising for continuity; full detail in Rebecca's original (see raw/rebecca-draft.md).**

Rebecca's recommended 5-phase research programme to move from directional evidence to investment-grade confidence:

- **Phase 1 (1-2 weeks, minimal cost):** Desk research. Semrush Audience Overlap dashboard ($289/mo or 7-day free trial), SimilarWeb Pro audience overlap, keyword gap analysis.
- **Phase 2 (3-4 weeks, $15-25K):** Quantitative survey of 1,000-2,000 Groupon coupons page visitors. Intercept via Qualtrics or Hotjar. Conjoint analysis on Bucks vs cash vs gift card.
- **Phase 3 (2-3 weeks, internal):** Behavioural analysis of existing data. Genie install-to-purchase analysis (981 Genie installs), coupons-to-deals cross-purchase analysis, Bloomreach email cohort test.
- **Phase 4 (4-6 weeks, $10-20K):** Qualitative depth interviews. 15-20 heavy cashback users (using 2+ platforms, earning $100+/yr).
- **Phase 5 (ongoing, built into PoC):** Live A/B testing. Extension activation incentives, stacking behaviour tracking, Bucks redemption funnel.

I'd add **Phase 1.5**: independent audit of at least one month's mystery-shopper activity to stress-test tracking reliability across Rakuten, Capital One Shopping, and Coupert. Tracking failure is the #1 churn driver across all three and Groupon must out-perform on this specific dimension from day one.

---

## 6. Executive Due Diligence Checklist

**Carried from Rebecca §5, selected high-leverage items with confidence ratings applied.**

### 6.1 Is the market opportunity real and big enough?

- Global cashback market $8-10B in 2024 growing to $22-23B by 2033 [Data, High]
- 76% of shoppers prefer cashback-offering stores [Data - Rebecca ref 16, Medium]
- 84% of Groupon app users on iOS [Data - Groupon internal, High]
- Honey's 8M-user exodus = the largest category acquisition window in years [Data - 9to5Google, High]
- **Red flag to watch:** the underlying category is under pressure. Rakuten flat revenue FY2025, Ziff Davis Tech & Shopping -18%, Ibotta revenue per redemption falling -5% YoY. Growth comes from B2B2C distribution and displacement of declining players, not category expansion. [Opinion, Medium]

### 6.2 Will users actually adopt this?

- Groupon users already stack 2-3 cashback extensions (affinity data) [Data, High]
- Bucks redeemable on local experiences is genuinely unique [Opinion, High]
- Safari extension bundled inside the Groupon app has a distribution path validated by Honey [Data, High]
- **BUT: activation rate of bundled Safari extensions is NOT publicly disclosed by Honey or Capital One Shopping.** We should assume moderate (10-30% of app users) until proven otherwise. [Data gap / Estimate, Low confidence]

### 6.3 Do the unit economics work?

- **This is the largest open question.** [Data gap]
- Rakuten's 2.4% International operating margin suggests the free tier is near break-even. Rakuten+ $100/yr paid tier launched Nov 2025 is a signal even the category leader can't make enough on the free tier alone.
- Capital One Shopping almost certainly runs at break-even on Rewards P&L in isolation, making up the difference via credit-card cross-sell. Groupon's equivalent cross-sell product is Groupon deals/experiences.
- **Required internal data: average commission per click-out by merchant category, redemption rate vs breakage on Groupon Bucks (if any exist today), Genie retention curve, coupons-to-deals crossover rate.** See `data-gaps.md`.

### 6.4 Can we actually build and ship this?

- Mobile eng for Safari extension: medium effort, ~6-8 weeks for iOS-first MVP
- Bucks ledger + redemption: medium effort, dependent on registration layer
- Safari extension bundling in Groupon app: requires App Store resubmit; US+IDN+EU rollout staggered
- **Critical dependency: identity / registration layer.** All loyalty mechanics require logged-in state. Current coupons page is largely anonymous. This is Phase 1 of the loyalty roadmap, not Phase 2.

### 6.5 Competitive dynamics and timing risks

- Honey acquisition window is time-bound. Every month Groupon delays is a month Coupert, Capital One Shopping, and Rakuten absorb the displaced users. [Opinion, High]
- AI-assistant displacement of shopping search (RetailMeNot Q4 2025 -18%) is a category-wide risk. Groupon's merchant direct relationships are the buffer - no one can replace a Local deal at a specific restaurant.
- Rakuten+ paid tier, if it proves traction (public data due early 2026), may reshape the economics of the free tier.

### 6.6 How do we measure success?

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

### 6.7 Internal data to pull immediately

Carried forward verbatim from Rebecca §5.7 plus my additions. See `data-gaps.md` for the consolidated list and owners.

---

## 7. Implications for Groupon's Strategy

### 7.1 Groupon's unique position

Unlike every competitor analysed, Groupon is the only platform that can bridge online coupons to local, in-person experiences. Rakuten bridges coupons to retail rewards. Ibotta bridges receipts to cashback. Only Groupon can offer "Earn Bucks from Nike, spend them on a massage near you." This is an unmatched strategic moat. [Rebecca §6.1]

### 7.2 Validation of proposed initiatives

**Layer 1 - Monetise (Immediate, Q2 now).** Every competitor monetises coupon traffic through multiple channels. Groupon's 30M annual sessions are an under-monetised asset. ~8 MD. Zero dependencies. [Rebecca §6.2]

**Layer 2 - Genie + Rewards (High conviction, Q2).** Extension users are demonstrably the highest-value segment. Capital One's $45-80 acquisition cost, Rakuten's $50 referral, and Honey's $235 per-user PayPal acquisition price (at peak) all confirm high extension-user LTV. Honey's scandal has created a unique acquisition window. ~15 MD. [Rebecca §6.2]

**Layer 3 - Safari Extension bundled with Groupon app (Strategic bet, Q2-Q3).** Honey and Rakuten both operate iOS Safari extensions today, confirming App Store feasibility. With 84% of Groupon app users on iOS, this is the largest untapped engagement channel. 2-week spike + registration layer. [Rebecca §6.2]

**Cashback / Bucks PoC (Growth driver, Q3+).** Every major competitor now operates cashback. Not having it is a competitive disadvantage. Groupon Bucks redeemable on local experiences is structurally advantaged. Requires registration layer first. [Rebecca §6.2]

### 7.3 Risks and considerations

- **Regulatory scrutiny of extensions.** Honey scandal led to Chrome Web Store policy change (Mar 2025) and multiple class actions. Design with transparent affiliate practices from day one. [Rebecca §6.3]
- **User extension fatigue.** Bundling Safari inside the Groupon app (as proposed) removes this friction. [Rebecca §6.3]
- **Payout economics.** Competitors paying cash face ongoing cost pressure. Groupon Bucks, redeemable only in-app against deals, offer structurally lower cost-of-reward while driving core business. [Rebecca §6.3]
- **Competitive response.** If Groupon's Safari extension gains traction, expect Rakuten and Honey to pursue deeper app integrations. Speed of execution matters. [Rebecca §6.3]
- **Trust-collapse risk.** Every mechanic must be transparently user-positive. The Honey chronology is the cautionary tale. If Groupon adopts ANY mechanic that only works when users don't understand it, instrument it honestly and publicly before launch. [My addition - High priority]

### 7.4 Recommended prioritisation

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

## 8. Slickdeals - Separate Partnership Workstream

**Slickdeals is NOT a loyalty competitor. It is a UGC deal-hunting community that Dusan has flagged as a potential partner for replacing Goods on core Groupon. This section summarises the standalone feasibility analysis at `partnership-feasibility-slickdeals.md`.**

### 8.1 Recommendation: Conditional Go on Option B (90-day embedded pilot), NOT full Goods replacement

**Dusan's thesis that Slickdeals is the #1 partner candidate is defensible IF the goal is "fill the Goods surface with credible physical-goods deals fast." But the framing "replace Goods" misdiagnoses the problem.**

- Goods failed on inventory/fulfilment economics, not on curation.
- A UGC feed solves demand-side deal discovery, which is a different problem.
- The community belongs to slickdeals.net. If the partnership ends, Groupon has zero residual audience - that's the DEAL BREAKER from the brief.

### 8.2 Core facts (2026 state)

- **Ownership:** Goldman Sachs Merchant Banking + Hearst since June 2018 ($500M deal). 8-year hold suggests exit within 12-24 months. Possible buyers: Amazon (owns Woot), Ziff Davis, Rakuten. [Data - Bloomberg, PR Newswire, Fried Frank; High]
- **Revenue:** $35-50M estimated 2025; working range $45-55M for 2026. [Data/Estimate, Medium]
- **Traffic:** 12M MAU, 40% DAU/MAU (excellent), 25M monthly visitors, +5% MoM Mar 2026. [Data - SimilarWeb; High]
- **Audience:** 63% male, 70% aged 18-44, higher income, US-only. **Inverse gender skew vs Groupon.** [Data - Slickdeals corp, SimilarWeb; High]
- **Economics:** Affiliate commissions 1-8.5% of GMV; SD holds negotiating leverage in any deal. [Data - enactsoft, HBS case; Medium-High]
- **AI shipping velocity:** March 2025 iOS redesign, AWS SageMaker personalisation rolled out (7% merchant click lift at re:Invent 2025). [Data - AWS re:Invent 2025 SMB206; High]

### 8.3 Five honest findings

1. **No public precedent for a white-label SD feed on a retail partner's core site.** Either strategic whitespace or a signal that partners prefer direct affiliate networks.
2. **The community is non-transferable.** Rent, not own. If partnership ends, the inventory ends.
3. **SD's upper-funnel pivot shifts incentives away from maximising affiliate click-out.** Neville Crawley's stated strategy is to convert MAU to DAU and go brand-advertising heavy. Partner incentives may diverge from Groupon's.
4. **Dusan's framing misdiagnoses the Goods problem.** Fulfilment, not curation.
5. **Amazon (owns Woot) is the most likely SD buyer.** Change-of-control risk is real.

### 8.4 Partnership conditions (must all be true)

- Pilot scope: 90 days, single Goods sub-category (e.g. consumer electronics), <5% of Goods surface
- 30-day termination clause, no exclusivity
- Change-of-control right to terminate on SD acquisition
- 24-month commission rate protection
- Light co-branding only ("Powered by Slickdeals"), not full SD takeover
- Groupon-side moderation filter (only deals with >N community votes, no expired)
- Metric gate: minimum $X revenue/mo + Y% CTR lift for renewal
- Parallel in-house "Groupon Deals Feed" project as alternative

### 8.5 Do not

- Sign a co-branded storefront (Option C) before Option B pilot succeeds.
- Acquire - Groupon market cap ~$600M-$900M; SD likely commands $700M-$1.2B+. Transformative capital commitment without strategic rationale.
- Let "replace Goods" framing drive the contract structure.

---

## 9. Data Gaps, Red Flags, Yellow Flags

### 9.1 Data gaps (consolidated from all agents + Rebecca + my additions)

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

### 9.2 Red flags (issues that could undermine the analysis or the business)

- **Trust-collapse vulnerability.** Every loyalty mechanic that is not transparently user-positive is a time-bomb. The Honey chronology is a 12-month loss of 40% of Chrome users. Groupon must architect the mechanic with transparency from day one - retrofitting trust after a MegaLag-equivalent expose is impossible.
- **Category saturation.** Rakuten revenue flat FY2025, Ziff Davis Tech & Shopping -18% Q4 2025, Ibotta revenue-per-redemption -5% YoY. The cashback extension market is not growing - it is consolidating. Groupon's entry must be additive (Bucks on local experiences) not substitutive (better cashback).
- **Time-bound acquisition window.** Honey's displaced users are being absorbed by Coupert / Capital One Shopping / Rakuten weekly. The longer Groupon delays, the smaller the available pool.
- **Regulatory escalation.** Rakuten Advertising, Impact.com, and Awin cut Honey off over five days in Jan 2026. The affiliate ecosystem is rewriting what is acceptable. Groupon's affiliate mechanic must meet the new standard, not the 2024 standard.

### 9.3 Yellow flags (monitor, not blockers)

- **"Honey shutdown" narrative may be inaccurate.** Sources describe degradation, user exodus, and affiliate-network termination - not a full shutdown. The PayPal wallet still runs Honey. Re-verify before exec messaging.
- **$45 Capital One Shopping anchor is an order of magnitude, not a fixed CAC.** Recent observed range is $40-80, with 90-day retention gate. Update the sizing model accordingly.
- **iOS Safari extension activation rates are undisclosed by all competitors.** Groupon sizing must assume 10-30% activation until we have our own data.
- **SD PE exit clock.** GS has held 8 years. If Amazon buys SD, any Groupon partnership would likely be killed or radically shifted. Change-of-control terms are non-negotiable.

---

## 10. Source Reference Index

### Rebecca's original references [1]-[60]

See `raw/rebecca-draft.md` for the full list. Citations in this merged document use Rebecca's numbering when referencing her-originated data, and my-side references [M1]-[M70] for mine.

### My additional references [M1]-[M70]

**Rakuten [M1]-[M27]:** rakuten.com/blog (Big Fat Check schedule), rakuten.com/help (welcome bonus terms, how Rakuten works, Safari iOS walkthrough), Rakuten Group FY2024 Financial Results Feb 14 2025 (press release), Rakuten Group Q3 FY2025 Results Nov 13 2025, SimilarWeb rakuten.com Mar 2026, Trustpilot (36,643 reviews 4.6 stars), Dollar Sprout Rakuten Review 2025, CNBC Select Rakuten Review 2025, Rakuten+ launch WWD / Retail TouchPoints Nov 12 2025, Bilt Newsroom Rakuten partnership, Statista Rakuten quarterly US GMS, Justia Oganesyan v Rakuten USA docket 4:2025cv01534, PhatWallet Big Fat Check bounce thread Mar 2024.

**Capital One Shopping [M28]-[M48]:** capitaloneshopping.com help center, CNBC Wikibuy acquisition Nov 2018, PR Newswire class action settlement announcement Sep 2025, ABA Banking Journal Dec 2025 preliminary approval, classaction.org Capital One influencer lawsuit, SimilarWeb capitaloneshopping.com Mar 2026, Apple Community Safari #2 ranking July 2025, Doctor of Credit referral bonus history, Frequent Miler $80 referral + gift card redemption options, Trustpilot capitaloneshopping.com (1.3 stars, 305 reviews), Milestalk "I'm done with Capital One Shopping", PhatWallet $45-bonus thread, Chrome Web Store Capital One Shopping 6M+ users.

**PayPal Honey [M49]-[M70]:** 9to5Google Honey tracking series (Jan 3 2025, Mar 31 2025, May 23 2025, Jul 7 2025, Dec 22 2025, Dec 31 2025), ppc.land Rakuten Advertising termination Jan 2026, ppc.land Impact.com removal, ppc.land Awin suspension, Affiverse MegaLag Part 2 coverage, Cohen Milstein case page In Re PayPal Honey Browser Extension Litigation, Orrick Dec 2025 dismissal coverage, Ben Edelman benedelman.org Honey breaches analysis, heise.de Honey Safari iOS bundling flag, PayPal Q4 2025 earnings release Feb 3 2026, help.joinhoney.com (Gold program, Safari extension, Droplist), joinhoney.com/terms, PayPal Gold Program T&Cs (paypalobjects.com PDF), MegaLag YouTube Part 1 and Part 2, TechCrunch $4B acquisition Nov 2019, Wikipedia PayPal Honey (policy changes and lawsuits section).

**Tier 2 [M71]-[M84]:** Ibotta investor relations Q4 2025 + Q3 2025, Motley Fool Ibotta Q4 2025 earnings call transcript, IPN website, Grocery Dive DoorDash + Instacart partnerships, RetailMeNot 1% floor announcement Feb 25 2026, Ziff Davis Q4 2025 earnings Feb 2026, A Media Operator Ziff Davis affiliate drop, Dollar Sprout Coupert review, Coupert vs Honey 2025 test, Latka Coupert revenue, Crunchbase Coupert profile, Trustpilot coupert.com.

*Starbucks references (initially [M85]-[M96]) removed with scope pruning; Starbucks raw research preserved at `raw/tier2-scan-and-starbucks-benchmark.md` for audit trail.*

**Slickdeals [M97]-[M110]:** Slickdeals corporate / sales pages, Warburg Pincus to Goldman Sachs sale 2018 (PR Newswire, Bloomberg, Fried Frank), Groupon Q3 2025 results (investor.groupon.com), LA Business Journal Slickdeals upper-funnel pivot, AWS re:Invent 2025 SMB206 (Slickdeals AI with SageMaker), SimilarWeb slickdeals.net + SD vs Groupon comparison, HBS Digital Innovation case studies (Slickdeals Monetizing Frugality / Treasure Hunting), Awin publisher spotlight, Kevel customers case, Seeger Weiss Honey/Cap One class action.

---

## 11. Appendix

### 11.1 AI funnel transparency (Adam's Apr 20 requirement)

See `ai-funnel-appendix.md`. Summary: 5 parallel research subagents (Opus 4.7, 1M context) ran 2-6 WebSearch rounds each. Rebecca's Google Doc fetched via `gws docs documents get` CLI (direct API, no copy-paste). Every claim labelled [Data] / [Estimate] / [Opinion] / [Assumption] with High/Medium/Low confidence. Data gaps declared explicitly rather than filled with guesses. Raw per-agent outputs preserved in `raw/` for audit trail.

### 11.2 Glossary

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

### 11.3 Deltas from Rebecca's April 2026 draft (for audit transparency)

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
