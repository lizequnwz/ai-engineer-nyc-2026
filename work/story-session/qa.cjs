/* Content and DOM behavior checks. No browser rendering is claimed. */
const fs = require('node:fs'), path = require('node:path');
const assert = require('node:assert/strict'), crypto = require('node:crypto');
const {JSDOM, VirtualConsole} = require('../qa/node_modules/jsdom');
const root = path.resolve(__dirname, '../..');
const html = fs.readFileSync(path.join(root, 'outputs/ai-engineer-2026-five-stories.html'), 'utf8');
const guideHtml = fs.readFileSync(path.join(root, 'outputs/ai-engineer-2026-five-stories-presenter-guide.html'), 'utf8');
const content = JSON.parse(fs.readFileSync(path.join(__dirname, 'briefing.json')));
const build = JSON.parse(fs.readFileSync(path.join(__dirname, 'validation/build-report.json')));

function setup(hash = '', source = html) {
  const errors = [], virtualConsole = new VirtualConsole();
  virtualConsole.on('jsdomError', error => errors.push(error.message));
  const dom = new JSDOM(source, {url: 'https://offline-briefing.invalid/' + hash,
    runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole,
    beforeParse(w) {
      w.HTMLElement.prototype.scrollIntoView = function () { this.dataset.scrolled = 'true'; };
      w.HTMLDialogElement.prototype.showModal = function () { this.open = true; };
      w.HTMLDialogElement.prototype.close = function () { this.open = false; this.dispatchEvent(new w.Event('close')); };
      w.HTMLElement.prototype.requestFullscreen = async () => { w.__fullscreenCalls = (w.__fullscreenCalls || 0) + 1; };
      w.print = () => {
        w.dispatchEvent(new w.Event('beforeprint'));
        w.__printSnapshot = {
          visibleSlides: [...w.document.querySelectorAll('.slide')].filter(el => !el.hidden).length,
          detailsOpen: [...w.document.querySelectorAll('details')].every(el => el.open)
        };
        w.dispatchEvent(new w.Event('afterprint'));
      };
    }});
  const w = dom.window, d = w.document;
  const $ = selector => d.querySelector(selector), $$ = selector => [...d.querySelectorAll(selector)];
  const click = selector => { const el = $(selector); assert.ok(el, selector); el.focus(); el.click(); };
  const key = (value, target = d.body, extra = {}) => target.dispatchEvent(new w.KeyboardEvent('keydown', {key: value, bubbles: true, cancelable: true, ...extra}));
  const active = () => $$('.slide').filter(slide => !slide.hidden);
  return {dom, w, d, $, $$, click, key, active, errors};
}

function contrast(a, b) {
  const luminance = hex => hex.slice(1).match(/../g).map(v => parseInt(v,16) / 255)
    .map(v => v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4)
    .reduce((sum, v, i) => sum + v * [.2126,.7152,.0722][i], 0);
  const x = luminance(a), y = luminance(b);
  return (Math.max(x,y) + .05) / (Math.min(x,y) + .05);
}

