import os
import logging
import threading
import subprocess
from datetime import datetime, timedelta
import darkdetect
from PySide6.QtCore import Qt, Signal, Slot, QDateTime, QDate, QTime
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,
    QProgressBar, QLineEdit, QDateTimeEdit, QFileDialog
)
from PySide6.QtGui import QFont, QColor, QGuiApplication, QIcon
from BlurWindow.blurWindow import GlobalBlur

import modules.logic as logic
from modules.constants import *

logger = logging.getLogger(__name__)

DEFAULT_DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads", "EVRT_logs")

class LogDownloaderApp(QWidget):
    log_signal = Signal(str)
    finished_signal = Signal(int)

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.is_dark = darkdetect.isDark()
        self.current_status = "ALL"
        
        self.is_running = False
        self.stop_requested = False
        self.current_action = ""
        self.current_download_dir = ""
        
        self.setup_window()
        self.setup_ui()
        self.apply_theme()
        
        self.log_signal.connect(self.update_log_table)
        self.finished_signal.connect(self.on_finished)
        
        # Connect text change to enable/disable buttons
        self.sn_input.textChanged.connect(self.check_input_fields)
        self.check_input_fields() # Initial check
        
        app = QGuiApplication.instance()
        if app:
            app.styleHints().colorSchemeChanged.connect(self.on_os_theme_changed)

    def on_os_theme_changed(self, scheme):
        is_os_dark = (scheme == Qt.ColorScheme.Dark)
        if self.is_dark != is_os_dark:
            self.is_dark = is_os_dark
            self.apply_theme()
            self.theme_btn.setText("💡 Dark" if self.is_dark else "🌙 Light")
            GlobalBlur(self.winId(), Dark=self.is_dark, QWidget=self)

    def setup_window(self):
        self.setWindowTitle(APP_NAME)
        self.resize(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        
        # Set Icon (from assets/images/icon.ico)
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "images", "icon.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowSystemMenuHint)
        GlobalBlur(self.winId(), Dark=self.is_dark, QWidget=self)
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None
        
    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.apply_theme()
        self.theme_btn.setText("💡 Dark" if self.is_dark else "🌙 Light")
        GlobalBlur(self.winId(), Dark=self.is_dark, QWidget=self)

    def _on_status_change(self, val):
        self.current_status = val
        for btn in self.status_btns:
            btn.setProperty("active", "true" if btn.text() == val else "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)

    def apply_theme(self):
        bg = "rgba(0, 0, 0, 0.6)" if self.is_dark else "rgba(255, 255, 255, 0.6)"
        text_color = "white" if self.is_dark else "black"
        border_color = "rgba(255, 255, 255, 0.2)" if self.is_dark else "rgba(0, 0, 0, 0.2)"
        input_bg = "rgba(128,128,128,0.3)" if self.is_dark else "rgba(255,255,255,0.7)"
        
        qss = f"""
            QWidget#CentralWidget {{
                background-color: {bg};
                border: 1px solid {border_color};
                border-radius: 20px;
            }}
            QLabel {{ color: {text_color}; font-family: '{FONT_PRIMARY}'; font-size: 14px; font-weight: 500; }}
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 {COLOR_PRIMARY_START}, stop:1 {COLOR_PRIMARY_END});
                color: white; border-radius: 8px; padding: 6px 12px; font-weight: bold;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 {COLOR_PRIMARY_START_HOVER}, stop:1 {COLOR_PRIMARY_END_HOVER});
            }}
            QPushButton:disabled {{ background: gray; }}
            
            QPushButton#CloseBtn {{ background-color: {COLOR_CLOSE_NORMAL}; border: 1px solid {COLOR_CLOSE_BORDER}; border-radius: 8px; padding: 0; }}
            QPushButton#CloseBtn:hover {{ background-color: {COLOR_CLOSE_HOVER}; }}
            QPushButton#MinBtn {{ background-color: {COLOR_MIN_NORMAL}; border: 1px solid {COLOR_MIN_BORDER}; border-radius: 8px; padding: 0; }}
            QPushButton#MinBtn:hover {{ background-color: {COLOR_MIN_HOVER}; }}
            QPushButton#MaxBtn {{ background-color: {COLOR_MAX_NORMAL}; border: 1px solid {COLOR_MAX_BORDER}; border-radius: 8px; padding: 0; }}
            QPushButton#MaxBtn:hover {{ background-color: {COLOR_MAX_HOVER}; }}
            
            QPushButton#ThemeBtn {{
                background: {input_bg}; border: 1px solid {border_color}; color: {text_color}; font-weight: normal;
            }}
            
            QPushButton#SegBtn {{
                background: {input_bg}; border: 1px solid {border_color}; border-radius: 6px; color: {text_color}; font-weight: normal; padding: 4px 12px;
            }}
            QPushButton#SegBtn[active="true"] {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 {COLOR_PRIMARY_START}, stop:1 {COLOR_PRIMARY_END});
                color: white; font-weight: bold; border: none;
            }}
            QPushButton#StopMode {{
                background: {COLOR_CLOSE_NORMAL};
                color: white;
            }}
            QPushButton#SegBtn:hover {{
                background: rgba(128,128,128,0.5);
            }}
            QPushButton#SegBtn[active="true"]:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 {COLOR_PRIMARY_START_HOVER}, stop:1 {COLOR_PRIMARY_END_HOVER});
            }}
            
            QTableWidget {{
                background: transparent; color: {text_color}; gridline-color: {border_color};
                border: 1px solid {border_color}; border-radius: 8px;
            }}
            QHeaderView::section {{
                background-color: rgba(0, 0, 0, 0.2); color: {text_color}; padding: 4px; border: none; font-weight: bold;
            }}
            QLineEdit, QDateTimeEdit {{
                background: {input_bg}; color: {text_color}; 
                border: 1px solid {border_color}; border-radius: 5px; padding: 5px; font-family: '{FONT_MONO}', monospace;
            }}
        """
        self.setStyleSheet(qss)

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        
        self.central_widget = QWidget()
        self.central_widget.setObjectName("CentralWidget")
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        layout.addWidget(self.central_widget)

        # Header 3 buttons
        header = QHBoxLayout()
        self.close_btn = QPushButton("")
        self.close_btn.setObjectName("CloseBtn")
        self.close_btn.setFixedSize(16, 16)
        self.close_btn.clicked.connect(self.close)

        self.min_btn = QPushButton("")
        self.min_btn.setObjectName("MinBtn")
        self.min_btn.setFixedSize(16, 16)
        self.min_btn.clicked.connect(self.showMinimized)

        self.max_btn = QPushButton("") 
        self.max_btn.setObjectName("MaxBtn")
        self.max_btn.setFixedSize(16, 16)
        self.max_btn.clicked.connect(self.toggle_maximize)

        header.addWidget(self.close_btn)
        header.addSpacing(4)
        header.addWidget(self.min_btn)
        header.addSpacing(4)
        header.addWidget(self.max_btn)
        header.addSpacing(15)
        
        title = QLabel(APP_TITLE)
        title.setFont(QFont(FONT_PRIMARY, 16, QFont.Bold))
        title.setStyleSheet(f"color: {COLOR_PRIMARY_START};")
        header.addWidget(title)
        header.addStretch()
        
        # Theme button
        self.theme_btn = QPushButton("💡 Dark" if self.is_dark else "🌙 Light")
        self.theme_btn.setObjectName("ThemeBtn")
        self.theme_btn.setFixedSize(100, 32)
        self.theme_btn.clicked.connect(self.toggle_theme)
        header.addWidget(self.theme_btn)
        
        self.main_layout.addLayout(header)

        # Filters Layout - Row 1
        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Types:"))
        self.sn_input = QLineEdit("QB95R1|QB95R2")
        self.sn_input.setPlaceholderText("e.g. QB95R1|QB95R2")
        row1.addWidget(self.sn_input)
        
        row1.addSpacing(20)
        row1.addWidget(QLabel("Status:"))
        self.status_btns = []
        for s in ["ALL", "PASS", "FAIL"]:
            btn = QPushButton(s)
            btn.setObjectName("SegBtn")
            btn.setCheckable(True)
            btn.setFixedSize(60, 30)
            btn.setProperty("active", "true" if s == self.current_status else "false")
            btn.clicked.connect(lambda *args, val=s: self._on_status_change(val))
            row1.addWidget(btn)
            self.status_btns.append(btn)
            
        row1.addStretch()
        self.main_layout.addLayout(row1)

        # Filters Layout - Row 1.5 (Link Filter)
        row1_5 = QHBoxLayout()
        row1_5.addWidget(QLabel("Link Filter:"))
        self.link_filter_input = QLineEdit()
        self.link_filter_input.setPlaceholderText("e.g. *JCI*MMI* or /JCI/LVI/IQ5/MMI")
        row1_5.addWidget(self.link_filter_input)
        self.main_layout.addLayout(row1_5)

        # Filters Layout - Row 1.7 (Save Dir)
        row1_7 = QHBoxLayout()
        row1_7.addWidget(QLabel("Save Dir:"))
        self.save_dir_input = QLineEdit()
        self.save_dir_input.setPlaceholderText(self.get_default_download_dir())
        row1_7.addWidget(self.save_dir_input)
        
        self.browse_btn = QPushButton("Browse")
        self.browse_btn.setFixedWidth(80)
        self.browse_btn.setObjectName("ThemeBtn")
        self.browse_btn.clicked.connect(self.browse_save_dir)
        row1_7.addWidget(self.browse_btn)
        self.main_layout.addLayout(row1_7)

        # Filters Layout - Row 2
        now = datetime.now()
        default_end = QDateTime(QDate(now.year, now.month, now.day), QTime(7, 0))
        default_start = default_end.addDays(-1)
        
        row2 = QHBoxLayout()
        row2.addWidget(QLabel("From:"))
        self.start_dt = QDateTimeEdit(default_start)
        self.start_dt.setDisplayFormat(DATETIME_FORMAT_UI)
        self.start_dt.setCalendarPopup(True)
        row2.addWidget(self.start_dt)
        
        row2.addSpacing(10)
        row2.addWidget(QLabel("To:"))
        self.end_dt = QDateTimeEdit(default_end)
        self.end_dt.setDisplayFormat(DATETIME_FORMAT_UI)
        self.end_dt.setCalendarPopup(True)
        row2.addWidget(self.end_dt)
        
        row2.addStretch()
        self.scan_btn = QPushButton("SCAN")
        self.scan_btn.setFixedWidth(100)
        self.scan_btn.setObjectName("SegBtn")
        self.scan_btn.clicked.connect(self.start_scan)
        row2.addWidget(self.scan_btn)
        
        row2.addSpacing(10)
        
        self.start_btn = QPushButton("FAST DOWNLOAD")
        self.start_btn.setFixedWidth(140)
        self.start_btn.clicked.connect(self.start_download)
        row2.addWidget(self.start_btn)
        
        self.main_layout.addLayout(row2)

        # Table
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Time", "Status/Filename"])
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.setSortingEnabled(True) # Cho phép sắp xếp khi click vào Header
        self.main_layout.addWidget(self.table)

        # Progress
        self.progress = QProgressBar()
        self.progress.setStyleSheet("QProgressBar::chunk { background-color: #00d4ff; border-radius: 4px; }")
        self.progress.setFixedHeight(8)
        self.progress.setTextVisible(False)
        self.main_layout.addWidget(self.progress)

    def check_input_fields(self):
        # Nếu đang chạy thì không xét ở đây (sẽ xét lúc finish)
        if self.is_running:
            return
            
        has_text = bool(self.sn_input.text().strip())
        self.scan_btn.setEnabled(has_text)
        self.start_btn.setEnabled(has_text)

    def start_scan(self):
        if self.is_running and self.current_action == "SCAN":
            self.stop_requested = True
            self.log_signal.emit("Stopping Scan...")
            return
            
        self.current_action = "SCAN"
        self._prepare_and_start_worker(scan_only=True)

    def start_download(self):
        if self.is_running and self.current_action == "DOWNLOAD":
            self.stop_requested = True
            self.log_signal.emit("Stopping Download...")
            return
            
        self.current_action = "DOWNLOAD"
        self._prepare_and_start_worker(scan_only=False)

    def _prepare_and_start_worker(self, scan_only):
        self.is_running = True
        self.stop_requested = False
        
        if self.current_action == "SCAN":
            self.scan_btn.setText("STOP")
            self.scan_btn.setObjectName("StopMode")
            self.start_btn.setEnabled(False)
        else:
            self.start_btn.setText("STOP")
            self.start_btn.setObjectName("StopMode")
            self.scan_btn.setEnabled(False)
            
        # Nạp lại QSS cho nút STOP
        self.scan_btn.style().unpolish(self.scan_btn)
        self.scan_btn.style().polish(self.scan_btn)
        self.start_btn.style().unpolish(self.start_btn)
        self.start_btn.style().polish(self.start_btn)

        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        self.progress.setRange(0, 0)
        
        types = [x.strip() for x in self.sn_input.text().split('|') if x.strip()]
        link_filter = self.link_filter_input.text().strip()
        download_dir = self.save_dir_input.text().strip()
        if not download_dir:
            download_dir = self.get_default_download_dir()
        download_dir = os.path.abspath(os.path.expandvars(os.path.expanduser(download_dir)))
        self.current_download_dir = download_dir
            
        start_str = self.start_dt.dateTime().toString(DATETIME_FORMAT_UI)
        end_str = self.end_dt.dateTime().toString(DATETIME_FORMAT_UI)
        status_filter = self.current_status
        
        thread = threading.Thread(target=self._worker, args=(types, link_filter, download_dir, start_str, end_str, status_filter, scan_only), daemon=True)
        thread.start()

    def _worker(self, types, link_filter, download_dir, start_str, end_str, status_filter, scan_only):
        try:
            results = logic.download_logs_logic(
                self.config['EVERYTHING']['host'],
                self.config['EVERYTHING']['port'],
                self.config['EVERYTHING']['user'],
                self.config['EVERYTHING']['pass'],
                types, link_filter, start_str, end_str, status_filter,
                download_dir,
                progress_callback=lambda m: self.log_signal.emit(str(m)),
                scan_only=scan_only,
                stop_check=lambda: self.stop_requested
            )
            self.finished_signal.emit(len(results))
        except Exception as e:
            self.log_signal.emit(f"ERROR: {str(e)}")
            self.finished_signal.emit(-1)

    @Slot(str)
    def update_log_table(self, message):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(datetime.now().strftime(TIME_FORMAT_LOGS)))
        self.table.setItem(row, 1, QTableWidgetItem(message))
        self.table.scrollToBottom()

    @Slot(int)
    def on_finished(self, count):
        self.is_running = False
        
        # Trả lại tên và giao diện ban đầu
        self.scan_btn.setText("SCAN")
        self.scan_btn.setObjectName("SegBtn")
        self.start_btn.setText("FAST DOWNLOAD")
        self.start_btn.setObjectName("")
        
        self.scan_btn.style().unpolish(self.scan_btn)
        self.scan_btn.style().polish(self.scan_btn)
        self.start_btn.style().unpolish(self.start_btn)
        self.start_btn.style().polish(self.start_btn)
        
        self.check_input_fields() # Kiểm tra lại xem ô SN có rỗng không để Disable/Enable
        
        self.table.setSortingEnabled(True)
        self.progress.setRange(0, 100)
        self.progress.setValue(100)
        
        status_msg = "Cancelled" if self.stop_requested else "Finished"
        msg = f"{self.current_action} {status_msg}. Total: {count} files." if count >= 0 else f"{self.current_action} Failed."
        self.update_log_table(msg)
        
        if self.current_action == "DOWNLOAD" and count >= 0 and not self.stop_requested:
            self.open_download_folder()

    def browse_save_dir(self):
        default_dir = self.get_default_download_dir()
        selected_dir = QFileDialog.getExistingDirectory(self, "Select Download Directory", default_dir)
        if selected_dir:
            self.save_dir_input.setText(selected_dir)

    def get_default_download_dir(self):
        configured_dir = self.config.get('DEFAULT', 'download_dir', fallback='', raw=True).strip()
        if configured_dir:
            return os.path.abspath(os.path.expandvars(os.path.expanduser(configured_dir)))
        return DEFAULT_DOWNLOAD_DIR

    def open_download_folder(self):
        if not self.current_download_dir:
            return
        try:
            os.makedirs(self.current_download_dir, exist_ok=True)
            if os.name == "nt":
                os.startfile(self.current_download_dir)
            else:
                subprocess.Popen(["xdg-open", self.current_download_dir])
        except Exception as e:
            logger.error(f"Error opening download folder: {e}")
            self.update_log_table(f"ERROR opening folder: {e}")
