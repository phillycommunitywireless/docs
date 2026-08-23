"""Hide pages that have no content yet from the navigation.

A stub page is one whose body is nothing but its heading. Those pages still
build and still exist at their URL, but they are dropped from the nav so
readers do not click into a blank page. As soon as someone writes a line of
content, the page reappears in the nav with no config change.

Set `hide_empty_pages: false` in `extra` to turn this off and see every stub.
"""

import logging
import re

log = logging.getLogger("mkdocs.hooks.hide_empty_pages")

FRONTMATTER = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
HEADING = re.compile(r"^\s{0,3}#{1,6}\s.*$", re.MULTILINE)


def _is_empty(page):
    path = page.file.abs_src_path
    if not path:
        return False
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return False
    text = FRONTMATTER.sub("", text)
    text = HEADING.sub("", text)
    return not text.strip()


def _prune(items, hidden):
    kept = []
    for item in items:
        if item.is_section:
            item.children = _prune(item.children, hidden)
            if item.children:
                kept.append(item)
            continue
        if item.is_page and _is_empty(item):
            hidden.append(item.file.src_uri)
            continue
        kept.append(item)
    return kept


def _flatten(items, out):
    for item in items:
        if item.is_section:
            _flatten(item.children, out)
        elif item.is_page:
            out.append(item)
    return out


def on_nav(nav, config, files):
    if config.get("extra", {}).get("hide_empty_pages") is False:
        return nav

    hidden = []
    nav.items = _prune(nav.items, hidden)
    if not hidden:
        return nav

    nav.pages = _flatten(nav.items, [])
    for i, page in enumerate(nav.pages):
        page.previous_page = nav.pages[i - 1] if i > 0 else None
        page.next_page = nav.pages[i + 1] if i + 1 < len(nav.pages) else None

    log.info(
        "hide_empty_pages: %d page(s) hidden from the nav: %s",
        len(hidden),
        ", ".join(sorted(hidden)),
    )
    return nav
