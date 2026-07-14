import math
import random

def sketchy_line(x1, y1, x2, y2, is_main=True):
    if is_main:
        return f'M {x1:.1f} {y1:.1f} L {x2:.1f} {y2:.1f}'
    else:
        dx = x2 - x1
        dy = y2 - y1
        L = math.hypot(dx, dy)
        if L == 0: return ''
        ux, uy = dx/L, dy/L
        ox, oy = -uy * random.uniform(0.5, 1.5), ux * random.uniform(0.5, 1.5)
        nx1 = x1 + ox - ux * random.uniform(0, 2)
        ny1 = y1 + oy - uy * random.uniform(0, 2)
        nx2 = x2 + ox + ux * random.uniform(0, 2)
        ny2 = y2 + oy + uy * random.uniform(0, 2)
        return f'M {nx1:.1f} {ny1:.1f} L {nx2:.1f} {ny2:.1f}'

def sketchy_circle(cx, cy, r, is_main=True):
    if is_main:
        return f'M {cx} {cy-r} C {cx+r*1.1} {cy-r} {cx+r*1.1} {cy+r} {cx} {cy+r} C {cx-r*1.1} {cy+r} {cx-r*1.1} {cy-r} {cx} {cy-r} Z'
    else:
        r1, r2, r3, r4 = r, r*random.uniform(0.9, 1.1), r, r*random.uniform(0.9, 1.1)
        ox, oy = random.uniform(-1, 1), random.uniform(-1, 1)
        return f'M {cx+ox} {cy-r1+oy} C {cx+r2+ox} {cy-r1+oy} {cx+r2+ox} {cy+r3+oy} {cx+ox} {cy+r3+oy} C {cx-r4+ox} {cy+r3+oy} {cx-r4+ox} {cy-r1+oy} {cx+ox} {cy-r1+oy} Z'

def sketchy_rect(x, y, w, h, is_main=True):
    if is_main:
        return f'M {x} {y} L {x+w} {y} L {x+w} {y+h} L {x} {y+h} Z'
    else:
        return (
            sketchy_line(x, y, x+w, y, False) + ' ' +
            sketchy_line(x+w, y, x+w, y+h, False) + ' ' +
            sketchy_line(x+w, y+h, x, y+h, False) + ' ' +
            sketchy_line(x, y+h, x, y, False)
        )

random.seed(123)

main_paths = []
sketch_paths = []
shadow_paths = []

def add_line(x1, y1, x2, y2, has_arrow=False):
    main_paths.append(sketchy_line(x1, y1, x2, y2, True))
    sketch_paths.append(sketchy_line(x1, y1, x2, y2, False))
    if has_arrow:
        dx, dy = x1-x2, y1-y2
        L = math.hypot(dx, dy)
        if L > 0:
            ux, uy = dx/L, dy/L
            # Arrow head
            ax1 = x2 + ux * 5 - uy * 4
            ay1 = y2 + uy * 5 + ux * 4
            ax2 = x2 + ux * 5 + uy * 4
            ay2 = y2 + uy * 5 - ux * 4
            main_paths.append(sketchy_line(x2, y2, ax1, ay1, True))
            main_paths.append(sketchy_line(x2, y2, ax2, ay2, True))
            sketch_paths.append(sketchy_line(x2, y2, ax1, ay1, False))
            sketch_paths.append(sketchy_line(x2, y2, ax2, ay2, False))

def add_circle(cx, cy, r, inner_r=0, shadow=True):
    main_paths.append(sketchy_circle(cx, cy, r, True))
    sketch_paths.append(sketchy_circle(cx, cy, r, False))
    if inner_r > 0:
        main_paths.append(sketchy_circle(cx, cy, inner_r, True))
        sketch_paths.append(sketchy_circle(cx, cy, inner_r, False))
    if shadow:
        shadow_paths.append(f'<path d="{sketchy_circle(cx, cy, r, True)}" fill="#ffffff" />')
        shadow_paths.append(f'<path d="{sketchy_circle(cx, cy, r, False)}" stroke="#82e0d8" stroke-width="15" fill="none" />')

def add_rect(x, y, w, h, shadow=True):
    main_paths.append(sketchy_rect(x, y, w, h, True))
    sketch_paths.append(sketchy_rect(x, y, w, h, False))
    if shadow:
        shadow_paths.append(f'<path d="{sketchy_rect(x, y, w, h, True)}" fill="#ffffff" />')
        shadow_paths.append(f'<path d="{sketchy_rect(x, y, w, h, False)}" stroke="#82e0d8" stroke-width="15" fill="none" />')

