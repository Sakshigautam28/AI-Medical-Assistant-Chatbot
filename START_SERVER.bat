@echo off
REM Start Sentinel Alpha Backend Server Automatically
REM This file starts the Python server in the background

cd /d "%~dp0"
echo Starting Sentinel Alpha Server...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from python.org
    pause
    exit /b 1
)

REM Start the server
echo Starting: python ai_service.py
python ai_service.py

REM Keep window open if there's an error
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Server failed to start
    pause
)
