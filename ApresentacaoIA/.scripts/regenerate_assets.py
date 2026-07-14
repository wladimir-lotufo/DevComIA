import os

def create_ai_types():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <!-- Design System: MIRA SKETCH (Vazado, Linhas Coloridas) -->
  
  <g stroke-linecap="round" stroke-linejoin="round" fill="none">
    
    <!-- Conectores (Chumbo e Cyan) -->
    <g stroke-width="3" stroke-dasharray="10, 8">
      <path d="M 400,300 Q 550,150 650,150" stroke="#82e0d8" />
      <path d="M 400,300 Q 550,300 650,300" stroke="#FF904D" />
      <path d="M 400,300 Q 550,450 650,450" stroke="#1a1a1a" />
      <path d="M 400,300 Q 250,200 150,200" stroke="#82e0d8" />
      <path d="M 400,300 Q 250,400 150,400" stroke="#FF904D" />
    </g>

    <!-- Centro: IA -->
    <g transform="translate(400, 300)">
      <circle cx="0" cy="0" r="60" stroke="#1a1a1a" stroke-width="5" />
      <circle cx="0" cy="0" r="70" stroke="#82e0d8" stroke-width="2" stroke-dasharray="5,5" />
      <text x="0" y="10" font-family="sans-serif" font-size="32" font-weight="bold" fill="#1a1a1a" stroke="none" text-anchor="middle">IA</text>
    </g>

    <!-- Nódulos Externos -->
    <g stroke-width="4">
      <!-- LLM (Direita, Cima) -->
      <circle cx="650" cy="150" r="40" stroke="#82e0d8" />
      <text x="650" y="100" font-family="sans-serif" font-size="24" font-weight="bold" fill="#82e0d8" stroke="none" text-anchor="middle">LLM</text>

      <!-- Visão Computacional (Direita, Centro) -->
      <circle cx="650" cy="300" r="40" stroke="#FF904D" />
      <text x="650" y="250" font-family="sans-serif" font-size="24" font-weight="bold" fill="#FF904D" stroke="none" text-anchor="middle">Visão Comp.</text>

      <!-- ML (Direita, Baixo) -->
      <circle cx="650" cy="450" r="40" stroke="#1a1a1a" />
      <text x="650" y="520" font-family="sans-serif" font-size="24" font-weight="bold" fill="#1a1a1a" stroke="none" text-anchor="middle">Machine Learning</text>

      <!-- Melhor Caminho A* (Esquerda, Cima) -->
      <circle cx="150" cy="200" r="40" stroke="#82e0d8" />
      <text x="150" y="150" font-family="sans-serif" font-size="24" font-weight="bold" fill="#82e0d8" stroke="none" text-anchor="middle">A* (Busca)</text>

      <!-- Outros (Esquerda, Baixo) -->
      <circle cx="150" cy="400" r="40" stroke="#FF904D" />
      <text x="150" y="470" font-family="sans-serif" font-size="24" font-weight="bold" fill="#FF904D" stroke="none" text-anchor="middle">Outros...</text>
    </g>
    
    <!-- Detalhes de Sketch -->
    <g stroke="#1a1a1a" stroke-width="1.5">
      <path d="M 380,280 C 390,270 410,270 420,280" />
      <path d="M 640,140 C 645,135 655,135 660,140" />
      <path d="M 140,190 C 145,185 155,185 160,190" />
    </g>
  </g>
