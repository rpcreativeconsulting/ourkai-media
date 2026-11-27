import sys
sys.path.insert(0,'/home/claude/ourkai-media/engine3'); sys.path.insert(0,'/home/claude/ourkai-media/engine3/reels')
from cardlib import render
G='#d4af6e'; INK='#f5efe0'
LOCK='file:///home/claude/ourkai-media/media/brand/ourkai-lockup-vertical-tagline-gold-1200.png'
sh='<div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(10,9,8,.3),rgba(10,9,8,0) 30%,rgba(10,9,8,.35) 55%,rgba(10,9,8,.8) 80%,rgba(10,9,8,.9))"></div>'
shc='<div style="position:absolute;inset:0;background:radial-gradient(ellipse 85% 45% at 50% 52%,rgba(10,9,8,.6),rgba(10,9,8,.15) 80%)"></div>'
def H(t,s=150,top=1120,c=INK): return f'<div class="blk" style="top:{top}px;text-align:center"><div class="h" style="color:{c};font-size:{s}px;line-height:1;text-shadow:0 6px 40px rgba(0,0,0,.6)">{t}</div></div>'
def B(t,top,s=50): return f'<div class="blk" style="top:{top}px;text-align:center"><div class="b" style="color:#efe7d2;font-size:{s}px;line-height:1.35;margin:0;text-shadow:0 3px 24px rgba(0,0,0,.6)">{t}</div></div>'
def K(t,top,c=G,s=28): return f'<div style="position:absolute;left:0;right:0;top:{top}px;text-align:center"><div class="k" style="color:{c};font-size:{s}px;letter-spacing:.3em">{t}</div></div>'
c={}
c['c1']=sh+H('Waiting to<br>start?',170,1040)
c['c2']=sh+H(f'Start <span style="color:{G}">Tuesday.</span>',170,1120)
c['c3a']=sh+K('TUE · DEC 1',330,'rgba(245,239,224,.8)')+H('Open.',320,620,G)
c['c3b']=B('One of twelve kinds of day<br>in the Chinese almanac.',1010)+K('IN USE FOR 2,000+ YEARS',1170)
c['c3c']=B('Open days are made<br>for beginnings.',1010,56)
for i,w in enumerate(['Launch it.','Sign up.','Book it.']):
    c[f'c4{i}']=sh+H(w,200,1100)
c['c5']=shc+H(f'Same day.<br><span style="color:{G}">Different for you.</span>',130,780)+B('Your element. Your hour. Your year.',1110,46)
c['c6']=shc+H(f'oürkai reads<br>it for <span style="color:{G}">you.</span>',140,760)+K('COMMENT OURKAI',1130,G,34)
c['c7']=f'<div style="position:absolute;inset:0;background:#0e0d0b"></div><img src="{LOCK}" style="position:absolute;left:50%;top:47%;width:340px;transform:translate(-50%,-50%)">'
render(c,'/home/claude/scratch/r1/f')
