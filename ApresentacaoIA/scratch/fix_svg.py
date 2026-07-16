import sys
import re

file_path = r'd:\repos\DevComIA\ApresentacaoIA\.assets\aplicacoes.svg'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Update Texto column y-coordinates
for i, line in enumerate(lines):
    if '<!-- Gemini -->' in line:
        lines[i+1] = re.sub(r'y="167"', 'y="187"', lines[i+1])
        lines[i+2] = re.sub(r'y="180"', 'y="200"', lines[i+2])
    elif '<!-- NotebookLM -->' in line:
        lines[i+1] = re.sub(r'y="202"', 'y="227"', lines[i+1])
        lines[i+2] = re.sub(r'y="215"', 'y="240"', lines[i+2])
    elif '<!-- Apresentações -->' in line:
        lines[i+1] = re.sub(r'y="242"', 'y="267"', lines[i+1])
        lines[i+2] = re.sub(r'y="255"', 'y="280"', lines[i+2])
    elif '<!-- Chatbots (Wpp) -->' in line:
        lines[i+1] = re.sub(r'y="282"', 'y="307"', lines[i+1])
        lines[i+2] = re.sub(r'y="295"', 'y="320"', lines[i+2])

# We need to extract the blocks for Antigravity, Claude, Codex, OpenCode
antigravity_idx = -1
claude_idx = -1
codex_idx = -1
opencode_idx = -1

for i, line in enumerate(lines):
    if '<!-- Antigravity -->' in line: antigravity_idx = i
    elif '<!-- Claude -->' in line: claude_idx = i
    elif '<!-- Codex -->' in line: codex_idx = i
    elif '<!-- OpenCode -->' in line: opencode_idx = i

if antigravity_idx != -1:
    antigravity_block = lines[antigravity_idx:antigravity_idx+3]
    claude_block = lines[claude_idx:claude_idx+3]
    codex_block = lines[codex_idx:codex_idx+3]
    opencode_block = lines[opencode_idx:opencode_idx+3]
    
    # Modify y-coords for Claude (to 1)
    claude_block[1] = re.sub(r'y="187"', 'y="147"', claude_block[1])
    claude_block[2] = re.sub(r'y="200"', 'y="160"', claude_block[2])
    
    # Modify y-coords for Codex (to 2)
    codex_block[1] = re.sub(r'y="227"', 'y="187"', codex_block[1])
    codex_block[2] = re.sub(r'y="240"', 'y="200"', codex_block[2])
    
    # Modify y-coords for OpenCode (to 3)
    opencode_block[1] = re.sub(r'y="267"', 'y="227"', opencode_block[1])
    opencode_block[2] = re.sub(r'y="280"', 'y="240"', opencode_block[2])
    
    # Modify Antigravity (to 4, larger and highlighted)
    # y to 267 (img) and 290 (text)
    # font-size to 20, width/height to 32
    # x for image = 215
    
    ag_img = antigravity_block[1]
    ag_img = re.sub(r'x="[^"]+"', 'x="215"', ag_img)
    ag_img = re.sub(r'y="[^"]+"', 'y="267"', ag_img)
    ag_img = re.sub(r'width="18"', 'width="32"', ag_img)
    ag_img = re.sub(r'height="18"', 'height="32"', ag_img)
    antigravity_block[1] = ag_img
    
    ag_text = antigravity_block[2]
    ag_text = re.sub(r'y="[^"]+"', 'y="290"', ag_text)
    ag_text = re.sub(r'font-size="14"', 'font-size="20"', ag_text)
    ag_text = re.sub(r'fill="#1a1a1a"', 'fill="#0055ff"', ag_text)
    antigravity_block[2] = ag_text
    
    # Add a highlight background
    highlight = '  <rect x="180" y="255" width="240" height="50" fill="#e3f2fd" rx="8" />\n'
    
    # Replace the lines
    new_blocks = claude_block + codex_block + opencode_block + [highlight] + antigravity_block
    
    # We replace from antigravity_idx to opencode_idx+3
    end_idx = opencode_idx + 3
    lines = lines[:antigravity_idx] + new_blocks + lines[end_idx:]
    
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('SVG updated successfully.')
