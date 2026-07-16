import base64
import os
import sys

image_path = r'd:\repos\DevComIA\ApresentacaoIA\.assets\logos\Antigravity.jpg'
output_path = r'd:\repos\DevComIA\ApresentacaoIA\.assets\Antigravity.svg'

if not os.path.exists(image_path):
    print(f"Error: {image_path} not found")
    sys.exit(1)

# Read the image and encode as base64
with open(image_path, "rb") as f:
    encoded_string = base64.b64encode(f.read()).decode("utf-8")

# Prepare SVG content
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <image href="data:image/jpeg;base64,{encoded_string}" x="0" y="0" width="100" height="100" />
</svg>"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Successfully generated {output_path}")
