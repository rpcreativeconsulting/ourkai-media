import sys
sys.path.insert(0,'/home/claude/ourkai-media/engine3'); sys.path.insert(0,'/home/claude/ourkai-media/engine3/reels')
from cardlib import render
G='#d4af6e'; INK='#f5efe0'
LOCK='file:///home/claude/ourkai-media/media/brand/ourkai-lockup-vertical-tagline-gold-1200.png'
def end(q,act,after):
    return (f'<div style="position:absolute;inset:0;background:#0e0d0b"></div>'
      f'<div class="blk" style="top:470px;text-align:center"><div class="h" style="color:{INK};font-size:92px;line-height:1.05">{q}</div></div>'
      f'<img src="{LOCK}" style="position:absolute;left:50%;top:860px;width:280px;transform:translateX(-50%)">'
      f'<div style="position:absolute;left:0;right:0;top:1440px;text-align:center"><div class="k" style="color:{G};font-size:34px;letter-spacing:.28em">{act}</div>'
      f'<div class="b" style="color:#cfc6ae;font-size:36px;margin-top:22px">{after}</div></div>')
c={'fe_ig':end(f'Want to know<br><span style="color:{G}">your mix?</span>','COMMENT OURKAI','Get notified when we release the app.'),
   'fe_fb':end(f'Want to know<br><span style="color:{G}">your mix?</span>','OURKAI.IO','Get notified when we release the app.'),
   'r4_ig':end(f'Want to see<br><span style="color:{G}">who feeds you?</span>','COMMENT OURKAI','Get notified when we release the app.'),
   'r4_fb':end(f'Want to see<br><span style="color:{G}">who feeds you?</span>','OURKAI.IO','Get notified when we release the app.')}
render(c,'/home/claude/scratch/endwhy/f')
