import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_nodes_from([1,2,3,4])

node_b = {1}
node_a = {2}
node_n = {3}
node_au = {4}

pos = nx.spring_layout(G)  
#pos = {1:(5000,8020), 2:(7150,6620), 3:(6675, 5180), 4:(5475,8200)}

G.add_edges_from([(1,1), (1,2), (1,3), (1,4)])# Cada nodo es reflexivo pero no me sale la flechita
G.add_edges_from([(2,2), (2,1), (2,3), (2,4)])#igualmente no sale el reflexivo en si mismo
G.add_edges_from([(3,3), (3,1), (3,2), (3,4)])#no sale el reflexivo en si mismo
G.add_edges_from([(4,4), (4,1), (4,3), (4,2)])#es reflexivo en si mismo

nx.draw_networkx_nodes(G, pos, nodelist=node_b, node_size=3000, node_color='g', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=node_a, node_size=3000, node_color='y', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=node_n, node_size=3000, node_color='b', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=node_au, node_size=3100, node_color='r', node_shape='o')

nx.draw_networkx_edges(G, pos, width=1, alpha=0.8, edge_color='black', )

labels = {}
labels[1] = r'Blanco'
labels[2] = r'Asiatico'
labels[3] = r'Negro'
labels[4] = r'Australoide'

plt.axis('off')

nx.draw_networkx_labels(G, pos, labels, font_size=10)

#plt.xlim (2000,16000)
plt.autoscale (enable=true, axis='both')
plt.savefig("imagenes/Fig03.eps")
#nx.draw(G)
plt.show()