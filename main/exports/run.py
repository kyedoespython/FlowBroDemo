from load_csv import get_csv
from transform_to import transform_db

df, csv_location = get_csv()

transform_db(df, csv_location)