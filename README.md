UTILISATEURS SOUS WINDOWS - INSTRUCTIONS :

1. Téléchargez le dossier zip depuis github.com.
2. Décompressez le dossier.

3. Exécutez le fichier "Install.bat" et attendez la fin de l'installation.

ENSUITE :

4. Lancez le fichier "Launch_SHOVEL.bat" pour ouvrir l'application.
5. Une fois l'application ouverte, cliquez sur le bouton "Chercher communes dans l'INSEE". Cela ouvrira une fenêtre de texte où vous pourrez insérer les liens des communes de l'INSEE. Les liens ressembleront à ceci : https://www.insee.fr/fr/statistiques/2011101?geo=COM-42218
   - Les chiffres "42218" correspondent au numéro de la commune. Vous pouvez simplement copier-coller l'URL de l'INSEE et modifier les derniers chiffres après le "-".
6. Une fois que vous avez ajouté les URLs, cliquez sur le bouton "Exécuter". Cela lancera le script Python pour télécharger toutes les tables depuis les URLs spécifiées.
   - NE VOUS INQUIÉTEZ PAS SI L'APPLICATION NE RÉPOND PAS, ELLE EST EN TRAIN DE COPIER LES TABLES EN FICHIERS EXCEL.

7. Cette opération créera un nouveau dossier nommé "tableaux_excel".

8. Pour convertir les fichiers Excel en fichiers CSV, cliquez sur le bouton "Convertir Excel en CSV". L'application vous demandera si vous souhaitez effectuer la conversion. Une fois confirmé, un nouveau dossier nommé "tableaux_csv" sera créé avec tous les fichiers convertis au format CSV.

9. Si vous souhaitez trier ou rechercher des fichiers dans le dossier, utilisez le bouton "Trier/Rechercher dossier". Cela ouvrira une fenêtre de dialogue où vous pourrez saisir le nom du fichier que vous recherchez. Ce bouton permet de regrouper toutes les tables du type "POP G1" pour toutes les communes que vous avez téléchargées, en les rangeant ensemble.

REMARQUE : Vous devez saisir le nom complet du fichier à l'exception du code de la commune. Par exemple, "42022_tableauEMP T6 - Emplois selon le statut profession.." deviendra "_tableauEMP T6 - Emplois selon le statut profession.." 