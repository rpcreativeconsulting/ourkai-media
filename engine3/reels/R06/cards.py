import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, '..')))
from cardlib import card, render, SCRIM, TOPSCRIM
WORK = os.environ.get('OURKAI_WORK', '/home/claude/work')
CARDS = {
 'c1': card(True, bottom=470, kicker='BaZi', head='You were born<br>into a moment.'),
 'c2': card(True, bottom=470, head='That moment<br>has four pillars.', hm=True, body='Year, month, day and hour.'),
 'c3': card(True, bottom=470, head='Eight characters.<br><span class="zh">八字</span>, <span class="py">BāZì</span>.', hm=True, body='Each pillar has a stem and a branch.'),
 'c4': card(True, bottom=470, head='Your Day Master<br>is one layer.', hm=True, body='Your full chart', accent='is the rest.'),
 'c5': card(True, top=330, center=True, kicker='Your turn', head='How well do you<br>know your own<br>moment?', hm=True, body="The app's You reads all four pillars,", accent='and shows why.', cta='Comment one word'),
 'scrim': SCRIM,
 'topscrim': TOPSCRIM,
}
render(CARDS, f'{WORK}/reels/R06/cards')