</svg>"""
    return svg

def create_llm_process():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 400" width="100%" height="100%">
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    
    <!-- Setas de Fluxo -->
    <g stroke="#1a1a1a" stroke-width="4" stroke-dasharray="12,6">
      <path d="M 300,200 L 420,200" />
      <path d="M 400,180 L 420,200 L 400,220" />
      
      <path d="M 580,200 L 700,200" />
      <path d="M 680,180 L 700,200 L 680,220" />
    </g>

    <!-- Contexto (Esquerda) -->
    <g transform="translate(150, 200)">
      <rect x="-100" y="-80" width="200" height="160" rx="15" stroke="#FF904D" stroke-width="6" />
      <path d="M -70,-40 L 70,-40 M -70,0 L 50,0 M -70,40 L 70,40" stroke="#FF904D" stroke-width="4" stroke-dasharray="8,4" />
      <text x="0" y="-100" font-family="sans-serif" font-size="28" font-weight="bold" fill="#FF904D" stroke="none" text-anchor="middle">Contexto</text>
      <!-- Sombra Sketch -->
      <rect x="-90" y="-70" width="200" height="160" rx="15" stroke="#FF904D" stroke-width="2" opacity="0.3" />
    </g>

    <!-- LLM (Centro) -->
    <g transform="translate(500, 200)">
      <!-- Brain Icon Base -->
      <path d="M -50,-30 C -80,-30 -80,30 -50,40 C -20,60 20,60 50,40 C 80,30 80,-30 50,-30 C 20,-50 -20,-50 -50,-30 Z" stroke="#82e0d8" stroke-width="8" />
      <path d="M 0,-40 L 0,50" stroke="#82e0d8" stroke-width="4" stroke-dasharray="5,5" />
      <path d="M -30,-10 C -10,0 -10,20 -30,30" stroke="#82e0d8" stroke-width="3" />
      <path d="M 30,-10 C 10,0 10,20 30,30" stroke="#82e0d8" stroke-width="3" />
      <text x="0" y="-70" font-family="sans-serif" font-size="32" font-weight="bold" fill="#82e0d8" stroke="none" text-anchor="middle">LLM API</text>
      <text x="0" y="80" font-family="sans-serif" font-size="20" fill="#1a1a1a" stroke="none" text-anchor="middle">(Processamento)</text>
    </g>

    <!-- Resultado (Direita) -->
    <g transform="translate(850, 200)">
      <polygon points="0,-70 70,0 0,70 -70,0" stroke="#1a1a1a" stroke-width="6" />
      <polygon points="0,-55 55,0 0,55 -55,0" stroke="#1a1a1a" stroke-width="2" opacity="0.4" />
      <text x="0" y="110" font-family="sans-serif" font-size="28" font-weight="bold" fill="#1a1a1a" stroke="none" text-anchor="middle">Resultado</text>
      <!-- Estrelas Sketch -->
      <path d="M 0,-20 L 5,-5 L 20,0 L 5,5 L 0,20 L -5,5 L -20,0 L -5,-5 Z" stroke="#FF904D" stroke-width="2" fill="#FF904D" />
    </g>

  </g>
</svg>"""
    return svg

def create_vibe_coding():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    
    <!-- Título Principal -->
    <text x="400" y="80" font-family="sans-serif" font-size="40" font-weight="bold" fill="#FF904D" stroke="none" text-anchor="middle">Vibe Coding</text>
    <text x="400" y="120" font-family="sans-serif" font-size="24" fill="#1a1a1a" stroke="none" text-anchor="middle">Humano (Diretriz) + IA (Geração)</text>

    <!-- Humano (Esquerda) -->
    <g transform="translate(250, 350)">
      <!-- Corpo -->
      <path d="M -50,150 C -50,50 50,50 50,150" stroke="#1a1a1a" stroke-width="6" />
      <!-- Cabeça -->
      <circle cx="0" cy="-20" r="50" stroke="#1a1a1a" stroke-width="6" />
      <!-- Sorriso/Óculos Sketch -->
      <path d="M -20,-30 L 20,-30" stroke="#1a1a1a" stroke-width="3" />
      <path d="M -15,-10 C -5,5 5,5 15,-10" stroke="#1a1a1a" stroke-width="3" />
      <!-- Balão de Fala -->
      <path d="M 30,-60 Q 50,-90 90,-90 Q 150,-90 150,-40 Q 150,10 90,10 Q 60,10 50,0 Z" stroke="#FF904D" stroke-width="4" />
      <text x="100" y="-35" font-family="sans-serif" font-size="20" font-weight="bold" fill="#FF904D" stroke="none" text-anchor="middle">Crie a feature!</text>
    </g>

    <!-- Integração / Mágica (Centro) -->
    <g transform="translate(400, 350)">
      <path d="M -30,-40 C 0,-80 30,-40 0,0 C -30,40 0,80 30,40" stroke="#82e0d8" stroke-width="5" stroke-dasharray="10,5" />
      <path d="M -15,0 L 15,0 M 0,-15 L 0,15" stroke="#82e0d8" stroke-width="3" />
    </g>

    <!-- Notebook / IA (Direita) -->
    <g transform="translate(550, 350)">
      <!-- Tela -->
      <rect x="-80" y="-80" width="160" height="120" rx="10" stroke="#1a1a1a" stroke-width="6" />
      <!-- Teclado -->
      <path d="M -100,50 L 100,50 L 120,90 L -120,90 Z" stroke="#1a1a1a" stroke-width="6" />
      <path d="M -80,70 L 80,70" stroke="#1a1a1a" stroke-width="2" />
      <!-- Código Sketch na Tela -->
      <path d="M -60,-50 L -20,-50 M -60,-30 L 20,-30 M -60,-10 L 0,-10 M -60,10 L 40,10" stroke="#82e0d8" stroke-width="5" />
      <!-- Sparkles de IA -->
      <path d="M 60,-100 L 70,-70 L 100,-60 L 70,-50 L 60,-20 L 50,-50 L 20,-60 L 50,-70 Z" stroke="#82e0d8" stroke-width="3" fill="#82e0d8" />
    </g>

  </g>
</svg>"""
    return svg

def save_svg(filename, content):
    path = os.path.join('d:/repos/DevComIA/ApresentacaoIA/.assets', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

save_svg('ai_types.svg', create_ai_types())
save_svg('llm_process.svg', create_llm_process())
save_svg('vibe_coding.svg', create_vibe_coding())

print("All SVGs regenerated with new rules.")
