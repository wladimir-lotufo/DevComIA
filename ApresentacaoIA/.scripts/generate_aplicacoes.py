import os
import urllib.request
from urllib.error import URLError
import base64

def get_base64_image(filepath):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "rb") as f:
        data = f.read()
    ext = filepath.split('.')[-1].lower()
    mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
    encoded = base64.b64encode(data).decode('utf-8')
    return f"data:{mime};base64,{encoded}"

logos_dir = r"d:\repos\DevComIA\ApresentacaoIA\.assets\logos"
os.makedirs(logos_dir, exist_ok=True)

apps = [
    {"name": "ChatGPT", "domain": "openai.com", "x": 100, "y": 160},
    {"name": "Gemini", "domain": "google.com", "x": 100, "y": 180},
    {"name": "NotebookLM", "domain": "notebooklm.google.com", "x": 100, "y": 215},
    {"name": "Apresentações", "domain": "docs.google.com", "x": 100, "y": 255},
    {"name": "Chatbots (Wpp)", "domain": "whatsapp.com", "x": 100, "y": 295},
    
    {"name": "Antigravity", "domain": "google.com", "x": 300, "y": 160},
    {"name": "Claude", "domain": "anthropic.com", "x": 300, "y": 200},
    {"name": "Codex", "domain": "openai.com", "x": 300, "y": 240},
    {"name": "OpenCode", "domain": "github.com", "x": 300, "y": 280},
    
    {"name": "Midjourney", "domain": "midjourney.com", "x": 500, "y": 160},
    {"name": "Leonardo.ai", "domain": "leonardo.ai", "x": 500, "y": 200},
    {"name": "Nano Banana", "domain": "gemini.google.com", "x": 500, "y": 240},
    
    {"name": "Whisper", "domain": "openai.com", "x": 700, "y": 160},
    {"name": "Audiobox", "domain": "meta.com", "x": 700, "y": 200},
]

# Create transparent 1x1 PNG for fallback
fallback_png = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
fallback_path = os.path.join(logos_dir, "fallback.png")
if not os.path.exists(fallback_path):
    with open(fallback_path, "wb") as f:
        f.write(fallback_png)

