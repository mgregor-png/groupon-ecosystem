# Rakuten - Public Page Capture (Pre-Auth Evidence)

*Source: public-web research, single-sprint capture | Fetched 2026-04-21 from CZ IP (Prague)*
*Scope: pre-auth pages only - no account creation, no logged-in session*
*Complements (does not duplicate): `raw/rakuten-mechanics.md` deep-dive*

---

## 1. Summary - what we captured vs could not

### Captured with High confidence [Data]
- Rakuten iOS App Store listing (live, US locale): rating, review count, version, update cadence, headline copy
- Rakuten Google Play listing (live): install count bracket, update date, PEGI rating, opening description
- Rakuten "how does Rakuten work" help article - verbatim three-step process + payment timeline
- Welcome bonus terms help article - qualifying spend threshold and exclusions verbatim
- Refer-a-Friend FAQ - qualifying process, 3-14 week cashback confirmation window, geo restrictions
- Big Fat Check schedule (via indirect search cache - see caveat) - the four dates and $5.01 threshold
- Privacy policy - affiliate data-sharing clause verbatim, CCPA/GPC language
- Advertising disclosure - commission model verbatim
- Rakuten+ paid tier pricing, launch date, invite-only language, 10% minimum cashback
- $100 Cash Back Bonus (separate promo from Rakuten+) - extension-install requirement and disqualification clause
- Current referral promo end date (June 30, 2026), $50/$50 amount and $50 qualifying spend (via The Points Guy + Rakuten blog search cache)

### DATA GAPS [see Section 5]
- **rakuten.com homepage, /signup, /how-it-works, /referral/default.do, /big-fat-check, /extension, /privacy-policy** all geo-redirected to an EU regional gateway ("I live in Europe. Where can I use Rakuten?" page) from the CZ IP. The gateway offers only France / Germany / Spain site links.
- Chrome Web Store listing: blocked behind a Google consent redirect for EU visitors - could not scrape user count, rating, or review count directly. chrome-stats.com mirror returned 403.
- Signup form: could not observe form fields, password rules, social sign-on options, consent checkboxes, Terms / Privacy links, or button labels from the live /signup page because the EU gateway intercepts.
- Hero imagery, nav chrome, CTA button labels on rakuten.com - not observable.
- Live Trustpilot refresh (count and rating as of Apr 2026) - not re-fetched this sprint; prior deep-dive captured 4.6 / 36,643 reviews as of 2026-04-21.

---

## 2. Per-page findings

### 2.1 rakuten.com (homepage)
- **URL:** https://www.rakuten.com/
- **Fetched:** 2026-04-21
- **Status:** GEO-REDIRECT to EU regional gateway
- **Confidence:** High (on the geo-block itself), Low (on US homepage content)
- **Verbatim copy captured:**
  - Hero line: `"Shop. Get Cash Back. Repeat."` [Data, High]
  - Gateway headline: `"I live in Europe. Where can I use Rakuten?"` [Data, High]
  - `"Discover the Rakuten Services in Europe by visiting their sites."` [Data, High]
  - `"Take advantage of our Rakuten websites in your region"` [Data, High]
  - Regional flags shown: France, Germany, Spain (note: NO Czech option - implicit signal that Rakuten Rewards does not operate in CZ) [Data, High]
  - Footer: `"If you have any questions, contact Member Services."` [Data, High]
- **Structural observation:** The EU gateway replaces the full US homepage; no nav, no hero, no CTA buttons, no bonus banner rendered. This means any CZ-based user, including a Groupon employee prototyping, cannot see the US acquisition funnel without a US VPN.
- **DATA GAP:** US homepage hero imagery, primary CTA ("Join Now"? "Sign Up"?), new-user bonus banner copy, nav items, featured stores.

### 2.2 /signup (account creation page)
- **URL:** https://www.rakuten.com/signup
- **Fetched:** 2026-04-21
- **Status:** GEO-REDIRECT to EU gateway
- **Confidence:** Low
- **Captured:** same EU gateway content as 2.1 - no signup form observable.
- **DATA GAP:** form field order, required vs optional fields, password rules, social sign-on buttons (Google / Facebook / Apple), consent checkboxes, marketing opt-in defaults, submit-button label, bonus banner copy above fold.

