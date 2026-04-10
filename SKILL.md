---
name: universal-project-launcher
description: 自動化 Python/Node.js/Java 專案的環境設定、依賴安裝與安全啟動。Automates setup, dependency installation, and secure launch for Python/Node.js/Java projects with deep security auditing.
---

# Universal Project Launcher (Python, Node.js, Java)

## Workflow

### Step 1: Intelligent Tech Stack & Entry Point Selection
1. **Detection**: Scan for ecosystem markers:
   - **Python**: `requirements.txt`, `pyproject.toml`
   - **Node.js**: `package.json`
   - **Java**: `pom.xml`, `build.gradle`
2. **Identify Entry Points**: Execute `scripts/scan_project_entry.py` to find valid launch paths (GUI, CLI, or Framework-specific like Streamlit/Flask).
3. **⚠️ MANDATORY SELECTION**: Present all detected entry points to the user and **ask for confirmation**.
   - If multiple found: Let the user choose using `ask_user`.
   - If zero/incorrect found: Ask the user to manually provide the entry point filename.
   - **DO NOT** proceed to environment setup or installation before this confirmation.

### Step 2: Environment & Dependency Management (Automated)
1. **Virtual Environment Creation**:
   - **Python**: Execute `python -m venv .venv`.
   - **Node.js**: Ensure local directory readiness for `npm install`.
2. **Environment Activation**: Automatically link execution to the local environment (e.g., `.venv\Scripts\python.exe`) to ensure dependency isolation.
   - **PowerShell Execution Rule**: When running executable paths with spaces or quotes in PowerShell, always prefix with `&` (e.g., `& ".venv\Scripts\python.exe" "entry.py"`).

### Step 3: Mandatory Dependency Installation & Security Audit
1. **Dependency Installation (PIP/NPM)**:
   - 🛡️ **Vulnerability Scan**: Use `mcp_osvScanner` to check for known flaws in `requirements.txt` or `package.json`.
   - **Block High-Risk Packages**: If critical vulnerabilities are found, HALT installation and notify the user immediately.
2. **Behavioral Code Audit**:
   - Execute `scripts/security_audit.py` on the entry point and locally imported modules.
   - 🛡️ **Checkpoints**: Hardcoded secrets (`API_KEY`), Command injections (`os.system`), and Suspicious network exfiltration.

### Step 4: Verified Launch & Persistent Launcher Creation
1. **⚠️ MANDATORY SECURITY GATE**: After completing Step 3, display a summary of findings and explicitly ask: "I have audited the source code and found no malicious patterns. Do you approve the launch?"
2. **Immediate Background Launch**: Use `python -u` (Unbuffered) to launch the app and monitor real-time logs for successful startup signals.
3. **Persistent Launcher Generation**: 
   - Execute `scripts/create_launcher.py` with detected entry point.
   - Automatically create a `launch_[project_name].bat` file in the root directory for future one-click access.
   - **Environment Validation**: Includes a check for Python 3.x during launcher creation.

## Windows Stability Standards (Mandatory)

### .BAT Launcher Design
- **All English**: Use English only for titles, echoes, and variable names (no UTF-8 in .bat source).
- **Pure Linear Execution**: No `if` blocks or loops in `.bat`. Ensure the flow is a direct sequence of commands.
- **No Emoji**: Remove all emoji and special symbols from launcher text.
- **Environment Flags**: Every launcher must start with `set PYTHONUTF8=1`.

### Path Handling
- **Absolute Reference**: Always use `"%~dp0"` to resolve local file paths.
- **Quote Safety**: Every file path reference must be enclosed in double quotes (e.g., `"%~dp0.venv\Scripts\python.exe"`) to prevent crashes on paths containing spaces.

### GUI Defensive Initialization (Python)
- **Safe Initialization**: All `pyttsx3.init()` or `ttk.Style()` assignments must be wrapped in `try...except` blocks.
- **Visual Warm-up**: Call `app.update()` (or root window update) immediately before the final `mainloop()` call to ensure the window handle is fully ready.

## Key Principles
- **Safety Over Speed**: Never bypass the security audit for the sake of a faster launch.
- **Seamless Automation**: Transform complex multi-terminal manual setups into a single, unified AI-driven command.
- **Fail-Fast Validation**: If the app fails to start or outputs errors during the initial launch, report the exact failure point to the user immediately.
- **Shell Compatibility**: Use CMD-compatible syntax for `.bat` generation and PowerShell-safe syntax (`&`) for direct agent executions.
