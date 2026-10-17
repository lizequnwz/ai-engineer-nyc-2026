(()=>{
'use strict';
const DATA=JSON.parse(document.getElementById('report-data').textContent);
const sessions=new Map(DATA.sessions.map(s=>[s.id,s]));
const qs=s=>document.querySelector(s),qsa=s=>[...document.querySelectorAll(s)];
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const url=s=>'https://ai.engineer/nyc/2026/schedule?session='+encodeURIComponent(s.id);
const dayName=d=>d.endsWith('13')?'Tuesday':'Wednesday';
const shortDay=d=>d.endsWith('13')?'Tue Oct 13':'Wed Oct 14';
const clock=m=>`${Math.floor(m/60)%12||12}:${String(m%60).padStart(2,'0')}`;
const period=m=>m<720?'AM':'PM';
const range=(a,b)=>period(a)===period(b)?`${clock(a)}–${clock(b)} ${period(b)}`:`${clock(a)} ${period(a)}–${clock(b)} ${period(b)}`;
const slotId=slot=>'slot-'+slot.date+'-'+slot.startMinutes;
const leadership=s=>s.topics.some(t=>t.includes('Leadership'));
const speakerText=s=>s.speakers.length?s.speakers.map(p=>p.name+(p.company?' · '+p.company:'')).join(' / '):'Speaker not published';
const speakerHtml=s=>s.speakers.length?s.speakers.map(p=>`<strong>${esc(p.name)}</strong>${p.company?' · '+esc(p.company):''}`).join('<br>'):'Speaker not published';
let activeDay='2026-10-13';
let currentNoteId;
const drafts=new Map();
const draftFields=['decision','takeaway','evidence','label','maturity','risk','test','followup'];
let toastTimer;
function toast(text){const el=qs('#toast');el.textContent=text;el.hidden=false;clearTimeout(toastTimer);toastTimer=setTimeout(()=>el.hidden=true,4200)}
function download(name,text,type='text/plain;charset=utf-8'){const b=new Blob([text],{type});const u=URL.createObjectURL(b);const a=document.createElement('a');a.href=u;a.download=name;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),1000)}
async function copy(text){try{await navigator.clipboard.writeText(text);toast('Copied to clipboard.')}catch(e){download('conference-text.txt',text);toast('Clipboard unavailable here. Downloaded the text instead.')}}
const pickById=new Map(DATA.slots.flatMap(sl=>sl.picks.map(p=>[p.id,p])));

function renderSpotlights(){
 const groups=[
 {title:'Permission-aware knowledge',why:'Make the source boundary explicit before asking the model to reason.',items:[['88f71c9f-f0a9-4f42-96c0-0e1492bad1c2','Tue 11:55 · Can Your AI Analyst Keep a Secret?'],['9b002687-09cf-42e2-9282-532ed9d0c184','Wed 11:30 · Did reranking improve the answer?']]},
 {title:'Whole-system evaluation',why:'A local improvement must survive the full agent and its real workload.',items:[['30afe596-abe2-417c-bd5a-313fa4bc54b3','Tue 11:30 · Can you defend its decision?'],[DATA.slots.find(s=>s.date.endsWith('13')&&s.startMinutes===920).picks[0].id,'Tue 3:20 · Did the agent fix cause a regression?']]},
 {title:'Evidence before autonomy',why:'Retain the sources and behaviors that make a result reviewable.',items:[[DATA.slots.find(s=>s.date.endsWith('14')&&s.startMinutes===895).picks[0].id,'Wed 2:55 · Deployment gates'],['1cbc625f-7f07-49bb-9c5c-57c95f07ba77','Wed 4:48 · Process supervision']]}
 ];
 qs('#must-catch').innerHTML=groups.map((g,i)=>`<article class="panel"><div class="eyebrow teal">High-conviction cluster / 0${i+1}</div><h3>${g.title}</h3><p class="small muted">${g.why}</p>${g.items.map(([id,label])=>{const s=sessions.get(id);return `<p class="small" style="margin:8px 0"><a href="${url(s)}" target="_blank" rel="noopener">${esc(label)}</a></p>`}).join('')}</article>`).join('');
}

