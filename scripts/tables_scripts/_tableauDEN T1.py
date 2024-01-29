import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox

def process_csv_and_show_message():
    try:
        # Load the CSV file
        csv_path = '../results/tableauDEN T1.csv'  # Replace with your file path
        df = pd.read_csv(csv_path)

        # Renaming columns for clarity
        df = df.rename(columns={
            "U___n___n___a___m___e___d___:_______0_______l___e___v___e___l_______0_______U___n___n___a___m___e___d___:_______0_______l___e___v___e___l_______1": "Category",
            "E___n___t___r___e___p___r___i___s___e___s_______c___r___é___é___e___s_______N___o___m___b___r___e": "Enterprises_Created_Number",
            "E___n___t___r___e___p___r___i___s___e___s_______c___r___é___é___e___s_______%": "Enterprises_Created_Percent",
            "D___o___n___t_______e___n___t___r___e___p___r___i___s___e___s_______i___n___d___i___v___i___d___u___e___l___l___e___s_______N___o___m___b___r___e": "Individual_Enterprises_Number",
            "D___o___n___t_______e___n___t___r___e___p___r___i___s___e___s_______i___n___d___i___v___i___d___u___e___l___l___e___s_______%": "Individual_Enterprises_Percent",
            "C___o___d___e": "Code"
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

        # Specify the path where to save the modified CSV file
        output_csv_path = '../results/Modified_tableauDEN T1.csv'  # Replace with your desired output path

        # Save the modified DataFrame to the specified path
        df.to_csv(output_csv_path, index=False)

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
