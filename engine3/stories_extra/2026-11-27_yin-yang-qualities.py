import sys
sys.path.insert(0,'/home/claude/ourkai-media/engine3'); sys.path.insert(0,'/home/claude/ourkai-media/engine3/reels')
from cardlib import render
G='#d4af6e'; INK='#f5efe0'; SOFT='#cfc6ae'
yang=['Outgoing','Always on the go','Starts things','Talks it out','Up with the sun','Says yes first']
yin=['Inward','Needs a nap','Finishes things','Thinks it through','Up past midnight','Says “let me think”']
def col(title,items,align):
    li=''.join(f'<div style="font-family:\'oK Source Serif\';font-size:44px;line-height:1.25;color:#efe7d2;margin-top:22px">{x}</div>' for x in items)
    return f'<div style="flex:1;text-align:{align}"><div class="k" style="color:{G};font-size:30px;letter-spacing:.3em">{title}</div><div style="width:48px;height:2px;background:{G};margin:18px 0 0 {"auto" if align=="right" else "0"}"></div>{li}</div>'
html=(f'<img src="file:///home/claude/work/bg/slate.png" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'
 f'<div class="blk" style="top:290px"><div class="k" style="color:{SOFT};font-size:28px;letter-spacing:.26em">FIND YOURSELF</div>'
 f'<div style="width:56px;height:3px;background:{G};margin:22px 0 30px"></div>'
 f'<div class="h" style="color:{INK};font-size:104px;line-height:1.02">Are you <span style="color:{G}">more</span><br>Yin or Yang?</div></div>'
 f'<div style="position:absolute;left:96px;right:96px;top:700px;display:flex;gap:40px">{col("YANG",yang,"left")}<div style="width:1px;background:rgba(245,239,224,.18)"></div>{col("YIN",yin,"right")}</div>'
 f'<div class="blk" style="top:1270px"><div class="b" style="color:{SOFT};font-size:40px;margin:0">Everyone has both. <span class="a" style="color:{G}">Your chart shows your mix.</span></div></div>')
render({'1':html},'/home/claude/scratch/yy/f')