function routeRows(day){
 const slots=DATA.slots.filter(s=>s.date===day);
 const rows=[{start:day.endsWith('13')?495:510,end:535,title:day.endsWith('13')?'Badge, coffee, and room orientation':'Arrive, check changes, and prepare',detail:'Level 1 Lobby → Simons Room (Metropolitan East)',why:'Find your first room and review the day’s one question per talk.',kind:'break'},
 {start:535,end:630,title:'Welcome + morning plenaries',detail:'Simons Room (Metropolitan East) · 5 sequential talks',why:day.endsWith('13')?'Prioritize Bridgewater’s knowledge platform and Two Sigma’s safety/utility tradeoffs.':'Prioritize policy-driven workflows and the security incident/defense discussion.',kind:'plenary'}];
 for(const sl of slots){const s=sessions.get(sl.picks[0].id);rows.push({start:s.startMinutes,end:s.endMinutes,title:s.title,detail:speakerText(s)+' · '+s.room,why:sl.picks[0].question,slot:sl,session:s,kind:'talk'});if(sl.startMinutes===740){rows.push({start:758,end:805,title:'Lunch + one focused peer conversation',detail:'Lunch break is listed noon–2 PM',why:'Ask for a production failure that changed someone’s design. Keep the exchange concrete.',kind:'break'});rows.push({start:805,end:815,title:'10-minute note cleanup',detail:'Complete three useful notes, then move to the 1:40 talk',why:'Separate speaker claims from your own application hypotheses.',kind:'break'})}}
 rows.push({start:963,end:985,title:'Synthesis + transfer to featured keynotes',detail:'Reserve the gap; expo closes at 4:30 PM',why:'Write today’s 3–2–1 draft or resolve one pre-selected expo question, then return to Simons by 4:25.',kind:'break'});
 rows.push({start:985,end:1050,title:'Featured keynotes + closing remarks',detail:'Simons Room (Metropolitan East) · 3 sequential talks',why:day.endsWith('13')?'Institutional perspective plus horizon scanning; several abstracts remain unpublished.':'Make 4:48 PM process supervision a priority; evaluate behavior as well as final answers.',kind:'plenary'});
 rows.push({start:1050,end:day.endsWith('13')?1070:1095,title:day.endsWith('13')?'20-minute daily digest':'30–45-minute conference synthesis',detail:day.endsWith('13')?'Before any optional evening event':'Default evening plan; networking events require confirmed access',why:day.endsWith('13')?'Three useful patterns, two unresolved risks, one experiment.':'Compare both days; choose Adopt / Test / Watch / Reject and outline the manager summary.',kind:'break'});
 return rows.sort((a,b)=>a.start-b.start);
}
function keynoteCard(s){const info=DATA.keynotes[s.id];return `<article class="keynote-card"><span class="when">${range(s.startMinutes,s.endMinutes)}${info.priority?' · HIGH PRIORITY':''}</span><strong>${esc(s.title)}</strong><div class="small muted">${esc(speakerText(s))}</div><p>${esc(info.focus)}</p>${info.caveat?`<p><b>Limit:</b> ${esc(info.caveat)}</p>`:''}<a href="${url(s)}" target="_blank" rel="noopener">Official session ↗</a></article>`}
function renderRoute(){
 const day=activeDay;const ks=DATA.sessions.filter(s=>s.date===day&&s.type==='keynote').sort((a,b)=>a.startMinutes-b.startMinutes);
 const rows=routeRows(day);const picks=DATA.slots.filter(s=>s.date===day).map(s=>s.picks[0]);
 const counts=Object.fromEntries(['Retrieval','Evals','Security','Production','Strategy','Models'].map(t=>[t,picks.filter(p=>p.theme===t).length]));
 qs('#route-content').innerHTML=`<div class="route-intro"><strong>${dayName(day)}’s learning arc:</strong> ${day.endsWith('13')?'Context → evaluation evidence → defensibility → permissions → numerical reliability → operational improvement.':'Analyst workflows → context ablations → answer-level eval → authority boundaries → release gates → evidence layers.'}<br><span class="small muted">11 selected concurrent talks + 8 plenary talks. All default concurrent choices avoid the Leadership Track label. Access and capacity still require local confirmation.</span></div><div class="route-columns"><div class="timeline">${rows.map(r=>`<div class="timeline-time">${range(r.start,r.end)}</div><div class="timeline-body ${r.kind==='break'?'break':''}"><h3>${esc(r.title)}</h3><div class="route-detail">${esc(r.detail)}${r.slot?`<a href="#${slotId(r.slot)}" class="slot-link" data-show-slot="${slotId(r.slot)}">Compare top 3 ↗</a>`:''}</div><p class="route-why">${r.session?'<strong>Capture:</strong> ':''}${esc(r.why)}</p></div>`).join('')}</div><aside class="route-aside"><article class="panel"><div class="eyebrow teal">Plenary listening guide</div><h3>Stay in Simons. Vary your note depth.</h3><p class="small muted">No parallel choices in these blocks. All 8 talks are reviewed below, including those with limited advance detail.</p><details class="plenary-group" open><summary>Morning · 9:00–10:30 AM</summary>${ks.filter(s=>s.startMinutes<720).map(keynoteCard).join('')}</details><details class="plenary-group" open><summary>Evening · 4:30–5:24 PM</summary>${ks.filter(s=>s.startMinutes>720).map(keynoteCard).join('')}</details></article><article class="panel" style="margin-top:20px"><h3>Today’s primary themes</h3><p class="small muted">Counts across the 11 selected concurrent talks; one primary category per talk.</p>${Object.entries(counts).map(([t,n])=>`<div class="coverage-row"><span>${t}</span><div class="coverage-track"><div class="coverage-bar" style="width:${n/11*100}%"></div></div><span class="coverage-num">${n}</span></div>`).join('')}</article></aside></div>`;
 qsa('.route-tab').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.day===day)));
}
function renderChoices(){
 qs('#choice-content').innerHTML=DATA.slots.map(sl=>{
 const all=DATA.sessions.filter(s=>s.date===sl.date&&s.startMinutes===sl.startMinutes&&['talk','breakout'].includes(s.type));
 const others=all.filter(s=>!sl.picks.some(p=>p.id===s.id));
 const warning=sl.notes||'';
 return `<article class="slot" id="${slotId(sl)}" data-date="${sl.date}"><div class="slot-heading"><span class="slot-date">${shortDay(sl.date)}</span><h3>${clock(sl.startMinutes)} ${period(sl.startMinutes)} choice slot</h3><span class="pool">${all.length} scheduled talks · top 3 ranked</span></div>${warning?`<p class="slot-warning">${esc(warning)}</p>`:''}<div class="choice-grid">${sl.picks.map((p,i)=>{const s=sessions.get(p.id);return `<article class="choice ${i===0?'first':''}" data-id="${s.id}" data-theme="${esc(p.theme)}"><div class="choice-inner"><div class="choice-top"><span class="rank ${i===0?'first':''}">#${i+1} ${i===0?'RECOMMENDED':'ALTERNATIVE'}</span><span class="pill" data-theme="${esc(p.theme)}">${esc(p.theme)}</span></div><h4>${esc(s.title)}</h4><div class="speaker">${speakerHtml(s)}</div><p class="room">${range(s.startMinutes,s.endMinutes)} · ${esc(s.room)}${leadership(s)?'<br><strong style="color:var(--rust)">Leadership Track · confirm access</strong>':''}</p><p class="choice-reason">${esc(p.reason)}</p><details><summary>Tradeoff + what to capture</summary><p><b>Opportunity cost / limit:</b> ${esc(p.tradeoff)}</p><p><b>Carry this question:</b> ${esc(p.question)}</p></details><a class="source-link" href="${url(s)}" target="_blank" rel="noopener">Official abstract & speaker details ↗</a><button type="button" class="inline-link no-print" style="font-size:12px;text-align:left;margin-top:8px;display:inline-flex;min-height:44px;justify-content:flex-start" data-note-id="${s.id}">Use in note workspace</button></div></article>`}).join('')}</div>${others.length?`<details class="others"><summary>Other scheduled options in this slot (${others.length})</summary><ul>${others.map(s=>`<li><a href="${url(s)}" target="_blank" rel="noopener">${esc(s.title)}</a> · ${esc(speakerText(s))} · ${esc(s.room)}${leadership(s)?' · Leadership Track; confirm access':''}${!s.hasAbstract?' · abstract not published':''}</li>`).join('')}</ul></details>`:''}</article>`;
 }).join('');
 applyFilters();
}
function applyFilters(){
 const day=qs('#day-filter').value,theme=qs('#theme-filter').value,query=qs('#query').value.trim().toLowerCase();let slots=0,cards=0;
 qsa('.slot').forEach(sl=>{let visible=0;qsa(`#${sl.id} .choice`).forEach(c=>{const s=sessions.get(c.dataset.id),p=pickById.get(s.id);const hay=[s.title,s.room,speakerText(s),p.reason,p.tradeoff,p.question].join(' ').toLowerCase();const match=(day==='all'||s.date===day)&&(theme==='all'||c.dataset.theme===theme)&&(!query||hay.includes(query));c.hidden=!match;if(match){visible++;cards++}});sl.hidden=visible===0;if(visible)slots++});
 qs('#filter-status').textContent=`Showing ${cards} of 66 ranked recommendations across ${slots} of 22 concurrent slots. Filters preserve each talk’s original rank.`;qs('#empty-choices').hidden=slots!==0;
}
function setupNotes(){
 const chosen=new Set([...pickById.keys(),...Object.keys(DATA.keynotes)]);
 const sorted=DATA.sessions.filter(s=>chosen.has(s.id)).sort((a,b)=>a.date.localeCompare(b.date)||a.startMinutes-b.startMinutes||a.title.localeCompare(b.title));
 qs('#note-session').innerHTML=['2026-10-13','2026-10-14'].map(d=>`<optgroup label="${dayName(d)} · ${d}">${sorted.filter(s=>s.date===d).map(s=>`<option value="${s.id}">${clock(s.startMinutes)} ${period(s.startMinutes)} · ${esc(s.title)}</option>`).join('')}</optgroup>`).join('');
 loadNote(qs('#note-session').value);
}
function saveNote(){if(currentNoteId)drafts.set(currentNoteId,Object.fromEntries(draftFields.map(f=>[f,qs('#note-'+f).value])))}
function loadNote(id){saveNote();currentNoteId=id;qs('#note-session').value=id;const s=sessions.get(id);const draft=drafts.get(id)||{decision:pickById.get(id)?.question||DATA.keynotes[id]?.question||'What decision can this session help me make?',label:'Speaker claim',maturity:'Unclear'};draftFields.forEach(f=>qs('#note-'+f).value=draft[f]||'');qs('#note-session-meta').innerHTML=`${esc(shortDay(s.date))} · ${range(s.startMinutes,s.endMinutes)}<br>${esc(speakerText(s))}<br>${esc(s.room)} · <a href="${url(s)}" target="_blank" rel="noopener">Official session</a>`}
function noteText(id=currentNoteId){saveNote();const s=sessions.get(id),d=drafts.get(id);return `# ${s.title}\n\nSpeaker/company: ${speakerText(s)}\nDate/time: ${s.date} · ${range(s.startMinutes,s.endMinutes)} EDT\nRoom: ${s.room}\nOfficial source: ${url(s)}\n\n## Decision / question\n${d.decision}\n\n## Takeaway + mechanism\n${d.takeaway}\n\n## Evidence\nStrongest level: ${d.label}\nMaturity: ${d.maturity}\n${d.evidence}\n\n## Failure / control / tradeoff\n${d.risk}\n\n## Our hypothesis + smallest test\n${d.test}\n\n## Questions / materials / follow-up\n${d.followup}\n\nEvidence reminder: conference claims are not internally validated findings.\n`}
const noteTemplate=`# TALK / SPEAKER / COMPANY\nDate / time / room / official URL:\nDecision this could inform:\n\n## One-sentence takeaway\n\n## Mechanism\nData → retrieval/model → tools → checks → output\n\n## Strongest evidence\nClaim + attributed source:\nWorkload/sample + baseline + metric + period:\nMaturity: demo / pilot / production / unclear\nLevel: CLAIM / SHOWN / CHECKED\nMissing details / counterexamples:\n\n## Failure mode / control / tradeoff\n\n## Our application hypothesis (separate from speaker evidence)\n\n## Smallest test + success measure + stop rule\n\n## Open speaker question\n\n## Slides / repository / recording (if offered)\n\n## Follow-up\nPerson → reason → agreed next action\n\nTags: retrieval / evals / reliability / controls / economics\n\n# Daily 3–2–1 digest\n3 useful patterns + source talks:\n2 unresolved risks / competing claims:\n1 experiment to propose:\nWhat changed my mind:\n`;
function utcStamp(date,m){const [y,mo,d]=date.split('-').map(Number);return new Date(Date.UTC(y,mo-1,d,Math.floor(m/60)+4,m%60)).toISOString().replace(/[-:]/g,'').replace(/\.\d{3}Z$/,'Z')}
const icsEsc=s=>String(s).replace(/\\/g,'\\\\').replace(/\n/g,'\\n').replace(/,/g,'\\,').replace(/;/g,'\\;');
function foldICS(line){const enc=new TextEncoder();let out='',part='';for(const c of line){if(enc.encode(part+c).length>73){out+=part+'\r\n';part=' '+c}else part+=c}return out+part}
function exportCalendar(){const events=[];for(const d of ['2026-10-13','2026-10-14']){for(const r of routeRows(d)){if(r.kind==='plenary')continue;events.push({date:d,start:r.start,end:r.end,title:r.title,location:r.session?r.session.room:r.detail,description:r.why+(r.session?'\n'+speakerText(r.session)+'\n'+url(r.session):''),id:r.session?.id||d+'-'+r.start})}for(const s of DATA.sessions.filter(s=>s.date===d&&(s.type==='keynote'||(s.type==='other'&&[535,536,985,1045].includes(s.startMinutes))))){events.push({date:d,start:s.startMinutes,end:s.endMinutes,title:s.title,location:s.room,description:(DATA.keynotes[s.id]?.focus||'Conference remarks')+'\n'+url(s),id:s.id})}}
 const lines=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Personal Conference Field Guide//AI Engineer NYC 2026//EN','CALSCALE:GREGORIAN','METHOD:PUBLISH','X-WR-CALNAME:AI Engineer NYC 2026 - Recommended Path'];
 for(const e of events.sort((a,b)=>a.date.localeCompare(b.date)||a.start-b.start)){lines.push('BEGIN:VEVENT','UID:'+e.id+'@aie-personal-guide','DTSTAMP:20261010T191137Z','DTSTART:'+utcStamp(e.date,e.start),'DTEND:'+utcStamp(e.date,e.end),'SUMMARY:'+icsEsc(e.title),'LOCATION:'+icsEsc(e.location),'DESCRIPTION:'+icsEsc(e.description+'\nPlanning snapshot Oct 10, 2026. Tentative schedule; verify access and changes.'),'STATUS:TENTATIVE','END:VEVENT')}lines.push('END:VCALENDAR');download('ai-engineer-nyc-2026-recommended-path.ics',lines.map(foldICS).join('\r\n')+'\r\n','text/calendar;charset=utf-8');toast('Calendar exported: both days, recommended talks and planning buffers.');
}
let printState;
function preparePrint(){
 if(printState)return;
 printState={filters:['query','day-filter','theme-filter'].map(id=>[id,qs('#'+id).value]),day:activeDay,routes:qs('#route-content').innerHTML,details:qsa('details').map(d=>[d,d.open])};
 qs('#query').value='';qs('#day-filter').value='all';qs('#theme-filter').value='all';applyFilters();qsa('details').forEach(d=>d.open=true);
 const both=['2026-10-13','2026-10-14'].map(d=>{activeDay=d;renderRoute();return `<h3 class="print-only" style="margin-top:20px">${dayName(d)} · ${d}</h3>`+qs('#route-content').innerHTML}).join('');
 activeDay=printState.day;qs('#route-content').innerHTML=both;
}
function restorePrint(){
 if(!printState)return;const state=printState;printState=undefined;activeDay=state.day;qs('#route-content').innerHTML=state.routes;
 state.details.forEach(([d,open])=>{if(d.isConnected)d.open=open});state.filters.forEach(([id,value])=>qs('#'+id).value=value);applyFilters();qsa('.route-tab').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.day===activeDay)));
}
function printReport(){window.print()}
window.addEventListener('beforeprint',preparePrint);
window.addEventListener('afterprint',restorePrint);


