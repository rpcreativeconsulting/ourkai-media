# R06 "You were born into a moment." Run from ${OURKAI_WORK}/reels/R06 after R06/cards.py and R06/diagram.py.
# The paper clip plays forward then back (candlelight breathing) under the three diagram beats.
set -e
S=src; C=cards; T=28.23; W=${OURKAI_WORK:-/home/claude/work}
SC="fps=24,settb=1/24,setsar=1,format=yuv420p"; UP="scale=1080:1920:flags=lanczos"
ffmpeg -v error -y \
 -i $S/v1_candle.mp4 -i $S/v2_paper.mp4 -loop 1 -t 5.4 -i $S/q_wax.png -i $W/reels/shared/endcard_v2.mp4 \
 -framerate 24 -i dia/%04d.png \
 -loop 1 -t $T -i $C/scrim.png -loop 1 -t $T -i $C/topscrim.png \
 -loop 1 -t $T -i $C/c1.png -loop 1 -t $T -i $C/c2.png -loop 1 -t $T -i $C/c3.png -loop 1 -t $T -i $C/c4.png -loop 1 -t $T -i $C/c5.png \
 -filter_complex "
 [0]$UP,$SC[A];
 [1]split[pa][pb];[pb]reverse[pr];[pa][pr]concat=n=2:v=1,setpts=1.52*PTS,minterpolate=fps=24:mi_mode=blend,$UP,$SC[P];
 [2]scale=2160:-2,crop=2160:3840,zoompan=z='1+0.05*on/130':d=130:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=24,$SC[Q];
 [3]fps=24,$SC[E];
 [4]setpts=PTS+3.6/TB,format=rgba[dia];
 [A][P]xfade=transition=fade:duration=0.6:offset=3.6[x1];
 [x1][Q]xfade=transition=fade:duration=0.6:offset=18.13[x2];
 [x2][E]xfade=transition=fade:duration=0.6:offset=22.73,trim=0:$T[base];
 [5]format=rgba,fade=out:st=17.6:d=0.6:alpha=1[s];
 [6]format=rgba,fade=in:st=18.1:d=0.6:alpha=1,fade=out:st=22.5:d=0.5:alpha=1[ts];
 [7]format=rgba,fade=in:st=0.3:d=0.5:alpha=1,fade=out:st=3.0:d=0.4:alpha=1[o1];
 [8]format=rgba,fade=in:st=4.0:d=0.5:alpha=1,fade=out:st=7.7:d=0.4:alpha=1[o2];
 [9]format=rgba,fade=in:st=8.9:d=0.5:alpha=1,fade=out:st=12.6:d=0.4:alpha=1[o3];
 [10]format=rgba,fade=in:st=13.7:d=0.5:alpha=1,fade=out:st=17.3:d=0.4:alpha=1[o4];
 [11]format=rgba,fade=in:st=18.6:d=0.6:alpha=1,fade=out:st=22.3:d=0.4:alpha=1[o5];
 [base][s]overlay=shortest=1[v0];[v0][dia]overlay=eof_action=pass[vd];[vd][ts]overlay=shortest=1[vt];[vt][o1]overlay=shortest=1[v1];[v1][o2]overlay=shortest=1[v2];
 [v2][o3]overlay=shortest=1[v3];[v3][o4]overlay=shortest=1[v4];[v4][o5]overlay=shortest=1,fade=out:st=27.6:d=0.63,format=yuv420p[v]" \
 -map "[v]" -an -r 24 -c:v libx264 -preset veryfast -crf 18 -movflags +faststart R06_picture_silent.mp4
