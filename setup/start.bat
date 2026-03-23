@echo off
:: Activates the Python virtual environment (if present) and starts starter.py.

set ROBUS_CORE=%~dp0..
for %%I in ("%ROBUS_CORE%") do set PARENT=%%~dpI

if exist "%ROBUS_CORE%\venv\Scripts\activate.bat" (
    echo Activating venv: %ROBUS_CORE%\venv
    call "%ROBUS_CORE%\venv\Scripts\activate.bat"
) else if exist "%ROBUS_CORE%\env\Scripts\activate.bat" (
    echo Activating venv: %ROBUS_CORE%\env
    call "%ROBUS_CORE%\env\Scripts\activate.bat"
) else if exist "%PARENT%\venv\Scripts\activate.bat" (
    echo Activating venv: %PARENT%\venv
    call "%PARENT%\venv\Scripts\activate.bat"
) else if exist "%PARENT%\env\Scripts\activate.bat" (
    echo Activating venv: %PARENT%\env
    call "%PARENT%\env\Scripts\activate.bat"
) else (
    echo No virtual environment found in:
    echo   %ROBUS_CORE%\venv
    echo   %ROBUS_CORE%\env
    echo   %PARENT%\venv
    echo   %PARENT%\env
    echo Using system Python.
)

python "%ROBUS_CORE%\utils\starter.py"