qs('#filters').addEventListener('submit',e=>e.preventDefault());
qs('#filters').addEventListener('input',applyFilters);
qs('#filters').addEventListener('change',applyFilters);
qs('#filters').addEventListener('reset',()=>setTimeout(applyFilters,0));
qs('#note-form').addEventListener('submit',e=>e.preventDefault());
qs('#note-session').addEventListener('change',()=>{loadNote(qs('#note-session').value);toast('Switched talk. Each talk’s draft is kept separately in this tab; export before closing.')});
document.addEventListener('click',e=>{
 const tab=e.target.closest('.route-tab');if(tab){activeDay=tab.dataset.day;renderRoute();return}
 const show=e.target.closest('[data-show-slot]');if(show){qs('#filters').reset();applyFilters();setTimeout(()=>document.getElementById(show.dataset.showSlot)?.scrollIntoView({block:'start'}),0);return}
 const note=e.target.closest('[data-note-id]');if(note){loadNote(note.dataset.noteId);qs('#notes').scrollIntoView({block:'start'});qs('#note-session').focus({preventScroll:true});toast('Selected talk and its separate draft. Export before closing.');return}
 const button=e.target.closest('[data-action]');if(!button)return;
 const a=button.dataset.action;
 if(a==='print')printReport();
 if(a==='calendar')exportCalendar();
 if(a==='template')download('ai-engineer-talk-and-daily-note-template.md',noteTemplate,'text/markdown;charset=utf-8');
 if(a==='export-note'){const s=sessions.get(qs('#note-session').value);download(s.date+'-'+String(s.startMinutes)+'-talk-note.md',noteText(),'text/markdown;charset=utf-8');toast('Note exported. Keep the file in your chosen notes workspace.');}
 if(a==='copy-note')copy(noteText());
 if(a==='export-all-notes'){saveNote();const ids=[...drafts.keys()];download('ai-engineer-nyc-2026-talk-notes.md',ids.map(id=>noteText(id)).join('\n\n---\n\n'),'text/markdown;charset=utf-8');toast(`Exported ${ids.length} visited-talk draft${ids.length===1?'':'s'}.`);}
 if(a==='copy-executive')copy(qs('#executive-template').textContent);
});
renderSpotlights();renderRoute();renderChoices();setupNotes();
if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>{for(const en of entries)if(en.isIntersecting){qsa('.sidebar nav a').forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+en.target.id))}},{rootMargin:'-5% 0px -70% 0px',threshold:0});qsa('section').forEach(s=>observer.observe(s))}
})();
