import re

with open('.assets/brain2.svg', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all d="..." attributes
paths = re.findall(r' d="([^"]+)"', content)
brain_outer = paths[0]
brain_inner = paths[1]

def draw_text(text, x, y, scale=1.0, spacing=1.2):
    letters = {
        'A': "M 0,10 L 5,0 L 10,10 M 2.5,5 L 7.5,5",
        'C': "M 10,2 C 5,-2 0,0 0,5 C 0,10 5,12 10,8",
        'E': "M 10,0 L 0,0 L 0,10 L 10,10 M 0,5 L 8,5",
        'I': "M 5,0 L 5,10 M 2,0 L 8,0 M 2,10 L 8,10",
        'O': "M 5,0 C -2,0 -2,10 5,10 C 12,10 12,0 5,0 Z",
        'L': "M 0,0 L 0,10 L 8,10",
        'M': "M 0,10 L 0,0 L 5,5 L 10,0 L 10,10",
        'P': "M 0,10 L 0,0 L 5,0 C 10,0 10,5 5,5 L 0,5",
        'R': "M 0,10 L 0,0 L 5,0 C 10,0 10,5 5,5 L 0,5 M 5,5 L 10,10",
        'S': "M 10,2 C 5,-2 0,2 5,5 C 10,8 5,12 0,8",
        'N': "M 0,10 L 0,0 L 10,10 L 10,0",
        'T': "M 0,0 L 10,0 M 5,0 L 5,10",
        'U': "M 0,0 L 0,7 C 0,12 10,12 10,7 L 10,0",
        'D': "M 0,10 L 0,0 L 5,0 C 10,0 10,10 5,10 L 0,10",
        'X': "M 0,0 L 10,10 M 0,10 L 10,0",
    }
    pts_res = []
    cx = x
    for char in text:
        if char == ' ':
            cx += 10 * scale * spacing
            continue
        if char in letters:
            pts = letters[char].split(' ')
            npts = []
            for pt in pts:
                if ',' in pt:
                    px, py = map(float, pt.split(','))
                    npts.append(f"{cx + px * scale},{y + py * scale}")
                else:
                    npts.append(pt)
            pts_res.append(" ".join(npts))
        cx += 10 * scale * spacing
    return " ".join(pts_res)

bg = '<rect x="0" y="0" width="200" height="200" fill="#ffffff" />'

ctx_x, ctx_y = 10, 75
ctx_w, ctx_h = 35, 45
ctx_fill = f'<path d="M {ctx_x},{ctx_y} L {ctx_x+ctx_w},{ctx_y} L {ctx_x+ctx_w},{ctx_y+ctx_h} L {ctx_x},{ctx_y+ctx_h} Z" fill="#ffffff" />'
ctx_shadow = f'<path d="M {ctx_x+5},{ctx_y+5} L {ctx_x+ctx_w+5},{ctx_y+5} L {ctx_x+ctx_w+5},{ctx_y+ctx_h+5} L {ctx_x+5},{ctx_y+ctx_h+5} Z" />'
ctx_main = f'<path d="M {ctx_x-1},{ctx_y+2} L {ctx_x+ctx_w+2},{ctx_y-1} L {ctx_x+ctx_w-1},{ctx_y+ctx_h+1} L {ctx_x+2},{ctx_y+ctx_h-2} Z" />'
ctx_sketch = f'<path d="M {ctx_x+1},{ctx_y-1} L {ctx_x+ctx_w-2},{ctx_y+2} L {ctx_x+ctx_w+1},{ctx_y+ctx_h-1} L {ctx_x-2},{ctx_y+ctx_h+2} Z" />'
ctx_lines_main = f'<path d="M {ctx_x+8},{ctx_y+15} L {ctx_x+ctx_w-8},{ctx_y+15} M {ctx_x+8},{ctx_y+25} L {ctx_x+ctx_w-8},{ctx_y+25} M {ctx_x+8},{ctx_y+35} L {ctx_x+ctx_w-15},{ctx_y+35}" />'
ctx_lines_sketch = f'<path d="M {ctx_x+7},{ctx_y+16} L {ctx_x+ctx_w-7},{ctx_y+14} M {ctx_x+9},{ctx_y+24} L {ctx_x+ctx_w-9},{ctx_y+26} M {ctx_x+7},{ctx_y+36} L {ctx_x+ctx_w-14},{ctx_y+34}" />'
text_ctx = draw_text("CONTEXTO", 4, 130, scale=0.6)

res_x, res_y = 155, 75
res_w, res_h = 35, 45
res_fill = f'<path d="M {res_x},{res_y} L {res_x+res_w},{res_y} L {res_x+res_w},{res_y+res_h} L {res_x},{res_y+res_h} Z" fill="#ffffff" />'
res_shadow = f'<path d="M {res_x+5},{res_y+5} L {res_x+res_w+5},{res_y+5} L {res_x+res_w+5},{res_y+res_h+5} L {res_x+5},{res_y+res_h+5} Z" />'
res_main = f'<path d="M {res_x-1},{res_y+2} L {res_x+res_w+2},{res_y-1} L {res_x+res_w-1},{res_y+res_h+1} L {res_x+2},{res_y+res_h-2} Z" />'
res_sketch = f'<path d="M {res_x+1},{res_y-1} L {res_x+res_w-2},{res_y+2} L {res_x+res_w+1},{res_y+res_h-1} L {res_x-2},{res_y+res_h+2} Z" />'
res_star_main = f'<path d="M {res_x+17.5},{res_y+10} L {res_x+20},{res_y+17} L {res_x+27.5},{res_y+17} L {res_x+21.5},{res_y+22} L {res_x+24},{res_y+29} L {res_x+17.5},{res_y+25} L {res_x+11},{res_y+29} L {res_x+13.5},{res_y+22} L {res_x+7.5},{res_y+17} L {res_x+15},{res_y+17} Z" />'
res_star_sketch = f'<path d="M {res_x+18.5},{res_y+11} L {res_x+21},{res_y+18} L {res_x+26.5},{res_y+18} L {res_x+22.5},{res_y+21} L {res_x+23},{res_y+28} L {res_x+18.5},{res_y+24} L {res_x+12},{res_y+28} L {res_x+14.5},{res_y+21} L {res_x+8.5},{res_y+18} L {res_x+14},{res_y+18} Z" />'
text_res = draw_text("RESULTADO", 143, 130, scale=0.6)

a1_x1 = ctx_x + ctx_w + 5
a1_x2 = 60
a1_y = 97.5
arr1_main = f'<path d="M {a1_x1},{a1_y} L {a1_x2},{a1_y} M {a1_x2-5},{a1_y-5} L {a1_x2},{a1_y} L {a1_x2-5},{a1_y+5}" />'
arr1_sketch = f'<path d="M {a1_x1+1},{a1_y-1} L {a1_x2-1},{a1_y+1} M {a1_x2-4},{a1_y-6} L {a1_x2-1},{a1_y-1} L {a1_x2-6},{a1_y+4}" />'

a2_x1 = 140
a2_x2 = res_x - 5
a2_y = 97.5
arr2_main = f'<path d="M {a2_x1},{a2_y} L {a2_x2},{a2_y} M {a2_x2-5},{a2_y-5} L {a2_x2},{a2_y} L {a2_x2-5},{a2_y+5}" />'
arr2_sketch = f'<path d="M {a2_x1+1},{a2_y-1} L {a2_x2-1},{a2_y+1} M {a2_x2-4},{a2_y-6} L {a2_x2-1},{a2_y-1} L {a2_x2-6},{a2_y+4}" />'

tx = 61.6
ty = 59.1
scale = 0.15
v_eff = 'vector-effect="non-scaling-stroke"'

brain_group_fill = f'''
<g transform="translate({tx}, {ty}) scale({scale})">
  <path d="{brain_outer}" fill="#ffffff" />
  <g transform="translate(96, 96) scale(10)"><path d="{brain_inner}" fill="#ffffff" /></g>
</g>
'''
brain_group_shadow = f'''
<g transform="translate({tx+3}, {ty+3}) scale({scale})">
  <path d="{brain_outer}" {v_eff} />
</g>
'''
brain_group_main = f'''
<g transform="translate({tx}, {ty}) scale({scale})">
  <path d="{brain_outer}" {v_eff} />
  <g transform="translate(96, 96) scale(10)"><path d="{brain_inner}" {v_eff} /></g>
</g>
'''
brain_group_sketch = f'''
<g transform="translate({tx-0.5}, {ty+0.5}) scale({scale})">
  <path d="{brain_outer}" {v_eff} />
  <g transform="translate(96, 96) scale(10)"><path d="{brain_inner}" {v_eff} /></g>
</g>
'''

text_llm = draw_text("LLM API", 65, 55, scale=0.7)
text_api = draw_text("PROCESSA", 77, 130, scale=0.6)

svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <!-- Design System: MIRA SKETCH -->
  
  {bg}
  
  {ctx_fill}
  {res_fill}
  {brain_group_fill}
  
  <g stroke="#82e0d8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.5" stroke-width="15">
    {ctx_shadow}
    {res_shadow}
    {brain_group_shadow}
  </g>

  <g stroke="#1a1a1a" fill="none" stroke-linecap="round" stroke-linejoin="round">
    
    <g stroke-width="4.5">
      {ctx_main}
      {res_main}
      {brain_group_main}
    </g>
    
    <g stroke-width="2.0">
      {ctx_sketch}
      {res_sketch}
      {brain_group_sketch}
    </g>
    
    <g stroke-width="3.0">
      {arr1_main}
      {arr2_main}
      {ctx_lines_main}
      {res_star_main}
    </g>
    <g stroke-width="1.5">
      {arr1_sketch}
      {arr2_sketch}
      {ctx_lines_sketch}
      {res_star_sketch}
    </g>
    
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

print("Brain inserido com sucesso!")
