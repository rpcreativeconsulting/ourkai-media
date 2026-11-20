"""Grid 1 (posts 1-9) · LIVE since Nov 17, 2026 · rebuilt Nov 20 as the spec, from the posted tiles.

Grid 1 was rendered in an earlier chat and its files were not kept. This spec recreates it
from the matrix copy and the backgrounds' Runway task ids, checked by eye against the live
posts. Kickers here stay in the sage label colour, as on the live grid (Grid 2 later moved
them to the palace grey).

Backgrounds: Runway task ids below; fetch fresh URLs with Runway get_task and save each as
$OURKAI_WORK/bg/<name>.png. 'bowl' (post 5) is Runway asset a2cd21e6, made by Ryan in the
Runway app; it has no task URL, Ryan supplied the file on Nov 20; it lives in the repo as media/sources/bowl.png.

Layout on the profile (Lo Shu, newest top left):
    6 · 4 SE   1 · 9 S    7 · 2 SW
    2 · 3 E    5 · 5 C    3 · 7 W
    8 · 8 NE   4 · 1 N    9 · 6 NW
Post 3 is a 5-slide carousel (SLIDES).
"""
import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
WORK = _os.environ.get('OURKAI_WORK', '/home/claude/work')

BACKGROUNDS = {
    'leafpaper': 'fbe1f502-b629-4c7b-9ca1-1fa29c9e9dbe',  # post 1 · pale leaf shadows on handmade paper (the redo that went live)
    'sky':       '610f20ec-0b81-4714-94a1-666387c08b85',  # post 2 · pale morning sky, thin high clouds
    'window':    '92450a3e-140f-4c32-96aa-58867dd1db38',  # post 6 · window light on a dark plaster wall
    'silk':      'e572776b-ed67-4bc2-88b5-da0b9e96d466',  # post 7 · dark silk, one warm line
    'branch':    '7d4fe9dc-cdbb-435b-a74f-9734304c50c3',  # post 9 · frosted bare branch, winter dusk
    'paper':     '2ce98312-8a6f-42ea-9cdc-dc6ae3824c10',  # shared paper (posts 3, 4, slides)
    'slate':     '5ddfefae-351d-40c8-8d28-99d76b29f0f0',  # shared slate (post 8)
    'bowl':      'asset a2cd21e6-661c-4632-8850-83020fdb5cf5',  # post 5 · Ryan's stone bowl (file needed)
}

TILES = [  # profile order
    dict(post=6, slug='light-needs-shadow', template='horizon', bg='window', dark=True, kicker='Yin and Yang', palace='4 · SE · 6',
         head='Light needs shadow.', body="Yin and Yang aren't at war.", accent='They make each other.'),
    dict(post=1, slug='read-the-day', template='horizon', bg='leafpaper', dark=False, kicker='A modern almanac', palace='9 · S · 1',
         head='Read the day before you live it.', body='Your birth details, read against', accent='the day ahead.'),
    dict(post=7, slug='too-much-of', template='sky', bg='silk', dark=True, kicker='Yin and Yang', palace='2 · SW · 7',
         head='Which do you have too much of?', body='Yang moves out: bright, active, spending. Yin draws in:', accent='quiet, still, storing.'),
    dict(post=2, slug='same-sky', template='horizon', bg='sky', dark=False, kicker='Timing', palace='3 · E · 2',
         head='Same sky. A different day for everyone.', body='Each day, read against', accent='your own chart.'),
    dict(post=5, slug='your-life-unlocked', template='brand', bg='bowl', dark=True, palace='5 · Center · 5'),
    dict(post=3, slug='four-systems', template='plate', bg='paper', dark=False, kicker='Four systems', palace='7 · W · 3', art='four_columns',
         head='Four classical systems. One reading of you.', cta='Swipe →'),
    dict(post=8, slug='two-lines', template='plate', bg='slate', dark=True, kicker='The two lines', palace='8 · NE · 8', art='two_lines',
         head='Everything starts with two lines.', body='Solid is Yang. Broken is Yin. Six make', accent='the 64 hexagrams.', cta='Save this'),
    dict(post=4, slug='today-asks', template='question', bg='paper', dark=False, kicker='Find yourself', palace='1 · N · 4',
         head='What does today ask of you?', sub='Calculated, not guessed. Coming soon.', cta='See how it reads · link in bio'),
    dict(post=9, slug='not-lazy-winter', template='horizon', bg='branch', dark=True, kicker='Winter is Yin', palace='6 · NW · 9',
         head="You're not lazy. It's winter.", body='The Yin season is for', accent='storing energy, not spending it.', cta='Save this'),
]

