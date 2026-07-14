import math
import random

# Brain outline polygon
brain_outline = [
    (50, 130), (40, 110), (35, 90), (45, 60), (70, 40), (100, 30), 
    (130, 35), (155, 55), (170, 80), (175, 100), (170, 130), (150, 150),
    (130, 155), (120, 175), (105, 185), (95, 180), (100, 150), (80, 145), 
    (65, 140)
]

def point_in_polygon(x, y, poly):
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

random.seed(42)

nodes = []
for _ in range(3000):
    x = random.uniform(20, 190)
    y = random.uniform(20, 190)
    if point_in_polygon(x, y, brain_outline):
        too_close = False
        for nx, ny, _ in nodes:
            if math.hypot(nx - x, ny - y) < 8.5:
                too_close = True
                break
        if not too_close:
            r = random.choice([2, 2.5, 3, 3, 4, 4.5, 5])
            nodes.append((x, y, r))

edges = set()
for i, (x1, y1, r1) in enumerate(nodes):
    dists = []
    for j, (x2, y2, r2) in enumerate(nodes):
        if i != j:
            d = math.hypot(x1 - x2, y1 - y2)
            dists.append((d, j))
    dists.sort()
    k = random.randint(3, 5)
    for d, j in dists[:k]:
        if d < 35:
            edges.add(tuple(sorted((i, j))))

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

main_paths = []
sketch_paths = []
for i, j in edges:
    x1, y1, _ = nodes[i]
    x2, y2, _ = nodes[j]
    main_paths.append(sketchy_line(x1, y1, x2, y2, True))
    sketch_paths.append(sketchy_line(x1, y1, x2, y2, False))

node_paths = []
for x, y, r in nodes:
    r1, r2, r3, r4 = r, r*random.uniform(0.9, 1.1), r, r*random.uniform(0.9, 1.1)
    p = f'M {x} {y-r1} C {x+r2} {y-r1} {x+r2} {y+r3} {x} {y+r3} C {x-r4} {y+r3} {x-r4} {y-r1} {x} {y-r1} Z'
    node_paths.append(p)

brain_bg = 'M ' + ' L '.join([f'{x} {y}' for x, y in brain_outline]) + ' Z'

svg_content = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">',
    '  <!-- ==========================================',
    '       Design System: MIRA SKETCH',
    '       ========================================== -->',
    '  <!-- Fundo Base -->',
    '  <rect x="0" y="0" width="200" height="200" fill="#ffffff" />',
    '  <!-- Fundo Cerebro (esconde sobreposicoes traseiras se houver) -->',
    '  <path d="M 40 100 Q 30 70 60 50 Q 100 30 140 50 Q 170 70 170 100 Q 160 140 130 140 Q 120 170 110 180 Q 90 170 95 140 Q 70 145 40 130 Z" fill="#ffffff" />',
    '  <!-- Sombreamento Cyan -->',
    '  <g stroke="#82e0d8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.6">',
    '    <path d="M 70 80 Q 120 60 150 100" stroke-width="18" />',
    '    <path d="M 60 130 Q 100 110 130 140" stroke-width="16" />',
    '    <path d="M 100 140 Q 110 160 110 175" stroke-width="12" />',
    '  </g>',
    '  <!-- Contornos e Rabiscos -->',
    '  <g stroke="#1a1a1a" fill="none" stroke-linecap="round" stroke-linejoin="round">',
    '    <g stroke-width="3.5">',
    '      <path d="' + ' '.join(main_paths) + '" />',
    '    </g>',
    '    <g stroke-width="1.5">',
    '      <path d="' + ' '.join(sketch_paths) + '" />',
    '    </g>',
    '  </g>',
    '  <!-- Nos -->',
    '  <g fill="#1a1a1a">',
    '    <path d="' + ' '.join(node_paths) + '" />',
    '  </g>',
    '</svg>'
]

with open('d:/repos/DevComIA/Samples/brain2.svg', 'w') as f:
    f.write('\n'.join(svg_content))
print(f'Generated SVG with {len(nodes)} nodes and {len(edges)} edges')
