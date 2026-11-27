import subprocess,sys
SRC=sys.argv[1]; OUT=sys.argv[2]
END=18.0; CLIP=12.0
fc=[f"[0:v]setpts=1.2*PTS,fps=30,scale=1080:1920:flags=lanczos,setsar=1,"
    f"eq=gamma='1':brightness=0:eval=frame,"
    f"eq=brightness='if(between(t,6.6,9.4),0.035,0)':contrast='if(between(t,6.6,9.4),1.04,1)':eval=frame,"
    f"trim=0:{CLIP},setpts=PTS-STARTPTS,format=yuv420p[a]",
    f"color=c=0x0e0d0b:s=1080x1920:r=30:d={END-CLIP},format=yuv420p,setsar=1[b]",
    "[a][b]concat=n=2:v=1[bg]"]
inp=['-an','-i',SRC]
prev='bg'; idx=1; L=0
def add(png,st,en,slide=24,fi=0.3,fo=0.25):
    global prev,idx,L
    inp.extend(['-loop','1','-t',f'{en-st:.2f}','-i',f'f/{png}.png'])
    y=f"if(lt(t-{st},0.5),{slide}*pow(1-(t-{st})/0.5,2),0)"
    fc.extend([f"[{idx}:v]format=rgba,fade=t=in:st=0:d={fi}:alpha=1,fade=t=out:st={en-st-fo:.2f}:d={fo}:alpha=1,setpts=PTS+{st}/TB[l{L}]",
               f"[{prev}][l{L}]overlay=y='{y}':eval=frame:eof_action=pass:enable='between(t,{st},{en})'[o{L}]"])
    prev=f'o{L}'; idx+=1; L+=1
add('l1',0.25,2.6); add('l2',3.6,5.6); add('l3',5.8,7.5); add('l4',7.8,9.9); add('l5',10.1,11.8)
add('e1',12.0,14.7,30,0.4); add('e2',12.9,14.7,20,0.4); add(sys.argv[3] if len(sys.argv)>3 else 'logo',14.8,END,0,0.35,0.01)
inp+=['-i','/home/claude/scratch/reel/bed.mp3']
fc.append(f"[{idx}:a]atrim=0:{END},afade=t=in:d=0.6,afade=t=out:st={END-1.2}:d=1.2[au]")
subprocess.run(['ffmpeg','-y','-v','error']+inp+['-filter_complex',';'.join(fc),'-map',f'[{prev}]','-map','[au]','-t',str(END),'-r','30',
  '-c:v','libx264','-crf','17','-preset','veryfast','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',OUT],check=True)