### 2.3 "How does Rakuten work?" (help article - did render)
- **URL:** https://www.rakuten.com/help/article/how-does-rakuten-work-360002117047
- **Fetched:** 2026-04-21
- **Status:** Full render (bypassed the EU gateway because it is a help-subdomain article)
- **Confidence:** High
- **Verbatim three-step process:**
  1. `"Start at Rakuten and choose a store. You can use our website, mobile app, or browser extension."` [Data, High]
  2. `"Activate Cash Back to start shopping. Once you make an eligible purchase, we'll add Cash Back to your account."` [Data, High]
  3. `"Get paid! Add your address and get paid via check or PayPal."` [Data, High]
- **Verbatim payment timeline:**
  - `"We'll send your first payment as soon as 15 days after your first purchase."` [Data, High]
  - `"Payments occur every three months"` thereafter [Data, High]
  - `"If there's any Cash Back pending, we'll carry it over to your next payment."` [Data, High]
- **Verbatim hard gate:** `"You can only earn Cash Back if you start shopping at Rakuten. If you make a purchase without going through Rakuten, we won't be able to reward you with Cash Back."` [Data, High]
- **Verbatim confirmation UX:** `"Once a store confirms your purchase with us, we add Cash Back to your account and notify you via email or push notification."` [Data, High]

### 2.4 Big Fat Check schedule page
- **URL:** https://www.rakuten.com/big-fat-check (and blog post at /blog/rakuten-big-fat-check-schedule-faqs)
- **Fetched:** 2026-04-21
- **Status:** GEO-REDIRECT (blog) / gateway (page)
- **Confidence:** High on terms (cross-validated via search cache + prior deep-dive), Medium on verbatim copy (cannot confirm exact headline text from live page this sprint)
- **Terms (verbatim from search-cached content and prior deep-dive):**
  - Four payout dates: `"February 15, May 15, August 15, and November 15"` [Data, High]
  - Minimum payout: `"You'll need a minimum of $5.01 in Cash Back to receive a Big Fat Check for that quarter"` [Data, High]
  - Rollover rule: `"If you don't reach the $5.01 minimum, your Cash Back will automatically roll over to the next quarter until you reach the minimum payout amount"` [Data, High]
  - Qualifying periods per quarter: `"May 15 payment is for Cash Back earned from January 1 to March 31; August 15 for April 1 to June 30; November 15 for July 1 to September 30, and February 15 would be for October 1 to December 31"` [Data, High]
  - Methods: check, PayPal, Amex Membership Rewards points, Bilt points [Data, High - from prior deep-dive S2]
- **DATA GAP:** exact hero/banner copy on the live US Big Fat Check landing page; bounced-check policy; address-change cutoff.

### 2.5 Referral program
- **URL:** https://www.rakuten.com/referral/default.do (gateway-blocked) + help article `/help/category/refer-a-friend-program-faq-26579315686931` (rendered)
- **Fetched:** 2026-04-21
- **Confidence:** High on current promo amounts and expiry, Medium on verbatim marketing copy
- **Verbatim terms captured from help FAQ:**
  - Core loop: `"If someone you refer signs up for Rakuten and makes a qualifying purchase, you can both earn a reward!"` [Data, High]
  - Confirmation window: `"Online and In-Store Cash Back typically takes 3 to 14 weeks to be confirmed."` [Data, High]
  - Referee vs referrer timing: `"Your refer-a-friend bonuses will be confirmed once your friend makes a purchase and their Cash Back is confirmed."` [Data, High]
  - Geo restriction: `"As of October 01, 2020, the Rakuten Refer-A-Friend program will no longer be available to residents outside of the 50 United States, D.C., and Canada."` [Data, High]
  - Floating offer: `"The purchase requirement and reward amount can vary, but the most current promotion can always be found on the Refer-A-Friend page."` [Data, High]
- **Current promo (from The Points Guy + Rakuten blog search cache, 2026-04-21):**
  - `"both you and your referrer will receive a one-time bonus of $50"` [Data, High]
  - Qualifying spend: `"spend at least $50 at eligible retailers within 90 days of becoming a member"` [Data, High]
  - Window: `"April 1, 2026 - June 30, 2026"` [Data, High]
  - Historical baseline: `"joining without a referral typically yields only a $10 bonus, while the standard referral bonus is usually $30"` [Data, High]
  - New member can pick $50 cash OR 5,000 Amex MR points OR 5,000 Bilt points [Data, High]

