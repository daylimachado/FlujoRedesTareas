import matplotlib.pyplot as plt
import networkx as nx

G  =  nx.DiGraph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)

node_a = {1,2}
node_b = {3,4}
node_ab = {5,6}
node_o = {7,8}
#Se cambiaron los layout y el mejor resultado fue con el circular
#pos = nx.spring_layout(G) 
pos = nx.circular_layout(G,dim=2,scale=1, center=(0,0)) 
#pos = nx.shell_layout(G)
#pos = nx.rescale_layout(G)

G.add_edges_from([(1,1), (8,1), (7,1), (2,1)])# Cada nodo es reflexivo pero no me sale la flechita
G.add_edges_from([(2,2), (8,2)])#igualmente no sale el reflexivo en si mismo
G.add_edges_from([(3,3), (8,3), (7,3), (4,3)])#no sale el reflexivo en si mismo
G.add_edges_from([(4,4), (8,4)])#es reflexivo en si mismo
G.add_edges_from([(5,5), (1,5), (2,5), (3,5), (4,5), (6,5), (7,5), (8,5)])# es reflexivo en si mismo
G.add_edges_from([(6,6), (4,6), (8,6), (2,6)])
G.add_edges_from([(7,7), (8,7)])
G.add_edges_from([(8,8)])

nx.draw_networkx_nodes(G, pos, nodelist=node_a, node_size=800, node_color='g', node_shape='o', alpha=0.3)
nx.draw_networkx_nodes(G, pos, nodelist=node_b, node_size=800, node_color='y', node_shape='o', alpha=0.3)
nx.draw_networkx_nodes(G, pos, nodelist=node_ab, node_size=800, node_color='b', node_shape='o', alpha=0.3)
nx.draw_networkx_nodes(G, pos, nodelist=node_o, node_size=800, node_color='r', node_shape='o', alpha=0.8)
#nx.draw_networkx_nodes(G, pos, nodelist=node_o, node_size=800, node_color='r', node_shape='on', alpha=0.1)
labels = {}
labels[1] = r'A+'
labels[2] = r'A-'
labels[3] = r'B+'
labels[4] = r'B-'
labels[5] = r'AB+'
labels[6] = r'AB-'
labels[7] = r'O+'
labels[8] = r'O-'
nx.draw_networkx_labels(G, pos, labels, font_size=10)

#pos1 = pos
#
#for key, value in G.edges:   
#    print("(", pos[key][0] - 0.5, ", ", pos[key][1] - 0.5, ")\n")
#    pos1[key][0] = pos1[key][0] + 0.1
#    pos1[key][1] = pos1[key][1]
#
  
nx.draw_networkx_edges(G, pos, width=2, alpha=1, edge_color='black', scale=0.5 )
#print(pos)
plt.axis('on')
plt.savefig("imagenes1/Fig06.eps")
plt.show()

