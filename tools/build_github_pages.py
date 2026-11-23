#!/usr/bin/env python3
"""Build the bilingual Showcase for a GitHub Pages project path."""

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
from tempfile import TemporaryDirectory
from urllib.parse import unquote, urljoin, urlsplit

from showcase_workflow import ROOT, config, now, prepare, write


ROOT_LINK = re.compile(r'(\s(?:href|src)=["\'])/(?!/)')


class PageLinks(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.line_offsets = [0] + [match.end() for match in re.finditer('\n', html)]
        self.tags = []
        self.links = []
        self.ids = set()
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        line, column = self.getpos()
        offset = self.line_offsets[line - 1] + column
        self.tags.append((offset, self.get_starttag_text()))
        for name, value in attrs:
            if name in ('href', 'src') and value:
                self.links.append(value)
            elif name == 'id':
                self.ids.add(value)


def mount_html(html, base_path):
    parts = []
    cursor = 0
    for offset, tag in PageLinks(html).tags:
        replacement = ROOT_LINK.sub(lambda match: f'{match[1]}{base_path}/', tag)
        if replacement != tag:
            parts.extend((html[cursor:offset], replacement))
            cursor = offset + len(tag)
    return ''.join(parts) + html[cursor:]


def mount_reader_script(script_path, base_path):
    script = script_path.read_text(encoding='utf-8')
    replacements = {
        "fetch('/search.json')": f"fetch('{base_path}/search.json')",
        "location.pathname==='/' || location.pathname==='/index.html'":
            f"location.pathname==='{base_path}/' || location.pathname==='{base_path}/index.html'",
        "location.replace(legacy[key])": f"location.replace('{base_path}'+legacy[key])",
    }
    for original, replacement in replacements.items():
        if script.count(original) != 1:
            raise ValueError(f'Update GitHub Pages URL mounting for reader script: {original}')
        script = script.replace(original, replacement)
    script_path.write_text(script, encoding='utf-8')


def mount_site(dist, base_path):
    for page in dist.rglob('*.html'):
        html = page.read_text(encoding='utf-8')
        page.write_text(mount_html(html, base_path), encoding='utf-8')
    search_path = dist / 'search.json'
    search = json.loads(search_path.read_text(encoding='utf-8'))
    manifest_path = dist / 'book-manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    for row in search + manifest['chapters'] + manifest['english_chapters']:
        row['url'] = base_path + row['url']
    search_path.write_text(json.dumps(search, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    mount_reader_script(dist / 'assets/site.js', base_path)
    return search, manifest


def verify_mounted_site(dist, base_path, search, manifest):
    pages = {}
    for path in dist.rglob('*.html'):
        route = '/' + path.relative_to(dist).as_posix()
        pages[route] = PageLinks(path.read_text(encoding='utf-8'))

    def check_link(href, origin):
        url = urlsplit(urljoin(base_path + origin, href))
        if url.scheme or url.netloc:
            return
        path = unquote(url.path)
        if not path.startswith(base_path + '/'):
            raise ValueError(f'Link escapes GitHub Pages project path: {origin} -> {href}')
        route = path.removeprefix(base_path)
        if route == '/':
            route = '/index.html'
        if not (dist / route.lstrip('/')).is_file():
            raise ValueError(f'Missing GitHub Pages target: {origin} -> {href}')
        if url.fragment and (route not in pages or unquote(url.fragment) not in pages[route].ids):
            raise ValueError(f'Missing GitHub Pages anchor: {origin} -> {href}')

    for route, page in pages.items():
        for href in page.links:
            check_link(href, route)
    for row in search + manifest['chapters'] + manifest['english_chapters']:
        check_link(row['url'], '/index.html')
    print(f'Verified mounted page, asset, and search links across {len(pages)} HTML pages')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-path', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    base_path = args.base_path.rstrip('/')
    if base_path and not re.fullmatch(r'(?:/[\w.-]+)+', base_path):
        parser.error('--base-path must be an absolute URL path')
    if args.output.exists() and (not args.output.is_dir() or any(args.output.iterdir())):
        parser.error('--output must be a new or empty directory')

    with TemporaryDirectory(prefix='beyond-code-pages-') as scratch:
        checkout = Path(scratch)
        write(checkout / '.openai/hosting.json', {
            'project_id': config(ROOT)['project_id'],
            'static': {'directory': 'dist'},
        })
        prepare(ROOT, checkout, now()[:10])
        dist = checkout / 'dist'
        search, manifest = mount_site(dist, base_path)
        verify_mounted_site(dist, base_path, search, manifest)
        shutil.copytree(dist, args.output, dirs_exist_ok=True)


if __name__ == '__main__':
    main()