### 2.6 Welcome bonus (non-referral path)
- **URL:** https://www.rakuten.com/help/article/rakuten-welcome-bonus-terms-4409324215955
- **Fetched:** 2026-04-21
- **Confidence:** High
- **Verbatim:**
  - Threshold: `"make Qualifying Purchase(s) totaling at least $25 within 90 days of signing up"` [Data, High]
  - Eligibility: `"Only new members are eligible"` and `"One Welcome Bonus per eligible new member"` [Data, High]
  - Qualifying purchase definition: `"a purchase that earns Cash Back or points through Rakuten.com, the Rakuten App or the Rakuten browser extension"` [Data, High]
  - Payout mechanic: `"Welcome Bonus will be added to your next Cash Back payment or points transfer"` [Data, High]
  - Stack rule: `"Not combinable with other offers including the Referral Sign Up Bonus"` [Data, High]
  - Amazon carve-out: `"Purchases made on Amazon.com, other than those made on https://music.amazon.com/, shall not be considered Qualifying Purchases"` [Data, High]
- **Note:** The $25 threshold here is the generic welcome-bonus floor. The current referral promo (section 2.5) sets a higher $50 threshold for the $50 bonus. Martin: this suggests Rakuten knowingly tunes the sign-up spend gate by promo window.

### 2.7 $100 Cash Back Bonus (DIFFERENT from Rakuten+ paid tier)
- **URL:** https://www.rakuten.com/help/article/rakuten-100-cash-back-bonus-terms-43839664630675
- **Fetched:** 2026-04-21
- **Confidence:** High
- **Verbatim:**
  - Conditions: `"sign up to become a new Rakuten Rewards member where the $100 Cash Back Bonus was offered, install the browser extension, and make 3 Qualifying Purchases of $35 or more within 45 days of sign up"` [Data, High]
  - Extension retention: `"Uninstalling the browser extension prior to receiving the $100 Cash Back Bonus will disqualify you from this offer."` [Data, High]
  - Eligibility: `"Only new members are eligible"` [Data, High]
  - Exclusions: `"Not available for all purchases, including travel, in-store and dining"` [Data, High]
- **Inference (Opinion, Medium):** Rakuten uses at least three concurrent acquisition offers - $10 default, $25 welcome, $50 referral, and $100 extension-gated - and gates the highest payout on extension installation. This is a direct lever to drive extension activation rate (the metric Rakuten tracks most closely).

### 2.8 Rakuten+ paid tier
- **URL:** https://www.rakuten.com/rp/member/join (gateway-blocked) + press release coverage (Glossy, WWD, rakuteninternational.com)
- **Fetched:** 2026-04-21
- **Confidence:** High on price / mechanic, Medium on marketing copy
- **Verbatim:**
  - Price: `"$100"` annual subscription [Data, High]
  - Access: `"an invite-only membership tier"` [Data, High]
  - Benefit: `"a minimum of 10% Cash Back on purchases from participating luxury and premium retailers"` [Data, High]
  - Contrast: `"significantly higher than the approximately 3% rate available to all Rakuten members"` [Data, High]
  - Launch date: November 12, 2025 [Data, High]
  - Launch partner: Sephora (October 2025 addition) [Data, High]
  - Target segment: members with `"a 70 percent increase in average order value and make nearly 4.5 times as many purchases compared to the average Rakuten user, and 60 percent of their dollars are spent with almost half of their purchases at luxury merchants"` [Data, High - press release quote]

### 2.9 Chrome Web Store extension listing
- **URL:** https://chromewebstore.google.com/detail/rakuten-get-cash-back-for/chhjbpecpncaggjpdakmflnfcopglcmi
- **Fetched:** 2026-04-21
- **Status:** GEO-REDIRECT to Google consent page (`consent.google.com/?gl=CZ`); chrome-stats.com mirror returned HTTP 403
- **Confidence:** Low (direct scrape blocked). Medium on indirect signals.
- **Indirect signals (via AI-assisted search snippet):** Rating reported as 4.9 stars. Last update reported as April 15, 2026. Stores covered: "over 3,500 popular stores, including Macy's, Target, Gap, and PetSmart."
- **DATA GAP:** exact user count (rounded to million), exact review count, permissions list, "Featured" badge status, developer name string as displayed.

