# Honey - Public Page Capture (Pre-Auth Only)

**Fetched:** 2026-04-21 (from CZ IP, no account created, no signup completed)
**Researcher:** Claude / startup-competitors public-evidence pass
**Companion doc:** `raw/honey-mechanics-and-cautionary-tale.md` (forensic deep dive - this file adds pre-auth web evidence, not duplicates)
**Scope:** joinhoney.com, help.joinhoney.com, paypal.com Honey pages, App Store, Wikipedia, Chrome Web Store (partial - geo + 403). No authenticated content.

---

## 1. Summary

**Headline number:** Honey appears to still display "17 million members and counting" as a trust badge on joinhoney.com home and "141,786 Chrome Store reviews" with a five-star rating on the Honey Gold feature page. [Data - WebFetch joinhoney.com 2026-04-21, Confidence High for verbatim text] The 17M figure is marketing copy, not a live Chrome Web Store counter - the Chrome Web Store listing itself (chromewebstore.google.com/detail/...bmnlcjabgnpnenekpadlanbbkooimhnj) could not be fetched from a CZ IP (Google consent redirect + chrome-stats.com 403). Press tracking reported ~12M Chrome users at end of Dec 2025. [Data - 9to5Google Dec 31 2025, via Wikipedia] **Net: Honey's home page still shows a pre-scandal 17M number that is stale by ~5M users. This is itself a signal.**

**Current trust-posture summary:** Honey's public pages show **zero post-scandal accommodation**. There is no mention of the MegaLag expose, the class action, the Rakuten/Impact/Awin affiliate terminations, the "problematic code" PayPal admitted to disabling on Jan 12, 2026, or any "we have heard you, here is what we changed" language. The Terms of Use were last updated **January 16, 2024 (US)** and **February 16, 2024 (EU)** - ~2 years stale and predating the entire scandal. The affiliate-commission disclosure on the homepage is a single "Ad Disclosure" footer link plus a one-sentence mention on the Gold page: *"In some cases, we earn a commission when you buy items from partner stores. We share some earnings with you through Gold."* This is the minimum required compliance language. No transparency upgrades visible. [Data - WebFetch 2026-04-21, Confidence High]

**iOS Safari surfacing:** The PayPal app iOS Safari extension is the most strategically important Honey surface and the technical precedent Groupon wants to validate. The activation flow is described in PayPal's help article as: **"Once you have the latest version of the PayPal app, you can enable the PayPal Honey mobile Safari extension."** Only available for US iOS 15+ members. PayPal Rewards redemption is US-only; extension functionality covers 10 countries (US, CA, AU, UK, DE, FR, NL, IT, ES, IN). [Data - help.joinhoney.com + paypal.com/us/cshelp/help593, Confidence High] **No public step-by-step flow with screenshots was found on PayPal's or Honey's own pre-auth pages** - the detail lives in deeper help articles that require the app installed. This is itself a tell about how bundled/invisible the install is.

**Rebrand status:** The rebrand from "Honey Gold" to "PayPal Rewards" is live in the iOS app store copy (*"Big update! Honey Gold is now PayPal Rewards. That means more ways to earn and redeem, like spending points at checkout."*) and on the Business partner page (*"Incentivize passive shoppers to be active buyers with PayPal Rewards"*, *"Help cultivate shopper loyalty with PayPal's points-based program"*). But the consumer-facing /features/honeygold and /features/paypalrewards pages still use "Honey Gold" interchangeably with no migration banner. Dual naming in 2026 suggests the rebrand was announced Oct 2022 but consumer messaging has not converged. [Data, Confidence High]

---

## 2. Per-Page Findings

### 2.1 joinhoney.com (home)

- **URL:** https://www.joinhoney.com/
- **Fetched:** 2026-04-21
- **Confidence:** High (verbatim copy extracted)

