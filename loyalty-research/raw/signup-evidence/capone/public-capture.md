# Capital One Shopping - Public Page Evidence Capture

**Fetch date:** 2026-04-21
**Scope:** Pre-auth public pages only (no account creation)
**Fetched from:** CZ IP (Prague)
**Companion doc:** `../capital-one-shopping-mechanics.md` (deep teardown - not duplicated here)
**Purpose:** Verifiable, copy-verbatim primary-source evidence for the loyalty-research package

---

## 1. Summary

### Verdict on the $45 install offer (critical)

**The $45 install offer is NOT the currently visible headline on capitaloneshopping.com as of 2026-04-21.** [Data, High confidence]

What IS shown instead on the pre-auth landing:
- No specific dollar signup bonus on the homepage hero at all. Homepage copy focuses on "daily offers", auto-applied coupons, and merchant reward percentages (e.g. "+2% back at Target", "+up to 16.5% back at DoorDash")
- The current structural offer in market is **$80 referrer / $80 new user**, not $45. This requires a referral link - you cannot reach it from the homepage on a fresh visit.
- App Store copy for the iOS Safari Extension mentions a **separate "sign up bonus"** gated on "add the Safari Shopping extension, allow access on all sites, create or log in to your account, verify your email and **spend $10 in 21 days**" with rewards "issued within 30 days". Dollar amount not stated in the App Store copy.

