@echo off
setlocal

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.8 or later.
    exit /b 1
)

:: Check Python version
for /f "tokens=2" %%I in ('python --version 2^>^&1') do set PYTHON_VERSION=%%I
for /f "tokens=1 delims=." %%I in ("%PYTHON_VERSION%") do set PYTHON_MAJOR=%%I
for /f "tokens=2 delims=." %%I in ("%PYTHON_VERSION%") do set PYTHON_MINOR=%%I

if %PYTHON_MAJOR% LSS 3 (
    echo Python 3.8 or later is required.
    exit /b 1
)
if %PYTHON_MAJOR%==3 (
    if %PYTHON_MINOR% LSS 8 (
        echo Python 3.8 or later is required.
        exit /b 1
    )
)

:: Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not installed. Please install pip.
    exit /b 1
)

echo Installing ENOUGH...

:: Install the package in development mode
pip install -e .

echo Installation complete! You can now use 'enough' command.
pause 
pause 