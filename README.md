# 🤖 LVI_LX_LOG_DOWNLOAD_EVRT

<p align="center">
  <br>
  <i>**LVI_LX_LOG_DOWNLOAD_EVRT** is an application developed in Python.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License">
</p>

<p align="center"><a href="#quick-start">🚀 Quick Start</a> • <a href="#features">💡 Features</a> • <a href="#setup">📖 Setup</a> • <a href="https://jatechvn.github.io/">🌐 Website</a></p>

<p align="center">🇺🇸 English • <a href="i18n/README.vi.md">🇻🇳 Tiếng Việt</a> • <a href="i18n/README.zh-CN.md">🇨🇳 中文</a> • <a href="i18n/README.ja-JP.md">🇯🇵 日本語</a> • <a href="i18n/README.es.md">🇪🇸 Español</a> • <a href="i18n/README.fr.md">🇫🇷 Français</a> • <a href="i18n/README.de.md">🇩🇪 Deutsch</a> • <a href="i18n/README.ru.md">🇷🇺 Русский</a> • <a href="i18n/README.pt.md">🇵🇹 Português</a> • <a href="i18n/README.ko.md">🇰🇷 한국어</a></p>

---

<a id="introduction"></a>
## Introduction

The project is standardized according to professional project structures, supporting efficient source code management via Git.

<a id="features"></a>
## Features

- Quick setup and professional packaging.
- Lightweight configuration, easy to maintain and extend.
- Automated Git push workflow with included script.

---

## Directory Structure

```text
LVI_LX_LOG_DOWNLOAD_EVRT/
├── main.py                    # Entry point of the application
├── run.bat                    # Quick start script on Windows
├── requirements.txt           # Dependencies list
├── config.ini                 # Simple configuration file
├── config.json                # Structured JSON configuration file
├── .gitignore                 # Git ignore patterns
├── README.md                  # Project documentation (this file)
├── LICENSE                    # License file
├── ABOUT.txt                  # Project short description
├── git_push.bat               # Auto push script to GitHub
│
├── logs/                      # Application logs
│
├── modules/                   # Core modules containing business logic
│   ├── ui.py                  # User Interface
│   ├── logic.py               # Core Logic
│   ├── utils.py               # Helper Functions
│   ├── constants.py           # Constants
│   └── logger_config.py       # Logger Config
│
└── assets/                    # Static assets of the application
```

---

<a id="setup"></a>
## Setup & Usage Guide

### System Requirements
*   OS: **Windows 10/11**
*   Interpreter: **Python 3.13** or matching environment.

<a id="quick-start"></a>
### How to Run
1. Install required dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
2. Run the application:
   ```cmd
   run.bat
   ```

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
