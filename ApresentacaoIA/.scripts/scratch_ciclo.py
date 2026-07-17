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
    '¸': "M 5,10 C 2,12 8,12 5,14",
    '1': "M 2,2 L 5,0 L 5,10",
    '2': "M 0,2 C 0,0 10,0 10,4 C 10,7 0,7 0,10 L 10,10",
    '3': "M 0,0 L 10,0 L 5,5 L 10,5 C 12,8 5,12 0,8",
    '4': "M 8,10 L 8,0 L 0,6 L 10,6",
    '.': "M 4,9 L 6,9 L 6,11 L 4,11 Z"
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

def gen_title(text, cx, cy, scale=1.0):
    spacing = 1.2
    w = len(text) * 10 * scale * spacing
    return draw_text(text, cx - w/2, cy, scale, spacing)

main_title = gen_title("É POSSÍVEL USAR IA PARA GRANDES SISTEMAS?", 200, 10, 1.1)

# Títulos (Fora do círculo)
t1 = gen_title("1. GERAÇÃO", 200, 40, 0.7)
t2 = gen_title("2. REVISÃO", 420, 215, 0.7)
t3 = gen_title("3. AJUSTES", 200, 380, 0.7)
t4 = gen_title("4. TUNNING", -20, 225, 0.7)

