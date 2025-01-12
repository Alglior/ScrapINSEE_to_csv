#!/bin/bash

# Installation des dépendances système nécessaires
echo "Installation des dépendances système nécessaires..."
sudo apt-get update
sudo apt-get install -y \
    python3-tk \
    python3-dev \
    tk-dev \
    python3-venv \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libsqlite3-dev \
    wget \
    libbz2-dev

# Télécharger et installer Python 3.10
echo "Téléchargement de l'installateur Python 3.10..."
wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz
tar -xzf Python-3.10.0.tgz
cd Python-3.10.0

# Configurer avec tkinter activé
./configure --enable-optimizations --with-tcltk-includes="-I/usr/include" --with-tcltk-libs="-L/usr/lib"
make -j $(nproc)
sudo make altinstall

# Revenir au répertoire précédent et nettoyer
cd ..
rm Python-3.10.0.tgz
rm -rf Python-3.10.0

echo "Python 3.10 installé avec succès."

# Configuration de l'environnement
echo "Configuration de l'environnement..."
cd scripts
python3.10 requirements.py

echo "Installation terminée avec succès!"