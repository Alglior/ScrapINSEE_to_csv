@echo off
echo Activating the virtual environment "shovel_insee"...

REM Change the path below if the virtual environment is located elsewhere
call scripts/shovel_insee\activate.bat  # Use activate.bat for cmd.exe

echo Virtual environment activated.

echo Running start.py...
REM Change directory to the scripts folder
cd scripts
python start.py
REM Change back to the original directory
cd ..

echo start.py has finished running.
exit
