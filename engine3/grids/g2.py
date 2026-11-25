"""Grid 2 (posts 10-18) · APPROVED DESIGN · the spec any session rebuilds from.

Approved by Ryan in the Nov 17 chat "Current Social Plan - Organizing brand assets project"
(Grids 1-4 draft), rebuilt and checked Nov 18. Do not reinterpret: build exactly this.

Backgrounds are Runway task ids. Signed URLs expire after a day, so fetch a fresh URL with
Runway get_task(id) and save it to $OURKAI_WORK/bg/<bg>.png before building.
paper and slate are the shared textures for graphic tiles.

Look rules (match the live Grid 1):
- kickers in the palace grey: DARK['label'] = DARK['soft'], LIGHT['label'] = LIGHT['soft']
- no wordmark on outer tiles
- fonts only from the engine3 type lock (render.py refuses fallbacks)

Layout on the profile (Lo Shu, newest top left):
    10 · 4 SE   15 · 9 S    11 · 2 SW
    16 · 3 E    14 · 5 C    17 · 7 W
    12 · 8 NE   18 · 1 N    13 · 6 NW
Fill (posting) order: 13, 18, 12, 17, 14, 16, 11, 15, 10.

Nov 18 revision (Ryan chose set B): 10 frost on glass, 11 rings on water, 13 deep indigo (dark).
13 is a deliberate dark corner: it breaks the light/dark checkerboard at 6 NW by choice.
redwood and hills are retired from this grid (kept in BACKGROUNDS for reference).
"""
import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
WORK = _os.environ.get('OURKAI_WORK', '/home/claude/work')

BACKGROUNDS = {
    'redwood': 'de9c577a-0faf-4fde-9b31-231e17e72251',   # G2-4SE · pale mist in a redwood forest
    'ember':   'a0a9dfe1-43c9-4226-adf3-1f452d97914b',   # G2-9S  · ember in dark ash, calm lower 40%
    'hills':   '3d841d08-0189-47bb-b785-3ea78ffdee8d',   # G2-2SW · low sun over golden hills, calm upper 55%
    'rain':    'e2e4fe7c-c37d-49f7-81b8-0820af12e818',   # G2-3E  · rain on dark water, calm upper 50%
    'frost':   'ef7e420a-be96-4be9-ad7f-7642f6ad1896',   # G2-4SE · frost melting on a pale window (chosen Nov 18, set B)
    'rings':   '35f01ebe-d390-4b64-910b-967016e8583f',   # G2-2SW · rings on still pale water, calm upper (chosen Nov 18, set B)
    'indigo':  'c1643c7e-7479-442e-9690-d2e171f52fb4',   # G2-6NW · deep indigo hand-dyed cloth (chosen Nov 18, set B)
    'paper':   '2ce98312-8a6f-42ea-9cdc-dc6ae3824c10',   # shared paper texture
    'slate':   '5ddfefae-351d-40c8-8d28-99d76b29f0f0',   # shared slate texture
}

# template: horizon | sky | plate | character | question  (engine3/templates.py)
TILES = [
    dict(post=10, slug='phases-not-things', template='horizon', bg='frost', dark=False, kicker='The five elements', palace='4 · SE · 10',
         head="They're phases, not things.", body='Wood, Fire, Earth, Metal, Water:', accent='five ways energy moves.'),
    dict(post=15, slug='everything-feeds', template='horizon', bg='ember', dark=True, kicker='The cycles', palace='9 · S · 15',
         head='Everything feeds something.', body='Wood feeds Fire. Fire makes Earth.', accent='The Production cycle.'),
    dict(post=11, slug='your-center', template='sky', bg='rings', dark=False, kicker='The five elements', palace='2 · SW · 11',
         head='Which element is your center?', body='Your Day Master belongs to one of five.', accent='Which is yours?'),
    dict(post=16, slug='everything-checked', template='sky', bg='rain', dark=True, kicker='The cycles', palace='3 · E · 16',
         head='Everything is checked by something.', body='Water puts out Fire. Fire melts Metal.', accent='The Controlling cycle.'),
    dict(post=14, slug='major-snow', template='character', bg='paper', dark=False, kicker='大雪 · Major Snow', palace='5 · Center · 14', char='大雪',
         head='The darkest month begins.', body='Dec 6, 6:52 PM Pacific.', accent='Dec 7 in Asia.'),
    dict(post=17, slug='feed-can-tire', template='plate', bg='slate', dark=True, kicker='The cycles', palace='7 · W · 17', art=('cycle', True, True),
         head='What you feed can tire you.', body='Fire burns through Wood. Wood drinks Water.', accent='The Weakening cycle.', cta='Save this'),
    dict(post=12, slug='every-season', template='plate', bg='paper', dark=False, kicker='The five elements', palace='8 · NE · 12', art=('five_seasons', False),
         head='One element for every season.', body=None, accent=None, cta='Swipe for all five →', carousel='slides 2-5 to build'),
    dict(post=18, slug='who-feeds-you', template='question', bg='slate', dark=True, kicker='Find yourself', palace='1 · N · 18',
         head='Who feeds you? Who drains you?', sub='The same three cycles run between people.', cta='Tag someone'),
    dict(post=13, slug='winter-water', template='character', bg='indigo', dark=True, kicker='Find yourself', palace='6 · NW · 13', char='水',
         head='Winter belongs to Water.', body='Right now, the season is', accent="Water's."),
]


