"""Highlight 2 'The app' (Phase 1), five Story frames, 1080 x 1920 (Ryan, Nov 27).

Real app screens, past date (Fri Sep 25), labelled as a sample chart (canon 13).
Text stays inside 280..1500 px. Frame 5 leaves room for the Get notified link sticker.
    python3 engine3/stories_extra/highlight_the-app.py  -> /home/claude/scratch/app/out/1..5.png
"""
import sys
sys.path.insert(0, '/home/claude/ourkai-media/engine3'); sys.path.insert(0, '/home/claude/ourkai-media/engine3/reels')
from cardlib import render

G = '#d4af6e'; INK = '#f5efe0'; SOFT = '#cfc6ae'
SLATE = 'file:///home/claude/work/bg/slate.png'
SRC = 'file:///home/claude/scratch/app/src'
LOCKUP = 'file:///home/claude/ourkai-media/media/brand/ourkai-lockup-vertical-tagline-gold-600.png'


def ground():
    return f'<img src="{SLATE}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'


def head(kicker, title, accent=None, top=300):
    t = title if not accent else title.replace(accent, f'<span style="color:{G}">{accent}</span>')
    return (f'<div class="blk" style="top:{top}px"><div class="k" style="color:{SOFT};font-size:28px;letter-spacing:.26em">{kicker}</div>'
            f'<div style="width:56px;height:3px;background:{G};margin:22px 0 28px"></div>'
            f'<div class="h" style="color:{INK};font-size:88px;line-height:1.04">{t}</div></div>')


def screen(name, label, top=640, w=400):
    h = int(w * 1417 / 700)
    return (f'<img src="{SRC}/{name}.jpg" style="position:absolute;left:{(1080-w)//2}px;top:{top}px;width:{w}px;height:{h}px;'
            f'border-radius:44px;border:2px solid rgba(212,175,110,.45);box-shadow:0 30px 80px rgba(0,0,0,.55)">'
            f'<div class="k" style="position:absolute;left:0;right:0;top:{top+h+22}px;text-align:center;color:{SOFT};'
            f'font-size:24px;letter-spacing:.24em">{label}</div>')


LABEL = 'SAMPLE CHART · FRI SEP 25'

FRAMES = {
    '1': ground()
        + f'<img src="{LOCKUP}" style="position:absolute;left:390px;top:330px;width:300px">'
        + '<div class="blk" style="top:820px;text-align:center">'
          f'<div class="h" style="color:{INK};font-size:96px;line-height:1.05">Read the day<br>before you <span style="color:{G}">live it.</span></div>'
          f'<div class="b" style="color:{SOFT};font-size:42px;margin-top:40px">Four classical systems. One reading of you.<br>Calculated, not guessed.</div></div>',
    '2': ground() + head('YOU', 'What you’re made of.', 'made of.') + screen('you', LABEL),
    '3': ground() + head('TIMING · TODAY', 'Same day. Different for everyone.', 'Different') + screen('today', LABEL),
    '4': ground() + head('FENG SHUI', 'What is your space saying?', 'saying?') + screen('fengshui', LABEL),
    '5': ground()
        + '<div class="blk" style="top:420px;text-align:center">'
          f'<div class="k" style="color:{SOFT};font-size:28px;letter-spacing:.26em">THE APP</div>'
          f'<div style="width:56px;height:3px;background:{G};margin:22px auto 34px"></div>'
          f'<div class="h" style="color:{INK};font-size:100px;line-height:1.04">Want to see <span style="color:{G}">yours?</span></div>'
          f'<div class="b" style="color:{SOFT};font-size:44px;margin-top:40px">Get notified when the app drops.</div></div>'
          f'<img src="{LOCKUP}" style="position:absolute;left:440px;top:1240px;width:200px;opacity:.9">',
}

if __name__ == '__main__':
    render(FRAMES, '/home/claude/scratch/app/out')
