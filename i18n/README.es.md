# 🤖 LVI_LX_LOG_DOWNLOAD_EVRT

<p align="center">
  <br>
  <i>**LVI_LX_LOG_DOWNLOAD_EVRT** es una aplicación desarrollada en Python.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License">
</p>

<p align="center"><a href="#quick-start">🚀 Quick Start</a> • <a href="#features">💡 Features</a> • <a href="#setup">📖 Setup</a> • <a href="https://jatechvn.github.io/">🌐 Website</a></p>

<p align="center"><a href="../README.md">🇺🇸 English</a> • <a href="README.vi.md">🇻🇳 Tiếng Việt</a> • <a href="README.zh-CN.md">🇨🇳 中文</a> • <a href="README.ja-JP.md">🇯🇵 日本語</a> • 🇪🇸 Español • <a href="README.fr.md">🇫🇷 Français</a> • <a href="README.de.md">🇩🇪 Deutsch</a> • <a href="README.ru.md">🇷🇺 Русский</a> • <a href="README.pt.md">🇵🇹 Português</a> • <a href="README.ko.md">🇰🇷 한국어</a></p>

---

<a id="introduction"></a>
## Introducción

El proyecto está estandarizado de acuerdo con estructuras de proyectos profesionales, lo que permite una gestión eficiente del código fuente a través de Git.

<a id="features"></a>
## Características Clave

- Configuración rápida y empaquetado profesional.
- Configuración ligera, fácil de mantener y extender.
- Flujo de trabajo de envío automático a Git mediante el script incluido.

---

## Estructura de Directorios

```text
LVI_LX_LOG_DOWNLOAD_EVRT/
├── main.py                    # Punto de entrada de la aplicación
├── run.bat                    # Script de inicio rápido para Windows
├── requirements.txt           # Lista de dependencias
├── config.ini                 # Archivo de configuración simple
├── config.json                # Archivo de configuración JSON estructurado
├── .gitignore                 # Patrones para ignorar en Git
├── README.md                  # Documentación del proyecto (este archivo)
├── LICENSE                    # Archivo de licencia
├── ABOUT.txt                  # Breve descripción del proyecto
├── git_push.bat               # Script de envío automático a GitHub
│
├── logs/                      # Archivos de registro de la aplicación
│
├── modules/                   # Módulos principales con la lógica de negocio
│   ├── ui.py                  # Giao diện người dùng
│   ├── logic.py               # Logic nghiệp vụ chính
│   ├── utils.py               # Các hàm tiện ích dùng chung
│   ├── constants.py           # Hằng số cấu hình
│   └── logger_config.py       # Cấu hình logging
│
└── assets/                    # Recursos estáticos de la aplicación
```

---

<a id="setup"></a>
## Guía de Instalación y Uso

### Requisitos del Sistema
*   Sistema Operativo: **Windows 10/11**
*   Intérprete: **Python 3.13** o entorno equivalente.

<a id="quick-start"></a>
### Cómo Ejecutar
1. Instalar dependencias necesarias:
   ```cmd
   pip install -r requirements.txt
   ```
2. Ejecutar la aplicación:
   ```cmd
   run.bat
   ```

---

## Licencia

Este proyecto está bajo la **Licencia MIT**. Ver el archivo [LICENSE](LICENSE) para más detalles.
