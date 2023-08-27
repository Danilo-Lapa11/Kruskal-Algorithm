import pandas as pd
from geopy.distance import geodesic as gdist

class Graph:

	def __init__(self, vertices):
		self.V = vertices # qtd de vertices 
		self.graph = [] # Grafo

	def addEdge(self, tupla1, tupla2):

		# calculando a distância entre os pontos usando latitude e longitude de cada aeroporto 
		w = gdist((tupla1[1], tupla1[2]), (tupla2[1], tupla2[2])).kilometers # peso da aresta = distancia em Km arredondados
		self.graph.append([tupla1[0], tupla2[0], round(w)])

	# Encontrar o conjunto ao qual o vértice pertence
	def find(self, parent, i):

		if parent[i] != i:
			parent[i] = self.find(parent, parent[i])
		return parent[i]

	# Faz a união dos dois conjuntos por classificação
	def union(self, parent, rank, x, y):

		if rank[x] < rank[y]:
			parent[x] = y
		elif rank[x] > rank[y]:
			parent[y] = x
		else:
			parent[y] = x
			rank[x] += 1

	def KruskalMST(self):

		MST_result = []
		# Iterador para iterar a MST_result
		e = 0

		# Ordena as arestas usando a chave como o peso de cada aresta
		self.graph = sorted(self.graph, key=lambda item: item[2])

		parent = [] 
		rank = []

		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Iterador para as arestas ordenadas
		i = 0
		while i < (self.V - 1):
			# armazena os valores da aresta de menor peso 
			u, v, w = self.graph[i]
			i = i + 1

			x = self.find(parent, u)
			y = self.find(parent, v)

			# Verifica se a aresta gera um ciclo
			if x != y:
				e = e + 1
				MST_result.append([u, v, w])
				self.union(parent, rank, x, y)

		return MST_result

# Leitura da base de dados
db = pd.read_csv('airports.csv')

# Instância do grafo
g = Graph(len(db))

# Captação dos dados da base de dados e adição das arestas
for idx, row in db.iterrows():

	airport_1 = (idx , row['LATITUDE'], row['LONGITUDE'])
	index_airport = row['Numero_Aleatorio'] # Index destino da Aresta
	destiny_line = db.iloc[index_airport] # armazena o array da linha do Dataframe pelo index
	airport_2 = (index_airport, destiny_line[5], destiny_line[6])

	g.addEdge(airport_1, airport_2)

# Cria a MST com o algoritmo de Kruskal
MST = g.KruskalMST()

#Imprime a Árvore de Spanning Mínimo (MST) com nomes de aeroportos

for edge in MST:
    airport1_idx, airport2_idx, distance = edge
    airport1 = db.loc[airport1_idx, 'AIRPORT']
    airport2 = db.loc[airport2_idx, 'AIRPORT']
    print(f"{airport1} <--> {airport2}, Distance: {distance} km")
