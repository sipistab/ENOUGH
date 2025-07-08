@echo off
SETLOCAL

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is required but not installed. Please install Python first.
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is required but not installed. Please install pip first.
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install requirements
echo Installing dependencies...
pip install -r Core\requirements.txt

REM Install package in development mode
echo Installing sentence-completion...
pip install -e .

echo Installation complete! You can now use 'sentence-completion' command.
pause 