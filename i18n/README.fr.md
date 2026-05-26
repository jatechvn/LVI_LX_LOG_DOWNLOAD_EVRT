# 🤖 LVI_LX_LOG_DOWNLOAD_EVRT

<p align="center">
  <br>
  <i>**LVI_LX_LOG_DOWNLOAD_EVRT** est une application développée en Python.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License">
</p>

<p align="center"><a href="#quick-start">🚀 Quick Start</a> • <a href="#features">💡 Features</a> • <a href="#setup">📖 Setup</a> • <a href="https://jatechvn.github.io/">🌐 Website</a></p>

<p align="center"><a href="../README.md">🇺🇸 English</a> • <a href="README.vi.md">🇻🇳 Tiếng Việt</a> • <a href="README.zh-CN.md">🇨🇳 中文</a> • <a href="README.ja-JP.md">🇯🇵 日本語</a> • <a href="README.es.md">🇪🇸 Español</a> • 🇫🇷 Français • <a href="README.de.md">🇩🇪 Deutsch</a> • <a href="README.ru.md">🇷🇺 Русский</a> • <a href="README.pt.md">🇵🇹 Português</a> • <a href="README.ko.md">🇰🇷 한국어</a></p>

---

<a id="introduction"></a>
## Introduction

Le projet est standardisé selon des structures de projet professionnelles, supportant une gestion efficace du code source via Git.

<a id="features"></a>
## Caractéristiques Principales

- Configuration rapide et packaging professionnel.
- Configuration légère, facile à maintenir et à étendre.
- Processus d'envoi automatique vers Git grâce au script fourni.

---

## Structure des Répertoires

```text
LVI_LX_LOG_DOWNLOAD_EVRT/
├── main.py                    # Point d'entrée de l'application
├── run.bat                    # Script de démarrage rapide sur Windows
├── requirements.txt           # Liste des dépendances
├── config.ini                 # Fichier de configuration simple
├── config.json                # Fichier de configuration JSON
├── .gitignore                 # Modèles d'exclusion Git
├── README.md                  # Documentation du projet (ce fichier)
├── LICENSE                    # Fichier de licence
├── ABOUT.txt                  # Brève description du projet
├── git_push.bat               # Script d'envoi automatique vers GitHub
│
├── logs/                      # Journaux d'activité de l'application
│
├── modules/                   # Modules principaux contenant la logique métier
│   ├── ui.py                  # Giao diện người dùng
│   ├── logic.py               # Logic nghiệp vụ chính
│   ├── utils.py               # Các hàm tiện ích dùng chung
│   ├── constants.py           # Hằng số cấu hình
│   └── logger_config.py       # Cấu hình logging
│
└── assets/                    # Ressources statiques de l'application
```

---

<a id="setup"></a>
## Guide d'Installation et d'Utilisation

### Configuration Système Requise
*   Système d'exploitation : **Windows 10/11**
*   Interpréteur : **Python 3.13** ou environnement correspondant.

<a id="quick-start"></a>
### Comment Lancer
1. Installer les dépendances requises :
   ```cmd
   pip install -r requirements.txt
   ```
2. Lancer l'application :
   ```cmd
   run.bat
   ```

---

## Licence

Ce projet est sous **Licence MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
