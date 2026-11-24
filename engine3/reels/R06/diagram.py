"""R06 four-pillar diagram, frame by frame (transparent PNGs, 24 fps, from T0 to T1 of the Reel).
Columns read right to left, as a chart is written: Year, Month, Day, Hour. Each pillar: a stem square over a branch square.
Beat 2 (4.3 s): pillars draw in from the right. Beat 3 (8.9 s): the eight squares fill. Beat 4 (13.7 s): the day stem (the Day Master) lights; the rest dim."""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, '..')))
from cardlib import page, check_fonts
WORK = os.environ.get('OURKAI_WORK', '/home/claude/work')
OUT = f'{WORK}/reels/R06/dia'
FPS, T0, T1 = 24, 3.6, 18.2
GOLD = '212,175,110'
cols = [('時', 'Hour'), ('日', 'Day'), ('月', 'Month'), ('年', 'Year')]  # left to right on screen
CW, GAP, X0, Y0, SQ, SG = 180, 56, 96, 380, 180, 24
parts = []
for i, (zh, en) in enumerate(cols):
    x = X0 + i * (CW + GAP)
    parts.append(f'<div class="col" id="c{i}" style="left:{x}px;top:{Y0}px">'
                 f'<div class="zh hz">{zh}</div><div class="lab">{en}</div>'
                 f'<svg width="{SQ}" height="{2*SQ+SG}" style="display:block;margin-top:30px;overflow:visible">'
                 f'<rect id="s{i}" class="sq" x="1.5" y="1.5" width="{SQ-3}" height="{SQ-3}"/>'
                 f'<rect id="b{i}" class="sq" x="1.5" y="{SQ+SG+1.5}" width="{SQ-3}" height="{SQ-3}"/></svg>'
                 + ('<div id="dm" class="dm">Day<br>Master</div>' if en == 'Day' else '') + '</div>')
CSS = f"""
.col{{position:absolute;width:{CW}px;text-align:center}}
.hz{{font-size:78px;line-height:1;color:rgb({GOLD})}}
.lab{{font-family:'oK Mono';font-weight:400;font-size:24px;letter-spacing:.22em;text-transform:uppercase;color:#b0a78f;margin-top:16px}}
.sq{{fill:rgba({GOLD},0);stroke:rgb({GOLD});stroke-width:2;stroke-dasharray:{4*(SQ-3)};stroke-dashoffset:{4*(SQ-3)}}}
.dm{{position:absolute;left:0;width:{CW}px;top:{78+16+30+24+30+SQ/2-28}px;font-family:'oK Mono';font-weight:400;font-size:20px;letter-spacing:.22em;line-height:1.4;text-transform:uppercase;color:#0e0d0b;opacity:0}}
"""
JS = f"""<script>
const cl=x=>Math.max(0,Math.min(1,x)), ease=x=>{{x=cl(x);return 1-Math.pow(1-x,3)}};
const P={4*(SQ-3)};
function at(t){{
  const out=1-ease((t-17.6)/0.55);
  for(let i=0;i<4;i++){{
    const k=3-i;                       // Year (right) draws first
    const d=ease((t-(4.3+k*0.6))/0.9);
    const col=document.getElementById('c'+i);
    const dim=(i==1)?1:1-0.55*ease((t-13.7)/0.8);
    col.style.opacity=(cl((t-(4.3+k*0.6))/0.5))*dim*out;
    for(const [id,j] of [['s'+i,0],['b'+i,1]]){{
      const r=document.getElementById(id);
      r.style.strokeDashoffset=P*(1-d);
      const f=ease((t-(8.9+(k*2+j)*0.28))/0.6);
      let a=0.16*f;
      if(i==1&&j==0){{ const m=ease((t-13.7)/0.8); a=a+(0.72-a)*m; r.style.strokeWidth=2+1.5*m; }}
      r.style.fill=`rgba({GOLD},${{a}})`;
    }}
  }}
  document.getElementById('dm').style.opacity=ease((t-14.2)/0.7)*out;
}}
</script>"""
html = page('<div id="root">' + ''.join(parts) + '</div>' + JS, CSS)
os.makedirs(OUT, exist_ok=True)
open(f'{OUT}/diagram.html', 'w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto(f'file://{OUT}/diagram.html')
    check_fonts(pg)
    n = int(round((T1 - T0) * FPS))
    for i in range(n):
        pg.evaluate(f'at({T0 + i / FPS})')
        pg.screenshot(path=f'{OUT}/{i:04d}.png', omit_background=True)
    b.close()
print('diagram frames', n)
