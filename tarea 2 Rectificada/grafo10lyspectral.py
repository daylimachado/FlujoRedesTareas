import matplotlib.pyplot as plt
import networkx as nx

G=nx.MultiDiGraph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_edge(1,2, weight=3)
G.add_edge(1,2, weight=4)
G.add_edge(2,3, weight=3)
G.add_edge(2,3, weight=4)
G.add_edge(3,4, weight=3)
G.add_edge(3,4, weight=4)
G.add_edge(4,5, weight=3)
G.add_edge(4,5, weight=4)

medio=[(1,2),(2,3),(3,4),(4,5)]
ruta=[(1,2),(2,3),(3,4),(4,5)]

#pos = nx.spring_layout(G)
#pos=nx.kamada_kawai_layout(G, dist=None, pos=None, weight='weight', scale=0.5, center=None, dim=2)

pos=nx.spectral_layout(G, weight='weight', scale=1, center=None, dim=2)

nx.draw_networkx_nodes(G, pos, node_size=800, node_color='#ecf815', node_shape='o')

nx.draw_networkx_edges(G, pos, edgelist=medio, width=6, alpha=0.8,
edge_color='black', style='dashed')

nx.draw_networkx_edges(G, pos, edgelist=ruta,width=4, alpha=0.5,
edge_color='r')

labels = {}
labels[1] = r'Mat'
labels[2] = r'Hab'
labels[3] = r'Monty'
labels[4] = r'Torr'
labels[5] = r'Sing'

plt.axis('off')

nx.draw_networkx_labels(G, pos, labels, font_size=10)

plt.savefig("imagenes1/Fig10.eps")
plt.show()