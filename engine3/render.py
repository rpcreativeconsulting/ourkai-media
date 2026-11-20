"""Render a board to PNG, and refuse if any brand font did not load."""
import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
WORK = _os.environ.get('OURKAI_WORK', '/home/claude/work')
import sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, _os.path.normpath(_os.path.join(_HERE, '.')))
from ourkai_type import REQUIRED


def render(html_path, png_path, width=1088, height=1448, scale=1):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--allow-file-access-from-files'])
        pg = b.new_page(viewport={'width': width, 'height': height}, device_scale_factor=scale)
        pg.goto('file://' + html_path)
        pg.evaluate("(req) => Promise.all(req.map(f => document.fonts.load(f, 'Aǎ天'))).then(() => document.fonts.ready)", REQUIRED)
        pg.wait_for_timeout(500)
        missing = pg.evaluate("(req) => req.filter(f => !document.fonts.check(f, 'Aǎ天') || ![...document.fonts].some(ff => f.includes(ff.family) && ff.status === 'loaded'))", REQUIRED)
        used = pg.evaluate("[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.style+' '+f.weight)")
        if missing:
            b.close()
            raise SystemExit(f'FONT LOCK FAILED, not rendered. Missing: {missing}')
        pg.screenshot(path=png_path)
        b.close()
        return used


if __name__ == '__main__':
    used = render(sys.argv[1], sys.argv[2], *(int(a) for a in sys.argv[3:]))
    print('fonts loaded:', sorted(set(used)))
