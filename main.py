import pandas as pd
from geopy.distance import geodesic as gdist

class Graph:

	def __init__(self, vertices):
		self.V = vertices # qtd de vertices 
		self.graph = []

	# Function to add an edge to graph
	def addEdge(self, p1, lat1, lon1, p2, lat2, lon2):
		
		# # calculando a distância entre os pontos usando latitude e longitude de cada aeroporto 
		w = gdist((lat1, lon1), (lat2, lon2)).kilometers

		self.graph.append([p1, p2, round(w)])


# Leitura da base de dados
db = pd.read_csv('airports.csv')

# Instância do grafo
g = Graph(len(db))

# # Captação dos dados da base de dados
# for idx, row in db.iterrows():
# 	print((row['AIRPORT'], row['LATITUDE'], row['LONGITUDE']))


g.addEdge('Yakutat', 59.50336056, -139.6602261, 'Yuma MCAS-Yuma International', 32.65658333, -114.6059722)
g.addEdge('Eglin Air Force Base', 30.48325, -86.5254, 'Northwest Arkansas Regional', 36.28186944, -94.30681111)
g.addEdge('Yellowstone', 44.68839917, -111.1176375, 'Yuma MCAS-Yuma International', 32.65658333, -114.6059722)


print(g.graph)


