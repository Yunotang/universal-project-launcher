# 萬用專案啟動器 (僅限 Windows 作業環境)

此儲存庫包含一個專為 **Gemini CLI** 設計的擴展功能（Skill），提供自動化、安全優先的工作流程，用於在多種技術棧上設置並啟動軟體專案。

> **注意：** 本工具專為 **Windows** 系統設計，並使用 `.bat` 腳本實現持久化啟動功能。

## 系統需求
- **作業系統**：Windows 10 或 11 (64-bit)
- **環境**：CMD 或 PowerShell (Windows 原生環境)
- **相依工具**：需在 PATH 中安裝 Python 3.x、Node.js 或 Java。

## 📦 核心工作流程

```mermaid
graph LR
    A[💡 技術棧偵測] --> B[🛡️ 安全性審核]
    B --> C[📦 依賴安裝]
    C --> D[🚀 背景即時啟動]
    D --> E[✅ 建立 .BAT 啟動檔]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ff9,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
```

----------------------------------------

## 功能特點
- **智慧技術棧偵測**：自動識別 Python、Node.js 與 Java 專案，包含對 Java `main` 類別與 Node.js `package.json` 的深層偵測。
- **環境與依賴管理**：處理 `venv`、`npm install` 以及 Java 建置工具配置，並驗證 Python 版本 (3.11/3.13)。
- **強化安全性審核**：在啟動前執行 OSV 掃描與深層行為審計。現在支援：
  - **不分大小寫金鑰偵測** (API_KEY, AWS Access Key 等)。
  - **不安全函式掃描** (Python `pickle`, `yaml.load`, JavaScript `innerHTML` 等)。
- **自動化啟動策略**：
  - **背景即時啟動**：在 Gemini CLI 中直接運行。
  - **持久啟動檔**：自動生成 `launch_[專案名].bat`，未來只需按一下即可秒開專案，包含自動啟動虛擬環境邏輯。

## 安裝方式

直接從 GitHub 安裝：

```bash
gemini skills install https://github.com/Yunotang/universal-project-launcher.git
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
