set -e
S=src; C=cards
T=26.94
ffmpeg -v error -y \
 -i $S/a.mp4 -i $S/b.mp4 -loop 1 -t 5.5 -i ${OURKAI_WORK:-/home/claude/work}/reels/shared/grounds/plaster.png -i ${OURKAI_WORK:-/home/claude/work}/reels/shared/endcard_v2.mp4 \
 -loop 1 -t $T -i $C/c1.png -loop 1 -t $T -i $C/c2.png -loop 1 -t $T -i $C/c3.png \
 -loop 1 -t $T -i $C/c4.png -loop 1 -t $T -i $C/c5.png \
 -filter_complex "
 [0]setpts=1.8*PTS,minterpolate=fps=24:mi_mode=blend,scale=1434:1920:flags=lanczos,crop=1080:1920,setsar=1,format=yuv420p[A];
 [1]setpts=1.8*PTS,minterpolate=fps=24:mi_mode=blend,scale=1434:1920:flags=lanczos,crop=1080:1920,setsar=1,format=yuv420p[B];
 [2]scale=2160:-2,crop=2160:3840,zoompan=z='1+0.06*on/132':d=132:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=24,setsar=1,format=yuv420p[Cs];
 [3]fps=24,setsar=1,format=yuv420p[D];
 [A][B]xfade=transition=fade:duration=0.8:offset=8.27[AB];
 [AB][Cs]xfade=transition=fade:duration=0.8:offset=16.54[ABC];
 [ABC][D]xfade=transition=fade:duration=0.6:offset=21.44,trim=0:$T[base];
 [4]format=rgba,fade=in:st=0.3:d=0.6:alpha=1,fade=out:st=3.6:d=0.5:alpha=1[o1];
 [5]format=rgba,fade=in:st=4.4:d=0.6:alpha=1,fade=out:st=7.5:d=0.5:alpha=1[o2];
 [6]format=rgba,fade=in:st=8.9:d=0.6:alpha=1,fade=out:st=12.3:d=0.5:alpha=1[o3];
 [7]format=rgba,fade=in:st=13.0:d=0.6:alpha=1,fade=out:st=16.1:d=0.5:alpha=1[o4];
 [8]format=rgba,fade=in:st=17.2:d=0.7:alpha=1,fade=out:st=20.9:d=0.5:alpha=1[o5];
 [base][o1]overlay=shortest=1[v1];[v1][o2]overlay=shortest=1[v2];[v2][o3]overlay=shortest=1[v3];
 [v3][o4]overlay=shortest=1[v4];[v4][o5]overlay=shortest=1,fade=out:st=26.3:d=0.64,format=yuv420p[v]" \
 -map "[v]" -r 24 -c:v libx264 -preset veryfast -crf 18 -movflags +faststart -an R02_light-needs-shadow_v2_silent.mp4
