#!/usr/bin/env python3
"""Capture competitor landing / signup / extension / help pages as PNGs for pattern analysis.

Run after: pip install --user playwright && python -m playwright install chromium
"""
import asyncio
import json
import os
import site
import sys
from datetime import datetime, timezone
from pathlib import Path

# user site-packages (playwright installed to user-level)
site.addsitedir(os.path.expanduser("~/Library/Python/3.14/lib/python/site-packages"))

from playwright.async_api import async_playwright, TimeoutError as PWTimeout  # type: ignore

BASE = Path(__file__).parent
LOG = BASE / "_errors.log"
INVENTORY = BASE / "_inventory.json"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
VIEWPORT = {"width": 1440, "height": 900}

# Structure: (slug, label, url, wait_selector_optional)
TARGETS = [
    # RAKUTEN (expect EU redirect from CZ IP)
    ("rakuten", "01-landing", "https://www.rakuten.com/", None),
    ("rakuten", "02-signup-page", "https://www.rakuten.com/join", None),
    ("rakuten", "03-how-it-works", "https://www.rakuten.com/help/article/how-does-rakuten-work-360002117047", None),
    ("rakuten", "04-big-fat-check-faq", "https://www.rakuten.com/blog/rakuten-big-fat-check-schedule-faqs/", None),
    ("rakuten", "05-safari-walkthrough", "https://www.rakuten.ca/button/safari/walkthrough", None),
    ("rakuten", "06-referral-page", "https://www.rakuten.com/referral", None),
    ("rakuten", "07-chrome-web-store", "https://chromewebstore.google.com/detail/rakuten-cash-back-browser/chhjbpecpncaggjpdakmflnfcopglcmi", None),
    ("rakuten", "08-ios-app-store", "https://apps.apple.com/us/app/rakuten-cash-back-deals/id723134859", None),
    ("rakuten", "09-rakuten-plus", "https://www.rakuten.com/rp/member/join", None),

    # CAPITAL ONE SHOPPING
    ("capital-one-shopping", "01-landing", "https://capitaloneshopping.com/", None),
    ("capital-one-shopping", "02-signup-signin", "https://capitaloneshopping.com/sign-in", None),
    ("capital-one-shopping", "03-how-it-works", "https://capitaloneshopping.com/how-it-works", None),
    ("capital-one-shopping", "04-rewards-page", "https://capitaloneshopping.com/rewards", None),
    ("capital-one-shopping", "05-chrome-web-store", "https://chromewebstore.google.com/detail/capital-one-shopping-save/nenlahapcbofgnanklpelkaejcehkggg", None),
    ("capital-one-shopping", "06-ios-app-store", "https://apps.apple.com/us/app/capital-one-shopping-save-now/id1089294040", None),
    ("capital-one-shopping", "07-ios-safari-extension", "https://apps.apple.com/us/app/capital-one-shopping-extension/id1477110326", None),

    # PAYPAL HONEY
    ("honey", "01-landing", "https://www.joinhoney.com/", None),
    ("honey", "02-features-droplist", "https://www.joinhoney.com/features/droplist", None),
    ("honey", "03-features-gold", "https://www.joinhoney.com/features/honeygold", None),
    ("honey", "04-terms", "https://www.joinhoney.com/terms", None),
    ("honey", "05-chrome-web-store", "https://chromewebstore.google.com/detail/honey-automatic-coupons-r/bmnlcjabgnpnenekpadlanbbkooimhnj", None),
    ("honey", "06-ios-app-store", "https://apps.apple.com/us/app/paypal-honey-coupons-rewards/id1358499588", None),
    ("honey", "07-paypal-help-bundled-extension", "https://www.paypal.com/us/cshelp/article/what-is-the-paypal-honey-mobile-safari-extension-help593", None),
    ("honey", "08-help-safari-mobile", "https://help.joinhoney.com/article/350-honey-mobile-safari-extension", None),

    # IBOTTA
    ("ibotta", "01-landing", "https://home.ibotta.com/", None),
    ("ibotta", "02-how-it-works", "https://home.ibotta.com/how-it-works/", None),
    ("ibotta", "03-ipn-performance-network", "https://ipn.ibotta.com/", None),
    ("ibotta", "04-ios-app-store", "https://apps.apple.com/us/app/ibotta-cash-back-savings-app/id559887125", None),
    ("ibotta", "05-investor-relations", "https://investors.ibotta.com/", None),

    # RETAILMENOT
    ("retailmenot", "01-landing", "https://www.retailmenot.com/", None),
    ("retailmenot", "02-guaranteed-cashback", "https://www.retailmenot.com/cashback", None),
    ("retailmenot", "03-ios-app-store", "https://apps.apple.com/us/app/retailmenot-cash-back-codes/id376121913", None),

    # COUPERT
    ("coupert", "01-landing", "https://www.coupert.com/", None),
    ("coupert", "02-welcome", "https://www.coupert.com/welcome", None),
    ("coupert", "03-cashback-help", "https://help.coupert.com/cash-back/coupert-cash-back/", None),
    ("coupert", "04-chrome-web-store", "https://chromewebstore.google.com/detail/coupert-automatic-coupons/mfidniedemcgceagapgdekdbmanojomk", None),
    ("coupert", "05-vs-honey-blog", "https://www.coupert.com/research/coupert-vs-honey-which-coupon-extension-performs-best-in-2025", None),

    # SLICKDEALS (partnership workstream)
    ("slickdeals", "01-landing", "https://slickdeals.net/", None),
    ("slickdeals", "02-corp-how-it-works", "https://corp-site.slickdeals.net/how-slickdeals-works/", None),
    ("slickdeals", "03-api-sales", "https://corp-site.slickdeals.net/api-sales/", None),
    ("slickdeals", "04-advertising-audience", "https://sales.slickdeals.net/audience", None),
]


