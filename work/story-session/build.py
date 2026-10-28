"""Build the analytical presentation and guide from local editorial sources."""
from pathlib import Path
from html import escape as h
import json
import re
from visuals import render_exhibit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / 'outputs'
DECK_NAME = 'ai-engineer-2026-five-stories.html'
GUIDE_NAME = 'ai-engineer-2026-five-stories-presenter-guide.html'
CONTENT = json.loads((HERE / 'briefing.json').read_text())
TITLE, SUBTITLE = CONTENT['title'], CONTENT['subtitle']
SLIDES, CHAPTERS, DISCUSSION = CONTENT['slides'], CONTENT['chapters'], CONTENT['discussion']
SOURCES = {s['id']: s for s in json.loads((HERE / 'research/sources.json').read_text())['sources']}
BRIEFS = json.loads((HERE / 'research/briefs.json').read_text())
CASE_OPENERS = {next(s['id'] for s in SLIDES if s['source'] == key) for key in SOURCES}
CSS = (HERE / 'deck.css').read_text()
JS = (HERE / 'deck.js').read_text()


def paragraphs(text):
    return ''.join(f'<p>{h(p.strip())}</p>' for p in text.split('\n\n') if p.strip())


def clock(seconds):
    seconds = round(seconds)
    return f'{seconds // 60:02}:{seconds % 60:02}'


def source_links(slide):
    if not slide['source']:
        return '<div class="reading-links">' + ''.join(f'<a href="{h(s["url"])}" target="_blank" rel="noopener">{h(s["organization"])}</a>' for s in SOURCES.values()) + '</div>'
    source = SOURCES[slide['source']]
    url = f'{source["url"]}&t={slide["timestamp"]}s'
    links = f'<a href="{h(url)}" target="_blank" rel="noopener">Original recording · {clock(slide["timestamp"])}</a>'
    if source['officialTranscript']:
        links += f'<a href="{h(source["officialTranscript"])}" target="_blank" rel="noopener">Organizer transcript</a>'
    return f'<div class="reading-links">{links}</div>'


def slide_notes(slide, full_brief=False):
    html = ''
    if slide['source']:
        context = BRIEFS[slide['source']]['context']
        html += f'<h3>{h(context["label"])}</h3><p><strong>{h(context["name"])}.</strong> {h(context["description"])}</p>'
    html += '<h3>Further explanation and evidence boundaries</h3>' + paragraphs(slide['reading'])
    if slide['technical']:
        html += '<details><summary>Technical illustration</summary><pre>' + h(slide['technical']) + '</pre></details>'
    if slide['source']:
        source, brief = SOURCES[slide['source']], BRIEFS[slide['source']]
        html += f'<h3>{h(source["title"])}</h3><p>{h(source["speaker"])} · {h(source["organization"])}</p>'
        html += source_links(slide)
        if full_brief:
            html += '<h3>Mechanism in the talk</h3>' + paragraphs(brief['mechanism'])
            html += '<h3>Evidence limits</h3>' + paragraphs(brief['limits'])
    else:
        html += source_links(slide)
    return html


def render_slide(slide, index):
    chapter = next(label for key, label, _ in CHAPTERS if key == slide['chapter'])
    if slide['source']:
        source = SOURCES[slide['source']]
        context = BRIEFS[slide['source']]['context']
        url = f'{source["url"]}&t={slide["timestamp"]}s'
        credit = f'<div class="source-credit-block"><a class="source-talk" href="{h(url)}" target="_blank" rel="noopener">{h(source["title"])}</a><span class="source-byline">{h(source["speaker"])} · {h(source["organization"])} · {clock(slide["timestamp"])}</span><span class="source-context" data-source-context="{slide["source"]}"><strong>{h(context["label"])}: {h(context["name"])}.</strong> {h(context["description"])}</span></div>'
    else:
        credit = '<span>Synthesis · Kepler, Bridgewater, Contour, Arize, Max Kanat-Alexander</span>'
    lead_class = 'slide-lead case-context' if slide['id'] in CASE_OPENERS else 'slide-lead'
    lead_prefix = '<strong>Case context.</strong> ' if slide['id'] in CASE_OPENERS else ''
    return f'''<section class="slide" id="slide-{slide['id']}" data-slide="{slide['id']}" data-title="{h(slide['title'])}" data-chapter="{slide['chapter']}" aria-labelledby="title-{slide['id']}">
<div class="face"><header class="slide-header"><div class="slide-topline"><span class="chapter-label">{h(chapter)}</span><span class="origin">{h(slide['origin'])}</span></div><h2 class="slide-title" id="title-{slide['id']}" tabindex="-1">{h(slide['title'])}</h2><p class="{lead_class}">{lead_prefix}{h(slide['lead'])}</p></header>
<div class="analysis">{render_exhibit(slide)}</div>
<div class="application-line"><strong>Engineering implication</strong><p>{h(slide['application'])}</p></div>
<footer class="slide-credit"><div class="credit-main">{credit}<button type="button" data-show-source="{slide['id']}">Detail &amp; sources</button></div><span class="slide-index">{index + 1:02} / {len(SLIDES):02}</span></footer></div>
<div class="reading-material">{slide_notes(slide)}<details><summary>Presenter’s notes</summary>{paragraphs(slide['script'])}</details></div></section>'''


