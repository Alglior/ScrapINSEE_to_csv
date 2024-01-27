import os
import re
import shutil

def search_and_copy_csv_files(parent_folder, file_pattern, destination_folder):
    pattern = re.compile(r'\d+_{}'.format(file_pattern))
    for root, dirs, files in os.walk(parent_folder):
        for file in files:
            if pattern.match(file):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} to {destination_path}")

parent_folder = "tableaux_csv"
file_pattern = "tableauACT G1 - Part des salariés de 15 ans ou plu...csv"
destination_folder = os.path.join("results", "tableauACT G1 -")

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

search_and_copy_csv_files(parent_folder, file_pattern, destination_folder)
