import pandas as pd
from geopy.distance import geodesic as gdist

# Leitura da base de dados
db = pd.read_csv('Kruskal-Algorithm/airports.csv')

# Captação dos dados da base de dados
for idx, row in db.iterrows():
    print((row['AIRPORT'], row['LATITUDE'], row['LONGITUDE']))






# vou add isso dps 

# # calculando a distância entre os pontos usando lat e lon de cada aeroporto 
# distance = gdist((39.04614278, -84.6621725), (32.84711389, -96.85177222)).kilometers

