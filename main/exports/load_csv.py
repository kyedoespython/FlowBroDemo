from transform_to import transform_db

import pandas as pd
import os

def get_csv():
    csv_location = input("enter the path to your csv file: ")
    return validate_csv_location(csv_location)

def validate_csv_location(csv_location):
    if os.path.exists(csv_location):
        df = pd.read_csv(csv_location)
        display_row__path(df, csv_location)

        return df, csv_location
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Error: check your path: ({csv_location})\n")

        return None, None

def display_row__path(cleaned_csv, csv_location):
    os.system("cls" if os.name == "nt" else "clear")
    print("#" * 90)
    print(f"File Selected: {os.path.basename(csv_location)}\n[located at]: {csv_location}")
    print("#" * 90)
    print(f"Total Rows: {len(cleaned_csv)}\n")
    display_columns_vertical(cleaned_csv)

def display_columns_vertical(df):
    for i, column in enumerate(df.columns):
        print(f"{i}: {column}")