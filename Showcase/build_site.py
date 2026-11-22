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
FIGURES = {f['id']: f for f in BOOK['figures']}
for figure in FIGURES.values():
    viewbox = ET.parse(CONTENT / 'figures' / f'{figure["id"]}.svg').getroot().get('viewBox').split()
    figure['width'], figure['height'] = [round(float(v)) for v in viewbox[2:]]
SEARCH = []
MANIFEST = {'date': BOOK['date'], 'source_fingerprint': BOOK['source_fingerprint'], 'chapters': [], 'figures': BOOK['figures']}
GROUPS = [('问题与基础', 1, 3), ('意图、上下文与事实', 4, 6), ('执行与验证', 7, 10),
          ('认知、自治与观察', 11, 14), ('记忆、演化与组织', 15, 17),
          ('责任、安全与运行', 18, 20), ('生命周期与实践', 21, 23)]


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
def url(ch): return f'/chapters/{ch["number"]:02}.html'
def short(ch): return re.sub(r'^第\d+章\s*', '', ch['title'])


def navigation(current=0):
    parts = []
    for title, start, end in GROUPS:
        links = ''.join(f'<a href="{url(c)}"{chr(32)+"aria-current=\"page\"" if c["number"] == current else ""}><span class="chapter-number">{c["number"]:02}</span><span>{escape(short(c))}</span></a>' for c in CHAPTERS if start <= c['number'] <= end)
        parts.append(f'<section><h2>{title}</h2>{links}</section>')
    return ''.join(parts)


