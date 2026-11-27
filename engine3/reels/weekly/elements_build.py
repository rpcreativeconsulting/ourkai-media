import subprocess
FPS=30; END=17.0
fc=[]
fc.append("[0:v]setpts=1.25*PTS,fps=30,scale=1080:1920,setsar=1,tpad=stop_mode=clone:stop_duration=2.4,"
          "eq=brightness='if(gt(t,12.4),-0.25*min((t-12.4)/0.6,1),0)':eval=frame,trim=0:14.8,setpts=PTS-STARTPTS,format=yuv420p[a]")
fc.append("color=c=0x0e0d0b:s=1080x1920:r=30:d=2.2,format=yuv420p,setsar=1[b]")
fc.append("[a][b]concat=n=2:v=1[bg]")
inp=['-i','clip.mp4']
prev='bg'; idx=1; L=0
def add(png,st,en,slide=26,fade=0.25):
    global prev,idx,L
    inp.extend(['-loop','1','-t',f'{en-st:.2f}','-i',f'f/{png}.png'])
    y=f"if(lt(t-{st},0.45),{slide}*pow(1-(t-{st})/0.45,2),0)"
    fc.extend([f"[{idx}:v]format=rgba,fade=t=in:st=0:d={fade}:alpha=1,fade=t=out:st={en-st-0.2:.2f}:d=0.2:alpha=1,setpts=PTS+{st}/TB[l{L}]",
               f"[{prev}][l{L}]overlay=y='{y}':eval=frame:eof_action=pass:enable='between(t,{st},{en})'[o{L}]"])
    prev=f'o{L}'; idx+=1; L+=1
add('hook',0.1,1.45); add('fire',1.5,2.45); add('earth',2.75,5.2); add('metal',5.6,7.75)
add('water',8.1,10.1); add('wood',10.45,12.35); add('end1',12.6,14.8,30); add('end2',14.8,END,0,0.35)
inp+=['-i','/home/claude/scratch/v7/music.mp3','-i','/home/claude/scratch/v7/music.mp3']
fc.append(f"[{idx}:a]atrim=0:{END}[m1];[{idx+1}:a]atrim=0.45:3.2,asetpts=PTS-STARTPTS,volume=0.8,adelay=14750|14750[m2];[m1][m2]amix=inputs=2:normalize=0,atrim=0:{END},afade=t=out:st={END-1}:d=1[au]")
subprocess.run(['ffmpeg','-y','-v','error']+inp+['-filter_complex',';'.join(fc),'-map',f'[{prev}]','-map','[au]','-t',str(END),'-r','30','-c:v','libx264','-crf','17','-preset','veryfast','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart','R-elements_v1.mp4'],check=True)
