import sys,subprocess,numpy as np
# usage: clean.py in_audio out_wav [extra_af]
src,out=sys.argv[1],sys.argv[2]; extra=sys.argv[3] if len(sys.argv)>3 else ''
N=','.join(f'bandreject=f={50*k}:width_type=h:w=4' for k in range(1,41))  # 50 Hz .. 2 kHz, 4 Hz wide
af=f"aresample=48000,highpass=f=40:poles=2,highpass=f=40:poles=2,{N},{N}"+(','+extra if extra else '')
subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vn','-af',af,'-ar','48000','-ac','2',out+'.tmp.wav'],check=True)
L=float([l for l in subprocess.run(['ffmpeg','-hide_banner','-i',out+'.tmp.wav','-af','ebur128=framelog=quiet','-f','null','-'],capture_output=True,text=True).stderr.splitlines() if ' I:' in l][-1].split()[1])
g=-21-L
subprocess.run(['ffmpeg','-v','error','-y','-i',out+'.tmp.wav','-af',f'volume={g}dB,aresample=192000,alimiter=limit=0.56:level=false,aresample=48000','-ar','48000',out],check=True)
print(f'{src}: content level {L} LUFS, gain {g:.1f}')
