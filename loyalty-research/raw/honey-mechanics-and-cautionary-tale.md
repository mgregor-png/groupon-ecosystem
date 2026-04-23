# PayPal Honey - Mechanics + Trust Collapse Teardown
*Source: startup-competitors / Honey forensic | 2026-04-21*

---

## 1. TL;DR

PayPal Honey is simultaneously the best distributed coupon/loyalty extension on mobile (auto-bundled with the PayPal app on iOS across 10 countries including US/CA/UK/AU/DE/FR/NL/IT/ES/IN) and the most-damaged trust brand in the category. A December 2024 YouTube expose by MegaLag alleging commission hijacking and suppressed coupons triggered a sustained user exodus: from a Chrome peak of 20M in late 2024 to 12M by end of 2025 (a 40% loss in 12 months). [Data - 9to5Google Dec 31 2025]

Between Jan 12 - Jan 17, 2026, three major affiliate networks (Rakuten Advertising, Impact.com, Awin) removed or suspended Honey, cutting off access to thousands of retail partners - including ~2,000 clients from Rakuten alone. [Data - ppc.land, Affiverse, Jan 2026]

A consolidated class action is live: In Re PayPal Honey Browser Extension Litigation, N.D. Cal. Judge Beth Labson Freeman. The original complaint was dismissed without prejudice (Nov 2025); a 101-page Second Amended Consolidated Class Action Complaint was filed Jan 5, 2026 with 10+ named plaintiffs (content creators, not consumers), seeking damages over $5M. [Data - Cohen Milstein, Orrick, Jan 2026]

PayPal's defense: "Honey follows industry rules and practices, including last-click attribution." [Data - The Verge, 2025] PayPal on Jan 12, 2026 publicly acknowledged "problematic code" and said it had been disabled. [Data - Wikipedia Jan 2026]

**For Groupon**: Honey's distribution playbook (PayPal app bundling into Safari iOS) is worth studying and copying; Honey's product mechanics (Gold points, Droplist, auto-apply) are worth copying where transparent; Honey's trust posture (opaque merchant partnerships, last-click cookie overwrites, private-code scraping) is a blueprint for what NOT to do. The cautionary lesson is single-sentence: **every loyalty mechanic must be transparently user-positive - if a user learns how the flywheel actually works and feels cheated, the whole thing unwinds faster than it grew.**

---

## 2. The mechanics (20-point teardown, pre- and post-scandal)

### Signup + onboarding
1. **Signup flow**: Standalone signup at joinhoney.com is still possible (Chrome/Edge/Firefox/Safari desktop extension install). But the default distribution path on mobile is now PayPal app -> "Deals" tab -> enable Honey Safari extension. The Safari extension cannot be removed independently of the PayPal app, which heise.de flagged in 2024-2025 as a dark pattern. [Data - help.joinhoney.com, heise.de]
2. **Welcome bonus**: 500 Honey Gold ($5 value), earned by making an eligible purchase at a designated "welcome bonus" store within a time window. This is NOT a cash bonus on signup - it's a conditional promise that requires a purchase. [Data - moneysmylife.com, joinhoney.com]
3. **Referral**: $5 per friend who signs up and makes a first purchase, capped at $1,000. Referrals are cash (paid as USD/PayPal credit), not points. [Data - moneysmylife.com]
4. **Onboarding email cadence**: Not publicly documented. [Data gap]
5. **Push strategy pre-scandal (before Dec 2024)**: Aggressive YouTube creator sponsorships (MrBeast, Linus Tech Tips, Marques Brownlee, Markiplier, etc.). Creator promos were the primary acquisition channel. [Data - Newsweek, Wikipedia]
6. **Push strategy post-scandal**: YouTube creator sponsorships functionally dead - creators are the named plaintiffs in the class action. PayPal app bundling on iOS remains the primary distribution. No observable marketing ramp-up. [Opinion]

