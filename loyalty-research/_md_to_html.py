#!/usr/bin/env python3
"""Render the final report markdown to HTML with tables, headings, lists preserved for Google Docs import."""
import sys
from pathlib import Path

# prefer user-installed markdown
import site, os
site.addsitedir(os.path.expanduser("~/Library/Python/3.14/lib/python/site-packages"))

import markdown  # type: ignore

SRC = Path("/Users/mgregor/Claude-Work/CoS/projects/groupon-ecosystem/loyalty-research/loyalty-mechanics-final.md")
DST = Path("/Users/mgregor/Claude-Work/CoS/projects/groupon-ecosystem/loyalty-research/loyalty-mechanics-final.html")

md_text = SRC.read_text()

html_body = markdown.markdown(
    md_text,
    extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    output_format="html5",
)

# Google Docs imports HTML reasonably well with basic styling inlined for tables.
doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Loyalty Mechanics Reverse Engineering for Groupon</title>
<style>
body {{ font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.45; color: #111; max-width: 900px; margin: 2em auto; padding: 0 1em; }}
h1 {{ font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 4px; margin-top: 2em; }}
h2 {{ font-size: 16pt; margin-top: 1.6em; color: #333; }}
h3 {{ font-size: 13pt; margin-top: 1.3em; color: #444; }}
h4 {{ font-size: 11pt; margin-top: 1.1em; color: #555; }}
p, li {{ font-size: 11pt; }}
table {{ border-collapse: collapse; margin: 1em 0; font-size: 10pt; }}
th, td {{ border: 1px solid #bbb; padding: 6px 9px; text-align: left; vertical-align: top; }}
th {{ background: #f2f2f2; font-weight: 700; }}
code {{ font-family: Consolas, Menlo, monospace; background: #f6f6f6; padding: 1px 4px; border-radius: 3px; font-size: 10pt; }}
pre {{ background: #f6f6f6; padding: 10px; border-radius: 4px; overflow-x: auto; }}
blockquote {{ border-left: 3px solid #888; padding-left: 12px; color: #444; margin: 1em 0; }}
strong {{ color: #000; }}
hr {{ border: 0; border-top: 1px solid #ccc; margin: 2em 0; }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

DST.write_text(doc)
print(f"Wrote {len(doc):,} chars to {DST}")
