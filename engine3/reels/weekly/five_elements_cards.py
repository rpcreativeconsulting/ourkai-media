import sys
sys.path.insert(0,'/home/claude/ourkai-media/engine3'); sys.path.insert(0,'/home/claude/ourkai-media/engine3/reels')
from cardlib import render
G='#d4af6e'; INK='#f5efe0'
LOCK='file:///home/claude/ourkai-media/media/brand/ourkai-lockup-vertical-tagline-gold-1200.png'
scrim='<div style="position:absolute;left:0;right:0;bottom:0;height:900px;background:linear-gradient(to bottom,rgba(10,9,8,0),rgba(10,9,8,.55) 55%,rgba(10,9,8,.75))"></div>'
def L(a,b): return scrim+(f'<div class="blk" style="bottom:470px;text-align:center"><div class="h" style="color:{INK};font-size:100px;line-height:1.05;text-shadow:0 4px 30px rgba(0,0,0,.6)">'
                          f'{a} <span style="color:{G}">{b}</span></div></div>')
c={}
c['l1']=L('Fire creates','Earth.')
c['l2']=L('Earth produces','Metal.')
c['l3']=L('Metal produces','Water.')
c['l4']=L('Water nourishes','Wood.')
c['l5']=L('Wood feeds','Fire.')
c['e1']=f'<div class="blk" style="top:800px;text-align:center"><div class="h" style="color:{INK};font-size:130px;line-height:1.05">Everything is<br>connected.</div></div>'
c['e2']=f'<div class="blk" style="top:1110px;text-align:center"><div class="h" style="color:{G};font-size:110px">Including you.</div></div>'
c['logo']=(f'<div style="position:absolute;inset:0;background:#0e0d0b"></div><img src="{LOCK}" style="position:absolute;left:50%;top:44%;width:340px;transform:translate(-50%,-50%)">'
           f'<div style="position:absolute;left:0;right:0;top:1260px;text-align:center"><div class="k" style="color:{G};font-size:34px;letter-spacing:.3em">COMMENT OURKAI</div></div>')
c['logo_fb']=c['logo'].replace('COMMENT OURKAI','OURKAI.IO')
render(c,'/home/claude/scratch/fe/f')