def shell(title, body, current=0, toc=''):
    nav = navigation(current)
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} · Beyond Code</title><meta name="description" content="Beyond Code：AI原生软件工程。23章完整工作稿与14张机制简图，支持全文搜索和章节阅读。">
<link rel="stylesheet" href="/assets/site.css"><script src="/assets/site.js" defer></script></head>
<body data-chapter="{current}"><a class="skip-link" href="#main">跳到正文</a>
<header class="topbar"><button class="menu-toggle" type="button" aria-label="打开章节目录" data-open-nav>目录</button>
<a class="brand" href="/"><span class="brandmark">B/</span><span>BEYOND CODE<small>AI-NATIVE SOFTWARE ENGINEERING</small></span></a>
<nav class="topnav" aria-label="全站导航"><a href="/">全书目录</a><a href="/figures.html">机制简图</a></nav>
<div class="header-actions"><span class="version">工作稿 · {UPDATED:%Y.%m.%d}</span><button type="button" data-open-search>搜索全书 <kbd>⌘ K</kbd></button><button type="button" data-theme aria-label="切换深色主题">深色</button></div></header>
<aside class="sidebar"><nav aria-label="章节目录">{nav}</nav><div class="sidebar-foot">23章正文 · 14张机制简图<br>同步至{UPDATED.year}年{UPDATED.month}月{UPDATED.day}日</div></aside>
<main id="main" class="content" tabindex="-1">{body}<footer><a href="/">Beyond Code</a><span>工作稿持续修订；案例的适用范围以正文为准。</span></footer></main>
{f'<aside class="page-toc"><h2>本章目录</h2><nav aria-label="本章小节">{toc}</nav><a class="back-top" href="#main">回到章首</a></aside>' if toc else ''}
<dialog id="nav-dialog"><div class="dialog-top"><strong>章节目录</strong><button type="button" data-close-dialog>关闭</button></div><nav aria-label="移动章节目录">{nav}</nav></dialog>
<dialog id="search-dialog"><div class="dialog-top"><label for="book-search">搜索全书</label><button type="button" data-close-dialog>关闭</button></div>
<form role="search"><input id="book-search" type="search" placeholder="搜索概念、例子或代码，如 Checkpoint、净增量" autocomplete="off"><button type="button" id="clear-search">清空</button></form>
<p id="search-status" role="status" aria-live="polite">输入关键词，搜索23章正文、表格、代码示例与图注。</p><ol id="search-results"></ol></dialog>
<dialog id="figure-dialog" aria-labelledby="figure-dialog-title"><div class="dialog-top"><strong id="figure-dialog-title">机制图</strong><button type="button" data-close-dialog>关闭</button></div><div class="figure-tools"><button type="button" data-zoom-out aria-label="缩小机制图">缩小</button><button type="button" data-zoom-in aria-label="放大机制图">放大</button><button type="button" data-zoom-fit>适合宽度</button><button type="button" data-zoom-reset>原尺寸</button></div><p id="figure-status" role="status">可横向、纵向滑动查看</p><div class="figure-viewport" tabindex="0" aria-label="可横向、纵向滚动的机制图"><img alt=""></div></dialog>
</body></html>'''


def render_chapter(ch):
    n = ch['number']; text = (CONTENT / 'chapters' / f'{n:02}.md').read_text()
    md = MarkdownIt('commonmark', {'html': False}).enable('table')
    tokens = md.parse(text); toc = []; found_figures = []; numbered = []; block_count = 0
    current_section = ch['title']; current_figure = None
    default_fence = md.renderer.rules['fence']
    md.renderer.rules['table_open'] = lambda ts, i, opts, env: '<p class="overflow-hint" data-reading-control>表格可左右滑动，查看其余列。</p><div class="table-scroll" tabindex="0" role="region" aria-label="可横向滚动的数据表">' + md.renderer.renderToken(ts, i, opts, env)
    md.renderer.rules['table_close'] = lambda ts, i, opts, env: '</table></div>\n'
    def fence(ts, i, opts, env):
        t = ts[i]
        if t.info.strip() == 'mermaid':
            f = FIGURES[t.meta['figure']]
            return f'<figure class="mechanism" id="{t.attrGet("id")}" data-figure="{f["id"]}">{figure_image(f)}<div data-reading-control><a href="/figures/{f["id"]}.svg" data-zoom>放大查看</a><a href="/figures/{f["id"]}.svg" target="_blank" rel="noopener">原尺寸 SVG</a><a href="/figures/{f["id"]}.png" download>下载 PNG</a></div></figure>\n'
        code_token = copy(t)
        code_token.attrs = {key: value for key, value in t.attrs.items() if key != 'id'}
        return f'<div id="{t.attrGet("id")}" class="code-block"><p class="overflow-hint" data-reading-control>代码可左右滑动，查看完整内容。</p>{default_fence([code_token], 0, opts, env)}</div>'
    md.renderer.rules['fence'] = fence
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.type == 'heading_open':
            label = tokens[i + 1].content
            numeric = re.match(rf'^({n}\.\d+(?:\.\d+)*)\s', label)
            fig = re.match(r'^图(\d+-\d+)\s', label)
            if i == 0:
                ident = f'chapter-{n}'; level = 'h1'
            elif i == 3 and t.tag == 'h2' and not numeric and not fig:
                ident = f'chapter-{n}-subtitle'; level = 'p'; t.attrSet('class', 'chapter-subtitle')
            elif numeric:
                ident = 'section-' + numeric[1].replace('.', '-'); level = 'h2' if numeric[1].count('.') == 1 else 'h3'
                toc.append({'id': ident, 'label': label, 'sub': level == 'h3'}); numbered.append(numeric[1])
            elif fig:
                ident = 'figure-' + fig[1]; level = 'h3'; current_figure = 'fig-' + fig[1]
            else:
                ident = f'heading-{n}-{i}'; level = t.tag
            t.tag = level; tokens[i + 2].tag = level; t.attrSet('id', ident)
            current_section = label
            if level != 'p': SEARCH.append({'chapter': n, 'title': short(ch), 'section': label, 'url': url(ch) + '#' + ident, 'text': label})
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
            if searchable: SEARCH.append({'chapter': n, 'title': short(ch), 'section': current_section, 'url': url(ch) + '#' + ident, 'text': searchable})
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
    prev = f'<a rel="prev" href="{url(CHAPTERS[n-2])}"><small>上一章</small>{escape(CHAPTERS[n-2]["title"])}</a>' if n > 1 else '<a href="/"><small>阅读入口</small>全书目录</a>'
    nxt = f'<a rel="next" href="{url(CHAPTERS[n])}"><small>下一章</small>{escape(CHAPTERS[n]["title"])}</a>' if n < 23 else '<a href="/"><small>已到最后一章</small>返回全书目录</a>'
    body = f'<div class="chapter-meta"><a href="/">全书目录</a><span>第 {n:02} / 23 章</span></div><details class="inline-toc"><summary>本章目录 · {len(toc)}节</summary>{toc_html}</details><article class="prose" id="chapter-body">{html}</article><nav class="chapter-pagination" aria-label="前后章节">{prev}{nxt}</nav>'
    (OUT / 'chapters' / f'{n:02}.html').write_text(shell(ch['title'], body, n, toc_html))
    MANIFEST['chapters'].append({'number': n, 'title': ch['title'], 'url': url(ch), 'source_sha256': ch['source_sha256'], 'reader_sha256': digest(text), 'rendered_text_sha256': digest(expected), 'rendered_text_characters': len(expected), 'numbered_sections': numbered, 'figures': found_figures})


def home():
    sections = []
    for label, start, end in GROUPS:
        rows = ''.join(f'<a class="chapter-row" href="{url(c)}"><span class="row-number">{c["number"]:02}</span><div><h3>{escape(short(c))}</h3><p>{escape(c["subtitle"])}</p></div><span class="row-action">阅读全文</span></a>' for c in CHAPTERS if start <= c['number'] <= end)
        sections.append(f'<section class="book-group"><h2>{label}</h2>{rows}</section>')
    return shell('全书目录', f'''<section class="book-hero"><p class="eyebrow">超越代码 · 完整工作稿</p><h1>Beyond Code<span>AI 原生软件工程</span></h1><p class="hero-description">从一次任务的意图与执行，到证据、协作、恢复和长期演进。沿着具体问题，理解受托智能执行需要哪些工程边界。</p><div class="book-stats"><span><b>23</b>章正文</span><span><b>14</b>张机制简图</span><span><b>{UPDATED:%m.%d}</b>{UPDATED.year}年更新</span></div><div class="hero-actions"><a class="primary-link" href="/chapters/01.html">从第1章开始</a><button type="button" data-open-search>带着问题搜索</button></div><p class="draft-note">当前版本为工作稿。正文区分观察事实、当时判断、事后推断与建议；案例保留失败、未知和适用范围。</p></section><section id="chapters"><div class="section-heading"><h2>全书目录</h2><a href="/figures.html">查看全部机制简图</a></div>''' + ''.join(sections) + '</section>')


def figure_image(f):
    return f'<a href="/figures/{f["id"]}.svg" data-zoom aria-label="放大图{f["number"]} {escape(f["title"])}"><img src="/figures/{f["id"]}.svg" alt="图{f["number"]} {escape(f["title"])}" width="{f["width"]}" height="{f["height"]}" loading="lazy"></a>'


def figures_page():
    cards = []
    for f in BOOK['figures']:
        cards.append(f'<section class="gallery-figure" id="{f["id"]}"><div class="section-heading"><h2>图{f["number"]} {escape(f["title"])}</h2><a href="/chapters/{f["chapter"]:02}.html#figure-{f["number"]}">回到正文</a></div>{figure_image(f)}<p>{escape(f["caption"])}</p><a href="/figures/{f["id"]}.svg" data-zoom>放大查看</a> · <a href="/figures/{f["id"]}.svg" target="_blank" rel="noopener">打开原尺寸 SVG</a></section>')
    return shell('机制简图', '<div class="gallery-intro"><p class="eyebrow">按问题阅读</p><h1>机制简图</h1><p>14张简图与所属章节原位对应。点击图形查看原尺寸；图注保留教学、建议机制与历史案例各自的范围。</p></div>' + ''.join(cards))


def main():
    assert [c['number'] for c in CHAPTERS] == list(range(1, 24))
    assert len(FIGURES) == 14
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
    (OUT / 'index.html').write_text(home())
    (OUT / 'figures.html').write_text(figures_page())
    (OUT / 'search.json').write_text(json.dumps(SEARCH, ensure_ascii=False, separators=(',', ':')))
    (OUT / 'book-manifest.json').write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=2))
    print(json.dumps({'chapters': len(CHAPTERS), 'figures': len(FIGURES), 'numbered_sections': sum(len(c['numbered_sections']) for c in MANIFEST['chapters']), 'search_passages': len(SEARCH), 'output': str(OUT)}))


if __name__ == '__main__': main()
