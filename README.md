# Shovel - Outil de collecte de données INSEE

## Instructions d'installation

1. Téléchargez le projet :
   - Cliquez sur le bouton vert "Code" sur GitHub
   - Sélectionnez "Download ZIP"
   - Décompressez le dossier ZIP
   - ou utiliser '''git clone https://github.com/Alglior/ScrapINSEE_to_csv.git''' dans l'emplacement du bon dossier

2. Installation :
   - Double-cliquez sur "Install.bat pour windows / install.sh pour linux(debian base)"
   - Attendez la fin de l'installation

## Utilisation

1. Lancez l'application :
   - Double-cliquez sur "Launch_SHOVEL.bat pour windows / Launch_SHOVEL.sh pour linux"  

2. Collecte des données :
   - Cliquez sur "Créer URLs INSEE"
   - Entrez les codes INSEE des communes (ex: 42218)
   - Les URLs seront automatiquement générées et sauvegardées dans un fichier urls.txt

3. Téléchargement des données :
   - Cliquez sur "Chercher commune dans l'INSEE"
   - Sélectionnez le fichier urls.txt généré précédemment
   - Cliquez sur "Démarrer téléchargement"
   - L'application va automatiquement :
     - Télécharger les tableaux Excel
     - Les convertir en CSV
     - Trier les fichiers par type de tableau
     - Combiner les tableaux similaires

4. Résultats :
   - Les fichiers Excel bruts seront dans le dossier "tableaux_excel"
   - Les fichiers CSV individuels seront dans "tableaux_csv"
   - Les fichiers triés et regroupés seront dans "results"
   - Les fichiers combinés seront dans le dossier "csv"

## Remarques

- Ne fermez pas l'application pendant le téléchargement
- Si le téléchargement échoue, utilisez le bouton "Effacer progression" pour recommencer
- Consultez la documentation complète via le bouton "Documentation"

