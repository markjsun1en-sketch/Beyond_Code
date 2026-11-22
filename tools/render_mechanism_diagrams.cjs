// Render chapter-owned Mermaid sources; generated images are not editable masters.
// Usage: node tools/render_mechanism_diagrams.cjs --mermaid-js PATH
//   Optional: --figures fig-16-1,fig-23-2 selects only named figures.
//   --preview-only all refreshes preview HTML from existing manifests without rendering images.
//   --playwright-module PATH --browser-path PATH [--batch phase-a|phase-b|phase-c|phase-d|phase-e] chapter.md [chapter.md ...]
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const args = process.argv.slice(2);
const options = {};
const chapters = [];
for (let i = 0; i < args.length; i++) {
  if (args[i].startsWith('--')) options[args[i].slice(2)] = args[++i];
  else chapters.push(path.resolve(args[i]));
}
const batch = options.batch || 'phase-a';
if (!['phase-a', 'phase-b', 'phase-c', 'phase-d', 'phase-e'].includes(batch)) throw new Error('Unknown --batch');
const root = path.resolve(__dirname, '..');
const output = path.join(root, 'OptimizedDocs', 'diagrams');
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');
const escapeHtml = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');

function writePreview(records, previewBatch) {
  const phaseLabel = `阶段 ${previewBatch.slice(-1).toUpperCase()}`;
  const cards = records.map(r => `<article><h2>图${escapeHtml(r.number)} ${escapeHtml(r.title)}</h2><div class="view-controls" role="group" aria-label="图${escapeHtml(r.number)}显示比例"><button type="button" data-view="fit" aria-pressed="true">适合窗口</button><button type="button" data-view="actual" aria-pressed="false">原尺寸</button><a href="${r.id}.svg" target="_blank" rel="noopener">打开SVG查看细节</a></div><div class="figure"><img src="${r.id}.svg" alt="${escapeHtml(r.title)}"></div><p>${escapeHtml(r.caption).replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')}</p><a href="../${encodeURIComponent(path.basename(r.chapter))}">返回所属章节</a></article>`).join('\n');
  fs.writeFileSync(path.join(output, `${previewBatch}-preview.html`), `<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>机制简图预览 · ${phaseLabel}</title><style>body{margin:0;background:#f2f4f6;color:#17212b;font:16px/1.8 "PingFang SC",sans-serif}main{max-width:1160px;margin:auto;padding:32px 24px}h1{font-size:26px}h2{font-size:21px}article{background:white;padding:24px;margin:24px 0;border:1px solid #d4dce3;border-radius:8px}.view-controls{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:12px 0}button{font:inherit;padding:3px 12px;border:1px solid #617587;border-radius:4px;background:white;color:#17212b;cursor:pointer}button[aria-pressed="true"]{background:#e2eaf0;font-weight:600}button:focus-visible,a:focus-visible{outline:3px solid #24577b;outline-offset:3px}.figure{overflow:auto;max-height:80vh;text-align:center;border:1px solid #edf0f3;padding:8px}.figure img{display:block;margin:auto;width:auto;height:auto;max-width:100%;max-height:76vh}.figure.actual img{max-width:none;max-height:none}p{color:#475569}a{color:#24577b}</style><main><h1>${phaseLabel} 机制简图</h1><p>默认先看完整关系；切换原尺寸可滚动阅读，或打开SVG放大细节。教学示意、案例机制与历史关系分别说明，图形不替代正文和原始证据。Mermaid源保存在所属章节，本页由脚本生成。</p>${cards}</main><script>document.querySelectorAll('[data-view]').forEach(button=>button.addEventListener('click',()=>{const article=button.closest('article');article.querySelector('.figure').classList.toggle('actual',button.dataset.view==='actual');article.querySelectorAll('[data-view]').forEach(peer=>peer.setAttribute('aria-pressed',String(peer===button)));}));</script></html>`);
}