def build(bgdir=_os.path.join(WORK, 'bg')):
    """Return [(post, html)] in profile order, using the engine3 templates."""
    import sys
    sys.path.insert(0, _os.path.normpath(_os.path.join(_HERE, '..')))
    import ourkai_type as T
    T.DARK['label'] = T.DARK['soft']
    T.LIGHT['label'] = T.LIGHT['soft']
    import templates as TP
    out = []
    for t in TILES:
        src = f"file://{bgdir}/{t['bg']}.png"
        k = t['template']
        if k == 'horizon':
            h = TP.horizon(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('body'), t.get('accent'), t.get('cta'))
        elif k == 'sky':
            h = TP.sky(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('body'), t.get('accent'), t.get('cta'))
        elif k == 'plate':
            name, *args = t['art']
            art = getattr(TP, 'art_' + name)(*args)
            h = TP.plate(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('body'), t.get('accent'), art=art, cta=t.get('cta'))
        elif k == 'character':
            h = TP.character(src, t['dark'], t['kicker'], t['palace'], t['char'], t['head'], t.get('body'), t.get('accent'), t.get('cta'))
        elif k == 'question':
            h = TP.question(src, t['dark'], t['kicker'], t['palace'], t['head'], t.get('sub'), t.get('cta'))
        out.append((t['post'], h))
    return out


# Post 12 carousel, slides 2-5, on the shared paper (built Nov 25; same layout as the Grid 3 carousels).
# Sources: five phases, seasons and directions (Huainanzi 3, Su Wen 4); Earth rules the last 18 days of each
# season and the center (Su Wen 29); winter is for storing (Su Wen 2).
EL12 = {'木': '#6b8e6e', '火': '#b14a36', '土': '#a4813a', '金': '#8a8578', '水': '#3f68a8'}  # art_five_seasons colours on light
SLIDES12 = [
    dict(n=2, chars='木火', label='Mù · Huǒ · spring and summer', head='Wood grows. Fire peaks.',
         body='Wood rules spring and the east: things start, stretch and reach. Fire rules summer and the south: everything out in the open, at full strength.'),
    dict(n=3, chars='金水', label='Jīn · Shuǐ · autumn and winter', head='Metal gathers. Water stores.',
         body='Metal rules autumn and the west: the harvest is cut and kept. Water rules winter and the north: life goes quiet and deep, saving its strength.'),
    dict(n=4, chars='土', label='Tǔ · the turns between', head='Earth holds the turns.',
         body='Earth has no season of its own. In the classical map it rules the last eighteen days of each one, and the center: the pause where one season hands to the next.'),
    dict(n=5, chars='row', label="Now · Water's season", head="Winter is Water's turn.",
         body="The classics say store, not spend: rest earlier, finish what's open, plan the spring. Your element is one layer. Your full chart is the rest.",
         cta='Save this'),
]


def build_slides(bgdir=_os.path.join(WORK, 'bg')):
    """Return [(name, html)] for post 12's carousel slides 2-5."""
    import sys
    sys.path.insert(0, _os.path.normpath(_os.path.join(_HERE, '..')))
    import ourkai_type as T
    T.LIGHT['label'] = T.LIGHT['soft']
    c = T.LIGHT
    out = []
    for s in SLIDES12:
        if s['chars'] == 'row':
            cells = ''.join(
                f'<div class="ok-zh" style="font-size:44px;color:{col};opacity:{1 if z == "水" else .32}">{z}</div>'
                for z, col in EL12.items())
            art = f'<div style="position:absolute;left:40px;right:40px;top:110px;display:flex;justify-content:space-between">{cells}</div>'
            label_top = 200
        else:
            size = 150 if len(s['chars']) == 1 else 118
            chars = ''.join(f'<span style="color:{EL12[z]};margin:0 6px">{z}</span>' for z in s['chars'])
            art = f'<div class="ok-zh" style="position:absolute;left:0;right:0;top:{60 if size == 150 else 76}px;text-align:center;font-size:{size}px">{chars}</div>'
            label_top = 238
        art += f'<div class="ok-label" style="position:absolute;left:0;right:0;top:{label_top}px;text-align:center;color:{c["label"]}">{s["label"]}</div>'
        cta = f'<div class="ok-label" style="color:{c["label"]};margin-top:16px">{s["cta"]}</div>' if s.get('cta') else ''
        h = (f'<div class="ok-tile" style="background:{c["ground"]}"><img class="bg" src="file://{bgdir}/paper.png" alt="">'
             f'<div class="ok-top"><span class="ok-label" style="color:{c["label"]}">The five elements</span>'
             f'<span class="ok-label" style="color:{c["soft"]}">{s["n"]} / 5</span></div>'
             f'<div class="ok-rule" style="background:{c["rule"]}"></div>{art}'
             f'<div class="ok-foot"><div class="ok-head" style="color:{c["head"]}">{s["head"]}</div>'
             f'<div class="ok-body" style="color:{c["body"]}">{s["body"]}</div>{cta}</div></div>')
        out.append((f'G2-12_every-season_slide-{s["n"]}', h))
    return out
