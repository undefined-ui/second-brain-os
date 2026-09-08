#!/usr/bin/env python3
"""Builds site/index.html (the guide) and site/resources.html (the catalog)."""
import json, os, html

D = json.load(open("site_data.json"))
OUT = "."
os.makedirs(OUT, exist_ok=True)
REPO = "https://github.com/undefined-ui/second-brain-os"

CSS = """
:root{
  --paper:#EAEEE9; --card:#F7F9F6; --ink:#15201B; --soft:#4B5A52; --faint:#7C8A82;
  --rule:#D2DACF; --accent:#1F6B52; --accent-bg:#E1EDE5; --num:#8A6B23;
  --w:68ch;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);
  font:17px/1.62 Charter,Georgia,"Iowan Old Style",serif;
  -webkit-font-smoothing:antialiased}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,"DejaVu Sans Mono",monospace}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline;text-underline-offset:3px}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:2px}

header{position:sticky;top:0;z-index:40;background:rgba(234,238,233,.94);
  backdrop-filter:blur(8px);border-bottom:1px solid var(--rule)}
.bar{max-width:1500px;margin:0 auto;padding:13px 22px;display:flex;gap:20px;align-items:center}
.brand{font:600 15px/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--ink);letter-spacing:-.01em}
.brand span{color:var(--accent)}
nav{display:flex;gap:18px;font-size:14.5px}
nav a{color:var(--soft)} nav a.on{color:var(--ink);font-weight:600}
.search{margin-left:auto;position:relative}
.search input{font:14px/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--ink);
  background:var(--card);border:1px solid var(--rule);border-radius:3px;
  padding:8px 11px;width:210px}
.search input::placeholder{color:var(--faint)}
.hits{position:absolute;right:0;top:40px;width:430px;max-height:62vh;overflow:auto;
  background:var(--card);border:1px solid var(--rule);border-radius:3px;display:none}
.hits.open{display:block}
.hit{display:block;padding:10px 13px;border-bottom:1px solid var(--rule);color:var(--ink)}
.hit:last-child{border:0}
.hit:hover{background:var(--accent-bg);text-decoration:none}
.hit b{font-weight:600;font-size:15px}
.hit i{display:block;font-style:normal;font-size:12.5px;color:var(--faint);
  font-family:ui-monospace,Menlo,monospace;margin-top:2px}

.wrap{max-width:1500px;margin:0 auto;padding:0 22px;display:grid;
  grid-template-columns:266px minmax(0,1fr) 210px;gap:44px;align-items:start}
@media(max-width:1180px){.wrap{grid-template-columns:240px minmax(0,1fr);gap:34px}.rail{display:none}}
.toc-btn{display:none;font:13px/1 ui-monospace,Menlo,monospace;background:var(--card);
  color:var(--ink);border:1px solid var(--rule);border-radius:3px;padding:8px 12px;cursor:pointer}
@media(max-width:860px){
  .bar{flex-wrap:wrap;gap:12px;padding:11px 16px}
  .brand{white-space:nowrap;font-size:14px}
  nav{gap:14px;font-size:14px}
  .toc-btn{display:block;margin-left:auto}
  nav a[href^="http"]{display:none}
  .search{margin-left:0;order:9;width:100%}
  .search input{width:100%}
  .hits{width:100%;left:0;right:auto}
  .wrap{grid-template-columns:1fr;gap:0;padding:0 16px}
  aside{position:static;height:auto;border-right:0;border-bottom:1px solid var(--rule);
    padding:14px 0 18px;display:none}
  aside.show{display:block}
  main{padding:24px 0 70px}
  body{font-size:16.5px}
}

aside{position:sticky;top:57px;height:calc(100vh - 57px);overflow:auto;
  padding:26px 18px 60px 0;border-right:1px solid var(--rule)}
.sec{margin-bottom:3px}
.sec>button{width:100%;text-align:left;background:none;border:0;cursor:pointer;
  font:600 14px/1.4 Charter,Georgia,serif;color:var(--ink);padding:6px 6px 6px 0;
  display:flex;gap:8px;align-items:baseline}
.sec>button .n{font:11px/1 ui-monospace,Menlo,monospace;color:var(--faint);margin-left:auto}
.sec>button .k{font:11px/1 ui-monospace,Menlo,monospace;color:var(--accent);width:20px}
.sec ol{list-style:none;padding:0 0 6px 28px;display:none}
.sec.open ol{display:block}
.sec ol a{display:block;padding:4px 6px 4px 10px;font-size:14px;color:var(--soft);
  border-left:1px solid var(--rule);line-height:1.35}
.sec ol a:hover{color:var(--ink);border-color:var(--accent);text-decoration:none}
.sec ol a.cur{color:var(--ink);font-weight:600;border-left:2px solid var(--accent);
  background:var(--accent-bg)}

main{padding:34px 0 90px;min-width:0}
.rail{position:sticky;top:80px;padding:38px 0;font-size:13px;color:var(--faint)}
.rail h4{font:11px/1 ui-monospace,Menlo,monospace;color:var(--faint);
  letter-spacing:.08em;margin-bottom:9px;font-weight:600}
.rail a{display:block;color:var(--soft);padding:3px 0;font-size:13px;line-height:1.35}
.rail .grp{margin-bottom:24px}

/* hero */
.hero{max-width:var(--w)}
.hero h1{font:600 clamp(34px,4.6vw,52px)/1.05 Charter,Georgia,serif;letter-spacing:-.025em;margin-bottom:14px}
.hero p{font-size:19px;color:var(--soft);margin-bottom:8px}
.figure{margin:30px 0 34px;background:var(--card);border:1px solid var(--rule);border-radius:4px;
  padding:10px 10px 4px;max-width:820px}
.figure figcaption{font:11.5px/1.5 ui-monospace,Menlo,monospace;color:var(--faint);padding:6px 8px 8px}
svg .edge{stroke:var(--accent);fill:none}
svg .node circle{fill:var(--card);stroke:var(--accent);stroke-width:1.5;cursor:pointer;
  transition:fill .15s}
svg .node:hover circle{fill:var(--accent-bg)}
svg .node text{font:12px ui-monospace,Menlo,monospace;fill:var(--ink);cursor:pointer}
svg .node .cnt{font-size:10px;fill:var(--faint)}
svg .node .idx{font-size:11px;fill:var(--accent);font-weight:600}
.stats{display:flex;flex-wrap:wrap;gap:26px;margin:26px 0 34px;padding-top:20px;border-top:1px solid var(--rule)}
.stat b{display:block;font:600 27px/1 Charter,Georgia,serif;color:var(--num)}
.stat span{font:12px/1.4 ui-monospace,Menlo,monospace;color:var(--faint)}
.seclist{max-width:var(--w)}
.seclist article{padding:16px 0;border-top:1px solid var(--rule)}
.seclist h3{font:600 18px/1.3 Charter,Georgia,serif;margin-bottom:3px}
.seclist p{font-size:15px;color:var(--soft)}
.seclist .pg{font:12px ui-monospace,Menlo,monospace;color:var(--faint);margin-top:5px}

/* article */
article.page{max-width:var(--w)}
.crumb{font:12px ui-monospace,Menlo,monospace;color:var(--faint);margin-bottom:10px}
article.page h1{font:600 clamp(28px,3.4vw,38px)/1.12 Charter,Georgia,serif;
  letter-spacing:-.02em;margin-bottom:22px}
article.page h2{font:600 21px/1.3 Charter,Georgia,serif;margin:34px 0 11px;
  padding-top:16px;border-top:1px solid var(--rule)}
article.page h3{font:600 17px/1.3 Charter,Georgia,serif;margin:22px 0 7px}
article.page p{margin-bottom:15px}
article.page ul,article.page ol{margin:0 0 16px 22px}
article.page li{margin-bottom:7px}
article.page blockquote{border-left:2px solid var(--accent);padding-left:16px;
  color:var(--soft);margin-bottom:16px}
article.page code{font-family:ui-monospace,Menlo,monospace;font-size:.86em;
  background:var(--card);border:1px solid var(--rule);border-radius:3px;padding:1px 5px}
article.page pre{background:var(--card);border:1px solid var(--rule);border-radius:4px;
  padding:14px 16px;overflow:auto;margin-bottom:17px}
article.page pre code{background:none;border:0;padding:0;font-size:13.5px;line-height:1.55}
article.page table{width:100%;border-collapse:collapse;margin-bottom:18px;font-size:14.5px}
article.page th{text-align:left;font-weight:600;padding:7px 10px 7px 0;
  border-bottom:1px solid var(--ink)}
article.page td{padding:8px 10px 8px 0;border-bottom:1px solid var(--rule);vertical-align:top}
article.page a.wiki{color:var(--accent);white-space:normal}
article.page a.wiki::before{content:"[[";color:var(--faint)}
article.page a.wiki::after{content:"]]";color:var(--faint)}
.pager{display:flex;gap:16px;justify-content:space-between;margin-top:46px;
  padding-top:18px;border-top:1px solid var(--rule);font-size:14px}
.pager a{max-width:46%}
.pager .lbl{display:block;font:11px ui-monospace,Menlo,monospace;color:var(--faint)}
.src{margin-top:34px;font:12px ui-monospace,Menlo,monospace;color:var(--faint)}

/* resources */
.rwrap{max-width:1180px;margin:0 auto;padding:34px 22px 90px}
.rwrap h1{font:600 clamp(30px,4vw,44px)/1.08 Charter,Georgia,serif;letter-spacing:-.025em}
.lede{max-width:62ch;color:var(--soft);margin:12px 0 24px;font-size:17px}
.controls{display:flex;flex-wrap:wrap;gap:9px;align-items:center;margin-bottom:8px;
  padding-bottom:18px;border-bottom:1px solid var(--rule)}
.chip{font:13px/1 ui-monospace,Menlo,monospace;background:var(--card);color:var(--soft);
  border:1px solid var(--rule);border-radius:20px;padding:7px 13px;cursor:pointer}
.chip.on{background:var(--accent);border-color:var(--accent);color:#F7F9F6}
.controls input{margin-left:auto;font:14px ui-monospace,Menlo,monospace;
  background:var(--card);border:1px solid var(--rule);border-radius:3px;padding:8px 11px;width:230px}
.count{font:12px ui-monospace,Menlo,monospace;color:var(--faint);padding:14px 0 4px}
.grp-h{font:600 15px/1 ui-monospace,Menlo,monospace;color:var(--faint);
  margin:26px 0 6px;padding-top:14px;border-top:1px solid var(--rule)}
.row{display:grid;grid-template-columns:minmax(180px,260px) 120px 1fr;gap:18px;
  padding:12px 0;border-bottom:1px solid var(--rule);align-items:baseline}
@media(max-width:760px){.row{grid-template-columns:1fr;gap:3px}}
.row .nm{font-weight:600;font-size:16px}
.row .mt{font:13px ui-monospace,Menlo,monospace;color:var(--num)}
.row .ds{color:var(--soft);font-size:15px}
.row .kd{font:11px ui-monospace,Menlo,monospace;color:var(--faint);display:block;margin-top:2px}
footer{border-top:1px solid var(--rule);padding:22px;text-align:center;
  font:12px ui-monospace,Menlo,monospace;color:var(--faint)}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""

SEARCHBOX = ('<div class="search"><input id="q" type="search" '
             'placeholder="search the guide" autocomplete="off">'
             '<div class="hits" id="hits"></div></div>')

def header(active):
    return f"""<header><div class="bar">
  <a class="brand" href="index.html">[[ second<span>brain</span>os ]]</a>
  <nav>
    <a href="index.html" class="{'on' if active=='guide' else ''}">Guide</a>
    <a href="resources.html" class="{'on' if active=='res' else ''}">Resources</a>
    <a href="{REPO}">Repo</a>
  </nav>
  {'<button class="toc-btn" id="toc">Index</button>' if active=='guide' else ''}
  {SEARCHBOX if active=='guide' else ''}
