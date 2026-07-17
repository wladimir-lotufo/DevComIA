import re
import os

letters = {
    'A': "M 0,10 L 5,0 L 10,10 M 2.5,5 L 7.5,5",
    'B': "M 0,10 L 0,0 L 5,0 C 10,0 10,5 5,5 C 10,5 10,10 5,10 L 0,10 M 0,5 L 5,5",
    'C': "M 10,2 C 5,-2 0,0 0,5 C 0,10 5,12 10,8",
    'D': "M 0,10 L 0,0 L 5,0 C 10,0 10,10 5,10 L 0,10",
    'E': "M 10,0 L 0,0 L 0,10 L 10,10 M 0,5 L 8,5",
    'F': "M 10,0 L 0,0 L 0,10 M 0,5 L 8,5",
    'G': "M 10,2 C 5,-2 0,0 0,5 C 0,10 5,12 10,8 L 10,5 L 6,5",
    'H': "M 0,0 L 0,10 M 10,0 L 10,10 M 0,5 L 10,5",
    'I': "M 5,0 L 5,10 M 2,0 L 8,0 M 2,10 L 8,10",
    'J': "M 10,0 L 10,8 C 10,12 0,12 0,8 L 0,6",
    'K': "M 0,0 L 0,10 M 10,0 L 0,5 L 10,10",
    'L': "M 0,0 L 0,10 L 8,10",
    'M': "M 0,10 L 0,0 L 5,5 L 10,0 L 10,10",
    'N': "M 0,10 L 0,0 L 10,10 L 10,0",
    'O': "M 5,0 C -2,0 -2,10 5,10 C 12,10 12,0 5,0 Z",
    'P': "M 0,10 L 0,0 L 5,0 C 10,0 10,5 5,5 L 0,5",
    'Q': "M 5,0 C -2,0 -2,10 5,10 C 12,10 12,0 5,0 Z M 7,8 L 11,12",
    'R': "M 0,10 L 0,0 L 5,0 C 10,0 10,5 5,5 L 0,5 M 5,5 L 10,10",
    'S': "M 10,2 C 5,-2 0,2 5,5 C 10,8 5,12 0,8",
    'T': "M 0,0 L 10,0 M 5,0 L 5,10",
    'U': "M 0,0 L 0,7 C 0,12 10,12 10,7 L 10,0",
    'V': "M 0,0 L 5,10 L 10,0",
    'W': "M 0,0 L 2.5,10 L 5,5 L 7.5,10 L 10,0",
    'X': "M 0,0 L 10,10 M 10,0 L 0,10",
    'Y': "M 0,0 L 5,5 L 10,0 M 5,5 L 5,10",
    'Z': "M 0,0 L 10,0 L 0,10 L 10,10",
    '?': "M 2,3 C 2,-1 8,-1 8,3 C 8,6 5,6 5,8 M 5,10.5 L 5,11.5",
    '~': "M 2.5,-3 C 5,-5 5,-1 7.5,-3",
    '´': "M 4,-1 L 7,-4",
    '¸': "M 5,10 C 2,12 8,12 5,14"
}

def draw_text(text, x, y, scale=1.0, spacing=1.2):
    paths = []
    cx = x
    text = text.upper()
    for char in text:
        if char == ' ':
            cx += 10 * scale * spacing
            continue
            
        has_tilde = False
        has_acute = False
        has_cedil = False
        
        if char in ['Ã', 'Õ']:
            has_tilde = True
            char = 'A' if char == 'Ã' else 'O'
        elif char in ['É', 'Í']:
            has_acute = True
            char = 'E' if char == 'É' else 'I'
        elif char == 'Ç':
            has_cedil = True
            char = 'C'
            
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
                for pt in letters['~'].split(' '):
                    if ',' in pt:
                        px, py = map(float, pt.split(','))
                        paths.append(f"{cx + px * scale},{y + py * scale}")
                    else:
                        paths.append(pt)
            if has_acute:
                for pt in letters['´'].split(' '):
                    if ',' in pt:
                        px, py = map(float, pt.split(','))
                        paths.append(f"{cx + px * scale},{y + py * scale}")
                    else:
                        paths.append(pt)
            if has_cedil:
                for pt in letters['¸'].split(' '):
                    if ',' in pt:
                        px, py = map(float, pt.split(','))
                        paths.append(f"{cx + px * scale},{y + py * scale}")
                    else:
                        paths.append(pt)
                        
        cx += 10 * scale * spacing
    
    return " ".join(paths)

files = [
    r"d:\repos\DevComIA\ApresentacaoIA\.assets\tokens.svg",
    r"d:\repos\DevComIA\ApresentacaoIA\.assets\providers.svg",
    r"d:\repos\DevComIA\ApresentacaoIA\.assets\llm_process.svg",
    r"d:\repos\DevComIA\ApresentacaoIA\.assets\aplicacoes.svg",
    r"d:\repos\DevComIA\ApresentacaoIA\.assets\ciclo_feedback.svg"
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find <text ...>TITLE</text>
    match = re.search(r'<text\s+x="([^"]+)"\s+y="([^"]+)".*?>([^<]+)</text>', content)
    if not match:
        print(f"Skipping {fpath}, no <text> found.")
        continue
        
    x_val = float(match.group(1))
    y_val = float(match.group(2))
    title_text = match.group(3)
    
    # Calculate starting x to center the text
    scale = 1.0
    # adjust scale for applications and feedback cycle to fit viewbox
    if "aplicacoes" in fpath:
        scale = 1.5
    if "ciclo_feedback" in fpath:
        scale = 0.6
        
    spacing = 1.2
    total_width = len(title_text) * 10 * scale * spacing
    start_x = x_val - (total_width / 2)
    start_y = y_val - (10 * scale) # move up to align with previous text baseline
    
    path_data = draw_text(title_text, start_x, start_y, scale, spacing)
    
    new_svg = f"""  <!-- Título Desenhado: {title_text.upper()} -->
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <g stroke-width="{2.5 * scale}">
      <path d="{path_data}" stroke="#1a1a1a" />
    </g>
    <g stroke-width="{1.0 * scale}">
      <path d="{path_data}" stroke="#1a1a1a" />
    </g>
  </g>"""

    # Replace <text ...>...</text> with new_svg
    new_content = re.sub(r'<text\s+x="[^"]+"\s+y="[^"]+".*?>[^<]+</text>', new_svg, content)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {fpath}")
