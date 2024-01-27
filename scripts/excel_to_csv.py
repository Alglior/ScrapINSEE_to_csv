import os
import pandas as pd

# Dossier contenant les fichiers Excel
excel_directory = "../tableaux_excel"

# Dossier où vous souhaitez enregistrer les fichiers CSV
csv_directory = "../tableaux_csv"

# Créer le dossier des fichiers CSV s'il n'existe pas
if not os.path.exists(csv_directory):
    os.mkdir(csv_directory)

# Parcourir la structure des dossiers dans le dossier Excel
for root, dirs, files in os.walk(excel_directory):
    for file in files:
        if file.endswith(".xlsx"):
            excel_file_path = os.path.join(root, file)
            csv_relative_path = os.path.relpath(excel_file_path, excel_directory)
            csv_file_path = os.path.join(csv_directory, os.path.splitext(csv_relative_path)[0] + ".csv")
            
            # Assurez-vous que le dossier du fichier CSV existe
            csv_file_folder = os.path.dirname(csv_file_path)
            if not os.path.exists(csv_file_folder):
                os.makedirs(csv_file_folder)
            
            # Lire le fichier Excel et le convertir en CSV
            df = pd.read_excel(excel_file_path)
            df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

print("Les fichiers Excel ont été convertis en fichiers CSV tout en conservant la structure des dossiers.")