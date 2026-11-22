#!/usr/bin/env python3
"""Verify every chapter, figure, internal link, search target and source text."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
import hashlib
import importlib.util
import json
import re
import argparse
from markdown_it import MarkdownIt

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'dist'


class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=[];self.links=[];self.images=[];self.h1=0;self.figures=[];self.body=[];self.in_article=False;self.body_depth=0
        self.codes=[];self.in_pre=False;self.code_parts=None;self.tables=[];self.row=None;self.cell=None;self.figure_dimensions=[]
        self.pagination={}
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if tag=='a' and a.get('rel') in ('prev','next'):self.pagination[a['rel']]=a.get('href')
        if tag in ('img','script') and 'src' in a:self.images.append(a['src'])
        if tag=='link' and 'href' in a:self.images.append(a['href'])
        if tag=='h1':self.h1+=1
        if tag=='pre':self.in_pre=True
        if tag=='code' and self.in_pre:self.code_parts=[]
        if tag=='table':self.tables.append([])
        if tag=='tr':self.row=[]
        if tag in ('td','th'):self.cell=[]
        if tag=='img' and a.get('src','').startswith('/figures/'):
            self.figure_dimensions.append((a.get('width'),a.get('height')))
        if 'data-figure' in a:self.figures.append(a['data-figure'])
        if tag=='article' and a.get('id')=='chapter-body':self.in_article=True;return
        if self.in_article:self.body.append(self.get_starttag_text())
    def handle_endtag(self,tag):
        if tag=='code' and self.code_parts is not None:self.codes.append(''.join(self.code_parts));self.code_parts=None
        if tag=='pre':self.in_pre=False
        if tag in ('td','th') and self.cell is not None:self.row.append(''.join(self.cell));self.cell=None
        if tag=='tr' and self.row is not None:self.tables[-1].append(self.row);self.row=None
        if tag=='article':self.in_article=False
        elif self.in_article:self.body.append(f'</{tag}>')
    def handle_data(self,data):
        if self.code_parts is not None:self.code_parts.append(data)
        if self.cell is not None:self.cell.append(data)
        if self.in_article:
            from html import escape
            self.body.append(escape(data))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--book-root',type=Path);args=parser.parse_args()
    spec=importlib.util.spec_from_file_location('reader_build',ROOT/'reader/build_site.py');build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)
    book=json.loads((ROOT/'content/book.json').read_text());manifest=json.loads((OUT/'book-manifest.json').read_text());search=json.loads((OUT/'search.json').read_text())
    errors=[];pages={};link_count=0
    for path in OUT.rglob('*.html'):
        s=path.read_text();p=Page();p.feed(s);pages['/'+str(path.relative_to(OUT))]=p
        duplicates=[key for key,count in Counter(p.ids).items() if count>1]
        if duplicates:errors.append(f'Duplicate IDs {path.name}: {duplicates[:5]}')
        if p.h1!=1:errors.append(f'Expected one H1: {path.name}')
    def resolve(href,current):
        u=urlsplit(href)
        if u.scheme or u.netloc:return
        route=unquote(u.path) or current
        if route=='/':route='/index.html'
        target=OUT/route.lstrip('/')
        if not target.is_file():errors.append(f'Missing file: {current} -> {href}');return
        if u.fragment and (route not in pages or unquote(u.fragment) not in pages[route].ids):errors.append(f'Missing anchor: {current} -> {href}')
    for route,p in pages.items():
        for href in p.links+p.images:resolve(href,route);link_count+=1
    assert len(pages)==25
    assert [x['number'] for x in manifest['chapters']]==list(range(1,24))
    for c in manifest['chapters']:
        p=pages[c['url']]
        if p.figures!=c['figures']:errors.append(f'Chapter figure mismatch: {c["number"]}')
        if build.digest(build.plain(''.join(p.body)))!=c['rendered_text_sha256']:errors.append(f'Final HTML text mismatch: {c["number"]}')
        source=(ROOT/'content/chapters'/f'{c["number"]:02}.md').read_text()
        if build.digest(source)!=c['reader_sha256']:errors.append(f'Reader source mismatch: {c["number"]}')
        reference=MarkdownIt('commonmark',{'html':False}).enable('table')
        fence=reference.renderer.rules['fence']
        reference.renderer.rules['fence']=lambda ts,i,opts,env:'' if ts[i].info.strip()=='mermaid' else fence(ts,i,opts,env)
        expected=Page();expected.feed(reference.render(source))
        if p.codes!=expected.codes:errors.append(f'Exact code block mismatch: {c["number"]}')
        if p.tables!=expected.tables:errors.append(f'Table rows or cells mismatch: {c["number"]}')
        if any(not w or not h for w,h in p.figure_dimensions):errors.append(f'Missing reserved figure size: {c["number"]}')
        if p.pagination.get('prev')!=(f'/chapters/{c["number"]-1:02}.html' if c['number']>1 else None):errors.append(f'Previous chapter incorrect: {c["number"]}')
        if p.pagination.get('next')!=(f'/chapters/{c["number"]+1:02}.html' if c['number']<23 else None):errors.append(f'Next chapter incorrect: {c["number"]}')
    if args.book_root:
        sync=json.loads((ROOT/'sync-report.json').read_text())
        for source in sync['source_files']:
            if hashlib.sha256((args.book_root/source['file']).read_bytes()).hexdigest()!=source['sha256']:errors.append(f'Outdated source snapshot: {source["file"]}')
    for row in search:resolve(row['url'],'/index.html')
    assert len({r['url'] for r in search})==len(search)
    assert {r['chapter'] for r in search}==set(range(1,24))
    for term,n in [('Checkpoint',7),('external-effect-unknown',8),('effect_unknown',14),('旧CardFace',23),('净增量',23)]:
        if not any(term in row['text'] and row['chapter']==n for row in search):errors.append(f'Search term missing: {term}')
    for f in book['figures']:
        for ext in ['svg','png']:
            actual=hashlib.sha256((OUT/'figures'/f'{f["id"]}.{ext}').read_bytes()).hexdigest()
            if actual!=f[f'{ext}_sha256']:errors.append(f'Figure hash mismatch: {f["id"]}')
    for path in OUT.rglob('*'):
        if path.suffix not in ['.html','.json']:continue
        if re.search(r'/Users/|file://|\.\./(?:Evidence|RevisedResult|OringinalDocs)/|CLM-|ER-2026|RR-0',path.read_text()):errors.append(f'Editorial path or ID in public output: {path.name}')
    report={'pages':len(pages),'chapters':23,'figures':14,'static_exports':28,'code_blocks_checked':sum(len(p.codes) for p in pages.values()),'tables_checked':sum(len(p.tables) for p in pages.values()),'links_and_assets_checked':link_count,'search_targets':len(search),'numbered_sections':sum(len(c['numbered_sections']) for c in manifest['chapters']),'all_chapter_texts_match':not any('text mismatch' in e for e in errors),'errors':errors}
    (ROOT/'verification-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(bool(errors))


if __name__=='__main__':main()
