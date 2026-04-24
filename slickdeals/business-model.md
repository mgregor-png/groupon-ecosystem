# Slickdeals - Business Model Reverse Engineering

*For: Dusan, Rebecca, Groupon Product Leadership | Prepared by Martin with AI assistance | 2026-04-23*
*Classification: Confidential. Working document.*

---

## TL;DR

Slickdeals is not a deals site. It is a **community-owned curation engine monetised via affiliate commissions** with a thin marketplace skin. The moat is 25 years of forum-accumulated trust and a power-user economy where ~5% of users drive ~20% of activity. Everything else - app, extension, newsletter, AI layer - is distribution surface on top of the community.

For Groupon, the reverse-engineering question has three useful answers:
1. **What's replicable** (deal alerts, voting algorithm, soft-incentive rewards, mobile-first UX) - all achievable in-house.
2. **What's NOT replicable** (the 25-year forum, power-user economy, deal editor corps) - cannot be bought, built, or partnered around.
3. **Where they leak margin** (thin affiliate take, high content-moderation cost, weak cashback vs Rakuten, no Safari extension) - the gaps Groupon could exploit competitively.

Business-model sustainability score: **Strong on durability, weak on growth trajectory.** Profitable, habit-forming, low churn. But growth is now flat-to-modest (~5% MoM traffic), upper-funnel pivot is slow, and a PE-exit within 12-24 months will likely force a strategic shift. [Opinion - High confidence on durability, Medium on exit timing]

---

## 1. What they are

Slickdeals is a **user-generated deal-curation platform** where community members post deals, vote on them, and discuss them in threads. Deals with sufficient upvotes reach the "Front Page". Consumers browse the Front Page or set alerts. When they click a deal and buy, Slickdeals earns an affiliate commission from the merchant.

**Scale (2026 state):**
- 12M monthly active users [Data - Slickdeals corp, 2025]
- ~25M monthly visitors, >1B visits annually [Data - Similarweb via Slickdeals corp]
- 40% DAU/MAU ratio [Data - LA Business Journal, 2024] - exceptional for a consumer site; comparable to major social networks
- 80% direct traffic share [Data - Similarweb, Mar 2026] - strongest brand/habit signal in the competitive set
- 4:50 avg session duration, 4.05 pages/visit, 37.3% bounce rate [Data - Similarweb, Mar 2026]
- 14 visits per week per active app user [Self-reported, Slickdeals podcast 2026]
- 5M+ iOS + Android combined app installs [Data - Slickdeals corp]
- ~200-220 employees [Estimate - not directly confirmed, carried from prior research]
- Revenue: **$45M-$55M range, 2026 working estimate** [Estimate - from enactsoft, martini.ai, earlier research]

**Ownership:**
- Goldman Sachs Merchant Banking (West Street Capital Partners VII) + Hearst Corporation since June 2018 [Data - Bloomberg, PR Newswire, 2018]
- Prior owner: Warburg Pincus. Reported 2018 transaction value ~$500M [Data - Bloomberg, 2018]
- 8-year PE hold is at the long end of normal; expect exit signal in 12-24 months [Opinion]
- No public evidence of 2025 or 2026 sale [Assumption - GS/Hearst still hold as of Apr 2026]

---

## 2. How they attract traffic (acquisition)

Acquisition is almost entirely organic. Slickdeals spends very little on paid acquisition and instead relies on habit loops that drive direct traffic. This is the single most important fact about the business model.

### Channel mix (desktop + mobile web, Mar 2026) [Data - Similarweb]
- **Direct: ~80%** - users type slickdeals.net or open the app. This is the dominant channel by a wide margin.
- **Organic search: ~15%** - long-tail "[product] slickdeals" searches + "[retailer] coupon slickdeals" queries. SD ranks well for niche product threads.
- **Paid search: <2%** - minimal brand-term defence only.
- **Referral: ~2-3%** - primarily from forum posts on Reddit, Twitter, and affiliate partners.
- **Social: <1%** - present on TikTok/Instagram but not a meaningful acquisition channel.
- **Email / newsletter: tracked separately as direct** - weekly newsletter is a major re-engagement tool but not a new-user acquisition source.

