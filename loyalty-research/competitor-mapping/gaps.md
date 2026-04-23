# Competitor Mapping - Gaps and Follow-Up Actions
*2026-04-22 | Inventory of what the automated capture could NOT get, with mitigation*

## Priority-ordered gap list

### P1 - Required for Friday package

| Gap | Owner | Mitigation path | Blocker? |
|---|---|---|---|
| **Chrome Web Store live install counts (Honey, Rakuten, Cap One Shopping, Coupert)** - Google consent wall blocks automated capture from CZ IP | Martin | Screenshot manually in a logged-in-to-Google session; takes 5 minutes, save to `competitor-mapping/<slug>/05-chrome-web-store-manual.png` | No (fast fix) |
| **Rakuten US web flows (signup form, welcome bonus page, Big Fat Check FAQ, Safari install walkthrough)** - geoblocked from CZ IP, redirects to EU chooser | Daniel (US content team) | Per existing subtask #6 - 10-min screen recording + screenshots from US IP | **YES - high risk if Daniel doesn't respond** |
| **Slickdeals landing / corporate pages** - Cloudflare bot challenge blocks automated capture | Martin | Screenshot manually in normal browser session with Cloudflare challenge solved; 5 min | No |
| **Honey terms page content** (to verify "not your property, not money, no value" language or its removal) | Martin | Scroll past cookie banner manually and capture | No |
| **Current Chrome install count for Honey** - 12M at Dec 2025, April 2026 number not publicly disclosed | Martin | Chrome Web Store manual screenshot; dovetails with the Chrome Web Store consent-wall gap above | No |

### P2 - Strengthens the package but not blocking

| Gap | Owner | Mitigation path |
|---|---|---|
| **Logged-in user experience** for Rakuten, Cap One, Honey, Coupert (welcome email, bonus-progress UI, first merchant offer, extension activation) | Martin | Real signups per subtask #1; burner emails and + aliases recommended |
| **Safari extension in action on Nike.com** (Rebecca's canonical test case) | Martin (Cap One, Honey, Coupert) + Daniel (Rakuten US) | Screen recordings; subtask #1 |
| **Mobile Safari rendering** of each landing page | Martin | Open on phone, screenshot; optional - desktop captures are sufficient for most pattern analysis |
| **Ibotta how-it-works page** - /how-it-works is 404, correct URL is in the footer nav | Anyone | Click the footer link, update `_capture.py` with correct URL, re-run for that one target |
| **Cap One Shopping how-it-works page** - /how-it-works is 404 | Anyone | Find the right URL via site search; same low-effort fix |
| **Ibotta investor relations latest filing / 10-K PDFs** - IR page captured but the actual 10-K content is on a linked PDF | Anyone | Download 10-K PDF separately if we need to cite specific passages |

### P3 - Nice to have, not critical

| Gap | Owner | Mitigation path |
|---|---|---|
| Below-the-fold content of all landing pages (testimonials, FAQ, footer) | Anyone | Full-page PNG already captured (non-fold versions). Just browse them manually when preparing the Friday slides. |
| RetailMeNot with GDPR consent accepted | Anyone | Click "Accept All" and re-capture one page; 2 min |
| **Ibotta vs RetailMeNot merchant-overlap comparison** - both show partial merchant grids on landing; could cross-reference | Rebecca (she has the Florence scrape) | Her existing subtask covers RetailMeNot + Cap One merchant overlap; Ibotta can fold in |

---

## Known structural limits of automated capture

These cannot be closed by tooling alone - documenting for context:

1. **Authenticated experience** is out of scope for this approach. Headless Chromium does not create accounts; it captures what an anonymous visitor sees. Any claim about "after signing up, the user sees X" requires a human session.
2. **Interactive states** (hover tooltips, dropdown menus, multi-step modals, video autoplay) are not captured by static PNG snapshots. Where a competitor's signup form has dynamic validation or conditional fields (Cap One, Rakuten likely), only the initial state is visible in the capture.
3. **Geographic content variation** is captured from one IP only. For every competitor except Rakuten, the CZ-IP version appears identical to what a US visitor would see (per spot-checks via US proxies in prior research). Rakuten is the exception.
4. **Dynamic content personalisation** (e.g. Amazon-style "recommended for you") doesn't apply to pre-auth captures but does apply to logged-in captures. Noting for completeness.

---

## Recommended next actions (next 24h)

1. **Martin, today EOD:** Open Chrome Web Store (logged into Google) and screenshot Honey, Rakuten, Cap One Shopping, Coupert extension pages. Save as `competitor-mapping/<slug>/05-chrome-web-store-manual.png`. Update `pattern-analysis.md` currency-clarity table with the live install counts.
2. **Martin, today EOD:** Screenshot Slickdeals landing in a normal browser (solve the Cloudflare challenge once). Save as `competitor-mapping/slickdeals/01-landing-manual.png`.
3. **Martin, today EOD:** Open Honey T&Cs in a normal browser, dismiss the cookie banner, capture the "your account" / "your property" / "expiration" / "redemption" sections. Save as `competitor-mapping/honey/04-terms-manual.png`. This is where the legal language for the final report's trust section is verified.
4. **Daniel (per subtask #6):** 10-min screen recording of Rakuten US. Save to G Drive or Slack back to Martin.
5. **Optional (Martin or anyone):** Find correct /how-it-works URLs for Cap One Shopping and Ibotta, re-run the capture script for those two URLs only.

---

## What NOT to spend time on

- Do not re-run the full capture script. It ran clean 82/82 screenshot files, 7/7 competitors covered. Only re-run individual failing targets.
- Do not attempt to automate around Cloudflare (Slickdeals). Human screenshot is fine, and Slickdeals is a partnership workstream, not the primary loyalty competitor.
- Do not attempt to automate signup flows. Burner signups by a human with a new email are faster and produce richer artefacts (welcome emails, activation screens) that automated tools would miss anyway.
- Do not invest in higher-resolution captures. 1440x900 is the standard laptop viewport; desktop 2560x1440 captures make for larger files without meaningful new information.

---

## Handoff for the Friday package

The inventory here fits Adam's Apr 20 transparency rule directly: every pattern claim in `pattern-analysis.md` has a PNG file. The G Drive upload path is one step:

```
Upload: projects/groupon-ecosystem/loyalty-research/competitor-mapping/
To:     Shared Drive -> Product -> Cashback research -> loyalty-research/competitor-mapping/
```

Total folder size: ~30 MB. 82 PNGs + 3 markdown docs + 2 Python scripts + 1 JSON inventory + 1 error log. Uploads in under a minute.
