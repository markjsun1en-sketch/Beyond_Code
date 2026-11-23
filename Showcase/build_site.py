#!/usr/bin/env python3
"""Build the complete reader from a synchronized, reader-facing content snapshot."""
from pathlib import Path
from html import escape
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from copy import copy
import hashlib
import json
import re
import shutil
import sys
from datetime import date
import xml.etree.ElementTree as ET
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'dist'
CONTENT = ROOT / 'content'
BOOK = json.loads((CONTENT / 'book.json').read_text())
UPDATED = date.fromisoformat(BOOK['date'])
CHAPTERS = BOOK['chapters']
ENGLISH = {ch['number']: ch for ch in BOOK['english_chapters']}
FIGURES = {f['id']: f for f in BOOK['figures'] + BOOK['english_figures']}
for figure in FIGURES.values():
    viewbox = ET.parse(CONTENT / 'figures' / f'{figure["id"]}.svg').getroot().get('viewBox').split()
    figure['width'], figure['height'] = [round(float(v)) for v in viewbox[2:]]
SEARCH = []
MANIFEST = {'date': BOOK['date'], 'source_fingerprint': BOOK['source_fingerprint'],
            'chapters': [], 'english_chapters': [], 'figures': BOOK['figures'],
            'english_figures': BOOK['english_figures']}
GROUPS = [
    ('问题与基础', 'Foundations', 1, 3),
    ('意图、上下文与事实', 'Intent, Context, and Truth', 4, 6),
    ('执行与验证', 'Execution and Verification', 7, 10),
    ('认知、自治与观察', 'Cognition, Autonomy, and Observation', 11, 14),
    ('记忆、演化与组织', 'Memory, Evolution, and Organization', 15, 17),
    ('责任、安全与运行', 'Accountability, Security, and Operations', 18, 20),
    ('生命周期与实践', 'Lifecycle and Practice', 21, 23),
]


