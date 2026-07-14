import math

def draw_text(text, x, y, scale=1.0, spacing=1.2):
    letters = {
        'A': "M 0,10 L 5,0 L 10,10 M 2.5,5 L 7.5,5",
        'C': "M 10,2 C 5,-2 0,0 0,5 C 0,10 5,12 10,8",
        'E': "M 10,0 L 0,0 L 0,10 L 10,10 M 0,5 L 8,5",
        'I': "M 5,0 L 5,10 M 2,0 L 8,0 M 2,10 L 8,10",
        'L': "M 0,0 L 0,10 L 8,10",
        'M': "M 0,10 L 0,0 L 5,5 L 10,0 L 10,10",
        'O': "M 5,0 C -2,0 -2,10 5,10 C 12,10 12,0 5,0 Z",
        'P': "M 0,10 L 0,0 L 5,0 C 10,0 10,5 5,5 L 0,5",
        'Q': "M 5,0 C -2,0 -2,10 5,10 C 12,10 12,0 5,0 Z M 7,8 L 11,12",
        'R': "M 0,10 L 0,0 L 5,0 C 10,0 10,5 5,5 L 0,5 M 5,5 L 10,10",
        'S': "M 10,2 C 5,-2 0,2 5,5 C 10,8 5,12 0,8",
        'T': "M 0,0 L 10,0 M 5,0 L 5,10",
        'U': "M 0,0 L 0,7 C 0,12 10,12 10,7 L 10,0",
        'V': "M 0,0 L 5,10 L 10,0",
        '*': "M 5,0 L 5,10 M 0,2.5 L 10,7.5 M 0,7.5 L 10,2.5",
        '~': "M 2.5,-3 C 5,-5 5,-1 7.5,-3",
        '´': "M 4,-1 L 7,-4",
        '.': "M 4,9 C 4,8 6,8 6,9 C 6,10 4,10 4,9 Z",
        '?': "M 2,3 C 2,-1 8,-1 8,3 C 8,6 5,6 5,8 M 5,10.5 L 5,11.5",
    }

    paths = []
    cx = x
    for char in text:
        if char == ' ':
            cx += 10 * scale * spacing
            continue
        
        has_tilde = False
        has_acute = False
        if char == 'Ã':
            char = 'A'
            has_tilde = True
        elif char == 'Õ':
            char = 'O'
            has_tilde = True
        elif char == 'É':
            char = 'E'
            has_acute = True
            
        if char in letters:
            pts = letters[char].split(' ')
            npts = []
            for pt in pts:
                if ',' in pt:
                    px, py = map(float, pt.split(','))
                    npts.append(f"{cx + px * scale},{y + py * scale}")
                else:
                    npts.append(pt)
            paths.append(" ".join(npts))
            
            if has_tilde:
                pts = letters['~'].split(' ')
                npts = []
                for pt in pts:
                    if ',' in pt:
                        px, py = map(float, pt.split(','))
                        npts.append(f"{cx + px * scale},{y + py * scale}")
                    else:
                        npts.append(pt)
                paths.append(" ".join(npts))
            if has_acute:
                pts = letters['´'].split(' ')
                npts = []
                for pt in pts:
                    if ',' in pt:
                        px, py = map(float, pt.split(','))
                        npts.append(f"{cx + px * scale},{y + py * scale}")
                    else:
                        npts.append(pt)
                paths.append(" ".join(npts))
                
        cx += 10 * scale * spacing
    
    return " ".join(paths)

# Helper function to shift paths
def shift_path(path_str, dx, dy):
    tokens = path_str.split(' ')
    new_tokens = []
    for t in tokens:
        if ',' in t:
            px, py = map(float, t.split(','))
            new_tokens.append(f"{px+dx},{py+dy}")
        else:
            new_tokens.append(t)
    return " ".join(new_tokens)

# ViewBox dimensions
VB_W = 320
VB_H = 300

# Center Box (IA) - using exactly the old path strings but shifting to new center
# Old center was 100, 100. New center 160, 150
c_x, c_y = 160, 150
dx_center = c_x - 100
dy_center = c_y - 100

box_w, box_h = 40, 40
cx1, cy1 = c_x - box_w/2, c_y - box_h/2
cx2, cy2 = c_x + box_w/2, c_y + box_h/2

box_shadow = f'<path d="M {cx1+5},{cy1+5} L {cx2+5},{cy1+5} L {cx2+5},{cy2+5} L {cx1+5},{cy2+5} Z" stroke="#1a1a1a" opacity="0.2" />'
box_main = f'<path d="M {cx1-1},{cy1+2} L {cx2+2},{cy1-1} L {cx2-1},{cy2+1} L {cx1+2},{cy2-2} Z" stroke="#1a1a1a" />'
box_sketch = f'<path d="M {cx1+1},{cy1-1} L {cx2-2},{cy1+2} L {cx2+1},{cy2-1} L {cx1-2},{cy2+2} Z" stroke="#1a1a1a" />'

text_ia = draw_text("IA", c_x - 11, c_y - 5, scale=1.0)
text_ia_main = f'<path d="{text_ia}" stroke="#1a1a1a" />'
text_ia_sketch = f'<path d="{text_ia}" stroke="#1a1a1a" />'

