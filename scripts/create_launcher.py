import os
import sys
import argparse

def create_bat_launcher(project_name, entry_point):
    """
    Creates a robust, linear, all-English Windows launcher (.bat).
    Follows Windows Stability Standards:
    - Pure linear execution (no IF blocks).
    - Absolute path referencing via %~dp0.
    - Forced UTF-8 via PYTHONUTF8=1.
    - No Emoji or non-ASCII characters.
    """
    
    # 1. Determine app type in Python (not in .bat)
    is_streamlit = False
    try:
        with open(entry_point, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if 'import streamlit' in content or 'from streamlit' in content:
                is_streamlit = True
    except:
        pass

    # 2. Construct absolute paths and command
    # Use %~dp0 to ensure the launcher works regardless of where it's called from
    python_exe = '"%~dp0.venv\\Scripts\\python.exe"'
    entry_abs = f'"%~dp0{os.path.basename(entry_point)}"'
    
    if is_streamlit:
        launcher_cmd = f'{python_exe} -m streamlit run {entry_abs}'
    else:
        launcher_cmd = f'{python_exe} {entry_abs}'

    # 3. Generate pure linear .bat content
    bat_content = f'''@echo off
setlocal
title {project_name} Launcher
cd /d "%~dp0"

set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
chcp 65001 >nul

echo ============================================
echo Starting {project_name}...
echo Target: {entry_abs}
echo ============================================

{launcher_cmd}

echo.
echo ============================================
echo Execution finished.
echo ============================================
pause
exit /b
'''
    # Use standard project name format
    safe_name = project_name.lower().replace(' ', '_')
    filename = f"launch_{safe_name}.bat"
    
    try:
        # Save with standard UTF-8 (w/o BOM) for maximum compatibility
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(bat_content)
        print(f"Success: Created standardized launcher -> {filename}")
        return True
    except Exception as e:
        print(f"Error: Failed to create launcher: {str(e)}")
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a standardized Windows launcher.')
    parser.add_argument('--name', required=True, help='Project name')
    parser.add_argument('--entry', required=True, help='Entry point filename')
    parser.add_argument('--path', help='Project path (optional)')
    
    args = parser.parse_args()
    
    if args.path:
        os.chdir(args.path)
        
    create_bat_launcher(args.name, args.entry)
