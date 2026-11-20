"""oürkai post templates (canon v3). Each template has one job in the funnel and needs one kind of background.

T1 Horizon   · hook                 · photo, calm lower 40%      · headline and body anchored to the bottom
T2 Sky       · second hook          · photo, calm upper 50%      · headline and body hang from the top
T3 Plate     · depth (save)         · shared paper or slate      · a drawn diagram in the middle, text at the bottom
T4 Character · solar terms, stems   · shared paper or slate      · one large Chinese character, text at the bottom
T5 Question  · find yourself        · shared paper or slate      · a large question, readable as a thumbnail
T6 Brand     · oürkai centers       · the bowl hero              · official lockup only
"""
import sys
sys.path.insert(0, '/home/claude/relaunch/engine3')
from ourkai_type import tile, DARK, LIGHT


def _c(dark):
    return DARK if dark else LIGHT


def _top(c, kicker, palace):
    return (f'<div class="ok-top"><span class="ok-label" style="color:{c["label"]}">{kicker}</span>'
            f'<span class="ok-label" style="color:{c["soft"]}">{palace}</span></div>'
            f'<div class="ok-rule" style="background:{c["rule"]}"></div>')


def _body(c, body, acc):
    if not body:
        return ''
    a = f' <span class="ok-accent" style="color:{c["accent"]}">{acc}</span>' if acc else ''
    return f'<div class="ok-body" style="color:{c["body"]}">{body}{a}</div>'


def _cta(c, cta):
    return f'<div class="ok-label" style="color:{c["label"]};margin-top:16px">{cta}</div>' if cta else ''


def horizon(img, dark, kicker, palace, head, body=None, acc=None, cta=None):
    return tile(img, '', dark, kicker, palace, head, body, acc, cta=cta)


def sky(img, dark, kicker, palace, head, body=None, acc=None, cta=None):
    c = _c(dark)
    return (f'<div class="ok-tile" style="background:{c["ground"]}"><img class="bg" src="{img}" alt="">{_top(c, kicker, palace)}'
            f'<div style="position:absolute;left:29px;right:29px;top:76px">'
            f'<div class="ok-head" style="color:{c["head"]}">{head}</div>{_body(c, body, acc)}{_cta(c, cta)}</div></div>')


def plate(tex, dark, kicker, palace, head, body=None, acc=None, art='', cta=None):
    c = _c(dark)
    return (f'<div class="ok-tile" style="background:{c["ground"]}"><img class="bg" src="{tex}" alt="">{_top(c, kicker, palace)}{art}'
            f'<div class="ok-foot"><div class="ok-head small" style="color:{c["head"]}">{head}</div>{_body(c, body, acc)}{_cta(c, cta)}</div></div>')


def character(tex, dark, kicker, palace, char, head, body=None, acc=None, cta=None, char_color=None):
    c = _c(dark)
    cc = char_color or (DARK['accent'] if dark else LIGHT['accent_large'])
    return (f'<div class="ok-tile" style="background:{c["ground"]}"><img class="bg" src="{tex}" alt="">{_top(c, kicker, palace)}'
            f'<div class="ok-zh" style="position:absolute;left:0;right:0;top:84px;text-align:center;font-size:{150 if len(char) == 1 else 104}px;color:{cc}">{char}</div>'
            f'<div class="ok-foot"><div class="ok-head small" style="color:{c["head"]}">{head}</div>{_body(c, body, acc)}{_cta(c, cta)}</div></div>')


def question(tex, dark, kicker, palace, head, sub=None, cta=None):
    c = _c(dark)
    s = f'<div class="ok-body" style="color:{c["body"]}">{sub}</div>' if sub else ''
    return (f'<div class="ok-tile" style="background:{c["ground"]}"><img class="bg" src="{tex}" alt="">{_top(c, kicker, palace)}'
            f'<div style="position:absolute;left:29px;right:29px;top:150px">'
            f'<div class="ok-head big" style="color:{c["head"]};line-height:1.02">{head}</div>{s}{_cta(c, cta)}</div></div>')


