set -e
S=src; C=cards; T=28.23
SC="setsar=1,format=yuv420p"
ffmpeg -v error -y \
 -loop 1 -t 4.2 -i ${OURKAI_WORK:-/home/claude/work}/reels/shared/grounds/cedar.png -i $S/fire.mp4 -i $S/rainember.mp4 -i $S/sprout.mp4 -i $S/ripples.mp4 -i ${OURKAI_WORK:-/home/claude/work}/reels/shared/endcard_v2.mp4 \
 -framerate 24 -i dia/%04d.png \
 -loop 1 -t $T -i $C/scrim.png -loop 1 -t $T -i $C/c1.png -loop 1 -t $T -i $C/c2.png -loop 1 -t $T -i $C/c3.png -loop 1 -t $T -i $C/c4.png -loop 1 -t $T -i $C/c5.png \
 -filter_complex "
 [0]scale=2160:-2,crop=2160:3840,zoompan=z='1+0.03*on/100':d=100:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=24,eq=brightness=-0.13:contrast=0.85:saturation=0.8,$SC[S1];
 [1]setpts=1.35*PTS,minterpolate=fps=24:mi_mode=blend,scale=1080:1937:flags=lanczos,crop=1080:1920,format=yuva444p,geq=lum='p(X,Y)':cb='p(X,Y)':cr='p(X,Y)':a='if(lt(Y,260),255*Y/260,255)'[Fa];color=c=0x0b0a08:s=1080x1920:r=24:d=5.46[Fb];[Fb][Fa]overlay=x=0:y=470:shortest=1,$SC[F];
 [2]setpts=1.08*PTS,minterpolate=fps=24:mi_mode=blend,scale=1080:1937:flags=lanczos,crop=1080:1920,$SC[R];
 [3]setpts=1.08*PTS,minterpolate=fps=24:mi_mode=blend,scale=1434:1920:flags=lanczos,crop=1080:1920,$SC[P];
 [4]setpts=1.9*PTS,minterpolate=fps=24:mi_mode=blend,scale=1242:2227:flags=lanczos,crop=1080:1920:81:0,$SC[Q];
 [5]fps=24,$SC[D];
 [S1][F]xfade=transition=fade:duration=0.6:offset=3.6[x1];
 [x1][R]xfade=transition=fade:duration=0.6:offset=8.45[x2];
 [x2][P]xfade=transition=fade:duration=0.6:offset=13.29[x3];
 [x3][Q]xfade=transition=fade:duration=0.6:offset=18.13[x4];
 [x4][D]xfade=transition=fade:duration=0.6:offset=22.73,trim=0:$T[base];
 [7]format=rgba,fade=out:st=17.6:d=0.6:alpha=1[s];
 [8]format=rgba,fade=in:st=0.3:d=0.5:alpha=1,fade=out:st=3.0:d=0.4:alpha=1[o1];
 [9]format=rgba,fade=in:st=4.0:d=0.5:alpha=1,fade=out:st=7.7:d=0.4:alpha=1[o2];
 [10]format=rgba,fade=in:st=8.9:d=0.5:alpha=1,fade=out:st=12.6:d=0.4:alpha=1[o3];
 [11]format=rgba,fade=in:st=13.7:d=0.5:alpha=1,fade=out:st=17.3:d=0.4:alpha=1[o4];
 [12]format=rgba,fade=in:st=18.6:d=0.6:alpha=1,fade=out:st=22.3:d=0.4:alpha=1[o5];
 [base][s]overlay=shortest=1[v0];[v0][6]overlay=eof_action=pass[vd];[vd][o1]overlay=shortest=1[v1];[v1][o2]overlay=shortest=1[v2];
 [v2][o3]overlay=shortest=1[v3];[v3][o4]overlay=shortest=1[v4];[v4][o5]overlay=shortest=1,fade=out:st=27.6:d=0.63,format=yuv420p[v]" \
 -map "[v]" -an -r 24 -c:v libx264 -preset veryfast -crf 18 -movflags +faststart R04_who-feeds-you_v4_silent.mp4
A="aformat=sample_rates=48000:channel_layouts=stereo"
ffmpeg -v error -y -i $S/s_end.mp3 -i $S/s_fire.mp3 -i $S/s_hiss.mp3 -i $S/s_drip.mp3 -i $S/s_end.mp3 -i $S/s_drops.mp3 -filter_complex "
[0]$A,atrim=0:4.4,afade=in:d=0.8,afade=out:st=3.6:d=0.8[a];
[1]$A,afade=in:d=0.6,afade=out:st=4.2:d=0.8,adelay=3600|3600[b];
[2]$A,afade=in:d=0.6,afade=out:st=4.8:d=0.8,adelay=8450|8450[c];
[3]$A,afade=in:d=0.6,afade=out:st=4.8:d=0.8,adelay=13290|13290[d];
[4]$A,afade=in:d=1.2,adelay=18130|18130[e];
[5]$A,volume=0.8,afade=out:st=4.0:d=1,adelay=18500|18500[f];
[a][b][c][d][e][f]amix=inputs=6:normalize=0:duration=longest,atrim=0:$T,afade=out:st=26.7:d=1.5,loudnorm=I=-21:TP=-3:LRA=11[m]" -map "[m]" -c:a pcm_s16le snd.wav
ffmpeg -v error -y -i R04_who-feeds-you_v4_silent.mp4 -i snd.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart R04_who-feeds-you_v4.mp4
