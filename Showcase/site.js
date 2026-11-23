(() => {
  'use strict';
  const searchDialog = document.getElementById('search-dialog');
  const navDialog = document.getElementById('nav-dialog');
  const input = document.getElementById('book-search');
  const status = document.getElementById('search-status');
  const results = document.getElementById('search-results');
  const language = document.documentElement.lang;
  const english = language === 'en';
  const idleText = status.textContent;
  const searchingText = english ? 'Searching…' : '正在检索全书…';
  const normalize = text => text.normalize('NFKC').toLocaleLowerCase();
  const chapterPath = path => path.replace(/\.html$/, '').replace(/\/index$/, '/');
  let indexPromise, searchIndex, sequence = 0, timer;
  const loadIndex = () => {
    if (!indexPromise) indexPromise = fetch('/search.json').then(response => {
      if (!response.ok) throw new Error('Search index unavailable');
      return response.json();
    }).then(rows => (searchIndex = rows.map(row => ({...row, normalized: normalize(row.text)})))).catch(error => {indexPromise = null; throw error;});
    return indexPromise;
  };
  function openSearch() {
    if (navDialog.open) navDialog.close();
    if (!searchDialog.open) searchDialog.showModal();
    input.focus();
    loadIndex().catch(() => {});
    if (!input.value) {try {input.value=sessionStorage.getItem('beyond-code-query')||'';} catch {} if(input.value)search();}
  }
  document.querySelectorAll('[data-open-search]').forEach(button => button.addEventListener('click', openSearch));
  document.querySelector('[data-open-nav]').addEventListener('click', () => navDialog.showModal());
  document.querySelectorAll('[data-close-dialog]').forEach(button => button.addEventListener('click', () => button.closest('dialog').close()));
  document.querySelectorAll('dialog').forEach(dialog => dialog.addEventListener('click', event => {if (event.target === dialog) {const bounds=dialog.getBoundingClientRect(); if(event.clientX<bounds.left||event.clientX>bounds.right||event.clientY<bounds.top||event.clientY>bounds.bottom)dialog.close();}}));
  document.addEventListener('keydown', event => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {event.preventDefault();openSearch();}
  });
  searchDialog.querySelector('form').addEventListener('submit', event => event.preventDefault());
  function foldedOffsets(text) {
    let folded='', offset=0;const starts=[],ends=[];
    for(const char of text){const part=normalize(char);for(let i=0;i<part.length;i++){starts.push(offset);ends.push(offset+char.length);}folded+=part;offset+=char.length;}
    return {text:folded,starts,ends};
  }
  function snippet(text, terms) {
    const folded=foldedOffsets(text), lower=folded.text;
    const positions = terms.map(t => lower.indexOf(t)).filter(p => p >= 0);
    const start = Math.max(0, (positions.length ? folded.starts[Math.min(...positions)] : 0) - 55);
    return (start ? '…' : '') + text.slice(start, start + 210) + (text.length > start + 210 ? '…' : '');
  }
  function highlighted(text, terms) {
    const fragment = document.createDocumentFragment();
    const folded=foldedOffsets(text), lower=folded.text;
    let cursor = 0, originalCursor=0;
    while (cursor < lower.length) {
      const matches = terms.map(term => ({term, position: lower.indexOf(term, cursor)})).filter(m => m.position >= 0).sort((a,b) => a.position-b.position || b.term.length-a.term.length);
      if (!matches.length) {fragment.append(document.createTextNode(text.slice(originalCursor)));break;}
      const {term, position} = matches[0];
      const start=folded.starts[position], end=folded.ends[position+term.length-1];
      fragment.append(document.createTextNode(text.slice(originalCursor, start)));
      const mark = document.createElement('mark');mark.textContent = text.slice(start,end);fragment.append(mark);cursor=position+term.length;originalCursor=end;
    }
    return fragment;
  }
  async function search() {
    const request = ++sequence;
    const query = input.value.trim();
    results.replaceChildren();
    if (!query) {status.textContent=idleText;return;}
    status.textContent=searchingText;
    try {
      const rows = searchIndex || await loadIndex();
      if (request !== sequence) return;
      const terms = normalize(query).split(/\s+/).filter(Boolean);
      const matches = rows.filter(row => terms.every(term => row.normalized.includes(term))).map(row => ({...row,score:(row.text===row.section?3:0)+(row.normalized===normalize(query)?5:0)})).sort((a,b) => b.score-a.score || Number(b.language===language)-Number(a.language===language) || a.chapter-b.chapter);
      if (english) {
        status.textContent = matches.length
          ? `“${query}” · ${matches.length} results${matches.length>60?' (showing the first 60)':''}`
          : `No matches for “${query}”. Try a shorter search.`;
      } else {
        status.textContent = matches.length ? `“${query}”：找到 ${matches.length} 处相关内容${matches.length>60?'，显示前60处；可增加关键词缩小范围。':'。'}` : `“${query}”：没有找到匹配内容。试试更短的关键词或不同表述。`;
      }
      for (const row of matches.slice(0,60)) {
        const li=document.createElement('li'), a=document.createElement('a'), chapter=document.createElement('span'), title=document.createElement('strong'), excerpt=document.createElement('p');
        a.href=row.url;
        a.lang=row.language;
        chapter.className='result-chapter';
        chapter.textContent=row.language==='en' ? `Chapter ${row.chapter} · ${row.title} (English)` : `第${row.chapter}章 · ${row.title}`;
        title.append(highlighted(row.section,terms));excerpt.append(highlighted(snippet(row.text,terms),terms));
        a.append(chapter,title,excerpt);li.append(a);results.append(li);
        a.addEventListener('click',()=>{
          const landing={url:row.url,query};
          try {sessionStorage.setItem('beyond-code-landing',JSON.stringify(landing));sessionStorage.setItem('beyond-code-query',query);} catch {}
          searchDialog.close();
          if(chapterPath(new URL(row.url,location.href).pathname)===chapterPath(location.pathname))requestAnimationFrame(()=>revealSearchMatch(landing));
        });
      }
    } catch {
      if (request===sequence)status.textContent=english ? 'Search is unavailable. Try again in a moment.' : '搜索暂时不可用，请稍后重试；章节目录仍可正常阅读。';
    }
  }
  input.addEventListener('input', () => {sequence++;clearTimeout(timer);results.replaceChildren();status.textContent=input.value.trim()?searchingText:idleText;timer=setTimeout(search,100);});
  document.getElementById('clear-search').addEventListener('click', () => {input.value='';clearTimeout(timer);try{sessionStorage.removeItem('beyond-code-query');sessionStorage.removeItem('beyond-code-landing');}catch{}clearSearchMarks();search();input.focus();});
  function clearSearchMarks() {
    document.querySelectorAll('#chapter-body mark.search-match').forEach(mark=>{const parent=mark.parentNode;mark.replaceWith(document.createTextNode(mark.textContent));parent.normalize();});
  }
  function revealSearchMatch(landing) {
    if(!landing)try{landing=JSON.parse(sessionStorage.getItem('beyond-code-landing'));}catch{}
    if(!landing)return;
    const destination=new URL(landing.url,location.href);
    if(chapterPath(destination.pathname)!==chapterPath(location.pathname)||destination.hash!==location.hash)return;
    const target=document.getElementById(location.hash.slice(1));
    if(!target)return;
    clearSearchMarks();
    const terms=normalize(landing.query).trim().split(/\s+/).filter(Boolean);
    const walker=document.createTreeWalker(target,NodeFilter.SHOW_TEXT), nodes=[];
    while(walker.nextNode())if(!walker.currentNode.parentElement.closest('[data-reading-control]'))nodes.push(walker.currentNode);
    for(const node of nodes)if(terms.some(term=>normalize(node.textContent).includes(term))){
      const fragment=highlighted(node.textContent,terms);fragment.querySelectorAll('mark').forEach(mark=>mark.classList.add('search-match'));node.replaceWith(fragment);
    }
    const hit=target.querySelector('mark.search-match');
    if(hit)requestAnimationFrame(()=>hit.scrollIntoView({block:'center',inline:'center'}));
  }
  window.addEventListener('hashchange',()=>{navDialog.close();revealSearchMatch();});
  revealSearchMatch();
  // Search terms stay in this browser tab; they are not added to page URLs.
  const figureDialog=document.getElementById('figure-dialog'), figureViewport=figureDialog.querySelector('.figure-viewport'), figureImage=figureViewport.querySelector('img');
  let figureWidth=1, figureScale=1;
  function resizeFigure(scale,center=true) {
    const old=figureScale, x=figureViewport.scrollLeft+figureViewport.clientWidth/2, y=figureViewport.scrollTop+figureViewport.clientHeight/2;
    figureScale=Math.max(.15,Math.min(3,scale));figureImage.style.width=`${figureWidth*figureScale}px`;
    const hint=english?'Scroll to explore the figure':'可横向、纵向滑动查看';
    document.getElementById('figure-status').textContent=`${Math.round(figureScale*100)}% · ${hint}`;
    if(center){figureViewport.scrollLeft=x*figureScale/old-figureViewport.clientWidth/2;figureViewport.scrollTop=y*figureScale/old-figureViewport.clientHeight/2;}
  }
  document.querySelectorAll('[data-zoom]').forEach(link=>link.addEventListener('click',event=>{
    if(event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;
    event.preventDefault();
    const original=link.closest('.mechanism,.gallery-figure').querySelector('img');
    figureWidth=Number(original.getAttribute('width'));figureImage.src=original.src;figureImage.alt=original.alt;
    figureImage.width=figureWidth;figureImage.height=Number(original.getAttribute('height'));
    document.getElementById('figure-dialog-title').textContent=original.alt;
    figureDialog.showModal();resizeFigure(1,false);figureViewport.scrollLeft=Math.max(0,(figureWidth-figureViewport.clientWidth)/2);figureViewport.scrollTop=0;
  }));
  figureDialog.querySelector('[data-zoom-out]').addEventListener('click',()=>resizeFigure(figureScale-.2));
  figureDialog.querySelector('[data-zoom-in]').addEventListener('click',()=>resizeFigure(figureScale+.2));
  figureDialog.querySelector('[data-zoom-fit]').addEventListener('click',()=>resizeFigure(figureViewport.clientWidth/figureWidth));
  figureDialog.querySelector('[data-zoom-reset]').addEventListener('click',()=>resizeFigure(1));
  function updateOverflowHints() {
    document.querySelectorAll('.overflow-hint').forEach(hint=>{const content=hint.nextElementSibling;hint.hidden=content.scrollWidth<=content.clientWidth+1;});
  }
  updateOverflowHints();window.addEventListener('resize',updateOverflowHints);
  const themeButton = document.querySelector('[data-theme]');
  function setTheme(theme) {
    document.documentElement.dataset.theme=theme;
    const dark=theme==='dark';
    themeButton.textContent=english?(dark?'Light':'Dark'):(dark?'浅色':'深色');
    themeButton.setAttribute('aria-label',english?(dark?'Switch to light theme':'Switch to dark theme'):(dark?'切换浅色主题':'切换深色主题'));
  }
  try {setTheme(localStorage.getItem('beyond-code-theme')==='dark'?'dark':'light');} catch {setTheme('light');}
  themeButton.addEventListener('click',()=>{const next=document.documentElement.dataset.theme==='dark'?'light':'dark';setTheme(next);try{localStorage.setItem('beyond-code-theme',next);}catch{}});
  // Keep old Showcase bookmarks useful while the visible navigation uses the current book.
  const legacy = {'导言':'/chapters/01.html','核心原则':'/chapters/03.html','成熟度模型':'/chapters/22.html','双层架构':'/chapters/03.html','上下文工程':'/chapters/05.html','Agent 拓扑':'/chapters/17.html','工具与权限':'/chapters/13.html','从意图到变更':'/chapters/07.html','Evidence-Driven DoD':'/chapters/09.html','质量门禁':'/chapters/10.html','失败恢复':'/chapters/08.html','记忆与知识':'/chapters/15.html','自我演进':'/chapters/16.html','治理预算':'/chapters/21.html','组织落地':'/chapters/22.html','principles':'/chapters/03.html','architecture':'/chapters/03.html','workflow':'/chapters/07.html','governance':'/chapters/21.html','start':'/chapters/01.html'};
  if (location.pathname==='/' || location.pathname==='/index.html') {let key='';try{key=decodeURIComponent(location.hash.slice(1));}catch{}if(legacy[key])location.replace(legacy[key]);}
})();
