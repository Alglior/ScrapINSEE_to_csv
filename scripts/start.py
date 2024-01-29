import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, Tk, simpledialog
from tkinter import PhotoImage
import subprocess
import os

def run_script1():
    # Créer une nouvelle fenêtre
    window = tk.Tk()
    window.title("Confirmer l'exécution")

    # Function to execute when window is closed
    def on_window_close():
        # Clear the contents of urls.txt
        with open("urls.txt", "w") as file:
            file.write("")

        print("La fenêtre avec la scrollbox est fermée et urls.txt a été vidé")
        window.destroy()

    # Function to add URL from the entry to the text area
    def add_url():
        # Enable the text area, add URL, then disable it
        text_area.config(state=tk.NORMAL)
        url = url_entry.get()
        text_area.insert(tk.END, url + "\n")
        text_area.config(state=tk.DISABLED)

    # Bind the close event to the on_window_close function
    window.protocol("WM_DELETE_WINDOW", on_window_close)

    # Ajouter une zone de texte avec une barre de défilement
    global text_area
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=30, state=tk.DISABLED)
    text_area.pack()

    # Ajouter un champ pour entrer une nouvelle URL
    global url_entry
    url_entry = tk.Entry(window, width=80)
    url_entry.pack()

    # Ajouter un bouton pour ajouter une URL
    add_url_button = tk.Button(window, text="Ajouter URL", command=add_url)
    add_url_button.pack()

    # Ajouter un bouton pour exécuter table.py
    proceed_button = tk.Button(window, text="Exécuter", command=lambda: subprocess.run(["python", "table.py"]))
    proceed_button.pack()
    
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

def run_script5():
    # Create a dialog box to input a folder name
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    new_folder_name = simpledialog.askstring("Input Folder Name", "Enter a new folder name:")

    # Check if the user entered a folder name
    if new_folder_name is not None:
        # Construct the new filename based on the entered folder name
        new_filename = f"../results/{new_folder_name}"

        try:
            with open('combine.py', 'r') as file:
                lines = file.readlines()

            for i, line in enumerate(lines):
                if 'filename =' in line:
                    lines[i] = f'filename = "{new_filename}"\n'

            with open('combine.py', 'w') as file:
                file.writelines(lines)

            messagebox.showinfo("Execution", "File combine.py updated!")

        except FileNotFoundError:
            messagebox.showerror("Error", "File combine.py not found.")
        
        try:
            subprocess.run(["python", "combine.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error executing combine.py: {str(e)}")

def run_script6():
    try:
        subprocess.run(["python", "tables_scripts/_tableauPOP G2.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script7():
    try:
        subprocess.run(["python", "tables_scripts/_tableauACT G1.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script8():
    try:
        subprocess.run(["python", "tables_scripts/_tableauACT G2.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script9():
    try:
        subprocess.run(["python", "tables_scripts/_tableauACT T1.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script10():
    try:
        subprocess.run(["python", "tables_scripts/_tableauACT T2.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script11():
    try:
        subprocess.run(["python", "tables_scripts/_tableauACT T3.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script12():
    try:
        subprocess.run(["python", "tables_scripts/_tableauACT T4.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script13():
    try:
        subprocess.run(["python", "tables_scripts/_tableauDEN G1.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script14():
    try:
        subprocess.run(["python", "tables_scripts/_tableauDEN G3.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script15():
    try:
        subprocess.run(["python", "tables_scripts/_tableauDEN T1.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Créer la fenêtre principale
window = tk.Tk()
window.title("Shovel - Outil de collecte de données")
# Rendre la fenêtre non redimensionnable
window.resizable(False, False)

# Dimensions de la fenêtre
window_width = 800
window_height = 450

# Positionner la fenêtre au centre de l'écran
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Create a Notebook widget to have two tabs
notebook = ttk.Notebook(window)
notebook.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create the first tab with current buttons
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Scraping des données INSEE")

frame_buttons = tk.Frame(tab1)
frame_buttons.pack(pady=10)

btn_script1 = tk.Button(frame_buttons, text="Chercher commune dans l'INSEE", command=run_script1, width=30, height=2)
btn_script1.grid(row=0, column=0, padx=5, pady=5)

btn_script2 = tk.Button(frame_buttons, text="Convertir excel en csv", command=run_script2, width=30, height=2)
btn_script2.grid(row=0, column=1, padx=5, pady=5)

btn_script3 = tk.Button(frame_buttons, text="Trier/rechercher les dossiers", command=run_script3, width=30, height=2)
btn_script3.grid(row=1, column=0, padx=5, pady=5)

btn_script4 = tk.Button(frame_buttons, text="Documentation", command=run_script4, width=30, height=2)
btn_script4.grid(row=1, column=1, padx=5, pady=5)

btn_script5 = tk.Button(frame_buttons, text="Combiner les tables", command=run_script5, width=30, height=2)
btn_script5.grid(row=2, column=0, padx=5, pady=5)

# Create the second tab with additional buttons
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Traitement des données")

frame_buttons2 = tk.Frame(tab2)
frame_buttons2.pack(pady=10)

# Créer un canvas pour contenir les boutons avec un ascenseur vertical
canvas = tk.Canvas(frame_buttons2)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Ajouter un ascenseur vertical
scrollbar = tk.Scrollbar(frame_buttons2, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Créer un cadre intérieur dans le canvas pour les boutons
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

# Ajouter les boutons à l'intérieur du cadre intérieur et les centrer horizontalement
button_width = 30
button_height = 2

# Utiliser une liste de noms de scripts et de fonctions pour simplifier le code
script_data = [
    ("_tableauPOP G2", run_script6),
    ("_tableauACT G1", run_script7),
    ("_tableauACT G2", run_script8),
    ("_tableauACT T1", run_script9),
    ("_tableauACT T2", run_script10),
    ("_tableauACT T3", run_script11),
    ("_tableauACT T4", run_script12),
    ("_tableauDEN G1", run_script13),
    ("_tableauDEN G3", run_script14),
    ("_tableauDEN T1", run_script15),
]

row_index = 0
column_index = 0

for text, command in script_data:
    if command is not None:
        btn = tk.Button(inner_frame, text=text, command=command, width=button_width, height=button_height)
        btn.grid(row=row_index, column=column_index, padx=5, pady=5)
    else:
        label = tk.Label(inner_frame, text=text)
        label.grid(row=row_index, column=column_index, padx=5, pady=5)

    # Avancer dans les colonnes
    column_index += 1

    # Passer à la deuxième colonne après chaque paire de boutons
    if column_index == 2:
        column_index = 0
        row_index += 1

# Configurer le canvas pour gérer le défilement
inner_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Configurer le canvas pour réagir à la taille de la fenêtre
frame_buttons2.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

# Ajuster la largeur du canvas
new_canvas_width = 650  # Vous pouvez ajuster la largeur en fonction de vos besoins
canvas.config(width=new_canvas_width)



# Ajouter et redimensionner l'image dans le coin inférieur droit
img = PhotoImage(file='univ.png')
img = img.subsample(2, 2)  # Réduire la taille de l'image de moitié
label_image = tk.Label(window, image=img)
label_image.place(relx=1.0, rely=1.0, anchor='se')

# Démarrer l'interface utilisateur
window.mainloop()
