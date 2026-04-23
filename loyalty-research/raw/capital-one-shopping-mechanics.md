# Capital One Shopping - Loyalty Mechanics Teardown
*Source: startup-competitors / Cap One deep dive | 2026-04-21*

---

## 1. TL;DR

Capital One Shopping (acquired as Wikibuy in Nov 2018 for undisclosed amount, ~$2M users at acquisition [Data, High confidence, CNBC 2018-11-20]) is a browser-extension-plus-mobile-app hybrid that automates coupon application, price comparison, and affiliate-rewards capture across 100,000+ retailers. It reports 6-10M+ active users in 2025-2026 and ranks #2 in the US App Store "Top Free Apps" category (Shopping). [Data, Medium-High: company-reported on capitaloneshopping.com, Apple Community July 2025]

**Core mechanic**: Users earn "Capital One Shopping Rewards" (1 credit = $1, a soft currency). These can ONLY be redeemed for digital gift cards at 50+ rotating retailers (no cash-out, no statement credit, no bank-account deposit). This is the exact "soft currency / non-real-cash" model Groupon is evaluating for "Bucks". [Data, High: Capital One help center + multiple reviews]

**Monetization**: Affiliate commissions (Cap One keeps the spread above what it returns as credits) + first-party shopping data fed to Rakuten Advertising's Audience Engine for credit-card customer acquisition targeting. Cap One explicitly states they "don't sell" user data but leverage it for their own credit-card funnel. [Data, High: Rakuten case study + press]

**The $45 bonus is REAL but not fixed at $45.** The signup/referral offer has fluctuated wildly from $10 (2020) -> $200 (Dec 2023 peak, lasted days) -> $40-$80 (2024-2026 norm). A specific "$45 after $15 purchase in 90 days" offer was documented on PhatWallet forums; the current (Feb-April 2026) headline is $80/$80 referral with a 90-day-install retention requirement. Offers are heavily targeted (YMMV) and US-only. [Data, High: Doctor of Credit, Frequent Miler, PhatWallet]

**Load-bearing caveat for Groupon**: Dusan's $45 LTV anchor is defensible as an order of magnitude but should be framed as "$40-$80 acquisition incentive, tied to 90-day retention, US-only, YMMV/targeted" - not a flat bounty. The *90-day retention requirement* is the more interesting LTV signal than the dollar amount.

**Biggest weakness**: Trustpilot 1.3/5 (305 reviews) vs App Store 4.9/5 (960K+). The gap is reward-tracking failures, gift-card-only redemption friction, and an active $4M class-action settlement (Dec 2025 preliminary approval) alleging Cap One's extension *silently overwrites competing affiliate cookies* to steal commissions. [Data, High: ABA Banking Journal, classaction.org]

---

## 2. The Mechanics (20-point list)

### 2.1 Signup flow [Estimate, Medium confidence - based on reviews + help center]
- Email + password (no phone required at signup)
- Install browser extension with "full permissions" (required to earn)
- Mobile signup also available (iOS, Android)
- No Capital One banking or credit card required - truly standalone

### 2.2 The $40-$80 install incentive [Data, High]
- Current (Apr 2026) headline: $80 for referrer + $80 for new user
- Condition: Install within 7 days, keep installed + active for 90 days, US-resident, never had an account before
- Historical range: $10 (2020) -> $40 -> $75 -> $200 (Dec 2023 peak) -> $40-80 (2024-26)
- A specific "$15 purchase in 90 days -> $45" variant has been documented
- Targeting: YMMV - many users cannot access any referral bonus
- Cap: $1,900 total referrals per referrer (was $500)

### 2.3 Onboarding email cadence [DATA GAP]
- Cap One does not publish; no leaked cadence found
- Has a "Mobile Extension Onboarding" page at capitaloneshopping.com/mobile-extension/onboarding but content not scraped
- Reasonable assumption: Welcome email + feature-education drip + price-drop alerts based on watchlist + monthly "$X available to redeem" nudge [Assumption, Low]

### 2.4 Push notification strategy [Estimate, Medium]
- Price-drop alerts on watchlist items
- Coupon-available alerts on retailer visits
- Rewards-posted confirmations
- Users report notifications can be aggressive; some complain in Chrome Community threads about "popping up"

### 2.5 Shopping Credits - the soft currency [Data, High]
- 1 credit = $1 USD (1:1, no obfuscation)
- Earn rate: variable by merchant, typically 1-10%, offer-based (NOT flat percentage like Rakuten)
- Some reward offers go much higher (45% at Sixt car rental documented; 30% at Klook)

