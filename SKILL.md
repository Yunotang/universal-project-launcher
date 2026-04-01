# Universal Project Launcher (Python, Node.js, Java)

## Overview

This skill provides an automated, security-focused workflow for setting up and launching any software project across multiple technical stacks. It handles environment creation, dependency synchronization, multi-layer security scanning, and ensures projects can be launched both immediately and persistently.

## Workflow

### Step 1: Intelligent Tech Stack & Entry Point Selection
1. **Detection**: Scan for markers of supported ecosystems:
   - **Python**: `requirements.txt`, `pyproject.toml`, or imports (`fastapi`, `flask`, `pyside6`, etc.).
   - **Node.js**: `package.json`, `next.config.js`, `vite.config.ts`.
   - **Java**: `pom.xml`, `build.gradle`, `application.properties`.
2. **Select**: 
   - If multiple entry points are found (e.g., `main.py` vs `server.py`), present a choice list using `ask_user`.

### Step 2: Environment & Dependency Management
1. **Python**: Create `venv`, install dependencies from `requirements.txt` or `pyproject.toml`.
2. **Node.js**: Ensure `node_modules` is present; execute `npm install` if needed.
3. **Java**: Ensure JDK is configured; execute `./mvnw install` or `./gradlew build`.

### Step 3: Mandatory Behavioral Code Scan & Security Audit
1. **Vulnerability Scan**: Use `mcp_osvScanner` to check for known flaws in project dependencies across all supported ecosystems.
2. **Deep Behavioral Audit (Local Files)**: Analyze main script/entry point **AND ALL LOCALLY IMPORTED .py/.js FILES** for:
   - **Hardcoded Secrets**: Scan for `API_KEY`, `PASSWORD`, `SECRET` strings.
   - **Command Injections**: Scan for `os.system`, `subprocess.run`, `eval`, `exec`.
   - **Data Exfiltration**: Scan for suspicious network connections (e.g., `requests.post` to unknown domains).
   - **Sensitive File Access**: Scan for `os.remove`, `shutil.rmtree`, or system configuration modification.
3. **⚠️ MANDATORY SECURITY GATE**: After completing Step 3 and before proceeding to Step 4, the agent **MUST** present a summary of the Security Audit to the user and explicitly confirm: "I have audited the source code and found no malicious patterns. Do you approve the launch?"

### Step 4: Dual Launch Strategy (Immediate & Persistent)
1. **Immediate Background Launch**: 
   - **Python**: Use `venv\Scripts\python.exe -u [main].py`.
   - **Node.js**: Use `npm run dev` or `npm start`.
   - **Validation**: Monitor stdout for successful startup signals.
2. **Persistent Launcher Creation**:
   - Generate a `launch_[project_name].bat` file in the project root.
3. **Notify**: Inform the user that the application has been launched in the background AND the persistent launcher is ready.

## Key Principles
- **Safety Over Speed**: Never prioritize a fast launch over a thorough code audit.
- **Ecosystem Agnostic**: Automatically adapt commands based on the detected language and framework.
- **Log Transparency**: Always use unbuffered modes (like `python -u`) to ensure real-time terminal logging.
- **Fail-Fast Validation**: The AI agent MUST verify a successful background startup signal before confirming completion to the user.
- **Background Persistence**: Ensure the application doesn't block the CLI while it runs.
