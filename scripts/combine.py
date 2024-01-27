import os
import pandas as pd

# filename contenant les fichiers CSV
filename = "../results/_tableauACT G1"

# Liste pour stocker tous les DataFrames des fichiers CSV
dfs = []

# Parcourir tous les fichiers dans le filename
for fichier in os.listdir(filename):
    if fichier.endswith('.csv'):
        chemin_complet = os.path.join(filename, fichier)
        
        # Charger le fichier CSV en DataFrame et l'ajouter à la liste
        df = pd.read_csv(chemin_complet)
        dfs.append(df)

# Concaténer tous les DataFrames en un seul
df_combine = pd.concat(dfs, ignore_index=True)

# Enregistrer le DataFrame combiné dans un fichier CSV
df_combine.to_csv('../results/fichier_combine.csv', index=False)

print("Combinaison terminée. Le fichier combiné a été enregistré.")