### 2.6 Redemption [Data, High]
- Gift-card-only. No cash. No bank deposit. No statement credit.
- 50+ retailers, but the list *rotates frequently* - a known pain point
- Recent removals: Lowe's, Home Depot, Macy's, Walmart, Safeway (at various times)
- Currently available (Feb 2026): Marriott Bonvoy, eBay, Uber/Uber Eats, Petco, Groupon, Zappos, Nike, Kohl's
- Variable by user (personalized/rationed redemption inventory)
- Processing: up to 3 business days for gift card to appear

### 2.7 Loyalty tiering [Data, High]
- No paid tier. No Cap One banking tie-in required.
- No VIP/status levels. Flat rewards for everyone.
- This is STRATEGIC - keeps it a standalone acquisition funnel for Cap One's actual revenue product (credit cards)

### 2.8 Price comparison - "watch for lower price" [Data, High]
- Active differentiator vs Honey. On Amazon product pages, extension alerts "this is $15 cheaper at Walmart"
- "Universal credit" - even when no coupon/reward exists, finds cross-retailer price gaps
- This is the Wikibuy original core feature (Walt Coon, 2014)

### 2.9 Coupon auto-apply rate vs Honey [Data, Medium]
- Cap One: 100,000+ retailers
- Honey: ~40,000 retailers
- Cap One claims faster code-testing at checkout (<30s)
- Honey shows 120-day price history; Cap One does not

### 2.10 Price drop alerts / watchlist [Data, High]
- Add-to-watchlist on retailer product pages
- Email + push when price drops
- Limited to participating retailers (not universal)

### 2.11 Merchant economics [Estimate, Medium]
- Operates as affiliate (last-click attribution via extension cookie injection)
- Avg commission: ~6% [Estimate, from affiliate-program reviews]
- Cap One keeps spread between commission and user rebate
- Merchant-side: no direct contract needed - operates through Rakuten/CJ/Impact/Partnerize networks

### 2.12 Traffic sources (SimilarWeb, Mar 2026) [Data, High]
- 66.7M monthly visits to capitaloneshopping.com (+58% MoM)
- 81.76% direct traffic (brand-strong)
- 97.21% US, 1.02% Canada, 0.93% UK
- Female-skew: 60.56% female, 39.44% male
- Largest demo: 25-34
- Bounce: 42.59%, Pages/visit: 1.88, Avg duration: 1:20
- Ranked #2 in Coupons & Rebates category