</div></header>"""

# ---------------- graph: sections on a ring in reading order, links as chords
import math
g = D["graph"]
order = list(D["sections"].keys())
CX, CY, RX, RY = 400, 232, 300, 150
pos = {}
for i, sec in enumerate(order):
    a = -math.pi/2 + 2*math.pi*i/len(order)
    pos[sec] = (CX + RX*math.cos(a), CY + RY*math.sin(a), a)

edges_svg = ""
for e in sorted(g["edges"], key=lambda e: e["w"]):
    x1, y1, _ = pos[e["a"]]; x2, y2, _ = pos[e["b"]]
    qx, qy = CX + (x1+x2-2*CX)*0.18, CY + (y1+y2-2*CY)*0.18
    edges_svg += (f'<path class="edge" d="M{x1:.0f},{y1:.0f} Q{qx:.0f},{qy:.0f} {x2:.0f},{y2:.0f}" '
                  f'stroke-width="{min(0.8+e["w"]*0.42, 3.4):.2f}" '
                  f'stroke-opacity="{min(0.35+e["w"]*0.12, 0.9):.2f}"/>')

nodes_svg = ""
for i, sec in enumerate(order):
    x, y, a = pos[sec]
    n = len([p for p in D["pages"] if p["section"] == sec])
    r = 8 + n*0.75
    cos = math.cos(a)
    anchor = "middle" if abs(cos) < 0.35 else ("start" if cos > 0 else "end")
    dx = 0 if anchor == "middle" else (r+9 if cos > 0 else -(r+9))
    dy = (r+18) if math.sin(a) > 0.35 else (-(r+12) if math.sin(a) < -0.35 else 5)
    nodes_svg += (f'<g class="node" data-sec="{sec}">'
                  f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}"/>'
                  f'<text x="{x+dx:.0f}" y="{y+dy:.0f}" text-anchor="{anchor}">'
                  f'{D["sections"][sec]["title"]}</text>'
                  f'<text class="cnt" x="{x+dx:.0f}" y="{y+dy+13:.0f}" text-anchor="{anchor}">{n} pages</text>'
                  f'<text class="idx" x="{x:.0f}" y="{y+3.5:.0f}" text-anchor="middle">{i+1}</text>'
                  f'</g>')

GRAPH = (f'<figure class="figure"><svg viewBox="0 0 800 470" role="img" '
         f'aria-label="The ten sections of the guide and the links between them">'
         f'{edges_svg}{nodes_svg}</svg>'
         f'<figcaption>The ten sections, in reading order, with the '
         f'{len(g["edges"])} places they reference each other. Thicker where they lean on '
         f'each other hardest. Click one to start there.</figcaption></figure>')

s = D["stats"]
STATS = f"""<div class="stats">
 <div class="stat"><b>{s['pages']}</b><span>pages</span></div>
 <div class="stat"><b>{s['sections']}</b><span>sections</span></div>
 <div class="stat"><b>{s['words']//1000}k</b><span>words</span></div>
 <div class="stat"><b>{s['links']}</b><span>vetted links</span></div>
 <div class="stat"><b>0</b><span>lock-in</span></div>
</div>"""

import re as _re
def inline(t):
    t = html.escape(t)
    return _re.sub(r"`([^`]+)`", r"<code>\1</code>", t)

seclist = ""
for sec, meta in D["sections"].items():
    first = D["order"][sec][0]
    seclist += (f'<article><h3><a href="#{first}">{html.escape(meta["title"])}</a></h3>'
                f'<p>{inline(meta["blurb"])}</p>'
                f'<div class="pg">{len(D["order"][sec])} pages</div></article>')

GUIDE = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Second Brain OS - the guide</title>
<meta name="description" content="A {s['pages']}-page guide to building a knowledge base your AI agent maintains, in plain markdown you own.">
<style>{CSS}</style></head><body>
{header('guide')}
<template id="hero"><div class="hero"><h1>A knowledge base your agent maintains</h1>
<p>Everything you read, watched and wrote, turned into linked pages and kept current by an agent. Plain markdown on your own machine.</p>
{GRAPH}{STATS}</div><div class="seclist">{seclist}</div></template>
<div class="wrap">
  <aside id="side"></aside>
  <main id="main"></main>
  <div class="rail" id="rail"></div>
</div>
<footer>Generated from the repository. <a href="{REPO}">github.com/undefined-ui/second-brain-os</a></footer>
<script id="data" type="application/json">{json.dumps({k:D[k] for k in ['pages','sections','order']})}</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);
const P={{}}; D.pages.forEach(p=>P[p.id]=p);
const FLAT=[]; Object.keys(D.order).forEach(s=>D.order[s].forEach(id=>FLAT.push(id)));
const HERO=document.getElementById('hero').innerHTML;

function side(cur){{
  const s=document.getElementById('side'); let h='';
  Object.keys(D.order).forEach((sec,i)=>{{
    const open = cur && cur.startsWith(sec);
    h+=`<div class="sec ${{open?'open':''}}" data-sec="${{sec}}">
      <button aria-expanded="${{!!open}}"><span class="k">${{String(i+1).padStart(2,'0')}}</span>
      ${{D.sections[sec].title}}<span class="n">${{D.order[sec].length}}</span></button><ol>`;
    D.order[sec].forEach(id=>{{
      h+=`<li><a href="#${{id}}" class="${{id===cur?'cur':''}}">${{P[id].title}}</a></li>`;
    }});
    h+='</ol></div>';
  }});
  s.innerHTML=h;
  s.querySelectorAll('.sec>button').forEach(b=>b.onclick=()=>{{
    const d=b.parentElement; d.classList.toggle('open');
    b.setAttribute('aria-expanded', d.classList.contains('open'));
  }});
}}

function render(){{
  const id=decodeURIComponent(location.hash.slice(1));
  const main=document.getElementById('main'), rail=document.getElementById('rail');
  if(!P[id]){{
    main.innerHTML=HERO; rail.innerHTML=''; side(null);
    main.querySelectorAll('svg .node').forEach(n=>n.onclick=()=>{{
      location.hash=D.order[n.dataset.sec][0];
    }});
    document.title='Second Brain OS - the guide';
    window.scrollTo(0,0); return;
  }}
  const p=P[id], i=FLAT.indexOf(id), prev=FLAT[i-1], next=FLAT[i+1];
  main.innerHTML=`<article class="page">
    <div class="crumb">${{p.section_title}} / page ${{D.order[p.section].indexOf(id)+1}} of ${{D.order[p.section].length}}</div>
    <h1>${{p.title}}</h1>${{p.html}}
    <div class="pager">
      ${{prev?`<a href="#${{prev}}"><span class="lbl">previous</span>${{P[prev].title}}</a>`:'<span></span>'}}
      ${{next?`<a href="#${{next}}" style="text-align:right"><span class="lbl">next</span>${{P[next].title}}</a>`:'<span></span>'}}
    </div>
    <div class="src">source: <a href="{REPO}/blob/main/${{p.path}}">${{p.path}}</a></div>
  </article>`;
  // rewrite internal links to hash routes, style them as wikilinks
  main.querySelectorAll('a[href$=".md"]').forEach(a=>{{
    if(/^https?:/.test(a.getAttribute('href'))) return;
    const parts=a.getAttribute('href').replace(/^\\.\\//,'').split('/');
    let target=null;
    const file=parts[parts.length-1].replace('.md','');
    if(file==='README'){{
      const sec=parts[parts.length-2]; if(D.order[sec]) target=D.order[sec][0];
    }} else {{
      const sec = parts.length>1 ? parts[parts.length-2] : p.section;
      const cand = sec+'/'+file;
      target = P[cand] ? cand : (P[p.section+'/'+file] ? p.section+'/'+file : null);
    }}
    if(target){{ a.setAttribute('href','#'+target); a.className='wiki'; }}
    else if(a.getAttribute('href').indexOf('..')===0 || !/^https?:/.test(a.getAttribute('href'))){{
      a.setAttribute('href','{REPO}/blob/main/'+a.getAttribute('href').replace(/^(\\.\\.\\/)+/,''));
    }}
  }});
  const heads=[...main.querySelectorAll('h2')];
  const outs=[...main.querySelectorAll('a.wiki')].slice(0,8);
  rail.innerHTML=(heads.length?`<div class="grp"><h4>on this page</h4>`+
      heads.map((h,n)=>{{h.id='h'+n;return `<a href="#${{id}}" onclick="document.getElementById('h${{n}}').scrollIntoView();return false">${{h.textContent}}</a>`}}).join('')+`</div>`:'')
    +(outs.length?`<div class="grp"><h4>links out</h4>`+
      outs.map(a=>`<a href="${{a.getAttribute('href')}}">${{a.textContent}}</a>`).join('')+`</div>`:'');
  side(id); document.title=p.title+' - Second Brain OS'; window.scrollTo(0,0);
}}

// search
const q=document.getElementById('q'), hits=document.getElementById('hits');
q.addEventListener('input',()=>{{
  const v=q.value.trim().toLowerCase();
  if(v.length<2){{hits.classList.remove('open');return;}}
  const r=D.pages.map(p=>{{
    let sc=0; const t=p.title.toLowerCase();
    if(t.includes(v)) sc+=10; if(t.startsWith(v)) sc+=6;
    const n=(p.text.toLowerCase().split(v).length-1); sc+=Math.min(n,6);
    return {{p,sc}};
  }}).filter(x=>x.sc>0).sort((a,b)=>b.sc-a.sc).slice(0,9);
  hits.innerHTML=r.length?r.map(x=>`<a class="hit" href="#${{x.p.id}}"><b>${{x.p.title}}</b><i>${{x.p.section_title}}</i></a>`).join('')
    :'<div class="hit"><i>nothing in the guide matches that</i></div>';
  hits.classList.add('open');
}});
q.addEventListener('keydown',e=>{{if(e.key==='Escape'){{q.value='';hits.classList.remove('open');q.blur();}}}});
document.addEventListener('click',e=>{{if(!e.target.closest('.search'))hits.classList.remove('open');}});
document.addEventListener('keydown',e=>{{
  if(e.key==='/'&&document.activeElement!==q){{e.preventDefault();q.focus();}}
  if(!P[decodeURIComponent(location.hash.slice(1))])return;
  const i=FLAT.indexOf(decodeURIComponent(location.hash.slice(1)));
  if(e.key==='ArrowRight'&&FLAT[i+1])location.hash=FLAT[i+1];
  if(e.key==='ArrowLeft'&&FLAT[i-1])location.hash=FLAT[i-1];
}});
hits.addEventListener('click',()=>{{hits.classList.remove('open');q.value='';}});
const toc=document.getElementById('toc');
if(toc){{toc.onclick=()=>document.getElementById('side').classList.toggle('show');}}
document.getElementById('side').addEventListener('click',e=>{{
  if(e.target.tagName==='A'&&innerWidth<=860) document.getElementById('side').classList.remove('show');
}});
addEventListener('hashchange',render); render();
</script></body></html>"""

open(f"{OUT}/index.html","w").write(GUIDE)

# ---------------- resources page
R = D["resources"]
kinds = []
for r in R:
    if r["kind"] not in kinds: kinds.append(r["kind"])

RES = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Second Brain OS - resources</title>
<meta name="description" content="{len(R)} checked links: Obsidian plugins by installs, repositories by stars, papers, tools and reading.">
<style>{CSS}</style></head><body>
{header('res')}
<div class="rwrap">
  <h1>Everything worth opening</h1>
  <p class="lede">{len(R)} links, each one checked. Plugins are ranked by installs from Obsidian's own community stats rather than by stars, because in this ecosystem the two disagree by an order of magnitude. Figures are from September 2026 and will drift.</p>
  <div class="controls" id="ctl">
    <button class="chip on" data-k="all">All</button>
    {"".join(f'<button class="chip" data-k="{html.escape(k)}">{html.escape(k)}</button>' for k in kinds)}
    <input id="rq" type="search" placeholder="filter" autocomplete="off">
  </div>
  <div class="count" id="count"></div>
  <div id="rows"></div>
</div>
<footer>Generated from the repository. <a href="{REPO}">github.com/undefined-ui/second-brain-os</a></footer>
<script id="rdata" type="application/json">{json.dumps(R)}</script>
<script>
const R=JSON.parse(document.getElementById('rdata').textContent);
let kind='all', term='';
function draw(){{
  const f=R.filter(r=>(kind==='all'||r.kind===kind) &&
    (!term || (r.name+' '+r.desc+' '+r.group).toLowerCase().includes(term)));
  document.getElementById('count').textContent=f.length+' of '+R.length+' shown';
  let h='', g=null;
  f.forEach(r=>{{
    const key=r.kind+' / '+r.group;
    if(key!==g){{g=key; h+=`<div class="grp-h">${{r.group||r.kind}}</div>`;}}
    h+=`<div class="row">
      <div><a class="nm" href="${{r.url}}">${{r.name}}</a><span class="kd">${{r.kind}}</span></div>
      <div class="mt">${{r.metric||''}}</div>
      <div class="ds">${{r.desc||''}}</div></div>`;
  }});
  document.getElementById('rows').innerHTML=h||'<div class="count">nothing matches that filter</div>';
}}
document.getElementById('ctl').addEventListener('click',e=>{{
  const b=e.target.closest('.chip'); if(!b)return;
  document.querySelectorAll('.chip').forEach(c=>c.classList.toggle('on',c===b));
  kind=b.dataset.k; draw();
}});
document.getElementById('rq').addEventListener('input',e=>{{term=e.target.value.trim().toLowerCase();draw();}});
draw();
</script></body></html>"""

open(f"{OUT}/resources.html","w").write(RES)
print("index.html", os.path.getsize(f"{OUT}/index.html")//1024, "KB |",
      "resources.html", os.path.getsize(f"{OUT}/resources.html")//1024, "KB")
