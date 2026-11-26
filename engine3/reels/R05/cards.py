import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, '..')))
from cardlib import card, render, SCRIM, TOPSCRIM
WORK = os.environ.get('OURKAI_WORK', '/home/claude/work')
Z = lambda c: f'<span class="zh">{c}</span>'
CARDS = {
 'c1': card(True, bottom=470, kicker='The Cosmic Trinity', head='Heaven, Earth,<br>and you.'),
 'c2': card(True, bottom=470, head=f'{Z("天")} Heaven:<br>the timing.', hm=True, body='The season, the year, the day.', accent='You can read it.'),
 'c3': card(True, bottom=470, head=f'{Z("地")} Earth:<br>the place.', hm=True, body='Your home, your desk, your city.', accent='It shapes your days.'),
 'c4': card(True, bottom=470, head=f'{Z("人")} You: the one<br>you can move.', hm=True, body='Your choices, your next step.', accent='This is where the work is.'),
 'c5': card(True, top=330, center=True, kicker='Your turn', head='Which one<br>runs your week?', hm=True, body='The app reads all three:', accent='Timing, Feng Shui and You.', cta='Send this to someone who needs it'),
 'scrim': SCRIM,
 'topscrim': TOPSCRIM,
}
render(CARDS, f'{WORK}/reels/R05/cards')