**Historical $45 offer (mechanics of record):**
The documented $45 variant was "$40 bonus after spending $15 within 90 days" (Dec 2024 public signup link per Doctor of Credit), not exactly $45. The "$45" that circulates in blog content appears to be SEO content on non-authoritative sites (Saint Augustine's, Martins Flooring) with promotional copy that may have never been an official Capital One Shopping headline. [Data, High - confirmed by Doctor of Credit Feb 24 2026 update, which lists every historical referral amount and does not list $45 anywhere]

**Dusan's $45 anchor is therefore fragile as a literal number.** The defensible range is **$40-$80 for a 90-day-retention install gate**, with the specific $45 variant being either (a) a YMMV historical variant, or (b) SEO content confusion. Recommend reframing the Groupon sizing to "$40-$80 industry-standard install CAC with a 90-day retention gate" rather than citing $45 as a fixed anchor.

### What IS currently live and verified [Data, High]
- Homepage (capitaloneshopping.com): live, shows daily offers and merchant percentages, no dollar signup bonus in hero
- Terms of Service: effective **November 19, 2025** (live)
- Privacy Policy: effective **February 18, 2026** (live)
- $80/$80 referral program with 90-day install retention + $1,900 referrer cap (live per Feb 24 2026 Doctor of Credit, Mar 30 2026 Upgraded Points)
- US-only, 18+, new-user-only
- iOS App 4.9 stars, 1.6M ratings (Wikibuy LLC)
- Class action settlement: $4M, preliminary approval Dec 18 2025, claim deadline **Apr 17 2026** (just passed), final hearing Jun 10 2026
- Business practice changes committed for min 2 years including an **ombudsman**

---

## 2. Per-Page Findings

### 2.1 Homepage - capitaloneshopping.com
**URL:** https://capitaloneshopping.com
**Fetched:** 2026-04-21
**Status:** 200, live
**Confidence:** High

**Verbatim hero copy:**
> "Save with your daily offers!"
> "It's kinda genius, join now for free."

**Primary CTA:** "Get this Deal" (repeated per-offer); "Continue" (account-creation flow)

**Form fields visible on homepage signup widget:**
- Email Address
- Password

**Value prop copy verbatim:**
> "Capital One Shopping earns a commission when you make eligible purchases from merchants and we may share those commissions with you as rewards"
> "Capital One Shopping gets you better offers, automatically applies coupon codes at checkout, and lets you know when prices drop on products you've viewed and purchased."

**Offer examples displayed:**
- "Earn up to $100 when you book a rental car over $100!" (rental cars)
- "+2% back" at Target
- "+up to 16.5% back" at DoorDash

**Footer links:** Privacy Policy, Terms of Service, Help Center, Capital One, About Capital One Shopping, Brands, Press, Sitemap

**Key observation:** No "$45", "$80", "$40", or any fixed dollar signup bonus appears on the pre-auth homepage hero. The "How do we make money" line is the transparency framing Cap One shows instead of a bonus.

---

### 2.2 /how-it-works
**URL:** https://capitaloneshopping.com/how-it-works
**Fetched:** 2026-04-21
**Status:** **404 - page does not exist**
**Confidence:** High

No dedicated /how-it-works page. This is surprising for an acquisition funnel and suggests Cap One relies on (a) the homepage + (b) the Capital One editorial blog at capitalone.com/learn-grow/.

---

### 2.3 /rewards and /gift-cards
**URLs:** https://capitaloneshopping.com/rewards, https://capitaloneshopping.com/gift-cards
**Fetched:** 2026-04-21
**Status:** **Both 404**
**Confidence:** High

**DATA GAP:** The ~50 retailer list, denomination options, and the explicit "1 Credit = $1" statement are NOT available on pre-auth public pages. They are behind the account login. [Data, High]

This matters for the research package: the "1 Credit = $1" framing in the deep-dive doc comes from Capital One's editorial + third-party reviews (Frequent Miler, Upgraded Points), not from a public Cap One Shopping marketing page. Groupon should not assume this is "publicly visible" to prospects.

---

### 2.4 Terms of Service
**URL:** https://capitaloneshopping.com/our-terms/terms-of-service
**Fetched:** 2026-04-21
**Status:** 200, live
**Effective date:** **November 19, 2025**
**Confidence:** High

**Verbatim affiliate/commission language:**
> "We earn a commission when you make eligible purchases from certain Merchants using the Shopping Browser Companion or Mobile App and we may share those commissions with you as Rewards."
> "Merchants may also pay us to feature them on our website, in emails, and elsewhere."

**Verbatim referral eligibility:**
> "For a Referrer to be eligible...said new user must use your custom referral link to install the Capital One Shopping desktop or mobile browser extension and enroll in an account."
> "A Refer-ee must be a qualifying new user...subject to verification by Capital One Shopping, including to verify that such new user does not have (and has not had) a Capital One Shopping User Account."

**Verbatim Shopping Rewards redemption:**
> "You may redeem Shopping Rewards provided, however, that you may not redeem more than a value of $500.00 worth of Shopping Rewards in any single transaction."
> "In order to be eligible to redeem Shopping Rewards...(2) you must have accumulated a minimum balance of $1.00 worth."

**Eligibility:**
> "You must be an individual 18 years of age or older to use the Services."
> "Except as expressed below, use of the Services is limited to permissible jurisdictions within the United States of America."

**Class action waiver (merchant-only, not user-level):**
> "IF YOU ARE A MERCHANT, YOU AND CAPITAL ONE SHOPPING AGREE THAT YOU AND CAPITAL ONE SHOPPING MAY BRING CLAIMS AGAINST THE OTHER ONLY IN YOUR OR OUR INDIVIDUAL CAPACITIES AND NOT AS A PLAINTIFF OR CLASS MEMBER IN ANY PURPORTED CLASS OR REPRESENTATIVE PROCEEDING."

**Observation:** The class-action waiver is scoped to merchants only. Regular users retain class-action standing, which is consistent with the Dec 2025 influencer/affiliate class suit proceeding.

---

### 2.5 Privacy Policy
**URL:** https://capitaloneshopping.com/our-terms/privacy-policy
**Fetched:** 2026-04-21
**Status:** 200, live
**Effective date:** **February 18, 2026** (updated post-settlement preliminary approval)
**Confidence:** High

**Verbatim data-sharing disclosures:**
> "Capital One Shopping does NOT sell your personal information to any third party for the third party's own marketing purposes"
> "we exchange lists of user email addresses with other Capital One affiliates located in the United States, Canada, and the UK"

**Cookie handling (verbatim):**
> [uses cookies to track] "coupons that you used"

**Key observation:** The privacy policy was updated Feb 18 2026, approximately 2 months after the class action preliminary approval (Dec 18 2025). It does NOT contain explicit post-settlement language about last-click attribution or competing-extension cookie behavior - those changes are presumably in the commissioning-side business practice commitments (ombudsman, compliance reviews), not in the consumer-facing privacy policy. [Opinion, Medium]

**DATA GAP:** No public-facing commitment about respecting competing affiliate cookies is visible on the privacy policy or ToS. The ombudsman commitment is in legal filings, not on the consumer pages.

---

### 2.6 Chrome Web Store listing
**URL:** https://chromewebstore.google.com/detail/capital-one-shopping-save/nenlahapcbofgnanklpelkaejcehkggg
**Fetched:** 2026-04-21
**Status:** **302 redirect to Google consent.google.com page from CZ IP**
**Confidence:** High on redirect, **DATA GAP** on user count

**DATA GAP: could not fetch Chrome Web Store listing from CZ IP.** The EU consent redirect blocks programmatic fetch. Per the deep-dive doc (and cached SimilarWeb/Chrome Web Store data from prior rounds), the listing shows "6M+ users, 10K+ reviews" - but I cannot independently verify from this session.

Action for fact-check: re-verify Chrome Web Store numbers from a US IP or via a US-based reviewer.

---

### 2.7 iOS App Store - main app
**URL:** https://apps.apple.com/us/app/capital-one-shopping-save-now/id1089294040
**Fetched:** 2026-04-21
**Status:** 200, live
**Confidence:** High

**Verbatim metadata:**
- Star rating: **4.9 stars**
- Ratings count: **1.6M ratings**
- Developer: **Wikibuy, LLC** (note: legacy Wikibuy branding on developer line)
- Category: Shopping
- Size: 161.5 MB
- Age rating: 4+
- Latest version: 2.127.0 (3 days ago from fetch date)

**Verbatim signup bonus language (app description):**
> "add the Safari Shopping extension, allow access on all sites, create or log in to your account, verify your email and spend $10 in 21 days"
> rewards "issued within 30 days of completing all sign up bonus requirements"

**Key observation:** The App Store version of the signup bonus does NOT state a dollar amount and uses a **$10 spend in 21 days** gate, not 90 days. This is a *different* install flow than the $80 web referral (90-day retention). The iOS Safari extension may be operating a distinct acquisition mechanic with lower commitment threshold.

**What's New:** "Performance improvements" (across multiple recent versions - no feature-launch signal)

**Notable user feedback from the public listing:**
- Positive: "a couple thousand dollars since I began using COS"
- Negative: "$1,000 in rewards" dispute claim denied

### 2.8 iOS App Store - Safari Extension (separate listing)
**URL:** https://apps.apple.com/us/app/capital-one-shopping-extension/id1477110326
**Fetched:** 2026-04-21
**Status:** 200, live
**Confidence:** High

**Verbatim metadata:**
- Star rating: "This app hasn't received enough ratings or reviews to display an overview" - **no rating visible** [Data, High]
- Review count: not displayed
- Developer: Wikibuy, LLC
- Version: 2.43.0 (dated Apr 13)

**Verbatim description:**
> "A simple and free way to help you save online. Here's how it works: Available coupons are instantly applied to your cart at checkout. Capital One Shopping searches for a better price while you shop at Amazon, Target, Nike and over 100,000 other stores...In the last year alone, we've saved users over $160 million."

**Key observation:** The dedicated Safari extension listing has **no aggregated rating** - this is a meaningful data point for Groupon. It suggests the extension is either (a) too new for significant review volume or (b) usage is concentrated inside the main iOS app rather than through this standalone extension SKU. For Groupon's iOS Safari extension planning, this suggests **users discover via the main app, not via a standalone extension store page**. [Opinion, Medium]

**Disclosure:** "Some services may not be available outside the United States."

---

### 2.9 Capital One editorial page
**URL:** https://www.capitalone.com/learn-grow/money-management/capital-one-shopping/
**Fetched:** 2026-04-21
**Status:** 200, live
**Confidence:** High

**Section headings verbatim:**
- What is Capital One Shopping?
- Is there a fee for Capital One Shopping?
- How does Capital One Shopping work?
- Coupon codes
- Price comparisons
- Price-drop notifications
- Rewards
- How to redeem Capital One Shopping Rewards
- Do Capital One Shopping Rewards expire?
- Key takeaways: Capital One Shopping

**Verbatim eligibility statement:**
> "It's free for everyone, even people who aren't already Capital One customers."

**Verbatim redemption language:**
> "redeem your Capital One Shopping Rewards for digital gift cards from dozens of retailers"

**Key observation:** This editorial page does NOT use the phrase "Shopping Credits" and does NOT state "1 Credit = $1". Users see "Rewards" consistently. The "1 Credit = $1" wording comes from third-party review sites, not Cap One's own marketing. **This is important: Groupon's Bucks concept should NOT assume the public understands a "1 unit = $1" soft currency just because Cap One does it. The public framing is "Rewards" with implied dollar equivalence.**

**No bonus dollar amounts** appear in the editorial.

---

### 2.10 Third-party verification of current offer (Doctor of Credit)
**URL:** https://www.doctorofcredit.com/join-capital-one-shopping-get-10-after-spending-10/
**Fetched:** 2026-04-21
**Last article update:** February 24, 2026
**Confidence:** High

**Current headline (verbatim quoted):**
$80/$80 referral bonus, YMMV.

**Historical amounts documented:**
- $200/$200 (Dec 2023, disputed)
- $75/$75 and $50/$50 (Nov 2023)
- $60/$60 (Nov 2025)
- $40/$40 (Mar 2024, Oct 2024, Aug 2025, current base rate)
- $30/$30 (Sep 2023)
- **$45 NOT in the historical list**

**Terms verbatim:**
> "install either the Shopping desktop or mobile extension in their primary browser with full permissions, and on a device in which the extension has never previously been installed" within 7 days
> "regularly use the Shopping extension and shop as they normally would" for 90 days
> "$1900 in referral bonuses from the referral program" (cap)
> "both the Referrer and Refer-ee must be located in and reside in the United States"

**December 2024 public (non-referral) link:** "$40 bonus after spending $15 within 90 days" - this is the closest historical match to "$45". Not $45.

---

### 2.11 Class action / affiliate disclosure (post-May 2025)
**Primary settlement site:** www.InfluencerMarketingClaims.com
**Court:** U.S. District Court for the Eastern District of Virginia
**Confidence:** High

**Verbatim key terms:**
- Class period: January 6, 2020 - December 18, 2025
- Settlement fund: approximately $4M
- Preliminary approval: December 18, 2025
- Claim deadline: **April 17, 2026** (4 days before this capture)
- Final approval hearing: June 10, 2026
- Compensation: "uncapped proof payments that reimburse 100% of qualifying commissions received after Nov. 1, 2023" OR "$20 alternative payment"

**Verbatim business-practice commitments:**
> "implementing enforceable business practice changes for at least two years, including regular compliance reviews and the appointment of an ombudsman to address affiliate and merchant concerns"

**Key observation:** The ombudsman and compliance review commitments are in the settlement filing, NOT in the consumer-facing ToS (Nov 19 2025 effective date predates the preliminary approval by 1 month) or Privacy Policy (Feb 18 2026 update). This means Cap One has not yet propagated any post-settlement affiliate-disclosure language into pre-auth consumer pages. [Opinion, High]

---

## 3. Inferences for Groupon (Bucks / soft-currency design)

### 3.1 The install bonus is a range, not a fixed anchor
[Opinion, High] The $45 literal figure is not the current headline. Rebase Groupon's planning on **$40-$80 as the range, with 90-day install retention as the enforcement mechanism**. That retention gate is more important than the dollar amount - it converts bonus-hunters into habit-formed users.

### 3.2 Cap One's pre-auth pages hide the currency mechanic
[Data, High] A fresh visitor sees "daily offers" and "auto-applied coupons" on the pre-auth homepage. They do NOT see "1 Credit = $1", a retailer list, or a bonus dollar amount. The transparent currency is an **internal retention feature**, not an acquisition hook.
**Implication for Groupon:** Bucks should be marketed on "daily offers + price match" value, NOT on "soft currency transparency". Currency mechanics reveal themselves only after account creation.

### 3.3 Two different signup gates exist in parallel
[Data, High] The web referral uses **90-day retention, no purchase**. The iOS Safari extension flow uses **21-day $10 spend**. Groupon should A/B test both - the 21-day spend gate is a lower friction bar for casual shoppers, the 90-day retention gate is a higher quality bar.

### 3.4 Chrome extension and iOS Safari extension are separate SKUs
[Data, High] The dedicated iOS Safari extension listing has no ratings aggregated. The main iOS app (4.9, 1.6M ratings) carries the review weight. **Groupon should bundle, not fragment** - one primary app with embedded Safari extension, not a standalone extension SKU.

### 3.5 Gift-card redemption is auth-gated on purpose
[Opinion, Medium-High] Cap One does not surface the retailer list on pre-auth pages. This is strategic: users commit an email + extension install before seeing what they can redeem into. That commitment tax is structural breakage insurance. Groupon should consider the same: do not show the redemption catalog until account is created.

### 3.6 Affiliate disclosure language has NOT been pushed to consumer-facing pages yet
[Opinion, High] Cap One's Privacy Policy (Feb 18 2026) and ToS (Nov 19 2025) do not contain post-settlement affiliate disclosure language. The ombudsman and compliance reviews are legal-side commitments. **Groupon can pre-empt this** by adding clean, consumer-facing affiliate disclosure language from day 1 - differentiation without regulatory pressure.

### 3.7 The iOS App Store "$10 in 21 days" rule is the interesting model
[Data, High] This is a PURCHASE-conditioned bonus, not a retention-conditioned one. It filters for actual shoppers, not bonus-install farmers. Groupon should consider this gate structure for Bucks activation, especially if Bucks needs to drive immediate order activity (not just installs).

---

## 4. Prompts / Queries Log (AI Funnel Appendix)

### 4.1 WebFetch prompts used
1. capitaloneshopping.com homepage - verbatim hero, value props, form fields, signup bonus mentions
2. /how-it-works - section headings, step-by-step, currency ratio (RESULT: 404)
3. /rewards, /gift-cards - retailer list, denominations (RESULT: both 404)
4. /help - FAQ titles, category headings
5. /our-terms/terms-of-service - commission language, referral eligibility, class action, effective date
6. /our-terms/privacy-policy - effective date, affiliate/attribution language, post-settlement disclosure
7. /our-terms/shopping-rewards-terms (RESULT: 404)
8. capitalone.com/learn-grow/money-management/capital-one-shopping/ - editorial explainer
9. Chrome Web Store listing (RESULT: 302 redirect to EU consent from CZ IP - DATA GAP)
10. App Store main iOS app (id1089294040) - rating, reviews, signup bonus
11. App Store Safari Extension (id1477110326) - rating, reviews, signup bonus
12. Doctor of Credit referral article - current bonus, historical list
13. Frequent Miler $80 article - terms verbatim
14. Thrifty Traveler Give-$80-Get-$80 - Mar 30 2026 update
15. Award Wallet - historical $40 reference

### 4.2 WebSearch queries used
1. `"Capital One Shopping $45 signup bonus 2026 terms conditions current"`
2. `"Capital One Shopping referral bonus current April 2026 $80 install"`
3. `"Capital One Shopping affiliate disclosure class action 2025 2026 terms update"`

### 4.3 Targeted sites hit
- capitaloneshopping.com (several subpaths)
- capitalone.com/learn-grow
- apps.apple.com (two listings)
- chromewebstore.google.com (blocked by consent redirect)
- doctorofcredit.com, frequentmiler.com, upgradedpoints.com, thriftytraveler.com, awardwallet.com
- influencermarketingclaims.com (via prnewswire)

---

## 5. Data Gaps

1. **$45 historical landing page:** Saint Augustine's article timed out on fetch. Could not verify whether the "$45 after $15 in 90 days" terms came from an actual Cap One Shopping landing page or from SEO content. **Recommendation:** Wayback Machine check of capitaloneshopping.com circa Dec 2023 to find the exact $45 offer page, if it ever existed as a headline rather than a YMMV targeted variant.

2. **Chrome Web Store numbers:** CZ IP blocks fetch. 6M+ user claim from the deep-dive doc remains uncited from a primary source in this capture. **Recommendation:** US-IP verification, or a direct screenshot from a US-based reviewer.

3. **Retailer list (~50 gift cards):** Behind account login. Cannot verify from pre-auth. The "50+ rotating retailers" claim in the deep-dive remains based on third-party sources (Frequent Miler).

4. **1 Credit = $1 statement:** No public Capital One Shopping marketing page states this verbatim. Confirmed only via third-party review content. The ToS states "minimum balance of $1.00 worth" of Rewards but does not define a "credit" unit.

5. **Post-settlement consumer-facing language:** No evidence Cap One has pushed settlement-related affiliate-disclosure language into the ToS (effective Nov 19 2025, pre-settlement) or Privacy Policy (effective Feb 18 2026, post-settlement but no explicit affiliate text). **Recommendation:** Re-check these documents Jun-Jul 2026 after the final hearing (Jun 10 2026) to see whether settlement terms force consumer-facing language changes.

6. **Current homepage screenshot:** WebFetch returned parsed markdown, not a visual capture. For the Groupon deck, a screenshot of the current pre-auth homepage is needed to show the absence of a dollar-bonus headline.

7. **Rankings:** Apple ranking "#2 Top Free Shopping" claim is not directly visible on the fetched App Store page - it's from earlier research cycles. Current ranking not independently verified.

8. **iOS $10 in 21 days bonus amount:** App Store description mentions the mechanic but does NOT disclose the dollar amount. DATA GAP on the specific dollar value of this variant.

---

## 6. Confidence Summary

| Finding | Confidence | Basis |
|---|---|---|
| $45 is NOT the current headline | High | Doctor of Credit, Frequent Miler, Thrifty Traveler all 2026 - consistent |
| $80/$80 is the current referral headline | High | Multiple Feb-Mar 2026 sources |
| 90-day install retention is the gate | High | ToS + third-party verified |
| ToS effective Nov 19 2025 | High | Direct fetch |
| Privacy Policy effective Feb 18 2026 | High | Direct fetch |
| iOS app 4.9 / 1.6M ratings | High | Direct fetch |
| Class action: $4M, Apr 17 2026 claim deadline, Jun 10 2026 hearing | High | Multiple legal sources |
| "1 Credit = $1" visible on public pages | Low - NOT VISIBLE on public pages, only third-party | DATA GAP |
| Retailer list on public pages | None - auth-gated | DATA GAP |
| Chrome Web Store 6M+ users | Unverified from this session (CZ IP blocked) | DATA GAP |

---

**END OF CAPTURE**
