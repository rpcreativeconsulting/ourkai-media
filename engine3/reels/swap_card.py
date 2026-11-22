"""Swap the words on one type card of a finished Reel without touching anything else.

The card's ground is rebuilt from its source still with the same zoompan the build used,
so frames where the old card shows are replaced by clean ground + new card. Frames where the
old card is faint inside a cross-fade are recovered exactly from the known card alpha.
The audio is not touched (the output is silent; mux the Reel's sound afterwards).

python3 swap_card.py SRC.mp4 GROUND.png OLD_CARD.png NEW_CARD.png OUT.mp4 \
    --ground-start 16.54 --pure-from 17.34 --pure-to 21.44 --fade-in 17.2 0.7 --fade-out 20.9 0.5
"""
import argparse,subprocess,numpy as np
from PIL import Image
ap=argparse.ArgumentParser()
for a in ['src','ground','old','new','out']: ap.add_argument(a)
ap.add_argument('--ground-start',type=float,required=True)   # xfade offset where the ground clip begins
ap.add_argument('--pure-from',type=float,required=True)      # end of the incoming cross-fade
ap.add_argument('--pure-to',type=float,required=True)        # start of the outgoing cross-fade
ap.add_argument('--fade-in',type=float,nargs=2,required=True)
ap.add_argument('--fade-out',type=float,nargs=2,required=True)
ap.add_argument('--zoom',default="scale=2160:-2,crop=2160:3840,zoompan=z='1+0.06*on/132':d=132:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=24")
a=ap.parse_args()
W,H=1080,1920;FS=W*H*3
g=subprocess.run(['ffmpeg','-v','error','-loop','1','-t','6','-i',a.ground,'-vf',a.zoom+',format=rgb24','-frames:v','132','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True,check=True).stdout
cs=np.frombuffer(g,dtype=np.uint8).reshape(-1,H,W,3).astype(np.float32)
def card(p):
    im=np.asarray(Image.open(p).convert('RGBA')).astype(np.float32)/255;return im[...,:3]*255,im[...,3:4]
Cn,An=card(a.new);Co,Ao=card(a.old)
fi,fid=a.fade_in;fo,fod=a.fade_out
def fa(t):
    if t<fi: return 0.0
    if t<fi+fid: return (t-fi)/fid
    if t<fo: return 1.0
    if t<fo+fod: return 1-(t-fo)/fod
    return 0.0
dec=subprocess.Popen(['ffmpeg','-v','error','-i',a.src,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','24','-i','-','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-movflags','+faststart',a.out],stdin=subprocess.PIPE)
n=0;err=[]
while True:
    b=dec.stdout.read(FS)
    if len(b)<FS: break
    t=n/24;al=fa(t)
    if al>0:
        F=np.frombuffer(b,dtype=np.uint8).reshape(H,W,3).astype(np.float32)
        k=int(round((t-a.ground_start)*24))
        if a.pure_from<=t<=a.pure_to and 0<=k<len(cs):
            B=cs[k]
            if al==1.0: err.append(np.abs((B*(1-Ao)+Co*Ao)-F).mean())
        else:
            ao=Ao*al;B=(F-Co*ao)/np.maximum(1-ao,1e-3)
        an=An*al;b=np.clip(B*(1-an)+Cn*an+0.5,0,255).astype(np.uint8).tobytes()
    enc.stdin.write(b);n+=1
enc.stdin.close();enc.wait();dec.wait()
print(f'frames {n}; old card re-rendered over rebuilt ground vs original: mean abs diff {np.mean(err):.2f} (under ~4 = aligned)')
