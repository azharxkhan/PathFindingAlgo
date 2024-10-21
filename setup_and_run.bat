@echo off

where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Download and install Python from https://www.python.org/downloads/
    pause
    exit /b
) else (
    echo Python is already installed.
)

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing pygame...
pip install pygame

echo Running the Python program...
python runprogram.py  

deactivate
