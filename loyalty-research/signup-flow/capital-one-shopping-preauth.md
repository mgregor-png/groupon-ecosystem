# Capital One Shopping - Public Pre-Auth User Experience

*AI-captured pre-authentication evidence for Groupon competitive intelligence*
*Access date: 2026-04-22 (fetched 2026-04-21 from CZ IP, Prague)*
*Scope: Public pages only - no account creation, no logged-in session*
*Companion docs: `raw/capital-one-shopping-mechanics.md` (deep teardown), `raw/signup-evidence/capone/public-capture.md` (prior capture, superseded in part by this file)*

---

## 1. Executive Summary - what pre-auth users see

**The single biggest headline:** The current (Apr 2026) sign-in flow is **passwordless / magic-link by default**. The sign-in page shows "Send me a sign in link" as the primary CTA, with "Sign in a different way" as a secondary option. This is a structural change from the "email + password" model captured in prior rounds. [Data, High - direct WebFetch 2026-04-21]

**The second biggest headline:** There is **no dollar-amount signup bonus on the pre-auth homepage hero**. The $80/$80 referral program exists but is only reachable via a referral link, not via organic visits. A different "$10 spend in 21 days" bonus appears only on the iOS App Store listing, not on the web homepage. [Data, High]

**The third headline:** The "1 Credit = $1" soft-currency mechanic, the ~50 gift card retailer list, and all redemption catalog details are **auth-gated**. Pre-auth prospects see "Rewards" framing with implied dollar equivalence (e.g. "+2% back at Target", "up to 16.5% back at DoorDash") but no explicit currency explanation. [Data, High]

**Trust posture:** Despite the Dec 2025 $4M affiliate-commission class action (preliminary approval Dec 18, 2025; final hearing Jun 10, 2026; claim deadline Apr 17, 2026 - 5 days before this capture), Cap One has **not added explicit post-settlement affiliate-disclosure language** to the consumer-facing Terms of Service (effective Nov 19, 2025) or Privacy Policy (effective Feb 18, 2026). The ombudsman + compliance review commitments live only in legal filings. [Opinion, High - based on direct fetch + settlement documents]

---

## 2. Per-Dimension Findings

### 2.1 Current headline install incentive (April 2026)

**Web pre-auth homepage:** No dollar-amount signup bonus visible in the hero. Homepage copy focuses on "daily offers", auto-applied coupons, and per-merchant reward percentages. [Data, High - WebFetch 2026-04-21, https://capitaloneshopping.com/]

**Referral program (gated behind referral link):** $80 for referrer + $80 for new user. Requires extension install within 7 days of account creation, full permissions, on a device that has never had the extension installed before. Retention gate: use the extension for 90 days. Referrer cap: $1,900 (up from $500 earlier in 2024). US-only, 18+, new users only. [Data, High - Doctor of Credit Feb 24 2026, Frequent Miler, Thrifty Traveler Mar 30 2026, Upgraded Points Apr 2026, corroborated via April 2026 WebSearch round]

**Separate iOS Safari extension bonus:** App Store description states "add the Safari Shopping extension, allow access on all sites, create or log in to your account, verify your email and **spend $10 in 21 days** to be eligible for your bonus" with rewards "issued within 30 days". Dollar amount not disclosed in the App Store copy. [Data, High - WebFetch apps.apple.com 2026-04-21]

**Historical $45 reference:** The "$45" figure Dusan anchors to does NOT appear in Doctor of Credit's verified historical list (which tracks $30/$40/$50/$60/$75/$80/$200 variants). The closest documented variant was "$40 bonus after spending $15 within 90 days" from a Dec 2024 public link. The "$45" figure appears primarily in SEO blog content (Saint Augustine's, Martins Flooring) of uncertain authority. [Data, High - cross-verified]

**YMMV nature:** All historical amounts are targeted/YMMV - many users cannot access any referral bonus on any given day. [Data, High]

