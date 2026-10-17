(() => {
  'use strict';
  const $ = s => document.querySelector(s);
  const $$ = s => [...document.querySelectorAll(s)];
  const base = JSON.parse($('#draft-data').textContent);
  let dirty = false, toastTimer;
  const fields = $$('[data-report-field]');
  function toast(message) { $('#toast').textContent=message; $('#toast').hidden=false; clearTimeout(toastTimer); toastTimer=setTimeout(()=>$('#toast').hidden=true,4000); }
  function filter() {
    const query=$('#firm-query').value.trim().toLowerCase(), type=$('#firm-type').value;
    let count=0;
    $$('.firm-row').forEach(row=> {row.hidden=!(row.textContent.toLowerCase().includes(query)&&(!type||row.dataset.evidence===type)); if(!row.hidden)count++;});
    $('#firm-count').textContent=`${count} of ${$$('.firm-row').length} firm perspectives shown`;
    $('#firm-empty').hidden=count!==0;
  }
  $('#firm-query').addEventListener('input',filter);
  $('#firm-type').addEventListener('change',filter);
  $('#firm-reset').addEventListener('click',()=>{$('#firm-query').value='';$('#firm-type').value='';filter();});
  fields.forEach(el=>el.addEventListener('input',()=>{dirty=true;}));
  function draft() {
    const entered=fields.filter(el=>el.value.trim());
    let text=base.markdown;
    if(entered.length){text+='\n\n---\n\n## Attendee update notes — unverified draft additions\n\n'; entered.forEach(el=>{text+=`### ${el.dataset.reportField}\n\n${el.value.trim()}\n\n`;});}
    return text;
  }
  function download() {
    const blob=new Blob([draft()],{type:'text/markdown;charset=utf-8'}), url=URL.createObjectURL(blob), a=document.createElement('a');
    a.href=url;a.download='ai-engineer-nyc-2026-team-report-draft.md';a.click();setTimeout(()=>URL.revokeObjectURL(url),2000);dirty=false;toast('Report draft exported, including entered updates.');
  }
  async function copy() {
    try { if(!navigator.clipboard?.writeText)throw new Error('Clipboard unavailable'); await navigator.clipboard.writeText(draft());dirty=false;toast('Report draft copied, including entered updates.'); }
    catch { toast('Clipboard access is unavailable here. Use Download report draft.'); }
  }
  const printStates=[];
  function beforePrint() {
    $('#printed-updates').replaceChildren();
    fields.filter(el=>el.value.trim()).forEach(el=>{const div=document.createElement('div'), h=document.createElement('h4'), p=document.createElement('p');div.className='print-note';h.textContent=el.dataset.reportField;p.textContent=el.value.trim();div.append(h,p);$('#printed-updates').append(div);});
    $('#printed-updates').hidden=!$('#printed-updates').children.length;
    $$('.source-details').forEach(el=>{printStates.push([el,el.open]);el.open=true;});
  }
  function afterPrint(){printStates.splice(0).forEach(([el,open])=>{el.open=open;});}
  window.addEventListener('beforeprint',beforePrint);window.addEventListener('afterprint',afterPrint);
  document.addEventListener('click',event=>{const button=event.target.closest('[data-action]');if(!button)return; if(button.dataset.action==='download')download();if(button.dataset.action==='copy')copy();if(button.dataset.action==='print')window.print();});
  window.addEventListener('beforeunload',event=>{if(dirty){event.preventDefault();event.returnValue='';}});
  filter();
})();
