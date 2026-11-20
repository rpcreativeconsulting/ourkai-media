import sys,os,subprocess
sys.path.insert(0,'/home/claude/relaunch/engine3')
from ourkai_type import css, REQUIRED
from playwright.sync_api import sync_playwright
FPS=24; DUR=5.5; N=int(FPS*DUR)
svg=open('lockup.svg').read().split('?>',1)[1]
html=f"""<html><head><meta charset=utf-8><style>{css()}
*{{margin:0}}body{{width:1080px;height:1920px;background:#0e0d0b;position:relative;overflow:hidden}}
#bg{{position:absolute;inset:0;background:#0e0d0b}}
#glow{{position:absolute;left:540px;top:700px;width:900px;height:900px;margin:-450px 0 0 -450px;border-radius:50%;
 background:radial-gradient(circle,rgba(212,175,110,.38) 0%,rgba(212,175,110,.14) 30%,rgba(212,175,110,0) 62%)}}
#logo{{position:absolute;left:190px;top:560px;width:700px}}
#logo svg{{width:700px;height:auto;display:block}}
#ask{{position:absolute;left:0;right:0;top:1330px;text-align:center;font-family:'oK Mono';font-weight:500;font-size:30px;letter-spacing:.26em;text-transform:uppercase;color:#d4af6e}}
</style></head><body><div id=bg></div><div id=logo>{svg}</div><div id=ask>Coming soon to the App Store</div>
<script>
const cl=x=>Math.max(0,Math.min(1,x)), ease=x=>{{x=cl(x);return 1-Math.pow(1-x,3)}};
function at(t){{
 const l=ease((t-0.3)/1.6);
 const L=document.getElementById('logo');L.style.opacity=l;L.style.transform=`scale(${{0.965+0.035*ease((t-0.5)/2.2)}})`;
 document.getElementById('ask').style.opacity=ease((t-2.6)/0.9);
}}
</script></body></html>"""
open('endcard.html','w').write(html)
os.makedirs('frames',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file:///home/claude/reels/shared/endcard.html')
    pg.evaluate("(req)=>Promise.all(req.map(f=>document.fonts.load(f,'Aǎ天'))).then(()=>document.fonts.ready)",REQUIRED)
    for i in range(N):
        pg.evaluate(f"at({i/FPS})")
        pg.screenshot(path=f'frames/{i:04d}.png')
    b.close()
subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(FPS),'-i','frames/%04d.png','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','endcard_v2.mp4'],check=True)
print('ok',N)
