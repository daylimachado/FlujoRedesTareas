import matplotlib.pyplot as plt
import networkx as nx

G=nx.MultiGraph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)

node_o = {4,5,6,7}
node_r = {1,2,3}

G.add_edge(4,3, weight=3)
G.add_edge(4,3, weight=5)
G.add_edge(3,7, weight=3)
G.add_edge(3,7, weight=5)
G.add_edge(1,5)
G.add_edge(5,3)
G.add_edge(3,6)
G.add_edge(6,2)

blue=[(4,3),(3,7),(1,5),(5,3),(3,6),(6,2)]
red=[(4,3),(3,7)]

labels = {}
labels[1] = r'R1'
labels[2] = r'R2'
labels[3] = r'S'
labels[4] = r'O'
labels[5] = r'O'
labels[6] = r'O'
labels[7] = r'O'

pos=nx.spring_layout(G, k=0.1, iterations=300, threshold=0.0001, weight='weight', scale=1)
nx.draw_networkx_nodes(G, pos, nodelist=node_o, node_size=600, node_color='b', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=node_r, node_size=600, node_color='y', node_shape='s')

nx.draw_networkx_edges(G, pos, edgelist=blue,width=6, alpha=0.5, edge_color='b', style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=red,width=6, alpha=0.5, edge_color='r')

nx.draw_networkx_labels(G, pos, labels, font_size=10)

plt.axis('on')
plt.savefig("imagenes1/Fig07.eps")
plt.show()