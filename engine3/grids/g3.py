"""Grid 3 (posts 19-27) · APPROVED by Ryan, Nov 20, 2026.

Yin grid: dark center and corners, light side squares. Chapters: 5 · The Cosmic Trinity (Yang,
light squares) and 6 · Self: BaZi (Yin, dark squares); center 人 · Self.

Layout on the profile (Lo Shu, newest top left):
    24 · 4 SE   19 · 9 S    25 · 2 SW
    20 · 3 E    23 · 5 C    21 · 7 W
    26 · 8 NE   22 · 1 N    27 · 6 NW
Fill (posting) order: 27, 22, 26, 21, 23, 20, 25, 19, 24.

Revisions
- Nov 20: four rounds of photo options (A-D) reviewed; Ryan approved 24 the match catching (fire, chosen over the water drop), 19 moon gate,
  25 frost crystal, 20 tea table. Center 23 moved off the shared slate (the bottom of the grid read
  as one grey) to stepping stones over black water. Unpicked options are logged in the matrix
  Assets sheet as Available.
- Nov 23: center 23 changed to a thumbprint in dark clay (an image that stands for "you"); post 22 rewritten from
  "Which realm do you ignore?" to "Three kinds of qi move your day." (people feel the three qi without knowing them).
- Posts 21 and 26 are carousel covers: slides 2-5 still to build.
"""
import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
WORK = _os.environ.get('OURKAI_WORK', '/home/claude/work')

BACKGROUNDS = {
    'match':          '6595c52e-6cfc-465a-9c59-4c8b92e4452e',  # 24 · a match the instant it catches
    'moongate':       'aedc6398-e3b1-4cce-ac60-a4a40731a2aa',  # 19 · moon gate in pale plaster framing a dawn sky
    'crystal':        '8c121ae7-0889-4eb7-9c9d-3963803fd983',  # 25 · one frost crystal on dark glass, lit gold
    'teatable':       '08058c9b-6569-4d24-8cc9-8900b5f8c4f7',  # 20 · low tea table, three cushions, morning sun
    'thumbprint':     'b2e6a72c-83b1-4f59-9ed0-3d55963bf55d',  # 23 · one thumbprint pressed into dark clay, warm side light
    'paper':          '2ce98312-8a6f-42ea-9cdc-dc6ae3824c10',  # shared paper (21, 22)
    'slate':          '5ddfefae-351d-40c8-8d28-99d76b29f0f0',  # shared slate (26, 27)
}

ZH = '<span class="ok-zh">{}</span>'

TILES = [  # profile order, approved
    dict(post=24, slug='born-into-a-moment', template='horizon', bg='match', dark=True, kicker='BaZi', palace='4 · SE · 24',
         head='You were born into a moment.', body='Year, month, day, hour:', accent='four pillars, eight characters.'),
    dict(post=19, slug='heaven-earth-you', template='horizon', bg='moongate', dark=False, kicker='The three realms', palace='9 · S · 19',
         head='Heaven, Earth, and you.',
         body=f'{ZH.format("天")} Cosmic, {ZH.format("地")} Earth, {ZH.format("人")} Self:', accent='the three realms.'),
    dict(post=25, slug='not-your-sun-sign', template='sky', bg='crystal', dark=True, kicker='BaZi', palace='2 · SW · 25',
         head='Not your sun sign. Your own chart.', body='About one in twelve share your sun sign.', accent='Your chart goes much further.'),
    dict(post=20, slug='right-time-place-people', template='sky', bg='teatable', dark=False, kicker='The three realms', palace='3 · E · 20',
         head='Right time. Right place. Right people.', body='An old Chinese saying,', accent='and a map of a good decision.'),
    dict(post=23, slug='third-realm', template='character', bg='thumbprint', dark=True, kicker='人 · Self', palace='5 · Center · 23', char='人',
         head='You are the third realm.', body='Heaven and Earth set the stage.', accent='You walk on it.'),
    dict(post=21, slug='three-realms-systems', template='plate', bg='paper', dark=False, kicker='The three realms', palace='7 · W · 21',
         art='three_realms', head='Three realms. Three systems.', cta='Swipe →'),
    dict(post=26, slug='meet-your-day-master', template='plate', bg='slate', dark=True, kicker='BaZi', palace='8 · NE · 26',
         art='ten_stems', head='Meet your Day Master.', body='The stem of your birth day is', accent='your center.', cta='Swipe for all ten →'),
    dict(post=22, slug='three-qi', template='question', bg='paper', dark=False, kicker='Find yourself', palace='1 · N · 22',
         head='Three kinds of qi move your day.', sub='Time, place and you. Most of us feel them without knowing their names.', cta='Comment the one you feel most'),
    dict(post=27, slug='which-day-master', template='question', bg='slate', dark=True, kicker='Find yourself', palace='6 · NW · 27',
         head='Ten Day Masters. Which are you?', sub='The Tree, the Rain, and eight more. Coming soon to the app.', cta='See how it reads · link in bio'),
]

