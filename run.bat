@echo off
REM Gunny - Quick Start Script for Windows

echo 🎯 Starting Gunny - CrewAI Project Generator
echo.

REM Check if UV is installed (preferred method)
where uv >nul 2>&1
if %errorlevel% equ 0 (
    echo ✨ Using UV (faster dependency management)
    echo 🚀 Launching Gunny...
    echo.
    uv run streamlit run app.py
    pause
    exit /b 0
)

REM Fallback to traditional Python/pip method
echo 💡 Tip: Install UV for faster dependency management: https://docs.astral.sh/uv/
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.10 or higher.
    pause
    exit /b 1
)

REM Check if Streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing dependencies...
    pip install -r requirements.txt
)

REM Run the app
echo 🚀 Launching Gunny...
echo.
streamlit run app.py

pause
