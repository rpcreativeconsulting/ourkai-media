"""Draft: post 77 · Grid 9 center · 立春 Start of Spring (one moment, several cities)."""
import sys
import os
HERE=os.path.dirname(os.path.abspath(__file__)); WORK=os.environ.get('OURKAI_WORK','/home/claude/work')
sys.path.insert(0, os.path.join(HERE, '..'))
import ourkai_type as T
from ourkai_type import css
from render import render
T.DARK['label'] = T.DARK['soft']
D = T.DARK
BG = f'file://{WORK}/bg/slate.png'

rows = [
    ('Beijing · Singapore', 'Thu Feb 4', '9:46 AM', True),
    ('Seoul · Tokyo', 'Thu Feb 4', '10:46 AM', False),
    ('Sydney', 'Thu Feb 4', '12:46 PM', False),
    ('London', 'Thu Feb 4', '1:46 AM', False),
    ('New York', 'Wed Feb 3', '8:46 PM', False),
    ('California', 'Wed Feb 3', '5:46 PM', False),
]
lab = "font-family:'oK Mono';font-weight:400;font-size:8.6px;letter-spacing:0.16em;text-transform:uppercase;line-height:1"
tbl = ''.join(
    f'<div style="display:flex;justify-content:space-between;padding:5.2px 0;border-top:0.5px solid rgba(237,230,212,0.16)">'
    f'<span style="{lab};color:{D["accent"] if hi else D["soft"]}">{c}</span>'
    f'<span style="{lab};color:{D["accent"] if hi else D["body"]}">{d} · {t}</span></div>'
    for c, d, t, hi in rows)

tile = (f'<div class="ok-tile" style="background:{D["ground"]}"><img class="bg" src="{BG}" alt="">'
        f'<div class="ok-top"><span class="ok-label" style="color:{D["label"]}">立春 · Start of Spring</span>'
        f'<span class="ok-label" style="color:{D["soft"]}">5 · Center · 77</span></div>'
        f'<div class="ok-rule" style="background:{D["rule"]}"></div>'
        f'<div class="ok-zh" style="position:absolute;left:0;right:0;top:96px;text-align:center;font-size:96px;color:{D["accent"]}">立春</div>'
        f'<div class="ok-foot">'
        f'<div class="ok-head small" style="color:{D["head"]}">The Coming of Spring.</div>'
        f'<div class="ok-body" style="color:{D["body"]};margin-top:6px;margin-bottom:10px">The sun reaches 315°. '
        f'<span class="ok-accent" style="color:{D["accent"]}">One moment, everywhere.</span></div>'
        f'{tbl}</div></div>')

head = f'<html><head><meta charset="utf-8"><style>{css()}body{{margin:0}}</style></head><body>'
open(f'{WORK}/p77.html', 'w').write(head + tile + '</body></html>')
os.makedirs(f'{WORK}/out', exist_ok=True)
print(render(f'{WORK}/p77.html', f'{WORK}/out/G9-77_coming-of-spring_DRAFT.png', 360, 480, 3))
