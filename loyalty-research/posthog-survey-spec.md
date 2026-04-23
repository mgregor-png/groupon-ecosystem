# PostHog Quick Survey Spec - Loyalty Tool Usage

**Asana:** https://app.asana.com/1/8437193015852/project/1210682964756930/task/1214151611162880
**Owner:** Martin
**Target launch:** Wed Apr 22
**Target close:** Mon Apr 28 (1 week) or 200 responses, whichever first

---

## Purpose

Get directional, fast, zero-spend signal on three questions that anchor the loyalty research:

1. **Do Groupon coupons users already use cashback tools?** (baseline stacking hypothesis test)
2. **Which ones?** (confirms/refutes Rebecca's SimilarWeb affinity data with first-party evidence)
3. **Would they use a Groupon loyalty tool?** (intent signal)

This is NOT the main survey. Rebecca coordinates with Mark Neary for the funded, incentivized, deeper survey (conjoint + depth). This one is the quick "do we even have evidence pointing the same direction" check.

---

## Survey design (3 questions, ~30 seconds)

### Q1. Do you use cashback or rewards tools when shopping online?
**Type:** Single choice
**Options:**
- Yes, regularly
- Sometimes
- No, never
- I don't know what those are

### Q2. Which cashback or rewards tools do you use?
**Type:** Multi-select (show only if Q1 = "Yes, regularly" or "Sometimes")
**Options:**
- Rakuten
- PayPal Honey
- Capital One Shopping
- Ibotta
- RetailMeNot
- Coupert
- Another one
- I don't remember the name

### Q3. Would you use a Groupon tool that gave you rewards for shopping at other websites (like Nike, Sephora) that you can spend on Groupon deals?
**Type:** Single choice
**Options:**
- Very interested
- Somewhat interested
- Not interested
- Not sure

**No open-text questions.** Protects response rate. Keeps analysis simple.

---

## Targeting

**URL pattern:** New UI coupons pages only.
- Confirm exact URL pattern with the front-end team. Likely candidates: `/coupons/*` served by the new platform; or via the feature flag / experiment cookie that identifies new UI.
- Exclude legacy UI so we are not sampling a different experience.

**User filters:**
- Exclude users who have already seen the survey in the last 30 days
- Exclude bot traffic (PostHog defaults cover most)
- Desktop + mobile (do not restrict)

**Trigger timing:**
- Delay: 12 seconds on page (ensures engagement, not bounce)
- Display: slide-in from bottom-right, dismissable
- Do NOT use a modal overlay (intrusive, hurts CSAT signals)

**Sample rate:**
- Start at 10% of eligible sessions
- If response rate is higher than expected and 200 hit early, throttle down
- If response rate is lower than expected, bump to 25% mid-week

---

## PostHog setup steps (Martin)

1. **Log into Groupon's PostHog** - project TBD, check with analytics team for the right project if there is more than one
2. **Surveys tab -> New survey**
3. **Add the three questions above** in order, with branching logic on Q2 conditional on Q1
4. **Targeting:**
   - URL match: new UI path pattern (confirm with front-end)
   - Display conditions: 12s delay, slide-in, once per user
   - Internal filter: exclude groupon.com staff if there is a cookie or property for that
5. **Thank-you screen** - one line: "Thanks - this helps us decide what we build next"
6. **Preview on staging** before launch
7. **Launch Wed Apr 22 morning**
8. **Check data Thu EOD + Friday morning** - rough aggregate numbers go into the Friday package

---

## Output into the Friday package

- Sample size (n) as of Fri morning
- Q1 answer distribution
- Q2 competitor mention frequency (compares against Rebecca's SimilarWeb affinity: RetailMeNot 1.000 > Rakuten 0.924 > CapOne 0.826 > Honey 0.815)
- Q3 intent distribution
- One-paragraph interpretation: does first-party signal agree with the third-party data, or diverge?

If n is too low (<50) by Friday, report as "preliminary, still collecting" - do not over-interpret.

---

## Questions to escalate to Mark Neary's survey

Leaving these OUT of the PostHog 3-question survey, save for Mark's incentivized deeper study:

- Conjoint: $5 Groupon Bucks (local) vs $5 PayPal cashback vs $5 gift card - perceived value comparison
- Tool switching triggers - what would make you stop using your current cashback tool
- Frequency of use per tool (daily / weekly / monthly)
- Satisfaction and frustrations with current tools
- Bucks redemption preference - online goods vs local experiences vs travel
- Local experiences frequency - how often do you book restaurants/spas/activities today

Rebecca drafts the Mark Neary question set in her subtask; Martin reviews.

---

## Risks to flag in the Friday doc

- **Selection bias:** only new-UI coupons visitors answer. Different from the full Groupon user base.
- **Response bias:** without incentive, highly engaged or highly opinionated users skew the sample.
- **Awareness artifact:** users may under-report tool usage because they do not recognize brand names. Mitigation in Q2 option: "Another one" + "I don't remember the name" captures this honestly.
- **Q3 intent vs behavior gap:** stated intent is a weak proxy for real adoption. Use this as directional signal only.

---

## Decision needed before launch

**Who approves the survey going live on new UI coupons pages?** Ask Rebecca during Thursday product meet if there is a standard approval flow. If yes, route through it. If no, just launch - it is a PostHog survey, not a product change.
