import math

def draw_text(text, x, y, scale=1.0, spacing=1.2):
    letters = {
        'A': "M 0,10 L 5,0 L 10,10 M 2.5,5 L 7.5,5",
        'C': "M 10,2 C 5,-2 0,0 0,5 C 0,10 5,12 10,8",
        'D': "M 0,10 L 0,0 L 5,0 C 10,0 10,10 5,10 L 0,10",
        'E': "M 10,0 L 0,0 L 0,10 L 10,10 M 0,5 L 8,5",
        'I': "M 5,0 L 5,10 M 2,0 L 8,0 M 2,10 L 8,10",
        'L': "M 0,0 L 0,10 L 8,10",
        'M': "M 0,10 L 0,0 L 5,5 L 10,0 L 10,10",
        'N': "M 0,10 L 0,0 L 10,10 L 10,0",
        'O': "M 5,0 C -2,0 -2,10 5,10 C 12,10 12,0 5,0 Z",
        'P': "M 0,10 L 0,0 L 5,0 C 10,0 10,5 5,5 L 0,5",
        'R': "M 0,10 L 0,0 L 5,0 C 10,0 10,5 5,5 L 0,5 M 5,5 L 10,10",
        'S': "M 10,2 C 5,-2 0,2 5,5 C 10,8 5,12 0,8",
        'T': "M 0,0 L 10,0 M 5,0 L 5,10",
        'U': "M 0,0 L 0,7 C 0,12 10,12 10,7 L 10,0",
        'V': "M 0,0 L 5,10 L 10,0",
        'X': "M 0,0 L 10,10 M 0,10 L 10,0",
        '*': "M 5,0 L 5,10 M 0,2.5 L 10,7.5 M 0,7.5 L 10,2.5",
        '~': "M 2.5,-3 C 5,-5 5,-1 7.5,-3",
        '.': "M 4,9 C 4,8 6,8 6,9 C 6,10 4,10 4,9 Z"
    }

    paths = []
    cx = x
    for char in text:
        if char == ' ':
            cx += 10 * scale * spacing
            continue
        
        has_tilde = False
        if char == 'Ã':
            char = 'A'
            has_tilde = True
        elif char == 'Õ':
            char = 'O'
            has_tilde = True
            
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
                
        cx += 10 * scale * spacing
    
    return " ".join(paths)

bg = '<rect x="0" y="0" width="200" height="200" fill="#ffffff" />'

# 1. Contexto (Document icon)
ctx_x, ctx_y = 10, 75
ctx_w, ctx_h = 35, 45
ctx_fill = f'<path d="M {ctx_x},{ctx_y} L {ctx_x+ctx_w},{ctx_y} L {ctx_x+ctx_w},{ctx_y+ctx_h} L {ctx_x},{ctx_y+ctx_h} Z" fill="#ffffff" />'
ctx_shadow = f'<path d="M {ctx_x+5},{ctx_y+5} L {ctx_x+ctx_w+5},{ctx_y+5} L {ctx_x+ctx_w+5},{ctx_y+ctx_h+5} L {ctx_x+5},{ctx_y+ctx_h+5} Z" />'
ctx_main = f'<path d="M {ctx_x-1},{ctx_y+2} L {ctx_x+ctx_w+2},{ctx_y-1} L {ctx_x+ctx_w-1},{ctx_y+ctx_h+1} L {ctx_x+2},{ctx_y+ctx_h-2} Z" />'
ctx_sketch = f'<path d="M {ctx_x+1},{ctx_y-1} L {ctx_x+ctx_w-2},{ctx_y+2} L {ctx_x+ctx_w+1},{ctx_y+ctx_h-1} L {ctx_x-2},{ctx_y+ctx_h+2} Z" />'
# Lines inside document
ctx_lines_main = f'<path d="M {ctx_x+8},{ctx_y+15} L {ctx_x+ctx_w-8},{ctx_y+15} M {ctx_x+8},{ctx_y+25} L {ctx_x+ctx_w-8},{ctx_y+25} M {ctx_x+8},{ctx_y+35} L {ctx_x+ctx_w-15},{ctx_y+35}" />'
ctx_lines_sketch = f'<path d="M {ctx_x+7},{ctx_y+16} L {ctx_x+ctx_w-7},{ctx_y+14} M {ctx_x+9},{ctx_y+24} L {ctx_x+ctx_w-9},{ctx_y+26} M {ctx_x+7},{ctx_y+36} L {ctx_x+ctx_w-14},{ctx_y+34}" />'
text_ctx = draw_text("CONTEXTO", 4, 130, scale=0.6)

