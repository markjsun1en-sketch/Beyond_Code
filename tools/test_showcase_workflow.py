"""Regression checks for stale-source and incomplete-publication failure modes."""
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import shutil
import unittest
import argparse
import sys
import showcase_workflow as flow


class PublicationWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = flow.ROOT
        cls.inputs = flow.source_inventory(cls.original)
        if not (cls.site/'showcase-prepared.json').exists():
            raise RuntimeError('Run prepare on the selected checkout first')

    def setUp(self):
        self.temp = TemporaryDirectory(prefix='showcase-workflow-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)/'book';self.root.mkdir()
        for name in self.inputs['files']:
            destination=self.root/name;destination.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(self.original/name,destination)
        self.checkout=Path(self.temp.name)/'site';self.checkout.mkdir()
        for name in ('content','reader','dist','.openai'):
            shutil.copytree(self.site/name,self.checkout/name,ignore=shutil.ignore_patterns('__pycache__'))
        for name in ('sync-report.json','showcase-prepared.json'):
            shutil.copyfile(self.site/name,self.checkout/name)

    def chapter(self):
        return next((self.root/'OptimizedDocs').glob('第9章_*'))

    def test_current_preparation_matches(self):
        self.assertEqual(flow.check_prepared(self.root,self.checkout)['source_fingerprint'],self.inputs['source_fingerprint'])

    def test_manuscript_change_requires_new_preparation(self):
        p=self.chapter();p.write_text(p.read_text()+'\n新的正文。\n')
        with self.assertRaisesRegex(ValueError,'changed after preparation'):flow.check_prepared(self.root,self.checkout)

    def test_caption_only_edit_is_detected(self):
        p=self.chapter();text=p.read_text();text=text.replace('建议机制：实线表示材料如何进入用途判断','建议机制：本次改写实线表示材料如何进入用途判断',1)
        self.assertNotEqual(text,p.read_text());p.write_text(text)
        with self.assertRaisesRegex(ValueError,'Stale caption'):flow.source_inventory(self.root)

    def test_title_only_edit_is_detected(self):
        p=self.chapter();p.write_text(p.read_text().replace('## 图9-1 旧证据能否用于这次决定','## 图9-1 已更新的图题',1))
        with self.assertRaisesRegex(ValueError,'Stale title'):flow.source_inventory(self.root)

    def test_bold_caption_uses_the_renderers_exact_rule(self):
        manifest=next(p for p in (self.root/'OptimizedDocs/diagrams').glob('phase-*-manifest.json') if any(f['id']=='fig-9-1' for f in flow.read(p)['figures']))
        data=flow.read(manifest);figure=next(f for f in data['figures'] if f['id']=='fig-9-1')
        p=self.chapter();old=figure['caption'];p.write_text(p.read_text().replace(old,'**'+old+'**',1))
        figure['caption']='*'+old+'*';flow.write(manifest,data)
        self.assertTrue(flow.source_inventory(self.root)['source_fingerprint'])

    def test_mermaid_only_edit_is_detected(self):
        p=self.chapter();p.write_text(p.read_text().replace('```mermaid\n','```mermaid\n%% new source\n',1))
        with self.assertRaisesRegex(ValueError,'Stale source_sha256'):flow.source_inventory(self.root)

    def test_export_damage_is_detected(self):
        p=self.root/'OptimizedDocs/diagrams/fig-9-1.svg';p.write_bytes(p.read_bytes()+b' ')
        with self.assertRaisesRegex(ValueError,'Stale or missing export'):flow.source_inventory(self.root)

    def test_reader_edit_requires_new_preparation(self):
        p=self.root/'Showcase/site.js';p.write_text(p.read_text()+'\n// changed\n')
        with self.assertRaisesRegex(ValueError,'changed after preparation'):flow.check_prepared(self.root,self.checkout)

    def test_snapshot_edit_is_detected(self):
        p=self.checkout/'content/chapters/09.md';p.write_text(p.read_text()+'lost provenance\n')
        with self.assertRaisesRegex(ValueError,'snapshot changed'):flow.check_prepared(self.root,self.checkout)

    def test_build_edit_is_detected(self):
        p=self.checkout/'dist/chapters/09.html';p.write_text(p.read_text()+'truncated replacement\n')
        with self.assertRaisesRegex(ValueError,'Build output changed'):flow.check_prepared(self.root,self.checkout)

    def test_online_old_search_index_is_detected(self):
        prepared=flow.check_prepared(self.root,self.checkout)
        def fetcher(url):
            name=url.removeprefix('https://example.test/')
            return b'[]' if name=='search.json' else (self.checkout/'dist'/name).read_bytes()
        with self.assertRaisesRegex(ValueError,'Published bytes differ: search.json'):
            flow.verify_online(self.checkout,prepared,'https://example.test',fetcher)

    def test_platform_script_is_allowed_but_code_whitespace_is_not(self):
        base=b'<article><pre><code>  a\n b</code></pre></article>'
        platform=base+b'<script>window.platform = true;</script>'
        self.assertEqual(flow.html_signature(base),flow.html_signature(platform))
        self.assertNotEqual(flow.html_signature(base),flow.html_signature(base.replace(b'  a',b'a')))

    def test_retry_preserves_failure_history(self):
        flow.save_release(self.root,{'version_number':1,'status':'deployed_unverified','error':'test-only readback failure'})
        flow.save_release(self.root,{'version_number':1,'status':'verified'})
        latest=flow.read(self.root/'Showcase/latest-release.json')
        self.assertEqual(latest['status'],'verified')
        self.assertTrue(any(x.get('error')=='test-only readback failure' for x in latest['history']))

    def test_failed_readback_cannot_be_recorded_verified(self):
        prepared=flow.check_prepared(self.root,self.checkout);cfg=flow.config(self.root)
        version={'project_id':cfg['project_id'],'id':'test-version','version_number':1,'source':{'commit_sha':'a'*40}}
        deployment={'project_id':cfg['project_id'],'version_id':'test-version','id':'test-deployment','status':'succeeded','url':cfg['url']}
        screenshot=Path(self.temp.name)/'test-only-image';screenshot.write_bytes(b'test fixture')
        review={'output_fingerprint':prepared['output_fingerprint'],'production_url':cfg['url'],'version_id':version['id'],'checks':dict.fromkeys(('desktop','mobile','search','figures','production'),True),'screenshots':[str(screenshot)]}
        paths=[]
        for name,value in [('version',version),('deployment',deployment),('review',review)]:
            path=Path(self.temp.name)/(name+'.json');flow.write(path,value);paths.append(path)
        with patch.object(flow.subprocess,'check_output',side_effect=['a'*40+'\n','']),patch.object(flow,'verify_online',side_effect=ValueError('test-only offline')):
            with self.assertRaisesRegex(ValueError,'offline'):flow.finish(self.root,self.checkout,*paths)
        self.assertEqual(flow.read(self.root/'Showcase/latest-release.json')['status'],'deployed_unverified')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--checkout',type=Path,required=True)
    args,remaining=parser.parse_known_args();PublicationWorkflowTests.site=args.checkout.resolve()
    unittest.main(argv=[sys.argv[0],*remaining])