def build_deck():
    short = ['Summary', 'Grounding', 'Context', 'Value', 'Evaluation', 'Quality', 'Takeaways']
    chapters = ''.join(f'<button type="button" data-chapter-jump="{key}" aria-label="{h(label)}: {duration} minutes" title="{h(label)} · {duration} min">{h(short[i])}</button>' for i, (key, label, duration) in enumerate(CHAPTERS))
    outline = ''
    for key, label, duration in CHAPTERS:
        links = ''.join(f'<a href="#present/{s["id"]}" data-slide-jump="{s["id"]}">{SLIDES.index(s) + 1:02}. {h(s["title"])}</a>' for s in SLIDES if s['chapter'] == key)
        outline += f'<li><span class="chapter-name">{h(label)} · {duration} min</span>{links}</li>'
    templates = ''.join(f'<template id="notes-{s["id"]}">{slide_notes(s, True)}</template>' for s in SLIDES)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>{h(TITLE)} · AI Engineer NYC 2026</title><meta name="description" content="An analytical engineering briefing on five AI Engineer cases, applied to text-to-SQL and institutional-sales meeting preparation."><style>{CSS}</style></head><body data-mode="read"><a class="skip-link" href="#main">Skip to the briefing</a>
<header class="app-header"><div class="wordmark">AI ENGINEERING<span>NYC 2026 / TEAM BRIEFING</span></div><h1 class="sr-only">{h(TITLE)}</h1><nav class="app-tools" aria-label="Briefing tools"><div class="mode-switch"><button type="button" data-mode-switch="present" aria-pressed="false">Slides</button><button type="button" data-mode-switch="read" aria-pressed="true">Read</button></div><button type="button" id="outline-toggle" aria-haspopup="dialog">Contents</button><a href="{GUIDE_NAME}" target="_blank" rel="noopener">Presenter guide</a><button type="button" id="print-deck">Print</button><button type="button" id="fullscreen-toggle" aria-pressed="false">Fullscreen</button></nav></header>
<main class="app-main" id="main"><div class="read-intro"><h2>{h(TITLE)}</h2><p>{h(SUBTITLE)}. The 22-slide briefing targets 35 minutes plus a separate 10-minute discussion. Each slide states its conclusion, provides supporting analysis, and identifies an engineering implication.</p><p>The reading edition adds source boundaries, technical illustrations, and presenter notes. All main-slide content is visible in both modes. The five original-release transcripts were reviewed October 27, 2026; case accounts, our applications, and fictional examples remain distinct.</p></div>{''.join(render_slide(s, i) for i, s in enumerate(SLIDES))}</main>
<footer class="delivery-bar"><nav class="chapter-nav" aria-label="Briefing sections">{chapters}</nav><span class="page-status" id="page-status"></span><div class="navigation"><span class="key-hint">← → / Space · F fullscreen</span><button type="button" id="previous">Previous</button><button type="button" id="next">Next</button></div><span class="fullscreen-message" id="fullscreen-message" role="status"></span></footer>
<div class="sr-only" id="live-status" aria-live="polite" aria-atomic="true"></div>
<dialog class="source-dialog" id="source-dialog" aria-labelledby="source-heading"><div class="dialog-heading"><h2 id="source-heading">Further detail</h2><button type="button" data-close-dialog>Close</button></div><div class="source-content" id="source-body"></div></dialog>
<dialog class="source-dialog" id="outline-dialog" aria-labelledby="outline-heading"><div class="dialog-heading"><h2 id="outline-heading">Briefing contents</h2><button type="button" data-close-dialog>Close</button></div><p>35 minutes of presentation followed by 10 minutes of discussion. Arrows or Space move between fully visible slides. Home and End jump to the first and last slides.</p><ol class="outline-list">{outline}</ol></dialog>
{templates}<script>{JS}\ndocument.getElementById('print-deck').addEventListener('click',()=>window.print());</script></body></html>'''


def build_guide():
    cumulative, rows, sections = 0, [], []
    for key, label, minutes in CHAPTERS:
        first = next(s['id'] for s in SLIDES if s['chapter'] == key)
        rows.append(f'<tr><td>{clock(cumulative * 60)}–{clock((cumulative + minutes) * 60)}</td><td><a href="#guide-{first}">{h(label)}</a></td><td>{minutes} min</td></tr>')
        cumulative += minutes
    elapsed = 0
    for i, slide in enumerate(SLIDES):
        end = elapsed + slide['minutes']
        next_title = SLIDES[i + 1]['title'] if i + 1 < len(SLIDES) else 'Ten-minute team discussion'
        sections.append(f'''<section class="guide-section" id="guide-{slide['id']}"><div class="guide-slide-top"><span>SLIDE {i + 1:02} / {len(SLIDES)} · {clock(elapsed * 60)}–{clock(end * 60)}</span><a href="{DECK_NAME}#present/{slide['id']}" target="_blank" rel="noopener">Open this slide</a></div><h2>{h(slide['title'])}</h2><div class="delivery-focus"><b>Discussion focus</b>{h(slide['focus'])}</div>{paragraphs(slide['script'])}<details><summary>Evidence, technical detail, and sources</summary>{slide_notes(slide)}</details><div class="guide-transition">Next: {h(next_title)}</div></section>''')
        elapsed = end
    source_sections = []
    for key, source in SOURCES.items():
        brief = BRIEFS[key]
        context = brief['context']
        moments = ''.join(f'<li><a href="{h(source["url"])}&amp;t={seconds}s" target="_blank" rel="noopener">{clock(seconds)} · {h(label)}</a></li>' for seconds, label in brief['moments'])
        source_sections.append(f'<section class="guide-section"><h2>{h(source["organization"])}</h2><p><a href="{h(source["url"])}" target="_blank" rel="noopener">{h(source["title"])}</a><br>{h(source["speaker"])}</p><h3>{h(context["label"])}</h3><p><strong>{h(context["name"])}.</strong> {h(context["description"])}</p><h3>Case context</h3>{paragraphs(brief["story"])}<h3>Mechanism</h3>{paragraphs(brief["mechanism"])}<h3>Evidence limits</h3>{paragraphs(brief["limits"])}<h3>Our application</h3>{paragraphs(brief["application"])}<ul>{moments}</ul></section>')
    discussion = ''.join(f'<h3>{i + 1:02}. {h(question)}</h3><p>{h(prompt)}</p>' for i, (question, prompt) in enumerate(DISCUSSION))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Presenter guide · {h(TITLE)}</title><style>{CSS}</style></head><body class="guide"><header class="guide-header"><span class="small-label">PRESENTER GUIDE / AI ENGINEER NYC 2026</span><h1>{h(TITLE)}</h1><p>{h(SUBTITLE)}. Analytical speaking notes, timing, engineering implications, source evidence, and a separate ten-minute team discussion.</p><div class="guide-tools"><a href="{DECK_NAME}" target="_blank" rel="noopener">Open presentation</a><a href="#discussion">Discussion</a><a href="#source-briefs">Source briefs</a><button type="button" id="print-guide">Print guide</button></div></header><main class="guide-main"><h2>Session structure</h2><p class="guide-note">Target: 35 minutes presenting and 10 minutes discussing. The fully visible slides support both explanation and independent reading. Timings are editorial allocations and still need rehearsal in the presenter’s voice. Keep this guide on a second screen.</p><table class="run-of-show"><thead><tr><th>Elapsed</th><th>Section</th><th>Duration</th></tr></thead><tbody>{''.join(rows)}<tr><td>35:00–45:00</td><td>Team discussion</td><td>10 min</td></tr></tbody></table><p class="guide-note">Research uses five complete original-release English auto-generated transcripts. Official metadata and organizer readings informed names and technical terms. Exhibits are original analyses or reconstructions. Optional recording links use individual-release timestamps.</p>{''.join(sections)}<section class="guide-section guide-discussion" id="discussion"><span class="small-label">35:00–45:00 / TEAM DISCUSSION</span><h2>Use the cases to examine our assumptions and tradeoffs</h2>{discussion}<p>Allow roughly three minutes per question and one minute for closing reflections. Follow useful concrete examples and invite limits on the analogies. No roadmap, experiment choice, or owner assignment is required.</p></section><div id="source-briefs"><h2>The five source briefs</h2>{''.join(source_sections)}</div></main><script>document.getElementById('print-guide').addEventListener('click',()=>window.print());let printState=[];window.addEventListener('beforeprint',()=>{{printState=[...document.querySelectorAll('details')].map(d=>[d,d.open]);printState.forEach(([d])=>d.open=true)}});window.addEventListener('afterprint',()=>printState.forEach(([d,open])=>d.open=open));</script></body></html>'''


