import pandas as pd
import tkinter as tk
from tkinter import messagebox

def process_csv_and_show_message():
    try:
        # Load the CSV file
        csv_path = '../results/_tableauACT T4.csv'  # Replace with your file path
        df = pd.read_csv(csv_path)

        # Renaming the first column to 'Category'
        df.rename(columns={df.columns[0]: "Category"}, inplace=True)

        # Check if both 'Ensemble' and 'Travaillent' exist in the Category column
        if 'Ensemble' in df['Category'].values and 'Travaillent' in df['Category'].values:
            # Function to combine two rows
            def combine_rows(row1, row2):
                combined_row = {}
                for col in df.columns:
                    if pd.api.types.is_numeric_dtype(df[col]):
                        combined_row[col] = row1[col] + row2[col]
                    else:
                        combined_row[col] = row1[col] if pd.notna(row1[col]) else row2[col]
                return combined_row

            # Locate and combine rows for 'Ensemble' and 'Travaillent'
            ensemble_row = df[df['Category'] == 'Ensemble'].iloc[0]
            travaillent_row = df[df['Category'] == 'Travaillent'].iloc[0]
            combined_row_data = combine_rows(ensemble_row, travaillent_row)
            combined_row_data['Category'] = 'Total_Ensemble_Travaillent'

            # Append and remove original rows
            df = pd.concat([df, pd.DataFrame([combined_row_data])], ignore_index=True)
            df = df[~df['Category'].isin(['Ensemble', 'Travaillent'])]

        # Clean and rename columns for clarity
        df.rename(columns={
            "2_______0_______0_______9": "Year_2009",
            "%": "Year_2009_Percent",
            "2_______0_______1_______4": "Year_2014",
            "%_______._______1": "Year_2014_Percent",
            "2_______0_______2_______0": "Year_2020",
            "%_______._______2": "Year_2020_Percent",
            "C___o___d___e": "Code"
        }, inplace=True)
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
        output_csv_path = '../results/_tableauACT T4-3.csv'  # Replace with your desired output path

        # Save the modified DataFrame
        df.to_csv(output_csv_path, index=False)

        # Show completion message
        messagebox.showinfo("Process Complete", f"Modified DataFrame saved at '{output_csv_path}'.")

    except Exception as e:
        # Print and show error message
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize Tkinter root
root = tk.Tk()
root.withdraw()  # We don't want a full GUI, so keep the root window from appearing

# Process the CSV and show the message box
process_csv_and_show_message()
