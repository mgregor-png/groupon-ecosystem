# Alternative Monetisation — Brainstorm Ideas
**For discussion:** Martin + Becky, 2026-03-26
**Primary lens:** Frequency-first — what gets core users to open the app 3x more per week?
**Success metric:** Double monetisation per UDV (more opens → more transactions → more revenue)

---

## The Big Insight

The highest-frequency savings apps (Fetch, Temu, Shopkick) have **decoupled "reason to open" from "intent to transact."** Groupon currently requires purchase intent to justify an open. Every idea below creates an open-worthy trigger *independent* of active deal hunting.

---

## Ideas

### 0. Foundation: Savings Wallet / Groupon Credits Balance
**Not a standalone feature — an enabler for everything below.** A visible, growing balance ("You've earned $14.20 this month") is the retention glue that makes streaks, spins, receipts, and referrals compound. Fetch, Ibotta, and Shopkick all use an accumulating balance as the primary daily-open driver. Users check their balance even when not shopping.

---

### 1. Daily Deal Drop + Check-in Streak
**What:** 3-5 curated deals rotate every 24 hours (visible only to app users). Opening the app daily builds a streak — hit 7 days and unlock a bonus (e.g. extra 10% off next purchase, exclusive deal access). Miss a day, lose the streak.

**Why it drives frequency:** Loss aversion is the strongest behavioural lever. Duolingo users who hit 7-day streaks are 3.6x more likely to stay engaged long-term. Temu's daily check-in drives 89% interaction rates. The time-limited deal rotation creates genuine FOMO — today's deals won't be here tomorrow.

**Groupon fit:** Local deals already have natural scarcity and freshness. The app install base is the distribution channel. Coupons team could curate the daily selection from existing inventory — no new supply needed.

**POC effort:** Low. Daily deal curation + streak counter UI + push notification. Could run as a 4-week test with a segment of app users.

**Risk to address:** Streak rewards must be concrete (credits, exclusive deal unlock) — not abstract. Duolingo streaks work because the daily activity has intrinsic value (learning). Groupon streaks are extrinsically motivated, so the reward needs to carry the weight.

---

### 2. "Watch This Deal" — Price & Availability Alerts
**What:** Let users save deals/categories they're interested in ("watching"). Notify them when: a deal restarts, a new deal appears in their watched category, or a price drops. Like Honey's Droplist but for local deals.

**Why it drives frequency:** Honey's Droplist model proves that deferred desire + permission-based alerts has the highest re-engagement quality. Users opt in, so notifications feel like a service, not spam. Each alert is a high-intent return visit.

**Groupon fit:** Groupon's deals are inherently cyclical — restaurants rerun offers, seasonal deals return. Currently there's no way for a user to say "tell me when there's a spa deal near me under $50." This fills a real gap.

**POC effort:** Medium. Requires a "Watch" button on deals/categories, a notification engine for deal-match triggers, and a saved-watches screen. Could start with category-level watches (simpler) before deal-level.

---

### 3. Spin-to-Win / Daily Reward Game
**What:** One daily spin (slot machine, scratch card, wheel) that awards variable rewards: Groupon credits, percentage-off coupons, or entries into a monthly prize draw. The reward is unknown until revealed — variable-ratio schedule.

**Why it drives frequency:** Temu's spin wheels drive 89.4% interaction rates. Fetch Play boosted customer lifetime value by 10% and monthly opens by 5%. Over 50% of Temu users made unplanned purchases after gamified interactions. The variable reward is the same mechanism as slot machines — maximises compulsive opens.

**Groupon fit:** This is the most "entertainment-first, commerce-second" idea. It works if Groupon is willing to give away small amounts of credit to drive daily opens. The cost per daily open is tiny vs. paid re-engagement (push notifications, retargeting ads). Works especially well with the price-sensitive audience who perceives any free credit as valuable.

**POC effort:** Low-medium. Spin wheel UI + reward logic + push reminder ("Your daily spin is waiting"). Could test with Groupon Bucks as the reward currency.

---

### 4. Community Picks / Social Deal Voting
**What:** Users can upvote deals. A "Trending" or "Community Picks" feed surfaces the highest-voted deals. Optional: users can submit external deals they've found (Slickdeals model), creating user-generated supply.

**Why it drives frequency:** Slickdeals converts 40% of its 12M MAU to DAU through community-curated content. Social proof ("68,000 people liked this deal") makes deals feel discovered, not sold. The feed refreshes constantly — there's always something new to check. Voting gives users agency and status.

**Groupon fit:** Moderate. Groupon has no community infrastructure today, but the voting layer is simple. Starting with just upvotes on existing deals (no UGC) is low-risk. The "trending near you" angle combines community signal with local relevance — unique to Groupon.