(async () => {
  const checks = [], t = setup();
  const {w,d,$,$$,click,key,active} = t;
  assert.deepEqual(t.errors, []);
  assert.equal(build.slides, 22);
  assert.equal(build.presentationMinutes + build.discussionMinutes, 45);
  assert.equal(active().length, 1);
  assert.equal(active()[0].dataset.slide, 'executive-summary');
  assert.equal(w.location.hash, '#present/executive-summary');
  assert.equal($('#previous').disabled, true);
  assert.equal($$('[data-reveal],.unrevealed,[inert],.opening-number,.ink').length, 0);
  assert.doesNotMatch(html, /Reveal next|staged reveal|What does 17 mean|opening-number/);
  assert.doesNotMatch(fs.readFileSync(path.join(__dirname,'deck.js'),'utf8'), /maxStep|data-reveal|\bstep\s*=/);
  checks.push('The 22-slide, 35+10 minute briefing opens on an executive summary; every main-slide element is visible and the reveal mechanism is removed');

  key('ArrowRight');
  assert.equal(active()[0].dataset.slide, 'three-failures');
  assert.equal(d.activeElement.id, 'title-three-failures');
  key('ArrowLeft');
  assert.equal(active()[0].dataset.slide, 'executive-summary');
  click('#next');
  key('ArrowRight', $('#next'));
  assert.equal(active()[0].dataset.slide, 'fact-address');
  const before = w.location.hash;
  key(' ', $('#next'));
  key('ArrowRight',d.body,{ctrlKey:true});
  key('ArrowRight',d.body,{metaKey:true});
  key('ArrowRight',active()[0].querySelector('.table-wrap'));
  assert.equal(w.location.hash,before);
  checks.push('Buttons and keys advance directly between slides; modifier shortcuts, focused control activation, and table scrolling retain their own keyboard behavior');

  click('#outline-toggle');
  assert.equal($('#outline-dialog').open,true);
  key('ArrowRight');
  assert.equal(w.location.hash,before);
  click('[data-slide-jump="one-row"]');
  assert.equal($('#outline-dialog').open,false);
  assert.equal(active()[0].dataset.slide,'one-row');
  assert.equal(d.activeElement.id,'title-one-row');
  assert.match(active()[0].querySelector('.face').textContent,/Row-count validation cannot detect entity and aggregation errors/);
  assert.match(active()[0].querySelector('.analysis').textContent,/−\$200,000/);
  assert.match(active()[0].querySelector('.analysis').textContent,/Entity and grain/);
  click('[data-show-source="one-row"]');
  assert.equal($('#source-dialog').open,true);
  assert.match($('#source-body').textContent,/synthetic|Synthetic/);
  assert.match($('#source-body').textContent,/-200000/);
  assert.match($('#source-body').textContent,/denominator/);
  assert.ok($('#source-body a').href.includes('dZgA6btnb_s&t=511s'));
  click('#source-dialog [data-close-dialog]');
  assert.equal(d.activeElement.dataset.showSource,'one-row');
  checks.push('Contents and detail dialogs restore meaningful focus; the SQL example displays scope/value checks and resolves to the correct source and technical illustration');

  click('[data-mode-switch="read"]');
  assert.equal(active().length,22);
  assert.equal(d.body.dataset.mode,'read');
  assert.equal($$('[inert],[data-reveal]').length,0);
  click('[data-mode-switch="present"]');
  assert.equal(active().length,1);
  assert.equal(active()[0].dataset.slide,'one-row');
  click('[data-chapter-jump="arize"]');
  assert.equal(active()[0].dataset.slide,'next-failure');
  assert.equal($('[data-chapter-jump="arize"]').getAttribute('aria-current'),'step');
  key('Home');
  for(const slide of $$('.slide')) {
    assert.equal(active()[0].dataset.slide,slide.dataset.slide);
    assert.equal(slide.querySelectorAll('.slide-title,.slide-lead,.analysis,.application-line').length,4);
    key('ArrowRight');
  }
  assert.equal(active()[0].dataset.slide,'reflection');
  assert.equal($('#next').disabled,true);
  key('Home'); assert.equal($('#previous').disabled,true);
  key('End'); assert.equal(active()[0].dataset.slide,'reflection');
  checks.push('Both modes, chapter navigation, every slide transition, and Home/End preserve the fully visible analytical content and correct boundary state');

  click('[data-chapter-jump="vault"]');
  const printHash=w.location.hash;
  click('#print-deck');
  assert.equal(w.__printSnapshot.visibleSlides,22);
  assert.equal(active().length,1);
  assert.equal(w.location.hash,printHash);
  click('#fullscreen-toggle'); await Promise.resolve();
  assert.equal(w.__fullscreenCalls,1);
  const reject=setup();
  reject.w.HTMLElement.prototype.requestFullscreen=async()=>{throw new Error('Unavailable')};
  reject.click('#fullscreen-toggle');
  await new Promise(resolve=>setTimeout(resolve,20));
  assert.match(reject.$('#fullscreen-message').textContent,/browser/);
  checks.push('Deck printing exposes all slides then restores the current slide; fullscreen uses the browser API and handles an unavailable command');

  const deep=setup('#present/grader');
  assert.equal(deep.active()[0].dataset.slide,'grader');
  deep.w.location.hash='#read/client-concern';
  await new Promise(resolve=>setTimeout(resolve,20));
  assert.equal(deep.active().length,22);
  assert.equal(deep.d.activeElement.id,'title-client-concern');
  const invalid=setup('#present/no-such-slide');
  assert.equal(invalid.w.location.hash,'#present/executive-summary');
  checks.push('Slide and reading deep links work; later hash changes focus the selected slide and invalid destinations normalize safely');

  const staticDom=new JSDOM(html),sd=staticDom.window.document;
  assert.equal(sd.body.dataset.mode,'read');
  assert.equal(sd.querySelectorAll('.slide').length,22);
  assert.equal(sd.querySelectorAll('.reading-material').length,22);
  assert.equal(sd.querySelectorAll('.slide[hidden]').length,0);
  const ids=[...sd.querySelectorAll('[id]')].map(el=>el.id);
  assert.equal(new Set(ids).size,ids.length);
  assert.equal(sd.querySelectorAll('h1').length,1);
  assert.equal(sd.querySelectorAll('script[src],link[rel="stylesheet"],img[src],iframe').length,0);
  assert.doesNotMatch(html,/@import|fetch\(|XMLHttpRequest|localStorage|sessionStorage|https?:\/\/fonts\./);
  for(const control of sd.querySelectorAll('button,a,summary')) assert.ok(control.textContent.trim()||control.getAttribute('aria-label'));
  for(const table of sd.querySelectorAll('table')) {
    const columns=table.querySelectorAll('thead th').length;
    assert.ok(columns>=2);
    for(const row of table.querySelectorAll('tbody tr')) assert.equal(row.children.length,columns);
    assert.ok([...table.querySelectorAll('thead th')].every(th=>th.scope==='col'));
    assert.ok([...table.querySelectorAll('tbody th')].every(th=>th.scope==='row'));
  }
  const faceWords=[...sd.querySelectorAll('.slide')].map(s=>({id:s.dataset.slide,words:s.querySelector('.face').textContent.trim().split(/\s+/).length}));
  assert.ok(faceWords.every(s=>s.words>=135&&s.words<=260),JSON.stringify(faceWords));
  assert.ok([...sd.querySelectorAll('.slide-title')].every(el=>!el.textContent.includes('?')));
  checks.push('Every slide has a conclusion, substantial visible analysis, and an engineering implication; tables have consistent cells and scoped headers; no-JavaScript reading and offline runtime independence remain complete');

  const guide=setup('',guideHtml),gd=guide.d;
  assert.equal(gd.querySelectorAll('.delivery-focus').length,22);
  assert.equal(gd.querySelectorAll('.guide-slide-top').length,22);
  assert.match(gd.querySelector('.run-of-show').textContent,/35:00–45:00/);
  assert.match(gd.querySelector('#discussion').textContent,/No roadmap/);
  assert.doesNotMatch(gd.body.textContent,/staged reveal|Reveal next|What does 17 mean/);
  guide.click('#print-guide');
  assert.equal(guide.w.__printSnapshot.detailsOpen,true);
  assert.ok([...gd.querySelectorAll('details')].every(el=>!el.open));
  for(const link of [...sd.querySelectorAll('a[href]'),...gd.querySelectorAll('a[href]')]) {
    const href=link.getAttribute('href');
    if(href.startsWith('https:'))continue;
    if(href.startsWith('#present/'))assert.ok(sd.getElementById('slide-'+href.split('/')[1]));
    else if(href.startsWith('#'))assert.ok(link.ownerDocument.getElementById(href.slice(1)),href);
    else assert.ok(fs.existsSync(path.join(root,'outputs',href.split('#')[0])),href);
  }
  checks.push('The updated guide matches all 22 slides, preserves 35+10 timing and reflection, opens and restores print details, and uses valid local links');

  const sources=JSON.parse(fs.readFileSync(path.join(__dirname,'research/sources.json'))).sources;
  const briefs=JSON.parse(fs.readFileSync(path.join(__dirname,'research/briefs.json')));
  assert.equal(sources.length,5);
  for(const source of sources){
    const bytes=fs.readFileSync(path.join(__dirname,'research',source.transcript));
    assert.equal(crypto.createHash('sha256').update(bytes).digest('hex'),source.sha256);
    assert.ok(bytes.toString().includes('Video ID: '+source.videoId));
    assert.ok(bytes.toString().includes('Captions: auto-generated'));
    assert.ok(briefs[source.id].limits.length>200);
  }
  for(const slide of content.slides){
    assert.ok(!('steps' in slide)&&!('theme'in slide)&&!('cue'in slide));
    assert.ok(slide.focus&&slide.application&&slide.lead);
    if(slide.source) assert.ok(sources.find(s=>s.id===slide.source).timestamps.includes(slide.timestamp));
  }
  assert.equal(sd.querySelectorAll('.case-context').length,5);
  assert.equal(sd.querySelectorAll('.source-context').length,content.slides.filter(s=>s.source).length);
  for(const source of sources){
    const context=briefs[source.id].context;
    assert.ok(context.label&&context.name&&context.description);
    const first=content.slides.find(s=>s.source===source.id);
    assert.ok(sd.querySelector('#slide-'+first.id+' .case-context'));
    for(const slide of content.slides.filter(s=>s.source===source.id)){
      const footer=sd.querySelector('#slide-'+slide.id+' .slide-credit');
      assert.equal(footer.querySelector('.source-talk').textContent,source.title);
      assert.ok(footer.querySelector('.source-byline').textContent.includes(source.speaker));
      assert.ok(footer.querySelector('.source-context').textContent.includes(context.name));
      assert.ok(footer.querySelector('.source-context').textContent.includes(context.description));
    }
  }
  assert.match(sd.querySelector('#slide-quality-spectrum .source-context').textContent,/Engineering perspective/);
  checks.push('Five case openers introduce the application or engineering perspective; every case footer retains the talk title, presenter, and accurate product/workflow context');
  assert.equal(800000-1000000,-200000);
  assert.match(sd.querySelector('#slide-two-readers').textContent,/precision@10/);
  assert.match(sd.querySelector('#slide-two-readers').textContent,/not answer accuracy/);
  assert.match(sd.querySelector('#slide-parked-idea').textContent,/P&L impact is still to come/);
  assert.match(sd.querySelector('#slide-compare-work').textContent,/Randomized assignment/);
  assert.match(sd.querySelector('#slide-quality-spectrum').textContent,/Replacement cost/);
  checks.push('All five original caption checksums and registered timestamps remain valid; retrieval/ROI limits, four quality factors, and fictional calculation scope are preserved');

  const pairs=[['#17324d','#ffffff'],['#243747','#ffffff'],['#4d5f71','#ffffff'],['#19675c','#ffffff'],['#17324d','#edf1f5'],['#17324d','#f7f9fa'],['#243747','#edf4f2'],['#19675c','#edf4f2'],['#4d5f71','#f3f6f8']];
  const contrasts=pairs.map(([foreground,background])=>({foreground,background,ratio:+contrast(foreground,background).toFixed(2)}));
  assert.ok(contrasts.every(pair=>pair.ratio>=4.5),JSON.stringify(contrasts));
  checks.push('All nine tested text/surface pairs meet 4.5:1 contrast in the restrained white, navy, and teal design');
  assert.deepEqual(t.errors,[]);assert.deepEqual(guide.errors,[]);
  for(const dom of [t.dom,reject.dom,deep.dom,invalid.dom,staticDom,guide.dom])dom.window.close();
  const limitations='Content, DOM interaction, source-provenance, and static CSS/contrast checks. The earlier browser URL-policy rejection prohibits a local-file preview workaround. Actual rendered geometry, projection readability, and print pagination remain unverified.';
  const report={passed:true,designRevision:'engineering-readout',checks,slides:22,scriptWords:build.scriptWords,faceWords,contrasts,limitations};
  fs.writeFileSync(path.join(__dirname,'validation/qa-report.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({passed:true,checks,visibleWords:{min:Math.min(...faceWords.map(s=>s.words)),max:Math.max(...faceWords.map(s=>s.words))},minContrast:Math.min(...contrasts.map(c=>c.ratio)),limitations},null,2));
})().catch(error=>{console.error(error);process.exitCode=1});
