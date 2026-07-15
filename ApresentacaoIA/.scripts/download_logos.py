import urllib.request
import os

urls = {
    'chatgpt': 'https://chatgpt.com',
    'gemini': 'https://gemini.google.com',
    'notebooklm': 'https://notebooklm.google.com',
    'whatsapp': 'https://whatsapp.com',
    'claude': 'https://claude.ai',
    'antigravity': 'https://deepmind.google',
    'leonardo': 'https://leonardo.ai',
    'banana': 'https://banana.dev',
    'whisper': 'https://openai.com',
    'audiobox': 'https://audiobox.metademolab.com'
}

os.makedirs('d:/repos/DevComIA/ApresentacaoIA/.assets/logos', exist_ok=True)

for name, url in urls.items():
    api_url = f'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url={url}&size=128'
    try:
        urllib.request.urlretrieve(api_url, f'd:/repos/DevComIA/ApresentacaoIA/.assets/logos/{name}.png')
        print(f'Downloaded {name}.png')
    except Exception as e:
        print(f'Failed for {name}: {e}')