# 2. LLM / Process (Brain / Neural Network inside a Cloud/API Box)
llm_x, llm_y = 80, 75
llm_w, llm_h = 40, 45
llm_fill = f'<path d="M {llm_x},{llm_y+10} Q {llm_x},{llm_y} {llm_x+10},{llm_y} L {llm_x+llm_w-10},{llm_y} Q {llm_x+llm_w},{llm_y} {llm_x+llm_w},{llm_y+10} L {llm_x+llm_w},{llm_y+llm_h-10} Q {llm_x+llm_w},{llm_y+llm_h} {llm_x+llm_w-10},{llm_y+llm_h} L {llm_x+10},{llm_y+llm_h} Q {llm_x},{llm_y+llm_h} {llm_x},{llm_y+llm_h-10} Z" fill="#ffffff" />'
llm_shadow = f'<path d="M {llm_x+5},{llm_y+15} Q {llm_x+5},{llm_y+5} {llm_x+15},{llm_y+5} L {llm_x+llm_w-5},{llm_y+5} Q {llm_x+llm_w+5},{llm_y+5} {llm_x+llm_w+5},{llm_y+15} L {llm_x+llm_w+5},{llm_y+llm_h-5} Q {llm_x+llm_w+5},{llm_y+llm_h+5} {llm_x+llm_w-5},{llm_y+llm_h+5} L {llm_x+15},{llm_y+llm_h+5} Q {llm_x+5},{llm_y+llm_h+5} {llm_x+5},{llm_y+llm_h-5} Z" />'
llm_main = f'<path d="M {llm_x-1},{llm_y+10} Q {llm_x-1},{llm_y-1} {llm_x+10},{llm_y+1} L {llm_x+llm_w-10},{llm_y-2} Q {llm_x+llm_w+1},{llm_y-1} {llm_x+llm_w+2},{llm_y+10} L {llm_x+llm_w-1},{llm_y+llm_h-10} Q {llm_x+llm_w+1},{llm_y+llm_h+1} {llm_x+llm_w-10},{llm_y+llm_h-1} L {llm_x+10},{llm_y+llm_h+2} Q {llm_x-2},{llm_y+llm_h+1} {llm_x+1},{llm_y+llm_h-10} Z" />'
llm_sketch = f'<path d="M {llm_x+1},{llm_y+12} Q {llm_x+1},{llm_y+1} {llm_x+12},{llm_y-1} L {llm_x+llm_w-8},{llm_y+2} Q {llm_x+llm_w-1},{llm_y+1} {llm_x+llm_w-2},{llm_y+12} L {llm_x+llm_w+1},{llm_y+llm_h-8} Q {llm_x+llm_w-1},{llm_y+llm_h-1} {llm_x+llm_w-12},{llm_y+llm_h+1} L {llm_x+8},{llm_y+llm_h-2} Q {llm_x+2},{llm_y+llm_h-1} {llm_x-1},{llm_y+llm_h-12} Z" />'
# Neural network nodes inside
llm_nodes_main = f'<path d="M {llm_x+10},{llm_y+15} A 2 2 0 1 0 {llm_x+10.1},{llm_y+15} M {llm_x+10},{llm_y+30} A 2 2 0 1 0 {llm_x+10.1},{llm_y+30} M {llm_x+20},{llm_y+22.5} A 2 2 0 1 0 {llm_x+20.1},{llm_y+22.5} M {llm_x+30},{llm_y+15} A 2 2 0 1 0 {llm_x+30.1},{llm_y+15} M {llm_x+30},{llm_y+30} A 2 2 0 1 0 {llm_x+30.1},{llm_y+30} M {llm_x+12},{llm_y+16} L {llm_x+18},{llm_y+21} M {llm_x+12},{llm_y+29} L {llm_x+18},{llm_y+24} M {llm_x+22},{llm_y+21} L {llm_x+28},{llm_y+16} M {llm_x+22},{llm_y+24} L {llm_x+28},{llm_y+29}" />'
llm_nodes_sketch = f'<path d="M {llm_x+11},{llm_y+17} L {llm_x+19},{llm_y+22} M {llm_x+11},{llm_y+28} L {llm_x+19},{llm_y+23} M {llm_x+21},{llm_y+22} L {llm_x+29},{llm_y+17} M {llm_x+21},{llm_y+23} L {llm_x+29},{llm_y+28}" />'
text_llm = draw_text("LLM", llm_x+12, llm_y-20, scale=0.7)
text_api = draw_text("PROCESSA", llm_x-3, 130, scale=0.6)

