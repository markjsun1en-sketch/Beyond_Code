#!/usr/bin/env python3
"""Prepare, check and verify publication of the existing Beyond Code Showcase.

Sites native tools own credentials, source push, version saving and deployment.
This entry point never deploys implicitly or stores credentials.
"""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
import argparse
import hashlib
import json
import re
import subprocess
import sys
import shutil

ROOT = Path(__file__).resolve().parent.parent
READERS = ('build_site.py', 'verify_site.py', 'site.css', 'site.js')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def fingerprint(files):
    return sha(json.dumps(files, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode())


def read(path):
    return json.loads(path.read_text())


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def now():
    return datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds')


def config(root):
    return read(root / 'Showcase/publication.json')


def chapter_files(root):
    return sorted((p for p in (root / 'OptimizedDocs').glob('第*章_*.md')
                   if p.name != '第2章_证据化修订样例.md'),
                  key=lambda p: int(re.match(r'第(\d+)', p.name)[1]))


def figure_inventory(root, chapters, manifests, expected_ids, english=False):
    from markdown_it import MarkdownIt
    paths = list(manifests)
    figures = {}
    for manifest in manifests:
        for figure in read(manifest)['figures']:
            ident = figure['id']
            require(ident not in figures, f'Duplicate figure {ident}')
            figures[ident] = figure
            for ext in ('svg', 'png'):
                path = manifest.parent / f'{ident}.{ext}'
                require(path.is_file() and sha(path.read_bytes()) == figure[f'{ext}_sha256'],
                        f'Stale or missing export: {ident}.{ext}; regenerate its owning batch')
                paths.append(path)
    require(set(figures) == set(expected_ids), 'Figure inventory differs from publication.json')
    seen = set()
    for chapter in chapters:
        text = chapter.read_text()
        blocks = list(re.finditer(r'```mermaid\r?\n([\s\S]*?)\r?\n```', text))
        tokens = MarkdownIt().parse(text)
        require(len(blocks) == sum(t.type == 'fence' and t.info.strip() == 'mermaid' for t in tokens),
                f'Unsupported Mermaid fence format in {chapter.name}')
        for match in blocks:
            prefix = 'Figure ' if english else '图'
            headings = list(re.finditer(rf'^#{{2,6}} {prefix}(\d+-\d+) (.+)$', text[:match.start()], re.M))
            require(bool(headings), f'Missing figure heading: {chapter.name}')
            number, title = headings[-1].groups()
            ident = f'fig-{number}' + ('-en' if english else '')
            require(ident in figures and ident not in seen, f'Unmapped or duplicate figure {ident}')
            seen.add(ident)
            figure = figures[ident]
            caption = re.sub(r'^\*|\*$', '', re.split(r'\n\s*\n', text[match.end():].lstrip())[0])
            expected = {'number': number, 'title': title, 'caption': caption,
                        'chapter': str(chapter.relative_to(root)), 'source_sha256': sha(match[1].encode())}
            for key, value in expected.items():
                require(figure[key] == value, f'Stale {key} for {ident}; regenerate its owning batch')
    require(seen == set(figures), 'Orphaned diagram export or missing chapter Mermaid source')
    return paths


def source_inventory(root):
    """Fail on missing chapters and stale figure sources, captions, or exports."""
    cfg = config(root)
    chapters = chapter_files(root)
    require([int(re.match(r'第(\d+)', p.name)[1]) for p in chapters] == cfg['chapter_numbers'],
            'Chapter inventory changed; reconcile publication.json and the reader before publishing')
    translations = root / 'Showcase/translations'
    expected_translations = [translations / f'{n:02}.en.md' for n in cfg['english_chapters']]
    require(sorted(translations.glob('*.en.md')) == expected_translations
            and cfg['english_chapters'] == cfg['chapter_numbers'],
            'The English edition must include the same chapter inventory as the Chinese edition')
    figure_ids = cfg['figure_ids']
    manifests = sorted((root / 'OptimizedDocs/diagrams').glob('phase-*-manifest.json'))
    paths = chapters + expected_translations + [root / 'Showcase/publication.json', root / 'tools/sync_showcase.py']
    paths += [root / 'Showcase' / name for name in READERS]
    paths += figure_inventory(root, chapters, manifests, figure_ids)
    paths += figure_inventory(root, expected_translations, [translations / 'diagrams/manifest.json'],
                              [f'{ident}-en' for ident in figure_ids], english=True)
    files = {str(p.relative_to(root)): sha(p.read_bytes()) for p in paths}
    return {'source_fingerprint': fingerprint(files), 'files': files}


def tree_files(path):
    return {str(p.relative_to(path)): sha(p.read_bytes()) for p in sorted(path.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}


def checkout_sources(checkout):
    files = {}
    for name in ('content', 'reader'):
        files.update({f'{name}/{p}': h for p, h in tree_files(checkout / name).items()})
    for name in ('.openai/hosting.json', 'sync-report.json'):
        files[name] = sha((checkout / name).read_bytes())
    return files


def check_identity(root, checkout):
    require(read(checkout / '.openai/hosting.json')['project_id'] == config(root)['project_id'],
            'Wrong Site checkout; do not create or substitute another Site')


def run(*args, cwd=None):
    subprocess.run(list(map(str, args)), cwd=cwd, check=True)


def prepare(root, checkout, date):
    check_identity(root, checkout)
    before = source_inventory(root)
    run(sys.executable, root / 'tools/sync_showcase.py', '--checkout', checkout, '--date', date)
    run(sys.executable, checkout / 'reader/build_site.py')
    run(sys.executable, checkout / 'reader/verify_site.py', '--book-root', root)
    after = source_inventory(root)
    require(before == after, 'Source changed during preparation; prepare again')
    public = read(checkout / 'dist/book-manifest.json')
    require(public['source_fingerprint'] == after['source_fingerprint'], 'Build fingerprint mismatch')
    outputs = tree_files(checkout / 'dist')
    result = {'schema': 1, 'prepared_at': now(), 'project_id': config(root)['project_id'],
              **after, 'checkout_sources': checkout_sources(checkout), 'outputs': outputs,
              'output_fingerprint': fingerprint(outputs), 'checks': read(checkout / 'verification-report.json')}
    write(checkout / 'showcase-prepared.json', result)
    print(json.dumps({'status': 'prepared', 'source_fingerprint': result['source_fingerprint'],
                      'output_fingerprint': result['output_fingerprint']}, ensure_ascii=False))


def check_prepared(root, checkout):
    check_identity(root, checkout)
    prepared = read(checkout / 'showcase-prepared.json')
    require(prepared['project_id'] == config(root)['project_id'], 'Prepared record belongs to another Site')
    require(source_inventory(root)['source_fingerprint'] == prepared['source_fingerprint'],
            'Book, figures or reader changed after preparation; prepare again')
    require(checkout_sources(checkout) == prepared['checkout_sources'],
            'Site snapshot changed after preparation; prepare again')
    require(tree_files(checkout / 'dist') == prepared['outputs'],
            'Build output changed after preparation; prepare again')
    require(not prepared['checks']['errors'], 'Preparation has unresolved errors')
    return prepared


class PublicHTML(HTMLParser):
    """Reader HTML signature; hosted platform inline scripts are outside the book.

    Local asset script references remain checked; their file bytes are checked too.
    Text inside pre/code retains exact whitespace.
    """
    def __init__(self):
        super().__init__(); self.parts = []; self.skip_script = False; self.pre = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'script' and not values.get('src', '').startswith('/assets/'):
            self.skip_script = True; return
        if self.skip_script: return
        if tag == 'pre': self.pre = True
        self.parts.append(('start', tag, sorted(attrs)))

    def handle_endtag(self, tag):
        if self.skip_script:
            if tag == 'script': self.skip_script = False
            return
        if tag == 'pre': self.pre = False
        self.parts.append(('end', tag))

    def handle_data(self, data):
        if self.skip_script: return
        if self.pre or data.strip(): self.parts.append(('text', data if self.pre else data.strip()))


def html_signature(raw):
    parser = PublicHTML(); parser.feed(raw.decode()); return parser.parts


def fetch(url):
    # macOS Python distributions may not inherit the system trust store. curl
    # uses its configured CA store; certificate and hostname checks stay on.
    if shutil.which('curl'):
        result = subprocess.run(['curl', '--fail', '--silent', '--show-error', '--location',
                                 '--proto', '=https', '--proto-redir', '=https', '--max-redirs', '5',
                                 '--max-time', '30', '--header', 'Cache-Control: no-cache', url],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        require(result.returncode == 0, result.stderr.decode(errors='replace').strip())
        return result.stdout
    request = Request(url, headers={'Cache-Control': 'no-cache', 'User-Agent': 'Beyond-Code-Publication-Check/1'})
    with urlopen(request, timeout=30) as response:
        require(response.status == 200, f'HTTP {response.status}: {url}')
        return response.read()


def verify_online(checkout, prepared, base_url, fetcher=fetch):
    def compare(item):
        name, expected_hash = item
        try:
            remote = fetcher(base_url.rstrip('/') + '/' + name)
            if name.endswith('.html'):
                require(html_signature(remote) == html_signature((checkout / 'dist' / name).read_bytes()),
                        f'Reader HTML differs: {name}')
            else:
                require(sha(remote) == expected_hash, f'Published bytes differ: {name}')
            return None
        except Exception as error:
            return f'{name}: {error}'
    with ThreadPoolExecutor(max_workers=4) as pool:
        errors = [error for error in pool.map(compare, prepared['outputs'].items()) if error]
    require(not errors, 'Online readback failed: ' + '; '.join(errors[:8]))
    return {'checked_at': now(), 'files_checked': len(prepared['outputs']), 'errors': []}


def tool_data(path):
    value = read(path)
    return value.get('structuredContent', value)


def save_release(root, record):
    path = root / 'Showcase/releases' / f'v{record["version_number"]:04}.json'
    previous = read(path) if path.exists() else {}
    history = previous.get('history', [])
    if previous and not history:
        history.append({'at': previous.get('verified_at', previous.get('recorded_at')), 'status': previous['status'],
                        **({'error': previous['error']} if previous.get('error') else {})})
    event = {'at': now(), 'status': record['status'], **({'error': record['error']} if record.get('error') else {})}
    if not history or (history[-1]['status'], history[-1].get('error')) != (event['status'], event.get('error')):
        history.append(event)
    record['history'] = history
    write(path, record)
    write(root / 'Showcase/latest-release.json', record)


def finish(root, checkout, version_path, deployment_path, review_path):
    version, deployment = tool_data(version_path), tool_data(deployment_path)
    cfg = config(root)
    require(version['project_id'] == deployment['project_id'] == cfg['project_id'], 'Wrong publication project')
    require(version['id'] == deployment['version_id'], 'Deployment does not belong to saved version')
    require(deployment['status'] == 'succeeded', 'Deployment has not succeeded; retain its ID and reconcile it')
    require(deployment['url'].rstrip('/') == cfg['url'].rstrip('/'), 'Unexpected production URL')
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=checkout, text=True).strip()
    require(commit == version['source']['commit_sha'], 'Saved version source differs from current checkout')
    previous = root / 'Showcase/latest-release.json'
    if previous.exists():
        require(read(previous)['version_number'] <= version['version_number'], 'Refusing to overwrite a newer release record')
    record = {'schema': 1, 'status': 'deployed_unverified', 'recorded_at': now(), 'project_id': cfg['project_id'],
              'url': cfg['url'], 'version_number': version['version_number'], 'version_id': version['id'],
              'deployment_id': deployment['id'], 'source_commit': commit}
    save_release(root, record)
    try:
        prepared = check_prepared(root, checkout)
        record.update({key: prepared[key] for key in ('source_fingerprint', 'output_fingerprint', 'files', 'checks')})
        require(not subprocess.check_output(['git', 'status', '--porcelain'], cwd=checkout, text=True).strip(),
                'Site source changed after push; reconcile source before recording completion')
        review = read(review_path)
        require(review['output_fingerprint'] == prepared['output_fingerprint'], 'Browser review belongs to another build')
        require(all(review.get('checks', {}).get(key) is True for key in ('desktop', 'mobile', 'search', 'figures', 'production')),
                'Browser review incomplete; do not invent pass results')
        require(review.get('production_url', '').rstrip('/') == cfg['url'].rstrip('/') and review.get('version_id') == version['id'],
                'Production browser review is not bound to this URL and saved version')
        require(bool(review.get('screenshots')), 'Save an observed browser screenshot')
        record['browser_review'] = review
        record['screenshot_hashes'] = {p: sha(Path(p).read_bytes()) for p in review['screenshots']}
        record['online'] = verify_online(checkout, prepared, cfg['url'])
        require(source_inventory(root)['source_fingerprint'] == prepared['source_fingerprint'],
                'Source changed during online verification; do not mark current book published')
        record['status'] = 'verified'; record['verified_at'] = now()
        save_release(root, record)
    except Exception as error:
        record['error'] = str(error); save_release(root, record); raise
    print(json.dumps({'status': record['status'], 'version': record['version_number'], 'url': cfg['url'],
                      'files_checked': record['online']['files_checked']}, ensure_ascii=False))


def status(root, online=False):
    current = source_inventory(root)
    path = root / 'Showcase/latest-release.json'
    latest = read(path) if path.exists() else {}
    changes = sorted(p for p in set(current['files']) | set(latest.get('files', {}))
                     if current['files'].get(p) != latest.get('files', {}).get(p))
    matched = latest.get('source_fingerprint') == current['source_fingerprint'] and latest.get('status') == 'verified'
    if online:
        public = json.loads(fetch(config(root)['url'] + '/book-manifest.json'))
        matched = matched and public.get('source_fingerprint') == current['source_fingerprint']
    result = {'status': 'current' if matched else 'needs_publication', 'recorded_version': latest.get('version_number'),
              'online_manifest_checked': online, 'changed_inputs': changes,
              'source_fingerprint': current['source_fingerprint']}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if matched else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ('prepare', 'check', 'finish'):
        entry = sub.add_parser(command); entry.add_argument('--checkout', type=Path, required=True)
        if command == 'prepare': entry.add_argument('--date', default=now()[:10])
        if command == 'finish':
            for flag in ('version-json', 'deployment-json', 'review-json'):
                entry.add_argument('--' + flag, type=Path, required=True)
    entry = sub.add_parser('status'); entry.add_argument('--online', action='store_true')
    args = parser.parse_args()
    if args.command == 'prepare': prepare(ROOT, args.checkout.resolve(), args.date)
    elif args.command == 'check':
        result = check_prepared(ROOT, args.checkout.resolve()); print(json.dumps({'status': 'ready', 'source_fingerprint': result['source_fingerprint']}))
    elif args.command == 'finish': finish(ROOT, args.checkout.resolve(), args.version_json, args.deployment_json, args.review_json)
    else: return status(ROOT, args.online)
    return 0


if __name__ == '__main__':
    try: sys.exit(main())
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as error:
        print(f'Showcase workflow stopped: {error}', file=sys.stderr); sys.exit(1)
