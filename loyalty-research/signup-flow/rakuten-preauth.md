# Rakuten - Public Pre-Auth Capture
*Captured 2026-04-22 via public web, no account created. Access from CZ (EU) IP; all rakuten.com root-level URLs auto-redirect to an EU regional chooser, so US-site content was captured via mirror sources (help.rakuten.com articles which do render content, plus reviewer screenshots dated 2025-2026 and Rakuten's own App Store listing).*

---

## 1. Landing page

**Source:** rakuten.com (US homepage), per search snippets 2026-04-22. Direct fetch from CZ IP returns the EU regional chooser, not the US homepage (see section 5 - Geography).

- **Title tag / meta:** "Promo Codes, Coupons & Cash Back | Shop 3,500+ Stores!" [Data; source: Google SERP title for rakuten.com, 2026-04-22]
- **Hero tagline:** "Shop. Get Cash Back. Repeat." [Data; source: visible even on EU redirect page rendering of rakuten.com, 2026-04-22]
- **Social-proof headline:** "Since 1999, Rakuten has paid members over $3.6 billion in cash back" [Data; source: homepage copy as quoted by multiple reviewer sites 2025-2026; >12 months old for exact figure - flag staleness, likely higher now]
- **Store count:** "3,500+ stores" (both on homepage and App Store listing) [Data]
- **Category nav (top-level):** All Categories, Clothing, Accessories, Travel & Vacations, Beauty & Wellness, Shoes, Electronics, Home & Garden, Home Improvement, Pets, Auto & Tires, Baby & Toddler, Toys & Games, Sports/Outdoors & Fitness, Food/Drinks & Restaurants, Books/Music & Media, Flowers, Business Supplies & Services, Events & Entertainment, Gifts [Data; reviewer aggregations 2025-2026]
- **Hero callouts rotation** (typical, reviewer screenshots): featured-store tiles with live %-cash-back badge (e.g. "10% Cash Back"), "Double Cash Back" banners on select merchants, a "Daily Double" carousel [Inference from reviewer screenshots; freshness ~6-9 months]

## 2. Signup funnel (fields + CTAs)

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

## 3. Welcome bonus + referral

### Welcome bonus (current as of 2026-04-22)

- **Amount:** $50 cash back (or 5,000 Amex Membership Rewards points, or 5,000 Bilt points - user's choice set in account preferences) [Data; multiple reviewer sources Feb-Apr 2026]
- **Qualifying spend:** $50 in eligible Rakuten-tracked purchases within 90 days of signup [Data]
- **Offer window:** April 1, 2026 - June 30, 2026 (extended from a prior March 31, 2026 deadline) [Data; awardwallet.com + doctorofcredit.com 2026]
- **Must sign up via referral link** - direct rakuten.com signup without a referral code typically shows a lower bonus or none [Data; multiple reviewer confirmations]
- **Payout:** bonus credited to next quarterly payment cycle, typically within 60 days of the qualifying purchase clearing [Data]
- **Geography:** 50 US states + DC only (resident AND physically located) [Data; help.ebates.com terms]

### Referral program (evergreen)

- **Structure:** double-sided $50 / $50 (referrer + referee both earn $50) [Data; aligned with current welcome bonus structure]
- **Referee qualifying condition:** same as welcome bonus ($50 spend in 90 days)
- **Referrer payout:** credited within 60 days of referee's qualifying purchase, added to next quarterly Big Fat Check
- **Share channels:** unique referral link shareable via text, email, social media - Rakuten generates a personalized URL
- **Cap:** "You may qualify for a Referral Bonus more than one time" - no stated maximum [Data]
- **Source:** rakuten.com/referral/default.do + help.ebates.com Refer-A-Friend Program Terms

### The "Big Fat Check" (payment mechanic)

- **What it is:** Rakuten's brand name for the physical paper check mailed to members every quarter. Now one of four payout options (others: PayPal, Amex MR transfer, Bilt transfer). [Data]
- **Payment calendar (quarterly):**
  - **Feb 15:** earnings from Oct 1 - Dec 31
  - **May 15:** earnings from Jan 1 - Mar 31
  - **Aug 15:** earnings from Apr 1 - Jun 30
  - **Nov 15:** earnings from Jul 1 - Sep 30
- **Minimum threshold:** $5.01 confirmed cash back as of the payment-date cutoff [Data]
- **Marketing tone:** The "Big Fat Check" is arguably Rakuten's most distinctive brand asset - a playful, physical artifact that turns a pedestrian ACH/PayPal payout into an unboxing moment. It has its own dedicated blog content and social posts. [Opinion]

## 4. How it works + Safari extension

### "How it works" - pre-auth framing (3 steps)

Per rakuten.com/blog/rakuten-explained and consistent across help-center and reviewer recaps:

1. **Sign up** (free, email + password)
2. **Shop through Rakuten** (website, app, or browser extension - "always start your shopping trip through Rakuten so the visit is tracked")
3. **Get Cash Back** (quarterly payout via Big Fat Check, PayPal, Amex MR, or Bilt)

Reinforcing "why this works" paragraph: "Stores pay Rakuten for sending them shoppers, and Rakuten shares that money with its members as Cash Back."

### Safari mobile extension - install page copy

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

### iOS App Store listing (rakuten.com/ios linked to id723134859)

- **App Store headline:** "Earn rewards & find coupons"
- **Rating:** 4.8 / 5 across 361K ratings [Data]
- **Size:** 147 MB
- **Min iOS:** 18.0+
- **Age rating:** 16+
- **Feature bullets:** stack cashback with sales/coupons/shipping/loyalty; auto-apply coupons at checkout; in-store + dining cashback (location-based); unlimited referral bonuses; multiple payout options (PayPal, check, gift card); detailed cashback status + payment tracking

## 5. Pre-auth copy / positioning themes

Distilled themes the prospective user absorbs before they ever log in:

1. **"Shop. Get Cash Back. Repeat."** - three-word loop tagline. Reinforces habit-forming behavior (the flywheel is the brand).
2. **Scale + trust:** "$3.6B paid to members since 1999," "3,500+ stores" - numeric legitimacy.
3. **Free + simple:** reviewers universally lead with "it's free, it's simple." Signup = email + password only. No cards to link.
4. **Multiple payout currencies:** cash (PayPal / check) OR Amex MR OR Bilt - the travel/points crowd is explicitly courted. This is a meaningful differentiator vs. Honey and Capital One Shopping.
5. **Big Fat Check as brand artifact:** physical check mailer is a retention and word-of-mouth asset (literal photos of checks on social).
6. **Mobile-first + Safari extension:** Rakuten is the only major cashback player with a working iOS Safari Web Extension in the App Store ecosystem as of Apr 2026. Honey has an iOS app but no Safari extension parity; Capital One Shopping ships a Safari extension via their app too. [Inference; confirmed independently by the Safari Extension Competitors reference in Martin's memory.]
7. **Non-disclosure of the welcome bonus on the unauth homepage:** The $50 bonus is primarily surfaced through referral landing pages, blog posts, and points-blog marketing - not the cold homepage hero. [Inference from reviewer screenshots] This is a deliberate choice: Rakuten wants users to come in via a referral link so the referrer earns, OR to sign up cold and THEN see the bonus. Worth noting.

## 6. Notes for Martin's manual capture (what to look for once logged in)

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

## 7. Data gaps (what is human-only)

Items in this report that could NOT be validated from public pre-auth sources and NEED manual capture:

- Exact welcome-email content (subject, body, CTA buttons)
- Logged-in home dashboard screenshot + bonus progress UI
- Exact copy of the "install the extension" in-product nudge
- Whether the Safari extension respects Safari's privacy mode / Intelligent Tracking Prevention quirks
- First-merchant activation UX specifics (interstitial? toast? redirect?)
- Time-to-first-payout-prompt (how long until Rakuten asks for address/payment method)
- A/B variants: Rakuten runs extensive homepage tests; this capture represents a single temporal snapshot of public copy and may not match what US users currently see
- Visual design / color / typography specifics for the logged-in experience

## 5b. Geography gate (supplementary)

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

## 8. Sources

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
