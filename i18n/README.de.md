# 🤖 LVI_LX_LOG_DOWNLOAD_EVRT

<p align="center">
  <br>
  <i>**LVI_LX_LOG_DOWNLOAD_EVRT** ist eine in Python entwickelte Anwendung.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License">
</p>

<p align="center"><a href="#quick-start">🚀 Quick Start</a> • <a href="#features">💡 Features</a> • <a href="#setup">📖 Setup</a> • <a href="https://jatechvn.github.io/">🌐 Website</a></p>

<p align="center"><a href="../README.md">🇺🇸 English</a> • <a href="README.vi.md">🇻🇳 Tiếng Việt</a> • <a href="README.zh-CN.md">🇨🇳 中文</a> • <a href="README.ja-JP.md">🇯🇵 日本語</a> • <a href="README.es.md">🇪🇸 Español</a> • <a href="README.fr.md">🇫🇷 Français</a> • 🇩🇪 Deutsch • <a href="README.ru.md">🇷🇺 Русский</a> • <a href="README.pt.md">🇵🇹 Português</a> • <a href="README.ko.md">🇰🇷 한국어</a></p>

---

<a id="introduction"></a>
## Einführung

Das Projekt ist nach professionellen Projektstrukturen standardisiert und unterstützt eine effiziente Quellcodeverwaltung über Git.

<a id="features"></a>
## Hauptmerkmale

- Schnelle Einrichtung und professionelle Paketierung.
- Leichtgewichtige Konfiguration, einfach zu warten und zu erweitern.
- Automatisierter Git-Push-Workflow mit mitgeliefertem Skript.

---

## Verzeichnisstruktur

```text
LVI_LX_LOG_DOWNLOAD_EVRT/
├── main.py                    # Haupteinstiegspunkt der Anwendung
├── run.bat                    # Schnellstart-Skript für Windows
├── requirements.txt           # Liste der Abhängigkeiten
├── config.ini                 # Einfache Konfigurationsdatei
├── config.json                # Strukturierte JSON-Konfigurationsdatei
├── .gitignore                 # Git-Ausschlussmuster
├── README.md                  # Projektdokumentation (diese Datei)
├── LICENSE                    # Lizenzdatei
├── ABOUT.txt                  # Kurze Projektbeschreibung
├── git_push.bat               # Automatisches Push-Skript zu GitHub
│
├── logs/                      # Anwendungsprotokolle
│
├── modules/                   # Kernmodule mit der Geschäftslogik
│   ├── ui.py                  # Giao diện người dùng
│   ├── logic.py               # Logic nghiệp vụ chính
│   ├── utils.py               # Các hàm tiện ích dùng chung
│   ├── constants.py           # Hằng số cấu hình
│   └── logger_config.py       # Cấu hình logging
│
└── assets/                    # Statische Ressourcen der Anwendung
```

---

<a id="setup"></a>
## Installations- und Nutzungsanleitung

### Systemanforderungen
*   Betriebssystem: **Windows 10/11**
*   Interpreter: **Python 3.13** oder entsprechende Umgebung.

<a id="quick-start"></a>
### Ausführung
1. Erforderliche Abhängigkeiten installieren:
   ```cmd
   pip install -r requirements.txt
   ```
2. Anwendung starten:
   ```cmd
   run.bat
   ```

---

## Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**. Weitere Details finden Sie in der [LICENSE](LICENSE)-Datei.
