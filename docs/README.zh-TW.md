# 💰 Ka-Ching

> **成功的聲音。為每個人打造的簡單記帳系統。**

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-Ninja-092E20?logo=django)
![Vue](https://img.shields.io/badge/Vue.js-3.0-4FC08D?logo=vue.js)
![Docker](https://img.shields.io/badge/Container-Podman%2FDocker-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-Apache%202.0-yellow)

<!-- Link to other language versions -->
[中文 (繁體)](./README.zh-TW.md)\
[English](../README.md)

## 📖 簡介

**Ka-Ching** 不是那種典型、枯燥的企業級 ERP。它是為了真實世界而打造的——無論是檸檬水攤、在地咖啡廳、大學社團，還是家庭裡的財務大臣。

我們相信，追蹤財務狀況不需要會計師執照。這應該就像收銀機打開的聲音一樣令人滿足。 _Ka-Ching!_

本專案旨在為那些覺得 Excel 太混亂、企業軟體太複雜的人，提供一個輕量、美觀且直觀的會計解決方案。它完美結合了**本地託管的隱私性**與**雲端存取的便利性**。

## ✨ 特色功能

- 🔐 **混合存取 (Hybrid Access)**：本地資料隱私結合 Cloudflare Zero Trust。無需開放任何防火牆連接埠即可安全地遠端存取。

- 📊 **穩固核心**：支援多重日期追蹤、智慧標籤以及細緻稽核軌跡的複式簿記系統。

- ✍️ **簽核流程**：內建預算與結算的簽核流程。從草稿到「已核准」輕鬆完成。

- 🖨️ **精準報表**：即時生成可供簽核的 PDF 以及便於分析的 CSV。

- 👥 **角色權限控制**：針對管理員 (Admins)、會計 (Accountants) 和檢視者 (Viewers) 提供細緻的權限管理。

## 🛠️ 技術堆疊

使用現代化、高效能工具構建：

- **基礎設施 (Infrastructure):**

  - **容器執行環境:** Podman (推薦) 或 Docker。
  - **閘道器 (Gateway):** 具備 **熱重載看門狗 (Hot-Reload Watchdog)** 的 Nginx。
  - **通道 (Tunnel):** 具備 **Token 看門狗 (Token Watchdog)** 的 Cloudflare Tunnel (`cloudflared`)。
  - **資料庫:** PostgreSQL 15。

- **後端 (Backend):**

  - **語言:** Python 3.12 (由 `uv` 管理，建置速度極快)。
  - **框架:** Django 5.0 + Django Ninja (類似 FastAPI 的開發體驗)。
  - **PDF 引擎:** WeasyPrint。

- **前端 (Frontend):**
  - **框架:** Vue 3 + Vite。
  - **狀態管理:** Pinia。
  - **UI 函式庫:** Naive UI (可設定)。

## 🚀 快速開始

### 事前準備

- 已安裝 [Podman](https://podman.io/) (推薦) 或 Docker Desktop。
- 已安裝 `podman-compose` 或 `docker-compose`。

### 安裝步驟

1. **複製專案 (Clone the repository)**

   ```bash
   git clone [https://github.com/yourusername/ka-ching.git](https://github.com/yourusername/ka-ching.git)
   cd ka-ching
   ```

2. **設定環境變數**
   在專案根目錄建立一個 .env 檔案：

   ```bash
   # .env
   DB_PASSWORD=secure_password_here
   DJANGO_SECRET=your_super_long_random_string
   # TUNNEL_TOKEN 是透過 UI 處理的，無需在此初始設定
   ```

3. **啟動系統引擎**

   ```bash
   podman-compose up -d
   ```

   _等待片刻，直到初始資料庫遷移和權限設定完成。_

4. **初次登入 (本地端)**

   - 打開瀏覽器並前往 `http://localhost:8080` (或 `http://localhost:8080/admin`)。
   - 預設憑證：
     - 帳號 (Username): `admin`
     - 密碼 (Password): `admin123`
   - **⚠️ 重要：** 請立即更改您的密碼，並更新您的 Email 以符合您的 Cloudflare 帳號 Email。

5. **設定 Cloudflare Tunnel Token（選用）**

   - 登入後台，前往「設定 (Settings)」頁面。
   - 在「Cloudflare Tunnel Token」欄位中輸入您的 Token，然後儲存設定。
   - 系統將自動配置並啟動 Cloudflare Tunnel，以便您可以從遠端安全存取您的 Ka-Ching 實例。

## 🗺️ 未來規劃

- [ ] 行動 App: 用於快速記帳的 PWA (漸進式網頁應用程式)。
- [ ] OCR 掃描: 上傳收據並利用 AI 自動填寫交易明細。
- [ ] 多幣別支援: 更好的外幣帳戶支援與匯率調整功能。
- [ ] 儀表板小工具: 可自定義的圖表與關鍵績效指標 (KPI)。

## 🤝 貢獻與參與

有好點子嗎？發現了 Bug？我們非常歡迎您的幫忙，讓 Ka-Ching 更加響亮！

1. Fork 本專案
2. 建立您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 發起 Pull Request

## 📄 授權條款

本專案採用 Apache 2.0 授權條款發布。詳情請參閱 LICENSE 文件。

<p align="center">Made with ❤️ 獻給各地的小型商家與夢想家。</p>
