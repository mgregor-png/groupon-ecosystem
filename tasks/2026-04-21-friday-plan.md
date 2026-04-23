# Loyalty Research - Friday Delivery Plan (UPDATED post-Rebecca sync)

**Owners:** Martin (lead) + Rebecca (collaborator, per Apr 21 sync)
**Deliverable:** Fri Apr 24, 1pm CET
**Output:** One G Drive folder (Shared Drive -> Product -> Cashback research -> loyalty-research) with summary + raw data + AI funnel materials. NOT public GitHub Pages.
**Constraint:** No waiting on Adam/Dusan approval - go.
**Cadence:** Weekly iteration via Adam's 5/15 going forward
**Next sync:** Thursday product meet

---

## 1. Commitment - what lands Friday 1pm CET

**One package** based on Rebecca's draft + Martin's complementary layers + AI funnel appendix.

### Sections inherited from Rebecca's draft (keep, lightly edit)
- §1 Market overview (keep)
- §2.1-2.6 six competitor profiles (edit for fact-check, add signup-flow evidence)
- §3 comparative tables (trim duplication)
- §4 SimilarWeb overlap + stacking hypothesis (keep, this is the best section)
- §5 Exec DD checklist (tighten, this is the work-plan spine)

### Sections Martin adds (new)
- §0 **One-page exec summary** at top with landed recommendation and $40M framing
- §2.7 **Slickdeals partnership analysis** (Dusan priority, not loyalty reverse-eng)
- §6 **Groupon-specific implications** rewrite with Bucks product decisions, Ernesto retention dependency, "no team owns loyalty" opportunity frame
- §6.x **Retention sizing model** - 3-scenario sensitivity table (conservative / base / aggressive) that anchors the $40M habit-formation claim; drives §0 headline
- **AI funnel companion doc** (separate file, cross-linked) - prompts, raw data, iterations per competitor AND for the sizing model
- Signup-flow inserts across §2.1, 2.2, 2.3 with screenshots from live signups

### Dropped (reconsidered)
- §2.8 Starbucks / loyalty-without-extension - single-brand first-party model does not transfer to Groupon's multi-merchant marketplace. Loyalty-vs-extension question handled by contrasting Rakuten points-partnerships vs CapOne soft-currency vs Honey transactional-cash WITHIN the extension set.
- AI funnel inline option - decided: companion doc, not inline. Reasoning: main doc stays exec-readable; funnel grows each weekly iteration; easier to cross-link specific prompts back to conclusions.

### Sections Martin drops / marks as gap
- Mark Brinded crossover analysis - flag as known gap, don't invent
- Merchant overlap data - flag as known gap
- Non-US caveat - one paragraph, not a full section

---

## 1b. Work split (post-Rebecca sync Apr 21)

### Martin owns
- **Live competitor signup capture** - Rakuten / CapOne / Honey. Manual for signup + extension UX + Nike test. AI subagents for public pre-auth pages + marketing copy in parallel. Screen recording where possible.
- **Fact-check Rebecca v1 load-bearing numbers** - top 5 claims against primary sources
- **Retention sizing model kick-off** - 3-scenario sensitivity. Martin drafts initial; Rebecca reviews and contributes inputs
- **PostHog quick survey** - 3 simple non-incentivized questions on new UI, launches Wed
- **AI funnel folder contribution** - Martin's Claude Code project folder (loyalty-research/ with raw/ + logs/)
- **Final assembly + send to Adam Friday 1pm CET**
- **Daniel chase (direct)** - for Rakuten US access via VPN blocker; Martin contacts Daniel himself

### Rebecca owns
- **Content + merchant crossover** - CapOne and RetailMeNot vs Groupon coupons footprint (Florence scrapes RetailMeNot; CapOne is new)
- **Keyword crossover** - SEMrush or AccuRanker audience overlap for groupon.com vs 4 competitors; confirms her SimilarWeb affinity data with second source
- **BI chase: coupons -> Groupon deal crossover** - via Mark Brinded; raises Asanas for various internal people
- **Mark Neary survey coordination** - submit 3-5 loyalty questions to his funded user survey (has incentive budget)
- **Continuing help on modeling** - review Martin's initial model and contribute inputs
- **AI funnel folder contribution** - Rebecca moves her work to Claude Code and contributes her project folder

---

## 2. Time-blocked schedule Tue-Fri

### Tue Apr 21 (today, from now)
**Pre 12:00 Mobile App planning:**
- Sign up for Rakuten using real email - capture signup flow screenshots, all inbound emails, push prompts
- Start `ai-funnel-log.md` - every prompt and raw input from now goes here
- Primary-source check on Rakuten "20M active" + "$4.6B cumulative" claims - Rakuten investor relations instead of sidehustlenation

**13:00-15:30 (between Mobile App and James sync):**
- Sign up for Capital One Shopping + PayPal Honey - same capture discipline
- Draft §2.7 Slickdeals skeleton (model / traffic / audience overlap / partnership economics)

**Post 16:00:**
- Write 1-page §0 exec summary with $40M framing
- Reply in Asana thread: "taking over, going for Friday, here's the split" (see §5 below)
- Ping Rebecca: thank her for the spine, agree on handoff (she can step back)

### Wed Apr 22
- **Morning block:** Fact-check 5 load-bearing numbers - Rakuten 20M, CapOne $45, Coupert 8M weekly, Ibotta 54M registered, Honey 13M Chrome. Replace secondary sources with primary or drop the claim.
- **Mid-day:** Rewrite §2.1 Rakuten deep dive with live signup evidence inserted (screenshots, email cadence day 1-2, extension UX on Nike test)
- **Afternoon:** Scaffold §8.3 AI funnel appendix structure - per-competitor sub-sections, paste accumulated prompts + raw data from log

