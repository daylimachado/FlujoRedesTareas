

import matplotlib.pyplot as plt
import networkx as nx

G = nx.MultiGraph ()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
E=[(1,2),(2,3),(3,4),(4,5),(5,1),(1,3),(5,3)]
for e in E:
    (u,v)=e
    G.add_edge(u,v,3)
    G.add_edge(u,v,4)
green=[(1,2),(2,3),(3,4),(4,5),(5,1),(1,3),(5,3)]
yelow=[(1,2),(2,3),(3,4),(4,5),(5,1),(1,3),(5,3)]
pos = nx.spring_layout(G)  
plt.axis('off')
nx.draw_networkx_nodes(G, pos ,node_size=400, node_color='black', node_shape='o')
nx.draw_networkx_edges(G, pos, edgelist=green, width=3, alpha=0.5,
edge_color='g', style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=yelow,width=4, alpha=0.5,
edge_color='y')
plt.savefig("imagenes/Fig08.eps")
plt.show()