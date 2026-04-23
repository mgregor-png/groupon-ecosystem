#!/usr/bin/env python3
"""Concatenate all loyalty-research markdown deliverables into one doc and render HTML for Google Docs upload."""
import os
import site
from pathlib import Path

site.addsitedir(os.path.expanduser("~/Library/Python/3.14/lib/python/site-packages"))

import markdown  # type: ignore

ROOT = Path("/Users/mgregor/Claude-Work/CoS/projects/groupon-ecosystem/loyalty-research")
OUT_MD = ROOT / "_consolidated-preview.md"
OUT_HTML = ROOT / "_consolidated-preview.html"

# Section ordering: most important first, deepest artefacts last
SECTIONS = [
    ("# Loyalty Research - Consolidated Preview (2026-04-22)",
     "*Generated 2026-04-22 for review. Combines final report + iteration outputs from Apr 21-22. "
     "Screenshots referenced below live in `competitor-mapping/` (upload folder separately to G Drive).*"),

    ("## Part 1 - Final merged report", "loyalty-mechanics-final.md"),
    ("## Part 2 - Retention uplift sizing model (shell)", "retention-uplift-model.md"),
    ("## Part 3 - Fact-check v1 (load-bearing numbers vs primary sources)", "fact-check-v1.md"),
    ("## Part 4 - Competitor visual mapping - pattern analysis", "competitor-mapping/pattern-analysis.md"),
    ("## Part 5 - Competitor visual mapping - inventory", "competitor-mapping/README.md"),
    ("## Part 6 - Competitor visual mapping - gaps", "competitor-mapping/gaps.md"),
    ("## Part 7 - Signup-flow pre-auth captures", None),  # multi-file
    ("## Part 8 - Slickdeals partnership workstream", "partnership-feasibility-slickdeals.md"),
    ("## Part 9 - Data gaps (internal + external asks)", "data-gaps.md"),
    ("## Part 10 - PostHog quick survey draft", "posthog-survey-draft.md"),
    ("## Part 11 - Daniel Rakuten ask draft", "daniel-rakuten-ask.md"),
    ("## Part 12 - AI funnel transparency appendix", "ai-funnel-appendix.md"),
    ("## Part 13 - Mechanic cards (full detail)", None),  # multi-file
]

MECHANIC_CARDS = [
    "mechanic-cards/01-quarterly-payout-ritual.md",
    "mechanic-cards/02-soft-currency-1-to-1.md",
    "mechanic-cards/03-weekly-anchor-day.md",
    "mechanic-cards/04-safari-extension-bundling.md",
    "mechanic-cards/05-trust-floor.md",
    "mechanic-cards/06-trust-and-transparency.md",
]

SIGNUP_FLOW_FILES = [
    "signup-flow/rakuten-preauth.md",
    "signup-flow/capital-one-shopping-preauth.md",
    "signup-flow/honey-preauth.md",
]


def read_md(rel):
    p = ROOT / rel
    if not p.exists():
        return f"\n\n*[File not found: {rel}]*\n\n"
    return p.read_text()


def demote_headers(text, levels=2):
    """Shift headers down N levels so nested docs stay under parent section headers."""
    out_lines = []
    for line in text.split("\n"):
        if line.startswith("#"):
            # count leading hashes
            i = 0
            while i < len(line) and line[i] == "#":
                i += 1
            if i <= 6 - levels:
                line = "#" * levels + line
        out_lines.append(line)
    return "\n".join(out_lines)


def main():
    parts = []
    # Title
    title_header, title_body = SECTIONS[0]
    parts.append(title_header)
    parts.append(title_body)
    parts.append("\n---\n")

    # Table of contents
    toc = ["## Table of contents\n"]
    for header, _ in SECTIONS[1:]:
        toc.append(f"- {header.replace('## ', '')}")
    parts.append("\n".join(toc))
    parts.append("\n---\n")

    # Each section
    for header, src in SECTIONS[1:]:
        parts.append(header)
        parts.append("")
        if src is None:
            # multi-file sections
            if "Signup-flow" in header:
                for f in SIGNUP_FLOW_FILES:
                    parts.append(f"### {Path(f).stem}")
                    parts.append("")
                    parts.append(demote_headers(read_md(f), levels=3))
                    parts.append("\n---\n")
            elif "Mechanic cards" in header:
                for f in MECHANIC_CARDS:
                    parts.append(f"### {Path(f).stem}")
                    parts.append("")
                    parts.append(demote_headers(read_md(f), levels=3))
                    parts.append("\n---\n")
        else:
            # demote by 1 so inner h1 becomes h2 under the Part heading
            parts.append(demote_headers(read_md(src), levels=1))
            parts.append("\n---\n")

    md_text = "\n".join(parts)
    OUT_MD.write_text(md_text)
    print(f"Wrote {len(md_text):,} chars to {OUT_MD}")

    # Convert to HTML
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc"],
        output_format="html5",
    )
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Loyalty Research - Consolidated Preview (2026-04-22)</title>
<style>
body {{ font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.45; color: #111; max-width: 900px; margin: 2em auto; padding: 0 1em; }}
h1 {{ font-size: 22pt; border-bottom: 3px solid #333; padding-bottom: 6px; margin-top: 1em; color: #111; }}
h2 {{ font-size: 17pt; margin-top: 2em; color: #222; border-bottom: 1px solid #ccc; padding-bottom: 3px; }}
h3 {{ font-size: 14pt; margin-top: 1.5em; color: #333; }}
h4 {{ font-size: 12pt; margin-top: 1.2em; color: #444; }}
h5 {{ font-size: 11pt; color: #555; }}
p, li {{ font-size: 11pt; }}
table {{ border-collapse: collapse; margin: 1em 0; font-size: 10pt; width: 100%; }}
th, td {{ border: 1px solid #bbb; padding: 6px 9px; text-align: left; vertical-align: top; }}
th {{ background: #f2f2f2; font-weight: 700; }}
code {{ font-family: Consolas, Menlo, monospace; background: #f6f6f6; padding: 1px 4px; border-radius: 3px; font-size: 10pt; }}
pre {{ background: #f6f6f6; padding: 10px; border-radius: 4px; overflow-x: auto; font-size: 10pt; }}
blockquote {{ border-left: 3px solid #888; padding-left: 12px; color: #444; margin: 1em 0; }}
strong {{ color: #000; }}
hr {{ border: 0; border-top: 1px solid #ccc; margin: 2em 0; }}
ul, ol {{ margin-left: 1.5em; }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""
    OUT_HTML.write_text(doc)
    print(f"Wrote {len(doc):,} chars to {OUT_HTML}")


if __name__ == "__main__":
    main()
