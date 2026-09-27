"""Check that every local link and image in the built site points at a real file.

`mkdocs build --strict` checks Markdown links, but not paths written in raw
HTML (e.g. `<img src="../../assets/...">` in the equipment grids). Those
paths are relative to the page's URL, and Spanish pages are served one
folder deeper (/es/...), so a path copied from an English page breaks. This
catches that.

Usage: check_built_links.py [SITE_DIR]   (default: site)
Exits 1 if anything doesn't resolve.
"""

import posixpath
import re
import sys
from pathlib import Path

LINK = re.compile(r'(?:src|href)="([^"#?]+)')
EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.IGNORECASE)


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
    broken = []
    for page in sorted(site.rglob("*.html")):
        url = "/" + page.relative_to(site).as_posix()
        folder = posixpath.dirname(url) + "/"
        for link in LINK.findall(page.read_text(encoding="utf-8", errors="ignore")):
            if EXTERNAL.match(link):
                continue
            target = posixpath.normpath(posixpath.join(folder, link))
            path = site / target.lstrip("/")
            if not (path.is_file() or (path / "index.html").is_file()):
                broken.append((url, link))

    for url, link in broken:
        print(f"{url}: {link} does not exist in the built site")
    if broken:
        print(f"\n{len(broken)} broken local link(s). Paths in raw HTML are relative to "
              "the page's URL; pages under docs/es/ need one more '../' than English ones.")
        sys.exit(1)
    print("All local links and images resolve.")


if __name__ == "__main__":
    main()