**Recommendation for Groupon sizing:** Reframe from "$45 anchor" to **"$40-$80 range with 90-day retention gate, US-only, YMMV"**. The retention mechanic is more strategically interesting than the dollar amount. [Opinion, High]

### 2.2 Signup form fields

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

### 2.3 "How it works" messaging

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

### 2.4 Shopping Credits explanation pre-auth

**"1 Credit = $1" is NOT visible on any Cap One pre-auth public page.** [Data, High - verified across /, /help, /rewards (404), /gift-cards (404), /our-terms/, and editorial]

The editorial page uses "Rewards" consistently. The ToS states users must accumulate "a minimum balance of $1.00 worth" of Rewards to redeem, and caps redemption at "$500.00 worth of Shopping Rewards in any single transaction" - but does not define a "credit" unit. [Data, High - direct ToS fetch]

The "1 Credit = $1" framing comes from third-party review content (Frequent Miler, Upgraded Points, The Points Guy, FinanceBuzz). It is **Groupon-internal research framing**, not Cap One marketing language. [Data, High]

**Implication:** Groupon's "Bucks" soft-currency concept should not assume prospects understand a "1 unit = $1" frame from Cap One precedent. Cap One hides the mechanic behind "Rewards" until account creation. [Opinion, High]

### 2.5 Redemption catalog messaging

**The gift-card-only constraint is NOT explicitly shown pre-auth.** The `/rewards` and `/gift-cards` pages both return 404 to unauthenticated visitors. [Data, High - verified in prior round]

Pre-auth users see only the outbound-shopping offer cards (e.g. "+2% back at Target") which create an implicit cashback expectation. The fact that Rewards can ONLY be redeemed as digital gift cards (no cash-out, no statement credit, no bank deposit) is auth-gated. [Data, High]

The Capital One editorial page uses the phrase "redeem your Capital One Shopping Rewards for digital gift cards from dozens of retailers" - "dozens" is the specific hedge language; no explicit "50+ retailers" number is published. [Data, High]

**Implication:** Cap One is strategically quiet about the gift-card-only constraint pre-auth. This is a retention-hostile mechanic that would hurt signup conversion if disclosed. [Opinion, High]

### 2.6 Safari extension install page copy

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

### 2.7 Chrome Web Store listing

**DATA GAP - CZ IP blocks Chrome Web Store directly.** EU consent redirect intercepts the fetch. chrome-stats.com mirror returned 403. [Gap, High]

**Indirect evidence (April 2026 WebSearch):**
- User count: "over 6 million users" (consistently cited across review sites April 2026) [Data, Medium-High]
- Review count: "over 10,000 reviews" (review-site citation); one source reports 91,392 ratings [Data, Medium - discrepancy unresolved]
- Star rating: 4.5 / 5 (most cited); one source says 4.7 [Data, Medium - discrepancy unresolved]
- Last updated: **April 20, 2026** (within 2 days of capture - indicates active maintenance) [Data, High]

**Recommendation:** US-IP verification needed to resolve review-count discrepancy. [Gap, High - carried forward from prior round]

### 2.8 iOS App Store listing refresh

- **Current rating (2026-04-21):** 4.9 stars, 1.6M ratings [Data, High]
- **Prior research anchor:** 4.9 / 960K historical [Data, from prior rounds]
- **Growth:** ~66% growth in ratings count over recent period (960K -> 1.6M). This is a strong retention / usage signal. [Inference, High]
- **Update cadence:** 3-4 days between releases (v2.127.0 released 2026-04-17) [Data, High]
- **What's New text:** "Performance improvements" - no feature-launch signaling in public release notes [Data, High]

### 2.9 Trust / privacy messaging (especially post-Dec 2025 class action)

**Class action status:** $4M settlement, preliminary approval Dec 18 2025, claim deadline **Apr 17 2026** (5 days before this capture), final approval hearing **Jun 10 2026**. Covers affiliate commissions allegedly diverted from content creators. [Data, High - ABA Banking Journal, classaction.org, InfluencerMarketingClaims.com]

