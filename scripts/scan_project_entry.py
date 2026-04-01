import os
import re
import json

GUI_LIBRARIES = [
    'tkinter', 'customtkinter', 'PyQt5', 'PyQt6', 'PySide2', 'PySide6', 'kivy', 'flet'
]

def scan_directory(directory='.'):
    results = {
        'python': [],
        'nodejs': [],
        'java': []
    }
    
    for root, dirs, files in os.walk(directory):
        # Skip common non-source directories
        skip_dirs = ['venv', '.venv', '__pycache__', 'node_modules', '.git', 'target', 'build', '.gradle']
        if any(d in root.split(os.sep) for d in skip_dirs):
            continue
            
        for filename in files:
            filepath = os.path.join(root, filename)
            rel_path = os.path.relpath(filepath, directory)

            # --- Python Detection ---
            if filename.endswith('.py'):
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if re.search(r'if\s+__name__\s*==\s*["\']__main__["\']\s*:', content):
                            has_gui = any(re.search(rf'\bimport\s+{lib}\b|\bfrom\s+{lib}\b', content) for lib in GUI_LIBRARIES)
                            results['python'].append({
                                'path': rel_path,
                                'type': 'gui' if has_gui else 'cli'
                            })
                except Exception:
                    pass

            # --- Node.js Detection ---
            if filename == 'package.json':
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        pkg = json.load(f)
                        main_file = pkg.get('main', 'index.js')
                        results['nodejs'].append({
                            'path': rel_path,
                            'entry': main_file,
                            'type': 'package'
                        })
                except Exception:
                    results['nodejs'].append({'path': rel_path, 'type': 'package'})
            elif filename in ['index.js', 'server.js', 'app.js']:
                results['nodejs'].append({'path': rel_path, 'type': 'direct-entry'})

            # --- Java Detection ---
            if filename.endswith('.java'):
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        if 'public static void main' in f.read():
                            results['java'].append({
                                'path': rel_path,
                                'type': 'main-class'
                            })
                except Exception:
                    pass
            elif filename in ['pom.xml', 'build.gradle']:
                results['java'].append({
                    'path': rel_path,
                    'type': 'build-config'
                })
    
    return results

if __name__ == '__main__':
    data = scan_directory()
    print("Detected Project Entry Points:")
    for lang, entries in data.items():
        if entries:
            print(f"\n[{lang.upper()}]")
            for entry in entries:
                print(f"- {entry['path']} ({entry['type']})")
