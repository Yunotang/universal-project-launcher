# 專案優化任務清單 (TODOS)

## 第一輪檢查：入口偵測優化
- [x] 修改 `scripts/scan_project_entry.py` 以支援 Java `main` 類別偵測。
- [x] 修改 `scripts/scan_project_entry.py` 以支援 Node.js `package.json` 讀取與 `index.js` 偵測。

## 第二輪檢查：資安稽核強化
- [x] 修改 `scripts/security_audit.py` 增加大小寫不敏感的正則表達式。
- [x] 增加對 Python `pickle`、`yaml.load` 與 JavaScript `innerHTML` 的掃描。

## 第三輪檢查：啟動功能實作
- [x] 新增 `scripts/create_launcher.py` 腳本，用於產生 Windows `.bat` 啟動檔。
- [x] 整合 Python 版本 (3.11/3.13) 檢查邏輯。

## 第四輪檢查：文件與範例
- [x] 更新 `README_zh-TW.md` 以符合最新的實作行為。
- [x] 確保 `SKILL.md` 中的自動化步驟與實際腳本輸出完全一致。

## 第五輪檢查：最終驗證
- [x] 執行完整的「偵測 -> 稽核 -> 啟動」流程，驗證偵測率。
- [x] 刪除測試用的漏洞檔案，環境清理完成。
