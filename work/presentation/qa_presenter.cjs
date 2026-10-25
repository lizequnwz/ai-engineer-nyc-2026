const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {JSDOM,VirtualConsole}=require('../qa/node_modules/jsdom');
const script=JSON.parse(fs.readFileSync(path.join(__dirname,'presenter-script.json'))),deck=JSON.parse(fs.readFileSync(path.join(__dirname,'deck-data.json')));
const html=fs.readFileSync(path.join(__dirname,'../../outputs/ai-engineer-nyc-2026-presenter-guide.html'),'utf8');
const errors=[],vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(e.message));let printed=false;
const dom=new JSDOM(html,{runScripts:'dangerously',virtualConsole:vc,beforeParse(w){w.print=()=>{printed=true}}}),d=dom.window.document;
assert.equal(script.sections.length,29);assert.equal(script.sections.reduce((n,s)=>n+s.minutes,0),40);
assert.deepEqual(script.sections.map(s=>s.slideId),deck.slides.filter(s=>s.core).map(s=>s.id));
assert.equal(d.querySelectorAll('.script-card').length,29);assert.equal(script.qa.length,8);
assert.equal(script.sections.filter(s=>/Audience prompt \d of 3/.test(s.deliveryCue)).length,3);
for(const s of script.sections){const slide=deck.slides.find(x=>x.id===s.slideId);assert.deepEqual(slide.speakerNotes,[...s.talkTrack,s.transition]);assert.equal(slide.minutes,s.minutes);assert.ok(s.talkTrack.every(p=>typeof p==='string'&&p.length>30));}
for(const a of d.querySelectorAll('a[href^="#"]'))assert.ok(d.getElementById(a.getAttribute('href').slice(1)));
assert.equal(d.querySelectorAll('[src],link[rel="stylesheet"]').length,0);assert.doesNotMatch(html,/fetch\(|localStorage|sessionStorage/);
d.getElementById('cue-toggle').click();assert.equal(d.body.classList.contains('cues-only'),true);assert.equal(d.getElementById('cue-toggle').getAttribute('aria-pressed'),'true');d.getElementById('cue-toggle').click();assert.equal(d.body.classList.contains('cues-only'),false);d.getElementById('print').click();assert.equal(printed,true);assert.deepEqual(errors,[]);
assert.match(d.getElementById('s11').textContent,/January twentieth/);assert.match(d.getElementById('s16').textContent,/invented fixture/);assert.match(d.getElementById('s23').textContent,/not a reported production incident/);
const result={date:'2026-10-25',coreSections:29,minutes:40,qa:8,audiencePrompts:3,checks:['All core IDs, order, spoken notes and pacing match the presentation','All 29 guide anchors and cue cards resolve','Cue view toggles with aria state; print calls browser print','No external runtime assets, storage or network calls','Eight Q&A and three planned audience prompts','Time-cutoff, next-period fixture and unknown-outcome boundaries present'],limits:['DOM and static source checks only; no browser rendering','Timing is a rehearsal target, not measured live delivery']};fs.writeFileSync(path.join(__dirname,'presenter-validation.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));dom.window.close();
