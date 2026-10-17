(() => {
  'use strict';
  const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
  const data=JSON.parse($('#deck-data').textContent), units=$$('.slide-unit');
  const coreCount=data.slides.filter(s=>s.core).length;
  let state={mode:'present',index:0,notes:false}, restoreFocus=null, toastTimer;
  const findIndex=id=>data.slides.findIndex(s=>s.id===id);
  const announce=message=>{$('#live-status').textContent=message;};
  const toast=message=>{$('#toast').textContent=message;$('#toast').hidden=false;clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('#toast').hidden=true,4000);};
  function setURL(push){const hash='#'+state.mode+'/'+data.slides[state.index].id;if(location.hash!==hash){history[push?'pushState':'replaceState'](null,'',hash);}}
  function update({scroll=false,focus=false,push=false}={}) {
    const s=data.slides[state.index];document.body.dataset.mode=state.mode;
    units.forEach((unit,i)=>{unit.hidden=state.mode==='present'&&i!==state.index;});
    $$('.mode-button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.mode===state.mode)));
    $('#prev').disabled=state.index===0;$('#next').disabled=state.index===data.slides.length-1;
    $('#next').textContent=state.index===coreCount-1?'Appendix →':'Next →';
    const count=s.core?`${state.index+1} / ${coreCount} · CORE`:`A${state.index-coreCount+1} / ${data.slides.length-coreCount} · APPENDIX`;
    $('#progress-status').textContent=state.mode==='present'?count:`Reading mode · ${coreCount} core slides + ${data.slides.length-coreCount} appendix pages`;
    $('#progress-fill').style.width=`${((Math.min(state.index+1,coreCount)/coreCount)*100).toFixed(1)}%`;
    $('#time-status').textContent=s.core?(s.minutes===0?'Discussion':`${s.minutes.toFixed(2).replace(/0+$/,'').replace(/\.$/,'')} min · ${s.cumulative.toFixed(1)} min elapsed target`):'Reference material';
    $('#speaker-toggle').setAttribute('aria-expanded',String(state.notes));
    $('#speaker-panel').hidden=!(state.notes&&state.mode==='present');
    $('#speaker-title').textContent='Speaker notes · '+s.title;
    $('#speaker-content').replaceChildren();
    s.speakerNotes.forEach(t=>{const p=document.createElement('p');p.textContent=t;$('#speaker-content').append(p);});
    $$('#outline-list a').forEach(a=>{a.setAttribute('aria-current',String(a.dataset.slide===s.id));a.href='#'+state.mode+'/'+a.dataset.slide;});
    setURL(push);
    if(scroll)units[state.index].scrollIntoView({block:'start',behavior:'auto'});
    if(focus){const h=units[state.index].querySelector('.slide-title');h.focus({preventScroll:true});}
    announce(`${state.mode==='present'?'Slide':'Reading'} ${count}: ${s.title}`);
  }
  function navigate(index,{focus=false,push=true}={}){state.index=Math.max(0,Math.min(data.slides.length-1,index));update({scroll:true,focus,push});}
  function setMode(mode){if(mode===state.mode)return;state.mode=mode;update({scroll:true,focus:true,push:true});}
  function fromURL(){const match=location.hash.match(/^#(present|read)\/(.+)$/);if(match){const i=findIndex(match[2]);if(i>=0){state.mode=match[1];state.index=i;}}update({scroll:state.mode==='read'});}
  function openDialog(dialog){restoreFocus=document.activeElement;dialog.showModal();dialog.querySelector('button').focus();}
  function closeDialog(dialog){dialog.close();if(restoreFocus?.isConnected)restoreFocus.focus();}
  function showSources(id){const s=data.slides[findIndex(id)],target=$('#source-list');$('#sources-title').textContent='Evidence & sources · '+s.title;target.replaceChildren();const note=document.createElement('p');note.className='modal-note';note.textContent=s.evidenceNote;target.append(note);s.sourceKeys.forEach(key=>{const src=data.sources[key],article=document.createElement('article'),k=document.createElement('span'),a=document.createElement('a'),p=document.createElement('p');article.className='source-item';k.className='source-id';k.textContent=key+' · '+src.kind;a.href=src.url;a.target='_blank';a.rel='noopener noreferrer';a.textContent=src.title;p.textContent=src.description;article.append(k,a,p);target.append(article);});if(!s.sourceKeys.length){const p=document.createElement('p');p.textContent='Editorial framing or a clearly labeled illustrative method. The source appendix explains the evidence boundary.';target.append(p);}openDialog($('#sources-dialog'));}
  async function fullscreen(){if(document.fullscreenElement){await document.exitFullscreen();}else if(document.documentElement.requestFullscreen){try{await document.documentElement.requestFullscreen();}catch{toast('Fullscreen is unavailable here. Use your browser’s fullscreen command.');}}else{toast('Use your browser’s fullscreen command to enlarge the presentation.');}}
  document.addEventListener('click',event=>{const control=event.target.closest('button,a[data-slide]');if(!control)return;if(control.dataset.mode){setMode(control.dataset.mode);return;}if(control.dataset.slide){event.preventDefault();closeDialog($('#outline-dialog'));navigate(findIndex(control.dataset.slide),{focus:true});return;}if(control.dataset.sources){showSources(control.dataset.sources);return;}switch(control.id){case'prev':navigate(state.index-1);break;case'next':navigate(state.index+1);break;case'outline-toggle':openDialog($('#outline-dialog'));break;case'speaker-toggle':state.notes=!state.notes;update();break;case'fullscreen-toggle':fullscreen();break;case'print-toggle':window.print();break;case'outline-close':closeDialog($('#outline-dialog'));break;case'sources-close':closeDialog($('#sources-dialog'));break;}});
  document.addEventListener('keydown',event=>{if(event.altKey||event.ctrlKey||event.metaKey||event.defaultPrevented)return;if($$('.modal').some(d=>d.open))return;const el=event.target;if(el.closest('button,a,input,textarea,select,summary,[contenteditable=true]'))return;let handled=true;switch(event.key){case'ArrowRight':case'PageDown':case' ':if(state.mode==='present')navigate(state.index+1);else handled=false;break;case'ArrowLeft':case'PageUp':if(state.mode==='present')navigate(state.index-1);else handled=false;break;case'Home':if(state.mode==='present')navigate(0);else handled=false;break;case'End':if(state.mode==='present')navigate(coreCount-1);else handled=false;break;case'r':case'R':setMode('read');break;case'p':case'P':setMode('present');break;case'o':case'O':openDialog($('#outline-dialog'));break;case'n':case'N':state.notes=!state.notes;update();break;case'f':case'F':fullscreen();break;default:handled=false;}if(handled)event.preventDefault();});
  $$('.modal').forEach(dialog=>dialog.addEventListener('close',()=>{if(restoreFocus?.isConnected)restoreFocus.focus();}));
  window.addEventListener('hashchange',fromURL);window.addEventListener('popstate',fromURL);
  let printState;
  window.addEventListener('beforeprint',()=>{printState={hidden:units.map(u=>u.hidden),details:$$('details').map(d=>[d,d.open])};units.forEach(u=>u.hidden=false);if(state.mode==='read')$$('details.reader-speaker').forEach(d=>d.open=false);});
  window.addEventListener('afterprint',()=>{if(!printState)return;units.forEach((u,i)=>u.hidden=printState.hidden[i]);printState.details.forEach(([d,open])=>d.open=open);printState=null;});
  fromURL();
})();