### 2.13 Acquisition channels [Data, Medium]
- Capital One credit-card app and .com cross-sell (9.68% of capitalone.com outbound desktop traffic goes to capitaloneshopping.com)
- Organic/direct dominant (brand recognition)
- Influencer/affiliate referrals (ironically - see class action)
- App Store ranking (#2 Top Free Shopping - organic discovery)

### 2.14 12-month user trajectory [DATA GAP]
- Cap One does not publish MAU/DAU
- Chrome Web Store: 6M+ users, 10K+ reviews
- App Store: 960K+ reviews at 4.9
- Similarweb Android app stats exist but specific trajectory not scraped this round

### 2.15 App Store 4.9 / 960K reviews - genuine? [Opinion, Medium]
- Most likely a mix: genuine high satisfaction for users who DO successfully redeem + in-app review prompts timed at "rewards-posted" dopamine peak + survivorship bias (users with tracking failures uninstall and don't leave App Store reviews because the app-side still works)
- Contrast with Trustpilot 1.3/5 (305 reviews) - this is where power-users with tracking complaints congregate
- The 4.9 is directionally real but upward-biased by prompt timing

### 2.16 Team size signal [DATA GAP, Low confidence]
- Capital One has 4,000+ open roles and 327 engineering jobs across the company
- Capital One Shopping specifically is hiring PMs and engineers in Austin (the Wikibuy origin city)
- No headcount disclosed. Active investment, not maintenance-mode. [Opinion, Medium]

### 2.17 Safari extension - iOS [Data, High]
- Ranked #2 on iOS App Store "Top Free" (Shopping category) per Apple Community July 2025
- Requires iOS 13+
- Activation flow: Install app -> Settings > Safari > Extensions > Capital One Shopping > Allow Extension -> per-site permission via "AA" menu
- Per-site activation is friction - users report having to re-enable on new sites
- This is the flow Groupon should study most closely for iOS ecosystem play

### 2.18 Commission loss or break-even? [Opinion, Medium]
- Almost certainly break-even or small loss on rewards P&L in isolation
- Makes up the difference via Cap One credit-card cross-sell conversion value (the real product)
- The class-action settlement ($4M for affiliate-hijacking) suggests aggressive revenue capture

### 2.19 How is Cap One monetizing this? [Data, High]
- Primary: Affiliate commissions (pay-per-sale via Rakuten/CJ/Impact networks)
- Secondary: First-party shopping data -> Rakuten Audience Engine for Cap One's own credit-card marketing targeting
- Tertiary: Brand-halo for Cap One financial products + acquisition-funnel for checking/savings
- NOT selling user data externally (per Cap One statements)

### 2.20 Key differentiator vs Rakuten and Honey [Data, High]
- vs Honey: 2.5x more retailers, price-comparison across retailers (Honey does intra-retailer price history only), gift-card-only (Honey has PayPal cash-out)
- vs Rakuten: Automated checkout flow (Rakuten requires clicking through portal), price comparison feature, but Rakuten has BIGGER cashback percentages on average ($312/yr Rakuten vs $94/yr Cap One Shopping per one comparison source)

### 2.21 Key WEAKNESS (user complaints, aggressive) [Data, High]
- Reward tracking failures with no recourse (multiple $100-$1,500 disputes documented)
- Support script: "wait 30-90 days" / "reached point where customer service can't proceed"
- Gift-card redemption inventory rotates and shrinks (users report best options disappear fast)
- Phone-number conflict bug prevents redemption (multiple reports)
- Class-action settlement Dec 2025 for affiliate-cookie hijacking ($4M)
- Trustpilot 1.3/5 rating

---

## 3. The $45 Bonus - What It Is, What It Means for LTV

### What the $45 bonus actually is [Data, High]
- A time-bound, heavily-targeted, US-only acquisition offer
- Historical offer was "$45 bonus after $15 qualifying purchase within 90 days of install"
- Current (2026) analogue: $80/$80 referral (both sides), with a 90-day install-retention requirement (no purchase needed on the latest variant)

### Mechanical breakdown
| Dimension | Detail | Confidence |
|---|---|---|
| Trigger | Install extension + maintain for 90 days OR make $15+ purchase | [Data, High] |
| Cohort | New users only (never had account) | [Data, High] |
| Geography | US-only | [Data, High] |
| Time window | 7 days to install after referral, 90 days to complete | [Data, High] |
| Payout form | Capital One Shopping Rewards (gift-card-only) | [Data, High] |
| Cap | $1,900 total for referrer (was $500) | [Data, High] |
| Targeting | YMMV - many existing users cannot generate referral links | [Data, High] |

### What this means for LTV [Opinion, Medium-High]
The $45-80 payment is *not* a signal of per-user monetization inside Cap One Shopping. It is a customer-acquisition cost for the PARENT entity (Capital One Financial Corp) that can underwrite this CAC because:
1. Cross-sell to credit cards / banking - where real LTV is $500+
2. First-party shopping behavioral data for underwriting and marketing
3. Competitive blocking vs Honey/Rakuten (keep consumers out of PayPal's funnel)

**For Groupon's sizing model**: The $45 anchor is defensible as an order of magnitude for an incentive required to get a high-friction install (Safari extension, browser permission grant, 90-day retention). But it is NOT the LTV of the user - it is the *acquisition bribe*. Groupon's equivalent CAC tolerance depends on whether it has an analogous downstream revenue product (Groupon+ membership? Credit-card partnership? Merchant-bundled loyalty?) to cross-sell into.

If Groupon cannot monetize installed users via downstream cross-sell, $45 per install is a straight subsidy with ~$5-15/yr (at ~6% affiliate commission on a $8-25 avg monthly order value) payback - a multi-year payback even at 80% retention. Capital One can afford it; Groupon's unit economics would need stress-testing.

---

## 4. Soft Currency (Bucks Inspiration) - Earn, Redeem, Breakage

### Earn
- 1 credit = $1 (1:1, transparent) [Data, High]
- Offer-based, not flat rate (varies by merchant, product category, time)
- Welcome/referral bonus as a flat credit injection

### Redeem
- Gift-card-only, 50+ rotating retailers
- No cash-out, no statement credit, no bank deposit
- Variable redemption inventory per user (rationing - not all users see all gift cards)

### Breakage signals (high breakage = high margin for issuer) [Opinion, High]
- Rotating redemption inventory reduces "redeem-at-your-favorite-retailer" option
- Denials after purchase confirmation (tracking "errors") reduce effective payout
- Recent removal of most-popular brands (Walmart, Home Depot, Macy's, Lowes) pushes users toward lower-preference redemptions or holding credits
- Phone-conflict redemption bugs prevent completion
- One blogger reported $99.44 in "gift cards never received" - pure breakage from Cap One's perspective

**Implied breakage rate**: [DATA GAP] No public disclosure. My estimate: 15-30% of earned credits never get redeemed, either because users abandon, hit bugs, or the preferred gift card is unavailable when they try. [Opinion, Low - speculative]

### Why this model is elegant
- Soft currency is a balance-sheet liability but not a cash outflow until redeemed
- Gift-card redemption is further downstream cost deferred + gift cards have their own breakage (3-10% industry standard)
- Compounding breakage: Cap One issues rewards -> some never redeemed -> of those redeemed, 5-10% of gift card value never spent -> real cash cost to Cap One is 60-80% of headline "earned"

---

## 5. Retention / Habit Drivers

### What Cap One Shopping does WELL for retention [Data + Opinion]
- Passive activation - extension works without user thinking about it (habit-free habit)
- Price-drop alerts on watchlisted items create "earned surprise" email opens
- Rewards-posted confirmations are dopamine hits that drive re-engagement
- 90-day retention requirement on bonus creates minimum tenure floor (~3 months)
- Gift-card redemption requires balance accumulation -> forces multi-visit behavior

### Weekly habit formation signal [Opinion, Medium]
- The extension is almost entirely *reactive* (it surfaces when you shop)
- Does NOT drive weekly active use the way Groupon would need
- Users probably open the web app or mobile app only at redemption time or when a price-drop notification fires
- If Groupon wants WEEKLY habit, the Cap One model is insufficient - needs a pull mechanic (daily deal, weekly offer reveal, streak, etc.)

### What's missing for habit
- No streaks / no daily reveal
- No gamification (no tiers, no progress bars beyond "$X to next redemption")
- No social / referral amplification inside product (only via the $80 referral link sharing)

---

## 6. Weaknesses and Churn Signals

### Documented churn causes
1. **Tracking failures** - single most common complaint across Reddit, Trustpilot, Milestalk, Frequent Miler [Data, High]
2. **Denial after confirmation** - reward shows as "confirmed" then flipped to "ineligible" 30-90 days later, past return window [Data, High]
3. **Poor customer service** - scripted responses, "wait 1 year before we investigate" form letters, account terminations [Data, High]
4. **Gift-card-only friction** - users want cash or PayPal (Honey has PayPal) [Data, High]
5. **Redemption inventory rotation** - users hold credits, find preferred retailer gone [Data, High]
6. **Phone-number conflict redemption bug** - prevents completion entirely [Data, Medium]
7. **Affiliate hijacking** - users indirectly affected as influencers/creators stop recommending the tool [Data, High]

### Public churn signal
- Trustpilot 1.3/5 on 305 reviews (concentrated power-user complaints)
- Multiple "I'm done with Capital One Shopping" blog posts with specific dollar amounts
- Class-action Dec 2025 (settling Apr 17 2026 claim deadline)

### Hidden churn signal
- The rotation of "best" redemption partners (Walmart, Home Depot, Macy's removed) suggests merchant pushback - merchants may be cutting Cap One off because of last-click hijacking
- If this trend continues, redemption catalog shrinks -> user value shrinks -> churn accelerates

---

## 7. What Groupon Should Copy

1. **1:1 transparent soft currency** (1 Buck = 1 dollar equivalent). The "1000 credits = ???" obfuscation Rakuten sometimes uses creates distrust. Cap One's clarity is a feature. [Confidence: High]

2. **No paid tier, no banking tie-in required.** Keep loyalty layer standalone. Cross-sell to merchant partners or subscription products separately. Don't make loyalty a Groupon+ feature. [Confidence: High]

3. **Gift-card-only redemption** to preserve unit economics. Breakage + gift-card-secondary-breakage compounds. Only add cash-out if structurally forced by competition. [Confidence: High]

4. **90-day install-retention gate** on the welcome bonus. This converts bonus-hunters into habit-formed users. Elegant CAC protection. [Confidence: High]

5. **Price-comparison alerts as universal-credit hook.** Even when no coupon or cashback exists, the "hey, it's cheaper elsewhere" alert creates value and keeps the tool useful. This is the Wikibuy DNA. [Confidence: High]

6. **Cross-retailer watchlist / price-drop alerts** as a pull-back-to-app mechanic. Groupon could watchlist deals and alert on reactivation. [Confidence: Medium]

7. **Rotating redemption inventory** - even if controversial, it allows Groupon to control P&L by cycling high-cost partners. Limit it to 20-30% rotation to avoid user outrage. [Confidence: Medium]

---

## 8. What Groupon Should NOT Copy

1. **Affiliate cookie hijacking / last-click overwrite.** This is the subject of the $4M class action and is destroying Cap One's relationship with influencers/creators. Groupon has a content+editorial audience - don't torch those relationships. [Confidence: High]

2. **Post-confirmation reward denials.** The single largest driver of bad reviews. If Groupon marks a reward "confirmed", it must pay it. Build a reserve-and-release system, not a confirm-and-revoke one. [Confidence: High]

3. **"Wait 1 year before we investigate" customer service script.** Will kill NPS. Groupon needs faster dispute SLA (30-day max). [Confidence: High]

4. **Gift-card-only with rotating inventory that removes top brands.** Cap One removed Walmart, Home Depot, Macy's, Lowe's. Groupon should lock in stable top-5 redemption partners (Amazon, Target, Walmart, Starbucks, Apple gift card or equivalents) with long-term contracts. [Confidence: High]

5. **Reactive-only model.** Groupon needs WEEKLY habit - Cap One's reactive extension is the wrong template. Add pull mechanics (daily deal reveal, weekly offer, streak). [Confidence: High]

6. **Safari extension per-site activation friction.** If Groupon ships iOS Safari extension, invest in one-tap "enable for all sites" UX to avoid Cap One's activation drop-off. [Confidence: Medium]

---

## 9. Data Gaps

1. **MAU / DAU** - No public numbers. "6M+ Chrome users" and "10M+ total" are company-stated vanity metrics, not activity metrics.
2. **Onboarding email cadence** - Not publicly documented; would require real account creation to capture.
3. **Redemption rate / breakage rate** - No disclosure. My 15-30% breakage estimate is informed speculation.
4. **Team headcount** - Not disclosed. Active hiring signals investment but exact size unknown.
5. **12-month trajectory** - Similarweb traffic shows +58% MoM in Mar 2026; need time-series.
6. **Unit economics** - Revenue per user, CAC payback period - not disclosed.
7. **Share of redeemed credits by top retailer** - Would reveal breakage-inventory strategy.
8. **Genuine vs prompted App Store reviews** - No evidence either way; assumption of prompt-timing bias is unvalidated.
9. **Cap One internal KPI for the Shopping product** - Is it CAC efficiency, credit-card conversion lift, or standalone P&L?
10. **The current headline bonus** - $40 / $45 / $80 / $200 rotates. Need live check at time of Groupon's decision.

---

## 10. Red Flags / Yellow Flags

### Red flags (things Groupon must avoid replicating)
- Affiliate cookie hijacking class action ($4M preliminary settlement Dec 2025)
- Post-confirmation reward denials
- Aggressive YMMV targeting that leaves most users with no bonus path
- Phone-number redemption bugs (operational failure)
- Merchant churn from redemption catalog (Walmart/Home Depot/Macy's gone)

### Yellow flags (worth watching, not disqualifying)
- Trustpilot 1.3 vs App Store 4.9 divergence - reviews are being gamed (prompt timing) OR genuine happy users outnumber power-user complainers
- 81.76% direct traffic is brand-strong but also means zero SEO/paid scale if brand erodes
- Rotating redemption inventory
- 90-day retention requirement may be too onerous for Groupon's audience (more casual than Cap One's financial-savvy user base)
- Reactive-only activation model may not drive WEEKLY habit

### Green flags (genuinely strong)
- 1:1 transparent currency
- No paid tier, no banking tie-in required - truly standalone
- Price comparison universal credit hook
- 6M+ Chrome users is real scale (Chrome Web Store public number)
- #2 Top Free App (Shopping) on iOS is real discovery channel

---

## 11. Sources

### Tier 1 (press, Cap One official, regulatory/legal)
- Capital One. "Capital One Shopping: How It Works." https://www.capitalone.com/learn-grow/money-management/capital-one-shopping/
- CNBC (2018-11-20). Wikibuy acquisition. https://www.cnbc.com/2018/11/20/capital-one-buys-startup-used-to-price-check-while-shopping-on-amazon.html
- Tech Startups (2018-11-20). Wikibuy acquired by Capital One. https://techstartups.com/2018/11/20/capital-one-buys-price-check-startup-wikibuy/
- PR Newswire (2025-09-19). Class action settlement announcement. https://www.prnewswire.com/news-releases/if-you-advertised-online-with-merchants-...
- ABA Banking Journal (2026-01). Virginia district court preliminary approval. https://bankingjournal.aba.com/2026/01/virginia-district-court-grants-preliminary-approval-for-settlement-in-influencer-lawsuit-against-capital-one/
- classaction.org. Settlement details. https://www.classaction.org/news/capital-one-steals-content-creators-online-sales-commissions-through-shopping-extension-class-action-claims
- Crunchbase. Acquisition profile. https://www.crunchbase.com/acquisition/capital-one-acquires-wikibuy--9716971f

### Tier 1.5 (SimilarWeb, App Store, Chrome Web Store)
- SimilarWeb. capitaloneshopping.com traffic analytics Mar 2026. https://www.similarweb.com/website/capitaloneshopping.com/
- App Store. Capital One Shopping: Save Now. https://apps.apple.com/us/app/capital-one-shopping-save-now/id1089294040
- App Store. Safari Extension. https://apps.apple.com/us/app/capital-one-shopping-extension/id1477110326
- Chrome Web Store. Capital One Shopping. https://chromewebstore.google.com/detail/capital-one-shopping-save/nenlahapcbofgnanklpelkaejcehkggg

### Tier 2 (industry press, affiliate/deals blogs, Rakuten case study)
- Rakuten Advertising case study. https://rakutenadvertising.com/resources/case-study-capital-one-shopping/
- Doctor of Credit. Referral bonus history. https://www.doctorofcredit.com/join-capital-one-shopping-get-10-after-spending-10/
- Frequent Miler. $80 referral bonus terms. https://frequentmiler.com/capital-one-shopping-offering-80-referral-bonus-for-both-sides/
- Frequent Miler. Gift card redemption options. https://frequentmiler.com/capital-one-shopping-gift-card-redemption-options/
- Upgraded Points. Capital One Shopping usage guide. https://upgradedpoints.com/credit-cards/capital-one-shopping/
- FinanceBuzz. Capital One Shopping vs Honey. https://financebuzz.com/capital-one-shopping-vs-honey
- FinanceBuzz. 2026 review ($1K+ savings). https://financebuzz.com/capital-one-shopping-review
- The Points Guy. Shopping portal guide. https://thepointsguy.com/loyalty-programs/capital-one-shopping/
- Dollar Sprout. Capital One Shopping review. https://dollarsprout.com/capital-one-shopping-review/

### Tier 3 (user sentiment - Reddit / Trustpilot / blogs)
- Trustpilot. capitaloneshopping.com reviews (1.3/5, 305 reviews). https://www.trustpilot.com/review/capitaloneshopping.com
- Milestalk. "Capital One Shopping: Why I'm Done With It." https://milestalk.com/capital-one-shopping-why-im-done-with-it/
- PhatWallet forums. $45 bonus after $15 purchase thread. https://phatwalletforums.com/topic/39722/
- MoneyPantry review. https://moneypantry.com/capital-one-shopping-review/
- Quora. Rip-off complaints. https://www.quora.com/I-have-read-many-online-complaints-Is-Capital-One-Shopping-a-rip-off
- Saint Augustine's (SEO content, lower quality but had $45 terms). https://explore.st-aug.edu/exp/unlocking-major-savings-the-definitive-guide-to-earning-your-capital-one-shopping-45-bonus
- Penny Hoarder. https://www.thepennyhoarder.com/save-money/capital-one-shopping-review/

### Labeling summary
- [Data] claims: sourced from Tier 1 or cross-verified across Tier 2
- [Estimate] claims: my computation from reported inputs
- [Opinion] claims: my inference, flagged as such
- [Assumption] claims: unverified reasonable prior
- DATA GAP: flagged where no source was found

### Freshness
- All sources checked Apr 21 2026
- Traffic data: Mar 2026 (1 month old)
- Class action: Dec 2025 preliminary approval, Apr 17 2026 claim deadline (live)
- Referral terms: Feb-Apr 2026 (current)
- Wikibuy acquisition: Nov 2018 (historical, stable fact)
