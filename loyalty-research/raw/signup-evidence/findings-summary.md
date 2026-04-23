# Signup-Evidence Findings Summary - 2026-04-21

**Source:** 3 parallel AI research agents, public-web only (pre-auth pages), 2026-04-21 afternoon.
**Geo:** CZ IP. All hard geoblocks + 404s flagged as data gaps.
**Full raw:** `raw/signup-evidence/{rakuten,capone,honey}/public-capture.md`

This summary rolls up the sharpest findings across all three competitors, grouped by whether they are (a) fact-checks against the existing `loyalty-mechanics-final.md` doc, (b) new mechanics worth copying, or (c) data gaps that still need resolution.

---

## A. Fact-check hits against the current final doc

Load-bearing claims that the AI research changed. Update §3.1, §3.2, §3.3 of `loyalty-mechanics-final.md` before Friday.

### A1. Rakuten welcome-vs-referral bonus is CONFLATED in the current doc

- **Final doc says:** "$50/$50 referral bonus, standard welcome $10" (from Rebecca §2.1) and refers to "$50 sign-up" multiple times
- **Reality (verbatim help-article):** Standard welcome is **$25 with 90-day qualifying threshold**. The $50/$50 is a **referral promo** currently live Apr 1 - Jun 30 2026 window. Different mechanics, different triggers.
- **Also:** A **$100 extension-install-gated bonus** exists separately: 3 x $35 qualifying purchases in 45 days, **disqualification clause if the user uninstalls the extension**. This is a distinct activation lever Rebecca's doc missed entirely.
- **Confidence:** High (verbatim from rakuten.com help CMS, CZ-IP-accessible)

### A2. Capital One $45 install anchor is NOT the current offer

- **Final doc says:** "$45 install incentive" throughout (sourced from millennialmoney.com, a review site)
- **Reality:** The current publicly visible offer is **$80/$80 referral with 90-day install-retention gate**. US-only, new-user-only, $1,900 referrer cap. Doctor of Credit's Feb 2026 historical list **has no $45 variant** - closest is Dec 2024 "$40 after $15 spend in 90 days".
- **A second mechanic found:** iOS App Store description advertises **$10 after $10 spend in 21 days** - a different gate entirely (purchase-conditioned not retention-conditioned).
- **Implication:** Drop "$45 anchor" from the headline and the sizing model. Replace with "$40-$80 industry install CAC range with retention OR purchase gates; targeted YMMV variants common".
- **Confidence:** High on "$45 not public"; Medium on "$45 never existed" (could be a targeted/YMMV offer Capital One does not publicise)

### A3. Honey Chrome user count is ~12M (not 13M)

- **Final doc says:** "13M Chrome users" (Rebecca §3.7)
- **Reality:** 9to5Google / Wikipedia show ~12M at end of Dec 2025. No April 2026 figure verifiable from CZ IP (Chrome Web Store blocked by Google consent redirect). **Honey's own homepage still displays a stale "17 million members and counting" badge** - itself a finding about Honey's reputation management.
- **Implication:** Update the number, keep the trend. Note the stale homepage badge as evidence of Honey's post-scandal posture.
- **Confidence:** High for 12M Dec 2025; Low for any April 2026 figure

### A4. Honey trust posture: silence, not accommodation

- **Final doc says:** Trust collapse is blueprint for what NOT to do.
- **New evidence:** **Zero post-scandal messaging** anywhere on joinhoney.com, help.joinhoney.com, or PayPal's Honey help pages. Terms of Use last updated **Jan 16, 2024 (US) / Feb 16, 2024 (EU)** - pre-scandal and still live. **No mention of MegaLag, class action, Jan 2026 Rakuten/Impact/Awin terminations, "problematic code" admission, or March 2025 Chrome Web Store policy change.** /how-it-works, /signup, /features, /how-honey-works all **404**. Only transparency language is a single "Ad Disclosure" footer + one sentence on the Gold page.
- **Leading indicator of consumer erosion:** **iOS App Store rating has dropped to 3.6/5 on 10K ratings** (forensic doc a year earlier had 4.8 / 2,400 ratings).
- **Implication:** Sharpens the "what NOT to do" card. Also validates the "this is a time-limited acquisition window" claim - Honey is not recovering, it is avoiding.
- **Confidence:** High

