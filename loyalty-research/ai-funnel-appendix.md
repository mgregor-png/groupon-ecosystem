# AI Funnel Transparency Appendix
*Loyalty Mechanics Reverse Engineering for Groupon | 2026-04-21*
*Per Adam's 2026-04-20 request: prompts used, raw data, what AI did, iteration log.*

---

## 1. What AI did (in plain English)

I used Claude Code (Opus 4.7, 1M context) to:
1. Fetch Rebecca's Google Doc research directly from Drive via the `gws docs documents get` CLI (no copy-paste, direct API). Result: 4.5MB JSON, parsed to 69K of clean markdown.
2. Spawn **5 parallel research subagents**, each with an independent WebSearch tool. Each agent ran 2-6 search rounds on a specific competitor or theme, wrote findings to a `raw/*.md` file, and returned a 300-word summary.
3. Read both Rebecca's draft and all 5 raw files, then synthesised a merged final report (this document's companion).
4. Applied a strict honesty protocol: label every claim `[Data]` / `[Estimate]` / `[Assumption]` / `[Opinion]`, date everything, flag confidence High / Medium / Low, declare data gaps rather than guess.

I did NOT use AI to generate numbers, invent statistics, or produce polished prose from thin air. Where a number isn't cited to a source, it's labelled `[Estimate]` or listed as a data gap.

## 2. Why this structure (and not a single all-in-one agent)

Three reasons for parallel specialist agents over one generalist:
- **Depth**: 6 search rounds per competitor beats a single scan. Rakuten's Big Fat Check mechanics and Capital One's $45 install trigger needed separate drill-downs.
- **Context hygiene**: Each agent returns a 300-word summary, not its full transcript. The main session stays uncluttered, which matters for the merge step.
- **Honest audit trail**: Separate `raw/*.md` files per agent make it trivial to trace any claim in the final report back to its research origin.

## 3. Agent roster and scope

| Agent | Competitor / Theme | Search rounds | Output file |
| --- | --- | --- | --- |
| A1 | Rakuten loyalty mechanics | 5-6 deep | `raw/rakuten-mechanics.md` |
| A2 | Capital One Shopping mechanics | 5-6 deep | `raw/capital-one-shopping-mechanics.md` |
| A3 | PayPal Honey mechanics + trust collapse | 5-6 deep | `raw/honey-mechanics-and-cautionary-tale.md` |
| A4 | Tier-2 scan (Ibotta, RetailMeNot, Coupert) + Starbucks pure-loyalty benchmark (later dropped from final) | 2-3 scan + 3-4 Starbucks | `raw/tier2-scan-and-starbucks-benchmark.md` |
| A5 | Slickdeals partnership feasibility (NOT loyalty) | 4-5 | `raw/slickdeals-partnership-feasibility.md` |

## 4. Prompts (verbatim, trimmed for length)

Full prompts are in the session transcript. Core instructions common to all five:

> - Label every claim: `[Data]` / `[Estimate]` / `[Assumption]` / `[Opinion]`
> - Rate confidence: High / Medium / Low
> - Date every data point. Flag anything >12 months old.
> - NO em-dashes, use plain hyphens.
> - Do not fabricate numbers. "DATA GAP: could not find X" is always better than a guess.
> - Be honest about weaknesses. If users complain, surface the complaints.
> - 5-6 search rounds minimum (Tier 1) / 2-3 rounds (Tier 2 / partnership)