### Core product
7. **Auto-coupon success rate**: Coupert's third-party test (2025) measured Honey at 33.33% success rate vs Coupert at 72.92% on the same basket. [Data - Coupert research, 2025 - note: Coupert is a competitor so treat as biased, but the differential is large enough to be directionally credible]
8. **Coupon suppression**: MegaLag Part 2 showed Honey allegedly prioritized merchant-approved codes over genuinely-best codes. Ben Edelman's contractual analysis (independent Harvard/legal scholar) confirms Honey contractually agrees with some merchants to suppress better codes. [Data - benedelman.org, MegaLag]
9. **Private code scraping**: Dec 2025 reporting (and MegaLag Part 2) alleged Honey scrapes codes users manually enter (employee codes, refund codes, one-time targeted codes) and redistributes to its full user base, refusing takedown unless the merchant partners with Honey. [Data - MegaLag Part 2, 9to5Google Dec 22 2025]
10. **Droplist (price tracking)**: Save items -> choose tracking duration 30/60/120 days -> set target price -> Honey emails when price drops. Supports Amazon, Macy's, Target, Walmart, Lowe's, Sephora and others. Multi-store comparison for identical items. Solid, uncontroversial feature. [Data - joinhoney.com/features/droplist]
11. **Price comparison at PDP**: Honey shows Amazon price vs alternate retailers on product pages. Uncontroversial feature. [Data - joinhoney.com]
12. **Honey Gold earn**: Varies by merchant, typically 1-10% of purchase value in points. 100 points = $1 (so 1 point = $0.01). Double-points promos exist. "ExclusiveOffers" yield higher earn rates. [Data - help.joinhoney.com]
13. **Honey Gold pending window**: 60-90 days before points clear and become redeemable - much longer than Coupert (7-15 days) or Rakuten (quarterly payouts). Long pending window benefits Honey's float and increases breakage. [Data - Coupert comparison 2025]

### Distribution + platform
14. **Safari iOS extension - the bundling play**: Enabled via PayPal app on iOS 15+. Cannot be uninstalled independently. This is the single biggest distribution moat in the category. Available in US, CA, UK, AU, DE, FR, NL, IT, ES, IN as of 2025-2026. PayPal Rewards (Gold points redemption) remains US-only. [Data - help.joinhoney.com]
15. **iOS App Store rating**: PayPal Honey app rated 4.8/5 on 2,400+ reviews (2025-2026 data). Note: the app store entry captures users who installed Honey deliberately - not the larger population who got it via PayPal app bundling. [Data - App Store]
16. **User count trend (Chrome)**: 20M peak late-2024 -> 17M Jan 2025 (3M lost in 2 weeks) -> 16M Mar 2025 -> 14M Jul 2025 -> 13M Dec 2025 -> 12M end-Dec 2025. ~40% loss in 12 months. [Data - 9to5Google tracking series, ppc.land]
17. **iOS trend**: No public data showing iOS user exodus at the same rate. The PayPal app bundling likely insulates iOS from the Chrome freefall - users who got Honey via PayPal app bundling often don't know they have it. This is the distribution asymmetry that matters for Groupon. [Opinion / Data gap - needs verification]

### Economics + stakeholders
18. **Merchant economics**: Honey takes 0.5-10% commission on partner merchant sales, up to 20% on luxury categories. [Data - thestrategystory.com, feedough.com]
19. **Merchant coverage gap**: MegaLag Part 2 revealed Honey had codes for 181,000 stores but only ~35,000 had affiliate partnerships - meaning 146,000 stores appeared on Honey without consent. [Data - MegaLag Part 2, Dec 2025]
20. **Acquisition cost / channel mix today**: YouTube creator channel is effectively dead. App-bundle distribution via PayPal is the dominant ongoing acquisition path. PayPal does not break out Honey revenue in 10-K/10-Q segments - it rolls into "Value Added Services" (~$3.4B in FY2025 total, not Honey-specific). [Data - PayPal Q4 2025 earnings press release, Feb 3 2026]

---

## 3. Honey Gold deep dive (points, breakage, redemption)

### Point mechanics
- **Earn rate**: Variable 1-10% of purchase value. Double-points promos common on partner-of-the-week pushes. [Data - help.joinhoney.com]
- **Point-to-dollar ratio**: 100 Honey Gold = $1.00. Minimum redemption 1,000 points ($10 gift card). [Data - help.joinhoney.com]
- **Pending window**: 60-90 days. [Data - Coupert comparison 2025]
- **Expiration**: PayPal Rewards points expire if user does not earn 10+ points within any rolling 365-day window. Some terms also allow PayPal to zero out points after 12 months of full account inactivity. [Data - paypalobjects.com Gold program T&Cs]

### Redemption options (US only)
- e-Gift cards starting at 1,000 points = $10 - partners include Nordstrom, Sephora, eBay, Walmart, Target, Amazon and others. [Data - help.joinhoney.com]
- Redeem as statement credit / PayPal balance. [Data - help.joinhoney.com]
- Historically Honey also advertised "real gold" redemption (from a 2015 tweet - likely deprecated, treat as historical). [Data - X/Twitter 2015]
- Once an e-gift card order is submitted, it is auto-activated and cannot be cancelled or exchanged. This is an irreversibility guard that reduces user-initiated reversal but also traps users who misclicked. [Data - help.joinhoney.com]