### What drives direct traffic
- **Habit loop from deal alerts** - users set alerts on products / categories / retailers. Alert fires, user visits to buy. Loop compounds.
- **Front Page check-in behaviour** - users open the app "with their coffee" [Self-reported, podcast 2026]; ritual use rather than utility use.
- **Forum reply notifications** - when a deal a user commented on gets new replies or expires, they come back to check.
- **Newsletter as re-engagement** - Slickdeals sends daily / weekly digest emails to the registered base. This is direct traffic dressed as direct (user clicks email -> direct load).
- **Podcast and partnership marketing** - paid relationship with Mark Saltzman and similar consumer-tech podcasts drives brand awareness to extension installs specifically [Self-reported, podcast 2026; disclosed paid partnership]. Low-volume but high-intent.

### What does NOT drive significant traffic (important for what Groupon should / should not copy)
- Paid social acquisition - they don't really do it
- Influencer sponsorships at Honey's scale - they don't really do it
- SEO-programmatic (millions of landing pages) - they don't really do it
- App Store paid placement - they don't really do it

**Why this matters for Groupon:** Slickdeals has built a durable audience without the paid-acquisition treadmill that Honey, RetailMeNot, and Rakuten rely on. The input is community content; the output is direct traffic. That is a structurally more profitable model than paid-funnel competitors. Groupon's coupons traffic is similarly organic and habit-forming - this suggests Groupon can build a similar loyalty layer without CAC blowing up.

---

## 3. How they engage users (the habit loop)

Traffic acquisition is the top of the funnel; engagement is where the value compounds. Slickdeals' engagement model is the single most replicable and studied part of their business.

### The core loop
1. **User arrives** (direct, alert, email, or search)
2. **Browses Front Page** - curated by community votes, not merchandising
3. **Engages with threads** - reads comments, votes, replies, asks questions
4. **Sets alerts** - product / keyword / retailer / category
5. **Returns** when alert fires or when they check out of habit
6. **Buys** via affiliate click-out
7. **Comes back to discuss** the purchase, which feeds step 3 for other users

The loop is self-reinforcing because each user's engagement (vote, comment, post) increases the platform's value for every other user. This is a classic UGC network-effect business.

### Engagement mechanics (inputs)
- **Voting (thumbs up / thumbs down) on deals** - crowd-curation substitute for editorial
- **Comment threads per deal** - expertise sharing, scepticism, price verification
- **Deal Editor program** - community-sourced content moderation layer [Data - Slickdeals corp]
- **Forum subcategories** - Electronics, Home, Food, etc. Long-tail discovery
- **Deal alerts (email + push)** - configurable, highly personalised
- **Newsletter (weekly / daily)** - curated top deals
- **Cashback Rewards program** (launched relatively recently) - reinforces purchase -> visit -> purchase loop
- **iOS / Android apps** - primary engagement surface for mobile-first users

### Evidence the loop works
- 40% DAU/MAU - exceptional stickiness [Data - LA Business Journal, 2024]
- 14 app visits / week for active users [Self-reported, podcast 2026]
- 80% direct traffic - habit, not discovery [Data - Similarweb Mar 2026]
- **~5% of users drive ~20% of activity / revenue** [Data - HBS case study] - power-user economy. This is the moat inside the moat.

### The power-user economy
This is the under-discussed mechanism. ~5% of Slickdeals users (the Deal Editors and top posters) are responsible for most of the content, moderation, and front-page-worthy deals. In exchange they get status, reputation, badges, and in some cases modest revenue share. It is not a formal creator program like YouTube - it's a soft status-driven economy.

**Implication for Groupon:** building a similar community from scratch means cultivating a power-user tier from day 1. Not building a feature, cultivating a sociology. This is the part that takes 2-3 years and has high failure risk.

---

## 4. Products (the surfaces)

Slickdeals exposes its community's output across four surfaces. Each surface has a specific role in the acquisition + engagement + monetisation chain.

### 4.1 Website (slickdeals.net) - the mothership
- Primary surface for power users, desktop users, and deep forum engagement
- 56.5M monthly visits [Data - Similarweb Mar 2026]
- The forum is here. All threads, all votes, all comments live on this domain.
- Cashback Rewards program dashboard lives here
- Front Page, Popular Deals, Trending, Weekly Newsletter archive all hosted here

### 4.2 Mobile app (iOS + Android) - the habit engine
- Free download on both platforms
- 5M+ combined installs [Data - Slickdeals corp]
- **App engagement rivals Instagram / Twitter with 14 visits / week** [Self-reported, podcast 2026]
- March 2025 iOS redesign: improved deal detail page, auto-fill posting, grid/list view, better search [Data - Slickdeals forum announcement, Mar 27 2025]
- Push notifications for alerts drive re-engagement
- Declared platform pivot: "more users on mobile than desktop now" [Self-reported, podcast 2026]

