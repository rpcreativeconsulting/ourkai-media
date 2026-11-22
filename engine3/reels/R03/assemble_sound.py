"""R03 natural soundscape: light assembly only (Ryan, Nov 22, option 1).
Each scene bed is used as generated; the only changes are one flat level per bed,
a short fade at each edge (0.15 s each side = 0.3 s cross-fade across the cut), a 0.5 s fade-in at frame 1,
and placing the beds end to end. No filters, no compression, no reshaping."""
import subprocess,numpy as np,json
SR=48000
BEDS=[ # file, start, length (scene boundaries = middle of each picture cross-fade)
 ('snd/R03_scene_A_wood_v1.wav',0.00,6.25),
 ('snd/R03_scene_B_fire_v2.wav',6.25,3.84),
 ('snd/R03_scene_C_earth_v1.wav',10.09,3.84),
 ('snd/R03_scene_D_metal_v3.mp3',13.93,3.84),
 ('snd/R03_scene_E_water_v1.wav',17.77,3.84),
 ('snd/R03_scene_F_question-end_v3.mp3',21.61,9.06),
]
TOTAL=30.667;TARGET_RMS=-24.0;PEAK_CAP=-4.5;EDGE=0.15
def load(p):
    b=subprocess.run(['ffmpeg','-v','error','-i',p,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True,check=True).stdout
    return np.frombuffer(b,dtype=np.float32).astype(np.float64)
out=np.zeros(int(TOTAL*SR)+SR);log=[]
for i,(p,st,ln) in enumerate(BEDS):
    x=load(p)[:int(ln*SR)]
    rms=20*np.log10(np.sqrt((x**2).mean())+1e-12);pk=20*np.log10(np.abs(x).max()+1e-12)
    g=min(TARGET_RMS-rms,PEAK_CAP-pk)              # one flat level per bed
    x=x*10**(g/20)
    e=int(EDGE*SR);ramp=np.linspace(0,1,e)
    fin=int(0.5*SR) if i==0 else e
    x[:fin]*=np.linspace(0,1,fin)                  # edge fades only
    if i<len(BEDS)-1: x[-e:]*=ramp[::-1]
    s=int(st*SR);out[s:s+len(x)]+=x
    log.append(dict(bed=p,gain_db=round(g,1),rms_after=round(rms+g,1),peak_after=round(pk+g,1)))
out=out[:int(TOTAL*SR)]
pcm=(np.clip(out,-1,1)*32767).astype(np.int16).tobytes()
subprocess.run(['ffmpeg','-v','error','-y','-f','s16le','-ar',str(SR),'-ac','1','-i','-','snd/R03_snd_assembled_v1.wav'],input=pcm,check=True)
print(json.dumps(log,indent=1))
print('overall peak %.1f dBFS'%(20*np.log10(np.abs(out).max())))
