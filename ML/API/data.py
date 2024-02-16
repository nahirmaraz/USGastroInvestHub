import pandas as pd

# Cargar DataFrames desde archivos ubicados en la carpeta datasets_API.
cities_FL = pd.read_parquet('datasets_API/cities_FL.parquet')
std_dfs = pd.read_pickle('API/datasets_API/std_dfs.pkl')