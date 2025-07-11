@echo off

REM Check Python version
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is required but not found. Please install Python and try again.
    exit /b 1
)

python -c "import sys; assert sys.version_info >= (3, 8), 'Python 3.8+ required'" >nul 2>&1
if errorlevel 1 (
    echo Python 3.8 or higher is required.
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install package in development mode
echo Installing ENOUGH...
pip install -e .

REM Create default directories
mkdir templates\nathaniel_branden_method 2>nul
mkdir templates\custom 2>nul
mkdir templates\starting_strength 2>nul
mkdir submissions\nathaniel_branden_method 2>nul
mkdir submissions\custom 2>nul
mkdir submissions\starting_strength 2>nul
mkdir main\progress 2>nul

echo Installation complete!
echo Run 'enough start' to begin. 