**Hero headline:** *"Love deals? You came to the right place."*
**Sub hero:** *"The Honey extension automatically searches for coupons on 30,000+ sites around the globe."*
**Secondary headline:** *"A shopping tool that does all the work"*
**Tagline cluster:** *"Scroll for more ways to save. It's kind of our thing."*

**Value props (verbatim):**
- *"Add Honey to your computer in seconds and we'll search for coupons and rewards."*
- *"Apply coupons with a click"*
- *"We'll pop up at checkout to search for coupons. If we find working codes, we'll automatically apply one to your cart."*
- *"Earn gift cards just for shopping"*
- *"Score Gold Rewards on your eligible purchases at some of your favorite stores."*
- *"Honey + PayPal, at your service."*
- *"Two good things come together. Join millions of members who shop with confidence."*
- *"Why spend more? Add Honey now."*

**Trust signals:**
- *"141,786 Chrome Store reviews"* + five-star visual
- *"17 million members and counting"*
- *"Honey is now part of the PayPal family. Learn more here"*

**CTAs:** *"Add to Chrome"* (x2)

**Compliance microcopy:**
- Footnote 1: *"These deals are subject to availability, and third-party store terms, conditions, and exclusions may apply."*
- Footnote 2: *"Terms and exclusions apply."*
- Footer link: *"Ad Disclosure"*

**Structural observations:**
- No visible signup form on the home. CTA is extension-install, not account signup.
- No social sign-on buttons on home.
- No mention of the 2024 scandal, class action, MegaLag, affiliate-network terminations.
- No badges for Chrome Web Store policy compliance (March 2025 rule).
- "17M members" is a static number. 9to5Google's rolling Chrome user tracker had Honey at 12M-13M end of 2025. [Opinion: confidence High, the home page is not reflecting reality]

### 2.2 joinhoney.com/how-it-works

- **URL:** https://www.joinhoney.com/how-it-works
- **Fetched:** 2026-04-21
- **Status:** **404 Not Found**
- **Confidence:** High (direct HTTP error)

**DATA GAP:** The "how it works" page that existed in earlier Honey site audits is gone. The current flow is scattered across /features/honeygold, /features/droplist, help.joinhoney.com. No single public explainer URL. [Opinion: this is a post-scandal tell - consolidating "how we work" on one page is what Honey most needs to do but has not.]

### 2.3 joinhoney.com/features/honeygold

- **URL:** https://www.joinhoney.com/features/honeygold
- **Fetched:** 2026-04-21
- **Confidence:** High

**Headline:** *"Earn gift cards just for shopping"*

**How it works (verbatim 3-step):**
1. *"Join Honey. First, create a Honey account. It's fast, easy, and free."*
2. *"Shop like normal. We'll let you know if there's a chance to earn Gold."*
3. *"Once you earn enough Gold, redeem it for a store gift card."*

**Supporting copy:**
- *"The more you shop, the more you earn."*
- *"We don't just look for coupons. We have our own rewards program too."*
- *"We'll let you know if Honey Gold is available when you shop at different stores."*
- *"Gold adds up fast"*
- *"We're always adding more stores with Gold."*
- *"Look for ways to earn extra Gold with exclusive offers."*
- *"Earn Gold, redeem, repeat."*

**Eligibility disclaimer (repeated):** *"Certain items, product categories, and purchases are ineligible for Honey Gold... We won't be able to determine if items are eligible until after purchase. Final amount awarded displays in your account."*

**The only transparency disclosure on the entire page:** *"In some cases, we earn a commission when you buy items from partner stores. We share some earnings with you through Gold."*

**Notable omissions:** No 1000 pts = $10 ratio shown. No minimum-redemption threshold. No pending-window. No expiration terms. All material economics are buried in the Terms or the gift-card help article. [Opinion: this is designed for breakage.]

### 2.4 joinhoney.com/terms (EU/UK) and /terms/us

- **EU/UK Terms URL:** https://www.joinhoney.com/terms
- **US Terms URL:** https://www.joinhoney.com/terms/us
- **Fetched:** 2026-04-21
- **Confidence:** High (verbatim quotes extracted)