**Consumer-facing pages - no post-settlement update language:**
- **Terms of Service** (`/our-terms/terms-of-service`): Effective **Nov 19, 2025** (predates preliminary approval by 1 month). Contains: `"We earn a commission when you make eligible purchases from certain Merchants using the Shopping Browser Companion or Mobile App and we may share those commissions with you as Rewards."` Class action waiver is **merchant-scoped only**, not user-scoped. [Data, High]
- **Privacy Policy** (`/our-terms/privacy-policy`): Effective **Feb 18, 2026** (post-settlement). Contains: `"Capital One Shopping does NOT sell your personal information to any third party for the third party's own marketing purposes"` and `"we exchange lists of user email addresses with other Capital One affiliates located in the United States, Canada, and the UK"`. **Does NOT contain** explicit post-settlement language about last-click attribution or competing-extension cookie behavior. [Data, High]

**Homepage affiliate disclosure (visible pre-auth):**
> "Capital One Shopping earns a commission when you make eligible purchases from merchants and we may share those commissions with you as rewards."

This line appears in homepage footer context. It is the standard commission-disclosure frame, not post-settlement transparency. [Data, High]

**The ombudsman + compliance-review commitments live in the settlement filing, not in consumer pages.** This is a material gap: Cap One's legal-side commitments are not yet reflected in marketing-facing trust language. [Opinion, High]

**Implication for Groupon:** Groupon can pre-empt this gap by adding clean, consumer-facing affiliate-disclosure language (e.g. "We respect the affiliate link you clicked first") from day 1 - differentiation without regulatory pressure. [Opinion, High]

### 2.10 Capital One bank tie-in messaging

**Editorial page verbatim:**
> "It's free for everyone, even people who aren't already Capital One customers."

**iOS App Store description verbatim:**
> "100% free for everyone - no Capital One bank or credit card account required!"

**Homepage:** No Capital One bank account promo visible. No "Apply for a Cap One card" upsell on pre-auth pages. [Data, High]

**Strategic observation:** Cap One Shopping is positioned as **standalone acquisition funnel**, NOT as a Cap One banking tie-in. This is consistent with Walt Coon's original Wikibuy DNA (acquired 2018, ~$2M users at acquisition). [Opinion, High]

**Backend monetization (not disclosed pre-auth):** Cap One uses Cap One Shopping's first-party data via Rakuten Advertising's Audience Engine for credit-card customer acquisition targeting. This is the real monetization but is not visible pre-auth. [Data, Medium-High - Rakuten case study]

---

## 3. Material Changes vs Prior Capture (2026-04-21 prior round)

1. **Sign-in flow is now passwordless-first.** Prior capture noted "Email + Password" as the form-field default. Current fetch (2026-04-21) shows "Send me a sign in link" as primary, password as secondary. This is a structural change within the past ~24 hours of capture time or was missed in prior capture. [Data, High - verify against prior screenshot if available]

2. **iOS main app ratings grew from 960K (prior research anchor) to 1.6M (current).** ~66% growth. Indicates sustained usage / install velocity. [Data, High]

3. **Chrome Web Store extension updated 2026-04-20** (2 days before fetch). Active maintenance signal. [Data, High]

4. **Class action claim deadline just passed (Apr 17, 2026).** Cap One has not yet propagated settlement language to consumer pages. Watch Jun 10, 2026 final hearing. [Opinion, High]

---

## 4. Data Gaps (carried forward + new)

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

## 5. Recommendations for Groupon

### 5.1 Rebase the $45 anchor
[Opinion, High] Drop "$45" as a fixed reference. Use **"$40-$80 range with 90-day retention gate, US-only, YMMV-targeted"**. The retention gate is the strategically interesting design element - it converts bonus-hunters into habit-formed users. An A/B between retention-gated ($80) and spend-gated ($10 in 21 days) would be informative.

