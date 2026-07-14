import re

content = open('d:/repos/DevComIA/ApresentacaoIA/.assets/brain2.svg', 'r', encoding='utf-8').read()
paths = re.findall(r'd="([^"]+)"', content)
print(f"Total paths: {len(paths)}")
if len(paths) > 0:
    print(f"Path 1 length: {len(paths[0])}")
    print(f"Path 1 start: {paths[0][:50]}")
    print(f"Path 1 end: {paths[0][-50:]}")
if len(paths) > 1:
    print(f"Path 2 length: {len(paths[1])}")
    print(f"Path 2 start: {paths[1][:50]}")
    print(f"Path 2 end: {paths[1][-50:]}")