---

## B. New mechanics worth adding to the final doc

Patterns the AI sprint surfaced that deserve their own treatment in §4 Mechanic Cards or as inserts to §3 deep dives.

### B1. Rakuten "uninstall penalty" on extension bonus

The $100 extension-install bonus has a **disqualification clause if the user uninstalls the extension**. This is a sharp retention mechanic - Groupon Bucks could include a similar "cumulative balance resets if you uninstall" for the Safari extension bundle, which is honest AND sticky.

Candidate for Card 04 (Safari Extension Bundling) or a new card.

### B2. Capital One "currency mechanic hidden pre-auth"

CapOne deliberately hides 1 Credit = $1, the retailer list, and dollar bonus mechanics from the public pages. Everything is gated behind account creation. This is a **deliberate design choice** - forces signup before the user can evaluate the offer.

Groupon Bucks has a choice to make: transparent pre-auth (Rakuten style - visible value driver) or gated (CapOne style - signup lever). Card 02 (1:1 Soft Currency) should call this out explicitly.

### B3. Rakuten affiliate-data-sharing explicit clause

Rakuten's privacy policy includes a **verbatim clause explicitly naming the "unique ID assigned to track that your shopping originated from our Services"** plus **Global Privacy Control (GPC) honor**.

This is a **post-Honey transparency differentiator**. Groupon could write a cleaner, more explicit version than Rakuten's and use it as a trust marker.

Addition to Card 06 (Trust and Transparency).

### B4. Capital One dual-gate mechanics

Two different install incentives running in parallel: $80/$80 referral (retention gate) AND $10 after $10 spend (purchase gate). Targeting different user psychologies (referral = social; first-purchase = conversion).

Groupon Bucks could run a similar dual-gate: one generous referral, one low-friction first-purchase. Worth testing.

### B5. Honey "bundled but independently removable" recommendation

The heise.de dark-pattern flag on Honey: users cannot uninstall the Honey extension without uninstalling the PayPal wallet. This is the one thing Groupon should explicitly NOT copy from Honey's iOS Safari bundling.

Addition to Card 04 (Safari Extension Bundling).

---

## C. Data gaps that still need resolution

Ordered by whether Daniel's US capture closes them.

### Daniel-closable (chase priority)
- Rakuten homepage hero CTA + signup form fields + password rules + social sign-on
- Rakuten Chrome Web Store metrics
- Rakuten Big Fat Check live hero copy
- Rakuten+ invite-request flow
- CapOne homepage current offer headline verification ($80/$80 vs other)
- CapOne /how-it-works, /rewards, /gift-cards (404 for both CZ and likely US public - confirm)
- CapOne Chrome Web Store metrics
- CapOne first-logged-in UX (is "1 Credit = $1" visible)
- Honey Chrome Web Store current April 2026 count
- Honey iOS Safari extension activation flow via PayPal app
- Honey US homepage (is "17M members" badge still shown from US IP?)

### Not Daniel-closable (need internal / primary data)
- Honey iOS Safari extension user count trajectory (no tracking series exists)
- CapOne "1 Credit = $1" verification on any public page (confirmed absent from Feb 18 2026 privacy policy too)
- Rakuten US Rewards standalone P&L (hidden in Rakuten Group International segment)

---

## D. Process notes for the AI funnel appendix

All three agents ran in parallel via the Task tool with `general-purpose` subagents. Each agent:
- Had its own WebFetch/WebSearch tool allowance
- Was instructed to label [Data]/[Estimate]/[Assumption]/[Opinion] and flag data gaps
- Was forbidden from inventing numbers
- Wrote its own raw output file (audit trail preserved)
- Returned a short completion report, not the full transcript

The three raw files totalled ~9,000 words of verbatim public-page evidence captured in ~50 minutes of parallel runtime. Human-equivalent effort for the same scope would have been ~6-8 hours.

Agent prompts are in the respective raw files' "Prompts/queries log" sections. This rolls up into the AI funnel companion / Adam's transparency requirement.
