import os
import shutil
import re
import subprocess
import sys

def run_combine_for_folder(folder_path, combine_script_path):
    try:
        # Exécuter combine.py avec le chemin complet du dossier
        subprocess.run([
            sys.executable,
            combine_script_path,
            folder_path  # Passer le chemin complet du dossier
        ], check=True)
        print(f"Fichiers combinés pour {os.path.basename(folder_path)}")
        
    except Exception as e:
        print(f"Erreur lors de la combinaison des fichiers pour {folder_path}: {str(e)}")

def find_and_sort_tables(directory):
    # Obtenir le chemin du dossier principal du projet (2 niveaux au-dessus du script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    
    # Création du dossier results dans le dossier principal du projet
    results_dir = os.path.join(project_dir, 'results')
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        print(f"Dossier results créé dans : {results_dir}")

    # Dictionnaire pour stocker les fichiers par type de tableau
    table_files = {}
    
    # Pattern pour extraire le type de tableau (ex: "tableauACT G2")
    pattern = r'tableau[A-Z]+ [A-Z][0-9]'

    # Parcourir tous les fichiers
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.csv'):
                # Chercher le motif dans le nom du fichier
                match = re.search(pattern, filename)
                if match:
                    table_type = match.group(0)  # Ex: "tableauACT G2"
                    if table_type not in table_files:
                        table_files[table_type] = []
                    table_files[table_type].append(os.path.join(root, filename))

    # Copier les fichiers dans leurs dossiers respectifs
    for table_type, files in table_files.items():
        # Créer un sous-dossier pour ce type de tableau dans results
        type_dir = os.path.join(results_dir, table_type.replace(" ", "_"))
        if not os.path.exists(type_dir):
            os.makedirs(type_dir)
        
        # Copier tous les fichiers de ce type
        for file_path in files:
            shutil.copy(file_path, type_dir)
        print(f"Copié {len(files)} fichiers dans {type_dir}")

    # Après avoir copié tous les fichiers, lancer combine.py pour chaque dossier
    combine_script_path = os.path.join(script_dir, 'combine.py')
    
    if os.path.exists(combine_script_path):
        print("\nCombining files in each result folder...")
        for table_type, files in table_files.items():
            type_dir = os.path.join(results_dir, table_type.replace(" ", "_"))
            run_combine_for_folder(type_dir, combine_script_path)
    else:
        print(f"Warning: combine.py not found at {combine_script_path}")

if __name__ == "__main__":
    # Utiliser le chemin absolu pour le dossier tableaux_csv
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    csv_dir = os.path.join(project_dir, 'tableaux_csv')
    
    if not os.path.exists(csv_dir):
        print(f"Erreur: Le dossier {csv_dir} n'existe pas!")
        print("Vérification des chemins:")
        print(f"- Dossier script: {script_dir}")
        print(f"- Dossier projet: {project_dir}")
        print(f"- Dossier CSV recherché: {csv_dir}")
    else:
        find_and_sort_tables(csv_dir)
        print("Tri des tables terminé !")