**POC effort:** Medium. Upvote button + trending feed algorithm + "popular near you" section. UGC deal submission is a later phase.

---

### 5. Receipt Scanning → Groupon Credits
**What:** Scan any local receipt (restaurant, salon, gym) and earn Groupon credits. If the receipt is from a Groupon merchant, earn bonus credits. Creates a post-purchase touchpoint for every local spend, not just Groupon transactions.

**Why it drives frequency:** Fetch Rewards gets more daily opens than Starbucks or Uber Eats by making "scan any receipt" a zero-friction habit. Attaching to an existing behaviour (getting a receipt) is the fastest path to habit formation. Ibotta drives $500M+ revenue from this model.

**Groupon fit:** Strong for local. Unlike Fetch (grocery/retail), Groupon could own "local services receipt scanning" — a category Fetch/Ibotta don't cover well. Every restaurant visit, haircut, or gym session becomes a Groupon touchpoint. Merchant data from receipts is also valuable for targeting.

**POC effort:** High if built in-house (OCR, receipt parsing, fraud detection). Medium if partnered with an existing receipt scanning provider. Could start with manual receipt upload + human review before automating.

---

### 6. "Groupon Select" Reinvention → Daily Exclusive Access
**What:** Revamp Groupon Select ($4.99/mo) from a flat discount into a daily-engagement membership: Select members get an exclusive "Member Deal of the Day" (not available to non-members), early access to new deals, streak bonuses, and a quarterly "Big Savings Report" showing total savings.

**Why it drives frequency:** Amazon Prime (90%+ renewal, $139/yr) and Costco (90.4% renewal) prove that paid membership drives purchase frequency through "fee recovery" psychology. Members shop more to justify the cost. Daily exclusive content gives a reason to open specifically because you're a member.

**Groupon fit:** Select already exists — the infrastructure is there. The gap is perceived value and daily engagement hook. Adding exclusive daily content + savings visibility could transform it from "nice to have" to "must check daily."

**POC effort:** Low-medium. Exclusive deal flagging + member-only daily deal push + savings dashboard. No new membership infrastructure needed.

---

### 7. Geo-Push: "You're Near a Deal"
**What:** When a user is near a Groupon merchant (within 200m), send a contextual push: "The spa next door has 40% off today." Passive, location-triggered engagement.

**Why it drives frequency:** Shopkick leads all shopping apps in frequency and session length because physical location is the trigger — not user intent. The notification arrives at the exact moment of opportunity. Rakuten's in-store cashback push drives similar behaviour.

**Groupon fit:** Very high. Groupon's USP is *local* deals — location-based triggers are the natural extension. Core app already has location permissions. This turns every walk past a merchant into a potential transaction without requiring the user to actively search.

**POC effort:** Medium. Requires merchant geofencing, contextual push notification logic, and opt-in UX. Privacy/battery considerations need careful handling.

---

### 8. Curated Local Content — "What to Do This Weekend"
**What:** Weekly push notification / in-app section: "Top 5 things to do in [City] this weekend" — curated from Groupon's deal inventory + editorial recommendations. Think The Strategist but for local experiences.

**Why it drives frequency:** Creates a weekly ritual ("What's Groupon recommending this weekend?"). Content-driven engagement is lower friction than transactional — users browse for inspiration, not with purchase intent. The Strategist earns $2M+/month from this model (editorial + affiliate).

**Groupon fit:** Natural. Groupon literally has the local deal inventory. Nobody else can say "here are 5 great restaurant deals near you this weekend" with actual attached offers. This positions the app as a *planning tool*, not just a discount marketplace.

**POC effort:** Low. Curated list from existing inventory + weekly push + in-app placement. Could be manual curation initially, automated later.

---

### 9. Last-Minute Local Deals (HotelTonight Model)
**What:** Groupon proactively fills merchant dead time — empty restaurant tables Tuesday lunch, salon gaps at 4pm, gym off-peak slots. "3 spa slots left today, 60% off." Deep discounts on genuinely time-sensitive inventory.

**Why it drives frequency:** Creates urgency-driven opens independent of user intent. Unlike standard deals (available for weeks), these expire in hours. Users learn to check "what's available right now near me?" — a fundamentally different, higher-frequency behaviour.

**Groupon fit:** Uniquely strong. Groupon already has merchant relationships and the local deal infrastructure. Nobody else can surface "your favourite salon has a 4pm gap today, 50% off." This is the intersection of Groupon's local advantage + time-sensitivity + real merchant value (filling dead time).

