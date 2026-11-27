import sys
sys.path.insert(0,'/home/claude/ourkai-media/engine3'); sys.path.insert(0,'/home/claude/ourkai-media/engine3/reels')
from cardlib import render
G='#d4af6e'; INK='#f5efe0'
LOCK='file:///home/claude/ourkai-media/media/brand/ourkai-lockup-vertical-tagline-gold-1200.png'
sh='<div style="position:absolute;inset:0;background:radial-gradient(ellipse 90% 40% at 50% 50%,rgba(10,9,8,.5),rgba(10,9,8,0) 80%)"></div>'
def H(t,s,top,c=INK): return f'<div class="blk" style="top:{top}px;text-align:center"><div class="h" style="color:{c};font-size:{s}px;line-height:1;text-shadow:0 6px 40px rgba(0,0,0,.65)">{t}</div></div>'
def K(t,top,c='#efe7d2',s=30): return f'<div style="position:absolute;left:0;right:0;top:{top}px;text-align:center"><div class="k" style="color:{c};font-size:{s}px;letter-spacing:.3em;text-shadow:0 2px 16px rgba(0,0,0,.7)">{t}</div></div>'
c={}
c['hook']=sh+H(f'You&#39;re made of<br>five elements.',140,800)
for k,(n,s,v) in {'fire':('Fire','Summer','Courtesy'),'earth':('Earth','Between seasons','Trust'),'metal':('Metal','Autumn','Integrity'),
                 'water':('Water','Winter','Wisdom'),'wood':('Wood','Spring','Kindness')}.items():
    c[k]=sh+H(n,190,820)+K(f'{s} · {v}',1040)
c['end1']=H(f'You&#39;re all five.',140,780)+H(f'<span style="color:{G}">The mix is yours.</span>',110,960)
c['end2']=(f'<div style="position:absolute;inset:0;background:#0e0d0b"></div><img src="{LOCK}" style="position:absolute;left:50%;top:44%;width:340px;transform:translate(-50%,-50%)">'
           +K('COMMENT OURKAI',1260,G,34))
render(c,'/home/claude/scratch/el/f')
