set -e
S=src; C=cards; T=30.0
SC="scale=1080:1937:flags=lanczos,crop=1080:1920,setsar=1,format=yuv420p"
ffmpeg -v error -y \
 -i $S/wood.mp4 -i $S/fire.mp4 -i $S/earth.mp4 -i $S/metal.mp4 -i $S/water.mp4 -loop 1 -t 4.6 -i ${OURKAI_WORK:-/home/claude/work}/reels/shared/grounds/basalt.png -i ${OURKAI_WORK:-/home/claude/work}/reels/shared/endcard_noask.mp4 \
 -loop 1 -t $T -i $C/scrim.png -loop 1 -t $T -i $C/c1.png -loop 1 -t $T -i $C/c2.png -loop 1 -t $T -i $C/c3.png -loop 1 -t $T -i $C/c4.png \
 -loop 1 -t $T -i $C/c5.png -loop 1 -t $T -i $C/c6.png -loop 1 -t $T -i $C/c7.png \
 -filter_complex "
 [0]fps=24,$SC[W];
 [1]setpts=1.1*PTS,minterpolate=fps=24:mi_mode=blend,$SC[F];
 [2]setpts=1.1*PTS,minterpolate=fps=24:mi_mode=blend,$SC[E];
 [3]setpts=1.1*PTS,minterpolate=fps=24:mi_mode=blend,$SC[M];
 [4]setpts=1.1*PTS,minterpolate=fps=24:mi_mode=blend,$SC[Wa];
 [5]scale=2160:-2,crop=2160:3840,zoompan=z='1+0.05*on/110':d=110:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=24,eq=brightness=-0.06:saturation=0.85,setsar=1,format=yuv420p[Q];
 [6]fps=24,setsar=1,format=yuv420p[D];
 [W][F]xfade=transition=fade:duration=0.6:offset=5.95[x1];
 [x1][E]xfade=transition=fade:duration=0.6:offset=9.79[x2];
 [x2][M]xfade=transition=fade:duration=0.6:offset=13.63[x3];
 [x3][Wa]xfade=transition=fade:duration=0.6:offset=17.47[x4];
 [x4][Q]xfade=transition=fade:duration=0.6:offset=21.31[x5];
 [x5][D]xfade=transition=fade:duration=0.6:offset=25.31,trim=0:$T[base];
 [7]format=rgba,fade=out:st=21.0:d=0.6:alpha=1[s];
 [8]format=rgba,fade=in:st=0.3:d=0.5:alpha=1,fade=out:st=2.8:d=0.4:alpha=1[o1];
 [9]format=rgba,fade=in:st=3.3:d=0.5:alpha=1,fade=out:st=5.6:d=0.4:alpha=1[o2];
 [10]format=rgba,fade=in:st=6.4:d=0.5:alpha=1,fade=out:st=9.4:d=0.4:alpha=1[o3];
 [11]format=rgba,fade=in:st=10.2:d=0.5:alpha=1,fade=out:st=13.2:d=0.4:alpha=1[o4];
 [12]format=rgba,fade=in:st=14.1:d=0.5:alpha=1,fade=out:st=17.1:d=0.4:alpha=1[o5];
 [13]format=rgba,fade=in:st=17.9:d=0.5:alpha=1,fade=out:st=20.9:d=0.4:alpha=1[o6];
 [14]format=rgba,fade=in:st=21.8:d=0.6:alpha=1,fade=out:st=24.9:d=0.4:alpha=1[o7];
 [base][s]overlay=shortest=1[v0];[v0][o1]overlay=shortest=1[v1];[v1][o2]overlay=shortest=1[v2];[v2][o3]overlay=shortest=1[v3];
 [v3][o4]overlay=shortest=1[v4];[v4][o5]overlay=shortest=1[v5];[v5][o6]overlay=shortest=1[v6];[v6][o7]overlay=shortest=1,fade=out:st=29.4:d=0.6,format=yuv420p[v]" \
 -map "[v]" -r 24 -c:v libx264 -preset veryfast -crf 18 -movflags +faststart -an R03_phases_v8_silent.mp4