def brand(img, palace):
    return (f'<div class="ok-tile" style="background:{DARK["ground"]}"><img class="bg" src="{img}" alt="">'
            f'<div class="ok-top" style="justify-content:flex-end"><span class="ok-label" style="color:{DARK["accent"]}">{palace}</span></div></div>')


# --- diagram art for plates ---
def art_two_lines():
    return (f'<div style="position:absolute;left:110px;top:130px;width:140px;display:flex;flex-direction:column;gap:26px">'
            f'<div style="height:10px;background:{DARK["accent"]}"></div>'
            f'<div style="height:10px;display:flex;justify-content:space-between"><div style="width:62px;background:{DARK["body"]}"></div><div style="width:62px;background:{DARK["body"]}"></div></div></div>'
            f'<div class="ok-label" style="position:absolute;left:262px;top:128px;color:{DARK["accent"]}">Yang</div>'
            f'<div class="ok-label" style="position:absolute;left:262px;top:164px;color:{DARK["soft"]}">Yin</div>')


def art_four_systems(dark=False):
    c = _c(dark)
    items = [('八字', 'BaZi'), ('風水', 'Feng Shui'), ('通書', 'Tong Shu'), ('奇門', 'Qi Men')]
    cells = ''.join(f'<div style="border:1px solid {c["rule"]};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px">'
                    f'<div class="ok-zh" style="font-size:24px;color:{c["head"]}">{z}</div><div class="ok-label" style="color:{c["label"]}">{e}</div></div>'
                    for z, e in items)
    return f'<div style="position:absolute;left:58px;right:58px;top:84px;height:200px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:10px">{cells}</div>'


def art_five_seasons(dark=False):
    c = _c(dark)
    els = [('#6b8e6e', 'Wood', 'Spring'), ('#b14a36', 'Fire', 'Summer'), ('#a4813a', 'Earth', 'Between'), ('#8a8578', 'Metal', 'Autumn'), ('#3f68a8', 'Water', 'Winter')]
    if dark:
        els = [('#8fb19c', 'Wood', 'Spring'), ('#c0392b', 'Fire', 'Summer'), ('#d4af6e', 'Earth', 'Between'), ('#c7c2b6', 'Metal', 'Autumn'), ('#5b8bd0', 'Water', 'Winter')]
    cols = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px"><div style="width:26px;height:26px;border-radius:13px;background:{col}"></div>'
                   f'<div class="ok-label" style="color:{c["head"]}">{n}</div><div class="ok-pinyin" style="color:{c["label"]}">{s}</div></div>' for col, n, s in els)
    return f'<div style="position:absolute;left:24px;right:24px;top:120px;display:flex;justify-content:space-between">{cols}</div>'


def art_cycle(dark=True, reverse=True):
    """Five elements on a pentagon; arrows show the Production cycle, or reversed for Weakening."""
    import math
    c = _c(dark)
    names = ['木', '火', '土', '金', '水']
    cx, cy, r = 180, 175, 82
    pts = [(cx + r * math.sin(2 * math.pi * i / 5), cy - r * math.cos(2 * math.pi * i / 5)) for i in range(5)]
    arrows = ''
    for i in range(5):
        a, b = (pts[(i + 1) % 5], pts[i]) if reverse else (pts[i], pts[(i + 1) % 5])
        ax, ay = a[0] + (b[0] - a[0]) * 0.25, a[1] + (b[1] - a[1]) * 0.25
        bx, by = a[0] + (b[0] - a[0]) * 0.75, a[1] + (b[1] - a[1]) * 0.75
        arrows += f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{c["rule"]}" stroke-width="1.4" marker-end="url(#ah)"/>'
    labels = ''.join(f'<text x="{x:.1f}" y="{y + 9:.1f}" text-anchor="middle" font-family="oK Noto SC" font-size="26" fill="{c["head"]}">{n}</text>' for (x, y), n in zip(pts, names))
    return (f'<svg style="position:absolute;left:0;top:0" width="360" height="300"><defs><marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">'
            f'<path d="M0,0 L6,3 L0,6" fill="none" stroke="{c["rule"]}" stroke-width="1.2"/></marker></defs>{arrows}{labels}</svg>')