**EU/UK last updated:** *"Last updated February 16, 2024"*
**US last updated:** *"Last updated January 16, 2024"*

**Revenue model language (EU):** *"Honey does not charge fees to you for its Service. We make money to sustain the Service when you purchase or engage with these offers."*
**Tracking language (EU):** *"Honey may track how you use the services we provide, including whether you click-on Honey links to third-party websites, your actions on those third-party merchant websites, and whether you use the discount or coupon codes displayed by Honey."*
**Revenue model (US):** *"We make money to sustain the Service when you purchase or engage with these offers."*
**Tracking (US):** *"To improve our services, PayPal may track how you use the services we provide, including whether you click on PayPal links to third-party websites, your actions on those third-party merchant websites, and whether you use the discount or coupon codes displayed by PayPal."*

**Honey Gold / PayPal Rewards - property disclaimer (EU):** *"Honey Gold loyalty rewards points cannot be purchased, are not your property, are not money, can expire as described below, and have no value prior to redemption."*
**US version:** *"Points are not money and have no value prior to redemption. Points can only be earned on eligible purchases."*

**365-day forfeiture (EU):** *"To maintain your Honey Gold loyalty rewards points, you must have an Active Account and earn at least 10 Honey Gold loyalty rewards points during each consecutive 365 day period."*
**US:** *"Points can expire. To prevent expiration, you must have an active account and earn at least 10 points during each consecutive 365-day period (for example, from April 10th of this year to April 10th of next year)."*

**Account-closure forfeiture (EU):** *"If your Honey account is closed for any reason, you will no longer be able to redeem any Honey Gold loyalty rewards points."*

**Arbitration + class action waiver (US, verbatim, all caps in original):**
*"THIS AGREEMENT CONTAINS (1) AN ARBITRATION PROVISION; (2) A WAIVER OF RIGHTS TO BRING A CLASS ACTION LAWSUIT AGAINST US; AND (3) A RELEASE BY YOU OF CLAIMS FOR DAMAGE AGAINST US THAT MAY ARISE OUT OF YOUR USE OF THE SERVICE, TO THE GREATEST EXTENT PERMITTED BY APPLICABLE LAW."*

Section header: *"ARBITRATION CLAUSE & CLASS ACTION WAIVER - IMPORTANT - PLEASE REVIEW AS THIS AFFECTS YOUR LEGAL RIGHTS"*

30-day opt-out clause: users may *"opt out of this ARBITRATION CLAUSE & CLASS ACTION WAIVER by sending an email to privacy@joinhoney.com within thirty (30) days of the first date you access or use the Service."*

**Post-March-2025 Chrome Web Store policy compliance language:** None found in either US or EU terms. [Confidence High - both versions stale from before the policy change]

**Scandal / legacy-code / class-action reference:** None. [Confidence High]

**Private-code / user-entered-code scraping language:** None. [Confidence High - the Terms still contain no language either forbidding or disclosing the practice MegaLag Part 2 exposed]

**Structural observation:** US Terms contain a **class action waiver** - directly relevant to the live In Re PayPal Honey litigation. Plaintiffs in that case are creators, not consumers, so the waiver does not block the current suit, but any future consumer plaintiff who signed up after Jan 16 2024 has a harder path. [Opinion, Confidence Medium]

### 2.5 help.joinhoney.com/article/350 (Honey Mobile Safari Extension)

- **URL:** https://help.joinhoney.com/article/350-honey-mobile-safari-extension
- **Fetched:** 2026-04-21
- **Confidence:** High

**Activation copy:** *"Once you have the latest version of our app, users will also be able to enable the Honey extension on Safari."*

**Supported countries (verbatim list):** *"US, CA, AU, UK, DE, FR, NL, IT, ES, and IN members"*

**iOS requirement:** *"iOS15 installed"*

**PayPal Rewards scope:** *"PayPal Rewards is also currently limited to US members only."*

