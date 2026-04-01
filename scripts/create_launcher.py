import os
import sys
import platform

def check_python_version():
    major, minor = sys.version_info.major, sys.version_info.minor
    # 遵循 GEMINI.md 要求：Python 3.11 或 3.13
    if major == 3 and (minor == 11 or minor == 13):
        return True
    return False

def create_bat_launcher(project_name, entry_point, project_type):
    bat_content = "@echo off\n"
    bat_content += f"echo Launching {project_name}...\n"
    
    if project_type == 'python':
        if os.path.exists('.venv'):
            bat_content += "call .venv\\Scripts\\activate\n"
        bat_content += f"python \"{entry_point}\"\n"
    elif project_type == 'nodejs':
        bat_content += f"node \"{entry_point}\"\n"
    elif project_type == 'java':
        bat_content += f"java -jar \"{entry_point}\"\n"
    
    bat_content += "pause\n"
    
    filename = f"launch_{project_name.lower().replace(' ', '_')}.bat"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(bat_content)
        print(f"✅ Success: Created persistent launcher -> {filename}")
        return True
    except Exception as e:
        print(f"❌ Error: Failed to create launcher: {str(e)}")
        return False

if __name__ == '__main__':
    if not check_python_version():
        print(f"⚠️ Warning: Current Python version ({sys.version}) does not match recommended 3.11/3.13.")
    
    # Example usage (can be called from the main workflow)
    if len(sys.argv) > 3:
        create_bat_launcher(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python create_launcher.py [project_name] [entry_point] [type]")