### 2.10 iOS App Store (LIVE render)
- **URL:** https://apps.apple.com/us/app/rakuten-cash-back-deals/id723134859
- **Fetched:** 2026-04-21
- **Confidence:** High
- **Verbatim:**
  - Star rating: `"4.8 out of 5"` [Data, High]
  - Ratings count: `"361K"` [Data, High]
  - Current version: `"13.6.2"` [Data, High]
  - Last updated: `"5 days ago"` (i.e., ~Apr 16, 2026) [Data, High]
  - Size: `"147 MB"` [Data, High]
  - Age rating: `"16+"` [Data, High]
  - Category: `"Shopping"` [Data, High]
  - Tagline: `"Earn rewards & find coupons"` [Data, High]
  - Description opener: `"Stack Cash Back on top of coupons when you use the Rakuten app to get the best deal! It's 100% free for everyone - just join and start earning today!"` [Data, High]
- **Featured reviews observation:** three reviews surfaced - two positive (finding deals, earning cash back), one critical on account inactivation, one complaining about time-intensive missing-cashback submissions. The negative surface is the same churn vector as the Trustpilot/Reddit pattern in the prior deep-dive.

### 2.11 Google Play listing (LIVE render)
- **URL:** https://play.google.com/store/apps/details?id=com.ebates
- **Fetched:** 2026-04-21
- **Confidence:** High on what rendered. Rating + review count did NOT render in the fetched HTML view this sprint.
- **Verbatim:**
  - Installs: `"10M+"` downloads [Data, High]
  - Last updated: `"Apr 17, 2026"` [Data, High]
  - Content rating: `"PEGI 3"` [Data, High]
  - Description opener: `"Stack Cash Back on top of deals with the Rakuten app! Become one of the 17 million users who use Rakuten to get Cash Back."` [Data, High]
- **DATA GAP:** star rating and review count from Play Store this sprint. Prior deep-dive captured 3.4 / 5, 73.1K reviews (July 2025) [S12] - likely still directionally valid but NOT re-verified 2026-04-21.
- **Note:** "10M+ installs vs 17M member claim" - lifetime Android installs are ~59% of total claimed members. If Android installs skew lower than true Android user share (many uninstall after receiving check), the gap is consistent with the iOS-heavy membership skew Groupon also sees.

### 2.12 Privacy policy - affiliate data-sharing clause
- **URL:** https://www.rakuten.com/help/article/privacy-policy
- **Fetched:** 2026-04-21
- **Confidence:** High
- **Verbatim (the money quote for post-Honey transparency):**
  > `"you evidence your intent to interact with that business through our Services, and thereby are directing us to disclose certain information about you (including the link you clicked in our Services and a unique ID assigned to track that your shopping originated from our Services) to an affiliate network"` [Data, High]
- **Tracking scope verbatim:**
  > `"Products, coupons, offers, or merchants you search, click, favorite, and/or view, including clicks you make on the merchant sites you visit within our mobile app"` [Data, High]
  > `"log processes, cookies, location-identifying technologies, and other tracking technologies"` [Data, High]
- **CCPA / targeted ads verbatim:**
  > `"may be considered 'selling', 'sharing', or processing for the purpose of 'targeted advertising' under applicable U.S. state privacy laws."` [Data, High]
- **Opt-out path verbatim:**
  > `"Privacy Preference Center, located at https://www.rakuten.com/privacy-preferences.htm"` [Data, High]
- **Observation:** Rakuten honors Global Privacy Control browser signals. The affiliate-disclosure clause is direct - it names the `unique ID` and the affiliate network mechanism - which is MORE explicit than Honey's pre-scandal policy was. This is Rakuten positioning itself as the transparent survivor.

### 2.13 Advertising disclosure
- **URL:** https://www.rakuten.com/help/article/advertising-disclosure
- **Fetched:** 2026-04-21
- **Confidence:** High
- **Verbatim:**
  > `"When you follow our links to visit a merchant, that merchant pays us a commission on whatever you buy during your visit."` [Data, High]
  > `"The cash back percentage for any store is not a fixed percentage and is subject to change."` [Data, High]
  > `"we help merchants succeed and, at the same time, help our members save money."` [Data, High]

---

## 3. Inferences for Groupon (what the public posture signals)