(async () => {
  if (options['preview-only']) {
    const batches = options['preview-only'] === 'all' ? ['phase-a', 'phase-b', 'phase-c', 'phase-d', 'phase-e'] : [batch];
    for (const name of batches) {
      const manifest = JSON.parse(fs.readFileSync(path.join(output, `${name}-manifest.json`), 'utf8'));
      writePreview(manifest.figures, name);
    }
    console.log(JSON.stringify({ refreshed_previews: batches }));
    return;
  }
  for (const key of ['mermaid-js', 'playwright-module', 'browser-path']) {
    if (!options[key]) throw new Error(`Missing --${key}`);
  }
  if (!chapters.length) throw new Error('Provide chapter Markdown files');
  const { chromium } = require(path.resolve(options['playwright-module']));
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({ executablePath: options['browser-path'], headless: true });
  let records = [];
  const seen = new Set();
  try {
    const page = await browser.newPage({ viewport: { width: 1440, height: 1100 }, deviceScaleFactor: 1.5 });
    await page.setContent('<!doctype html><meta charset="utf-8"><style>body{margin:0;background:white;font-family:"PingFang SC","Microsoft YaHei",sans-serif}#figure{display:inline-block;padding:24px}#figure svg{display:block;max-width:none!important}</style><div id="figure"></div>');
    await page.addScriptTag({ path: options['mermaid-js'] });
    await page.evaluate(() => mermaid.initialize({
      startOnLoad: false, securityLevel: 'strict', theme: 'base',
      fontFamily: 'PingFang SC, Microsoft YaHei, sans-serif',
      themeVariables: { primaryColor: '#f4f6f8', primaryTextColor: '#17212b', primaryBorderColor: '#617587', lineColor: '#475569', secondaryColor: '#ffffff', tertiaryColor: '#f8fafc', clusterBkg: '#fafbfd', clusterBorder: '#94a3b8', edgeLabelBackground: '#ffffff', fontSize: '18px' },
      flowchart: { htmlLabels: false, curve: 'linear', nodeSpacing: 30, rankSpacing: 42, padding: 16, useMaxWidth: false }
    }));
    for (const file of chapters) {
      const markdown = fs.readFileSync(file, 'utf8');
      for (const match of markdown.matchAll(/```mermaid\r?\n([\s\S]*?)\r?\n```/g)) {
        const headings = [...markdown.slice(0, match.index).matchAll(/^## 图(\d+-\d+) (.+)$/gm)];
        if (!headings.length) throw new Error(`Diagram lacks a figure heading: ${file}`);
        const [, number, title] = headings.at(-1);
        const id = `fig-${number}`;
        if (options.figures && !options.figures.split(',').includes(id)) continue;
        if (seen.has(id)) throw new Error(`Duplicate figure: ${id}`);
        seen.add(id);
        const source = match[1];
        const svg = await page.evaluate(async ({ id, source }) => {
          const result = await mermaid.render(id, source);
          document.getElementById('figure').innerHTML = result.svg;
          await document.fonts.ready;
          // Mermaid can emit HTML void tags in foreignObject labels. Embedded
          // HTML accepts these, but standalone SVG requires well-formed XML.
          const parser = new DOMParser();
          if (!parser.parseFromString(result.svg, 'image/svg+xml').querySelector('parsererror')) return result.svg;
          const normalized = new XMLSerializer().serializeToString(document.querySelector('#figure svg'));
          if (parser.parseFromString(normalized, 'image/svg+xml').querySelector('parsererror')) throw new Error(`Invalid SVG export: ${id}`);
          return normalized;
        }, { id, source });
        const svgPath = path.join(output, `${id}.svg`);
        const pngPath = path.join(output, `${id}.png`);
        fs.writeFileSync(svgPath, svg);
        await page.locator('#figure').screenshot({ path: pngPath });
        const bounds = await page.locator('#figure svg').boundingBox();
        if (!bounds || bounds.width < 50 || bounds.height < 50) throw new Error(`Empty render: ${id}`);
        const after = markdown.slice(match.index + match[0].length).trimStart();
        const caption = after.split(/\n\s*\n/)[0].replace(/^\*|\*$/g, '');
        records.push({ id, number, title, chapter: path.relative(root, file), source_sha256: sha256(source), svg_sha256: sha256(svg), png_sha256: sha256(fs.readFileSync(pngPath)), width: bounds.width, height: bounds.height, caption });
      }
    }
  } finally {
    await browser.close();
  }
  const manifestPath = path.join(output, `${batch}-manifest.json`);
  if (options.figures) {
    for (const id of options.figures.split(',')) if (!seen.has(id)) throw new Error(`Selected figure not found: ${id}`);
    if (fs.existsSync(manifestPath)) {
      const existing = JSON.parse(fs.readFileSync(manifestPath, 'utf8')).figures;
      const replacements = new Map(records.map(record => [record.id, record]));
      records = existing.map(record => replacements.get(record.id) || record).concat(records.filter(record => !existing.some(old => old.id === record.id)));
    }
  }
  const manifest = { renderer: 'Mermaid 11.12.1; Playwright with local Chrome', mermaid_js_sha256: sha256(fs.readFileSync(options['mermaid-js'])), source_policy: 'Edit Mermaid in the owning chapter, then regenerate. No manual edits to derived files.', figures: records };
  fs.writeFileSync(path.join(output, `${batch}-manifest.json`), JSON.stringify(manifest, null, 2) + '\n');
  writePreview(records, batch);
  console.log(JSON.stringify({ output, figures: records.map(({ id, width, height }) => ({ id, width, height })) }, null, 2));
})().catch(error => { console.error(error); process.exitCode = 1; });
