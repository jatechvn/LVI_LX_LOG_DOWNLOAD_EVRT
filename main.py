import sys
import os
import ctypes
import configparser

# ================================================================================
# 💡 WINDOWS TASKBAR ICON CONFIGURATION (AppUserModelID)
# ================================================================================
# Buộc Windows nhận diện đây là một ứng dụng độc lập độc nhất trên Taskbar
# thay vì nhóm nó dưới tiến trình chung "python.exe" của Python.
myappid = 'JA.LogDownloader.EVRT.1.0'
try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.logger_config import setup_logger
from modules.ui import LogDownloaderApp
from modules.constants import APP_NAME

def main():
    logger = setup_logger()
    logger.info(f"{APP_NAME} starting...")

    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    config.read(config_path)

    app = QApplication(sys.argv)
    
    # Thiết lập Window Icon toàn cục cho ứng dụng từ assets/images
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "images", "icon.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    else:
        logger.warning(f"Icon not found at: {icon_path}")

    window = LogDownloaderApp(config)
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