**POC effort:** Medium. Could start with a manual programme — 10-20 merchants in one city text a Groupon rep when they have gaps, deals go live within an hour. Test demand before building self-service tooling.

---

### 10. Merchant Self-Service — Instant Deal Publishing
**What:** Let merchants publish deals in 2-3 clicks (vs. the current multi-step Metro process). Real-time "flash deals" that merchants can activate when business is slow ("Tuesday afternoon, 50% off — 2 hours only").

**Why it drives frequency:** Flash deals create urgency and unpredictability — the same variable-reward mechanic that makes Slickdeals addictive. Users check back because "something new might have dropped." Merchant-generated supply also scales inventory without Groupon's sales team.

**Groupon fit:** Addresses both supply scaling (more deals = more reasons to open) and frequency (flash deals = urgency). Groupon has the merchant relationships; simplifying the tool could unlock a long tail of smaller businesses.

**POC effort:** High for Core (requires platform changes). But could test the concept with a manual "flash deal" programme — merchants message a Groupon rep, deal goes live within an hour.

---

## Quick Evaluation Matrix

| # | Idea | Frequency Impact | Speed to Test | Groupon Differentiation |
|---|------|:---:|:---:|:---:|
| 1 | Daily Deal Drop + Streak | ★★★★★ | ★★★★★ | ★★★ |
| 2 | Watch This Deal | ★★★★ | ★★★★ | ★★★★ |
| 3 | Spin-to-Win | ★★★★ | ★★★★ | ★★ |
| 4 | Community Picks | ★★★★ | ★★★ | ★★★ |
| 5 | Receipt Scanning | ★★★★ | ★★ | ★★★★ |
| 6 | Select Reinvention | ★★★★ | ★★★★ | ★★★ |
| 7 | Geo-Push | ★★★★ | ★★★ | ★★★★★ |
| 8 | Weekend Content | ★★★★ | ★★★★★ | ★★★★ |
| 9 | Last-Minute Deals | ★★★★★ | ★★★ | ★★★★★ |
| 10 | Merchant Self-Service | ★★★ | ★★ | ★★★★ |

---

## Recommendation: Lead Concept + Supporting Layer

**Primary concept: Daily Deal Drop + Streak (#1)**
Strongest behavioural evidence, lowest effort, uses existing inventory. The streak mechanic is the daily-open engine. Pair it with the **Savings Wallet** foundation so credits accumulate visibly.

**Complementary layer: Watch This Deal (#2)**
Passive re-engagement for users who don't want to check daily but will return when something matches their interest. This captures the "intent-based" segment that streaks miss.

**Sleeper pick: Weekend Content (#8) or Last-Minute Deals (#9)**
Weekend content is easiest to ship and most defensible — positions Groupon as a planning tool. Last-minute deals are the most uniquely Groupon idea — nobody else can do "your salon has a 4pm gap."

**Propose all four to Becky as a bundle** — they're not competing, they're complementary engagement layers targeting different user behaviours (daily habit, passive interest, weekly planning, spontaneous opportunity).

---

## Risks to Name Upfront
- **Cannibalisation:** Could daily deals train users to wait instead of buying now? Mitigate by making daily deals *additive* inventory (flash/exclusive), not discounts on what's already available.
- **Push notification fatigue:** 4-5 ideas here rely on push. Need a notification strategy — one daily digest, not 5 separate pushes. The "Morning Brief" format (one push aggregating all signals) solves this.
- **App landing experience:** Current app is built for purchase intent. If streaks/spins drive opens without intent, the home screen needs a "non-transactional" landing zone (daily deals tab, trending section).

---

## What We Considered and Set Aside
- **3P Marketplace (goods replacement):** Revenue play, not frequency. Being handled separately by Core.
- **Full cashback programme:** Not differentiated — every competitor has one. Promo test on Coupons pages is the separate workstream.
- **Social feed / user-generated content:** Requires community flywheel Groupon doesn't have. Cold-start problem is severe.
- **Referral/invite loop:** Good growth mechanic, but complements rather than drives frequency. Layer it on later.

---

## Discussion Questions for Becky
1. Does the **frequency-first** framing resonate, or does Dusan/Adam need to see revenue-first concepts too?
2. **My recommendation:** Go deep on the 4-concept bundle (Daily Deals + Watch + Weekend Content + Last-Minute). Does that feel right, or should we narrow to 1-2?
3. Is the app team open to **gamification mechanics** (streaks, daily rewards) or would that feel off-brand?
4. Does Becky have visibility into **Groupon Select** performance data? That determines whether #6 is worth pursuing.
5. **Geo-push** — does Core already do this? If not, why not?
6. What does "double monetisation" look like in actual numbers? Do we have current UDV revenue figures to anchor against?
