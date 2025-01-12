#!/bin/bash

# Afficher un message
echo "Activation de l'environnement virtuel 'shovel_insee'..."

# Activer l'environnement virtuel
# Assurez-vous que le chemin vers l'environnement virtuel est correct
source shovel_insee/bin/activate  # Utilisez activate pour bash

echo "Environnement virtuel activé."

# Exécuter start.py
echo "Exécution de start.py..."
# Changer de répertoire pour le dossier scripts
cd scripts
python start.py
# Revenir au répertoire original
cd ..

echo "start.py a terminé son exécution."
exit