# Define nodes with exact new coordinates
# New center is X=160, Y=150.
nodes = {
    'llm': {'x': 250, 'y': 150, 'color': '#82e0d8', 'text': 'LLM', 'txt_dx': 5, 'txt_dy': 20, 'orig': (150,100), 
            'shadow': 'M 140,100 C 130,85 170,85 160,100',
            'main': 'M 138,98 C 122,102 118,72 148,68 C 178,68 182,102 158,98 L 157,112 L 152,98 Z',
            'sketch': 'M 142,102 C 120,98 122,68 152,72 C 182,72 178,98 162,102 L 153,108 L 148,102 Z'},
    
    'visao': {'x': 60, 'y': 60, 'color': '#FF904D', 'text': 'VISÃO', 'txt_dx': 0, 'txt_dy': 25, 'orig': (45,35),
              'shadow': 'M 25,35 Q 45,20 65,35',
              'main': 'M 23,37 Q 45,13 67,33 Q 45,57 23,37 Z M 37,35 A 8 8 0 1 0 53,35 A 8 8 0 1 0 37,35',
              'sketch': 'M 27,33 Q 45,17 63,37 Q 45,53 27,33 Z M 39,35 A 6 6 0 1 0 51,35 A 6 6 0 1 0 39,35'},
              
    'ml': {'x': 50, 'y': 120, 'color': '#FF6B6B', 'text': 'ML', 'txt_dx': 5, 'txt_dy': 30, 'orig': (30,80),
           'shadow': 'M 20,95 L 30,80 L 45,65',
           'main': 'M 13,58 L 13,92 L 57,92 M 18,87 L 30,68 L 45,53 M 40,53 L 47,53 L 47,60',
           'sketch': 'M 17,62 L 17,88 L 53,88 M 22,83 L 30,72 L 45,57 M 38,57 L 47,57 L 47,64'},
           
    'astar': {'x': 50, 'y': 180, 'color': '#4ADE80', 'text': 'A*', 'txt_dx': 5, 'txt_dy': 25, 'orig': (30,125),
              'shadow': 'M 5,140 C 15,110 35,140 55,110',
              'main': 'M 3,137 C 15,103 35,137 57,103 M 50,103 L 60,103 M 55,98 L 55,108 M 51.5,99.5 L 58.5,106.5 M 51.5,106.5 L 58.5,99.5',
              'sketch': 'M 7,133 C 15,107 35,133 53,107'},
              
    'outros': {'x': 60, 'y': 240, 'color': '#60A5FA', 'text': 'OUTROS', 'txt_dx': -5, 'txt_dy': 15, 'orig': (45,170),
               'shadow': 'M 30,170 L 60,170',
               'main': 'M 28,163 L 62,167',
               'sketch': 'M 32,167 L 58,163'}
}

shadows, mains, sketches, texts, texts_sk, connectors = [], [], [], [], [], []

for k, n in nodes.items():
    dx = n['x'] - n['orig'][0]
    dy = n['y'] - n['orig'][1]
    col = n['color']
    
    shadow_p = shift_path(n['shadow'], dx, dy)
    main_p = shift_path(n['main'], dx, dy)
    sketch_p = shift_path(n['sketch'], dx, dy)
    
    op = ' opacity="0.2"' if k == 'outros' else ''
    shadows.append(f'<path d="{shadow_p}" stroke="{col}"{op} />')
    mains.append(f'<path d="{main_p}" stroke="{col}" />')
    sketches.append(f'<path d="{sketch_p}" stroke="{col}" />')
    
    txt = draw_text(n['text'], n['x'] - 15 + n['txt_dx'], n['y'] + n['txt_dy'], scale=0.6)
    texts.append(f'<path d="{txt}" stroke="{col}" />')
    texts_sk.append(f'<path d="{txt}" stroke="{col}" />')
    
    if k == 'llm':
        conn_p = f'M {cx2},{c_y} L {n["x"]-20},{n["y"]}'
    else:
        conn_p = f'M {cx1},{c_y} C {cx1-30},{c_y} {n["x"]+20},{n["y"]} {n["x"]+5},{n["y"]}'
    connectors.append(f'<path d="{conn_p}" stroke="{col}" />')

title_text = draw_text("O QUE É IA?", 90, 15, scale=1.4, spacing=1.1)
title_main = f'<path d="{title_text}" stroke="#1a1a1a" />'
title_sketch = f'<path d="{title_text}" stroke="#1a1a1a" />'


svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB_W} {VB_H}" width="100%" height="100%">
  <!-- Design System: MIRA SKETCH -->
  <g fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.5" stroke-width="15">
    {box_shadow}
    {''.join(shadows)}
  </g>

  <!-- Conectores -->
  <g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" stroke-dasharray="6,4">
    {''.join(connectors)}
  </g>

  <!-- 4. Contornos e Rabiscos -->
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <g stroke-width="4.5">
      {box_main}
      {''.join(mains)}
    </g>
    <g stroke-width="2.0">
      {box_sketch}
      {''.join(sketches)}
    </g>
    <g stroke-width="2.5">
      {text_ia_main}
      {''.join(texts)}
      {title_main}
    </g>
    <g stroke-width="1.0">
      {text_ia_sketch}
      {''.join(texts_sk)}
      {title_sketch}
    </g>
  </g>
</svg>
"""

with open(".assets/ai_types.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)

print("Gerado com sucesso!")
