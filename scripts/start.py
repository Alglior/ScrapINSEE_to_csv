import tkinter as tk
from tkinter import messagebox, scrolledtext, Tk, simpledialog
from tkinter import PhotoImage
import subprocess
import os

def run_script1():
    # Lire le contenu de urls.txt
    try:
        with open('urls.txt', 'r') as file:
            urls_content = file.read()
        # Créer une nouvelle fenêtre
        window = tk.Tk()
        window.title("Confirmer l'exécution")
        # Ajouter une zone de texte avec une barre de défilement
        text_area = scrolledtext.ScrolledText(window, wrap = tk.WORD, width = 100, height = 30)
        text_area.insert(tk.INSERT, f"Contenu de urls.txt:\n{urls_content}\n\nVoulez-vous exécuter table.py?")
        text_area.pack()
        # Ajouter un bouton pour exécuter table.py
        proceed_button = tk.Button(window, text = "Exécuter", command = lambda: subprocess.run(["python", "table.py"]))
        proceed_button.pack()
        # Exécuter la boucle principale de la fenêtre
        window.mainloop()
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Le fichier urls.txt n'a pas été trouvé.")

def run_script2():
    root = Tk()
    root.withdraw()  # Hide the main window
    MsgBox = messagebox.askquestion ('Execute Script','Vous allez à présent convertir les tableaux Excel en CSV. Êtes-vous sûr ?',icon = 'warning')
    if MsgBox == 'yes':
        subprocess.call(["python", "excel_to_csv.py"])
        messagebox.showinfo("Exécution", "Dossier csv créé avec succès")
    root.destroy()  # Destroy the main window

# -*- coding: utf-8 -*-

def run_script3():
    # Create a new tkinter window
    ROOT = tk.Tk()

    # Prevent the user from resizing the window
    ROOT.resizable(False, False)

    # Hide the window
    ROOT.withdraw()

    # Ask the user to enter a new value for the filename
    new_filename = simpledialog.askstring(title="Modification",
                                          prompt="Enter the new filename:")

    # Check if the user entered a value
    if new_filename:
        # Open the search.py file in read-write mode
        with open('search.py', 'r+', encoding='utf-8') as file:
            # Read the content of the file
            lines = file.readlines()

            # Find the line containing 'filename ='
            for i, line in enumerate(lines):
                if 'filename =' in line:
                    # Replace the entire line with the new value
                    lines[i] = f'filename = "{new_filename}.csv"\n'

            # Go back to the beginning of the file and write the updated content
            file.seek(0)
            file.writelines(lines)
            file.truncate()

        messagebox.showinfo("Execution", "File search.py updated!")

        # Execute the modified search.py script
        try:
            subprocess.run(["python", "search.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error executing search.py: {str(e)}")

def run_script4():
    messagebox.showinfo("Exécution", "Le fichier README.md va s'ouvrir dans votre lecteur par défaut.")
    
    # Ouvrir le fichier README.md dans le lecteur par défaut
    readme_path = "../README.md"
    
    if os.path.exists(readme_path):
        os.system(f"start {readme_path}")
    else:
        messagebox.showerror("Erreur", f"Le fichier {readme_path} n'a pas été trouvé.")


# Créer la fenêtre principale
window = tk.Tk()
window.title("Shovel - Outil de collecte de données")
# Rendre la fenêtre non redimensionnable
window.resizable(False, False)

# Dimensions de la fenêtre
window_width = 600
window_height = 300

# Positionner la fenêtre au centre de l'écran
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Créer un cadre pour organiser les boutons
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

# Créer des boutons pour lancer les scripts
btn_script1 = tk.Button(frame_buttons, text="Chercher commmune dans l'INSEE", command=run_script1, width=30, height=2)
btn_script1.grid(row=0, column=0, padx=5, pady=5)

btn_script2 = tk.Button(frame_buttons, text="Convertir excel en csv", command=run_script2, width=30, height=2)
btn_script2.grid(row=0, column=1, padx=5, pady=5)

btn_script3 = tk.Button(frame_buttons, text="Trier/rechercher les dossiers", command=run_script3, width=30, height=2)
btn_script3.grid(row=1, column=0, padx=5, pady=5)

btn_script4 = tk.Button(frame_buttons, text="Documentation", command=run_script4, width=30, height=2)
btn_script4.grid(row=1, column=1, padx=5, pady=5)
# Ajouter et redimensionner l'image dans le coin inférieur droit
img = PhotoImage(file='univ.png')
img = img.subsample(2, 2)  # Réduire la taille de l'image de moitié
label_image = tk.Label(window, image=img)
label_image.place(relx=1.0, rely=1.0, anchor='se')

# Démarrer l'interface utilisateur
window.mainloop()
