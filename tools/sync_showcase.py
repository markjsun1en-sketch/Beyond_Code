#!/usr/bin/env python3
"""Sync the current 23 reader chapters and 14 figures into the existing Sites checkout."""
from pathlib import Path
from urllib.parse import unquote
import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime
from zoneinfo import ZoneInfo
from showcase_workflow import source_inventory

ROOT = Path(__file__).resolve().parent.parent
SITE_ID = 'appgprj_6a8276ef7e0c81919a7e490c3ea5bfc2'
sha = lambda data: hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--checkout', type=Path, required=True)
    parser.add_argument('--date', default=datetime.now(ZoneInfo('Asia/Shanghai')).date().isoformat()); args=parser.parse_args()
    target = args.checkout.resolve(); hosting = target / '.openai/hosting.json'
    config = json.loads(hosting.read_text())
    if config['project_id'] != SITE_ID: raise ValueError('Refusing to sync into a different Site')
    inventory = source_inventory(ROOT)
    files = sorted((p for p in (ROOT/'OptimizedDocs').glob('第*章_*.md') if p.name!='第2章_证据化修订样例.md'),key=lambda p:int(re.match(r'第(\d+)',p.name)[1]))
    assert [int(re.match(r'第(\d+)',p.name)[1]) for p in files] == list(range(1,24))
    chapter_urls = {p.resolve():f'/chapters/{n:02}.html' for n,p in enumerate(files,1)}
    for folder in ['reader','content/chapters','content/figures']:(target/folder).mkdir(parents=True,exist_ok=True)
    for name in ['build_site.py','verify_site.py','site.css','site.js']:shutil.copyfile(ROOT/'Showcase'/name,target/'reader'/name)
    figures=[]
    for manifest in sorted((ROOT/'OptimizedDocs/diagrams').glob('phase-*-manifest.json')):
        for f in json.loads(manifest.read_text())['figures']:
            item={k:f[k] for k in ['id','number','title','caption','source_sha256','svg_sha256','png_sha256']}
            item['caption']=re.sub(r'\[([^\]]+)\]\(\.\./Evidence/receipts/[^)]+\)',r'\1',item['caption'])
            item['chapter']=int(f['number'].split('-')[0]);figures.append(item)
            for ext in ['svg','png']:
                source=manifest.parent/f'{f["id"]}.{ext}';assert sha(source.read_bytes())==f[f'{ext}_sha256']
                shutil.copyfile(source,target/'content/figures'/source.name)
    figures.sort(key=lambda f:tuple(int(x) for x in f['number'].split('-')))
    assert len(figures)==len({f['id'] for f in figures})==14
    chapters=[]; source_references=0; cross_links=0; removed_headers=0
    for n,p in enumerate(files,1):
        original=p.read_text(); lines=original.splitlines(); title=lines[0].lstrip('# ').strip();subtitle=lines[1].lstrip('# ').strip() if len(lines)>1 and lines[1].startswith('## ') else ''
        def replace_link(match):
            nonlocal source_references,cross_links
            label,dest=match[1],unquote(match[2].strip('<>'))
            if dest.startswith(('https://','http://','#')):return match[0]
            dest_path, _, anchor=dest.partition('#');resolved=(p.parent/dest_path).resolve()
            if resolved in chapter_urls:
                cross_links+=1;return f'[{label}]({chapter_urls[resolved]})'
            if dest_path.startswith('../Evidence/receipts/'):
                source_references+=1;return label
            raise ValueError(f'Unexpected reader link in {p.name}: {dest}')
        filtered=[];in_fence=False;marker=None
        for line in lines:
            if not in_fence and re.match(r'^> (工作稿状态|回接说明)：',line):removed_headers+=1;continue
            fence=re.match(r'^\s*(`{3,}|~{3,})',line)
            if fence:
                if not in_fence:in_fence=True;marker=fence[1][0]
                elif fence[1][0]==marker:in_fence=False
                filtered.append(line);continue
            filtered.append(line if in_fence else re.sub(r'\[([^\]]+)\]\(([^)]+)\)',replace_link,line))
        clean='\n'.join(filtered).rstrip()+'\n'
        assert not re.search(r'/Users/|file://|\.\./(?:Evidence|RevisedResult|OringinalDocs)/|CLM-|ER-2026|RR-0',clean)
        (target/'content/chapters'/f'{n:02}.md').write_text(clean)
        chapters.append({'number':n,'title':title,'subtitle':subtitle,'source_sha256':sha(original.encode()),'reader_sha256':sha(clean.encode()),'figures':[f['id'] for f in figures if f['chapter']==n]})
    book={'date':args.date,'chapters':chapters,'figures':figures,'source_fingerprint':inventory['source_fingerprint']}
    (target/'content/book.json').write_text(json.dumps(book,ensure_ascii=False,indent=2))
    (target/'reader/requirements.txt').write_text('markdown-it-py==4.0.0\n')
    config['static']={'directory':'dist'};hosting.write_text(json.dumps(config,indent=2)+'\n')
    report={'date':args.date,'chapters':23,'figures':14,'source_fingerprint':inventory['source_fingerprint'],'input_files':inventory['files'],'editorial_header_lines_removed':removed_headers,'source_labels_preserved':source_references,'cross_chapter_links_rewritten':cross_links,'source_files':[{'file':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes())} for p in files]}
    (target/'sync-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k not in ('source_files','input_files')},ensure_ascii=False))


if __name__=='__main__':main()