### Breakage (value Honey keeps because users don't redeem)
- **Expected breakage**: HIGH. Three load-bearing mechanics drive this:
  - Long 60-90 day pending window (users forget)
  - 365-day earn-at-least-10-points-or-lose-everything rolling rule (one inactive year zeros balance)
  - $10 minimum redemption threshold (many users accumulate $3-8 and never redeem)
  - Account closure forfeits all points immediately ("not your property, not money, no value prior to redemption" per terms) [Data - joinhoney.com/terms]
- **Estimate**: Industry cashback breakage typically 15-30%. Honey's structure likely at the high end of that range (20-30%). [Estimate - no public Honey-specific breakage data]
- Community reports (PayPal Community forum, MoneySavingExpert forum) document users whose Gold balances have disappeared without explanation. [Data - paypal-community.com, moneysavingexpert.com]

### Strategic read
Honey Gold is more restrictive than Rakuten (Rakuten pays cash via PayPal/check quarterly with no earn-threshold). It's also more restrictive than Coupert (Coupert pays cash via PayPal in 7-15 days). Honey's points system is optimized for **PayPal float + breakage**, not user value. This is important: it is one of the reasons why, even before the scandal, sophisticated deal hunters preferred Rakuten or Capital One Shopping.

---

## 4. Safari iOS extension via PayPal bundling - the distribution playbook

This is the single most important section for Groupon strategy.

### The mechanic
1. User downloads the PayPal app (for the wallet - PayPal has ~430M active accounts globally, ~200M+ iOS). [Data - PayPal statistics 2026]
2. PayPal app contains the Honey Safari Extension as a bundled component.
3. User opens PayPal app -> taps "Deals" tab -> is prompted to enable Honey Safari extension (the extension itself is already installed as part of PayPal).
4. Enabling requires granting Safari extension permissions (access to all websites). This is the only user-action gate.
5. Once enabled, Honey auto-pops in Safari whenever the user hits a supported retailer checkout.
6. **Critical**: Honey cannot be uninstalled separately from the PayPal app. To remove it, user must uninstall the entire PayPal app. [Data - Apple Community forum, heise.de]

### Why it works (copy this)
- **Zero-friction distribution**: Users don't install Honey deliberately; they install PayPal deliberately. Honey is a free rider on PayPal's wallet distribution.
- **Breadth of countries**: 10 countries (US, CA, UK, AU, DE, FR, NL, IT, ES, IN) - one of the widest Safari iOS coupon extension footprints. [Data - help.joinhoney.com]
- **Activation decoupled from install**: The install happens silently when PayPal updates; activation is the only user decision. This means activation rate is the key funnel metric PayPal cares about, not install rate.
- **Insulation from Chrome exodus**: A user who enabled Honey on iOS through PayPal often doesn't know they have Honey. They can't "uninstall Honey" the way a Chrome user can with one click. This is probably why iOS user counts aren't falling at Chrome-pace. [Opinion - strong]

### Why it's controversial
- German tech press (heise.de) flagged the forced bundle as anti-consumer. [Data - heise.de]
- Apple users in Apple Community forums complain they can't remove Honey. [Data - discussions.apple.com]
- The bundle makes it impossible for users to opt out of Honey while remaining PayPal users - a form of tying that Apple's own App Store guidelines don't explicitly prohibit but that raises consumer-rights flags. [Opinion]

### Activation rate
- **Public data**: None found. [Data gap]
- **Directional inference**: If activation were high, PayPal would likely disclose it in investor materials. It isn't disclosed, which suggests activation is moderate-at-best. The "Deals" tab in the PayPal app exists partly to drive activation, suggesting PayPal sees it as a work-in-progress funnel. [Opinion]

### Groupon implication
A Groupon Safari extension bundled with the Groupon app on iOS would replicate the most defensible piece of Honey's moat (forced-distribution bundling). Groupon has ~8M US iOS DAUs (estimate - verify) and ~25M global DAUs. That's a smaller base than PayPal but large enough to matter, AND Groupon already has retailer depth and merchant relationships that Honey needs to manufacture. Honey is vulnerable precisely because it needs 181,000 merchants to look comprehensive but only has 35,000 paying partners. Groupon's merchant network is inverse: narrower but fully contracted.

---

## 5. The 2024-2026 trust collapse - chronology, allegations, exodus numbers

