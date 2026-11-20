"""Build a grid from its approved spec (engine3/grids/gN.py).

    OURKAI_WORK=/home/claude/work python3 engine3/build_grid.py 2 [--tiles]

Backgrounds must be in $OURKAI_WORK/bg/<name>.png (fetch fresh URLs with Runway get_task
using the ids in the spec's BACKGROUNDS). Writes the 3x3 preview, and with --tiles each
tile at 1080 x 1440, to $OURKAI_WORK/out/.
"""
import os, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
WORK = os.environ.get('OURKAI_WORK', '/home/claude/work')
from ourkai_type import css
from render import render

n = sys.argv[1]
spec = importlib.import_module(f'grids.g{n}')
tiles = dict(spec.build(os.path.join(WORK, 'bg')))
order = [t['post'] for t in spec.TILES]          # profile order, as in the spec
slug = {t['post']: t.get('slug') for t in spec.TILES}
out = os.path.join(WORK, 'out'); os.makedirs(out, exist_ok=True)
head = f'<html><head><meta charset="utf-8"><style>{css()}body{{margin:0;background:#fff}}</style></head><body>'
gap = '<div style="width:360px;height:480px;background:#2a2824;display:flex;align-items:center;justify-content:center;color:#8a8370;font:12px monospace">missing background</div>'
open(f'{WORK}/board.html', 'w').write(head + '<div style="display:grid;grid-template-columns:repeat(3,360px);gap:4px">' + ''.join(tiles.get(p, gap) for p in order) + '</div></body></html>')
render(f'{WORK}/board.html', f'{out}/G{n}_grid-preview.png', 1088, 1448, 2)
if '--tiles' in sys.argv:
    for p in [p for p in order if p in tiles]:
        open(f'{WORK}/t.html', 'w').write(head + tiles[p] + '</body></html>')
        render(f'{WORK}/t.html', f'{out}/G{n}-{p}{"_" + slug[p] if slug[p] else ""}.png', 360, 480, 3)
    if hasattr(spec, 'build_slides'):
        for name, h in spec.build_slides(os.path.join(WORK, 'bg')):
            open(f'{WORK}/t.html', 'w').write(head + h + '</body></html>')
            render(f'{WORK}/t.html', f'{out}/{name}.png', 360, 480, 3)
print('built', out)