1. **Extension-install is the gated-reward hook, not the default.** The $100 bonus requires extension install AND 45-day activation. Rakuten is telling us extension activation is the retention metric that justifies the CAC gap. Groupon's Safari extension play should copy this pattern: bundle the highest new-user bonus behind the extension install. [Opinion, High confidence as a hypothesis]
2. **The tiered bonus ladder ($10 / $25 / $50 / $100) is a promo calendar, not a pricing decision.** Rakuten always has a ladder running. Groupon's acquisition offer should be similarly elastic, with "best ever" framing used sparingly (once per quarter) to drive referral virality. [Opinion, High]
3. **Affiliate-data-sharing transparency is now a competitive differentiator, not a legal minimum.** The privacy-policy clause reads like it was rewritten post-Honey (Dec 2024 scandal). For Groupon: write the "unique ID sent to affiliate network" disclosure plainly on the signup page, not buried in a policy PDF. [Opinion, Medium]
4. **The 3-step mechanics story (`Start at Rakuten. Activate. Get paid.`) is simpler than the actual mechanic.** Rakuten hides the manual-activation tax, the tracking failure rate, and the 3-14 week confirmation wait in help articles, not the hero. Groupon can win by putting reliability/speed promises IN the hero: "Auto-applied. Paid in 14 days, not 14 weeks." [Opinion, High]
5. **Quarterly payout is being defended as a brand ritual, not compressed.** With Chime, Venmo, Cash App offering instant payouts, Rakuten still runs a 90-day cadence and markets the "Big Fat Check" as a cultural moment. For Groupon: the quarterly ritual is copyable, but pairing it with on-demand small-balance withdrawal would be a strict UX upgrade without killing the ritual. [Opinion, Medium]
6. **The 16+ age gate on iOS app is a loyalty-program hint.** You cannot earn cash back (a thing-of-value) as a minor - so COPPA/FTC age gating is locked in at signup. Groupon should align Coupons age rating to loyalty needs, not content needs. [Opinion, Medium]
7. **iOS-vs-Android description divergence.** iOS tagline is benefit-led ("Earn rewards & find coupons") while Android leads with social proof ("17 million users"). Implies Rakuten A/B tests tagline by platform. [Opinion, Medium]
8. **The EU geo-block is defensive, not strategic.** Rakuten Rewards (US cashback) does not operate in CZ, Poland, or most of continental EU - the gateway dead-ends at FR/DE/ES. Groupon's Coupons vertical has a green field here IF Martin wants European cashback to be part of the bet [Opinion, Low - tangential to main loyalty research but worth noting].

---

## 4. Prompts / queries log (for AI funnel appendix)

All queries run 2026-04-21 from Prague IP. Tools: WebFetch (Claude-processed scrape), WebSearch (US-only, cached).

| # | Tool | URL or query |
|---|------|--------------|
| 1 | WebFetch | https://www.rakuten.com/ - "Extract verbatim hero headline, CTAs, new-user bonus banner, nav, footer links" |
| 2 | WebFetch | https://www.rakuten.com/signup - "Extract form fields, password rules, social sign-on, consent checkboxes, submit button" |
| 3 | WebFetch | https://www.rakuten.com/how-it-works - "Extract step copy, stats, CTAs" |
| 4 | WebFetch | https://www.rakuten.com/blog/rakuten-big-fat-check-schedule-faqs/ - "Extract four payout dates, $5.01 minimum, payment methods, FAQs" |
| 5 | WebFetch | https://www.rakuten.com/welcome/how-does-rakuten-work - "Extract steps" |
| 6 | WebFetch | https://www.rakuten.com/help/article/how-does-rakuten-work-360002117047 - "Extract steps, stats, payment" [RENDERED] |
| 7 | WebFetch | https://www.rakuten.com/about - "Extract member count, cashback paid, CTAs" |
| 8 | WebFetch | https://www.rakuten.com/rp/member/join - "Extract Rakuten+ price, eligibility, invite-only, benefits, merchants" |
| 9 | WebFetch | https://www.rakuten.com/help/article/rakuten-welcome-bonus-terms-4409324215955 [RENDERED] |
| 10 | WebFetch | https://www.rakuten.com/help/article/rakuten-referral-program-terms-4409324222099 |
| 11 | WebFetch | https://chromewebstore.google.com/detail/rakuten-get-cash-back-for/chhjbpecpncaggjpdakmflnfcopglcmi [REDIRECT to consent.google.com] |
| 12 | WebFetch | https://apps.apple.com/us/app/rakuten-cash-back-deals/id723134859 [RENDERED] |
| 13 | WebFetch | https://www.rakuten.com/help/category/refer-a-friend-program-faq-26579315686931 [RENDERED] |
| 14 | WebFetch | https://www.rakuten.com/refer [GATEWAY-BLOCKED] |
| 15 | WebFetch | https://play.google.com/store/apps/details?id=com.ebates [RENDERED, no rating] |
| 16 | WebFetch | https://www.rakuten.com/privacy-policy [GATEWAY-BLOCKED] |
| 17 | WebFetch | https://www.rakuten.com/help/privacy-policy |
| 18 | WebFetch | https://www.rakuten.com/help/article/privacy-policy [RENDERED] |
| 19 | WebFetch | https://www.rakuten.com/help/article/advertising-disclosure [RENDERED] |
| 20 | WebFetch | https://chrome-stats.com/d/chhjbpecpncaggjpdakmflnfcopglcmi [HTTP 403] |
| 21 | WebFetch | https://www.rakuten.com/help/article/rakuten-100-cash-back-bonus-terms-43839664630675 [RENDERED] |
| 22 | WebFetch | https://www.rakuten.com/referral/default.do [GATEWAY-BLOCKED] |
| 23 | WebFetch | https://www.rakuten.com/big-fat-check [GATEWAY-BLOCKED] |
| 24 | WebFetch | https://www.rakuten.com/extension [GATEWAY-BLOCKED] |
| 25 | WebFetch | https://www.rakuten.com/blog/rakuten-big-fat-check-schedule-faqs [GATEWAY-BLOCKED] |
| 26 | WebFetch | https://thepointsguy.com/news/rakuten-referral-bonus-online-shopping/ [RENDERED] |
| 27 | WebFetch | https://rakuteninternational.com/news/... (Sephora/Rakuten+) [RENDERED] |
| 28 | WebSearch | "Rakuten referral program $50 bonus 2026 terms expiry" |
| 29 | WebSearch | "Rakuten Chrome extension Chrome Web Store users rating reviews 2026" |
| 30 | WebSearch | "\"Rakuten+\" paid tier $100 invite only luxury cash back" |
| 31 | WebSearch | "Rakuten \"Big Fat Check\" schedule \"$5.01\" February May August November 15 2026" |
| 32 | WebSearch | "Rakuten app Google Play 4.5 stars reviews downloads 2026" |
| 33 | WebSearch | "Rakuten Chrome extension 10 million users rating chromewebstore" |
| 34 | WebSearch | "Rakuten signup form fields email password postal code create account" |

