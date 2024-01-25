import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
from io import StringIO
import re
from openpyxl import Workbook
from openpyxl.styles import Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows

# Fonction pour ajouter des bordures à toutes les cellules d'une feuille
def add_borders_to_sheet(ws):
    thin_border = Border(left=Side(style='thin'), 
                         right=Side(style='thin'), 
                         top=Side(style='thin'), 
                         bottom=Side(style='thin'))
    for row in ws.iter_rows():
        for cell in row:
            cell.border = thin_border

# L'URL de la page web que vous souhaitez analyser
url = "https://www.insee.fr/fr/statistiques/2011101?geo=COM-42330"

# Envoyer une requête GET pour obtenir le contenu de la page
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    
    output_directory = "tableaux_excel"
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)
    
    sanitized_url = re.sub(r'[\\/*?:"<>|]', "", url.replace("https://", ""))
    url_directory = os.path.join(output_directory, sanitized_url)
    if not os.path.exists(url_directory):
        os.mkdir(url_directory)
    
    com_number = re.search(r'COM-(\d+)', url)
    com_number = com_number.group(1) if com_number else "unknown"

    mots_cles = ["POP", "FAM", "LOG", "FOR", "EMP", "ACT", "RFD", "REV", "DEN", "TOU"]

    for index, table in enumerate(tables):
        table_text = table.get_text().strip().upper()
        
        for mot_cle in mots_cles:
            if mot_cle in table_text:
                keyword_directory = os.path.join(url_directory, mot_cle)
                if not os.path.exists(keyword_directory):
                    os.mkdir(keyword_directory)
                
                h3_title = table.find_previous("h3")
                if h3_title:
                    title_text = re.sub(r'[\\/*?:"<>|\n\r]+', "", h3_title.text.strip())
                    title_text = (title_text[:50] + '..') if len(title_text) > 50 else title_text
                else:
                    title_text = f"Tableau_{index + 1}"
                
                html_str = str(table)
                df = pd.read_html(StringIO(html_str))[0]
                
                if 'Unnamed: 0' in df.columns:
                    df.drop(columns=['Unnamed: 0'], inplace=True)
                
                # Créer un classeur Excel pour chaque tableau
                wb = Workbook()
                ws = wb.active
                
                # Ajouter les données du DataFrame à la feuille Excel
                for r_idx, df_row in enumerate(dataframe_to_rows(df, index=False, header=True), 1):
                    for c_idx, value in enumerate(df_row, 1):
                        ws.cell(row=r_idx, column=c_idx, value=value)
                
                # Ajouter des bordures aux cellules
                add_borders_to_sheet(ws)

                # Construire le nom du fichier Excel
                excel_filename = os.path.join(keyword_directory, f"{com_number}_{title_text}.xlsx")
                wb.save(excel_filename)

    print("Les tableaux ont été classés et convertis en fichiers Excel avec des bordures autour des cellules.")
else:
    print(f"La requête a échoué avec le code d'état {response.status_code}")
