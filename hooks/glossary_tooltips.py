"""Hover definitions for the acronyms used across the docs.

The definitions live in `includes/abbreviations.md` so they can be edited
without touching Python. Every page gets them appended, and the `abbr`
extension turns each occurrence of a term into a tooltip.

Marking up *every* occurrence underlines a common acronym dozens of times on
a long page, so `on_post_page` unwraps all but the first of each term.
"""

import re
from pathlib import Path

ABBREVIATIONS = Path(__file__).parent.parent / "includes" / "abbreviations.md"

ABBR = re.compile(r'<abbr title="(?P<title>[^"]*)">(?P<term>[^<]*)</abbr>')


def on_page_markdown(markdown, page, config, files):
    return markdown + "\n\n" + ABBREVIATIONS.read_text()


def on_post_page(output, page, config):
    seen = set()

    def replace(match):
        title = match.group("title")
        if title in seen:
            return match.group("term")
        seen.add(title)
        return match.group(0)

    return ABBR.sub(replace, output)