### 4.3 Browser extension - the checkout intercept
- Available for Chrome, Firefox, Edge [Self-reported, podcast 2026]
- **Notable absence: no Safari extension.** This is a major gap. Honey, Rakuten, and Capital One Shopping all have Safari iOS extensions; Slickdeals does not.
- Functions: auto-applies coupon codes at checkout, surfaces trending retailer-specific deals while shopping, deal alerts, early access to exclusive deals
- Install via browser stores or slickdeals.net/radio [Self-reported, podcast 2026]
- Explicitly supports Edge because "5-10% of desktop users browse on Edge" [Self-reported, podcast 2026] - reveals they measure browser share carefully
- Strategic purpose: extract affiliate commission at the point of purchase. The extension is where the actual monetisation event happens.

### 4.4 Cashback Rewards program - the retention layer
- Launched as a points-based cashback system; redemption via PayPal or gift cards [Data - Slickdeals corp]
- **Paid out ~$1M total cumulative** [Data - from earlier research]
- This is tiny relative to Rakuten's $4.6B or Ibotta's $2.7B - Slickdeals' cashback is nascent and not a primary driver
- Strategic purpose: defend user retention against Rakuten-style cashback competitors, not to generate revenue directly
- Users are advised to disable other cashback extensions when using Slickdeals' program [Data - Slickdeals support] - a tacit acknowledgement that attribution conflicts with Rakuten/Honey/Cap One

**Why this product mix matters for Groupon:** Slickdeals is a 4-surface product (web, app, extension, cashback) but the gravitational centre is the forum. Every other surface is a distribution wrapper. If Groupon wanted to compete, the centre of gravity would need to be something equally sticky - for Groupon, that is local experiences + Groupon Bucks + the deal inventory. Competing on deal curation alone against SD's 25-year community is a losing frame.

---

## 5. How they monetise (revenue model)

Revenue is ~$45-55M (2026 working estimate). The mix is heavily skewed toward affiliate commissions but has been intentionally diversifying toward upper-funnel advertising under CEO Neville Crawley.

### 5.1 Affiliate commissions (primary revenue stream)
- Merchants pay Slickdeals **3%-15% of GMV** via affiliate networks [Data - enactsoft, HBS case]
- Most common range: 1%-8.5% [Data - enactsoft]
- After affiliate network cut (10-20% of commission), **Slickdeals' net take rate: ~2.5%-12% of GMV** [Estimate]
- Affiliate network partners: Awin, ShareASale, FlexOffers [Data - Awin/ShareASale/FlexOffers]

### 5.2 Sponsored placements / Featured Deals (growing)
- Brands pay for elevated placement on the Front Page or specific surfaces
- Sponsored content spend +56% YoY; high-impact brand placements +47% YoY [Data - Slickdeals sales blog, 2022+]
- Neville Crawley's strategic push: "convert MAU to DAU and go upper-funnel" [Data - LA Business Journal, 2024]

### 5.3 Display advertising
- Google Ad Manager + private ad deals
- Kevel ad server partnership - retail-media-style ad platform [Data - Kevel customers page]
- Standard display revenue across forum pages and deal detail pages

### 5.4 Data / analytics services
- Brand analytics on user engagement, deal performance, category trends
- API Sales program: >10,000 merchants, deal types, categories, articles licensed to third-party apps / sites [Data - corp-site.slickdeals.net/api-sales]

### 5.5 The Cashback program (cost centre disguised as product)
- NOT a meaningful revenue line. $1M cumulative payout suggests this is a retention tool, not profit.
- Strategically: exists to prevent Rakuten from stealing Slickdeals' users via cashback offers.

### Revenue quality analysis
- **Durable**: 80% direct traffic means low CAC; affiliate commissions scale with user habit not paid spend
- **Concentration risk**: top retailers (Amazon, Walmart, Best Buy, Target) likely account for outsized share of affiliate commissions - exact split unknown [Data gap]
- **Regulatory exposure**: the Honey / Capital One Shopping class-action on commission theft [Data - Seeger Weiss case, 2024-2025] applies to the entire affiliate-extension category. Slickdeals has not been named but shares the business model.

---

## 6. Unit economics (what a user is worth)

This is the most interesting section and has the largest evidence gaps. Working estimates below.