SLIDES = [  # post 3, slides 2-5, on the shared paper
    dict(post=3, n=2, char='八字', label='BaZi', head='BaZi: your birth chart.',
         body='Four pillars from the year, month, day and hour you were born. In the app: You.'),
    dict(post=3, n=3, char='通書', label='Tong Shu', head='Tong Shu: the almanac.',
         body='Which days suit which actions, read against your chart. In the app: Today and Planner.'),
    dict(post=3, n=4, char='風水', label='Feng Shui', head='Feng Shui: your space.',
         body='How energy moves through your home, room by room, year by year. In the app: Feng Shui.'),
    dict(post=3, n=5, char='奇門', label='Qi Men', head='Qi Men: timing and direction.',
         body='Which way to move, and when. In the app: Directions.', cta='Coming soon · link in bio'),
]


def _art_four_columns(c):
    cols = [('奇門', 'Qi Men'), ('風水', 'Feng Shui'), ('通書', 'Tong Shu'), ('八字', 'BaZi')]  # read right to left
    boxes = ''.join(
        f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px">'
        f'<div style="width:66px;height:154px;border:1px solid {c["rule"]};display:flex;align-items:center;justify-content:center">'
        f'<div class="ok-zh" style="font-size:24px;line-height:1.35;color:{c["head"]};writing-mode:vertical-rl">{z}</div></div>'
        f'<div class="ok-label" style="font-size:7.4px;letter-spacing:.14em;color:{c["soft"]};white-space:nowrap">{e}</div></div>'
        for z, e in cols)
    return (f'<div style="position:absolute;left:29px;right:29px;top:84px;display:flex;justify-content:space-between">{boxes}</div>'
            f'<div class="ok-label" style="position:absolute;left:0;right:0;top:282px;text-align:center;font-size:7.4px;color:{c["soft"]}">Read right to left</div>')


def build(bgdir=None):
    """Return [(post, html)] in profile order. Post 5 is skipped unless bg/bowl.png exists."""
    import sys
    sys.path.insert(0, _os.path.normpath(_os.path.join(_HERE, '..')))
    import ourkai_type as T
    import templates as TP
    bgdir = bgdir or _os.path.join(WORK, 'bg')
    out = []
    for t in TILES:
        c = T.DARK if t['dark'] else T.LIGHT
        src = f"file://{bgdir}/{t['bg']}.png"
        k = t['template']
        if k == 'brand':
            if not _os.path.exists(f"{bgdir}/{t['bg']}.png"):
                continue
            lock = _os.path.normpath(_os.path.join(_HERE, '..', 'reels', 'lockup.svg'))
            h = TP.brand(src, t['palace']).replace('</div></div>', '</div>'
                f'<img src="file://{lock}" alt="" style="position:absolute;left:50%;top:86px;width:196px;transform:translateX(-50%)"></div>', 1)
        elif k == 'horizon':
            h = TP.horizon(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('body'), t.get('accent'), t.get('cta'))
        elif k == 'sky':
            h = TP.sky(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('body'), t.get('accent'), t.get('cta'))
        elif k == 'plate':
            art = _art_four_columns(c) if t['art'] == 'four_columns' else TP.art_two_lines()
            h = TP.plate(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('body'), t.get('accent'), art=art, cta=t.get('cta'))
        elif k == 'question':
            h = TP.question(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('sub'), t.get('cta'))
        out.append((t['post'], h))
    return out


def build_slides(bgdir=None):
    """Return [(name, html)] for the carousel slides."""
    import sys
    sys.path.insert(0, _os.path.normpath(_os.path.join(_HERE, '..')))
    import ourkai_type as T
    c = T.LIGHT
    bgdir = bgdir or _os.path.join(WORK, 'bg')
    out = []
    for s in SLIDES:
        cta = f'<div class="ok-label" style="color:{c["label"]};margin-top:16px">{s["cta"]}</div>' if s.get('cta') else ''
        h = (f'<div class="ok-tile" style="background:{c["ground"]}"><img class="bg" src="file://{bgdir}/paper.png" alt="">'
             f'<div class="ok-top"><span class="ok-label" style="color:{c["label"]}">Four systems</span>'
             f'<span class="ok-label" style="color:{c["soft"]}">{s["n"]} / 5</span></div>'
             f'<div class="ok-rule" style="background:{c["rule"]}"></div>'
             f'<div class="ok-zh" style="position:absolute;left:0;right:0;top:66px;text-align:center;font-size:104px;color:{c["accent_large"]}">{s["char"]}</div>'
             f'<div class="ok-label" style="position:absolute;left:0;right:0;top:196px;text-align:center;color:{c["label"]}">{s["label"]}</div>'
             f'<div class="ok-foot"><div class="ok-head" style="color:{c["head"]}">{s["head"]}</div>'
             f'<div class="ok-body" style="color:{c["body"]}">{s["body"]}</div>{cta}</div></div>')
        out.append((f'G1-3_four-systems_slide-{s["n"]}', h))
    return out