async def capture_one(browser, slug, label, url, wait_selector):
    out_dir = BASE / slug
    full_png = out_dir / f"{label}.png"
    fold_png = out_dir / f"{label}-fold.png"
    meta = {
        "slug": slug,
        "label": label,
        "url": url,
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "user_agent": UA,
        "viewport": VIEWPORT,
    }
    context = await browser.new_context(
        user_agent=UA,
        viewport=VIEWPORT,
        locale="en-US",
        # Accept-Language to soften EU redirects when possible
        extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
    )
    page = await context.new_page()
    status = "ok"
    final_url = url
    try:
        response = await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        if response:
            meta["http_status"] = response.status
        # small settle time for late-loading hero content
        await page.wait_for_load_state("networkidle", timeout=10000)
    except PWTimeout:
        status = "timeout_but_captured"
    except Exception as e:
        status = f"error:{type(e).__name__}:{e}"
    try:
        final_url = page.url
        meta["final_url"] = final_url
        meta["title"] = await page.title()
        # fold screenshot (viewport-sized)
        await page.screenshot(path=str(fold_png), full_page=False)
        # full-page
        await page.screenshot(path=str(full_png), full_page=True)
        size_full = full_png.stat().st_size if full_png.exists() else 0
        size_fold = fold_png.stat().st_size if fold_png.exists() else 0
        meta["fold_bytes"] = size_fold
        meta["full_bytes"] = size_full
    except Exception as e:
        status = f"{status};screenshot_err:{type(e).__name__}:{e}"
    meta["status"] = status
    await context.close()
    return meta


async def main():
    inventory = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # parallelize with semaphore (5 concurrent)
        sem = asyncio.Semaphore(5)

        async def bounded(args):
            async with sem:
                return await capture_one(browser, *args)

        results = await asyncio.gather(*[bounded(t) for t in TARGETS])
        await browser.close()
    inventory.extend(results)
    INVENTORY.write_text(json.dumps(inventory, indent=2))

    ok = sum(1 for r in inventory if r.get("status") == "ok")
    timeout = sum(1 for r in inventory if "timeout" in r.get("status", ""))
    err = sum(1 for r in inventory if "error" in r.get("status", ""))
    print(f"Done. {ok} OK / {timeout} timeout / {err} error / {len(inventory)} total.")
    # dump errors
    errs = [r for r in inventory if r.get("status") != "ok"]
    if errs:
        LOG.write_text("\n".join(f"{r['slug']}/{r['label']} ({r['url']}): {r['status']}" for r in errs))
        print(f"  wrote {len(errs)} error lines to {LOG}")


if __name__ == "__main__":
    asyncio.run(main())
