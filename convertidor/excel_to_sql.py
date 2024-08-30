from config.db import conn
import pandas as pd

def covertir(table, path):
    df = pd.read_excel(path)
    df.to_sql(name=table, con=conn, if_exists='append', index=False)