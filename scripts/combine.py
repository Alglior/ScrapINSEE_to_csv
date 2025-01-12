import pandas as pd
import os

def combine_csv_files(input_dir):
    all_data = []
    
    try:
        # Vérifier si le dossier existe
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"Le dossier {input_dir} n'existe pas")
            
        # Lister tous les fichiers CSV dans le dossier
        for fichier in os.listdir(input_dir):
            if fichier.endswith('.csv'):
                file_path = os.path.join(input_dir, fichier)
                # Lire le CSV en ignorant l'index
                df = pd.read_csv(file_path, index_col=False)
                
                # Nettoyer les noms de colonnes de plusieurs façons
                df.columns = [
                    col.replace('Unnamed: 0', '')
                       .replace('Unnamed:0', '')
                       .replace('__', '_')
                       .strip('_')
                       .strip() 
                    for col in df.columns
                ]
                
                # Supprimer toute colonne vide ou qui ne contient que des NaN
                df = df.dropna(axis=1, how='all')
                
                # Supprimer explicitement toute colonne qui commence par "Unnamed"
                unnamed_cols = [col for col in df.columns if col.startswith('Unnamed')]
                if unnamed_cols:
                    df = df.drop(columns=unnamed_cols)
                
                all_data.append(df)
        
        if not all_data:
            raise ValueError(f"Aucun fichier CSV trouvé dans {input_dir}")
            
        # Combiner tous les DataFrames
        combined_df = pd.concat(all_data, ignore_index=True)
        
        # Créer le dossier csv s'il n'existe pas
        csv_dir = os.path.join(os.path.dirname(os.path.dirname(input_dir)), 'csv')
        os.makedirs(csv_dir, exist_ok=True)
        
        # Sauvegarder le fichier combiné
        output_filename = os.path.basename(input_dir) + "_combined.csv"
        output_path = os.path.join(csv_dir, output_filename)
        combined_df.to_csv(output_path, index=False)
        print(f"Fichier combiné créé : {output_path}")
        
    except Exception as e:
        print(f"Erreur lors de la combinaison des fichiers : {str(e)}")
        raise

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
        combine_csv_files(input_dir)
    else:
        print("Veuillez spécifier le chemin du dossier à traiter")
