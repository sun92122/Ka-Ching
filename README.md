# 💰 Ka-Ching

> **The sound of success. Simple accounting for everyone.**

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-Ninja-092E20?logo=django)
![Vue](https://img.shields.io/badge/Vue.js-3.0-4FC08D?logo=vue.js)
![Docker](https://img.shields.io/badge/Container-Podman%2FDocker-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow)

<!-- Link to other language versions -->
[中文 (繁體)](./docs/README.zh-TW.md)\
[English](./README.md)

## 📖 Introduction

**Ka-Ching** is not your typical, boring enterprise ERP. It is built for the real world—the lemonade stands, the local coffee shops, the university clubs, and the family treasurers.

We believe that tracking your money shouldn't require a CPA license. It should be as satisfying as the sound of a cash register opening. _Ka-Ching!_

This project aims to provide a lightweight, aesthetically pleasing, and intuitive accounting solution for those who find Excel too messy and enterprise software too complex. It combines the privacy of local hosting with the convenience of cloud access.

## ✨ Features

- 🔐 Hybrid Access: Local data privacy meets Cloudflare Zero Trust. Secure remote access without opening a single port.

- 📊 Solid Core: Double-entry bookkeeping with multi-date tracking, smart tagging, and granular audit trails.

- ✍️ Approval Workflows: Built-in signing processes for budgets and settlements. From draft to "Approved" with ease.

- 🖨️ Pixel-Perfect Reports: Generate signature-ready PDFs and analysis-ready CSVs instantly.

- 👥 Role-Based Control: Granular permissions for Admins, Accountants, and Viewers.

## 🛠️ Tech Stack

Built with modern, high-performance tools:

- **Infrastructure:**

  - **Container Runtime:** Podman (Recommended) or Docker.
  - **Gateway:** Nginx with **Hot-Reload Watchdog**.
  - **Tunnel:** Cloudflare Tunnel (`cloudflared`) with **Token Watchdog**.
  - **Database:** PostgreSQL 15.

- **Backend:**

  - **Language:** Python 3.12 (Managed by `uv` for lightning-fast builds).
  - **Framework:** Django 5.0 + Django Ninja (FastAPI-like DX).
  - **PDF Engine:** WeasyPrint.

- **Frontend:**
  - **Framework:** Vue 3 + Vite.
  - **State Management:** Pinia.
  - **UI Library:** Naive UI (Configurable).

## 🚀 Getting Started

### Prerequisites

- [Podman](https://podman.io/) (Recommended) or Docker Desktop installed.
- `podman-compose` or `docker-compose`.

### Installation

1. **Clone the repository**

   ```bash
   git clone [https://github.com/yourusername/ka-ching.git](https://github.com/yourusername/ka-ching.git)
   cd ka-ching
   ```

2. **Configure Environment**
   Create a `.env` file in the root directory:

   ```bash
   # .env
   DB_PASSWORD=secure_password_here
   DJANGO_SECRET=your_super_long_random_string
   # TUNNEL_TOKEN is handled via UI, no need to set it here initially
   ```

3. **Start the Engine**

   ```bash
   podman-compose up -d
   ```

   _Wait a few moments for the initial database migration and permission seeding to complete._

4. **Initial Login (Local)**

   - Open your browser and go to `http://localhost:8080` (or `http://localhost:8080/admin`).
   - Default Credentials:
     - Username: `admin`
     - Password: `admin123`
   - **⚠️ IMPORTANT:** Change your password immediately and update your Email to match your Cloudflare account email.

5. **Go Live (Optional)**
   - Go to **Settings** in the frontend.
   - Paste your **Cloudflare Tunnel Token**.
   - The system will automatically start the tunnel and connect to the world.

## 🗺️ Roadmap

- [ ] **Mobile App:** A companion PWA for quick expense entry on the go.
- [ ] **OCR Scanning:** Upload receipts and auto-fill transaction details using AI.
- [ ] **Multi-Currency:** Better support for foreign currency accounts and exchange rate adjustments.
- [ ] **Dashboard Widgets:** Customizable charts and KPIs for the dashboard.

## 🤝 Contributing

Got a great idea? Found a bug? We'd love your help to make Ka-Ching even louder!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See LICENSE for more information.

<p align="center">Made with ❤️ for small businesses and dreamers everywhere.</p>
