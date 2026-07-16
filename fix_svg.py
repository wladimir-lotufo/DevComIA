import base64

with open(r'd:\repos\DevComIA\ApresentacaoIA\.assets\logos\Antigravity.jpg', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

svg_path = r'd:\repos\DevComIA\ApresentacaoIA\.assets\aplicacoes.svg'
with open(svg_path, 'r', encoding='utf-8') as f:
    content = f.read()

antigravity_block = '  <rect x="180" y="255" width="240" height="50" fill="transparent" rx="8" />\n  <!-- Antigravity -->\n  <image href="data:image/jpeg;base64,' + b64 + '" x="242.0" y="277" width="18" height="18" />\n  <text x="300" y="290" font-family="monospace, sans-serif" font-weight="bold" font-size="20" fill="#0055ff" text-anchor="middle">Antigravity</text>\n'

if '<!-- Antigravity -->' not in content:
    content = content.replace('  <!-- Midjourney -->', antigravity_block + '  <!-- Midjourney -->')
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Successfully added Antigravity block.')
else:
    print('Antigravity already in file.')
