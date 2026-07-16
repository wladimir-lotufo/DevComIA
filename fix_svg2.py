import base64
import re

png_path = r'd:\repos\DevComIA\ApresentacaoIA\.assets\logos\antigravity.png'
with open(png_path, 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

svg_path = r'd:\repos\DevComIA\ApresentacaoIA\.assets\aplicacoes.svg'
with open(svg_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The Antigravity image is currently a jpeg. We want to replace it.
# We look for the image tag immediately following <!-- Antigravity -->
# and replace its href with our new base64 png data.

# Find the block:
#   <!-- Antigravity -->
#   <image href="data:image/jpeg;base64,..." x="229.25" y="147" width="18" height="18" />
# We can use regex to replace the href safely.

def repl(match):
    prefix = match.group(1)
    suffix = match.group(3)
    return prefix + f'data:image/png;base64,{b64}' + suffix

new_content = re.sub(r'(<!-- Antigravity -->\s*<image href=")([^"]+)(")', repl, content)

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SVG fixed successfully.")
