"""oürkai type lock (canon v3). One source for fonts and type settings.

Every post, board and render takes its fonts from here. Values come from
ourkai-brand-kit.md §3 (sizes on a 1080 px post), scaled to the 360 px board
(1080 / 3). Fonts are served from our own files, never from a font CDN, and
render.py refuses to export if any font falls back.
"""
import os as _os
FONT_URL = "file://" + _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "fonts")) + "/"

# Font files. 'local' for rendering here, 'canvas' for the relaunch canvas assets.
FONT_FILES = {
    'local': {
        'Fraunces': FONT_URL + 'Fraunces.woff2',
        'Fraunces-Italic': FONT_URL + 'Fraunces-Italic.woff2',
        'SourceSerif4': FONT_URL + 'SourceSerif4.woff2',
        'SourceSerif4-Italic': FONT_URL + 'SourceSerif4-Italic.woff2',
        'JetBrainsMono': FONT_URL + 'JetBrainsMono.woff2',
        'NotoSerifSC': FONT_URL + 'NotoSerifSC-ourkai.woff2',
    },
    'canvas': {
        'Fraunces': '/_blob/fbe18a7ae8f912f60ba445e96d4af154',
        'Fraunces-Italic': '/_blob/aad35fa93a96d0b09219a8acd0a05d9c',
        'SourceSerif4': '/_blob/ecf539a4a1a2c2ce04e288761568d144',
        'SourceSerif4-Italic': '/_blob/2f534e6e9303cf134b3bc1cd666d38c8',
        'JetBrainsMono': '/_blob/5ae6a96cfde4a6518f749b91c2122b94',
        'NotoSerifSC': '/_blob/ee7405d5882a40b58635a2ee746c69e2',
    },
}

# Brand-kit colours
DARK = dict(ground='#0e0d0b', head='#f5efe0', body='#e6dec8', soft='#b0a78f', label='#8fb19c', accent='#d4af6e', rule='#d4af6e')
LIGHT = dict(ground='#ede6d4', head='#1f2419', body='#3a3f31', soft='#525647', label='#5a7d5e', accent='#1f2419', accent_large='#a47433', rule='#a47433')
# Brand kit: gold on light (#a47433) is for large text only, so small accent phrases on light posts take the headline ink in Fraunces italic.

# Scale: board px = post px / 3
S = 1 / 3

def css(target='local'):
    f = FONT_FILES[target]
    return f"""
@font-face{{font-family:'oK Fraunces';font-style:normal;font-weight:100 900;src:url({f['Fraunces']}) format('woff2')}}
@font-face{{font-family:'oK Fraunces';font-style:italic;font-weight:100 900;src:url({f['Fraunces-Italic']}) format('woff2')}}
@font-face{{font-family:'oK Source Serif';font-style:normal;font-weight:200 900;src:url({f['SourceSerif4']}) format('woff2')}}
@font-face{{font-family:'oK Source Serif';font-style:italic;font-weight:200 900;src:url({f['SourceSerif4-Italic']}) format('woff2')}}
@font-face{{font-family:'oK Mono';font-style:normal;font-weight:100 800;src:url({f['JetBrainsMono']}) format('woff2')}}
@font-face{{font-family:'oK Noto SC';font-style:normal;font-weight:400;src:url({f['NotoSerifSC']}) format('woff2')}}
.ok-tile{{position:relative;width:360px;height:480px;overflow:hidden}}
.ok-tile img.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.ok-top{{position:absolute;left:29px;right:29px;top:32px;display:flex;justify-content:space-between}}
.ok-rule{{position:absolute;left:29px;top:54px;width:22px;height:1.5px}}
.ok-foot{{position:absolute;left:29px;right:29px;bottom:32px;display:flex;flex-direction:column}}
.ok-label{{font-family:'oK Mono';font-weight:400;font-size:{28*S:.2f}px;letter-spacing:0.22em;text-transform:uppercase;line-height:1.3}}
.ok-pinyin{{font-family:'oK Mono';font-weight:300;font-size:{26*S:.2f}px;letter-spacing:0.14em;text-transform:uppercase}}
.ok-head{{font-family:'oK Fraunces';font-style:italic;font-weight:300;font-size:{104*S:.2f}px;letter-spacing:-0.026em;line-height:1.07;font-variation-settings:'opsz' 144}}
.ok-head.small{{font-size:{80*S:.2f}px}}
.ok-head.big{{font-size:{168*S:.2f}px}}
.ok-body{{font-family:'oK Source Serif';font-weight:400;font-size:{42*S:.2f}px;line-height:1.55;font-variation-settings:'opsz' 20;margin-top:12px}}
.ok-accent{{font-family:'oK Fraunces';font-style:italic;font-weight:400;font-variation-settings:'opsz' 72}}
.ok-num{{font-family:'oK Fraunces';font-style:normal;font-weight:300;font-size:{96*S:.2f}px;font-variation-settings:'opsz' 144}}
.ok-zh{{font-family:'oK Noto SC';font-weight:400;line-height:1}}
.ok-zh.row{{font-size:{120*S:.2f}px}}
.ok-zh.hero{{font-size:{440*S:.2f}px}}
.ok-tag{{font-family:'oK Mono';font-weight:400;font-size:{28*S:.2f}px;letter-spacing:0.38em;text-transform:uppercase}}
"""

# The font families render.py must find loaded before it exports anything
REQUIRED = [
    "300 italic 20px 'oK Fraunces'",
    "400 italic 20px 'oK Fraunces'",
    "400 20px 'oK Source Serif'",
    "400 20px 'oK Mono'",
    "400 20px 'oK Noto SC'",
]


def tile(img, alt, dark, kicker, palace, headline, body=None, accent=None, extra='', cta=None, head_cls='', middle=''):
    """A standard outer post: label and palace top, art in the middle, headline and body anchored to the bottom (brand kit §5)."""
    c = DARK if dark else LIGHT
    b = ''
    if body:
        acc = f' <span class="ok-accent" style="color:{c["accent"]}">{accent}</span>' if accent else ''
        b = f'<div class="ok-body" style="color:{c["body"]}">{body}{acc}</div>'
    cta_html = f'<div class="ok-label" style="color:{c["label"]};margin-top:16px">{cta}</div>' if cta else ''
    return (f'<div class="ok-tile" style="background:{c["ground"]}">'
            f'<img class="bg" src="{img}" alt="{alt}">{extra}'
            f'<div class="ok-top"><span class="ok-label" style="color:{c["label"]}">{kicker}</span>'
            f'<span class="ok-label" style="color:{c["soft"]}">{palace}</span></div>'
            f'<div class="ok-rule" style="background:{c["rule"]}"></div>{middle}'
            f'<div class="ok-foot"><div class="ok-head {head_cls}" style="color:{c["head"]}">{headline}</div>{b}{cta_html}</div>'
            f'</div>')