# Textos Internos (Dentro do círculo)
i1 = gen_title("SPECDRIVEN", 200, 150, 0.3)
i2 = gen_title("HUMANA", 270, 215, 0.3)
i3 = gen_title("VIBE CODING", 200, 270, 0.25)
i4 = gen_title("SKILLS", 130, 225, 0.3)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="-100 -50 600 550" width="100%" height="100%">
  <!-- ==========================================
       Design System: MIRA SKETCH
       ========================================== -->
  
  <!-- 2. Preenchimento do Corpo -->
  <g fill="#ffffff" stroke="none">
    <!-- Engrenagem Top (1) -->
    <path d="M 180 100 A 20 20 0 1 0 220 100 A 20 20 0 1 0 180 100" />
    <!-- Bloco/Lupa Right (2) -->
    <path d="M 310 200 L 340 200 L 340 230 L 310 230 Z" />
    <path d="M 320 220 A 15 15 0 1 0 350 220 A 15 15 0 1 0 320 220" />
    <!-- Prancheta Bottom (3) -->
    <path d="M 170 280 L 210 280 L 210 330 L 170 330 Z" />
    <path d="M 160 290 L 200 290 L 200 340 L 160 340 Z" />
    <!-- Prancheta/Cérebro Left (4) -->
    <path d="M 40 200 L 80 200 L 80 250 L 40 250 Z" />
    <path d="M 50 180 A 15 15 0 1 0 80 180 A 15 15 0 1 0 50 180" />
  </g>
  
  <!-- 3. Sombreamento em Cores (Marcador Aquarela) -->
  <g fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.6">
    <g stroke="#82e0d8">
      <!-- 1 -->
      <path d="M 185 115 A 20 20 0 0 0 215 115" stroke-width="15" />
      <!-- 2 -->
      <path d="M 315 225 L 335 225 L 335 205" stroke-width="10" />
      <!-- 3 -->
      <path d="M 200 295 L 200 335 L 165 335" stroke-width="12" />
      <!-- 4 -->
      <path d="M 80 205 L 80 245 L 45 245" stroke-width="12" />
    </g>
    <!-- Laranja / Vermelho vivo para o Ciclo (Setas) -->
    <g stroke="#ff904f">
      <!-- 1->2 -->
      <path d="M 230 110 Q 330 120 330 180" stroke-width="15" />
      <!-- 2->3 -->
      <path d="M 320 250 Q 300 310 220 310" stroke-width="15" />
      <!-- 3->4 -->
      <path d="M 150 310 Q 70 300 70 260" stroke-width="15" />
      <!-- 4->1 -->
      <path d="M 80 180 Q 90 100 170 100" stroke-width="15" />
    </g>
  </g>

  <!-- 4. Contornos e Rabiscos (Caneta) -->
  <g stroke="#1a1a1a" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <g stroke-width="4.5">
      <!-- Engrenagem (1) -->
      <path d="M 180 100 A 20 20 0 1 0 220 100 A 20 20 0 1 0 180 100" />
      <path d="M 195 75 L 205 75 M 225 95 L 225 105 M 195 125 L 205 125 M 175 95 L 175 105 M 185 85 L 180 80 M 215 85 L 220 80 M 215 115 L 220 120 M 185 115 L 180 120" />
      <path d="M 190 100 A 10 10 0 1 0 210 100 A 10 10 0 1 0 190 100" />
      
      <!-- Lupa/Bloco (2) -->
      <path d="M 310 200 Q 340 198 342 202 Q 340 230 338 232 Q 312 230 310 228 Z" />
      <path d="M 315 208 L 335 208 M 315 215 L 325 215 M 315 222 L 330 222" />
      <path d="M 320 220 A 15 15 0 1 0 350 220 A 15 15 0 1 0 320 220" />
      <path d="M 332 232 L 345 245" />

      <!-- Prancheta Traseira e Frontal (3) -->
      <path d="M 170 280 Q 210 278 212 282 Q 210 330 208 332 Q 172 330 170 328 Z" />
      <path d="M 185 275 Q 195 275 195 280 Q 185 280 185 275" />
      <path d="M 160 290 Q 200 288 202 292 Q 200 340 198 342 Q 162 340 160 338 Z" />
      <path d="M 175 285 Q 185 285 185 290 Q 175 290 175 285" />
      <path d="M 165 300 L 190 300 M 165 310 L 185 310 M 165 320 L 195 320" />

      <!-- Prancheta/Cérebro (4) -->
      <path d="M 40 200 Q 80 198 82 202 Q 80 250 78 252 Q 42 250 40 248 Z" />
      <path d="M 55 195 Q 65 195 65 200 Q 55 200 55 195" />
      <path d="M 50 180 A 15 15 0 1 0 80 180 A 15 15 0 1 0 50 180" />
      <path d="M 45 215 L 75 215 M 45 225 L 65 225" />

      <!-- Setas de Conexão -->
      <path d="M 230 110 Q 330 120 330 180" />
      <path d="M 322 170 L 330 180 L 340 175" stroke-linejoin="miter" />
      
      <path d="M 320 250 Q 300 310 220 310" />
      <path d="M 235 305 L 220 310 L 225 325" stroke-linejoin="miter" />

      <path d="M 150 310 Q 70 300 70 260" />
      <path d="M 80 270 L 70 260 L 60 265" stroke-linejoin="miter" />

      <path d="M 80 180 Q 90 100 170 100" />
      <path d="M 160 92 L 170 100 L 160 110" stroke-linejoin="miter" />
    </g>

    <g stroke-width="2.0">
      <!-- Efeito Sketch Fino -->
      <path d="M 178 102 A 21 21 0 1 0 222 98 A 21 21 0 1 0 178 102" />
      <path d="M 308 202 Q 342 196 340 204 Q 338 232 336 230 Q 310 232 312 226 Z" />
      <path d="M 168 282 Q 212 276 210 284 Q 208 332 206 330 Q 170 332 172 326 Z" />
      <path d="M 38 202 Q 82 196 80 204 Q 78 252 76 250 Q 40 252 42 246 Z" />
      
      <path d="M 228 112 Q 332 122 328 178" />
      <path d="M 318 248 Q 298 312 218 312" />
      <path d="M 148 312 Q 68 298 72 258" />
      <path d="M 78 182 Q 88 98 168 102" />
    </g>
  </g>

  <!-- Títulos e Textos Internos -->
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <g stroke-width="2.0">
      <path d="{main_title}" stroke="#1a1a1a" />
    </g>
    <g stroke-width="1.0">
      <path d="{main_title}" stroke="#1a1a1a" />
    </g>

    <g stroke-width="1.5">
      <path d="{t1}" stroke="#1a1a1a" />
      <path d="{t2}" stroke="#1a1a1a" />
      <path d="{t3}" stroke="#1a1a1a" />
      <path d="{t4}" stroke="#1a1a1a" />
    </g>
    <g stroke-width="0.8">
      <path d="{t1}" stroke="#1a1a1a" />
      <path d="{t2}" stroke="#1a1a1a" />
      <path d="{t3}" stroke="#1a1a1a" />
      <path d="{t4}" stroke="#1a1a1a" />
    </g>

    <!-- Internos (caneta azul/laranja ou preta?) Usando preto fino e azul -->
    <g stroke="#ff904f" stroke-width="1.0">
      <path d="{i1}" />
      <path d="{i2}" />
      <path d="{i3}" />
      <path d="{i4}" />
    </g>
    <g stroke="#1a1a1a" stroke-width="0.4">
      <path d="{i1}" />
      <path d="{i2}" />
      <path d="{i3}" />
      <path d="{i4}" />
    </g>
  </g>
</svg>"""

with open("d:/repos/DevComIA/ApresentacaoIA/.assets/ciclo_feedback.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print("Updated ciclo_feedback.svg")
