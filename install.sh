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
rm -rf Python-3.10.0

echo "Python 3.10 installé avec succès."

# Aller dans le dossier scripts et exécuter requirements.py
echo "Configuration de l'environnement..."
cd scripts
python3 requirements.py

echo "Installation terminée avec succès!"