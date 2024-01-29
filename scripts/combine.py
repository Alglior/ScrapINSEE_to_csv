import os
import pandas as pd

# filename contenant les fichiers CSV
filename = "../results/_tableauDEN G1"

# Extraire le nom du fichier CSV combiné à partir de filename
nom_fichier_combine = filename.split('/')[-1]

# Liste pour stocker tous les DataFrames des fichiers CSV
dfs = []

# Parcourir tous les fichiers dans le filename
for fichier in os.listdir(filename):
    if fichier.endswith('.csv'):
        chemin_complet = os.path.join(filename, fichier)
        
        # Charger le fichier CSV en DataFrame et l'ajouter à la liste
        df = pd.read_csv(chemin_complet)
        df.columns = ['_'.join(map(str, col)).strip().replace('U_n_n_a_m_e_d_:_ _0', '').replace(' ', '_') for col in df.columns.values]
        dfs.append(df)

# Concaténer tous les DataFrames en un seul
df_combine = pd.concat(dfs, ignore_index=True)

# Enregistrer le DataFrame combiné dans un fichier CSV
fichier_combine_path = f'../results/{nom_fichier_combine}.csv'
df_combine.to_csv(fichier_combine_path, index=False)

print(f"Combinaison terminée. Le fichier combiné a été enregistré sous le nom : {nom_fichier_combine}_combine.csv")
