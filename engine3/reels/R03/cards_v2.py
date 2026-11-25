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
.zh{font-family:'oK Noto SC';font-size:150px;line-height:1;margin-bottom:34px}
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
 'c1':card(True,bottom=470,kicker='The five elements',head="You've heard of<br>Chinese medicine.",hm=True,body='Few know the five elements',accent='it rests on.'),
 'c2':'<div class="blk" style="bottom:470px"><div class="zh" style="color:#d4af6e">木</div><div class="h m" style="color:#f5efe0">Wood grows.</div><div class="b" style="color:#e6dec8"><span class="py">Mù</span> · <span class="a" style="color:#d4af6e">spring, and the east</span></div></div>',
 'c3':'<div class="blk" style="bottom:470px"><div class="zh" style="color:#d4af6e">火</div><div class="h m" style="color:#f5efe0">Fire peaks.</div><div class="b" style="color:#e6dec8"><span class="py">Huǒ</span> · <span class="a" style="color:#d4af6e">the heart, in the classical map</span></div></div>',
 'c4':'<div class="blk" style="bottom:470px"><div class="zh" style="color:#d4af6e">土</div><div class="h m" style="color:#f5efe0">Earth steadies.</div><div class="b" style="color:#e6dec8"><span class="py">Tǔ</span> · <span class="a" style="color:#d4af6e">the turn of every season</span></div></div>',
 'c5':'<div class="blk" style="bottom:470px"><div class="zh" style="color:#d4af6e">金</div><div class="h m" style="color:#f5efe0">Metal gathers.</div><div class="b" style="color:#e6dec8"><span class="py">Jīn</span> · <span class="a" style="color:#d4af6e">its virtue is righteousness</span></div></div>',
 'c6':'<div class="blk" style="bottom:470px"><div class="zh" style="color:#d4af6e">水</div><div class="h m" style="color:#f5efe0">Water rests.</div><div class="b" style="color:#e6dec8"><span class="py">Shuǐ</span> · <span class="a" style="color:#d4af6e">it stores the will</span></div></div>',
 'c7':card(True,top=700,center=True,kicker='Your turn',head='Which one<br>sounds like you?',cta='Send this to someone who needs it'),
 'scrim':'<div style="position:absolute;left:0;right:0;bottom:0;height:1250px;background:linear-gradient(to bottom,rgba(14,13,11,0) 0%,rgba(14,13,11,.55) 45%,rgba(14,13,11,.8) 100%)"></div>',
}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':W,'height':H})
    for k,v in CARDS.items():
        open(f'{WORK}/reels/R03/cards_v2/{k}.html','w').write(f'<html><head><meta charset="utf-8"><style>{css()}{BASE}</style></head><body>{v}</body></html>')
        pg.goto(f'file://{WORK}/reels/R03/cards_v2/{k}.html')
        pg.evaluate("(req)=>Promise.all(req.map(f=>document.fonts.load(f,'Aǎ天'))).then(()=>document.fonts.ready)",REQUIRED)
        pg.wait_for_timeout(300)
        miss=pg.evaluate("(req)=>req.filter(f=>!document.fonts.check(f,'Aǎ天'))",REQUIRED)
        if miss: raise SystemExit(f'font lock failed {miss}')
        pg.screenshot(path=f'{WORK}/reels/R03/cards_v2/{k}.png',omit_background=True)
    b.close()
print('cards ok')