### Chronology
- **Dec 21, 2024**: MegaLag publishes "Exposing the Honey Influencer Scam" on YouTube. Core allegations: (1) Honey hijacks affiliate cookies at checkout via last-click attribution, stealing commission revenue from YouTube creators who promoted the products; (2) Honey suppresses better coupons in favor of merchant-approved codes; (3) Honey is a "scam" that makes its money by taking from creators and shoppers, not by finding better deals. Video goes viral. [Data - MegaLag YouTube, Wikipedia]
- **Dec 22, 2024**: First wave of coverage - TechCrunch, The Verge, 9to5Google, Newsweek. [Data - multiple]
- **Dec 29 2024 - Jan 5 2025**: First class-action filings. Kristensen Law Group files on behalf of creators seeking $5M+ damages. Multiple additional firms (DiCello Levitt, Lieff Cabraser, Gibbs Mura, Cohen Milstein) file in parallel. [Data - classlawgroup.com, dicellolevitt.com, lieffcabraser.com]
- **Early Jan 2025**: Ryan Hudson, Honey co-founder, breaks silence. Defends Honey's practices, says the extension saved consumers billions. PayPal issues statement: "Honey follows industry rules and practices, including last-click attribution." [Data - Wikipedia, The Verge]
- **Jan 2025**: 3M Chrome users gone in ~2 weeks (20M -> 17M). [Data - 9to5Google Jan 3 2025]
- **Mar 2025**: Google updates Chrome Web Store policy to prohibit extensions from claiming affiliate commissions without providing user discounts. Honey modifies its extension to stop claiming commissions on no-discount transactions. User count: 16M. [Data - 9to5Google Mar 31 2025, GIGAZINE Apr 2 2025]
- **May 2025**: 4M+ users gone (down to 16M). [Data - 9to5Google]
- **Jul 2025**: Down to 14M. [Data - 9to5Google Jul 7 2025]
- **Nov 2025**: Judge Beth Labson Freeman dismisses the initial complaint without prejudice - ruled plaintiffs didn't sufficiently identify injury. Leave to amend granted. [Data - Orrick, thePMA]
- **Dec 21, 2025**: MegaLag Part 2 - "He Released Part 2 of the Honey Investigation." New allegations: Honey scraped private codes (employee codes, one-time refund codes) and redistributed them; refused takedown unless merchants partnered with Honey; 146,000 of 181,000 stores on Honey have no affiliate relationship. Triggers fresh wave of uninstalls. [Data - YouTube, 9to5Google Dec 22 2025]
- **Dec 31, 2025**: User count hits 12M (down 8M from peak, ~40% loss in 12 months). [Data - 9to5Google Dec 31 2025]
- **Jan 5, 2026**: Plaintiffs file Second Amended Consolidated Class Action Complaint - 101 pages, 10+ named plaintiffs (Ahntourage Media, Aaron Ramirez, Angry Snowboarder, Brevard Marketing, Red Beard Studios, Storm Productions, Gents Scents, Daniel Lachman, Justin Tech Tips, Stuber Holdings, Dan Becker LLC). Includes actual affiliate agreements with Bergdorf Goodman et al., documenting commission rates and qualifying-link definitions Honey allegedly violated. [Data - Cohen Milstein, lawfold.com]
- **Jan 12, 2026**: Rakuten Advertising terminates Honey, cutting off ~2,000 retail partners. PayPal public statement: "acknowledged problematic code in Honey, have disabled it." PayPal blames "legacy code implemented prior to its acquisition of Honey." [Data - Affiverse, ppc.land, Wikipedia]
- **Jan 17, 2026**: Impact.com removes Honey from Discovery Marketplace, suspends the account. CEO David Yovanno cites "attribution non-compliance." [Data - ppc.land]
- **Jan 21, 2026**: Awin confirms "breaches confirmed" and suspends payments, blocks Honey from new advertiser programs. Stops short of full removal. [Data - hellopartner.com]

### The core allegations (what Honey allegedly did)
1. **Commission hijacking via last-click attribution**: When a user who had clicked a creator's affiliate link arrived at checkout, Honey would open its popup, get the user to click it (often for a "no better code found" popup), and that click overwrote the creator's affiliate cookie with Honey's. Honey then collected the commission. MegaLag's showcase example: a $35 NordVPN affiliate commission redirected from a creator to Honey, user got $0.89 Honey Gold back. [Data - MegaLag]
2. **Suppressed coupons**: Honey had contractual agreements with some merchants to NOT surface codes better than a merchant-approved default. Users who saw "no better code found" were often one click away from real better codes on RetailMeNot. [Data - MegaLag, Ben Edelman analysis]
3. **Private-code scraping (MegaLag Part 2)**: Honey captured codes users typed manually and rebroadcast them to all Honey users - even when merchants asked for takedown. Codes intended for employees / refunds / retention offers leaked at scale. [Data - MegaLag Part 2, Dec 2025]

