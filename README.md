# ourkai-media

Finished oürkai social media (feed tiles, Reels, Story frames, Highlight covers) and the engine that renders them.

- `media/` — approved, finished files. Vista Social imports them from their public raw links. Names follow the canon: `feed/G#/G#-NN_slug.png`, `reels/R##_slug.mp4`, `stories/YYYY-MM-DD_slug/N.png`, `highlights/N_name.png`.
- `engine3/` — the locked type and templates (`ourkai_type.py`, `templates.py`, `render.py`), each grid's approved spec (`grids/gN.py`) and the Reel tools (`reels/`).
- `fonts/` — Fraunces, Source Serif 4, JetBrains Mono and Noto Serif SC, open-source under the SIL Open Font License.

The rules live in the oürkai Instagram Canon (v3.2); the posts live in the content matrix.

## Building

```
git clone https://github.com/rpcreativeconsulting/ourkai-media
export OURKAI_WORK=/home/claude/work        # scratch: backgrounds in $OURKAI_WORK/bg, output in $OURKAI_WORK/out
python3 engine3/build_grid.py 2 --tiles     # rebuilds Grid 2 exactly from engine3/grids/g2.py
```

Backgrounds are Runway task ids, listed in each grid spec and the matrix Assets sheet; fetch a fresh URL with Runway `get_task` and save it as `$OURKAI_WORK/bg/<name>.png`. Reels: `engine3/reels/R##/cards.py` (type cards), `build.sh` (ffmpeg cut), `endcard.py` (the shared end card). Needs Playwright with Chrome, and ffmpeg.

This repo is the master copy of the engine. Every session (chat or scheduled run) clones it; approved specs and finished files are pushed back here.
