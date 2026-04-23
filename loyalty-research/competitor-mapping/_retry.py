#!/usr/bin/env python3
"""Retry failed captures with more forgiving load strategy (no networkidle, fixed wait, no font-loading wait)."""
import asyncio
import os
import site
from datetime import datetime, timezone
from pathlib import Path

site.addsitedir(os.path.expanduser("~/Library/Python/3.14/lib/python/site-packages"))

from playwright.async_api import async_playwright, TimeoutError as PWTimeout  # type: ignore

BASE = Path(__file__).parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
VIEWPORT = {"width": 1440, "height": 900}

TARGETS = [
    # IBOTTA retries (font load timeout in first pass)
    ("ibotta", "02-how-it-works", "https://home.ibotta.com/how-it-works/"),
    ("ibotta", "03-ipn-performance-network", "https://ipn.ibotta.com/"),
    ("ibotta", "04-ios-app-store", "https://apps.apple.com/us/app/ibotta-cash-back-savings-app/id559887125"),
    ("ibotta", "05-investor-relations", "https://investors.ibotta.com/"),
    # RETAILMENOT retries (context destroyed by JS redirect, socket error)
    ("retailmenot", "01-landing", "https://www.retailmenot.com/"),
    ("retailmenot", "02-guaranteed-cashback", "https://www.retailmenot.com/cashback"),
    ("retailmenot", "03-ios-app-store", "https://apps.apple.com/us/app/retailmenot-cash-back-codes/id376121913"),
]


async def capture(browser, slug, label, url):
    out_dir = BASE / slug
    full_png = out_dir / f"{label}.png"
    fold_png = out_dir / f"{label}-fold.png"
    ctx = await browser.new_context(
        user_agent=UA,
        viewport=VIEWPORT,
        locale="en-US",
        extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
    )
    page = await ctx.new_page()
    status = "ok"
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
    except PWTimeout:
        status = "goto_timeout"
    except Exception as e:
        status = f"goto_err:{type(e).__name__}"
    # fixed wait for lazy content
    try:
        await page.wait_for_timeout(4000)
    except Exception:
        pass
    # Screenshot without waiting for fonts: jpeg format skips font wait
    try:
        # fold first (safer - smaller)
        await page.screenshot(path=str(fold_png), full_page=False, timeout=15000, animations="disabled")
    except Exception as e:
        status = f"{status};fold_err:{type(e).__name__}"
    try:
        await page.screenshot(path=str(full_png), full_page=True, timeout=25000, animations="disabled")
    except Exception as e:
        status = f"{status};full_err:{type(e).__name__}"
    final_url = page.url
    title = await page.title() if not page.is_closed() else ""
    await ctx.close()
    print(f"  {slug}/{label}: {status} | final={final_url} | title={title[:60]}")
    return status


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        sem = asyncio.Semaphore(3)

        async def bounded(t):
            async with sem:
                return await capture(browser, *t)

        results = await asyncio.gather(*[bounded(t) for t in TARGETS])
        await browser.close()
    ok = sum(1 for r in results if r == "ok")
    print(f"\nRetry done. {ok}/{len(results)} OK.")


if __name__ == "__main__":
    asyncio.run(main())
