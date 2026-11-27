import subprocess, librosa, numpy as np
y,sr=librosa.load('beat.mp3'); _,b=librosa.beat.beat_track(y=y,sr=sr,units='time')
p=float(np.median(np.diff(b))); g0=b[0]-p   # grid starting one beat before first detected
grid=lambda n: 0.0 if n==0 else g0+n*p
AUD=librosa.get_duration(y=y,sr=sr)
FPS=30
# (card, background grade, start beat)
seq=[('h1','gold',0),('h2','gold',1),('d1','earth',4),('d2','metal',6),('d3','metal',8),('d4','water',10),('d5','water',12),('d6','wood',14),('t1','gold',16),('t2','gold',20),('logo','gold',25)]
end=min(AUD,grid(27))
G={'gold':'eq=saturation=1.05','earth':'hue=h=-6:s=1.2,eq=gamma_b=0.92','metal':'hue=s=0.2,eq=brightness=0.03:contrast=1.08','water':'hue=h=175:s=1.15','wood':'hue=h=70:s=1.0'}
BG='/home/claude/scratch/reel/bg_pp.mp4'
offs=[1,3,0,9,15,6,20,12,24,4,0]
inp=[];fc=[];segs=[]
for i,(k,gr,sb) in enumerate(seq):
    s=grid(sb); e=grid(seq[i+1][2]) if i+1<len(seq) else end
    n=round((e-s)*FPS); segs.append((k,s,n))
    inp+=['-stream_loop','-1','-i',BG]
    fc.append(f"[{i}:v]trim={offs[i]}:{offs[i]+n/FPS+0.5},setpts=PTS-STARTPTS,scale=1620:2880,zoompan=z='1+0.12*pow(1-on/{n},3)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps={FPS},{G[gr]},trim=end_frame={n},setpts=PTS-STARTPTS,format=yuv420p[g{i}]")
fc.append(''.join(f'[g{i}]' for i in range(len(seq)))+f'concat=n={len(seq)}:v=1[bg]')
prev='bg'; base=len(seq)
for i,(k,s,n) in enumerate(segs):
    inp+=['-loop','1','-t',f'{n/FPS:.3f}','-i',f'f/{k}.png']
    fi='' if i==0 else 'fade=t=in:st=0:d=0.1:alpha=1,'
    fc.append(f'[{base+i}:v]format=rgba,{fi}setpts=PTS+{s:.4f}/TB[c{i}]')
    fc.append(f"[{prev}][c{i}]overlay=eof_action=pass:enable='between(t,{s:.4f},{s+n/FPS:.4f})'[v{i}]"); prev=f'v{i}'
inp+=['-i','beat.mp3']
fc.append(f'[{base+len(segs)}:a]atrim=0:{end},afade=t=out:st={end-0.4}:d=0.4[a]')
subprocess.run(['ffmpeg','-y','-v','error']+inp+['-filter_complex',';'.join(fc),'-map',f'[{prev}]','-map','[a]','-t',f'{end:.3f}','-r',str(FPS),'-c:v','libx264','-crf','18','-preset','veryfast','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart','R-week_v6_fast.mp4'],check=True)
print('tempo',60/p,'end',end,' '.join(f'{s+n/FPS/2:.2f}' for k,s,n in segs))
