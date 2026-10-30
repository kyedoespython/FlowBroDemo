import pandas as pd
import os
import sqlite3

def transform_db(df, csv_location):
    FILENAME = os.path.basename(csv_location)
    f_name, f_type = os.path.splitext(FILENAME)
    DB_NAME = f"{f_name}.db"

    Create_DB(DB_NAME, f_name, df)

def Create_DB(DB_NAME, f_name, df):
    conn = sqlite3.connect(DB_NAME)

    # if_exists -> delete, replace with new data, index=False -> gets rid of index's default
    df.to_sql(name=f_name, con=conn, if_exists="replace", index=False)

    conn.close()