# 3. Resultado (Document with Star)
res_x, res_y = 155, 75
res_w, res_h = 35, 45
res_fill = f'<path d="M {res_x},{res_y} L {res_x+res_w},{res_y} L {res_x+res_w},{res_y+res_h} L {res_x},{res_y+res_h} Z" fill="#ffffff" />'
res_shadow = f'<path d="M {res_x+5},{res_y+5} L {res_x+res_w+5},{res_y+5} L {res_x+res_w+5},{res_y+res_h+5} L {res_x+5},{res_y+res_h+5} Z" />'
res_main = f'<path d="M {res_x-1},{res_y+2} L {res_x+res_w+2},{res_y-1} L {res_x+res_w-1},{res_y+res_h+1} L {res_x+2},{res_y+res_h-2} Z" />'
res_sketch = f'<path d="M {res_x+1},{res_y-1} L {res_x+res_w-2},{res_y+2} L {res_x+res_w+1},{res_y+res_h-1} L {res_x-2},{res_y+res_h+2} Z" />'
# Star inside document
res_star_main = f'<path d="M {res_x+17.5},{res_y+10} L {res_x+20},{res_y+17} L {res_x+27.5},{res_y+17} L {res_x+21.5},{res_y+22} L {res_x+24},{res_y+29} L {res_x+17.5},{res_y+25} L {res_x+11},{res_y+29} L {res_x+13.5},{res_y+22} L {res_x+7.5},{res_y+17} L {res_x+15},{res_y+17} Z" />'
res_star_sketch = f'<path d="M {res_x+18.5},{res_y+11} L {res_x+21},{res_y+18} L {res_x+26.5},{res_y+18} L {res_x+22.5},{res_y+21} L {res_x+23},{res_y+28} L {res_x+18.5},{res_y+24} L {res_x+12},{res_y+28} L {res_x+14.5},{res_y+21} L {res_x+8.5},{res_y+18} L {res_x+14},{res_y+18} Z" />'
text_res = draw_text("RESULTADO", 143, 130, scale=0.6)

# 4. Arrows
# Arrow 1: Contexto -> Processa
a1_x1 = ctx_x + ctx_w + 5
a1_x2 = llm_x - 5
a1_y = 97.5
arr1_main = f'<path d="M {a1_x1},{a1_y} L {a1_x2},{a1_y} M {a1_x2-5},{a1_y-5} L {a1_x2},{a1_y} L {a1_x2-5},{a1_y+5}" />'
arr1_sketch = f'<path d="M {a1_x1+1},{a1_y-1} L {a1_x2-1},{a1_y+1} M {a1_x2-4},{a1_y-6} L {a1_x2-1},{a1_y-1} L {a1_x2-6},{a1_y+4}" />'

# Arrow 2: Processa -> Resultado
a2_x1 = llm_x + llm_w + 5
a2_x2 = res_x - 5
a2_y = 97.5
arr2_main = f'<path d="M {a2_x1},{a2_y} L {a2_x2},{a2_y} M {a2_x2-5},{a2_y-5} L {a2_x2},{a2_y} L {a2_x2-5},{a2_y+5}" />'
arr2_sketch = f'<path d="M {a2_x1+1},{a2_y-1} L {a2_x2-1},{a2_y+1} M {a2_x2-4},{a2_y-6} L {a2_x2-1},{a2_y-1} L {a2_x2-6},{a2_y+4}" />'


svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <!-- Design System: MIRA SKETCH -->
  
  <!-- Fundo Base -->
  {bg}
  
  <!-- Preenchimento Branco -->
  {ctx_fill}
  {llm_fill}
  {res_fill}
  
  <!-- Sombreamento (Cyan) -->
  <g stroke="#82e0d8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.5" stroke-width="15">
    {ctx_shadow}
    {llm_shadow}
    {res_shadow}
  </g>

  <!-- Contornos e Rabiscos -->
  <g stroke="#1a1a1a" fill="none" stroke-linecap="round" stroke-linejoin="round">
    
    <!-- Camada de Traço Principal -->
    <g stroke-width="4.5">
      {ctx_main}
      {llm_main}
      {res_main}
    </g>
    
    <!-- Camada de Efeito Sketch -->
    <g stroke-width="2.0">
      {ctx_sketch}
      {llm_sketch}
      {res_sketch}
    </g>
    
    <!-- Arrows -->
    <g stroke-width="3.0">
      {arr1_main}
      {arr2_main}
    </g>
    <g stroke-width="1.5">
      {arr1_sketch}
      {arr2_sketch}
    </g>

    <!-- Detalhes Internos -->
    <g stroke-width="3.0">
      {ctx_lines_main}
      {llm_nodes_main}
      {res_star_main}
    </g>
    <g stroke-width="1.5">
      {ctx_lines_sketch}
      {llm_nodes_sketch}
      {res_star_sketch}
    </g>
    
    <!-- Textos -->
    <g stroke-width="2.5">
      <path d="{text_ctx}" />
      <path d="{text_api}" />
      <path d="{text_res}" />
      <path d="{text_llm}" />
    </g>
    <g stroke-width="1.0">
      <path d="{text_ctx}" />
      <path d="{text_api}" />
      <path d="{text_res}" />
      <path d="{text_llm}" />
    </g>

  </g>
</svg>
"""

with open(".assets/llm_process.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)

print("Gerado com sucesso!")