**Functionality:** Will *"automatically look for coupons and PayPal Rewards points when you shop on your phone."*

**Contact:** *"Still have questions? Reach out to us at yourfriends@joinhoney.com."*

**Critical absence:** No step-by-step numbered activation flow, no disable/uninstall instructions, no privacy/permission disclosures. User is handed off to the PayPal app for everything.

### 2.6 paypal.com/us/cshelp/help593 (PayPal Honey Mobile Safari Extension)

- **URL:** https://www.paypal.com/us/cshelp/article/what-is-the-paypal-honey-mobile-safari-extension-help593
- **Fetched:** 2026-04-21
- **Confidence:** High

*"Once you have the latest version of the PayPal app, you can enable the PayPal Honey mobile Safari extension."*

*"PayPal Honey will automatically look for coupons to earn cash back by racking up Gold points with eligible stores and products or with ExclusiveOffers and double the points on double cash back offers when you shop on your phone."*

*"The PayPal Honey mobile Safari extension is only available for US members with iOS15 installed."*

*"It isn't available everywhere yet; we're adding new regions as quickly as possible. Check back often to see if it's available in your country."*

*"Currently, Android doesn't support browser extensions on Chrome. We hope to be able to bring our extension to Android in the future once Google makes this possible."*

**Structural:** The page uses "Gold points" language (not "PayPal Rewards points") - internal inconsistency with the rebrand. [Opinion Confidence High]

### 2.7 App Store - PayPal Honey: Coupons, Rewards

- **URL:** https://apps.apple.com/us/app/paypal-honey-coupons-rewards/id1358499588
- **Fetched:** 2026-04-21
- **Confidence:** High for top-level data; Medium for review sentiment

