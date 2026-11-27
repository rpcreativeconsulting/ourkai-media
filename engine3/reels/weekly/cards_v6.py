import sys
sys.path.insert(0,'/home/claude/ourkai-media/engine3'); sys.path.insert(0,'/home/claude/ourkai-media/engine3/reels')
from cardlib import render
G='#d4af6e'; INK='#f5efe0'; SOFT='#cfc6ae'
LOCK='file:///home/claude/ourkai-media/media/brand/ourkai-lockup-vertical-tagline-gold-1200.png'
veil='<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 48%,rgba(14,13,11,.62),rgba(14,13,11,.35) 70%),linear-gradient(to bottom,rgba(14,13,11,.25),rgba(14,13,11,0) 30%,rgba(14,13,11,.0) 70%,rgba(14,13,11,.55))"></div>'
def H(t,size=150): return f'<div class="h" style="color:{INK};font-size:{size}px;line-height:1.0;text-shadow:0 4px 40px rgba(0,0,0,.45)">{t}</div>'
def K(t,c=G): return f'<div class="k" style="color:{c};font-size:32px;letter-spacing:.28em">{t}</div>'
def blk(inner,top=700): return f'<div class="blk" style="top:{top}px;text-align:center">{inner}</div>'
c={}
c['h1']=veil+blk(H('Not every day',160),760)
c['h2']=veil+blk(H('Not every day',160)+H(f'is for <span style="color:{G}">everything.</span>',160),700)
days=[('TUE · DEC 1','Start<br>something.','OPEN DAY · EARTH'),
      ('WED · DEC 2','Finish<br>something.','CLOSE DAY · METAL'),
      ('THU · DEC 3','Make<br>the plan.','ESTABLISH DAY · METAL'),
      ('FRI · DEC 4','Clear<br>it out.','REMOVE DAY · WATER'),
      ('SAT · DEC 5','Gather<br>and receive.','FULL DAY · WATER'),
      ('SUN + MON','Talk it<br>through.','BALANCE DAYS · WOOD')]
for i,(k,h,s) in enumerate(days,1):
    c[f'd{i}']=veil+blk(K(k)+'<div style="height:48px"></div>'+H(h,170)+'<div style="height:52px"></div>'+K(s,SOFT),640)
c['t1']=veil+blk(H(f"That's <span style='color:{G}'>everyone's</span> week.",130)+
   f'<div class="b" style="color:#e6dec8;font-size:50px;margin-top:44px">Yours depends on your element,<br>your hour, your year.</div>',700)
c['t2']=veil+blk(H(f'oürkai shows you how<br>to make the most<br>of <span style="color:{G}">your</span> day.',112)+
   f'<div class="b" style="color:#e6dec8;font-size:50px;margin-top:36px">Every day.</div>'
   f'<div class="cta" style="color:{G};font-size:30px;letter-spacing:.2em;margin-top:64px">Comment OURKAI to get notified</div>',640)
c['logo']=f'<div style="position:absolute;inset:0;background:#0e0d0b"></div><img src="{LOCK}" style="position:absolute;left:50%;top:50%;width:560px;transform:translate(-50%,-50%)">'
render(c,'/home/claude/scratch/v6/f')