### Revenue per user
- $45-55M revenue / 12M MAU = **~$3.75-$4.60 per MAU per year** [Estimate - simple division]
- Revenue per MAU is lower than Ibotta's ~$6.30/MAU-equivalent but with a fundamentally different cost structure
- Comparison: Rakuten pays $50 referral bonus, implying LTV well above $50 [Data - Rakuten]. SD's ARPU of $4 suggests either a much longer LTV tail or a very different margin profile.

### Probable cost structure (speculative, based on scale)
- Headcount ~200 at ~$150k-$200k fully loaded US average = $30-40M payroll [Estimate]
- Infrastructure, content moderation tools, affiliate platform costs = $5-10M [Estimate]
- Marketing / acquisition = small (they don't paid-market much)
- Leaves: $5-15M EBITDA or similar operating income [Estimate]
- Private company so numbers are inferred; could be off by ±50% [Caveat]

### What this implies
- Slickdeals is **profitable but not highly profitable**. It is a solid PE-owned cashflow business, not a venture-growth story.
- The reason Crawley is pushing upper-funnel brand advertising is margin expansion, not survival. Brand ads have higher CPMs than affiliate commissions.
- Labor cost is the main constraint on scaling. Content moderation and Deal Editor operations do not compress linearly with volume.

### Why this matters for Groupon
- If Groupon replicates the model, it would reach similar ARPU. $4 x addressable MAU - if Groupon coupons brings 20-30M US MAU - would suggest $80-120M in affiliate revenue if done well. [Estimate, assumption-heavy]
- But profit margin would be similar: ~$10-20M operating income per year. Interesting, not transformative.
- The strategic value is not revenue, it is retention and engagement. A Slickdeals-like community inside Groupon would compound direct traffic and reduce Groupon's own CAC.

---

## 7. Upsells and expansion vectors

Where does Slickdeals grow revenue from here? The published signals and observed behaviour suggest five vectors.

### 7.1 Upper-funnel brand advertising (current priority)
- CEO Crawley's explicit strategy [Data - LA Business Journal, 2024]
- 56% YoY sponsored spend growth [Data - Slickdeals sales blog, 2022+]
- Taps retail-media budgets that go to Google Shopping / Amazon Ads today

### 7.2 Deeper merchant partnerships
- Moving from "one of many affiliate publishers" to "exclusive deal source" for select retailers
- Leverage: 12M MAU + high DAU/MAU ratio gives negotiation power

### 7.3 AI-powered deal surfacing
- Amazon SageMaker + Siamese models + XGBoost personalisation shipped in 2025 [Data - AWS re:Invent 2025 SMB206]
- Measured lift: **merchant outbound clicks + revenue +7%** [Data - AWS re:Invent 2025]
- Personalisation is a quiet margin-expander

### 7.4 AI chat integration (Perplexity + PayPal, Nov 2025)
- Slickdeals deal surfacing inside Perplexity AI chat experience [Data - SD forum thread 18875527, Nov 2025]
- Early bet on AI-shopping surfaces (which may or may not become major acquisition channels)

### 7.5 Geographic expansion
- Slickdeals is US-only. UK, Canada, Australia are underserved English-speaking markets.
- No public sign they are actually doing this [Data gap]
- Likely constrained by the same moderation-and-curation cost that limits scaling.

### 7.6 Cashback program (in progress but thin)
- The Rewards program is the slowest-growing surface. $1M cumulative payout vs Rakuten's $4.6B.
- Probably more defensive than offensive.

### Upsells they are NOT pursuing (telling)
- Paid subscription ("Slickdeals Plus") - discussed but not shipped
- Exclusive deal tier - partially attempted via Featured Deals but not productised as a consumer premium
- Marketplace / direct sales - deliberately not a marketplace; they route traffic out

---

## 8. Value chain (who captures what)

The Slickdeals value chain has 4 actors. Mapping who captures value at each step is the clearest way to see the model.

### Actors
1. **Merchant / retailer** (e.g., Best Buy, Macy's, Amazon)
2. **Affiliate network** (Awin, ShareASale, FlexOffers)
3. **Slickdeals** (platform + community)
4. **User / community** (reader + deal-poster + Deal Editor)

### Value flow on a typical $100 transaction
| Step | Actor | Input | Output | Value captured |
|---|---|---|---|---|
| 1 | User / Deal Editor | Time, expertise | Deal post on SD forum | Status, reputation, badges, small cash (for Editors only) |
| 2 | Community | Votes, comments | Front Page promotion of good deals | Better deals surfaced -> more trust |
| 3 | Reader | Attention | Click on Front Page deal | Saves money on purchase |
| 4 | Affiliate network | Tracking link | Attribution | 10-20% of the commission |
| 5 | Slickdeals | Platform, community, brand trust | Outbound click | 80-90% of the commission (~3-12% of GMV) |
| 6 | Merchant | Product, inventory, fulfilment | $100 sale | $100 GMV minus 3-15% commission = $85-97 net |

### The unusual value-capture feature
- The user / deal-poster captures **almost nothing** in cash. They get status, badges, a modest sense of community belonging. This is the UGC-platform paradox: the people who generate the content get the least cash.
- Slickdeals captures most of the commission.
- Merchants accept the commission because they treat Slickdeals as a performance-marketing channel.

### Why this works (and is fragile)
- Works because the status economy is genuinely valuable to power users. Badges and reputation mean something in a 25-year forum.
- Fragile because if a competitor (or Slickdeals itself) started paying Deal Editors cash, the economics shift. Rakuten could in theory pay deal-posters directly and cream off SD's top 5%.
- Slickdeals' content moderation and badge system is effectively a defence against this attack. It is not merely a feature - it is a moat against competitor recruitment.

### Where margin leaks (opportunities)
- **No Safari iOS extension** - Slickdeals misses the Apple-users-in-Safari traffic that Honey, Rakuten, Cap One Shopping capture. This is a product gap, not a business-model gap, but it cedes high-intent traffic at checkout.
- **Cashback program is underdeveloped** - Rakuten could peel off casual users with a bigger cashback offer.
- **International** - 0% of the non-US market is served.
- **AI-commerce surfaces** - early bet with Perplexity but not a strong presence yet.

---

## 9. What is replicable vs non-transferable moat

This is the question Dusan actually wants answered. Honest breakdown.

### Replicable (Groupon could build these)
1. **Voting / front-page algorithm** - straightforward engineering. Reddit-style algorithm, 2-4 sprints.
2. **Deal alerts (product / keyword / retailer)** - configurable push + email. 2-3 sprints.
3. **Browser extension with auto-apply + trending retailer deals** - non-trivial but proven pattern. 6-8 weeks of mobile eng.
4. **Cashback Rewards program** - covered in loyalty-research mechanic cards; 6-8 sprints.
5. **Mobile-first app UX** - Groupon has app infrastructure already.
6. **Newsletter / digest email** - exists at Groupon already; can be retargeted.
7. **AI deal scoring** - SD uses SageMaker + Siamese models; Groupon can adopt same pattern, +7% outbound click lift is the benchmark.

### Non-transferable moat (cannot buy, build, or partner around)
1. **25 years of forum content** - historical threads, discussion depth, SEO long-tail. Cannot be replicated without time.
2. **Power-user economy** (5% of users, 20% of activity) - cultivating a status-driven community takes 2-3 years minimum and has high failure risk.
3. **Deal Editor corps** - the moderation layer is human-judgment dependent and cannot be AI-replaced at quality parity.
4. **Brand trust signal** ("slickdeals.net" = legitimacy in the deals community) - accumulated, not purchasable.
5. **Direct traffic habit** (80% direct) - the result of years of good deals. Requires deal quality first; traffic habit follows.

### What's uncertain / partially replicable
- **Deal velocity from community sourcing vs AI-curated feed** - Slickdeals gets thousands of user-posted deals per day. A well-tuned AI scraper across affiliate networks might match the volume but miss the quality signal from human curation.
- **Moderation discipline** - Slickdeals has refined this over 20 years; Groupon would need to build from zero.

### Strategic takeaway for Groupon
- **If the goal is to replicate Slickdeals' moat:** 2-3 years, $10-20M investment, high failure risk [Estimate - from prior research]. The success case is owned-audience + community-driven content; the failure case is a deserted forum and wasted capex.
- **If the goal is to benefit from Slickdeals' assets:** partner. See partnership-feasibility doc in loyalty-research folder. Short-term, lower-cost, reversible.
- **If the goal is to steal Slickdeals' users:** build a cashback program (card 02, 05 in mechanic cards) and a Safari extension (card 04). These address SD's two biggest product gaps.

---

## 10. What this means for Groupon

Five implications, ordered by conviction.

1. **Slickdeals' main vulnerability is product gaps, not model flaws.** No Safari extension, weak cashback, no international. Groupon's loyalty layer with Bucks + Safari extension (Safari extension bundling mechanic) would directly attack these gaps without needing to build a competing forum. High conviction.

2. **Groupon's coupons traffic is more similar to Slickdeals' model than it looks.** Both are organic, habit-forming, direct-traffic-heavy. Both rely on content rather than paid acquisition. This means Groupon can plausibly adopt Slickdeals-style engagement mechanics (alerts, front-page voting, cashback) without blowing up CAC. High conviction.

3. **The partnership conversation (Dusan's original framing) misdiagnoses the problem.** Goods did not fail from curation; it failed from fulfilment economics. Embedding a Slickdeals feed does not solve fulfilment. See partnership-feasibility-slickdeals.md for the full analysis. Medium-high conviction.

4. **PE-exit timing is a clock.** GS/Hearst have held 8 years. An exit in 12-24 months is highly likely. If Amazon (owns Woot) buys Slickdeals, any partnership terms would be killed or radically shifted. This affects partnership timing regardless of shape. Medium conviction on timing, high conviction on direction.

5. **The power-user economy is the piece Groupon should study hardest.** Not the front-page algorithm, not the voting, not the extension. The moat-within-the-moat is how Slickdeals cultivated ~5% of users into doing ~20% of the work for status rather than cash. If Groupon wants a similar moat, cultivating power users inside Groupon's audience is a 2-3 year commitment, not a feature launch. Medium conviction.

---

## 11. Data sources and confidence

### Primary / High-confidence
- Slickdeals corporate site (corp-site.slickdeals.net, slickdeals.net/about)
- AWS re:Invent 2025 session SMB206 (AI and personalisation measured lifts)
- Similarweb Pro exports (March 2026)
- LA Business Journal profile of Neville Crawley (2024)
- Bloomberg / PR Newswire (2018 acquisition)
- HBS case study (power-user economy, deal volume)

### Secondary / Medium-confidence
- enactsoft, martini.ai (revenue estimates)
- Awin / ShareASale / FlexOffers publisher pages (affiliate terms)
- Kevel customers page (ad-tech partnership)

### Self-reported (Medium-Low confidence, PR-flavoured)
- Slickdeals podcast 2026 with Regina Conway + Mark Saltzman - source: https://www.youtube.com/watch?v=9_DIFQoEucU
- Specifically: 14 visits / week claim, "rivals Instagram / Twitter engagement" claim, mobile-migration claim, 5-10% Edge users claim
- Mark Saltzman is a disclosed paid partner; treat his framing as promotional

### Explicit data gaps
- Top-retailer revenue concentration (% from Amazon / Walmart / Best Buy etc.) - not published
- Exact commission rates by merchant tier - inferred from affiliate network ranges only
- 2025 or 2026 sale / exit activity - nothing public
- International expansion plans - nothing public
- Deal Editor program economics (how many, how paid if at all) - nothing published in detail
- Power-user cohort dynamics (true % of users driving % of revenue in 2026 vs HBS case) - stale

### Explicit non-research
- Primary customer interviews with Slickdeals users have NOT been conducted for this doc. Replicating their moat might require that step separately.
- Cannot test Slickdeals' extension or app flows from outside the US without workarounds.

---

## 12. Next steps

If we want to deepen this:

1. **Interview 3-5 active Slickdeals power users** - 30-min calls, the only way to understand the status economy from the inside. Rebecca's research network or a vendor like UserInterviews. Budget: ~$1K + a week.
2. **Pull Slickdeals SEC / registration data** - private company but GS filings may disclose segment-level data.
3. **Mystery-shop the extension end-to-end** - install, track attribution for 30 days across a few retailers, see what the commission split looks like in practice.
4. **Benchmark Slickdeals' cashback against Rakuten's** - side-by-side walk-through with identical retailer baskets.
5. **Build a 1-pager for Dusan** - condensed version of this doc, focused on the three implications he cares about (can we partner, can we build it, what's the time pressure).

---

## Changelog

- v0.1 (2026-04-23): Initial reverse-engineering draft. Built from existing loyalty-research/partnership-feasibility-slickdeals.md + raw/slickdeals-partnership-feasibility.md + Slickdeals podcast summary + SimilarWeb data + prior research.
- v0.2 (pending): Rebecca review, Dusan feedback, any corrections on interview-sourced numbers.
