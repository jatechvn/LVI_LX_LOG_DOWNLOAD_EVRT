# 🤖 LVI_LX_LOG_DOWNLOAD_EVRT

<p align="center">
  <br>
  <i>**LVI_LX_LOG_DOWNLOAD_EVRT** là một ứng dụng được phát triển bằng ngôn ngữ Python.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License">
</p>

<p align="center"><a href="#quick-start">🚀 Quick Start</a> • <a href="#features">💡 Features</a> • <a href="#setup">📖 Setup</a> • <a href="https://jatechvn.github.io/">🌐 Website</a></p>

<p align="center"><a href="../README.md">🇺🇸 English</a> • 🇻🇳 Tiếng Việt • <a href="README.zh-CN.md">🇨🇳 中文</a> • <a href="README.ja-JP.md">🇯🇵 日本語</a> • <a href="README.es.md">🇪🇸 Español</a> • <a href="README.fr.md">🇫🇷 Français</a> • <a href="README.de.md">🇩🇪 Deutsch</a> • <a href="README.ru.md">🇷🇺 Русский</a> • <a href="README.pt.md">🇵🇹 Português</a> • <a href="README.ko.md">🇰🇷 한국어</a></p>

---

<a id="introduction"></a>
## Giới Thiệu Chung

Dự án được thiết lập chuẩn hóa theo khung dự án phát triển chuyên nghiệp, hỗ trợ quản lý mã nguồn hiệu quả qua Git.

<a id="features"></a>
## Tính Năng Nổi Bật

- Khởi tạo nhanh chóng và đóng gói chuyên nghiệp.
- Cấu hình tinh gọn, dễ bảo trì và phát triển mở rộng.
- Tự động hóa quy trình đẩy code lên Git thông qua script đi kèm.

---

## Cấu Trúc Mã Nguồn

```text
LVI_LX_LOG_DOWNLOAD_EVRT/
├── main.py                    # Điểm vào chương trình (entry point)
├── run.bat                    # Script khởi động nhanh trên Windows
├── requirements.txt           # Danh sách thư viện cần thiết
├── config.ini                 # File cấu hình đơn giản
├── config.json                # File cấu hình dạng JSON
├── .gitignore                 # Các tệp bỏ qua khi commit
├── README.md                  # Tài liệu giới thiệu dự án (File này)
├── LICENSE                    # Giấy phép sử dụng
├── ABOUT.txt                  # Tài liệu mô tả ngắn về dự án
├── git_push.bat               # Script đẩy code tự động lên GitHub
│
├── logs/                      # Nhật ký hoạt động của ứng dụng
│
├── modules/                   # Các module xử lý chính
│   ├── ui.py                  # Giao diện người dùng
│   ├── logic.py               # Logic nghiệp vụ chính
│   ├── utils.py               # Các hàm tiện ích dùng chung
│   ├── constants.py           # Hằng số cấu hình
│   └── logger_config.py       # Cấu hình logging
│
└── assets/                    # Tài nguyên tĩnh của ứng dụng
```

---

<a id="setup"></a>
## Hướng Dẫn Cài Đặt & Sử Dụng

### Điều kiện cấu hình hệ thống
*   Hệ điều hành: **Windows 10/11**
*   Trình thông dịch: **Python 3.13** hoặc môi trường phù hợp.

<a id="quick-start"></a>
### Khởi động ứng dụng
1. Cài đặt các thư viện cần thiết:
   ```cmd
   pip install -r requirements.txt
   ```
2. Khởi chạy ứng dụng:
   ```cmd
   run.bat
   ```

---

## Giấy Phép Sử Dụng

Dự án này được cấp phép theo các điều khoản của **MIT License**. Chi tiết xem tại tệp [LICENSE](LICENSE).
