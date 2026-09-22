#!/usr/bin/env python3
"""Build original, self-contained animated SVGs. Requires: pip install fonttools."""
from pathlib import Path
from html import escape
import math
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
    pen = SVGPathPen(glyphs)
    advance = 0
    for char in text:
        name = cmap[ord(char)]
        glyphs[name].draw(TransformPen(pen, (1, 0, 0, 1, advance, 0)))
        advance += glyphs[name].width + tracking * units / size
    scale = size / units
    return f'<path aria-label="{escape(text)}" fill="{color}" transform="translate({x} {y}) scale({scale} {-scale})" d="{pen.getCommands()}"/>'


PALETTES = {
    'light': dict(bg='#F4F7FC', ink='#17263D', muted='#52647B', line='#D9E2ED', accent='#007B8C', lime='#47752A', wash='#E6EEF8', surface='#FFFFFF'),
    'dark': dict(bg='#0C1525', ink='#ECF3FF', muted='#90A5BE', line='#24354D', accent='#50E3EF', lime='#C5F76B', wash='#14263C', surface='#102038'),
}

CSS = '''
.float{animation:float 6s ease-in-out infinite}
.float-alt{animation:float 6s ease-in-out -3s infinite}
.flow{stroke-dasharray:8 140;animation:flow 3.6s linear infinite}
.flow-fast{stroke-dasharray:5 75;animation:flow 2.4s linear infinite reverse}
.breathe{animation:breathe 3.8s ease-in-out infinite}
.twinkle{animation:twinkle 4s ease-in-out infinite}
.scan{animation:scan 4.8s ease-in-out infinite}
.turn{transform-box:fill-box;transform-origin:center;animation:turn 30s linear infinite}
.bar{transform-box:fill-box;transform-origin:bottom;animation:bar 3.2s ease-in-out infinite alternate}
.tile{animation:tile 3.2s ease-in-out infinite}
.cursor{animation:cursor 1.6s steps(2,end) infinite}
.track{animation:track 5s ease-in-out infinite}
.code-line{stroke-dasharray:160;animation:code 4s ease-in-out infinite}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
@keyframes flow{to{stroke-dashoffset:-296}}
@keyframes breathe{0%,100%{opacity:.35}50%{opacity:1}}
@keyframes twinkle{0%,100%{opacity:.18}50%{opacity:.8}}
@keyframes scan{0%,100%{transform:translateX(-45px);opacity:.1}50%{transform:translateX(45px);opacity:.85}}
@keyframes turn{to{transform:rotate(360deg)}}
@keyframes bar{from{transform:scaleY(.35);opacity:.4}to{transform:scaleY(1);opacity:1}}
@keyframes tile{0%,100%{opacity:.2}45%,60%{opacity:1}}
@keyframes cursor{0%,100%{opacity:.25}50%{opacity:1}}
@keyframes track{0%,100%{transform:translate(0,0)}50%{transform:translate(16px,-6px)}}
@keyframes code{0%,12%{stroke-dashoffset:150;opacity:.3}55%,85%{stroke-dashoffset:0;opacity:1}100%{stroke-dashoffset:150;opacity:.3}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}
'''


