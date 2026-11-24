"""Shared Reel card renderer (1080 x 1920), the same type as the R04 cards.
Usage from a Reel folder:  from cardlib import card, render ; render({'c1': card(...)}, outdir)
Fonts come only from our files; export stops if any font falls back."""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, '..')))
from ourkai_type import css, REQUIRED, DARK, LIGHT
W, H = 1080, 1920
BASE = """*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1920px;background:transparent;position:relative;overflow:hidden}
.blk{position:absolute;left:96px;right:96px}
.k{font-family:'oK Mono';font-weight:400;font-size:30px;letter-spacing:.24em;text-transform:uppercase}
.r{width:56px;height:3px;margin:22px 0 34px}
.h{font-family:'oK Fraunces';font-style:italic;font-weight:300;font-size:104px;line-height:1.06;letter-spacing:-.025em;font-variation-settings:'opsz' 144}
.h.m{font-size:84px}
.b{font-family:'oK Source Serif';font-weight:400;font-size:46px;line-height:1.45;margin-top:30px;font-variation-settings:'opsz' 20}
.a{font-family:'oK Fraunces';font-style:italic;font-weight:400;font-variation-settings:'opsz' 72}
.py{font-family:'oK Source Serif';font-style:italic;font-weight:400}
.zh{font-family:'oK Noto SC';font-style:normal;font-weight:400;letter-spacing:0}
.cta{font-family:'oK Mono';font-weight:500;font-size:30px;letter-spacing:.26em;text-transform:uppercase;margin-top:56px}
"""
SCRIM = '<div style="position:absolute;left:0;right:0;bottom:0;height:1150px;background:linear-gradient(to bottom,rgba(14,13,11,0) 0%,rgba(14,13,11,.5) 45%,rgba(14,13,11,.78) 100%)"></div>'
TOPSCRIM = '<div style="position:absolute;left:0;right:0;top:0;height:1300px;background:linear-gradient(to top,rgba(14,13,11,0) 0%,rgba(14,13,11,.5) 45%,rgba(14,13,11,.72) 100%)"></div>'


def card(dark, bottom=None, top=None, center=False, kicker=None, head=None, hm=False, body=None, accent=None, cta=None):
    c = DARK if dark else LIGHT
    gold = c['accent'] if dark else c['accent_large']
    pos = f"bottom:{bottom}px" if bottom is not None else f"top:{top}px"
    al = "text-align:center;" if center else ""
    s = f'<div class="blk" style="{pos};{al}">'
    if kicker:
        s += f'<div class="k" style="color:{c["soft"]}">{kicker}</div><div class="r" style="background:{gold};{"margin-left:auto;margin-right:auto" if center else ""}"></div>'
    if head:
        s += f'<div class="h{" m" if hm else ""}" style="color:{c["head"]}">{head}</div>'
    if body:
        acc = f' <span class="a" style="color:{gold if dark else c["head"]}">{accent}</span>' if accent else ''
        s += f'<div class="b" style="color:{c["body"]}">{body}{acc}</div>'
    if cta:
        s += f'<div class="cta" style="color:{gold}">{cta}</div>'
    return s + '</div>'


def page(inner, extra_css=''):
    return f'<html><head><meta charset="utf-8"><style>{css()}{BASE}{extra_css}</style></head><body>{inner}</body></html>'


def check_fonts(pg):
    pg.evaluate("(req)=>Promise.all(req.map(f=>document.fonts.load(f,'Aǎ天'))).then(()=>document.fonts.ready)", REQUIRED)
    pg.wait_for_timeout(300)
    miss = pg.evaluate("(req)=>req.filter(f=>!document.fonts.check(f,'Aǎ天'))", REQUIRED)
    if miss:
        raise SystemExit(f'font lock failed {miss}')


def render(cards, outdir):
    from playwright.sync_api import sync_playwright
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--allow-file-access-from-files'])
        pg = b.new_page(viewport={'width': W, 'height': H})
        for k, v in cards.items():
            f = f'{outdir}/{k}.html'
            open(f, 'w').write(page(v))
            pg.goto(f'file://{f}')
            check_fonts(pg)
            pg.screenshot(path=f'{outdir}/{k}.png', omit_background=True)
        b.close()
    print('cards ok', len(cards))