OPTIONS = {}  # approved Nov 20; earlier options in the matrix Assets sheet


def _art_three_realms(c):
    rows = [('天', 'Cosmic', 'Tong Shu · Planner'), ('地', 'Earth', 'Feng Shui · Directions'), ('人', 'Self', 'BaZi · You')]
    r = ''.join(
        f'<div style="display:flex;align-items:center;gap:16px;padding:11px 0;border-top:0.5px solid {c["rule"]}">'
        f'<div class="ok-zh" style="font-size:34px;width:40px;text-align:center;color:{c["accent_large"]}">{z}</div>'
        f'<div><div class="ok-label" style="color:{c["head"]}">{e}</div><div class="ok-label" style="font-size:8px;color:{c["soft"]};margin-top:4px">{s}</div></div></div>'
        for z, e, s in rows)
    return f'<div style="position:absolute;left:29px;right:29px;top:96px">{r}</div>'


def _art_ten_stems(c):
    stems = [('甲', 'Tree'), ('乙', 'Vine'), ('丙', 'Sun'), ('丁', 'Candle'), ('戊', 'Mountain'),
             ('己', 'Garden'), ('庚', 'Steel'), ('辛', 'Jewel'), ('壬', 'Ocean'), ('癸', 'Rain')]
    cells = ''.join(
        f'<div style="display:flex;flex-direction:column;align-items:center;gap:5px">'
        f'<div class="ok-zh" style="font-size:24px;color:{c["accent"]}">{z}</div>'
        f'<div class="ok-label" style="font-size:6.4px;letter-spacing:.12em;color:{c["soft"]}">{e}</div></div>'
        for z, e in stems)
    return f'<div style="position:absolute;left:29px;right:29px;top:96px;display:grid;grid-template-columns:repeat(5,1fr);row-gap:18px">{cells}</div>'


def build(bgdir=None, variant='A'):
    """Return [(post, html)] in profile order."""
    import sys
    sys.path.insert(0, _os.path.normpath(_os.path.join(_HERE, '..')))
    import ourkai_type as T
    T.DARK['label'] = T.DARK['soft']
    T.LIGHT['label'] = T.LIGHT['soft']
    import templates as TP
    bgdir = bgdir or _os.path.join(WORK, 'bg')
    swap = OPTIONS.get(variant, {})
    out = []
    for t in TILES:
        c = T.DARK if t['dark'] else T.LIGHT
        bg = swap.get(t['post'], t['bg'])
        src = f"file://{bgdir}/{bg}.png"
        k = t['template']
        if k == 'horizon':
            h = TP.horizon(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('body'), t.get('accent'), t.get('cta'))
        elif k == 'sky':
            h = TP.sky(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('body'), t.get('accent'), t.get('cta'))
        elif k == 'character':
            h = TP.character(src, t['dark'], t['kicker'], t['palace'], t['char'], t['head'], t.get('body'), t.get('accent'), t.get('cta'))
        elif k == 'plate':
            art = _art_three_realms(c) if t['art'] == 'three_realms' else _art_ten_stems(c)
            h = TP.plate(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('body'), t.get('accent'), art=art, cta=t.get('cta'))
        elif k == 'question':
            h = TP.question(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('sub'), t.get('cta'))
        out.append((t['post'], h))
    return out