# Build the tree of lines
# Top to knot
add_line(60, 30, 60, 50)
add_rect(56, 50, 8, 8, shadow=False) # knot
add_line(60, 58, 60, 100)
# From left yellow circle to knot
add_line(28, 115, 60, 115, has_arrow=True) # left circle points right? In image it points left
add_line(80, 115, 28, 115, has_arrow=True) # Left arrow
# trunk goes right
add_line(60, 100, 95, 100)
# branch to pie
add_line(95, 100, 95, 65)
add_line(95, 65, 120, 65, has_arrow=True)
# branch down
add_line(95, 100, 95, 130)
# branch to orange circle
add_line(95, 130, 168, 130)
# branch to blue square
add_line(95, 130, 95, 150)
add_line(95, 150, 110, 150)
add_line(110, 150, 110, 165)
add_line(110, 165, 138, 165, has_arrow=True)
# branch from trunk left to bottom cyan circle
add_line(60, 100, 60, 130)
add_line(60, 130, 80, 130)
add_line(80, 130, 80, 175)
add_line(80, 175, 70, 175)

# Text placeholders (horizontal lines)
def add_text_lines(x, y, lines=3):
    for i in range(lines):
        w = random.uniform(20, 35)
        add_line(x, y + i*6, x+w, y + i*6)

add_text_lines(45, 145, 4)
add_text_lines(120, 140, 2)
add_text_lines(70, 85, 2)
add_text_lines(150, 115, 2)

# Nodes
# Top cyan circle
add_circle(60, 20, 12, 5)
# Left yellow circle
add_circle(18, 115, 12, 5)
# Bottom cyan circle
add_circle(60, 180, 12, 5)
# Orange circle
add_circle(180, 130, 12, 5)

# Pie chart
add_circle(135, 60, 12, shadow=True)
# Pie lines
main_paths.append(sketchy_line(135, 60, 135, 48, True))
main_paths.append(sketchy_line(135, 60, 147, 60, True))
sketch_paths.append(sketchy_line(135, 60, 135, 48, False))
sketch_paths.append(sketchy_line(135, 60, 147, 60, False))
# floating slice
main_paths.append('M 138 45 A 12 12 0 0 1 150 56 L 150 50 A 12 12 0 0 0 142 42 Z')
sketch_paths.append('M 138 45 A 12 12 0 0 1 150 56 L 150 50 A 12 12 0 0 0 142 42 Z')

# Bar chart
add_line(105, 120, 140, 120) # base
add_rect(108, 110, 4, 10)
add_rect(114, 105, 4, 15)
add_rect(120, 95, 4, 25)
add_rect(126, 110, 4, 10)
add_rect(132, 100, 4, 20)

# Blue square
add_rect(142, 153, 20, 20)
add_rect(147, 158, 10, 10, shadow=False)

# Gauge
main_paths.append('M 20 85 A 15 15 0 0 1 50 85')
main_paths.append('M 15 85 A 20 20 0 0 1 55 85')
sketch_paths.append('M 20 86 A 15 15 0 0 1 50 86')
sketch_paths.append('M 15 84 A 20 20 0 0 1 55 84')
add_line(15, 85, 55, 85) # base
add_rect(20, 78, 4, 7)
add_rect(28, 75, 4, 10)
add_rect(36, 73, 4, 12)


svg_content = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">',
    '  <!-- ==========================================',
    '       Design System: MIRA SKETCH',
    '       ========================================== -->',
    '  <!-- 1. Fundo Base (Proteção contra Dark Mode) -->',
    '  <rect x="0" y="0" width="200" height="200" fill="#ffffff" />',
    '  <!-- 2 & 3. Sombreamento em Cores (Marcador Aquarela) -->',
    '  <g stroke-linecap="round" stroke-linejoin="round" opacity="0.6">',
    *['    ' + p for p in shadow_paths],
    '  </g>',
    '  <!-- 4. Contornos e Rabiscos (A Caneta Nanquim) -->',
    '  <g stroke="#1a1a1a" fill="none" stroke-linecap="round" stroke-linejoin="round">',
    '    <g stroke-width="4.5">',
    '      <path d="' + ' '.join(main_paths) + '" />',
    '    </g>',
    '    <g stroke-width="2.0">',
    '      <path d="' + ' '.join(sketch_paths) + '" />',
    '    </g>',
    '  </g>',
    '</svg>'
]

with open('diagram.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_content))
print('Done diagram.svg')