### User exodus numbers (Chrome only)
| Date | Users | Loss from peak |
|---|---|---|
| Pre-Dec 2024 | 20M | 0 |
| Jan 3, 2025 | 17M | -3M |
| Mar 31, 2025 | 16M | -4M |
| Jul 7, 2025 | 14M | -6M |
| Dec 22, 2025 | 13M | -7M |
| Dec 31, 2025 | 12M | -8M |
[Data - 9to5Google tracking series]

### iOS trend
No equivalent tracking data exists for iOS Safari. Inference: iOS losses are likely much smaller because (a) PayPal app bundling means many users don't know they have Honey, (b) the uninstall path requires removing the PayPal wallet, which most users won't do. [Opinion - high-confidence]

---

## 6. What Honey still does well (mechanics worth copying)

1. **Droplist price tracking** - clean, well-designed, gives users genuine value with no trust cost. [Data]
2. **PayPal app bundling into Safari iOS** - the single best mobile-coupon distribution playbook extant. Groupon should seriously consider replicating this with Groupon app -> Groupon Safari extension. [Opinion]
3. **Country breadth for Safari iOS** - 10 countries supported for the Safari extension is unmatched in the category. [Data]
4. **Referral program simplicity** - $5 per friend, cash, no points, cap at $1,000. This is the right shape for viral acquisition. [Data]
5. **Auto-pop at checkout** - Honey's popup timing (appears at first checkout page) is well-tuned. When it works, the apply-code flow is 1-click. The UX itself is good; the trust problem is that the code it applies isn't always the best available. [Opinion]
6. **In-app Deals tab inside PayPal** - embedded browsing inside the wallet app keeps discovery-to-checkout in one surface. [Data]
7. **Brand recognition at peak** - despite decline, Honey remains the most-recognized consumer coupon brand in the US (pre-scandal brand equity was massive, spent on creator sponsorships). [Opinion]

---

## 7. Lessons for Groupon (PRIMARY)

**The meta-lesson**: every mechanic must be transparently user-positive. If your loyalty flywheel has a mechanic that only works if users don't understand it, the mechanic is a liability waiting for a viral expose. MegaLag's video would have been impossible if Honey's economics had been transparent.

### Load-bearing mechanics on trust (copy carefully, instrument honestly)

1. **Attribution model disclosure**: If Groupon's extension is going to claim an affiliate commission on a sale, the user must see a clear "Groupon is earning from this purchase, this is how we fund your cashback" banner at checkout. No silent cookie overwrites. Build this as a core UX pattern from day one - it becomes a credibility moat that Honey cannot retrofit.
2. **Coupon ranking must be by success rate, not merchant relationship**: Publish the ranking logic. If Groupon has merchant partners who can reject codes being shown, disclose which retailers have this arrangement and why. Make it impossible to accuse Groupon of hiding better codes.
3. **Cashback liquidity**: Pay cash, not points. If points, minimum redemption under $5, pending window under 14 days, clear in-app countdown, no silent expiration. Honey's 60-90 day pending + 365-day inactivity forfeit rule is the breakage machine that Coupert and Capital One Shopping have built businesses on beating.
4. **Referral in cash, not points**: $5 cash per referral, paid immediately to PayPal/bank, no purchase requirement. Matches Honey's best mechanic.
5. **Safari iOS extension bundled with Groupon app**: This is the single most defensible move. Groupon app -> "Deals" tab -> enable Safari extension. Same pattern as Honey, but with full activation disclosure (user can disable/remove the extension independently if they want - that is the trust-positive version of the bundle).
6. **Private-code handling**: Do NOT scrape codes users type. This alone is a time-bomb waiting to explode (MegaLag Part 2 is what took Honey from 14M to 12M in six weeks). Design the code database to accept only codes from verified merchant feeds or affiliate network feeds - never from user behavior.
7. **Merchant relationship disclosure**: Publish the list of merchants Groupon has active affiliate/partnership agreements with. If a retailer is in the extension, show the user the provenance. Honey failed here: 146K of 181K stores had no affiliate relationship, which is why the extension looked comprehensive but was structurally fragile.

### Distribution lessons
8. **Bundle via app, activate via user action**: The best distribution is what's already in the user's pocket. Groupon app install -> Safari extension pre-installed but not active -> explicit activation prompt in-app.
9. **Country breadth matters for Safari iOS**: 10 countries took Honey years to unlock. Every country has its own merchant feed and affiliate network. This is defensible if done well.
10. **Don't rely on YouTube creator sponsorships as your primary acquisition channel**: That channel broke Honey. Creators are now the plaintiffs. Diversify acquisition before scaling.

