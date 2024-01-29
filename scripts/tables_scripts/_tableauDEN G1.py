import pandas as pd
import tkinter as tk
from tkinter import messagebox

def process_csv_and_show_message():
    try:
        # Load the CSV file
        csv_path = '../results/_tableauDEN G1.csv'  # Replace with the path to your CSV file
        df = pd.read_csv(csv_path)

        # Renaming columns for clarity and QGIS compatibility
        year_columns = [f"Year_{year}" for year in range(2013, 2023)]  # Prefixing with "Year_" to avoid starting with a number
        df.columns = ['Category'] + year_columns + ['Code']

        # Remove spaces in numbers and convert them to integers or floats
        for col in df.columns:
            if df[col].dtype == object: 
                df[col] = df[col].apply(lambda x: ''.join(str(x).split()) if isinstance(x, str) else x)
                try:
                    df[col] = pd.to_numeric(df[col], errors='ignore')
                except ValueError:
                    pass

        # Specify the path where to save the modified CSV file
        output_csv_path = '../results/_tableauDEN G1-2.csv'  # Replace with your desired output path

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
