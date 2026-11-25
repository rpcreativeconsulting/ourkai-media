"""Highlight covers and Story frames (canon v3.2 §15-16), 1080 x 1920, in the locked type.

    python3 engine3/stories.py covers            -> $OURKAI_WORK/out/highlights/N_name.png
    python3 engine3/stories.py 2026-11-24_depth  -> $OURKAI_WORK/out/stories/2026-11-24_depth/1.png

Grounds are the shared textures (Runway task ids in engine3/grids/g2.py), saved as
$OURKAI_WORK/bg/paper.png and slate.png. Text stays out of the top 280 px and bottom 420 px.
Cover symbols sit inside the centred 600 px circle that Instagram crops to.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.join(_HERE, 'reels'))
from ourkai_type import DARK, LIGHT
from cardlib import card, render

WORK = os.environ.get('OURKAI_WORK', '/home/claude/work')
BG = f"file://{WORK}/bg"


def ground(dark):
    return f'<img src="{BG}/{"slate" if dark else "paper"}.png" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'


def gold(dark):
    return DARK['accent'] if dark else LIGHT['accent_large']


# ---------- Highlight covers ----------
def _svg(inner, dark, sw=9):
    return (f'<svg width="600" height="600" viewBox="-150 -150 300 300" style="position:absolute;left:240px;top:660px" '
            f'fill="none" stroke="{gold(dark)}" stroke-width="{sw}" stroke-linecap="round">{inner}</svg>')


def _zh(ch, dark):
    return (f'<div class="zh" style="position:absolute;left:240px;top:660px;width:600px;height:600px;display:flex;'
            f'align-items:center;justify-content:center;font-size:300px;line-height:1;color:{gold(dark)}">{ch}</div>')


def _quarters():
    import math
    r, gap, s = 110, 9, ''
    for q in range(4):
        a0, a1 = math.radians(q * 90 + gap - 45), math.radians(q * 90 + 90 - gap - 45)
        s += (f'<path d="M {r*math.cos(a0):.1f} {r*math.sin(a0):.1f} A {r} {r} 0 0 1 '
              f'{r*math.cos(a1):.1f} {r*math.sin(a1):.1f}"/>')
    return s


COVERS = {
    '1_start-here': (True, _svg('<circle cx="0" cy="-26" r="54"/><circle cx="-44" cy="24" r="54"/><circle cx="44" cy="24" r="54"/>', True, 5)),
    '2_download':   (False, _svg('<line x1="0" y1="-110" x2="0" y2="110"/>', False)),
    '3_seasons':    (True, _svg(_quarters(), True)),
    '4_you':        (False, _zh('人', False)),
    '5_timing':     (True, _zh('天', True)),
    '6_home':       (False, _zh('地', False)),
    '7_vibes':      (True, _svg('<circle cx="-46" cy="0" r="80"/><circle cx="46" cy="0" r="80"/>', True, 8)),
}


def covers():
    render({k: ground(d) + art for k, (d, art) in COVERS.items()}, f'{WORK}/out/highlights')


# ---------- Story frames ----------
STORIES = {
    # Tue: depth, saved to Timing
    '2026-11-24_depth': ground(False)
        + '<div class="zh" style="position:absolute;left:0;right:0;top:470px;text-align:center;font-size:250px;'
          f'letter-spacing:.12em;padding-left:.12em;color:{gold(False)}">陰陽</div>'
        + card(False, bottom=470, kicker='The classical root', head='One hill. Two sides.',
               body='Yīn first meant the shaded slope of a hill, Yáng the sunlit one.',
               accent='Not two things. One hill, two kinds of light.'),
    # Thu: find yourself, poll sticker goes in the empty lower half; saved to Timing
    '2026-11-26_find-yourself': ground(True)
        + card(True, top=300, kicker='Find yourself', head='Right now, which do you have too much of?',
               body='Yang moves out: doing, speaking, spending. Yin draws in:',
               accent='resting, listening, storing.'),
    # Sat: slow read
    '2026-11-28_slow-read': ground(False)
        + card(False, bottom=520, kicker='Slow read', head='Some days are for starting. Some are for staying in.'),
}

# Multi-frame Stories: name -> list of frames (saved as 1.png, 2.png ...)
MULTI = {
    # Sat: posted right after the Slow read; both saved to Seasons
    '2026-11-28_raw-line': [
        ground(False) + card(False, bottom=520, kicker='Winter', head="That's not rest.<br>That's scrolling."),
        ground(False) + card(False, bottom=520, kicker='Winter', head='Winter is for storing.',
                             body='Not spending. Even your attention.',
                             accent='Put the phone down one hour earlier tonight.'),
    ],
}


def story(name):
    if name in MULTI:
        render({str(i + 1): f for i, f in enumerate(MULTI[name])}, f'{WORK}/out/stories/{name}')
    else:
        render({'1': STORIES[name]}, f'{WORK}/out/stories/{name}')


if __name__ == '__main__':
    for a in sys.argv[1:]:
        covers() if a == 'covers' else story(a)
