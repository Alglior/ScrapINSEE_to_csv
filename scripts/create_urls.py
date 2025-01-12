import tkinter as tk
from tkinter import filedialog, Text
import os

def create_urls_from_numbers():
    root = tk.Tk()
    root.withdraw()

    dialog = tk.Toplevel()  # Créer la fenêtre de dialogue
    dialog.title("Créer des URLs INSEE")
    dialog.geometry("400x500")

    def save_and_process():
        numbers = text_area.get("1.0", tk.END).strip().split('\n')
        
        # Ask for save location
        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Enregistrer le fichier URLs",
            initialdir=os.path.dirname(os.path.abspath(__file__))
        )
        
        if save_path:
            with open(save_path, 'w') as f:
                for number in numbers:
                    if number.strip():  # Skip empty lines
                        url = f"https://www.insee.fr/fr/statistiques/2011101?geo=COM-{number.strip()}"
                        f.write(f"{url}\n")
            dialog.destroy()

    # Add instructions
    label = tk.Label(dialog, text="Entrez les numéros (un par ligne):")
    label.pack(pady=10)

    # Add text area
    text_area = Text(dialog, height=20, width=40)
    text_area.pack(pady=10, padx=10)

    # Add save button
    save_button = tk.Button(dialog, text="Sauvegarder et Créer URLs", command=save_and_process)
    save_button.pack(pady=10)

    dialog.mainloop()

if __name__ == "__main__":
    create_urls_from_numbers()