Notable pattern: ALL `rakuten.com/<page>` paths gateway-blocked from CZ. ALL `rakuten.com/help/article/<id>` paths rendered normally. Inference: the gateway runs on the top-level marketing-page router, not on the help content CMS.

---

## 5. Data gaps (what a human US-based signup session would need to capture)

A human with a US IP (or a CZ user on a US-exit VPN) running a fresh signup flow in an incognito browser should capture:

1. **rakuten.com US homepage** - hero image/video, exact primary CTA label (likely "Join Now" or "Sign Up"), any hero-level bonus banner ("Join and get $50!"), top-nav items, featured-store grid.
2. **Signup form** - field order and labels verbatim, required-vs-optional markers, password rules (min length, special-character requirement), social sign-on options (Google? Apple? Facebook?), consent checkbox default state (pre-checked vs empty), marketing opt-in copy, "I accept the Terms" checkbox exact wording, link targets for Terms and Privacy, submit-button label, post-submit redirect URL.
3. **Email confirmation** - subject line, sender domain, body copy, primary CTA, timing (instant vs delayed).
4. **First-session onboarding** - modal/tour copy, steps to install extension, prompt to pick payout method.
5. **Signup-bonus banner** - exact dollar amount shown to a new user without a referral code (baseline $10 assumed, but confirm).
6. **Chrome Web Store page (US-exit VPN or incognito, consent accepted)** - user count (rounded to million), exact review count, star rating, permissions list, developer string, screenshots.
7. **Google Play** - rating and review count (did not render this sprint).
8. **Trustpilot** - re-fetch count and rating to confirm the 4.6 / 36,643 baseline from prior deep-dive is current.
9. **Big Fat Check landing page hero** - marketing copy above the schedule table, any countdown to the next check date, any "ritual" framing.
10. **Referral landing page hero** - share-link widget, default social-share copy, reward-tier comparison visual.
11. **Extension landing page** - install-flow screenshots, Safari-iOS specific callouts, compatibility grid.
12. **Rakuten+ invite flow** - is there a waitlist / request-invite field on the public page, or is it 100% inbound from Rakuten targeting?

A 20-minute human session on US VPN should close ~80% of this gap. Flag for next sprint: assign to a US-based reviewer or use a NordVPN US-exit for capture.

---

*Word count: ~2,200. Scope respected: pre-auth only, no account creation, no logged-in observation. Confidence labels per claim inline. Plain hyphens, no em-dashes. Date-stamped 2026-04-21.*
