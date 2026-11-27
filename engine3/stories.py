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
from cardlib import card, render, SCRIM, TOPSCRIM

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
    # Thu: find yourself, poll sticker in the empty lower half (Yang: I push / Yin: I hold); saved to You.
    # Nov 27 (Ryan): headline simplified to 'Are you more Yin or Yang?' for beginners; 'more' keeps it a tendency.
    # v3.3 rework Nov 25: matches R02, asks which way they lean instead of asking them to diagnose themselves.
    '2026-11-26_find-yourself': ground(True)
        + card(True, top=300, kicker='Find yourself', head='Are you more Yin or Yang?',
               body='Lean Yang, and you push.', accent='Lean Yin, and you hold.'),
    # Sat: slow read
    '2026-11-28_slow-read': ground(False)
        + card(False, bottom=520, kicker='Slow read', head='Some days are for starting. Some are for staying in.'),
}

# Mon: week in the season (Seasons). v3.3 Nov 25: the lake-ice ground is retired (water/ice look already on the feed).
_RAT = dict(kicker='This week in the season', head="Winter's deepest month starts Sunday.",
            body='Major Snow on Dec 6 opens <span class="zh">子</span> <span class="py">Zǐ</span>, the Rat month, '
                 'when Water runs at its fullest. In the classical map Water holds wisdom. December fills up fast,',
            accent='so keep some quiet for yourself.')
# Chosen by Ryan Nov 25 (option A): morning tea in a shaft of sun (Runway 02dd207b), cup in the top half fading into the dark table under the type.
STORIES['2026-11-30_rat-month'] = (
    '<div style="position:absolute;inset:0;background:#0d0b09"></div>'
    f'<img src="{BG}/tea.png" style="position:absolute;left:0;top:0;width:100%;height:1080px;object-fit:cover;object-position:50% 40%">'
    '<div style="position:absolute;left:0;right:0;top:640px;height:440px;background:linear-gradient(to bottom,rgba(13,11,9,0),#0d0b09)"></div>'
    + card(True, bottom=470, **_RAT))
# Option B (lit window, Runway d79498ce, text at the top) was shown and not picked.


def _phases():
    cells = [('木', 'Wood', 'Spring', '#7d9a6a'), ('火', 'Fire', 'Summer', '#c0674f'), ('土', 'Earth', 'The turns', '#b8955a'),
             ('金', 'Metal', 'Autumn', '#c9c3b4'), ('水', 'Water', 'Winter', '#7b93ad')]
    row = ''.join(
        f'<div style="width:176px;text-align:center"><div class="zh" style="font-size:118px;color:{DARK["accent"]}">{zh}</div>'
        f'<div class="k" style="font-size:24px;letter-spacing:.2em;margin-top:26px;color:{DARK["head"]}">{en}</div>'
        f'<div class="k" style="font-size:22px;letter-spacing:.2em;margin-top:10px;color:{DARK["soft"]}">{season}</div></div>'
        for zh, en, season, _ in cells)
    return f'<div style="position:absolute;left:96px;right:96px;top:420px;display:flex;justify-content:space-between">{row}</div>'


# Tue: depth (Seasons). The five phases follow the year; Earth rules the turns between seasons.
STORIES['2026-12-01_depth'] = ground(True) + _phases() + card(
    True, bottom=470, kicker='The classical root', head='One element for every season.',
    body='Wood grows in spring, Fire peaks in summer, Metal gathers in autumn, Water rests in winter.',
    accent='Earth holds the turns between.')


# Thu Nov 26 (US Thanksgiving): gratitude, tied to the Resource relationship (the element that produces your Day Master).
# Proverb: yǐn shuǐ sī yuán, "when you drink water, think of its source" (Yu Xin, Northern Zhou), paraphrased.
STORIES['2026-11-26_thanksgiving'] = ground(False) + card(
    False, bottom=470, kicker='Thanksgiving', head='When you drink, remember the well.',
    body='In BaZi, the element that feeds yours is called Resource: the people, teachers and quiet hours that keep you going.',
    accent='Today, thank yours.')


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
