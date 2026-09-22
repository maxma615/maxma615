#!/usr/bin/env python3
"""Regenerate self-contained README artwork. Requires: pip install fonttools."""
from pathlib import Path
from html import escape
import re
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'readme'
font = instantiateVariableFont(TTFont(OUT / 'fonts' / 'SpaceGrotesk.ttf'), {'wght': 650})
glyphs = font.getGlyphSet()
cmap = font.getBestCmap()
units = font['head'].unitsPerEm


def lettering(text, x, y, size, color, tracking=0):
    """Outline the licensed typeface so image rendering needs no installed fonts."""
    pen = SVGPathPen(glyphs)
    advance = 0
    for char in text:
        name = cmap[ord(char)]
        glyphs[name].draw(TransformPen(pen, (1, 0, 0, 1, advance, 0)))
        advance += glyphs[name].width + tracking * units / size
    scale = size / units
    return f'<path aria-label="{escape(text)}" fill="{color}" transform="translate({x} {y}) scale({scale} {-scale})" d="{pen.getCommands()}"/>'


PALETTES = {
    'light': dict(bg='#F3F7F3', ink='#142D26', muted='#4E685E', line='#CCDDD4', accent='#147E64', wash='#DCECE2', arm='#F9FCFA', detail='#78988B'),
    'dark': dict(bg='#111B23', ink='#EBF4EF', muted='#9CB7AA', line='#293F3B', accent='#80E6B8', wash='#1C3730', arm='#192B2D', detail='#5E8779'),
}


def robot(p):
    return f'''
    <ellipse cx="170" cy="238" rx="108" ry="16" fill="{p['wash']}"/>
    <path d="M31 238H282 M170 48V251" stroke="{p['line']}" stroke-dasharray="3 8"/>
    <circle cx="212" cy="87" r="46" fill="none" stroke="{p['line']}"/>
    <circle class="target-ring" cx="212" cy="87" r="59" fill="none" stroke="{p['accent']}" opacity=".25" stroke-dasharray="2 8"/>
    <path d="M147 221V194L115 119L214 67L231 87L146 140L183 194V221Z" fill="{p['arm']}" stroke="{p['detail']}" stroke-width="2.4" stroke-linejoin="round"/>
    <path class="trace" d="M165 215V196L130 132L221 77" fill="none" stroke="{p['accent']}" stroke-width="3" stroke-linecap="round"/>
    <path d="M221 77L246 101L235 117 M246 101L262 89L273 101" fill="none" stroke="{p['ink']}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M242 126L258 135L273 126V110L258 101L242 110Z M242 110L258 119L273 110 M258 119V135" fill="none" stroke="{p['accent']}" stroke-width="1.5"/>
    <g fill="{p['arm']}" stroke="{p['ink']}" stroke-width="2.5">
      <circle cx="165" cy="195" r="14"/><circle cx="130" cy="132" r="19"/><circle cx="221" cy="77" r="11"/>
    </g>
    <g fill="{p['accent']}"><circle cx="165" cy="195" r="4"/><circle cx="130" cy="132" r="6"/><circle cx="221" cy="77" r="3"/></g>
    <path d="M137 217H193L202 235H128Z" fill="{p['arm']}" stroke="{p['detail']}" stroke-width="2.4"/>
    <path d="M141 227H190" stroke="{p['accent']}" stroke-width="2"/>
    <g fill="none" stroke="{p['detail']}" stroke-width="1.3"><path d="M51 71H63M57 65V77 M263 192H275M269 186V198"/></g>
    <path class="scan" d="M231 153L280 153L280 80" fill="none" stroke="{p['accent']}" stroke-width="1.5" stroke-dasharray="4 6" opacity=".4"/>
    '''


