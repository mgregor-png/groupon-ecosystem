#!/usr/bin/env python3
"""Extract a Google Docs API JSON dump into readable markdown."""
import json
import sys
from pathlib import Path

src = Path("/Users/mgregor/Claude-Work/CoS/projects/groupon-ecosystem/loyalty-research/raw/rebecca-draft-raw.json")
dst = Path("/Users/mgregor/Claude-Work/CoS/projects/groupon-ecosystem/loyalty-research/raw/rebecca-draft.md")

raw = src.read_text()
start = raw.find("{")
doc = json.loads(raw[start:])
title = doc.get("title", "Untitled")

HEADING_PREFIX = {
    "TITLE": "# ",
    "SUBTITLE": "## ",
    "HEADING_1": "# ",
    "HEADING_2": "## ",
    "HEADING_3": "### ",
    "HEADING_4": "#### ",
    "HEADING_5": "##### ",
    "HEADING_6": "###### ",
    "NORMAL_TEXT": "",
}


def text_run_to_md(elem):
    tr = elem.get("textRun")
    if not tr:
        # inlineObjectElement, pageBreak, etc.
        if "inlineObjectElement" in elem:
            return "[inline-object]"
        if "horizontalRule" in elem:
            return "\n---\n"
        return ""
    content = tr.get("content", "")
    style = tr.get("textStyle", {}) or {}
    link = style.get("link", {}).get("url") if style.get("link") else None
    bold = style.get("bold")
    italic = style.get("italic")
    # Preserve line breaks within a run as real newlines; Docs sometimes uses \v for line break.
    content = content.replace("\v", "  \n")
    if link:
        text = content.rstrip("\n")
        trailing = content[len(text):]
        return f"[{text}]({link}){trailing}"
    if bold and content.strip():
        text = content.rstrip("\n")
        trailing = content[len(text):]
        return f"**{text}**{trailing}"
    if italic and content.strip():
        text = content.rstrip("\n")
        trailing = content[len(text):]
        return f"*{text}*{trailing}"
    return content


def paragraph_to_md(para):
    style = (para.get("paragraphStyle") or {}).get("namedStyleType", "NORMAL_TEXT")
    prefix = HEADING_PREFIX.get(style, "")
    bullet = para.get("bullet")
    # indentation for nested bullets
    nesting = 0
    if bullet:
        nesting = bullet.get("nestingLevel", 0) or 0
    inline = "".join(text_run_to_md(e) for e in para.get("elements", []))
    inline = inline.rstrip("\n")
    if not inline.strip() and not bullet:
        return ""
    if bullet:
        indent = "  " * nesting
        return f"{indent}- {inline}"
    return f"{prefix}{inline}"


def table_to_md(table):
    rows = []
    for row in table.get("tableRows", []):
        cells = []
        for cell in row.get("tableCells", []):
            cell_text = []
            for se in cell.get("content", []):
                if "paragraph" in se:
                    t = paragraph_to_md(se["paragraph"])
                    if t:
                        cell_text.append(t.lstrip("# ").strip())
            cells.append(" ".join(cell_text).replace("|", "\\|") or " ")
        rows.append("| " + " | ".join(cells) + " |")
    if not rows:
        return ""
    # Insert header separator after first row
    header = rows[0]
    col_count = header.count("|") - 1
    sep = "|" + "|".join([" --- "] * col_count) + "|"
    return "\n".join([rows[0], sep] + rows[1:])


out = [f"# {title}", "", "*Source: Rebecca's Google Doc, fetched via gws on 2026-04-21*", ""]

for se in doc.get("body", {}).get("content", []):
    if "paragraph" in se:
        md = paragraph_to_md(se["paragraph"])
        if md:
            out.append(md)
        else:
            out.append("")
    elif "table" in se:
        out.append("")
        out.append(table_to_md(se["table"]))
        out.append("")
    elif "sectionBreak" in se:
        out.append("")
    elif "tableOfContents" in se:
        out.append("<!-- table of contents -->")

md_text = "\n".join(out)
# Collapse >2 blank lines
import re
md_text = re.sub(r"\n{3,}", "\n\n", md_text)
dst.write_text(md_text)
print(f"Wrote {len(md_text)} chars to {dst}")
print(f"Title: {title}")
print(f"First 40 lines:")
for line in md_text.split("\n")[:40]:
    print(f"  {line}")
