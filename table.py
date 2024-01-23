import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

# L'URL de la page web que vous souhaitez analyser
url = "https://www.insee.fr/fr/statistiques/2011101?geo=COM-42330"

# Envoyer une requête GET pour obtenir le contenu de la page
response = requests.get(url)

# Vérifier si la requête a réussi (code 200 signifie succès)
if response.status_code == 200:
    # Analyser la page avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver tous les tableaux sur la page
    tables = soup.find_all('table')

    # Créer un répertoire pour stocker les tableaux classés
    output_directory = "tableaux_classes"
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    # Mots-clés à rechercher dans le contenu des tableaux
    mots_cles = ["POP", "FAM", "LOG", "FOR", "EMP", "ACT", "RFD", "REV", "DEN", "TOU"]

    # Parcourir les tableaux
    for index, table in enumerate(tables):
        # Obtenir le texte du tableau pour vérifier les mots-clés
        table_text = table.get_text().strip().upper()
        
        # Vérifier si les mots-clés sont présents dans le texte du tableau
        for mot_cle in mots_cles:
            if mot_cle in table_text:
                # Créer un sous-répertoire pour le mot-clé s'il n'existe pas
                keyword_directory = os.path.join(output_directory, mot_cle)
                if not os.path.exists(keyword_directory):
                    os.mkdir(keyword_directory)

                # Extraire les données tabulaires à partir du code HTML
                df = pd.read_html(str(table))[0]  # Utilisez le premier DataFrame trouvé
                # Enregistrer les données dans un fichier CSV
                csv_filename = os.path.join(keyword_directory, f"Tableau_{index + 1}.csv")
                df.to_csv(csv_filename, index=False)

    print("Les tableaux ont été classés dans des dossiers en fonction des mots-clés et convertis en fichiers CSV.")

else:
    print(f"La requête a échoué avec le code d'état {response.status_code}")
