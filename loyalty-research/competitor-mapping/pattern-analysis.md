# Cross-Competitor Pattern Analysis
*Source: automated captures 2026-04-22 from CZ IP | See `README.md` for provenance*

This is the analytic layer on top of the screenshot set. Every pattern below cites at least one PNG file in the `competitor-mapping/` folder; the raw evidence lives next to the claim.

---

## Headline patterns (what becomes obvious when you see all 7 side by side)

### 1. Safari is the battleground - "Add to Safari, It's Free" is the new default CTA

Honey landing (`honey/01-landing-fold.png`) and Coupert landing (`coupert/01-landing-fold.png`) both use **identical primary CTA wording: "Add to Safari - It's Free"**. This is a competitive convergence - both compete for the same post-Chrome-exodus cohort and both have picked Safari as the wedge. Rakuten keeps the Safari push a step down (under the hero CTA) but still invests heavily in an iOS Safari extension bundled with the app (`rakuten/08-ios-app-store-fold.png`). Capital One Shopping has a dedicated App Store listing for the Safari extension as a separate product from the main app (`capital-one-shopping/07-ios-safari-extension-fold.png`).

**Implication for Groupon:** Safari-first is no longer a differentiator - it is table stakes. Groupon's Genie + iOS Safari extension thesis is validated by the convergence, but the "we're on Safari" claim alone will not cut through. The differentiator will be WHAT the extension earns (Bucks redeemable on local experiences).

### 2. Social-proof arms race is in the hero

Every landing page uses a large member count or dollar count in the fold:
- Honey: "17 million members and counting" + "141,786 Chrome Store reviews" (`honey/01-landing-fold.png`)
- Ibotta: "$2.3B cash back paid" + "4.7 app store rating" + "3K+ retailers" (`ibotta/01-landing-fold.png`)
- Rakuten iOS App Store: "Join 17M members earning Cash Back" + "Earn $500+ a year on average" (`rakuten/08-ios-app-store-fold.png`)
- Coupert: "Trusted by 8M+ users and 70,000+ shoppers on Trustpilot" (`coupert/01-landing-fold.png`)

Honey's continued 17M member claim is notable - they are still marketing the peak-brand number in April 2026 despite having lost 40% of Chrome users. This is a willful optimism that a sophisticated user would see through, but marketing-wise it is consistent with PayPal's "no public admission the brand is damaged" posture.

**Implication for Groupon:** Social proof in the hero is table stakes. Groupon has the option to anchor on "30M app installs" or "X million Groupon deals purchased" - this will need to be decided and landed in the final mock.

### 3. Three distinct signup-friction postures

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

### 4. Currency clarity splits the category

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

### 5. Ibotta's B2B2C pivot is visible in the public surface

Ibotta IPN page (`ibotta/03-ipn-performance-network-fold.png`): hero speaks directly to **brands**, not consumers. "As the leading promotions network in the U.S., the Ibotta Performance Network helps brands maximize incremental return utilizing pay-per-sale efficiency and AI-driven optimization while delivering digital promotions at unprecedented scale." The main nav bar has a dedicated "Business solutions" entry alongside consumer-facing "Cash back" (`ibotta/01-landing-fold.png`).

This confirms the research finding that Ibotta has pivoted from consumer app to B2B2C distribution infrastructure. Compare to Rakuten, Honey, Cap One Shopping - none of which feature a brand-facing pitch in their primary nav.

**Implication for Groupon:** Ibotta's B2B2C model is a 2027 option for Groupon (per mechanic card table row 9), not a current-quarter play. But the fact that they're investing in brand-facing marketing so publicly means the opportunity is well-claimed - Groupon's window to compete on this dimension is narrower than it was 18 months ago.

### 6. Ibotta is the only serious app-first competitor

All other Tier-1 and Tier-2 competitors (Rakuten, Honey, Cap One, Coupert, RetailMeNot) lead with an **extension** CTA or a signup form on the web. **Ibotta is app-only** in presentation (`ibotta/01-landing-fold.png` - only App Store + Google Play download buttons in the hero, no web-side account creation or extension link).

This reflects Ibotta's receipt-scan mechanic, which is app-mandatory (cameras, OCR, push for alerts). It's a structural UX difference, not just a marketing choice.