def svg(w, h, title, desc, body, static=False, defs=''):
    style = '' if static else f'<style>{CSS}</style>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
{style}<defs>{defs}</defs>{body}</svg>'''


def processor():
    """An isometric edge processor, drawn as layers and circuit traces."""
    s = []
    # Ambient orbital paths and a circuit substrate.
    s.append('<ellipse cx="236" cy="285" rx="205" ry="100" fill="url(#aura)"/>')
    s.append('<ellipse cx="236" cy="241" rx="211" ry="111" fill="none" stroke="#284966" stroke-dasharray="2 10"/>')
    s.append('<path d="M26 231L236 111L446 231L236 351Z" fill="#091A2D" stroke="#24445E"/>')
    s.append('<path d="M26 231V244L236 365L446 244V231L236 351Z" fill="#0A1322" stroke="#234059"/>')
    # Multiple animated packet routes feed the central compute die.
    routes = ['M39 232L106 193L173 232', 'M433 232L365 193L299 231',
              'M109 309L170 274L201 292', 'M364 309L303 274L269 293',
              'M108 181L163 149L215 179', 'M365 179L308 147L258 176']
    for i, d in enumerate(routes):
        s.append(f'<path d="{d}" fill="none" stroke="#254D67" stroke-width="2"/>')
        s.append(f'<path class="flow" style="animation-delay:-{i*.65}s" d="{d}" fill="none" stroke="{["#55E6F1", "#C5F76B"][i%2]}" stroke-width="2.5" stroke-linecap="round"/>')
    # Pins follow the two visible package edges.
    for i in range(8):
        a = 147+i*11
        b = 221+i*6.3
        s.append(f'<path d="M{a} {b}l-17 10v8l17-10 M{472-a} {b}l17 10v8l-17-10" fill="none" stroke="#527389" stroke-width="3"/>')
    s.append('<g class="float">')
    s.append('<path d="M133 208L236 149L339 208V235L236 294L133 235Z" fill="url(#package)" stroke="#47708B"/>')
    s.append('<path d="M133 208L236 267L339 208L236 149Z" fill="url(#chipTop)" stroke="#64D4E9" stroke-width="1.3"/>')
    s.append('<path d="M145 208L236 156L327 208L236 260Z" fill="none" stroke="#508BA5" opacity=".7"/>')
    s.append('<path d="M236 267V294" stroke="#47708B"/>')
    s.append('<path class="breathe" d="M133 220L236 279L339 220" fill="none" stroke="#4EE9F0" stroke-width="2"/>')
    # Compute tiles, in perspective; the die has its own light sweep.
    s.append('<g transform="matrix(.92 .53 -.92 .53 236 170)">')
    s.append('<rect width="72" height="72" rx="5" fill="#0C2639" stroke="#7FDDE3"/>')
    for r in range(4):
        for c in range(4):
            s.append(f'<rect class="tile" style="animation-delay:-{(r+c)*.34}s" x="{7+c*15}" y="{7+r*15}" width="12" height="12" rx="2" fill="{["#50DDE9", "#BCF575"][(r+c)%3==0]}" opacity=".7"/>')
    s.append('</g>')
    s.append('<path d="M133 196L236 137L339 196L236 255Z" fill="none" stroke="#73DCE7" stroke-dasharray="3 6" opacity=".2"/>')
    s.append('</g>')
    # Floating model plate above the hardware.
    s.append('<g class="float-alt"><path d="M166 120L236 80L306 120L236 160Z" fill="#173547" fill-opacity=".6" stroke="#5AA8BB" stroke-opacity=".8"/>')
    s.append('<path d="M182 120L236 89L290 120L236 151Z" fill="none" stroke="#68EAEE" opacity=".55"/>')
    for i in range(4):
        s.append(f'<path class="breathe" style="animation-delay:-{i*.8}s" d="M{194+i*14} {113+i*8}l32-18" stroke="#BAEF77" stroke-width="3"/>')
    s.append('</g>')
    s.append('<path d="M236 162V188 M182 153V199 M290 153V199" fill="none" stroke="#5BE5EA" stroke-dasharray="2 6" opacity=".45" class="flow-fast"/>')
    # Device nodes located on the perimeter.
    for x, y, color in [(72,214,'#57DBEC'), (390,214,'#C5F76B'), (152,306,'#C5F76B'), (322,306,'#57DBEC')]:
        s.append(f'<path d="M{x-16} {y}l16-9 16 9-16 9Z" fill="#123046" stroke="{color}"/><circle class="breathe" cx="{x}" cy="{y}" r="3" fill="{color}"/>')
    s.append('<g stroke="#6D94AD" fill="none"><path d="M76 177V130H116 M362 176V115H325" stroke-width=".8"/></g>')
    s += [lettering('INPUT', 58, 119, 9, '#9BB6CC', 1),lettering('INFERENCE', 326, 103, 9, '#9BB6CC', .7)]
    return ''.join(s)


def hero(theme, mobile, static):
    w, h = (640, 740) if mobile else (960, 440)
    defs = '''
