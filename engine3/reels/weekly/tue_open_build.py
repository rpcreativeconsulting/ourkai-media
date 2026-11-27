import subprocess
FPS=30; W,H=1080,1920
C='clips/'
END=16.4
cuts=[0,1.88,3.62,7.06,7.82,8.57,9.33,13.12,14.8,END]
def n(i): return round((cuts[i+1]-cuts[i])*FPS)
inp=[];fc=[]
def push(z=0.05,i=0): return f"scale=1620:2880:flags=lanczos,zoompan=z='1+{z}*on/{n(i)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}"
def fit(): return f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}"
segs=[]
# S0 door still
inp+=['-loop','1','-i','/home/claude/scratch/sb/src/door.png']; segs.append(f"[0:v]{fit()},{push(0.04,0)},trim=end_frame={n(0)},setpts=PTS-STARTPTS,setsar=1,format=yuv420p[s0]")
# S1 door opening (sped)
inp+=['-i',C+'door.mp4']; segs.append(f"[1:v]setpts=0.42*PTS,{fit()},trim=end_frame={n(1)},setpts=PTS-STARTPTS,setsar=1,format=yuv420p[s1]")
# S2 earth
inp+=['-i',C+'earth.mp4']; segs.append(f"[2:v]{fit()},{push(0.06,2)},trim=end_frame={n(2)},setpts=PTS-STARTPTS,setsar=1,format=yuv420p[s2]")
for j,(f,o) in enumerate([('note.mp4',1.6),('key.mp4',1.0),('cal.mp4',1.8)]):
    k=3+j; inp+=['-ss',str(o),'-i',C+f]; segs.append(f"[{k}:v]{fit()},{push(0.08,k)},trim=end_frame={n(k)},setpts=PTS-STARTPTS,setsar=1,format=yuv420p[s{k}]")
# S6 five strips
base=6
for j,f in enumerate(['earth','metal','water','wood','fire']):
    inp+=['-stream_loop','-1','-i',C+f+'.mp4']
    lit=f"between(t,{0.38*j:.2f},{0.38*(j+1):.2f})"
    segs.append(f"[{base+j}:v]fps={FPS},scale=-2:{H},crop=216:{H},setsar=1,drawbox=x=0:y=0:w=iw:h=ih:color=black@0.55:t=fill:enable='lt(t,1.9)*not({lit})',drawbox=x=0:y=0:w=iw:h=ih:color=black@0.5:t=fill:enable='gte(t,1.9)'[p{j}]")
segs.append(''.join(f'[p{j}]' for j in range(5))+f"hstack=inputs=5,trim=end_frame={n(6)},setpts=PTS-STARTPTS,setsar=1,format=yuv420p[s6]")
# S7 gold flow
inp+=['-stream_loop','-1','-i','/home/claude/scratch/reel/bg_pp.mp4']; k=base+5
segs.append(f"[{k}:v]trim=6:12,setpts=PTS-STARTPTS,{fit()},trim=end_frame={n(7)},setpts=PTS-STARTPTS,setsar=1,format=yuv420p[s7]")
# S8 black for logo
segs.append(f"color=c=0x0e0d0b:s={W}x{H}:r={FPS}:d={n(8)/FPS:.3f},setsar=1,format=yuv420p[s8]")
fc+=segs+[''.join(f'[s{i}]' for i in range(9))+'concat=n=9:v=1[bg]']
idx=k+1; prev='bg'; L=0
def add(png,st,en,slide=28,fade=0.22):
    global idx,prev,L
    inp.extend(['-loop','1','-t',f'{en-st:.3f}','-i',f'f/{png}.png'])
    y=f"if(lt(t-{st:.3f},0.4),{slide}*pow(1-(t-{st:.3f})/0.4,2),0)"
    fc.extend([f'[{idx}:v]format=rgba,fade=t=in:st=0:d={fade}:alpha=1,setpts=PTS+{st:.3f}/TB[l{L}]',
               f"[{prev}][l{L}]overlay=x=0:y='{y}':eval=frame:eof_action=pass:enable='between(t,{st:.3f},{en:.3f})'[o{L}]"])
    prev=f'o{L}'; idx+=1; L+=1
add('c1',0.15,1.88)
add('c2',2.15,3.62)
add('c3a',3.62,7.06,40)
add('c3b',4.45,5.85,20)
add('c3c',5.85,7.06,20)
add('c40',7.06,7.82,24,0.12); add('c41',7.82,8.57,24,0.12); add('c42',8.57,9.33,24,0.12)
add('c5',11.25,13.12,30)
add('c6',13.12,14.8,30)
add('c7',14.8,END,0,0.3)
inp+=['-i','/home/claude/scratch/v7/music.mp3','-i','/home/claude/scratch/v7/music.mp3']
a=idx
fc.append(f"[{a}:a]atrim=0:{END}[m1];[{a+1}:a]atrim=0.45:3.2,asetpts=PTS-STARTPTS,volume=0.8,adelay=14750|14750[m2];"
          f"[m1][m2]amix=inputs=2:normalize=0,atrim=0:{END},afade=t=out:st={END-1.0}:d=1.0[a]")
subprocess.run(['ffmpeg','-y','-v','error']+inp+['-filter_complex',';'.join(fc),'-map',f'[{prev}]','-map','[a]','-t',str(END),'-r',str(FPS),
  '-c:v','libx264','-crf','17','-preset','veryfast','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart','R-tue_open_v1.mp4'],check=True)
