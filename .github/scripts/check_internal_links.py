#!/usr/bin/env python3
"""Internal link check for the static site.

Fails (exit 1) on:   broken internal links, #fragments that don't exist on
                     the target page.
Warns (annotation) on: HTML pages with no incoming link from another page,
                     pages linked from only one other page, pages missing
                     from sitemap.xml, and English pages whose links point to
                     a Serbian page that has an English equivalent.

Run locally:  python3 .github/scripts/check_internal_links.py
"""
import os
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = "https://apartmani-igalo.com/"
SKIP_DIRS = {".git", ".github", "seo-reports", "node_modules"}
SKIP_SCHEMES = ("tel:", "mailto:", "sms:", "viber:", "javascript:", "data:")

# English page -> Serbian page it must not link to (use the English twin instead).
EN_PAGES = {
    "vesti/beaches-herceg-novi.html", "vesti/restaurants-herceg-novi.html",
    "vesti/10-reasons-why-to-travel-to-herceg-novi-montenegro.html",
    "rent-a-bike-herceg-novi-igalo.html", "mimosa-festival-herceg-novi.html",
    "monthly-rental-igalo.html",
}
SR_WITH_EN_TWIN = {
    "index.html": "/en/", "about.html": "/en/about.html",
    "blatna-plaza.html": "/en/blatna-plaza.html", "cesta-pitanja.html": "/en/faq.html",
}
LANG_SWITCH = re.compile(r"Srpski|Srpska|\(SR\)")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.ids, self._a = [], set(), None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "href" in a:
            self._a = [a["href"], "", self.getpos()[0], a.get("lang")]

    def handle_data(self, data):
        if self._a is not None:
            self._a[1] += data

    def handle_endtag(self, tag):
        if tag == "a" and self._a is not None:
            self.links.append(self._a)
            self._a = None


def url_of(rel):
    return BASE + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)


def main():
    pages = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT).replace(os.sep, "/")
                p = Page()
                with open(os.path.join(dirpath, fn), encoding="utf-8") as fh:
                    p.feed(fh.read())
                pages[rel] = p

    errors, warnings = [], []
    incoming = defaultdict(set)
    for src, p in sorted(pages.items()):
        for href, text, line, lang in p.links:
            if href.startswith(SKIP_SCHEMES) or href.startswith("#"):
                continue
            u = urlparse(urljoin(url_of(src), href))
            if u.netloc not in ("apartmani-igalo.com", "www.apartmani-igalo.com"):
                continue
            path = unquote(u.path).lstrip("/")
            if path == "" or path.endswith("/"):
                path += "index.html"
            if path not in pages:
                if not os.path.exists(os.path.join(ROOT, path)):
                    errors.append((src, line, f"broken link {href}"))
                continue
            if u.fragment and u.fragment not in pages[path].ids:
                errors.append((src, line, f"missing #{u.fragment} on {path}"))
            if path != src:
                incoming[path].add(src)
            if (src in EN_PAGES or src.startswith("en/")) and path in SR_WITH_EN_TWIN \
                    and not LANG_SWITCH.search(text) and lang != "sr":
                warnings.append((src, line, f"English page links Serbian {path}; use {SR_WITH_EN_TWIN[path]}"))

    sitemap = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    for rel in sorted(pages):
        if rel == "404.html":
            continue
        n = len(incoming[rel])
        if n == 0:
            warnings.append((rel, 1, "orphan: no other page links here"))
        elif n == 1:
            warnings.append((rel, 1, f"weak: only linked from {next(iter(incoming[rel]))}"))
        if url_of(rel) not in sitemap:
            warnings.append((rel, 1, "not in sitemap.xml"))

    gh = os.environ.get("GITHUB_ACTIONS") == "true"
    for kind, items in (("error", errors), ("warning", warnings)):
        for f, line, msg in items:
            print(f"::{kind} file={f},line={line}::{msg}" if gh else f"{kind.upper()}: {f}:{line} {msg}")
    links = sum(len(p.links) for p in pages.values())
    print(f"{len(pages)} pages, {links} links, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
