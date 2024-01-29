#!/bin/bash

# Afficher un message
echo "Téléchargement de l'installateur Python 3.10..."
# Télécharger l'installateur Python
wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz

# Afficher un message
echo "Installation de Python 3.10..."
# Extraire l'archive
tar -xzf Python-3.10.0.tgz
cd Python-3.10.0

# Configurer et installer Python
./configure
make
sudo make install

# Revenir au répertoire précédent
cd ..

# Supprimer l'archive téléchargée
rm Python-3.10.0.tgz

echo "Python 3.10 installé avec succès."

# Exécuter requirements.py
echo "Exécution de requirements.py..."
# Changer de répertoire pour le dossier scripts
cd scripts
python requirements.py
# Revenir au répertoire original
cd ..

echo "requirements.py a terminé son exécution."