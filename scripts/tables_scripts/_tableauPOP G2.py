import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox

def process_csv_and_show_message():
    try:
        # Charger le fichier CSV
        csv_path = '../results/_tableauPOP G2.csv'
        df = pd.read_csv(csv_path)

        # Renommer les colonnes pour plus de clarté
        df = df.rename(columns={
            "Unnamed: 0": "Age_Group",
            "2_______0_______0_______9": "2009",
            "2_______0_______1_______4": "2014",
            "2_______0_______2_______0": "2020",
            "C___o___d___e": "code"
        })
        # Remove spaces in numbers and convert them to integers or floats
        for col in df.columns:
            if df[col].dtype == object:  # Check if the column type is 'object', which is often used for strings
                df[col] = df[col].apply(lambda x: ''.join(str(x).split()) if isinstance(x, str) else x)
                # Try converting to float or intw
                try:
                    df[col] = pd.to_numeric(df[col], errors='ignore')
                except ValueError:
                    pass  # If conversion fails, leave the column as is

        # Pivoter le DataFrame
        df_pivoted = df.pivot_table(index=["code"], columns=["Age_Group"], values=["2009", "2014", "2020"]).reset_index()
        df_pivoted.columns = ['_'.join(col).strip() for col in df_pivoted.columns.values]

        # Specify the path where to save the modified CSV file
        output_csv_path = '../results/_tableauPOP G2.csv'

        # Save the modified DataFrame to a temporary CSV file
        temp_csv_path = '../results/temp_modified_tableauPOP_G2.csv'
        df_pivoted.to_csv(temp_csv_path, index=False)

        # Remove the old CSV file and replace it with the new one
        if os.path.exists(output_csv_path):
            os.remove(output_csv_path)
        os.rename(temp_csv_path, output_csv_path)

        # Show completion message
        messagebox.showinfo("Process Complete", f"Modified DataFrame has replaced the old file at '{output_csv_path}'.")

    except Exception as e:
        # Show error message
        messagebox.showerror("Error", f"Il y a eu une erreur. Le fichier est déjà peut-être traiter. ERREUR {e}")

# Initialize Tkinter root
root = tk.Tk()
root.withdraw()  # We don't want a full GUI, so keep the root window from appearing

# Process the CSV and show the message box
process_csv_and_show_message()
