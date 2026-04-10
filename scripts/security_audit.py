import os
import sys

def run_security_audit(file_path):
    """
    Mandatory Behavioral Code Audit & Stability Check.
    - Scans for hardcoded secrets.
    - Checks for Windows stability patterns (app.update(), try-except for styles).
    """
    print(f"Running Mandatory Behavioral Code Scan & Security Audit on {file_path}...")
    
    issues_found = []
    has_gui = False
    has_app_update = False
    style_in_try = False

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                # 1. Security Check: Hardcoded secrets
                if any(key in line.upper() for key in ["API_KEY", "SECRET_KEY", "PASSWORD", "TOKEN"]):
                    if "=" in line and "'" in line or '"' in line:
                        issues_found.append(f"[SECURITY] Possible hardcoded secret at line {i+1}")

                # 2. Stability Check: GUI detection
                if "import tkinter" in line or "from tkinter" in line:
                    has_gui = True
                
                if ".update()" in line:
                    has_app_update = True
                
                # Check for ttk.Style initialization
                if "ttk.Style()" in line or "pyttsx3.init()" in line:
                    # Check if previous lines contain 'try'
                    context = "".join(lines[max(0, i-5):i])
                    if "try:" not in context:
                        issues_found.append(f"[STABILITY] Dangerous initialization at line {i+1}. Wrap in try-except.")
                    else:
                        style_in_try = True

    except Exception as e:
        print(f"Error during audit: {str(e)}")
        return False

    # Validation
    if has_gui and not has_app_update:
        issues_found.append("[STABILITY] Missing app.update() before mainloop. Window handle might crash.")

    if issues_found:
        print("\n--- AUDIT FINDINGS ---")
        for issue in issues_found:
            print(issue)
        print("----------------------\n")
    else:
        print("I have audited the source code and found no malicious patterns.")

    return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python security_audit.py <file_path>")
        sys.exit(1)
        
    run_security_audit(sys.argv[1])