### Thu Apr 23
- **Morning:** Rewrite §2.2 Capital One Shopping + §2.3 Honey deep dives with signup evidence. Honey's iOS Safari UX is the technical precedent - make that explicit.
- **Mid-day:** Build §6.x **retention sizing model** - three-scenario sensitivity table. Inputs: MAU x engagement x frequency uplift x AOV x take rate x (1 - reward cost%). Populate conservative/base/aggressive columns using public proxies + industry benchmarks (Amex MR, Amazon Prime, Starbucks Rewards frequency multipliers, loyalty literature 15-25%). Flag which inputs need Ernesto validation.
- **Afternoon:** §6 rewrite - $40M frame anchored in sizing model aggressive column, Mikhail quote, Ernesto dependency, specific Bucks product decisions (multiplier / expiry / category lock). Populate AI funnel companion doc with iteration entries including the sizing model's prompts/inputs.

### Fri Apr 24 morning (deadline 1pm CET)
- **07:00-09:00:** Final pass through whole doc, trim §3 duplication, lock §0 exec summary recommendation
- **09:00-10:30:** Add source-quality tiering table (primary / press / aggregator / review) - cheap, pre-empts AI-slop scepticism
- **10:30-12:00:** Distribution decision + publish. NOT public GitHub Pages. Options: Drive (Florence's approach) or private repo with noindex. Default: Drive copy so Adam/Dusan can comment inline.
- **12:00-13:00:** Send to Adam with 3-bullet cover note pointing at §0 recommendation, AI funnel appendix, and the 5 questions flagged for Dusan edit.

---

## 3. Cut list (drop if time slips)

Priority-ordered, drop from bottom up:
1. Source-quality tiering table - nice, not essential for v1
2. Non-US caveat paragraph
3. §6 specific Bucks product decisions - can stay directional

**Never cut:** §0 exec summary, §2.7 Slickdeals, §6.x retention sizing model ($40M anchor), AI funnel companion doc (Adam required), signup-flow evidence inserts.

---

## 4. Start-immediately block (next ~90 min)

**Concrete order:**

1. Open `ai-funnel-log.md` in `projects/groupon-ecosystem/deliverables/` - fresh file, headings: "Prompts used | Raw inputs | Iterations | Human edits." Paste this plan at the top as seed context.
2. Open a fresh Chrome profile (clean session for competitor capture)
3. Sign up for Rakuten with capture-ready real email. Screenshot: landing, signup form, email verify, first logged-in screen, extension install prompt, first merchant offer
4. Install Rakuten Safari extension. Navigate to Nike. Capture extension activation UX (the doc already flags Nike as the test case)
5. Leave Rakuten running and sign up for Capital One Shopping same way. Capture $45 incentive offer - is it still live? Screenshot the actual offer page.
6. Sign up for PayPal Honey same way. Capture iOS Safari extension behaviour if accessible (CZ VPN limitation flagged - Daniel via Zoe for US capture is the backup).
7. At 11:45 stop - prep for 12:00 Mobile App planning.

**While signups are happening:** run primary-source checks on Rakuten 20M + $4.6B claims in parallel browser tabs. Goal: one replaced citation before noon.

---

## 5. Asana reply - send today

Post in the task thread before EOD, to Adam + Rebecca:

> Taking point on this. Rebecca kicked off a strong v1 (link) - I will build the Friday package on top of her spine rather than run parallel research.
>
> Additions from me by Fri 1pm CET:
> - Slickdeals as a partnership workstream per Dusan
> - One-pager exec summary with $40M habit-formation frame
> - Live signup-flow evidence for Rakuten / Capital One Shopping / Honey
> - AI funnel appendix (prompts, raw data, iterations)
> - Loyalty-without-extension benchmark (Starbucks)
>
> Rebecca - huge thanks for the SimilarWeb overlap data and DD checklist, both stay. You can step back from here; I will pull from you only if I need US-side flow capture via Daniel.
>
> FYI on format calls I am making (not asking - just flagging):
> - AI funnel will be a companion doc cross-linked from the main, not inline. Keeps the exec doc readable while iterations accumulate.
> - Framing leads with habit-formation revenue uplift on core deals. Sizing it via 3-scenario sensitivity (conservative / base / aggressive). Commission-only number sits underneath as one lever of several, not the headline.

---

## 6. Risk register

| Risk | Impact | Mitigation |
|---|---|---|
| VPN blocks US-only flows on any competitor | Breaks §2.x signup evidence | Capture what works; flag gap; ping Zoe/Daniel if Honey iOS Safari breaks |
| Primary-source check invalidates multiple Rebecca claims | Scramble to rewrite sections | Drop unverified claims rather than paper over; transparency is Adam's new rule |
| Mobile App 12:00 or James 15:30 runs over | Lose afternoon block | Accept - cut list takes the hit, not Slickdeals/AI funnel |
| Adam replies with major scope change | Whole plan shifts | Rely on cadence rule: weekly iteration, incorporate in next round |
| Distribution rule blocks Drive | Last-minute scramble | Fallback: private GitHub repo with noindex meta + robots, per Florence precedent |

---

## 7. What this plan explicitly does NOT do

- Wait for Adam or Dusan green-light on framework before executing
- Run a parallel market-research pass to Rebecca's
- Go deep on six competitors - tiered focus only: Rakuten + CapOne + Honey deep; Ibotta + RetailMeNot + Coupert stay at Rebecca's surface depth; Slickdeals partnership angle separate; Starbucks as single loyalty-without-extension anchor
- Produce polished slideware - plain doc, Adam asked for process over polish
- Answer the crossover question (Mark Brinded status) - flagged as gap
