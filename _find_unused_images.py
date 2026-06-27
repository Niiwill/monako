import os
import re
root = os.getcwd()
img_files = []
for dirpath, dirnames, filenames in os.walk(root):
    for fn in filenames:
        if fn.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')):
            img_files.append(os.path.relpath(os.path.join(dirpath, fn), root).replace('\\', '/'))
refs = set()
pat = re.compile(r'(?:(?:src|href|data-src)=\s*["\']?|url\(\s*["\']?)([^"\')>\s]+)', re.I)
for dirpath, dirnames, filenames in os.walk(root):
    for fn in filenames:
        if fn.lower().endswith(('.html', '.htm', '.css', '.js')):
            path = os.path.join(dirpath, fn)
            try:
                with open(path, encoding='utf-8', errors='ignore') as f:
                    text = f.read()
            except Exception:
                continue
            for m in pat.finditer(text):
                val = m.group(1)
                if 'images/' in val or 'images\\' in val:
                    n = val.split('#')[0].split('?')[0]
                    n = n.replace('\\', '/')
                    if n.startswith(('http://', 'https://')):
                        idx = n.find('/images/')
                        if idx != -1:
                            n = n[idx+1:]
                    if n.startswith('/'):
                        n = n[1:]
                    refs.add(n)
                    if n.startswith('../'):
                        refs.add(n[3:])
used = set()
for f in img_files:
    if f in refs:
        used.add(f)
    elif any(f.endswith('/' + os.path.basename(r)) for r in refs):
        used.add(f)
    elif any(f == r.replace('..', '').lstrip('/') for r in refs):
        used.add(f)
unused = sorted([f for f in img_files if f not in used])
print('TOTAL images:', len(img_files))
print('REFERENCED images:', len([f for f in img_files if f in used]))
print('UNUSED images:', len(unused))
for f in unused:
    print(f)