def make_svg(theme, mobile):
    p = PALETTES[theme]
    w, h = (640, 520) if mobile else (960, 352)
    artwork = []
    if mobile:
        artwork += [lettering('MAX.MA / FIELD NOTES', 38, 47, 16, p['muted'], 1.4),
                    lettering('Max.Ma', 32, 166, 113, p['ink'], -5),
                    lettering('ROBOTICS & EDGE AI', 39, 208, 23, p['accent'], 1.1)]
        artwork.append(f'<path d="M39 238H601" stroke="{p["line"]}"/>')
        for idx, label in enumerate(['SENSE', 'LEARN', 'BUILD']):
            y = 297 + idx * 62
            artwork.append(lettering(f'0{idx+1}', 39, y, 15, p['accent']))
            artwork.append(lettering(label, 81, y, 22, p['ink'], 1.1))
        artwork.append(f'<g transform="translate(260 207) scale(1.02)">{robot(p)}</g>')
        artwork.append(lettering('MODELS TO MACHINES', 39, 484, 16, p['muted'], 1.4))
        artwork.append(f'<path d="M287 477H594" stroke="{p["line"]}"/><circle class="packet" cx="590" cy="477" r="3" fill="{p["accent"]}"/>')
    else:
        artwork += [lettering('MAX.MA / FIELD NOTES', 49, 49, 12, p['muted'], 1.7),
                    lettering('Max.Ma', 43, 170, 119, p['ink'], -5.2),
                    lettering('ROBOTICS & EDGE AI', 51, 214, 20, p['accent'], 1.3)]
        artwork.append(f'<path d="M51 244H568" stroke="{p["line"]}"/>')
        for idx, label in enumerate(['SENSE', 'LEARN', 'BUILD']):
            x = 51 + idx * 168
            artwork.append(lettering(f'0{idx+1}', x, 277, 11, p['accent'], .7))
            artwork.append(lettering(label, x + 28, 277, 13, p['ink'], .9))
        artwork.append(f'<g transform="translate(584 35) scale(1.08)">{robot(p)}</g>')
        artwork.append(lettering('MODELS TO MACHINES', 51, 322, 10, p['muted'], 1.5))
        artwork.append(f'<path d="M246 318H906" stroke="{p["line"]}"/><circle class="packet" cx="902" cy="318" r="3" fill="{p["accent"]}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">Max.Ma — Robotics &amp; Edge AI</title>
<desc id="desc">A personal profile cover with a robotic arm, outlined Space Grotesk lettering, and a short signal animation. It settles after five seconds and respects reduced motion.</desc>
<style>
.trace{{stroke-dasharray:450;stroke-dashoffset:0;animation:trace 3.2s cubic-bezier(.2,.6,.3,1) 1 both}}
.target-ring{{animation:target 4.6s ease-out 1;transform-box:fill-box;transform-origin:center}}
.scan{{animation:scan 4.6s ease-out 1}}
.packet{{opacity:0;animation:packet 4.6s ease-in-out 1}}
@keyframes trace{{from{{stroke-dashoffset:450}}to{{stroke-dashoffset:0}}}}
@keyframes target{{0%{{transform:scale(.65);opacity:0}}45%{{opacity:.55}}100%{{transform:scale(1);opacity:.25}}}}
@keyframes scan{{0%,100%{{opacity:.4}}40%{{opacity:1;stroke-dashoffset:35}}}}
@keyframes packet{{0%{{transform:translateX(-260px);opacity:0}}20%{{opacity:1}}85%{{opacity:1}}100%{{transform:translateX(0);opacity:0}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{p['line']}" stroke-width=".6" opacity=".28"/></pattern></defs>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="18" fill="{p['bg']}" stroke="{p['line']}"/>
<rect x="24" y="24" width="{w-48}" height="{h-48}" rx="12" fill="url(#grid)"/>
{''.join(artwork)}
</svg>'''


if __name__ == '__main__':
    for theme in PALETTES:
        for mobile in [False, True]:
            path = OUT / f'hero-{theme}{"-mobile" if mobile else ""}.svg'
            path.write_text(make_svg(theme, mobile), encoding='utf-8')
            print(f'{path.relative_to(ROOT)} ({path.stat().st_size:,} bytes)')
            static = re.sub(r'<style>.*?</style>', '<style>.packet{opacity:0}</style>', path.read_text(), flags=re.S)
            static = static.replace('and a short signal animation. It settles after five seconds and respects reduced motion.', 'with a static signal diagram for readers who prefer reduced motion.')
            static_path = path.with_stem(path.stem + '-static')
            static_path.write_text(static, encoding='utf-8')
            print(f'{static_path.relative_to(ROOT)} ({static_path.stat().st_size:,} bytes)')
