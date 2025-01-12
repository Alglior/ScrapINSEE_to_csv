import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, Tk, simpledialog, filedialog
from tkinter import PhotoImage
import subprocess
import os
import sys
from tqdm import tqdm
import time  # Ajouter cet import en haut du fichier avec les autres imports
import threading  # Ajouter cet import en haut du fichier

# Obtenir les chemins
PYTHON_PATH = sys.executable
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
current_file_path = os.path.join(SCRIPT_DIR, "urls.txt")  # Définir la variable globalement

def add_url():
    new_url = url_entry.get()
    if (new_url):
        try:
            with open(current_file_path, 'a') as file:
                file.write(f"{new_url}\n")
            update_text_area()
            url_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors de l'écriture dans le fichier: {e}")

def update_text_area():
    try:
        with open(current_file_path, 'r') as file:
            urls_content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.INSERT, f"Contenu de {os.path.basename(current_file_path)}:\n{urls_content}\n\nVoulez-vous exécuter table.py?")
    except FileNotFoundError:
        messagebox.showerror("Erreur", f"Le fichier {current_file_path} n'a pas été trouvé.")

def run_table_with_progress():
    try:
        # Lire le nombre total d'URLs
        with open(current_file_path, 'r') as f:
            total_urls = len([line for line in f if line.strip()])
        
        # Créer une fenêtre de progression
        progress_window = tk.Toplevel()
        progress_window.title("Téléchargement en cours")
        progress_window.geometry("300x150")
        
        # Label pour afficher le progrès
        progress_label = tk.Label(progress_window, text="0/" + str(total_urls) + " tables téléchargées")
        progress_label.pack(pady=10)
        
        # Barre de progression
        progress_bar = ttk.Progressbar(progress_window, length=200, mode='determinate', maximum=total_urls)
        progress_bar.pack(pady=10)
        
        # Créer un fichier temporaire pour suivre la progression
        progress_file = os.path.join(SCRIPT_DIR, "download_progress.txt")
        if (os.path.exists(progress_file)):
            os.remove(progress_file)
            
        def update_progress():
            if (os.path.exists(progress_file)):
                with open(progress_file, 'r') as f:
                    current = int(f.read().strip() or 0)
                progress_bar['value'] = current
                progress_label.config(text=f"{current}/{total_urls} tables téléchargées")
                
                if (current < total_urls):
                    progress_window.after(100, update_progress)
                else:
                    progress_window.destroy()
                    # Lancer automatiquement la conversion en CSV
                    subprocess.call([PYTHON_PATH, os.path.join(SCRIPT_DIR, "excel_to_csv.py")])
                    messagebox.showinfo("Succès", "Téléchargement et conversion en CSV terminés!")
            else:
                progress_window.after(100, update_progress)
        
        # Démarrer la mise à jour de la progression
        update_progress()
        
        # Exécuter table.py avec le fichier de progression ET le chemin du fichier URLs
        subprocess.Popen([
            PYTHON_PATH,
            os.path.join(SCRIPT_DIR, "table.py"),
            "--progress-file",
            progress_file,
            "--urls-file",
            current_file_path  # Ajout du chemin complet du fichier URLs
        ])
        
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du téléchargement: {str(e)}")

