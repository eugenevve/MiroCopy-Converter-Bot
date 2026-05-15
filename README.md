# 📄 MiroCopy-Converter-Bot

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org)
[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-green.svg)](https://docs.aiogram.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)](https://www.docker.com)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Open%20Bot-blue?logo=telegram)](https://t.me/mirocopy_converter_bot)

A simple Telegram bot that converts images into a single PDF file.

👉 **Try it here:** https://t.me/mirocopy_converter_bot

---

## ✨ Features

- 📷 Convert single image to PDF
- 🖼 Convert multiple images (albums) into one PDF
- 🗒 Convert txt file to pdf
- 🌍 Multi-language support
- 🔍 Inline-mode support
- ⚡ Fast and asynchronous processing
- 🧹 Automatic temporary file cleanup

---

## 🛠 Tech Stack

- **Python 3.13**
- **Aiogram 3.x** - Telegram Bot framework
- **img2pdf** - Image to PDF conversion
- **python-dotenv** - Environment variables management

---

## 🚀 Quick Start

### 1. Clone repository

```bash
git clone https://github.com/eugeneviktorov/mirocopy-converter-bot.git
cd mirocopy-converter-bot
```

---

### 2. Create `.env` file

Create a `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token
DEBUG_MODE=True
```

---

### 3. Run locally

#### Create virtual environment

```bash
python -m venv .venv
```

#### Activate it

```bash
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Start bot

```bash
python main.py
```

---

## 🐳 Run with Docker

```bash
docker-compose up --build -d
```

Make sure `.env` file exists on the server.

---

## ⚙️ Configuration

Environment variables:

| Variable   | Description             |
| ---------- | ----------------------- |
| BOT_TOKEN  | Telegram bot API token  |
| DEBUG_MODE | Telegram bot debug mode |

---

## 🌍 Supported Languages

- English (EN)
- Russian (RU)
- Spanish (ES)
- Portuguese (PT)
- Indonesian (ID)
- Arabic (AR)

Language is automatically detected from Telegram settings.

---

## 📁 Project Structure

```bash
assets/
bot/
  core/
  handlers/
  locales/
  services/
  telegram/
  ui/
  utils/
docs/
.gitignore
deploy.sh
docker-compose.yml
Dockerfile
LICENSE
main.py
README.md
requirements.txt
```

---

## 🧠 How It Works

1. The user sends an image(s) or file
2. The bot downloads the data
3. Converts them into PDF
4. Sends PDF back to user
5. Cleans temporary files

---

## 📌 Notes

- Large files or albums may take a few seconds to process
- Temporary files are deleted automatically
