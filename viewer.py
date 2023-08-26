import networkx as nx
import matplotlib.pyplot as plt
from main import *

G = nx.Graph()

# Adiciona as arestas no vizualizador
for edge in MST:
    # Para vizualizar o grafo completo -> g.graph
    # Para vizualizar a MST -> MST

    source, target, weight = edge
    G.add_edge(source, target, weight=weight)

# Cria um layout para os nós
pos = nx.spring_layout(G)

# Desenha o grafo
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightgreen', font_size=8)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()