class Plain(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.skip: self.skip += tag not in ('img', 'br', 'hr', 'input', 'meta', 'link'); return
        if 'data-reading-control' in attrs or tag in ('script', 'style'): self.skip = 1; return
        if tag in ('p', 'div', 'li', 'td', 'th', 'tr', 'pre', 'h1', 'h2', 'h3', 'h4', 'blockquote'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if self.skip: self.skip -= 1
        elif tag in ('p', 'li', 'td', 'th', 'tr', 'pre', 'h1', 'h2', 'h3', 'h4'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)


def plain(html):
    p = Plain(); p.feed(html); return re.sub(r'\s+', ' ', ''.join(p.parts)).strip()


def digest(value): return hashlib.sha256(value.encode()).hexdigest()
def chapter_stem(ch):
    suffix = '-en' if ch.get('language') == 'en' else ''
    return f'{ch["number"]:02}{suffix}'


def url(ch): return f'/chapters/{chapter_stem(ch)}.html'
def short(ch): return re.sub(r'^(?:第\d+章|Chapter \d+\.)\s*', '', ch['title'])


def navigation(current, english):
    chapters = ENGLISH.values() if english else CHAPTERS
    parts = []
    for zh, en, start, end in GROUPS:
        title = en if english else zh
        links = ''.join(f'<a href="{url(c)}"{chr(32)+"aria-current=\"page\"" if c["number"] == current else ""}><span class="chapter-number">{c["number"]:02}</span><span>{escape(short(c))}</span></a>' for c in chapters if start <= c['number'] <= end)
        parts.append(f'<section><h2>{title}</h2>{links}</section>')
    return ''.join(parts)


def shell(title, body, current=0, toc='', english=False, gallery=False):
    nav = navigation(current, english)
    language = 'en' if english else 'zh-CN'
    def label(zh, en):
        return en if english else zh
    contents_url = label('/', '/en.html')
    gallery_url = label('/figures.html', '/figures-en.html')
    github_main_url = 'https://github.com/markjsun1en-sketch/Beyond_Code/blob/main'
    readme_file = label('README.md', 'README.en.md')
    if current:
        other_url = url(CHAPTERS[current - 1] if english else ENGLISH[current])
    elif gallery:
        other_url = label('/figures-en.html', '/figures.html')
    else:
        other_url = label('/en.html', '/')
    other_language = label('en', 'zh-CN')
    alternate = f'<link rel="alternate" hreflang="{other_language}" href="{other_url}">'
    switch = f'<a class="language-switch" href="{other_url}" lang="{other_language}" hreflang="{other_language}">{label("English", "中文")}</a>'
    return f'''<!doctype html>
<html lang="{language}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} · Beyond Code</title><meta name="description" content="{label('Beyond Code：AI原生软件工程。23章完整工作稿与14张机制简图，支持全文搜索和章节阅读。', 'Beyond Code: AI-Native Software Engineering. Read and search 23 chapters and 14 diagrams.')}">
{alternate}
<link rel="stylesheet" href="/assets/site.css"><script src="/assets/site.js" defer></script></head>
<body data-chapter="{current}"><a class="skip-link" href="#main">{label('跳到正文', 'Skip to content')}</a>
<header class="topbar"><button class="menu-toggle" type="button" aria-label="{label('打开章节目录', 'Open book contents')}" data-open-nav>{label('目录', 'Contents')}</button>
<a class="brand" href="{contents_url}" aria-label="Beyond Code"><span class="brandmark">B/</span><span>BEYOND CODE<small>AI-NATIVE SOFTWARE ENGINEERING</small></span></a>
<nav class="topnav" aria-label="{label('全站导航', 'Site navigation')}"><a href="{contents_url}">{label('全书目录', 'Contents')}</a><a href="{gallery_url}">{label('机制简图', 'Figures')}</a></nav>
<div class="header-actions"><span class="version">{label('工作稿', 'Working manuscript')} · {UPDATED:%Y.%m.%d}</span>{switch}<button type="button" data-open-search>{label('搜索全书', 'Search')} <kbd>⌘ K</kbd></button><button type="button" data-theme aria-label="{label('切换深色主题', 'Switch to dark theme')}">{label('深色', 'Dark')}</button></div></header>
<aside class="sidebar"><nav aria-label="{label('章节目录', 'Book contents')}">{nav}</nav><div class="sidebar-foot">{label(f'23章正文 · 14张机制简图<br>同步至{UPDATED.year}年{UPDATED.month}月{UPDATED.day}日', f'23 chapters · 14 figures<br>Updated {UPDATED:%Y-%m-%d}')}</div></aside>
<main id="main" class="content" tabindex="-1">{body}<footer>
<nav aria-label="{label('页脚导航', 'Footer navigation')}">
<a href="{contents_url}">Beyond Code</a> · <a href="{github_main_url}/{readme_file}" lang="en" hreflang="{language}">GitHub README</a> · <a href="{github_main_url}/LICENSE" lang="en">MIT License</a>
</nav><span>{label('工作稿持续修订；案例的适用范围以正文为准。', 'Working manuscript. Each case states the scope of its conclusions.')}</span></footer></main>
{f'<aside class="page-toc"><h2>{label("本章目录", "In this chapter")}</h2><nav aria-label="{label("本章小节", "Chapter sections")}">{toc}</nav><a class="back-top" href="#main">{label("回到章首", "Back to top")}</a></aside>' if toc else ''}
<dialog id="nav-dialog"><div class="dialog-top"><strong>{label('章节目录', 'Book contents')}</strong><button type="button" data-close-dialog>{label('关闭', 'Close')}</button></div><nav aria-label="{label('章节目录', 'Book contents')}">{nav}</nav></dialog>
<dialog id="search-dialog"><div class="dialog-top"><label for="book-search">{label('搜索全书', 'Search the book')}</label><button type="button" data-close-dialog>{label('关闭', 'Close')}</button></div>
<form role="search"><input id="book-search" type="search" placeholder="{label('搜索概念、例子或代码，如 Checkpoint、净增量', 'Search concepts, examples, or code')}" autocomplete="off"><button type="button" id="clear-search">{label('清空', 'Clear')}</button></form>
<p id="search-status" role="status" aria-live="polite">{label('搜索中英文正文、表格、代码示例与图注。', 'Search both languages, including tables, code examples, and captions.')}</p><ol id="search-results"></ol></dialog>
<dialog id="figure-dialog" aria-labelledby="figure-dialog-title"><div class="dialog-top"><strong id="figure-dialog-title">{label('机制图', 'Figure')}</strong><button type="button" data-close-dialog>{label('关闭', 'Close')}</button></div><div class="figure-tools"><button type="button" data-zoom-out>{label('缩小', 'Zoom out')}</button><button type="button" data-zoom-in>{label('放大', 'Zoom in')}</button><button type="button" data-zoom-fit>{label('适合宽度', 'Fit width')}</button><button type="button" data-zoom-reset>{label('原尺寸', 'Actual size')}</button></div><p id="figure-status" role="status">{label('可横向、纵向滑动查看', 'Scroll to explore the figure')}</p><div class="figure-viewport" tabindex="0" aria-label="{label('可横向、纵向滚动的机制图', 'Scrollable figure')}"><img alt=""></div></dialog>
</body></html>'''


def render_chapter(ch):
    n = ch['number']; text = (CONTENT / 'chapters' / f'{chapter_stem(ch)}.md').read_text()
    english = ch.get('language') == 'en'
    table_hint = 'Scroll to see more columns.' if english else '表格可左右滑动，查看其余列。'
    table_label = 'Scrollable table' if english else '可横向滚动的数据表'
    code_hint = 'Scroll to see the full example.' if english else '代码可左右滑动，查看完整内容。'
    zoom_label, svg_label, png_label = ('Zoom in', 'Actual-size SVG', 'Download PNG') if english else ('放大查看', '原尺寸 SVG', '下载 PNG')
    md = MarkdownIt('commonmark', {'html': False}).enable('table')
    tokens = md.parse(text); toc = []; found_figures = []; numbered = []; block_count = 0
    current_section = ch['title']; current_figure = None
    default_fence = md.renderer.rules['fence']
    md.renderer.rules['table_open'] = lambda ts, i, opts, env: f'<p class="overflow-hint" data-reading-control>{table_hint}</p><div class="table-scroll" tabindex="0" role="region" aria-label="{table_label}">' + md.renderer.renderToken(ts, i, opts, env)
    md.renderer.rules['table_close'] = lambda ts, i, opts, env: '</table></div>\n'
    def fence(ts, i, opts, env):
        t = ts[i]
        if t.info.strip() == 'mermaid':
            f = FIGURES[t.meta['figure']]
            return f'<figure class="mechanism" id="{t.attrGet("id")}" data-figure="{f["id"]}">{figure_image(f)}<div data-reading-control><a href="/figures/{f["id"]}.svg" data-zoom>{zoom_label}</a><a href="/figures/{f["id"]}.svg" target="_blank" rel="noopener">{svg_label}</a><a href="/figures/{f["id"]}.png" download>{png_label}</a></div></figure>\n'
        code_token = copy(t)
        code_token.attrs = {key: value for key, value in t.attrs.items() if key != 'id'}
        return f'<div id="{t.attrGet("id")}" class="code-block"><p class="overflow-hint" data-reading-control>{code_hint}</p>{default_fence([code_token], 0, opts, env)}</div>'
    md.renderer.rules['fence'] = fence
    def index_passage(text, ident, section):
        SEARCH.append({'chapter': n, 'language': 'en' if english else 'zh-CN', 'title': short(ch),
                       'section': section, 'url': url(ch) + '#' + ident, 'text': text})

    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.type == 'heading_open':
            label = tokens[i + 1].content
            numeric = re.match(rf'^({n}\.\d+(?:\.\d+)*)\s', label)
            fig = re.match(r'^(?:图|Figure )(\d+-\d+)\s', label)
            if i == 0:
                ident = f'chapter-{n}'; level = 'h1'
            elif i == 3 and t.tag == 'h2' and not numeric and not fig:
                ident = f'chapter-{n}-subtitle'; level = 'p'; t.attrSet('class', 'chapter-subtitle')
            elif numeric:
                ident = 'section-' + numeric[1].replace('.', '-'); level = 'h2' if numeric[1].count('.') == 1 else 'h3'
                toc.append({'id': ident, 'label': label, 'sub': level == 'h3'}); numbered.append(numeric[1])
            elif fig:
                ident = 'figure-' + fig[1]; level = 'h3'
                current_figure = f'fig-{fig[1]}' + ('-en' if english else '')
            else:
                ident = f'heading-{n}-{i}'; level = t.tag
            t.tag = level; tokens[i + 2].tag = level; t.attrSet('id', ident)
            current_section = label
            if level != 'p': index_passage(label, ident, label)
            i += 3; continue
        if t.level == 0 and (t.nesting == 1 or t.type == 'fence'):
            block_count += 1; ident = f'passage-{n}-{block_count}'; t.attrSet('id', ident)
            if t.type == 'fence' and t.info.strip() == 'mermaid':
                if current_figure not in FIGURES: raise ValueError(f'Missing figure in chapter {n}')
                f = FIGURES[current_figure]
                assert f['chapter'] == n and digest(t.content.rstrip('\n')) == f['source_sha256']
                t.meta['figure'] = current_figure; found_figures.append(current_figure)
            j = i + 1
            if t.nesting == 1:
                depth = 1
                while j < len(tokens) and depth:
                    depth += tokens[j].nesting; j += 1
            rendered = md.renderer.render(tokens[i:j], md.options, {})
            searchable = plain(rendered)
            if searchable: index_passage(searchable, ident, current_section)
            i = j; continue
        i += 1
    html = md.renderer.render(tokens, md.options, {})
    reference_md = MarkdownIt('commonmark', {'html': False}).enable('table')
    original_fence = reference_md.renderer.rules['fence']
    reference_md.renderer.rules['fence'] = lambda ts, i, opts, env: '' if ts[i].info.strip() == 'mermaid' else original_fence(ts, i, opts, env)
    expected = plain(reference_md.render(text))
    assert plain(html) == expected, f'Rendered text differs in chapter {n}'
    assert found_figures == ch['figures'], f'Figure order differs in chapter {n}'
    toc_html = ''.join(f'<a href="#{t["id"]}" class="{"subsection" if t["sub"] else "section"}">{escape(t["label"])}</a>' for t in toc)
    chapters = ENGLISH if english else {c['number']: c for c in CHAPTERS}
    contents_url, contents_label = ('/en.html', 'Contents') if english else ('/', '全书目录')
    previous_label, next_label = ('Previous chapter', 'Next chapter') if english else ('上一章', '下一章')
    prev = f'<a rel="prev" href="{url(chapters[n-1])}"><small>{previous_label}</small>{escape(chapters[n-1]["title"])}</a>' if n > 1 else f'<a href="{contents_url}">{contents_label}</a>'
    nxt = f'<a rel="next" href="{url(chapters[n+1])}"><small>{next_label}</small>{escape(chapters[n+1]["title"])}</a>' if n < 23 else f'<a href="{contents_url}">{contents_label}</a>'
    chapter_number = f'Chapter {n:02} of 23' if english else f'第 {n:02} / 23 章'
    toc_label = 'In this chapter' if english else f'本章目录 · {len(toc)}节'
    pagination_label = 'Previous and next chapters' if english else '前后章节'
    edition_note = ''
    if english and n == 6:
        edition_note = '<p class="edition-note">This chapter follows the reader-facing draft. The Chinese working manuscript has a different section structure.</p>'
    body = f'<div class="chapter-meta"><a href="{contents_url}">{contents_label}</a><span>{chapter_number}</span></div>{edition_note}<details class="inline-toc"><summary>{toc_label}</summary>{toc_html}</details><article class="prose" id="chapter-body">{html}</article><nav class="chapter-pagination" aria-label="{pagination_label}">{prev}{nxt}</nav>'
    (OUT / url(ch).lstrip('/')).write_text(shell(ch['title'], body, n, toc_html, english))
    key = 'english_chapters' if english else 'chapters'
    MANIFEST[key].append({'number': n, 'title': ch['title'], 'url': url(ch), 'source_sha256': ch['source_sha256'], 'reader_sha256': digest(text), 'rendered_text_sha256': digest(expected), 'rendered_text_characters': len(expected), 'numbered_sections': numbered, 'figures': found_figures})


def home(english=False):
    sections = []
    chapters = ENGLISH.values() if english else CHAPTERS
    action = 'Read chapter' if english else '阅读全文'
    byline = f'<p class="book-byline">{"By" if english else "作者"} mac1en</p>'
    for zh, en, start, end in GROUPS:
        label = en if english else zh
        rows = ''.join(f'<a class="chapter-row" href="{url(c)}"><span class="row-number">{c["number"]:02}</span><div><h3>{escape(short(c))}</h3><p>{escape(c["subtitle"])}</p></div><span class="row-action">{action}</span></a>' for c in chapters if start <= c['number'] <= end)
        sections.append(f'<section class="book-group"><h2>{label}</h2>{rows}</section>')
    if english:
        intro = f'''<section class="book-hero"><p class="eyebrow">English edition · Working manuscript</p><h1>Beyond Code<span>AI-Native Software Engineering</span></h1>{byline}<p class="hero-description">What does it take to delegate software work to agents? Follow a task from intent and execution through evidence, collaboration, recovery, and long-term evolution.</p><div class="book-stats"><span><b>23</b>chapters</span><span><b>14</b>figures</span><span><b>{UPDATED:%m.%d}</b>updated in {UPDATED.year}</span></div><div class="hero-actions"><a class="primary-link" href="/chapters/01-en.html">Start with Chapter 1</a><button type="button" data-open-search>Search the book</button></div></section><section id="chapters"><div class="section-heading"><h2>Contents</h2><a href="/figures-en.html">Browse all figures</a></div>'''
    else:
        intro = f'''<section class="book-hero"><p class="eyebrow">超越代码 · 完整工作稿</p><h1>Beyond Code<span>AI 原生软件工程</span></h1>{byline}<p class="hero-description">从一次任务的意图与执行，到证据、协作、恢复和长期演进。沿着具体问题，理解受托智能执行需要哪些工程边界。</p><div class="book-stats"><span><b>23</b>章正文</span><span><b>14</b>张机制简图</span><span><b>{UPDATED:%m.%d}</b>{UPDATED.year}年更新</span></div><div class="hero-actions"><a class="primary-link" href="/chapters/01.html">从第1章开始</a><button type="button" data-open-search>带着问题搜索</button></div><p class="draft-note">当前版本为工作稿。正文区分观察事实、当时判断、事后推断与建议；案例保留失败、未知和适用范围。</p></section><section id="chapters"><div class="section-heading"><h2>全书目录</h2><a href="/figures.html">查看全部机制简图</a></div>'''
    return shell('Contents' if english else '全书目录', intro + ''.join(sections) + '</section>', english=english)


def figure_image(f):
    english = f['id'].endswith('-en')
    label = f'{"Figure " if english else "图"}{f["number"]} {escape(f["title"])}'
    zoom = 'Enlarge ' if english else '放大'
    return f'<a href="/figures/{f["id"]}.svg" data-zoom aria-label="{zoom}{label}"><img src="/figures/{f["id"]}.svg" alt="{label}" width="{f["width"]}" height="{f["height"]}" loading="lazy"></a>'


def figures_page(english=False):
    cards = []
    number_label, chapter_label, zoom_label, svg_label = ('Figure ', 'Read in context', 'Enlarge', 'Open actual-size SVG') if english else ('图', '回到正文', '放大查看', '打开原尺寸 SVG')
    figures = BOOK['english_figures'] if english else BOOK['figures']
    for f in figures:
        chapter = ENGLISH[f['chapter']] if english else CHAPTERS[f['chapter'] - 1]
        cards.append(f'<section class="gallery-figure" id="{f["id"]}"><div class="section-heading"><h2>{number_label}{f["number"]} {escape(f["title"])}</h2><a href="{url(chapter)}#figure-{f["number"]}">{chapter_label}</a></div>{figure_image(f)}<p>{escape(f["caption"])}</p><a href="/figures/{f["id"]}.svg" data-zoom>{zoom_label}</a> · <a href="/figures/{f["id"]}.svg" target="_blank" rel="noopener">{svg_label}</a></section>')
    title = 'Figures' if english else '机制简图'
    description = 'Open a figure at full size or follow its link to the relevant chapter.' if english else '14张简图与所属章节原位对应。点击图形查看原尺寸；图注保留教学、建议机制与历史案例各自的范围。'
    return shell(title, f'<div class="gallery-intro"><h1>{title}</h1><p>{description}</p></div>' + ''.join(cards), english=english, gallery=True)


def main():
    assert [c['number'] for c in CHAPTERS] == list(range(1, 24))
    assert list(ENGLISH) == list(range(1, 24))
    assert len(BOOK['figures']) == len(BOOK['english_figures']) == 14
    if OUT.is_symlink(): raise ValueError('Refusing a symlink output directory')
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    for folder in ['chapters', 'assets', 'figures']: (OUT / folder).mkdir(exist_ok=True)
    for name in ['site.css', 'site.js']: shutil.copyfile(ROOT / 'reader' / name, OUT / 'assets' / name)
    for f in FIGURES.values():
        for ext in ['svg', 'png']:
            source = CONTENT / 'figures' / f'{f["id"]}.{ext}'
            assert hashlib.sha256(source.read_bytes()).hexdigest() == f[f'{ext}_sha256']
            shutil.copyfile(source, OUT / 'figures' / source.name)
    for ch in CHAPTERS: render_chapter(ch)
    for ch in ENGLISH.values(): render_chapter(ch)
    (OUT / 'index.html').write_text(home())
    (OUT / 'en.html').write_text(home(english=True))
    (OUT / 'figures.html').write_text(figures_page())
    (OUT / 'figures-en.html').write_text(figures_page(english=True))
    (OUT / 'search.json').write_text(json.dumps(SEARCH, ensure_ascii=False, separators=(',', ':')))
    (OUT / 'book-manifest.json').write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=2))
    print(json.dumps({'chapters': len(CHAPTERS), 'english_chapters': len(ENGLISH), 'figures': len(FIGURES), 'numbered_sections': sum(len(c['numbered_sections']) for c in MANIFEST['chapters']), 'search_passages': len(SEARCH), 'output': str(OUT)}))


if __name__ == '__main__': main()
