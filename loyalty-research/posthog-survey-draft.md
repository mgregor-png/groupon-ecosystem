# PostHog Quick Survey - Draft Wording (subtask #4)
*Target: new-UI coupons pages | Non-incentivized | Directional signal only | Apr 22 2026*

## Survey configuration

- **Placement:** new-UI coupons pages only (not legacy)
- **Trigger:** after 10 seconds on page OR on scroll-depth 40%, once per user per 30 days
- **Max length:** 3 questions, no free-text (to protect response rate with no incentive)
- **Incentive:** none (deeper + incentivized version lives in Mark Neary's funded survey track)
- **Est. response rate:** 2-5% unincentivized is realistic; below 2% means the UX is wrong
- **Conditional logic:** not supported in the tool. All three questions show to all respondents. Q2 includes an escape option ("Do not remember") so non-users of cashback tools can skip past it gracefully.

## The 3 questions

### Q1 - Current tool usage
> **Do you use cashback or coupon tools when shopping online?**
>
> - Yes, regularly
> - Sometimes
> - No
> - Not sure what those are

Response-shape rationale: 4 options (not 3) adds the "not sure" path. If a meaningful share picks "not sure", the category education gap is material to Groupon's positioning.

### Q2 - Which tools
> **Which do you currently use? (select all that apply)**
>
> - Rakuten
> - PayPal Honey
> - Capital One Shopping
> - Ibotta
> - RetailMeNot
> - Coupert
> - Other
> - None
> - Do not remember

Response-shape rationale:
- 6 competitors map directly to our competitive scope. Order is deliberate (by category scale / overlap with Groupon per SimilarWeb).
- "Other" captured without free-text to stay single-click.
- "None" for users who actively don't use any tool.
- **"Do not remember"** is the escape for respondents who answered "No" or "Not sure what those are" in Q1 - gives them a graceful single-click path out without forcing a guess or a "None" that they may not actually mean. Since PostHog doesn't support conditional logic, this is how we avoid forcing non-users into a false-negative answer that would skew the Q2 concentration analysis.

### Q3 - Willingness to add Groupon
> **Would you use a Groupon cashback tool alongside what you use today?**
>
> - Yes, definitely
> - Probably
> - Maybe
> - Probably not
> - No

Response-shape rationale: 5-point Likert is more informative than 3-point yes/no/maybe. Lets us separate "yes definitely" (high conviction) from "maybe" (soft positive).

"Alongside what you use today" reads cleanly for users who stack AND for users who don't use anything today (they can still answer "Yes, definitely" meaning "I'd try Groupon regardless"). Stays aligned with Rebecca's stacking thesis without forcing non-users into an awkward frame.

## Important framing choices

- **"Cashback or coupon tools"** in Q1 (not just "cashback") - captures Honey / RetailMeNot users who may not self-identify as cashback-savvy. If we say only "cashback", response rate drops because Honey users say "I don't do cashback".
- **"Alongside what you use today"** in Q3 - anchors on Rebecca's stacking thesis. We're NOT asking them to switch; we're measuring slot availability in the existing stack. Critical framing.
- **Groupon not "Groupon Bucks"** in Q3 - don't introduce new terminology in the question. "Bucks" means nothing to users yet.
- **"Do not remember" in Q2** - designed for the No / Not-sure segment from Q1 to have a clean exit when PostHog forces Q2 on everyone. Without it, non-users would be pushed toward "None", which is a different signal ("I actively don't use any" vs "this question doesn't apply to me").

## What we'll learn (and what we won't)

**Will learn:**
- Rough share of coupons-page users who already use any cashback tool (Q1)
- Concentration of competitor usage inside the coupons-page audience (Q2 - filter out "Do not remember" before analysis)
- Raw willingness-to-try signal for Groupon cashback (Q3)

**Won't learn (this needs the Mark Neary funded version):**
- Stacking vs switching behaviour
- Rate sensitivity (conjoint: $5 Bucks vs $5 PayPal vs $5 gift card)
- Frustrations with current tools
- Trigger points for adding or removing a tool
- Demographic cuts (survey of this length can't capture it honestly)

## Launch checklist

- [ ] PostHog survey configured on new-UI coupons pages only (not legacy)
- [ ] 30-day once-per-user cap set
- [ ] Trigger: 10 seconds on page OR 40% scroll depth
- [ ] Skip option visible on every question
- [ ] Funnel instrumented: impression -> response -> question-1-answer -> question-2-answer -> question-3-answer
- [ ] Target: n=500-1000 responses before drawing conclusions
- [ ] Review after 2 weeks; extend or retire

## Analysis cut pre-registered (to avoid p-hacking)

Before the survey runs, the primary cut is:
1. **Q2 stacked bar** showing competitor-usage concentration. **Filter out "Do not remember" responses before building the concentration view** - they represent non-users or unsure-users and would dilute the signal from actual users. Cross-tab against Q1 to confirm the filter: respondents who answered "No" or "Not sure" in Q1 and then picked something other than "None" / "Do not remember" in Q2 are interesting outliers (possibly brand recall without conscious use).
2. **Q3 net positive** ("definitely" + "probably" as single bucket) as a go/no-go directional signal for the Bucks extension investment. Cross-tab against Q1 to see if willingness differs between current cashback users and non-users.

Everything else is secondary / exploratory.
