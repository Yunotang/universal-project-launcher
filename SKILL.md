---
name: universal-project-launcher
description: 自動化 Python/Node.js/Java 專案的環境設定、依賴安裝與安全啟動。偵測到 requirements.txt, package.json, pom.xml 或使用者要求「跑這個專案」時啟動。
---

# Universal Project Launcher (Python, Node.js, Java)

## Trigger Conditions
當偵測到以下情況時，Gemini CLI 應主動建議啟動此技能：
- 專案根目錄存在 `requirements.txt`、`package.json` 或 `pom.xml`。
- 使用者要求「幫我執行這個程式」、「如何啟動這個專案？」或「環境怎麼架設？」。
- 偵測到 Python (`.py`)、Node.js (`.js`) 或 Java (`.java`) 原始碼檔案。

## Workflow

### Step 0: 環境檢查 (Date & CMD)
1. **日期確認**：執行 `cmd /c "date /t"` 確保啟動器與日誌時間戳記精確。
2. **指令限制**：嚴禁在 `run_shell_command` 中使用 `&&` 串接指令，必須拆分為獨立呼叫。

### Step 1: Intelligent Tech Stack & Entry Point Selection
1. **Detection**: Scan for ecosystem markers:
   - **Python**: `requirements.txt`, `pyproject.toml`
   - **Node.js**: `package.json`
   - **Java**: `pom.xml`, `build.gradle`
2. **Identify Entry Points**: Execute `scripts/scan_project_entry.py` to find valid launch paths.
3. **⚠️ MANDATORY SELECTION**: 使用 `ask_user` 讓使用者確認偵測到的進入點。**未經確認前不得進入下一步**。

### Step 2: Environment & Dependency Management
1. **Python**: 執行 `python -m venv .venv`，並使用路徑 `.venv\Scripts\python.exe` 執行。
2. **Node.js**: 檢查 `node_modules` 是否存在。若無，**詢問**使用者是否需要手動執行 `npm install`。
3. **Java**: 驗證 `java -version` 與 Maven/Gradle 環境。

### Step 3: Mandatory Dependency Installation & Security Audit
1. **🛡️ Vulnerability Scan**: 使用 `mcp_osvScanner` 檢查依賴文件的已知漏洞。
2. **Behavioral Code Audit**: 對進入點檔案執行 `scripts/security_audit.py`。
   - **查核點**：Hardcoded Secrets、`os.system` 呼叫、可疑的網路連線。

### Step 4: Verified Launch & Persistent Launcher Creation
1. **⚠️ MANDATORY SECURITY GATE**: 顯示審計摘要並詢問：「我已完成原始碼審計且未發現惡意行為。您是否同意啟動？」
2. **Immediate Background Launch**: 使用 `python -u` 啟動並監控實時日誌。
3. **Persistent Launcher**: 執行 `scripts/create_launcher.py` 產生 `launch_[project_name].bat`。
   - **驗證**：產生的 `.bat` 內含 Python 3.11/3.13 版本檢查。

## Key Principles
- **安全重於速度**：不因追求快速啟動而跳過安全審計。
- **使用者導向**：所有涉及環境變更或程式執行的操作，必須先徵得使用者同意。
- **Windows 相容性**：確保所有指令相容 Windows CMD 環境。