for app in apps:
    logo_filename = f"{app['name'].replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '')}.png"
    
    if app['name'] == 'Antigravity':
        logo_filename = 'Antigravity.jpg'
    elif app['name'] == 'OpenCode':
        logo_filename = 'OpenCode.jpg'
    elif app['name'] == 'Nano Banana':
        logo_filename = 'NanoBanana.jpg'

    logo_path = os.path.join(logos_dir, logo_filename)
    app['logo_href'] = f"logos/{logo_filename}"
    
    if not os.path.exists(logo_path):
        url = f"https://logo.clearbit.com/{app['domain']}?size=64"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(logo_path, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Downloaded logo for {app['name']}")
        except Exception as e:
            print(f"Could not download logo for {app['name']}, using fallback. Error: {e}")
            with open(logo_path, 'wb') as out_file:
                out_file.write(fallback_png)

svg_header = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 400" width="100%" height="100%">
  <!-- Sombreamento Cyan para os Títulos de Coluna -->
  <g stroke-linecap="round" stroke-linejoin="round" fill="none">
    <g stroke="#82e0d8" opacity="0.6" stroke-width="15">
      <path d="M 60 70 L 140 70" />
      <path d="M 260 70 L 340 70" />
      <path d="M 460 70 L 540 70" />
      <path d="M 660 70 L 740 70" />
      <path d="M 860 70 L 940 70" />
    </g>
  </g>

  <!-- Contornos e Rabiscos (Caneta) -->
  <g stroke="#1a1a1a" fill="none" stroke-linecap="round" stroke-linejoin="round">
    
    <!-- Traço Principal (Grossa) -->
    <g stroke-width="4.5">
      <path d="M 70 40 L 130 40 L 130 90 L 70 90 Z" />
      <path d="M 80 55 L 120 55 M 80 70 L 110 70" />
      <path d="M 280 40 L 260 65 L 280 90 M 320 40 L 340 65 L 320 90" />
      <path d="M 470 40 L 530 40 L 530 90 L 470 90 Z" />
      <circle cx="490" cy="55" r="5" />
      <path d="M 470 90 L 490 70 L 510 85 L 530 65" />
      <path d="M 670 65 L 680 40 L 690 90 L 700 50 L 710 80 L 720 65" />
      <circle cx="900" cy="65" r="20" />
      <path d="M 900 35 L 900 25 M 900 95 L 900 105 M 870 65 L 860 65 M 930 65 L 940 65" />
      <path d="M 878 43 L 871 36 M 922 87 L 929 94 M 878 87 L 871 94 M 922 43 L 929 36" />
    </g>
    
    <!-- Efeito Sketch (Fina) -->
    <g stroke-width="2.0">
      <path d="M 68 42 L 132 38 L 128 92 L 72 88 Z" />
      <path d="M 282 38 L 258 66 L 282 92 M 318 38 L 342 66 L 318 92" />
      <path d="M 468 42 L 532 38 L 528 92 L 472 88 Z" />
      <path d="M 668 66 L 682 38 L 688 92 L 702 48 L 708 82 L 722 64" />
      <circle cx="902" cy="63" r="18" />
    </g>

    <!-- Conexoes -->
    <g stroke-width="2.0" stroke-dasharray="5,5" opacity="0.5">
      <path d="M 100 130 L 100 350" />
      <path d="M 300 130 L 300 350" />
      <path d="M 500 130 L 500 350" />
      <path d="M 700 130 L 700 350" />
      <path d="M 900 130 L 900 350" />
    </g>
  </g>

  <!-- Textos -->
  <g fill="#1a1a1a" font-family="monospace, sans-serif" font-weight="bold" text-anchor="middle">
    <!-- Titulos Categorias -->
    <text x="100" y="120" font-size="16">Texto</text>
    <text x="300" y="120" font-size="16">Código</text>
    <text x="500" y="120" font-size="16">Imagem</text>
    <text x="700" y="120" font-size="16">Áudio</text>
    <text x="900" y="120" font-size="16">Bespoke</text>

    <!-- Apps Customizadas Fixa -->
    <text x="900" y="160" font-size="14">Aplicações</text>
    <text x="900" y="180" font-size="14">Customizadas</text>
  </g>
"""

svg_footer = "</svg>"

svg_apps = ""
for app in apps:
    # Estimate text width rough calculation: ~8.5 pixels per character (monospaced)
    text_w = len(app["name"]) * 8.5
    # Image size
    img_size = 18
    # Center everything together: half width = text_w/2, img is to the left
    # x is the center point
    # text left start = x - text_w/2
    # image left start = text left start - img_size - 6px margin
    
    img_x = app["x"] - (text_w/2) - img_size - 6
    img_y = app["y"] - 13 # Adjust y for center alignment with text
    
    logo_path = os.path.join(logos_dir, app['logo_href'].replace('logos/', ''))
    logo_base64 = get_base64_image(logo_path)
    
    svg_apps += f'''
  <!-- {app["name"]} -->
  <image href="{logo_base64}" x="{img_x}" y="{img_y}" width="{img_size}" height="{img_size}" />
  <text x="{app["x"]}" y="{app["y"]}" font-family="monospace, sans-serif" font-weight="bold" font-size="14" fill="#1a1a1a" text-anchor="middle">{app["name"]}</text>'''

full_svg = svg_header + svg_apps + "\n" + svg_footer

with open(r'd:\repos\DevComIA\ApresentacaoIA\.assets\aplicacoes.svg', 'w', encoding='utf-8') as f:
    f.write(full_svg)

print("aplicacoes.svg atualizado com logos reais com sucesso!")