### 5.2 Don't market "soft currency transparency"
[Opinion, High] Cap One hides "1 Credit = $1" behind auth. The pre-auth hook is "daily offers + coupons + price match", not currency mechanics. Groupon's Bucks pre-auth marketing should mirror this: lead with dollar savings on offers, not with soft-currency transparency.

### 5.3 Consider passwordless as a default
[Opinion, Medium] Cap One's current sign-in flow is magic-link-first. This lowers activation friction. Groupon should evaluate this against the "commitment tax" argument (making users invest in a password may improve day-7 retention).

### 5.4 Pre-empt affiliate-disclosure regulation
[Opinion, High] Cap One's consumer pages do NOT reflect settlement commitments. Groupon can ship clean affiliate-disclosure language from day 1 - a differentiator.

### 5.5 Bundle, don't fragment SKUs
[Opinion, High] Cap One's standalone iOS Safari extension SKU has zero ratings; all reviews are in the main iOS app (4.9 / 1.6M). Groupon's iOS Safari extension should be bundled inside a primary Groupon app, not a standalone SKU.

### 5.6 Auth-gate the redemption catalog
[Opinion, Medium-High] Cap One does not show the 50+ gift card list pre-auth. This is a commitment tax: users install + authenticate before discovering the redemption constraint. Groupon should consider the same posture.

### 5.7 Two parallel activation gates exist
[Data, High] Web referral: 90-day retention, no purchase required. iOS extension: $10 spend in 21 days. Groupon should A/B test both structures - they attract different user populations.

---

## 6. Sources (all fetched / verified 2026-04-21 or April 2026)

### Primary (direct fetch)
1. `https://capitaloneshopping.com/` - homepage [2026-04-21]
2. `https://capitaloneshopping.com/sign-in` - sign-in / signup [2026-04-21] - **key change: passwordless default**
3. `https://capitaloneshopping.com/our-terms/terms-of-service` - ToS effective Nov 19, 2025 [2026-04-21]
4. `https://capitaloneshopping.com/our-terms/privacy-policy` - Privacy Policy effective Feb 18, 2026 [2026-04-21]
5. `https://capitaloneshopping.com/help` - help center (structural only; articles not accessible via WebFetch)
6. `https://apps.apple.com/us/app/capital-one-shopping-save-now/id1089294040` - iOS main app [2026-04-21]
7. `https://apps.apple.com/us/app/capital-one-shopping-extension/id1477110326` - iOS Safari extension SKU (prior round, no aggregated rating)
8. `https://www.capitalone.com/learn-grow/money-management/capital-one-shopping/` - editorial

### Third-party corroboration (April 2026)
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

### Class action / legal
21. `https://www.influencermarketingclaims.com/` - settlement site
22. `https://www.prnewswire.com/news-releases/if-you-advertised-online-with-merchants-and-affiliate-networks-who-partnered-with-capital-one-shopping-...` - settlement notice
23. `https://www.classaction.org/news/capital-one-settlement-ends-affiliate-marketing-commission-class-action-lawsuit` - settlement
24. `https://bankingjournal.aba.com/2026/01/virginia-district-court-grants-preliminary-approval-for-settlement-in-influencer-lawsuit-against-capital-one/` - ABA Jan 2026
25. `https://openclassactions.com/settlements/capital-one-shopping-affiliate-settlement.php` - settlement details
26. `https://topclassactions.com/lawsuit-settlements/lawsuit-news/capital-one-hit-with-class-action-over-allegedly-unpaid-cashback-rewards/` - secondary suit (unpaid cashback)

### Web Store (indirect, CZ IP blocked)
27. `https://chromewebstore.google.com/detail/capital-one-shopping-save/nenlahapcbofgnanklpelkaejcehkggg` - blocked, via third-party mirror

---

## 7. Confidence Summary

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