def run_script1():
    # Créer une nouvelle fenêtre
    window = tk.Tk()
    window.title("Téléchargement des données INSEE")

    # Configuration du délai et tentatives
    config_frame = tk.Frame(window)
    config_frame.pack(fill=tk.X, padx=10, pady=5)
    
    tk.Label(config_frame, text="Délai entre les tentatives (secondes):").pack(side=tk.LEFT)
    retry_delay = tk.Entry(config_frame, width=10)
    retry_delay.insert(0, "300")  # 5 minutes par défaut
    retry_delay.pack(side=tk.LEFT, padx=5)
    
    tk.Label(config_frame, text="Tentatives max (0 = infini):").pack(side=tk.LEFT)
    max_retries = tk.Entry(config_frame, width=10)
    max_retries.insert(0, "0")
    max_retries.pack(side=tk.LEFT, padx=5)

    # Ajouter une barre de progression
    progress_frame = tk.Frame(window)
    progress_frame.pack(fill=tk.X, padx=10, pady=5)
    
    progress_label = tk.Label(progress_frame, text="Progression:")
    progress_label.pack(side=tk.LEFT)
    
    progress_bar = ttk.Progressbar(progress_frame, length=300, mode='determinate')
    progress_bar.pack(side=tk.LEFT, padx=5)
    
    url_count_label = tk.Label(progress_frame, text="0/0 URLs")
    url_count_label.pack(side=tk.LEFT)

    # Status label pour les messages
    status_label = tk.Label(window, text="Sélectionnez un fichier d'URLs pour commencer...", wraplength=350)
    status_label.pack(pady=5)

    # Variable pour contrôler l'exécution
    running = {'value': True}

    def stop_execution():
        running['value'] = False
        window.destroy()

    def update_progress():
        try:
            with open(current_file_path, 'r') as f:
                urls = f.readlines()
                total_urls = len(urls)
                progress_bar['maximum'] = total_urls
                
                # Lire la progression actuelle
                progress_file = os.path.join(SCRIPT_DIR, "download_progress.txt")
                if os.path.exists(progress_file):
                    with open(progress_file, 'r') as pf:
                        processed_urls = int(pf.read().strip() or 0)
                else:
                    processed_urls = 0
                    
                progress_bar['value'] = processed_urls
                url_count_label.config(text=f"{processed_urls}/{total_urls} URLs")
                
        except FileNotFoundError:
            progress_bar['value'] = 0
            url_count_label.config(text="0/0 URLs")
        
        if running['value']:
            window.after(1000, update_progress)

    def choose_file():
        global current_file_path
        initial_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Forcer la fenêtre au premier plan avant et après le dialogue
        window.lift()
        window.focus_force()
        
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Choisir le fichier URLs",
            initialdir=initial_dir
        )
        
        # Remettre la fenêtre au premier plan après la sélection
        window.lift()
        window.focus_force()
        
        if file_path:
            current_file_path = file_path
            status_label.config(text=f"Fichier sélectionné: {os.path.basename(file_path)}")
            update_progress()
            start_button.config(state=tk.NORMAL)

    def start_download():
        delay = int(retry_delay.get())
        retries = int(max_retries.get())
        attempt = 0

        while running['value']:
            try:
                status_label.config(text=f"Tentative {attempt + 1}...")
                window.update()

                # Exécuter table.py avec le fichier de progression
                progress_file = os.path.join(SCRIPT_DIR, "download_progress.txt")
                process = subprocess.Popen([
                    PYTHON_PATH,
                    os.path.join(SCRIPT_DIR, "table.py"),
                    "--progress-file",
                    progress_file,
                    "--urls-file",
                    current_file_path,
                    "--resume"
                ])

                while process.poll() is None and running['value']:
                    window.update()
                    time.sleep(0.1)

                if process.returncode == 0:
                    # Lancer la conversion en CSV après le téléchargement réussi
                    status_label.config(text="Conversion en CSV en cours...")
                    window.update()
                    subprocess.call([PYTHON_PATH, os.path.join(SCRIPT_DIR, "excel_to_csv.py")])
                    
                    # Ajouter l'appel au tri automatique
                    status_label.config(text="Tri des tables en cours...")
                    window.update()
                    subprocess.call([PYTHON_PATH, os.path.join(SCRIPT_DIR, "search.py")])
                    
                    messagebox.showinfo("Succès", "Téléchargement, conversion en CSV et tri des tables terminés!")
                    window.destroy()
                    break
                    
            except Exception as e:
                attempt += 1
                if retries > 0 and attempt >= retries:
                    messagebox.showerror("Erreur", "Nombre maximum de tentatives atteint")
                    break

                status_label.config(text=f"Erreur rencontrée: {str(e)}\nNouvelle tentative dans {delay} secondes...")
                window.update()

                for i in range(delay):
                    if not running['value']:
                        break
                    status_label.config(text=f"Reprise dans {delay - i} secondes...")
                    window.update()
                    time.sleep(1)

    def clear_progress():
        # Forcer la fenêtre au premier plan avant la boîte de dialogue
        window.lift()
        window.focus_force()
        
        response = messagebox.askquestion(
            "Confirmation",
            "Voulez-vous vraiment effacer la progression?\n\n"
            "Cela supprimera:\n"
            "- Le fichier de progression\n"
            "- Le cache de téléchargement\n"
            "La prochaine exécution recommencera depuis le début.",
            icon='warning'
        )
        
        # Remettre la fenêtre au premier plan après la boîte de dialogue
        window.lift()
        window.focus_force()
        
        if response == 'yes':
            try:
                # Supprimer le fichier de progression
                progress_file = os.path.join(SCRIPT_DIR, "download_progress.txt")
                if os.path.exists(progress_file):
                    os.remove(progress_file)
                
                # Réinitialiser la barre de progression
                progress_bar['value'] = 0
                url_count_label.config(text="0/0 URLs")
                status_label.config(text="Progression effacée. Prêt pour un nouveau téléchargement.")
                
                # Forcer encore une fois la fenêtre au premier plan
                window.lift()
                window.focus_force()
                messagebox.showinfo("Succès", "La progression a été effacée avec succès.")
                window.lift()
                window.focus_force()
                
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'effacement: {str(e)}")
                window.lift()
                window.focus_force()

    # Création des boutons
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    choose_button = tk.Button(button_frame, text="Sélectionner fichier URLs", command=choose_file)
    choose_button.pack(side=tk.LEFT, padx=5)

    start_button = tk.Button(button_frame, text="Démarrer téléchargement", command=start_download, state=tk.DISABLED)
    start_button.pack(side=tk.LEFT, padx=5)

    clear_button = tk.Button(button_frame, text="Effacer progression", command=clear_progress)
    clear_button.pack(side=tk.LEFT, padx=5)

    stop_button = tk.Button(button_frame, text="Arrêter", command=stop_execution)
    stop_button.pack(side=tk.LEFT, padx=5)

    # Centrer la fenêtre
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def run_script2():
    root = Tk()
    root.withdraw()  # Hide the main window
    MsgBox = messagebox.askquestion ('Execute Script','Vous allez à présent convertir les tableaux Excel en CSV. Êtes-vous sûr ?',icon = 'warning')
    if MsgBox == 'yes':
        subprocess.call([PYTHON_PATH, os.path.join(SCRIPT_DIR, "excel_to_csv.py")])
        messagebox.showinfo("Exécution", "Dossier csv créé avec succès")
    root.destroy()  # Destroy the main window

