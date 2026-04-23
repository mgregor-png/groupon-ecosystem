# Intake — Loyalty Mechanics Reverse Engineering for Groupon

**Date:** 2026-04-21
**Skill:** startup-competitors (asymmetric Deep)
**Source:** Martin Gregor / Adam Ward (Coupons). Builds on Apr 20 Rebecca debrief.
**Existing base doc:** `projects/groupon-ecosystem/knowledge/competitor-ecosystem-research-2026-04.md` (surface pass, 8 competitors)

## Goal
Identify the loyalty mechanics that will drive **weekly** Groupon habit formation across coupons + core, using competitor reverse engineering as the evidence base. Frame the opportunity as **$40M+ retention uplift**, not $4M coupon commission.

Safari extension is a delivery surface. Loyalty is the proposition. No team currently owns loyalty at Groupon.

## Competitors (asymmetric tiering)

**Tier 1 — Deep loyalty reverse engineering**
- Rakuten (cashback + Safari + longest-running, quarterly payout, Rakuten+ paid tier, points partnerships)
- Capital One Shopping (soft currency = Bucks inspiration, $45 install incentive, gift-card-only redemption)
- PayPal Honey (iOS Safari leader + cautionary tale post-2024 scandal)

**Tier 2 — Scan, top up the April doc**
- Ibotta (CPG / IPN B2B2C, $342M rev)
- RetailMeNot (1% cashback floor Feb 2026, 100M+ social reach)
- Coupert (post-Honey challenger, $1 withdrawal minimum hook)

**Tier 3 — Partnership feasibility, NOT loyalty**
- Slickdeals (UGC community, Dusan sees as #1 partner to replace Goods on core)

**Pure-loyalty benchmark (no Safari extension)**
- ~~Starbucks~~ — researched as pure-loyalty benchmark, then dropped from the final report. Honest finding: the habit engine is pre-loaded stored value + mobile order, which does not port to episodic commerce. Raw research preserved at `raw/tier2-scan-and-starbucks-benchmark.md`. Marriott Bonvoy was also considered and skipped (wrong frequency cadence).

## Research depth
Asymmetric Deep — 5 agents. 5-6 search rounds on Tier 1, 2-3 rounds on Tier 2 / benchmark / partnership.

## Deliverables
1. `loyalty-mechanics-teardown.md` — main synthesis (mechanics x competitor matrix, adoption order, commission cost)
2. `mechanic-cards/{mechanic}.md` — per-mechanic deep dives (signup bonus, soft currency, quarterly payout, tiering, push, email, etc.)
3. `partnership-feasibility-slickdeals.md` — standalone Goods replacement analysis
4. `data-gaps.md` — internal data we need (Ernesto, Mark Brenda, mobile)
5. `ai-funnel-appendix.md` — prompts, raw outputs, iteration log (Adam's Apr 20 requirement)
6. `loyalty-mechanics-final.md` — final merged report with Rebecca's research (Google Doc, fetched via gws)

## Constraints
- Distribution: NOT public GitHub Pages. Private repo / Drive / Groupon IQ.
- Style: no em-dashes, plain hyphens only.
- Label every major claim: [Data] [Estimate] [Assumption] [Opinion].
- Flag confidence: High / Medium / Low.
- Date everything; flag >12 months.
- Friday Apr 24, 1pm CET deliverable: rough-cut, not polished.
