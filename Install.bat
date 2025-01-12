@echo off
echo Installation de Python 3.10...

REM Télécharger Python 3.10
curl -o python-3.10.0.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

REM Installer Python silencieusement avec les options nécessaires
python-3.10.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

REM Attendre que l'installation soit terminée
timeout /t 10

REM Supprimer l'installateur
del python-3.10.0.exe

echo Python 3.10 installé avec succès.

REM Aller dans le dossier scripts et exécuter requirements.py
echo Configuration de l'environnement...
cd scripts
python requirements.py
cd ..

echo Installation terminée avec succès!
pause