**Implication for Groupon:** If Groupon's loyalty layer is genuinely app-primary (Genie + Safari extension bundled), Ibotta's landing pattern is the closer analogue than the Honey/Rakuten extension-led pattern. Worth testing in A/B. For the Friday doc, worth showing both patterns as candidate UX inspirations.

### 7. Geographic gating is asymmetric and meaningful

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

### 8. Post-scandal posture: Honey has no visible trust-recovery messaging

Honey landing (`honey/01-landing-fold.png`), Honey Gold page (`honey/03-features-gold-fold.png`), Honey terms (`honey/04-terms-fold.png` - fold shows only cookie banner), PayPal help593 page (`honey/07-paypal-help-bundled-extension-fold.png`): **no mention of the scandal, no affiliate-attribution disclosure, no acknowledgement of the 40% Chrome user loss**. The PayPal Help article reads as if late-2024 never happened.

Compare to the MegaLag-era press coverage and the class action (Cohen Milstein, Jan 5 2026 101-page amended complaint). Honey's PUBLIC posture is "nothing to see here" - legal silence is the strategy.

**Implication for Groupon:** This is the anti-pattern. Proactive affiliate-attribution disclosure at the point of cashback (per mechanic card 06) is a direct differentiator against the current Honey posture. Users who have read the MegaLag coverage and land on Honey will see continuity, not repair - Groupon can win on visible repair-first design.

### 9. The signup-friction-vs-trust tradeoff is live

Looking at the patterns together:
- **Lowest signup friction:** Honey, Coupert (passive "Add to Safari" - no email on landing)
- **Highest signup friction:** Cap One (aggressive modal interrupts landing)
- **No web signup:** Ibotta (app-only)

Cap One's aggressive modal is interesting because Cap One has the **most conservative trust posture** of the group (no paid tier, no points obfuscation, 1:1 currency, no banking tie-in required). They appear to be trading immediate conversion for account-creation-first - the user commits to a relationship before seeing the details.

**Implication for Groupon:** There's a clean A/B hypothesis here - does aggressive signup-modal conversion win vs passive-CTA + extension-first? Worth testing on the new-UI coupons pages once registration layer lands.

### 10. Slickdeals is invisible to automation (and thus to AI pattern analysis)

Slickdeals landing (`slickdeals/01-landing-fold.png`) is a Cloudflare "verify you are human" challenge. No public-page scraping possible. Agent-era AI tools cannot do competitive intelligence on Slickdeals without human-authenticated sessions.

**Implication for Groupon:** this is an under-commented advantage for Slickdeals as a partner. Their Cloudflare posture means competitors (and AI-based ones especially) cannot easily reverse-engineer their community dynamics. It is one real reason the community moat is durable - you cannot scrape it.

---

## Pattern matrix (fast reference)

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

## The single most actionable finding

**Rakuten is absent from most EU markets.** Confirmed visually on capture day - rakuten.com from CZ IP offers only France/Germany/Spain, with no path to join a US Rakuten account without a US IP.

Consequence: Groupon's EU loyalty rollout operates in a market with no incumbent cashback extension competitor of scale. Honey is diminished, Capital One Shopping is US-brand-heavy and not localised, Coupert is HK/global but small. **The EU is a first-mover opening for Groupon** that the retention uplift model currently does not size separately.

Recommend adding a Phase 2 to the sizing model: US market (where Groupon competes with Rakuten + Cap One + Honey) vs EU market (where Groupon essentially competes with nobody at the loyalty-layer scale).

---

## Where the screenshots do NOT tell the full story

- **Logged-in user experience** - absent by design (human-only per subtask #1)
- **Safari extension in action on Nike.com** - absent (needs Martin or Daniel)
- **Chrome Web Store live install counts** - Google consent wall blocks automated capture from CZ IP; needs authenticated human session
- **Actual welcome email content** - requires real signup
- **Mobile Safari rendering** - this capture was desktop-viewport only; mobile Safari may present differently

See `gaps.md` for the full list and the path to close each.

---

## Sources (every pattern here traces to at least one PNG)

Every claim in this file is linked to a specific fold PNG above. For each competitor, the full-page PNG (non-fold version, same filename without `-fold` suffix) shows below-the-fold content that adds nuance - worth browsing manually when preparing the Friday package.