---

## 8. What Groupon should NOT copy

1. **Silent cookie overwrites / last-click hijack**: This is the criminal mechanic. Even if "industry standard" is PayPal's legal defense, it is user-negative and transparently so in hindsight. Never do this.
2. **Opaque merchant ranking**: Do not let merchants pay to have their codes show when better codes exist. This is what MegaLag Part 1 destroyed Honey on.
3. **Scraping user-typed private codes**: This is what MegaLag Part 2 destroyed Honey on. Design it out of the system.
4. **Bundle-lock (can't uninstall extension without uninstalling wallet)**: This is anti-consumer and a vulnerability to App Store policy changes. Let users remove the extension independently.
5. **Long pending windows (60-90 days)**: This is breakage optimization. Competitors do 7-15 days and advertise the difference.
6. **365-day inactivity forfeiture with no warning**: This is breakage theater. Do at least a 30/60/90-day warning email cadence and a 2+ year grace period.
7. **"Not your property, not money, no value prior to redemption" language in terms**: This exact phrasing is in Honey's T&Cs and it's exactly the language that gets cited in class actions. Write terms that could be read aloud in court without embarrassment.
8. **Defending the legacy after exposure**: PayPal's "legacy code from pre-acquisition" framing in 2026 is what makes the situation worse - it concedes the code was bad but tries to shift blame backwards. If anything about Groupon's mechanic is questionable, fix it proactively and credit the fix publicly. Never wait for a MegaLag-equivalent to force it.

---

## 9. Data gaps

1. **Honey iOS Safari user count trend** - No public tracking series exists equivalent to the Chrome Web Store number. Needs estimation from PayPal app install data (if available via Sensor Tower / data.ai) and an assumed activation rate.
2. **Honey iOS Safari activation rate** - Not publicly disclosed. Could be inferred from any leaked PayPal investor decks or from Honey Gold redemption density by platform.
3. **Honey-specific revenue contribution to PayPal** - Not broken out in 10-K/10-Q filings. Rolls into "Value Added Services" (~$3.4B FY2025 total). Needs estimation from category benchmarks.
4. **Honey breakage rate** - Not disclosed. Industry benchmark 15-30%; likely Honey is at upper end given T&Cs structure.
5. **Onboarding email cadence** - Not publicly documented; requires signup-and-observe capture exercise.
6. **Actual merchant commission payments to Honey** - Known only at aggregate (0.5-10%, up to 20% luxury). No per-merchant disclosure.
7. **Migration evidence from Honey to Rakuten/Capital One Shopping/Coupert** - No quantified migration data found. Rakuten and Capital One Shopping haven't published "new user spike" disclosures in 2025-2026 quarterly reports that would confirm inflow from Honey. [Estimate: migration is happening but at smaller scale than 8M-lost-Honey-users because many users are going cold rather than switching]

---

## 10. Red flags / Yellow flags

### Red flags (high severity)
- **Class action is live and escalating**: Second Amended Complaint has 10+ named plaintiffs and 101 pages of evidence including actual merchant contracts. Dismissal in Nov 2025 was without prejudice; the amended complaint specifically addresses the injury-pleading deficiency the judge flagged. This is not dying.
- **Three major affiliate networks cut Honey off in 5 days (Jan 12-17, 2026)**: Rakuten (full removal), Impact.com (removal from Discovery Marketplace + account suspend), Awin (payments suspended, blocked from new programs). This is not a PR crisis; it's a structural business crisis. Honey's merchant pool is shrinking week-over-week.
- **PayPal's public admission (Jan 12, 2026)**: "Problematic code in Honey, have disabled it." This is an admission against interest that strengthens plaintiffs' case.
- **No leadership consolidation response**: No PayPal executive has been fired or publicly accountable for the Honey situation. The co-founder Ryan Hudson defended the practices. PayPal leadership has been opaque.

### Yellow flags (medium severity)
- **Honey Gold T&Cs language is class-action bait**: "Not your property, not money, no value prior to redemption" is the kind of phrasing that looks fine in normal operations and catastrophic in front of a jury.
- **Auto-coupon success rate of 33% per Coupert**: Even accounting for competitor bias, this is structurally weak. Users are one install away from a better tool.
- **iOS bundling is a regulatory risk**: German press (heise.de) has flagged it. Apple could change App Store policies on tying. EU DMA might touch it.
- **Chrome Web Store policy change (Mar 2025) forced a mechanic change**: Google already reshaped Honey's monetization once. They could do so again.
- **PayPal's "legacy code" deflection blames the pre-acquisition Honey team**: This is a contradiction with Ryan Hudson's (co-founder) public defense. The messaging is not aligned - two different stories from PayPal leadership and Honey founder.

---

## 11. Sources

### Tier 1 (SEC filings, court filings, official sources)
- [PayPal Reports Fourth Quarter and Full Year 2025 Results (Feb 3, 2026)](https://newsroom.paypal-corp.com/2026-02-03-PayPal-Reports-Fourth-Quarter-and-Full-Year-2025-Results)
- [PayPal Q3 2025 Earnings Presentation (Oct 28, 2025)](https://s205.q4cdn.com/875401827/files/doc_financials/2025/q3/PYPL-3Q-25-Earnings-Presentation.pdf)
- [In Re PayPal Honey Browser Extension Litigation - Cohen Milstein case page](https://www.cohenmilstein.com/case-study/in-re-paypal-honey-browser-extension-litigation/)
- [PayPal Secures Another Victory in Consolidated Honey Browser Extension Cases - Orrick (Dec 2025)](https://www.orrick.com/en/news/2025/12/paypal-secures-another-victory-in-consolidated-honey-browser-extension-cases)
- [DiCello Levitt Files Class Action Lawsuit Against PayPal](https://dicellolevitt.com/dicello-levitt-files-class-action-lawsuit-against-paypal-for-alleged-theft-of-affiliate-marketing-commissions/)
- [Lieff Cabraser - Honey/PayPal Commission Theft Allegations](https://www.lieffcabraser.com/consumer/honey-paypal/)
- [PayPal Gold Program Terms and Conditions (PDF)](https://www.paypalobjects.com/marketing/ua/pdf/US/en/pp-gold-program-tnc.pdf)
- [Honey Terms of Use](https://www.joinhoney.com/terms)
- [PayPal Completes Acquisition of Honey (Jan 6, 2020)](https://newsroom.paypal-corp.com/2020-01-06-PayPal-Completes-Acquisition-of-Honey)

### Tier 2 (reputable press)
- [Honey extension loses 3 million Chrome users - 9to5Google Jan 3, 2025](https://9to5google.com/2025/01/03/honey-paypal-chrome-extension-lost-users/)
- [Honey has now lost 4 million Chrome users - 9to5Google Mar 31, 2025](https://9to5google.com/2025/03/31/honey-extension-users-dropped-chrome-march-2025/)
- [Honey just lost a million more Chrome users - 9to5Google Jul 7, 2025](https://9to5google.com/2025/07/07/honey-just-lost-a-million-more-chrome-users/)
- [Honey accused of sketchy user data practices - 9to5Google Dec 22, 2025](https://9to5google.com/2025/12/22/honey-user-data-practices-reports/)
- [Honey has lost 8 million Chrome users - 9to5Google Dec 31, 2025](https://9to5google.com/2025/12/31/honey-chrome-users-fraud/)
- [Honey drops to 14 million Chrome users - ppc.land](https://ppc.land/honey-drops-to-14-million-chrome-users-amid-ongoing-affiliate-scandal/)
- [Impact.com kicked Honey off its network - ppc.land](https://ppc.land/impact-com-just-kicked-honey-off-its-network-for-hiding-cookie-theft/)
- [Awin confirms Honey violated affiliate policies - ppc.land](https://ppc.land/awin-confirms-honey-violated-affiliate-policies-suspends-payments/)
- [Honey loses access to 2,000 clients after Rakuten termination - ppc.land](https://ppc.land/honey-loses-access-to-2-000-clients-after-rakuten-network-termination/)
- [Tech giant PayPal accused of fraud over Honey - techxplore.com](https://techxplore.com/news/2025-01-tech-giant-paypal-accused-fraud.html)
- [Honey browser extension promoted by MrBeast - Newsweek](https://www.newsweek.com/honey-coupon-browser-extension-mrbeast-youtube-influencer-2007484)
- [PayPal to acquire Honey for $4B - TechCrunch (Nov 2019)](https://techcrunch.com/2019/11/20/paypal-to-acquire-shopping-and-rewards-platform-honey-for-4-billion/)
- [Shopping plugin Honey continues to be installed with PayPal on iPhones - heise.de](https://www.heise.de/en/news/Shopping-plugin-Honey-continues-to-be-installed-with-PayPal-on-iPhones-10234936.html)
- [The Honey Chrome extension is bleeding users - Chrome Unboxed](https://chromeunboxed.com/the-honey-chrome-extension-is-bleeding-users-after-being-labeled-as-a-scam/)
- [PayPal Q2 2025: Branded growth strong - Payment Expert](https://paymentexpert.com/2025/07/30/paypal-q2-2025-earnings/)

### Tier 3 (affiliate/industry press, MegaLag analyses, legal blogs)
- [Rakuten Advertising Becomes First Major Network to Remove PayPal Honey - Affiverse](https://www.affiversemedia.com/rakuten-advertising-becomes-first-major-network-to-remove-paypal-honey-following-attribution-controversy/)
- [Megalag & Honey Saga Update - Affiverse](https://www.affiversemedia.com/megalag-honey-saga-update-detection-evasion-testing-manipulation-claims-spotlight-in-latest-video/)
- [Honey Investigation Deepens: Part Two of MegaLag - Affiverse](https://www.affiversemedia.com/honey-investigation-deepens-what-part-two-of-megalag-reveals-about-browser-extension-risks-for-affiliate-programs/)
- [The Official Honey Response to Cookie Hijacking - Affiverse](https://www.affiversemedia.com/the-official-honey-response-to-cookie-hijacking/)
- [Ben Edelman - Honey's Contractual Breaches and Value (or Lack of It) to Merchants](https://www.benedelman.org/honey-breaches/)
- [Awin Takes The Middle Road For Their PayPal Honey Notice - Affiverse](https://www.affiversemedia.com/awin-takes-the-middle-road-for-paypal-honey-notice/)
- [Awin Says 'Breaches Confirmed' - Hello Partner](https://hellopartner.com/2026/01/21/awin-says-breaches-confirmed-sets-compliance-collaboration-with-honey/)
- [Honey Terminated from Affiliate Networks - Revel Marketing](https://www.revelinteractive.com/blogposts/honey-terminated-from-affiliate-networks-what-brands-should-know)
- [Gibbs Mura - PayPal Honey Browser Extension Scam Lawsuit](https://www.classlawgroup.com/honey-browser-extension-scam-lawsuit)
- [Influencers strike back with detailed contracts - ppc.land](https://ppc.land/influencers-strike-back-with-detailed-contracts-showing-honey-violated-terms/)
- [Honey Lawsuit 2026: Full Breakdown - lawfold.com](https://lawfold.com/honey-lawsuit/)
- [Key Takeaways from Honey Browser Lawsuit Dismissal - ThePMA](https://thepma.org/key-takeaways-from-honey-browser-lawsuit-dismissal/)
- [Coupert vs Honey 2025 testing](https://www.coupert.com/research/coupert-vs-honey-which-coupon-extension-performs-best-in-2025)
- [EcomScout Investigation - PayPal Honey Dataset](https://ecomscout.com/reports/paypal-honey-dataset)
- [How PayPal's Honey manipulated coupon codes - ppc.land](https://ppc.land/how-paypals-honey-manipulated-coupon-codes-and-diverted-affiliate-commissions/)
- [PayPal Honey - Wikipedia](https://en.wikipedia.org/wiki/PayPal_Honey)

### Honey-owned pages (for mechanics documentation)
- [Honey Gold / PayPal Rewards feature page](https://www.joinhoney.com/features/honeygold)
- [Redeeming PayPal Rewards for Gift Cards - help.joinhoney.com](https://help.joinhoney.com/article/85-redeem-paypal-rewards-for-gift-cards)
- [Honey Mobile Safari Extension - help.joinhoney.com](https://help.joinhoney.com/article/350-honey-mobile-safari-extension)
- [What is the PayPal Honey mobile Safari extension? - PayPal help](https://www.paypal.com/us/cshelp/article/what-is-the-paypal-honey-mobile-safari-extension-help593)
- [Droplist - joinhoney.com/features/droplist](https://www.joinhoney.com/features/droplist)
- [What is Droplist? - help.joinhoney.com](https://help.joinhoney.com/article/79-what-is-droplist)
- [PayPal Honey on App Store](https://apps.apple.com/us/app/paypal-honey-coupons-rewards/id1358499588)

### MegaLag videos (primary source)
- [Exposing the Honey Influencer Scam (Dec 21, 2024) - MegaLag YouTube](https://www.youtube.com/watch?v=vc4yL3YTwWk) [URL reconstructed from references - confirm original]
- [He Released Part 2 of the Honey Investigation (Dec 21, 2025) - YouTube](https://www.youtube.com/watch?v=rD1t6LMIYVE)
- [Ludwig finds out he got scammed by Honey - YouTube](https://www.youtube.com/watch?v=wcBrylnKP8A)
