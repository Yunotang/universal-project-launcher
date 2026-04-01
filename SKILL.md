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
2. **Identify Entry Points**: Execute `scripts/scan_project_entry.py` to find valid launch paths (GUI or CLI).

### Step 2: Environment & Dependency Management (Automated)
1. **Virtual Environment Creation**:
   - **Python**: Execute `python -m venv .venv`.
   - **Node.js**: Ensure local directory readiness for `npm install`.
2. **Environment Activation**: Automatically link execution to the local environment (e.g., `.venv\Scripts\python.exe`) to ensure dependency isolation.

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
3. **Persistent Launcher Generation**: Automatically create a `launch_[project_name].bat` file in the root directory for future one-click access.

## Key Principles
- **Safety Over Speed**: Never bypass the security audit for the sake of a faster launch.
- **Seamless Automation**: Transform complex multi-terminal manual setups into a single, unified AI-driven command.
- **Fail-Fast Validation**: If the app fails to start or outputs errors during the initial launch, report the exact failure point to the user immediately.
