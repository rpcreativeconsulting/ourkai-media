"""Grid 2 (posts 10-18) · APPROVED DESIGN · the spec any session rebuilds from.

Approved by Ryan in the Nov 17 chat "Current Social Plan - Organizing brand assets project"
(Grids 1-4 draft), rebuilt and checked Nov 18. Do not reinterpret: build exactly this.

Backgrounds are Runway task ids. Signed URLs expire after a day, so fetch a fresh URL with
Runway get_task(id) and save it to /home/claude/relaunch/render/bg/<bg>.png before building.
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
    dict(post=10, template='horizon', bg='frost', dark=False, kicker='The five elements', palace='4 · SE · 10',
         head="They're phases, not things.", body='Wood, Fire, Earth, Metal, Water:', accent='five ways energy moves.'),
    dict(post=15, template='horizon', bg='ember', dark=True, kicker='The cycles', palace='9 · S · 15',
         head='Everything feeds something.', body='Wood feeds Fire. Fire makes Earth.', accent='The Production cycle.'),
    dict(post=11, template='sky', bg='rings', dark=False, kicker='The five elements', palace='2 · SW · 11',
         head='Which element is your center?', body='Your Day Master belongs to one of five.', accent='Which is yours?'),
    dict(post=16, template='sky', bg='rain', dark=True, kicker='The cycles', palace='3 · E · 16',
         head='Everything is checked by something.', body='Water puts out Fire. Fire melts Metal.', accent='The Controlling cycle.'),
    dict(post=14, template='character', bg='paper', dark=False, kicker='大雪 · Major Snow', palace='5 · Center · 14', char='大雪',
         head='The darkest month begins.', body='Dec 6, 6:52 PM Pacific.', accent='Dec 7 in Asia.'),
    dict(post=17, template='plate', bg='slate', dark=True, kicker='The cycles', palace='7 · W · 17', art=('cycle', True, True),
         head='What you feed can tire you.', body='Fire burns through Wood. Wood drinks Water.', accent='The Weakening cycle.', cta='Save this'),
    dict(post=12, template='plate', bg='paper', dark=False, kicker='The five elements', palace='8 · NE · 12', art=('five_seasons', False),
         head='One element for every season.', body=None, accent=None, cta='Swipe for all five →', carousel='slides 2-5 to build'),
    dict(post=18, template='question', bg='slate', dark=True, kicker='Find yourself', palace='1 · N · 18',
         head='Who feeds you? Who drains you?', sub='The same three cycles run between people.', cta='Tag someone'),
    dict(post=13, template='character', bg='indigo', dark=True, kicker='Find yourself', palace='6 · NW · 13', char='水',
         head='Winter belongs to Water.', body='Right now, the season is', accent="Water's."),
]


def build(bgdir='/home/claude/relaunch/render/bg'):
    """Return [(post, html)] in profile order, using the engine3 templates."""
    import sys
    sys.path.insert(0, '/home/claude/relaunch/engine3')
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