**Title:** *"PayPal Honey: Coupons, Rewards App"*
**Subtitle:** *"Shopping, Deals, Discounts"*
**Rating:** **3.6 / 5, 10K ratings** [Data - WebFetch 2026-04-21]
**Version:** 4.4.0, dated January 27
**Developer:** *"Honey (Honey Science Corporation)"* (not "PayPal, Inc." - Honey's original LLC still listed)
**Size:** 413.2 MB
**Age:** 4+

**What's new (verbatim):** *"Big update! Honey Gold is now PayPal Rewards. That means more ways to earn and redeem, like spending points at checkout."*

**Description excerpt (verbatim):** *"PayPal Honey, the #1 shopping tool in America*, now has even more ways to save time and money. From coupons to cash back**, get the best of Honey right on your mobile device...Download Honey."*

**Privacy practices:** App collects purchase history, email, browsing history, location, user IDs, search history - all linked to user identity, used for advertising, analytics, personalization, app functionality.

**Notable negative review surfaced:** October 2023 review alleges *"all my points were gone from my account"*; user claims account terminated under *"high risk"* label without explanation. This exact pattern shows up repeatedly in PayPal community + MoneySavingExpert threads (forensic doc section 3).

**Cross-check:** The prior forensic doc quoted *"4.8/5 on 2,400+ reviews"*. The live current data is **3.6/5 on 10K+ ratings** - substantially worse than what was cited in the deep dive. This is the clearest quantitative trust-trend data point available on public pages. [Data - delta confidence High, the 2025 figure was likely accurate at time; the 2026 figure is today. Net: ~1.2 star drop and 4x review volume over ~1 year, mostly negative.]

### 2.8 Chrome Web Store - Honey extension listing

- **URL:** https://chromewebstore.google.com/detail/paypal-honey-automatic-co/bmnlcjabgnpnenekpadlanbbkooimhnj
- **Fetched:** 2026-04-21
- **Status:** **DATA GAP - could not fetch from CZ IP.** Google consent redirect blocked WebFetch. chrome-stats.com mirror returned HTTP 403.
- **Confidence:** Medium (figures triangulated from press, not direct capture)

Best available cross-reference (9to5Google tracker via Wikipedia, last updated April 20 2026):
- End of Dec 2025: ~12M users (down 8M from 20M peak)
- 9to5Google Jan 17 2025 reported a **temporary regrowth to 18M** between mid-Jan and mid-Jan 2025 before the downtrend resumed. [Data]
- **No April 2026 refresh available.** [Data gap - flag for manual US-IP capture]

Secondary source (gHacks/Hellotech/FinanceBuzz review aggregators) cite *"4.8 out of 5, 150,000+ reviews"* for the Chrome listing - but this is 2025 data, not live 2026. [Confidence Medium - likely directionally correct but not verifiable today from CZ]

The extension name in the URL slug has been updated to *"paypal-honey-automatic-co"* - i.e. the public-facing name is **"PayPal Honey: Automated Coupons & Cash Back"**, no longer just "Honey". This is a post-acquisition rebrand that is live on the store listing. [Data]

### 2.9 joinhoney.com/business (merchant / partner page)

- **URL:** https://www.joinhoney.com/business
- **Fetched:** 2026-04-21
- **Confidence:** High

**Headline:** *"Honey incentivizes loyal shoppers every day"*

**Merchant value props:**
- *"Partners experience an efficient way to attract buyers, from discovery to checkout"*
- *"Incentivize passive shoppers to be active buyers with PayPal Rewards"*
- *"Help drive engagement and influence purchase behavior"* (Droplist)
- *"Help cultivate shopper loyalty with PayPal's points-based program at the point-of-purchase"* (Rewards)
- *"Help reduce cart abandonment with our patented browser extension"* (Savings Finder)

**Language about Rakuten/Impact/Awin terminations:** **None.** [Confidence High]
**Language about the scandal or class action:** **None.** [Confidence High]
**Attribution transparency:** **None.** [Confidence High]

**Footer:** *"© 2026 PayPal, Inc."* (copyright updated) + *"Ad Disclosure"* link.

**Structural observation:** The merchant-facing pitch still reads as if the affiliate network is intact and the brand is pristine. A merchant reading this page in April 2026 would have zero signal that three major affiliate networks terminated or suspended Honey's access Jan 12-21 2026. This is **reputation recovery PR by omission, not by engagement**. [Opinion, Confidence High]

### 2.10 help.joinhoney.com/article/39 (What is the Honey extension)

- **URL:** https://help.joinhoney.com/article/39-what-is-the-honey-extension-and-how-do-i-get-it
- **Fetched:** 2026-04-21
- **Confidence:** High

*"PayPal Honey is a free browser extension that searches for deals on the internet."*
*"With one click Honey automatically searches for and tests available coupon codes at checkout on 30,000+ popular sites."*
*"Honey works on 30,000+ top stores like Macy's, J. Crew, Lowe's, Adidas, Stubhub, Ulta, Sephora, GameStop, Nike, Target, and Pizza Hut."*
Install options listed: Chrome, Firefox, Safari, Opera, Edge.
*"For US users, you can redeem your points at PayPal checkout by connecting your Honey and PayPal accounts."*

**Note:** The public count claimed is **30,000+ stores**. MegaLag Part 2 (Dec 2025) showed Honey actually had codes for 181,000 stores, of which only ~35,000 had affiliate agreements. So the public "30,000+" figure is approximately the *paid* affiliate set and has stayed stable. [Opinion, Confidence Medium - the brand is implicitly aligning "stores we work with" with "stores we have affiliate deals with", which is the defensive re-scoping the Chrome Web Store policy change forced.]

### 2.11 joinhoney.com/signup, /how-it-works, /features, /how-honey-works

- **Status:** All four URLs return **404 Not Found** as of 2026-04-21.
- **Confidence:** High

**DATA GAP:** Honey has no public /signup page. Signup appears to be triggered inline at extension install + email submission, not via a dedicated pre-auth URL. Form fields and social sign-on options cannot be captured from pre-auth pages. The iOS route bypasses the signup flow entirely by tying Honey identity to PayPal identity. [Opinion Confidence High]

### 2.12 joinhoney.com/privacy

- **Status:** Page returned essentially empty content to WebFetch (single word "Honey"). Likely blocks headless agents.
- **Confidence:** Low (page exists but content not captured)

**DATA GAP:** Could not extract privacy policy verbatim. Forensic doc cites the general collection categories (IP, cookies, web beacons, pixel tags). Post-scandal transparency updates, if any, not verified.

---

## 3. Inferences for Groupon

### 3.1 iOS Safari bundling - the technical precedent

Honey's public pages confirm the bundling pattern is **architecturally simple** and **messaged lightly**:

- The Honey iOS Safari extension ships inside the PayPal iOS app binary (413 MB app, consistent with bundled extension).
- Activation requires: latest PayPal app + iOS 15+ + explicit user "enable" action in Safari settings.
- PayPal's own help article describes the enable step in a single sentence. There is no detailed in-app walkthrough on pre-auth public pages.
- The extension cannot be uninstalled independently of the PayPal app (separately confirmed via forensic doc - not contradicted by anything on public pages).
- Country breadth: 10 countries for the extension, US-only for Rewards redemption. [Confirmed from help.joinhoney.com verbatim.]

**Groupon implication (Confidence High):** The Honey/PayPal pattern is viable as a reference architecture. **Specifically**:
- Groupon iOS app can ship a Groupon Safari Web Extension as a bundled component.
- Activation decoupled from install: user installs Groupon for normal reasons, then activates extension from a "Deals" tab prompt.
- Geography: if Groupon's loyalty/rewards redemption is US-only at launch but the extension itself works in ~10 countries, that matches Honey's live rollout and is acceptable to Apple.
- The technical precedent does not require EU/DMA concessions that would block the pattern in Groupon's key markets.

**What NOT to copy on the bundling:** Honey's "cannot uninstall extension without uninstalling PayPal wallet" is specifically what heise.de and Apple Community forums flag as a dark pattern. Groupon should ship the extension as bundled-but-independently-removable. This is the one material deviation from Honey that keeps the pattern defensible.

### 3.2 What Honey's "post-scandal messaging" tells Groupon

**The clearest public-pages finding: Honey has chosen silence over explanation.**

No post-scandal accommodation is visible anywhere on joinhoney.com, help.joinhoney.com, or the PayPal help pages we captured. Specifically:
- Terms of Use last updated January/February 2024 (pre-scandal) - still live in April 2026.
- No transparency banner, no "how Honey earns" disclosure upgrade, no mention of the Chrome Web Store March 2025 policy change or what Honey did to comply.
- Merchant-facing page implies an intact affiliate network 3+ months after Rakuten/Impact/Awin terminations.
- Home page still displays "17M members" - stale by ~5M.
- "how it works" page is 404.

This is a **reputation-recovery strategy via attrition**: wait for the news cycle to move on, let the Chrome Web Store counter attrition out, keep the PayPal iOS bundle churning silently in the background. No proactive "we heard you" messaging.

**Groupon implication (Confidence High):** This is the NEGATIVE precedent. If Groupon's extension ever has a trust shock, the playbook MUST be the opposite:
- Timestamp a public "what changed" page within 48 hours of any material change.
- Put the attribution model on the home page above the fold, not buried as a footer "Ad Disclosure".
- Update Terms within 30 days of any mechanic change, with diff visible.
- Publish a merchant-facing compliance page showing which affiliate networks Groupon operates within and what the user-positive test is.

### 3.3 What to copy from the public-facing shape

- **Mobile-first help routing:** PayPal's help593 article is short, single-paragraph, points to the app. This pattern works. Groupon should not over-document the extension on public pages - let the app carry the walkthrough.
- **Country list transparency:** Honey's "US, CA, AU, UK, DE, FR, NL, IT, ES, IN" list for the extension and separate "US-only" list for Rewards redemption is the right shape. Groupon should mirror: extension available list is broader than redemption-live list.
- **Install-CTA as primary homepage action:** Honey home has "Add to Chrome" as the dominant CTA, not "Sign Up". That is the right funnel - install-first, account-later. Groupon's loyalty extension should follow the same pattern.

### 3.4 What to explicitly NOT copy

- **Stale user-count hero badges.** The "17M members and counting" claim on joinhoney.com in 2026 is marketing debt accumulating interest. Groupon should expose a live number or no number.
- **Transparency by omission.** Single "Ad Disclosure" footer link is not sufficient. Post-MegaLag, every cashback/coupon extension is under public scrutiny on attribution. Groupon should disclose attribution prominently at checkout popup and on home.
- **Ambiguous rebrand.** Honey still shows "Honey Gold" and "PayPal Rewards" interchangeably 3+ years post-announcement. If Groupon rebrands a points program, complete the migration in one wave.
- **Class action waiver + arbitration clause hidden in all-caps.** US legal tradecraft, but it's citation-bait in court filings and sends a defensive-posture signal. Groupon should write enforceable dispute-resolution language in plain prose.
- **Point economics buried.** The fact that 1000 pts = $10, minimum redemption is $10, pending is 60-90 days, and 365-day inactivity forfeits the balance is NOT disclosed on /features/honeygold. It is only in the Terms. Groupon should publish point economics on the consumer-facing feature page, above the fold.

---

## 4. Prompts / Queries Log (for AI funnel appendix)

### WebFetch prompts (all from 2026-04-21 CZ IP)

1. **joinhoney.com/** - "Extract ALL visible copy verbatim from this landing page. I need: the main headline/hero copy, subheadlines, value propositions, trust signals (user counts, review counts, press logos, ratings), CTAs (exact button text)..."
2. **joinhoney.com/how-it-works** - "Extract ALL visible copy verbatim. I need every step of the how it works flow, any descriptions of Honey Gold, any mention of PayPal Rewards migration, any transparency/attribution disclosures..."
3. **joinhoney.com/features/honeygold** - "Extract verbatim ALL visible copy on this Honey Gold feature page..."
4. **joinhoney.com/terms** (EU) - "Extract verbatim the key sections of these terms, especially: (1) any language about affiliate commissions..."
5. **paypal.com/us/cshelp/article/...help593** - "Extract verbatim all visible copy on this PayPal help page describing the PayPal Honey mobile Safari extension..."
6. **joinhoney.com/terms/us** - "Extract verbatim the key sections of these US Honey Terms of Use..."
7. **chromewebstore.google.com/detail/...bmnlcjabgnpnenekpadlanbbkooimhnj** - "Extract verbatim from the Chrome Web Store listing for Honey..." (blocked by consent redirect)
8. **apps.apple.com/us/app/paypal-honey-coupons-rewards/id1358499588** - "Extract verbatim from the App Store listing..."
9. **joinhoney.com/privacy** - (blocked - returned single word)
10. **help.joinhoney.com/article/350-honey-mobile-safari-extension** - "Extract verbatim all visible copy..."
11. **help.joinhoney.com/article/85-redeem-paypal-rewards-for-gift-cards** - "Extract verbatim..."
12. **paypal.com/us/digital-wallet/ways-to-pay/rewards** - (404)
13. **paypalobjects.com/marketing/ua/pdf/US/en/pp-gold-program-tnc.pdf** - (PDF, extraction failed on compressed streams)
14. **joinhoney.com/how-honey-works** - (404)
15. **help.joinhoney.com/article/39-what-is-the-honey-extension-and-how-do-i-get-it** - "Extract verbatim the full article..."
16. **joinhoney.com/features** - (404)
17. **joinhoney.com/signup** - (404)
18. **joinhoney.com/business** - "Extract verbatim all visible copy on this Honey for Business / merchant partner page..."
19. **joinhoney.com/features/paypalrewards** - "Extract verbatim all copy on this PayPal Rewards feature page..."
20. **chrome-stats.com/d/bmnlcjabgnpnenekpadlanbbkooimhnj** - (403 blocked)
21. **en.wikipedia.org/wiki/PayPal_Honey** - "Extract latest data on: (1) current Chrome Web Store user count..."
22. **help.joinhoney.com/article/83-how-can-i-earn-honey-gold** - (404)

### WebSearch queries

1. *"Honey Chrome Web Store users April 2026 current count rating"*
2. *"Honey Chrome Web Store extension rating reviews 2026 bmnlcjabgnpnenekpadlanbbkooimhnj"*
3. *"PayPal Honey" iOS app rating reviews 2026 "id1358499588"*
4. *"Honey Gold is now PayPal Rewards" 2025 2026 announcement migration*
5. *Honey merchant page "join our network" advertisers affiliate joinhoney 2026*

---

## 5. Data Gaps

1. **Live Chrome Web Store user count as of April 2026** - could not fetch the Chrome Web Store listing from CZ IP. Consent redirect + chrome-stats.com 403. Requires either US IP capture or PayPal Q1 2026 earnings disclosure (next release late April 2026). Best-available: ~12M at end of Dec 2025 per 9to5Google tracker.
2. **Live Chrome Web Store rating + review count** - same blockage. 2025 press cites "4.8 stars, ~150K reviews" but that is not verifiable today. iOS App Store has dropped to **3.6 / 10K ratings** which is a leading indicator.
3. **Signup flow field inventory** - /signup URL returns 404. Signup flow appears to be email-inline at install and not a dedicated pre-auth page. Social sign-on options cannot be confirmed from pre-auth.
4. **Privacy policy verbatim** - page blocks WebFetch. Post-scandal updates (if any) not confirmed.
5. **PayPal Rewards T&Cs PDF** - compressed stream PDF, extraction failed. Verbatim "1000 pts = $10", minimum-redemption, and expiration language not confirmed from the program T&Cs document itself. Text is cited in the forensic doc via secondary help.joinhoney.com articles but not from the primary T&Cs source.
6. **iOS Safari extension activation step-by-step** - neither PayPal nor Honey publish a numbered walkthrough on pre-auth pages. Likely intentional (the flow is in-app).
7. **Current affiliate network status on Honey-owned pages** - /business page is silent on Jan 2026 terminations by Rakuten, Impact.com, Awin. Would need to compare against archive.org snapshots to confirm no quiet edits, but snapshot diffing is out of scope for this pass.

---

## Appendix A: Confidence Matrix

| Claim | Source | Confidence |
|---|---|---|
| "17 million members and counting" on homepage | Direct WebFetch 2026-04-21 | High |
| "141,786 Chrome Store reviews" on Honey Gold page | Direct WebFetch 2026-04-21 | High |
| iOS App Store rating 3.6/5 on 10K ratings | Direct WebFetch App Store 2026-04-21 | High |
| Chrome Web Store current user count ~12M | 9to5Google tracker via Wikipedia, end Dec 2025 | Medium (stale 4 months) |
| Terms last updated Jan/Feb 2024 | Direct WebFetch 2026-04-21 | High |
| No post-scandal transparency content on public pages | Exhaustive pre-auth capture | High |
| /how-it-works, /signup, /features, /how-honey-works all 404 | Direct HTTP errors 2026-04-21 | High |
| 10-country extension availability | help.joinhoney.com/article/350 verbatim | High |
| Honey Gold -> PayPal Rewards rebrand live in App Store copy | App Store "what's new" 2026-04-21 | High |
| /business page omits Rakuten/Impact/Awin terminations | Direct WebFetch 2026-04-21 | High |
| Class action waiver + arbitration clause in US Terms verbatim | Direct WebFetch 2026-04-21 | High |
| 1000 pts = $10 conversion | Forensic doc only (not verified from public pages today) | Medium |

---

*End of public-capture.md. Companion forensic doc at `../honey-mechanics-and-cautionary-tale.md` for mechanics, trust-collapse chronology, and class-action detail.*
