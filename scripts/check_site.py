"""Check the static site's structure, local resources and fragment links."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import struct
import sys


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_BASE = "https://noob-debug-cyber.github.io/milhon-site/"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.links = []
        self.errors = []
        self.main_count = 0
        self.h1_count = 0
        self.lang = None
        self.has_title = False
        self.has_viewport = False
        self.has_icon = False
        self.has_description = False
        self.canonicals = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        element_id = attrs.get("id")
        if element_id:
            if element_id in self.ids:
                self.errors.append(f"duplicate id: {element_id}")
            self.ids.add(element_id)
        if tag == "html":
            self.lang = attrs.get("lang")
        elif tag == "main":
            self.main_count += 1
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "title":
            self.has_title = True
        elif tag == "meta" and attrs.get("name") == "viewport":
            self.has_viewport = True
        elif tag == "meta" and attrs.get("name") == "description":
            self.has_description = bool(attrs.get("content", "").strip())
        elif tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonicals.append(attrs.get("href"))
        elif tag == "link" and "icon" in attrs.get("rel", "").split():
            self.has_icon = True
        elif tag == "img" and "alt" not in attrs:
            self.errors.append("image without alt attribute")
        for attribute in ("href", "src"):
            if attribute in attrs:
                self.links.append(attrs[attribute])


def check():
    pages = {}
    errors = []
    for path in sorted(ROOT.glob("*.html")):
        page = Page(path)
        page.feed(path.read_text(encoding="utf-8"))
        page.close()
        pages[path] = page
        requirements = {
            "missing document language": bool(page.lang),
            "expected one main landmark": page.main_count == 1,
            "expected one h1": page.h1_count == 1,
            "missing page title": page.has_title,
            "missing viewport": page.has_viewport,
            "missing favicon": page.has_icon,
            "missing page description": page.has_description,
            "canonical URL does not match the public page": page.canonicals
            == [PUBLIC_BASE + ("" if path.name == "index.html" else path.name)],
        }
        errors.extend(f"{path.name}: {message}" for message in page.errors)
        errors.extend(f"{path.name}: {message}" for message, ok in requirements.items() if not ok)

    if not pages:
        errors.append("no HTML pages found")
    resources = set()
    for path, page in pages.items():
        for value in page.links:
            url = urlsplit(value)
            if url.scheme or url.netloc:
                continue
            if url.path.startswith("/"):
                errors.append(f"{path.name}: root-relative URL incompatible with a repository site: {value}")
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(ROOT):
                errors.append(f"{path.name}: local resource escapes the site: {value}")
            elif not target.is_file():
                errors.append(f"{path.name}: missing local resource: {value}")
            else:
                resources.add(target)
                if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                    errors.append(f"{path.name}: missing anchor: {value}")

    for path in sorted(resources):
        if path.suffix.lower() == ".png":
            content = path.read_bytes()
            if content[:8] != b"\x89PNG\r\n\x1a\n" or content[12:16] != b"IHDR" or len(content) < 33:
                errors.append(f"{path.relative_to(ROOT)}: invalid PNG header")
            else:
                width, height = struct.unpack(">II", content[16:24])
                if not width or not height:
                    errors.append(f"{path.relative_to(ROOT)}: empty PNG dimensions")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Static checks passed: {len(pages)} pages, {len(resources)} local resources, no broken local links or anchors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())
