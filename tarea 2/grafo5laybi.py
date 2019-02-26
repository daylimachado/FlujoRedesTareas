import matplotlib.pyplot as plt
import networkx as nx

G  =  nx . DiGraph ()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(6)

G.add_node(4)
G.add_node(5)

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(5,6)
G.add_edge(3,6)

G.add_cycle([5,3])

labels = {}
labels[1] = r'$Op1$'
labels[2] = r'$Op2$'
labels[3] = r'$Op3$'
labels[4] = r'$Op4$'
labels[5] = r'$Op5$'
labels[6] = r'$Op6$'

pos = nx.bipartite_layout(G, {4,5},align='horizontal', scale=0.7)

nx.draw_networkx_nodes(G, pos, node_size=500, node_color='r', node_shape='o')
nx.draw_networkx_edges(G, pos, width=2, alpha=0.8, edge_color='black')
nx.draw_networkx_labels(G, pos, labels, font_size=10)

plt.axis('off')

plt.savefig("imagenes1/Fig05.eps")

plt.show()
