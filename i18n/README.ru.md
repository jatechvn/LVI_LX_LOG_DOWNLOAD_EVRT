# 🤖 LVI_LX_LOG_DOWNLOAD_EVRT

<p align="center">
  <br>
  <i>**LVI_LX_LOG_DOWNLOAD_EVRT** — это приложение, разработанное на Python.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License">
</p>

<p align="center"><a href="#quick-start">🚀 Quick Start</a> • <a href="#features">💡 Features</a> • <a href="#setup">📖 Setup</a> • <a href="https://jatechvn.github.io/">🌐 Website</a></p>

<p align="center"><a href="../README.md">🇺🇸 English</a> • <a href="README.vi.md">🇻🇳 Tiếng Việt</a> • <a href="README.zh-CN.md">🇨🇳 中文</a> • <a href="README.ja-JP.md">🇯🇵 日本語</a> • <a href="README.es.md">🇪🇸 Español</a> • <a href="README.fr.md">🇫🇷 Français</a> • <a href="README.de.md">🇩🇪 Deutsch</a> • 🇷🇺 Русский • <a href="README.pt.md">🇵🇹 Português</a> • <a href="README.ko.md">🇰🇷 한국어</a></p>

---

<a id="introduction"></a>
## Описание проекта

Проект стандартизирован в соответствии с профессиональной структурой проекта и поддерживает эффективное управление исходным кодом с помощью Git.

<a id="features"></a>
## Ключевые возможности

- Быстрая настройка и профессиональная упаковка.
- Легковесная конфигурация, простота поддержки и расширения.
- Автоматизированный процесс отправки изменений в Git с помощью встроенного скрипта.

---

## Структура каталогов

```text
LVI_LX_LOG_DOWNLOAD_EVRT/
├── main.py                    # Точка входа в приложение
├── run.bat                    # Скрипт запуска для Windows
├── requirements.txt           # Список зависимостей
├── config.ini                 # Простой файл конфигурации
├── config.json                # Файл конфигурации JSON
├── .gitignore                 # Файл исключений Git
├── README.md                  # Документация проекта (этот файл)
├── LICENSE                    # Файл лицензии
├── ABOUT.txt                  # Краткое описание проекта
├── git_push.bat               # Скрипт автоотправки кода на GitHub
│
├── logs/                      # Журналы работы приложения
│
├── modules/                   # Основные модули с бизнес-логикой
│   ├── ui.py                  # Giao diện người dùng
│   ├── logic.py               # Logic nghiệp vụ chính
│   ├── utils.py               # Các hàm tiện ích dùng chung
│   ├── constants.py           # Hằng số cấu hình
│   └── logger_config.py       # Cấu hình logging
│
└── assets/                    # Статические ресурсы приложения
```

---

<a id="setup"></a>
## Руководство по установке и запуску

### Системные требования
*   Операционная система: **Windows 10/11**
*   Интерпретатор: **Python 3.13** или соответствующая среда.

<a id="quick-start"></a>
### Запуск
1. Установите необходимые зависимости:
   ```cmd
   pip install -r requirements.txt
   ```
2. Запустите приложение:
   ```cmd
   run.bat
   ```

---

## Лицензия

Этот проект распространяется под **лицензией MIT**. Подробности см. в файле [LICENSE](LICENSE).
