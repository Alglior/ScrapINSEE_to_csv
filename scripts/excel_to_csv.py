import os
import pandas as pd

# Obtenir le chemin du dossier principal du projet (un niveau au-dessus de scripts)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Définir les chemins complets pour les dossiers excel et csv
excel_directory = os.path.join(PROJECT_DIR, "tableaux_excel")
csv_directory = os.path.join(PROJECT_DIR, "tableaux_csv")

# Créer le dossier des fichiers CSV s'il n'existe pas
if not os.path.exists(csv_directory):
    os.makedirs(csv_directory)

# Parcourir la structure des dossiers dans le dossier Excel
for root, dirs, files in os.walk(excel_directory):
    for file in files:
        if file.endswith(".xlsx"):
            excel_file_path = os.path.join(root, file)
            # Calculer le chemin relatif par rapport au dossier excel
            csv_relative_path = os.path.relpath(excel_file_path, excel_directory)
            csv_file_path = os.path.join(csv_directory, os.path.splitext(csv_relative_path)[0] + ".csv")
            
            # Créer les sous-dossiers nécessaires dans le dossier csv
            csv_file_folder = os.path.dirname(csv_file_path)
            if not os.path.exists(csv_file_folder):
                os.makedirs(csv_file_folder)
            
            # Lire le fichier Excel et le convertir en CSV
            df = pd.read_excel(excel_file_path)
            df.columns = ['_'.join(map(str, col)).strip().replace('U_n_n_a_m_e_d_:_ _0', '').replace(' ', '_') for col in df.columns.values]
            df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

print("Les fichiers Excel ont été convertis en fichiers CSV tout en conservant la structure des dossiers.")