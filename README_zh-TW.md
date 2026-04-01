# 萬用專案啟動器 (Python, Node.js, Java)

此儲存庫包含一個專為 **Gemini CLI** 設計的擴展功能（Skill），提供自動化、安全優先的工作流程，用於在多種技術棧上設置並啟動軟體專案。

## 功能特點
- **智慧技術棧偵測**：自動識別 Python、Node.js 與 Java 專案。
- **環境與依賴管理**：處理 `venv`、`npm install` 以及 Java 建置工具配置。
- **強制安全性審核**：在任何啟動前執行 OSV 漏洞掃描與深層行為程式碼分析（如 `os.system`、`eval`、`exec`、硬編碼金鑰等）。
- **雙重啟動策略**：在背景啟動應用程式以供立即使用，並產生一個持久的 `.bat` 啟動檔供日後使用。

## 安裝方式

直接從 GitHub 安裝：

```bash
gemini skills install https://github.com/<您的用戶名>/universal-project-launcher.git
```

或從本地安裝：

```bash
gemini skills install . --scope user --consent
```

## 自動化工作流程 (不再需要手動操作)

本 Skill 將原本需要開啟額外終端機執行的繁瑣流程全部自動化：

1. **建立虛擬環境**：自動偵測並建立 `.venv` 或 `node_modules`。
2. **啟動虛擬環境**：自動掛載環境，確保依賴隔離。
3. **依賴安裝與安全檢查**：執行 `pip install` 或 `npm install`。
   - 🛡️ **安全性檢查**：安裝前會比對 OSV 數據庫，攔截已知漏洞套件。
4. **啟動、驗證與建立快捷啟動檔**：
   - 🛡️ **代碼審核**：啟動前進行深層行為審計（API Key、系統調用）。
   - **快速啟動**：自動生成 `launch_[專案名].bat`，未來只需按一下即可秒開專案。

## 如何使用
安裝完成後，重新載入您的技能：
`/skills reload`

接著直接詢問 Gemini CLI：
- 「幫我設定環境並啟動我的專案。」
- 「掃描此資料夾並開啟伺服器。」
- 「驗證安全性並執行應用程式。」

## 安全優先
此技能優先考量安全性。在自動化行為審核後，**必須**提供手動安全確認（Manual Confirmation），否則不會啟動任何應用程式。