# -*- coding: utf-8 -*-

def run_script3():
    # Create a new tkinter window
    ROOT = tk.Tk()
    ROOT.resizable(False, False)
    ROOT.withdraw()

    # Ask the user to enter a new value for the filename
    new_filename = simpledialog.askstring(title="Modification",
                                          prompt="Enter the new filename:")

    # Check if the user entered a value
    if new_filename:
        # Use full path for search.py
        search_path = os.path.join(SCRIPT_DIR, "search.py")
        
        try:
            # Open the search.py file in read-write mode
            with open(search_path, 'r+', encoding='utf-8') as file:
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
            subprocess.run([PYTHON_PATH, search_path])
        except FileNotFoundError:
            messagebox.showerror("Error", f"Le fichier search.py n'a pas été trouvé à l'emplacement:\n{search_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error executing search.py: {str(e)}")

def run_script4():
    messagebox.showinfo("Exécution", "Le fichier README.md va s'ouvrir dans votre lecteur par défaut.")
    
    # Ouvrir le fichier README.md dans le lecteur par défaut
    readme_path = os.path.join(os.path.dirname(SCRIPT_DIR), "README.md")
    
    if os.path.exists(readme_path):
        if sys.platform == "linux":
            subprocess.run(["xdg-open", readme_path])
        else:
            os.system(f"start {readme_path}")
    else:
        messagebox.showerror("Erreur", 
            "Le fichier README.md n'a pas été trouvé.\n"
            f"Chemin recherché : {readme_path}")