<linearGradient id="back" x2="1" y2="1"><stop stop-color="#101C32"/><stop offset="1" stop-color="#050C16"/></linearGradient>
<radialGradient id="glow"><stop stop-color="#17566C" stop-opacity=".5"/><stop offset="1" stop-color="#0A1324" stop-opacity="0"/></radialGradient>
<radialGradient id="aura"><stop stop-color="#1EB7C4" stop-opacity=".28"/><stop offset="1" stop-color="#1EB7C4" stop-opacity="0"/></radialGradient>
<linearGradient id="chipTop" x2="1" y2="1"><stop stop-color="#214A63"/><stop offset=".5" stop-color="#133348"/><stop offset="1" stop-color="#0B1A2F"/></linearGradient>
<linearGradient id="package" x2="1"><stop stop-color="#193D51"/><stop offset="1" stop-color="#071722"/></linearGradient>
<linearGradient id="name" x2=".9" y2="1"><stop stop-color="#FFFFFF"/><stop offset="1" stop-color="#B5CADF"/></linearGradient>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r=".7" fill="#7692AF" opacity=".19"/></pattern>
'''
    s = [f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="18" fill="url(#back)" stroke="{PALETTES[theme]["line"]}"/>',
         f'<rect x="16" y="16" width="{w-32}" height="{h-32}" rx="12" fill="url(#dots)"/>',
         f'<ellipse cx="{w*.76}" cy="{h*.52}" rx="340" ry="270" fill="url(#glow)"/>']
    if mobile:
        s += [lettering('MAXMA615 / ENGINEERING', 36, 42, 13, '#9CB5CB', 1.5),
              '<circle class="breathe" cx="588" cy="37" r="4" fill="#C5F76B"/>',
              lettering('Max.Ma', 32, 154, 108, 'url(#name)', -5),
              lettering('EDGE COMPUTING', 38, 199, 24, '#C5F76B', 1.9),
              lettering('Intelligence, on device.', 38, 241, 25, '#D8E7F3', -.4),
              '<path d="M38 271H602" stroke="#263C54"/>',
              '<g transform="translate(17 247) scale(1.26)">'+processor()+'</g>',
              '<path d="M38 672H602" stroke="#263C54"/>',
              lettering('PYTHON / LINUX / RDK / BPU', 38, 709, 16, '#9CB5CB', 1)]
    else:
        s += [lettering('MAXMA615 / ENGINEERING', 44, 42, 11, '#9CB5CB', 1.3),
              '<circle class="breathe" cx="892" cy="37" r="3" fill="#C5F76B"/>',
              lettering('EDGE AI', 827, 42, 10, '#C5F76B', 1),
              lettering('Max.Ma', 37, 173, 116, 'url(#name)', -5.6),
              lettering('EDGE COMPUTING', 45, 219, 22, '#C5F76B', 1.8),
              lettering('Intelligence,', 45, 278, 32, '#D8E7F3', -.7),
              lettering('on device.', 45, 316, 32, '#D8E7F3', -.7),
              '<g transform="translate(467 18) scale(.98)">'+processor()+'</g>',
              '<path d="M44 369H916" stroke="#263C54"/>',
              lettering('PYTHON / LINUX / RDK / BPU', 45, 408, 11, '#9CB5CB', 1),
              lettering('QUANTIZE', 589, 408, 10, '#BCD1E1', 1),
              lettering('DEPLOY', 712, 408, 10, '#BCD1E1', 1),
              lettering('VALIDATE', 818, 408, 10, '#BCD1E1', 1)]
        for x in [562,685,791]:
            s.append(f'<circle class="breathe" style="animation-delay:-{x/180}s" cx="{x}" cy="404" r="3" fill="#55E5EA"/>')
    # Fine signals along the lower edge keep the whole cover connected.
    s.append(f'<path d="M22 {h-2}H{w-22}" stroke="#32627A"/>')
    s.append(f'<path class="flow" d="M22 {h-2}H{w-22}" stroke="#65E5EB" stroke-width="2"/>')
    return svg(w,h,'Max.Ma — Edge Computing & AI','Original edge processor artwork with flowing data packets, pulsing compute tiles and floating model layers. '+('Static version.' if static else 'Continuously looping animation.'), ''.join(s),static,defs)


def pipeline(theme,mobile,static):
    p=PALETTES[theme]
    w,h=(640,302) if mobile else (960,166)
    s=[f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="12" fill="{p["bg"]}" stroke="{p["line"]}"/>',lettering('FROM MODEL TO DEVICE',26,32,13,p['muted'],1.1)]
    labels=[('01','MODEL','ONNX'),('02','QUANTIZE','BPU'),('03','DEPLOY','RDK'),('04','VALIDATE','VISION')]
    for i,(n,label,tech) in enumerate(labels):
        x=26+(i%2)*306 if mobile else 26+i*235
        y=53+(i//2)*121 if mobile else 54
        width=276 if mobile else 206
        s.append(f'<rect x="{x}" y="{y}" width="{width}" height="96" rx="8" fill="{p["surface"]}" stroke="{p["line"]}"/>')
        s.append(lettering(n,x+15,y+25,12,p['accent'],1))
        s.append(lettering(label,x+15,y+54,18,p['ink'],.2))
        s.append(lettering(tech,x+15,y+78,10,p['muted'],.9))
        for j in range(5):
            s.append(f'<rect class="bar" style="animation-delay:-{i*.7+j*.3}s" x="{x+width-64+j*8}" y="{y+59-j%3*7}" width="4" height="{21+j%3*7}" rx="2" fill="{p["accent"]}"/>')
        s.append(f'<path class="flow-fast" d="M{x+12} {y+95}H{x+width-12}" fill="none" stroke="{p["accent"]}" stroke-width="2"/>')
        if not mobile and i<3:
            s.append(f'<path d="M{x+214} {y+48}h15m-5-4 5 4-5 4" fill="none" stroke="{p["accent"]}"/>')
    return svg(w,h,'Model → Quantize → Deploy → Validate','An animated overview of model deployment on edge devices; bars and packets are illustrative, not measured performance.', ''.join(s),static)


def card(kind,theme,static):
    p=PALETTES[theme]; s=[]
    s.append(f'<rect width="400" height="144" rx="8" fill="{p["bg"]}"/>')
    for x in range(16,400,20):
        for y in range(14,144,20):
            s.append(f'<circle cx="{x}" cy="{y}" r=".65" fill="{p["muted"]}" opacity=".18"/>')
    if kind=='models':
        for layer,x in enumerate([73,145,217,289]):
            for row in range(4):
                y=28+row*29
                if layer<3:
                    for nxt in [row,(row+1)%4]:
                        d=f'M{x} {y}L{x+72} {28+nxt*29}'
                        s.append(f'<path d="{d}" stroke="{p["line"]}"/><path class="flow-fast" style="animation-delay:-{row*.4+layer*.7}s" d="{d}" stroke="{p["accent"]}" fill="none"/>')
                s.append(f'<circle class="tile" style="animation-delay:-{layer*.5+row*.3}s" cx="{x}" cy="{y}" r="7" fill="{p["accent"]}"/>')
        s.append(lettering('MODEL ZOO', 312, 78, 9,p['muted'],.3))
    elif kind=='quantization':
        for j in range(15):
            height=18+int((math.sin(j*.65)+1)*26)
            s.append(f'<rect class="bar" style="animation-delay:-{j*.15}s" x="{26+j*9}" y="{110-height}" width="5" height="{height}" rx="2" fill="{p["accent"]}"/>')
        s.append(f'<path class="flow-fast" d="M177 74H222m-8-6 8 6-8 6" fill="none" stroke="{p["lime"]}" stroke-width="2"/>')
        for r in range(4):
            for c in range(8):
                s.append(f'<rect class="tile" style="animation-delay:-{(r+c)*.18}s" x="{242+c*15}" y="{40+r*17}" width="11" height="12" rx="2" fill="{p["accent"]}"/>')
        s += [lettering('ONNX',26,27,10,p['muted'],1),lettering('BPU / HBM',242,27,10,p['muted'],1)]
    elif kind=='vision':
        s.append(f'<rect x="38" y="20" width="324" height="108" rx="6" fill="{p["surface"]}" stroke="{p["line"]}"/>')
        s.append(f'<path d="M65 127L153 36H246L335 127 M165 127L188 36 M235 127L211 36" fill="none" stroke="{p["line"]}" stroke-width="2"/>')
        s.append(f'<g class="track"><rect x="153" y="58" width="84" height="47" rx="4" fill="{p["accent"]}" fill-opacity=".07" stroke="{p["accent"]}"/><path d="M153 68V58h10 M227 58h10v10 M237 95v10h-10 M163 105h-10V95" fill="none" stroke="{p["accent"]}" stroke-width="3"/>{lettering("VISION",164,50,9,p["accent"],.8)}</g>')
        s.append(f'<path class="scan" d="M200 25V121" stroke="{p["accent"]}" opacity=".3" stroke-width="2"/>')
    else:
        s.append(f'<rect x="46" y="19" width="308" height="109" rx="7" fill="{p["surface"]}" stroke="{p["line"]}"/>')
        for i,col in enumerate([p['accent'],p['lime'],p['muted']]):
            s.append(f'<circle cx="{62+i*11}" cy="32" r="2.5" fill="{col}"/>')
        s.append(lettering('RDK / DEVELOPER NOTES',180,36,8,p['muted'],.4))
        for i,length in enumerate([198,147,222,165]):
            s.append(f'<path class="code-line" style="animation-delay:-{3-i*.65}s" d="M66 {54+i*18}h{length}" stroke="{p["accent"] if i==0 else p["muted"]}" stroke-width="4" stroke-linecap="round"/>')
        s.append(f'<rect class="cursor" x="240" y="102" width="6" height="9" fill="{p["accent"]}"/>')
    return svg(400,144,f'{kind.title()} — edge computing project', 'A looping decorative illustration. '+('Static version.' if static else 'Not live telemetry.'),''.join(s),static)


if __name__ == '__main__':
    for theme in PALETTES:
        for static in [False,True]:
            suffix='-static' if static else ''
            for mobile in [False,True]:
                device='-mobile' if mobile else ''
                for name,builder in [('hero',hero),('pipeline',pipeline)]:
                    path=OUT/f'{name}-{theme}{device}{suffix}.svg'
                    path.write_text(builder(theme,mobile,static),encoding='utf-8')
                    print(f'{path.relative_to(ROOT)} ({path.stat().st_size:,} bytes)')
            for kind in ['models','quantization','vision','docs']:
                path=OUT/f'card-{kind}-{theme}{suffix}.svg'
                path.write_text(card(kind,theme,static),encoding='utf-8')
                print(f'{path.relative_to(ROOT)} ({path.stat().st_size:,} bytes)')
