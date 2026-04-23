# Groupon Ecosystem

Consolidated project covering the Groupon ecosystem framing: retention (Safari extension), monetisation (cashback, Groupon Bucks), and the overarching two-problem narrative. Merged from the former `cashback` project and the `groupon-ecosystem` strategy board repo on 2026-04-23.

## Metadata
- **Status:** Active
- **GitHub repo:** https://github.com/mgregor-png/groupon-ecosystem
- **GitHub Pages:** strategy board served from `index.html`
- **Last updated:** 2026-04-23

## Scope
Two problems, one ecosystem:
- **Problem A - Retention:** Users leave Groupon after redeeming a coupon. Solutions: Safari extension ("Save Everywhere"), Genie browser extension.
- **Problem B - Traffic:** Anonymous organic Coupons traffic not converting to Groupon shoppers. Solutions: cashback on Coupons pages, Groupon Bucks upsell, promo tests.

## Workstreams

### Strategy board (published)
- `index.html` - two-problem framing with Groupon Bucks bridge, Safari hero. Pages homepage.
- `assets/` - strategy board assets.

### Safari extension / Save Everywhere
- `deliverables/save-everywhere-final.html` - v5 strategy report (11 sections, iOS 84% confirmed, $4-5M floor).
- `deliverables/safari-extension-prototype.html` - 10-screen Stitch prototype.
- `deliverables/safari-extension-video.html` - video version.
- `deliverables/save-everywhere-rebecca-structure-*.html` - Rebecca-structure variants.
- `deliverables/save-everywhere-video.html`, `save-everywhere-v3.html`, `save-everywhere-prototype-v2.html`.

### Cashback / Monetisation
- `context.md` - cashback project context (POC 32 MD, Dusan's promo-first direction).
- `alternative-monetisation-brainstorm.{html,md,v2.html}` - alt-monetisation exploration.
- `alternative-monetisation-presentation.html` - presentation deck.
- `deliverables/coupons-initiatives-overview.html` - Problem B overview, 3 scenarios ($550K/$7M/$20M).
- `deliverables/ecosystem-recommendation-*.html` - recommendation variants (Adam/Becky versions).
- `promo-banners-showcase.html`, `promo-copy-*.html` - promo artefacts.

### Loyalty research (Apr 21)
- `loyalty-research/` - final merged report + 6 mechanic cards + Slickdeals workstream.
- `loyalty-research/competitor-mapping/` - 82 screenshots across 7 competitors (Capital One Shopping, Coupert, Honey, Ibotta, Rakuten, RetailMeNot, Slickdeals) plus `pattern-analysis.md`, `gaps.md`, `_inventory.json`, `_capture.py`.

## Key inputs / source material
- `Coupons _ Genie _ Cashback _ Groupon EcoSystem (2).pdf` - original ecosystem framing deck.
- `Permalink - with Platform.xlsx` - merchant / platform data.
- `inputs/` - raw source material (add new files here).
- `knowledge/` - processed knowledge and synthesis.

## Inputs processing
- Drop raw inputs into `inputs/` and log them in `inputs/.processed.md`.
- Processed knowledge goes into `knowledge/`.

## Folder map
- `index.html` + `assets/` - published strategy board.
- `deliverables/` - all output artefacts (HTML decks, reports).
- `loyalty-research/` - competitor deep-dive with screenshots.
- `inputs/` - raw source material.
- `knowledge/` - processed knowledge.
- `meetings/`, `meeting-notes.md` - meeting records.
- `tasks/` - work plans, weekly TODOs.
- `context.md` - cashback project context.
- `session-log.md` - session history.

## Domain Learnings
<!-- Claude captures key findings here as work progresses.
     One bullet per finding. Group by topic. Max ~100 lines. -->

### Ecosystem framing
- Problem A (retention) and Problem B (traffic) are the organising frame; Safari extension is Problem A, cashback is Problem B [source: Apr 16 initiatives overview].
- Safari + Genie are Problem A solutions; they're reference links in the Problem B overview, not deep-dives [source: Apr 16].

### Safari extension (Save Everywhere)
- iOS share of Groupon audience confirmed at 84% via Tableau (previously estimated 55%) - significantly strengthens the $4-5M revenue floor [source: Apr 14 v5 report].
- Revenue sizing anchored on conservative $4-5M floor; upside case $4-25M [source: Rebecca 1:1 Apr 14].
- Bucks economics framed as "lever not blocker" per Rebecca [source: Apr 14].

### Cashback
- Net economics: $1.13/user net (not $3.81 gross) - Adam's correction applied [source: Apr 16].
- Revenue range: $4-18M, not $4-25M [source: Apr 16].
- Downside (-$500K) > upside (+$220K) with current assumptions - retention play not revenue play [source: Apr 16].
- 40-50 MD eng estimate, two-part model with voucher upsell [source: Rebecca cashback strategy doc].
- Dusan direction post-MBR: don't start 32 MD POC yet - test hypothesis with simple promo on Coupons pages first [source: context.md].

### Loyalty research (Apr 21)
- Delivered 3 days early; final report at `loyalty-research/` [source: Apr 21 session].
- 7 competitors fully mapped: Capital One Shopping, Coupert, Honey, Ibotta, Rakuten, RetailMeNot, Slickdeals.
