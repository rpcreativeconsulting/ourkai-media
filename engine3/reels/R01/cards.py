import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
WORK = _os.environ.get('OURKAI_WORK', '/home/claude/work')
import sys
sys.path.insert(0,_os.path.normpath(_os.path.join(_HERE, '../..')))
from ourkai_type import css, REQUIRED, DARK, LIGHT
from playwright.sync_api import sync_playwright
W,H=1080,1920
BASE="""*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1920px;background:transparent;position:relative;overflow:hidden}
.blk{position:absolute;left:96px;right:96px}
.k{font-family:'oK Mono';font-weight:400;font-size:30px;letter-spacing:.24em;text-transform:uppercase}
.r{width:56px;height:3px;margin:22px 0 34px}
.h{font-family:'oK Fraunces';font-style:italic;font-weight:300;font-size:104px;line-height:1.06;letter-spacing:-.025em;font-variation-settings:'opsz' 144}
.h.m{font-size:84px}
.b{font-family:'oK Source Serif';font-weight:400;font-size:46px;line-height:1.45;margin-top:30px;font-variation-settings:'opsz' 20}
.a{font-family:'oK Fraunces';font-style:italic;font-weight:400;font-variation-settings:'opsz' 72}
.py{font-family:'oK Source Serif';font-style:italic;font-weight:500}
.cta{font-family:'oK Mono';font-weight:500;font-size:30px;letter-spacing:.26em;text-transform:uppercase;margin-top:56px}
"""
def card(dark,bottom=None,top=None,center=False,kicker=None,head=None,hm=False,body=None,accent=None,cta=None):
    c=DARK if dark else LIGHT
    gold=c['accent'] if dark else c['accent_large']
    pos=f"bottom:{bottom}px" if bottom is not None else f"top:{top}px"
    al="text-align:center;" if center else ""
    s=f'<div class="blk" style="{pos};{al}">'
    if kicker: s+=f'<div class="k" style="color:{c["soft"]}">{kicker}</div><div class="r" style="background:{gold};{"margin-left:auto;margin-right:auto" if center else ""}"></div>'
    if head: s+=f'<div class="h{" m" if hm else ""}" style="color:{c["head"]}">{head}</div>'
    if body:
        acc=f' <span class="a" style="color:{gold if dark else c["head"]}">{accent}</span>' if accent else ''
        s+=f'<div class="b" style="color:{c["body"]}">{body}{acc}</div>'
    if cta: s+=f'<div class="cta" style="color:{gold}">{cta}</div>'
    return s+'</div>'
CARDS={
 'c1':card(False,bottom=470,kicker='Timing',head='Same sky.<br>A different day<br>for everyone.'),
 'c2':card(False,bottom=470,head='Everyone wakes up<br>to the same date.',hm=True),
 'c3':card(False,bottom=470,head='Each day is one pillar.',hm=True,body='In Chinese timing, the days turn through a cycle of sixty, the',accent='<span class="py">Jiǎzǐ</span>.'),
 'c4':card(False,bottom=470,head='It meets every chart differently.',hm=True,body='The day that pushes one person forward',accent='asks another to wait.'),
 'c5':card(True,top=700,center=True,kicker='Your turn',head='How is today<br>meeting you?',cta='Comment one word'),
 'c6':'<div class="blk" style="top:1330px;text-align:center"><div class="b" style="color:#b0a78f;font-size:40px">Coming soon to the App Store.</div></div>',
}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':W,'height':H})
    for k,v in CARDS.items():
        open(f'{WORK}/reels/R01/cards/{k}.html','w').write(f'<html><head><meta charset="utf-8"><style>{css()}{BASE}</style></head><body>{v}</body></html>')
        pg.goto(f'file://{WORK}/reels/R01/cards/{k}.html')
        pg.evaluate("(req)=>Promise.all(req.map(f=>document.fonts.load(f,'Aǎ天'))).then(()=>document.fonts.ready)",REQUIRED)
        pg.wait_for_timeout(300)
        miss=pg.evaluate("(req)=>req.filter(f=>!document.fonts.check(f,'Aǎ天'))",REQUIRED)
        if miss: raise SystemExit(f'font lock failed {miss}')
        pg.screenshot(path=f'{WORK}/reels/R01/cards/{k}.png',omit_background=True)
    b.close()
print('cards ok')
