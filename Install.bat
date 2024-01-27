@echo off
echo Downloading Python 3.10 Installer...
curl -o python-3.10.0.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

echo Installing Python 3.10...
python-3.10.0.exe /quiet InstallAllUsers=1 PrependPath=1

echo Python 3.10 installed successfully.

echo Running requirements.py...
REM Change directory to the scripts folder
cd scripts
python requirements.py
REM Change back to the original directory
cd ..

echo requirements.py has finished running.
pause
