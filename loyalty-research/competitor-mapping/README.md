# Competitor Visual Mapping - Inventory & Provenance
*Captured 2026-04-22 | Source: automated Playwright capture from Martin's Czech Republic IP*

## What this is

Headless-Chromium captures of 7 competitors' public pre-authentication surfaces (landing pages, signup forms, help center mechanic pages, Chrome Web Store listings, iOS App Store listings). Intended as:
1. Visual evidence backing the loyalty-mechanics-final.md report
2. Pattern-analysis input (see `pattern-analysis.md`)
3. Primary-source screenshots for Friday's Adam package (upload this folder to G Drive Shared Drive -> Product -> Cashback research -> loyalty-research/competitor-mapping/)

## Capture provenance

- **Date:** 2026-04-22
- **Tool:** Playwright 1.58.0 + Chromium 1208
- **Script:** `_capture.py` (initial run, 41 URLs) + `_retry.py` (Ibotta + RetailMeNot retries with less strict load strategy)
- **User agent:** Safari 17.5 on macOS Sonoma (desktop)
- **Viewport:** 1440x900 (desktop at typical laptop resolution)
- **Location:** Czech Republic (EU) IP - affects results for Rakuten (hard geoblock), RetailMeNot (GDPR cookie wall), Slickdeals (Cloudflare bot challenge), Chrome Web Store (Google consent wall)
- **Output:** full-page PNG + fold (above-the-fold) PNG per URL = 82 total PNGs
- **Inventory file:** `_inventory.json` (per-URL metadata: http status, final URL, page title, byte counts, errors)

## Competitor coverage

| Competitor | URLs captured | Key captures that worked | Known limitations from CZ IP |
|---|---|---|---|
| Rakuten | 9 | EU geoblock landing, iOS App Store (US content), referral, Big Fat Check FAQ (geoblocked too) | rakuten.com and every transactional path auto-redirect to an EU regional chooser (FR/DE/ES only). Rakuten US is effectively closed to EU residents - a competitive opening for Groupon in EU. Daniel dependency confirmed critical. |
| Capital One Shopping | 7 | Landing (with aggressive signup modal), iOS App Store, Safari extension App Store, rewards page | /how-it-works returns 404; the URL structure has changed. Chrome Web Store needs Google cookie acceptance. |
| PayPal Honey | 8 | Landing, Honey Gold features, Droplist, terms, PayPal help593 bundled-extension article | Chrome Web Store needs Google consent. Terms page cookie banner blocked fold capture. |
| Ibotta | 5 | Landing, IPN B2B2C page, iOS App Store, investor relations | /how-it-works path returns 404; footer uses different URL |
| RetailMeNot | 3 | Landing (GDPR consent overlay), cashback, iOS App Store | GDPR consent overlay blocks content above the fold; second-pass capture still shows overlay |
| Coupert | 5 | Landing, welcome, Chrome Web Store (blocked), cashback help center, Coupert-vs-Honey blog | Google consent wall on Chrome Web Store |
| Slickdeals | 4 | API sales page, advertising audience page | **slickdeals.net hard-walls with Cloudflare bot challenge** - no landing-page capture possible via automated browsing. Partnership BD will need to access via authenticated human session. |

## File structure

```
competitor-mapping/
├── README.md                           # this file
├── pattern-analysis.md                 # cross-competitor pattern findings
├── gaps.md                             # what's missing and how to close it
├── _capture.py                         # reproducible capture script
├── _retry.py                           # retry script for font-load + JS-redirect failures
├── _inventory.json                     # JSON metadata per URL
├── _errors.log                         # errors from first capture pass
├── rakuten/                            # 18 PNGs (9 URLs x 2 formats)
├── capital-one-shopping/               # 14 PNGs (7 URLs x 2)
├── honey/                              # 16 PNGs (8 URLs x 2)
├── ibotta/                             # 10 PNGs (5 URLs x 2)
├── retailmenot/                        # 6 PNGs (3 URLs x 2)
├── coupert/                            # 10 PNGs (5 URLs x 2)
└── slickdeals/                         # 8 PNGs (4 URLs x 2)
```

## File naming convention

Within each competitor folder:
- `NN-slug.png` = full-page screenshot
- `NN-slug-fold.png` = above-the-fold (viewport-sized, 1440x900) screenshot
- `NN` (01, 02, ...) = capture order within the competitor, corresponds to `_capture.py` TARGETS list

## How to re-run

```bash
cd projects/groupon-ecosystem/loyalty-research/competitor-mapping
python3 _capture.py   # full run
# or
python3 _retry.py     # just the failed targets
```

Requires `pip install --user playwright && python -m playwright install chromium` one-time setup.

## Reproducibility notes

- Screenshots reflect the **public pre-auth experience from a CZ IP** at the captured moment. US-visible content (behind Rakuten geoblock) is different and requires Daniel's US capture.
- Cookie / GDPR / bot-protection overlays visible in several fold captures are genuine pre-auth friction that matters for the analysis, not just capture artifacts.
- Automated capture cannot reproduce mouse-hover states, modal interactions, or authenticated flows. Those are the human-capture portion of subtask #1.

## Provenance for Adam's package

Every claim in `pattern-analysis.md` is traceable to a specific PNG file in this folder. When the Friday package includes a competitor mechanic claim, the PNG lives here as evidence. This is what Adam's Apr 20 transparency rule translates to at the visual level.
