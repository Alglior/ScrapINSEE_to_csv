import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox

def process_csv_and_show_message():
    try:
        # Load the CSV file
        csv_path = '../results/_tableauACT T3.csv'  # Replace with your file path
        df = pd.read_csv(csv_path)

        # Renaming columns for clarity
        df = df.rename(columns={
            "Unnamed: 0": "Category",
            "H_______o_______m_______m_______e_______s": "Hommes",
            "d_______o_______n_______t_______________%_______________t_______e_______m_______p_______s_______________p_______a_______r_______t_______i_______e_______l": "Homme_temps_partiel",
            "F_______e_______m_______m_______e_______s": "Femmes",
            "d_______o_______n_______t_______________%_______________t_______e_______m_______p_______s_______________p_______a_______r_______t_______i_______e_______l_______._______1": "Femme_temps_partiel",
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

        # Pivoting the DataFrame
        df_pivoted = df.pivot(index="code", columns="Category", values=["Hommes", "Homme_temps_partiel", "Femmes", "Femme_temps_partiel"]).reset_index()
        df_pivoted.columns = ['_'.join(col).strip() for col in df_pivoted.columns.values]

        # Specify the path where to save the modified CSV file
        output_csv_path = '../results/_tableauACT T3-2.csv'  # Replace with your desired output path

        # Save the modified DataFrame to the specified path
        df_pivoted.to_csv(output_csv_path, index=False)

        # Show completion message
        messagebox.showinfo("Process Complete", f"Modified DataFrame saved at '{output_csv_path}'.")

    except Exception as e:
        # Show error message
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize Tkinter root
root = tk.Tk()
root.withdraw()  # We don't want a full GUI, so keep the root window from appearing

# Process the CSV and show the message box
process_csv_and_show_message()
