@echo off
setlocal enabledelayedexpansion

:: --- AN CMD XUONG TASKBAR ---
if not "%1"=="min" (
    start /min cmd /c "%~f0" min
    exit /b
)

:: --- TU DONG LAY TEN THU MUC LAM TEN PROJECT ---
for %%I in ("%~dp0.") do set "PROJ_NAME=%%~nxI"
title !PROJ_NAME! - Johnny's Automation Suite 📸🦞

:: --- CAU HINH GIAO DIEN ---
mode con: cols=85 lines=25
color 0B

echo.
echo  #############################################################################
echo  #                                                                           #
echo  #                 JOHNNY'S PROFESSIONAL DEPLOYMENT SYSTEM                   #
echo  #                                                                           #
echo  #  PROJECT: !PROJ_NAME!
echo  #                                                                           #
echo  #############################################################################
echo.
echo  [*] Thoi gian: %date% %time%
echo  [*] Thu muc: %~dp0
echo  [*] Moi truong: Python Virtual Environment (.venv)
echo.
echo  -----------------------------------------------------------------------------
echo  [ LOADING ] Dang kiem tra thanh phan cua [!PROJ_NAME!]...

:: --- KIEM tự động ---
set "MISSING_FILES="
if not exist "%~dp0main.py" set "MISSING_FILES=!MISSING_FILES! [main.py]"

if "!MISSING_FILES!" neq "" (
    color 0C
    echo.
    echo  [!] LOI: Khong tim thay file khoi chay !MISSING_FILES!
    echo  [?] Vui long dam bao ban dang dat run.bat trong thu muc goc cua project.
    echo  -----------------------------------------------------------------------------
    pause
    exit /b
)

echo  [  OK  ] Moi thu da san sang de khoi dong.
echo  -----------------------------------------------------------------------------
echo.
echo  [^] Dang khoi chay [!PROJ_NAME!]...
echo.

:: --- KHOI CHAY PYTHON QUA .VENV ---
"%~dp0.venv\Scripts\python.exe" "%~dp0main.py"

if %errorlevel% neq 0 (
    color 0C
    echo.
    echo  [!] !PROJ_NAME! DA DUNG DOT NGOT (Exit Code: %errorlevel%)
    echo  [*] Vui long kiem tra log hoac moi truong Python.
    echo.
    timeout /t 1 >nul
    exit
) else (
    echo.
    echo  [ SUCCESS ] !PROJ_NAME! da hoan tat nhiem vu.
    echo.
    timeout /t 5 >nul
)

