"""Hover definitions for the acronyms used across the docs.

The definitions live in `includes/abbreviations.md` so they can be edited
without touching Python. Every page gets them appended, and the `abbr`
extension turns each occurrence of a term into a tooltip. Pages in another
language's folder (e.g. `es/`) use `includes/abbreviations.<lang>.md` when it
exists, so Spanish pages get Spanish definitions.

Marking up *every* occurrence underlines a common acronym dozens of times on
a long page, so `on_post_page` unwraps all but the first of each term.
"""

import re
from pathlib import Path

INCLUDES = Path(__file__).parent.parent / "includes"
ABBREVIATIONS = INCLUDES / "abbreviations.md"

ABBR = re.compile(r'<abbr title="(?P<title>[^"]*)">(?P<term>[^<]*)</abbr>')


def on_page_markdown(markdown, page, config, files):
    lang = page.file.src_uri.split("/", 1)[0]
    translated = INCLUDES / f"abbreviations.{lang}.md"
    source = translated if translated.exists() else ABBREVIATIONS
    return markdown + "\n\n" + source.read_text()


def on_post_page(output, page, config):
    seen = set()

    def replace(match):
        title = match.group("title")
        if title in seen:
            return match.group("term")
        seen.add(title)
        return match.group(0)

    return ABBR.sub(replace, output)
