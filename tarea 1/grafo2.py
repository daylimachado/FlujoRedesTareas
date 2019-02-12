import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_nodes_from([0,1,2,3,4])
pos = nx.spring_layout(G)  

G.add_edge(0,1)
G.add_edge(0,3)
G.add_edge(1,4)
G.add_edge(1,2)
G.add_edge(3,1)
G.add_edge(0,4)

nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color='r')


labels = {}
labels[0] = r'Markt'
labels[1] = r'Prod'
labels[2] = r'Cald'
labels[3] = r'Comerc'
labels[4] = r'Planif'

plt.axis('off')

nx.draw_networkx_labels(G, pos, labels, font_size=10)
plt.savefig("imagenes/Fig02.eps")

plt.show()