def run_script5():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    new_folder_name = simpledialog.askstring("Input Folder Name", "Enter a new folder name:")

    # Check if the user entered a folder name
    if new_folder_name is not None:
        # Construire le chemin en remontant d'un niveau par rapport à SCRIPT_DIR
        parent_dir = os.path.dirname(SCRIPT_DIR)
        # Construct the new filename at the same level as the scripts folder
        new_filename = os.path.join(parent_dir, "csv", new_folder_name)

        try:
            # S'assurer que le dossier csv existe
            csv_dir = os.path.join(parent_dir, "csv")
            os.makedirs(csv_dir, exist_ok=True)

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
            subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "combine.py")])
        except Exception as e:
            messagebox.showerror("Error", f"Error executing combine.py: {str(e)}")

def run_script6():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauPOP G2.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script7():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauACT G1.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script8():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauACT G2.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script9():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauACT T1.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script10():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauACT T2.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script11():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauACT T3.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script12():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauACT T4.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script13():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauDEN G1.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script14():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauDEN G3.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_script15():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauDEN T1.py")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Ajouter cette fonction après les autres définitions de fonctions
def run_create_urls():
    def execute_script():
        try:
            script_path = os.path.join(SCRIPT_DIR, "create_urls.py")
            result = subprocess.run([PYTHON_PATH, script_path], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
            
            # Utiliser after pour mettre à jour l'interface depuis le thread
            if result.returncode == 0:
                window.after(0, lambda: messagebox.showinfo("Succès", "URLs créées avec succès!"))
            else:
                error_msg = result.stderr.decode() if result.stderr else "Erreur inconnue"
                window.after(0, lambda: messagebox.showerror("Erreur", 
                    f"Erreur lors de la création des URLs:\n{error_msg}"))
                
        except Exception as e:
            window.after(0, lambda: messagebox.showerror("Erreur", 
                f"Erreur lors de l'exécution: {str(e)}"))

    # Lancer l'exécution dans un thread séparé
    threading.Thread(target=execute_script, daemon=True).start()

def run_script16():
    try:
        subprocess.run([PYTHON_PATH, os.path.join(SCRIPT_DIR, "tables_scripts/_tableauREV T1.py")], check=True)
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

btn_create_urls = tk.Button(frame_buttons, text="Créer URLs INSEE", command=run_create_urls, width=30, height=2)
btn_create_urls.grid(row=0, column=0, padx=5, pady=5)

btn_script1 = tk.Button(frame_buttons, text="Chercher commune dans l'INSEE", command=run_script1, width=30, height=2)
btn_script1.grid(row=1, column=0, padx=5, pady=5)

btn_script4 = tk.Button(frame_buttons, text="Documentation", command=run_script4, width=30, height=2)
btn_script4.grid(row=2, column=0, padx=5, pady=5)


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
    ("_tableauREV T1", run_script16),
]

row_index = 0
column_index = 0

for text, command in script_data:
    if (command is not None):
        btn = tk.Button(inner_frame, text=text, command=command, width=button_width, height=button_height)
        btn.grid(row=row_index, column=column_index, padx=5, pady=5)
    else:
        label = tk.Label(inner_frame, text=text)
        label.grid(row=row_index, column=column_index, padx=5, pady=5)

    # Avancer dans les colonnes
    column_index += 1

    # Passer à la deuxième colonne après chaque paire de boutons
    if (column_index == 2):
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

# Replace the image loading code near the end of the file with:
try:
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Create path to the image file
    image_path = os.path.join(script_dir, 'univ.png')
    
    img = PhotoImage(file=image_path)
    img = img.subsample(2, 2)  # Réduire la taille de l'image de moitié
    label_image = tk.Label(window, image=img)
    label_image.place(relx=1.0, rely=1.0, anchor='se')
except Exception as e:
    print(f"Warning: Could not load image: {e}")
    # Continue without the image

# Démarrer l'interface utilisateur
window.mainloop()