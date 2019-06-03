import matplotlib.pyplot as plt
import networkx as nx

G  =  nx . DiGraph ()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)

node_r = {1}
node_nr = {2,3,4,5,6,7,8}
pos = nx.spring_layout(G)  # positions for all nodes



nx.draw_networkx_nodes(G, pos, nodelist=node_r, node_size=2000, node_color='r', node_shape='o')

nx.draw_networkx_nodes(G, pos, nodelist=node_nr, node_size=2000, node_color='y', node_shape='o')



labels = {}
labels[1] = r'$Markt$'
labels[2] = r'$Prod$'
labels[3] = r'$Cald$'
labels[4] = r'$Comerc$'
labels[5] = r'$Planif$'
labels[6] = r'$Planif$'
labels[7] = r'$Planif$'
labels[8] = r'$Planif$'


plt.axis('off')

nx.draw_networkx_labels(G, pos, labels, font_size=10)
plt.show()