def build_research_briefs():
    lines = [f'# Source briefs: {TITLE}', '', 'Reviewed October 27, 2026. Five complete original-release English auto-generated transcripts were extracted and reviewed. No audiovisual viewing or independent validation of company results is claimed.', '']
    for key, source in SOURCES.items():
        brief = BRIEFS[key]
        context = brief['context']
        lines += [f'## {source["organization"]}: {source["title"]}', '', f'{source["speaker"]} · [Original recording]({source["url"]})', '']
        lines += [f'**{context["label"]}: {context["name"]}.** {context["description"]}', '']
        for title, field in [('Case context', 'story'), ('Mechanism', 'mechanism'), ('Evidence limits', 'limits'), ('Our application', 'application')]:
            lines += [f'**{title}.** {brief[field]}', '']
        lines += [f'- [{clock(seconds)} · {label}]({source["url"]}&t={seconds}s)' for seconds, label in brief['moments']]
        lines += ['', f'Local caption: `{source["transcript"]}`. Acquisition method and checksum: `sources.json`.', '']
    (HERE / 'research/source-briefs.md').write_text('\n'.join(lines))


if __name__ == '__main__':
    assert len(SLIDES) == len({s['id'] for s in SLIDES}) == 22
    assert abs(sum(s['minutes'] for s in SLIDES) - 35) < .00001
    for key, _, duration in CHAPTERS:
        assert abs(sum(s['minutes'] for s in SLIDES if s['chapter'] == key) - duration) < .00001
    assert all(not {'steps', 'theme', 'cue'} & s.keys() for s in SLIDES)
    OUT.mkdir(exist_ok=True)
    (OUT / DECK_NAME).write_text(build_deck())
    (OUT / GUIDE_NAME).write_text(build_guide())
    build_research_briefs()
    counts = [{'id': s['id'], 'minutes': s['minutes'], 'scriptWords': len(re.findall(r"\b[\w’'-]+\b", s['script']))} for s in SLIDES]
    report = dict(designRevision='engineering-readout', slides=22, presentationMinutes=35, discussionMinutes=10, scriptWords=sum(s['scriptWords'] for s in counts), slidesDetail=counts)
    (HERE / 'validation/build-report.json').write_text(json.dumps(report, indent=2) + '\n')
    timing = dict(scriptWords=report['scriptWords'], assumedSpokenWordsPerMinute=140, estimatedSpeakingMinutes=round(report['scriptWords'] / 140, 2), remainingMinutesForTransitionsAndDiscussionPauses=round(35 - report['scriptWords'] / 140, 2), presentationTargetMinutes=35, discussionMinutes=10, status='Editorial pacing estimate; no spoken rehearsal or audio timing claimed.')
    (HERE / 'validation/timing-review.json').write_text(json.dumps(timing, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'slidesDetail'}, indent=2))
