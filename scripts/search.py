import os
import shutil

def find_files(directory, filename):
    matches = []

    for root, dirnames, filenames in os.walk(directory):
        for fname in filenames:
            if filename in fname:
                matches.append(os.path.join(root, fname))

    return matches

# Utilisation de la fonction
directory = '../tableaux_csv'  # Remplacez par le chemin du dossier à parcourir
filename = "_tableauACT T2 - Statut et condition d'emploi des 1...csv"
matches = find_files(directory, filename)

# Création du dossier "results" s'il n'existe pas
if not os.path.exists('../results'):
    os.makedirs('../results')

# Extract directory name from filename
dir_name = filename.split('-')[0].strip()

# Create new directory in results
new_dir_path = os.path.join('../results', dir_name)
if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

# Copie des fichiers trouvés dans le nouveau dossier
for match in matches:
    shutil.copy(match, new_dir_path)