Per-agent focus:
- **A1 (Rakuten):** quarterly payout mechanics (Big Fat Check), Rakuten+ paid tier, Amex/Bilt partnerships, in-store linked card, LTV signals from Rakuten Group filings, Safari iOS extension UX. See 20-point research brief in prompt.
- **A2 (Capital One Shopping):** the $45 install incentive triggers and conditions, Shopping Credits soft-currency economics (earn rate, breakage, gift-card-only redemption), App Store 4.9 / 960K reviews authenticity, Safari #2 ranking, is Capital One investing or in maintenance mode.
- **A3 (Honey):** MegaLag scandal chronology (Dec 2024 first video, Dec 2025 second), class-action status, PayPal app bundling activation flow, Chrome user loss month-by-month, what Honey still does well post-scandal, primary lesson for Groupon on trust.
- **A4 (Tier-2 + Starbucks):** where April-2026 surface doc is THIN (Ibotta IPN B2B2C, RetailMeNot Feb-2026 1% floor, Coupert post-Honey migration), plus Starbucks stars + tiering + mobile pre-load as pure-loyalty benchmark. Starbucks was subsequently dropped from the final report after the agent's honest "does not port" finding was accepted.
- **A5 (Slickdeals):** partnership economics for Goods replacement, audience overlap with Groupon, UGC moat Groupon can't build in-house, precedent partnerships, challenge the Dusan thesis honestly.

## 5. Iteration log

| Step | What changed, why |
| --- | --- |
| Initial intake | User brief gave me asymmetric tier structure (Tier 1 deep, Tier 2 scan, Tier 3 partnership) and an open question on pure-loyalty benchmark. |
| Research depth | Scored 8/9 on the startup-competitors skill's matrix (Deep), but deviated to Deep+scan+partnership mix rather than uniform Deep. Honest because the brief was asymmetric. |
| Starbucks vs Bonvoy | Recommended Starbucks over Marriott Bonvoy. Reason: Starbucks is daily/weekly frequency (matches habit goal), Bonvoy is low-frequency travel (wrong cadence). |
| Starbucks dropped | After research, Starbucks was removed from the final report. Honest finding from agent A4: the habit driver is pre-loaded stored value + mobile order, which does not port to Groupon (episodic, unpredictable-basket commerce). Raw research preserved in `raw/` for audit trail; benchmark removed from recommendation set. |
| Output shape pivot | Default skill produces battle cards. Switched to mechanic cards because Groupon isn't selling against Rakuten's sales team — we're learning from them. Battle cards would have been the wrong artifact. |
| Rebecca merge discovery | After fetching Rebecca's doc, found it was much richer than the brief implied (full report structure, 60+ cited sources, stacking-vs-switching thesis). Merge strategy shifted from "use her as draft input" to "use her structure as the skeleton, add depth/benchmark/partnership." |
| Honesty hits | Agents were instructed to surface competitor STRENGTHS and churn signals, not just weaknesses. Cherry-picking weaknesses would have been bad competitive intelligence. |

## 6. What AI is NOT good at here (transparency)

- **Primary customer research.** AI cannot replace the Phase 2 (survey) and Phase 4 (depth interviews) in Rebecca's research programme. Mechanics can be reverse engineered from public data; *why users feel loyal* cannot.
- **Internal data access.** AI cannot see Groupon's BI. Section 5.7 of Rebecca's doc (8 internal data requests) is unchanged by this AI pass.
- **Future-casting.** The Tier-1 teardowns reflect public mechanics in market today. If Rakuten launches a new tier next month, this report will be out of date.
- **Negotiation and politics.** Slickdeals partnership feasibility assesses whether it's the right *kind* of deal; the actual deal terms will be negotiated, not reverse engineered.

## 7. Raw research files (audit trail)

All raw outputs preserved in `raw/`:
- `rebecca-draft.md` — extracted from Rebecca's Google Doc via gws CLI
- `rakuten-mechanics.md` — agent A1
- `capital-one-shopping-mechanics.md` — agent A2
- `honey-mechanics-and-cautionary-tale.md` — agent A3
- `tier2-scan-and-starbucks-benchmark.md` — agent A4
- `slickdeals-partnership-feasibility.md` — agent A5

Every claim in the final report traces to one of these six files plus Rebecca's original citations [1]-[60].

## 8. Reproducibility

This research can be re-run by any team member:
1. `gws docs documents get --params '{"documentId":"1tck7N5UlkSWeSSNKpg-tWb2-VrUVeipEJR9XBLRxfUY"}'` — fetch Rebecca's doc
2. Replay the five agent prompts (above) in any Claude Code session with WebSearch enabled
3. Diff new raw files vs existing ones to see what changed in the market

The prompts are the actual audit; the document is the synthesis.
