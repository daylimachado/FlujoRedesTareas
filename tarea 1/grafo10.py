# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:33:22 2019

@author: lapi7
"""

import matplotlib.pyplot as plt
import networkx as nx

G  =  nx . MultiDiGraph ()

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
##G.add_edge(5,1, weight=3)
##G.add_edge(5,1, weight=4)
#G.add_edge(1,3, weight=3)
#G.add_edge(1,3, weight=4)
#G.add_edge(5,3, weight=3)
#G.add_edge(5,3, weight=4)

medio=[(1,2),(2,3),(3,4),(4,5)]
ruta=[(1,2),(2,3),(3,4),(4,5)]

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=500, node_color='b', node_shape='o')

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

plt.savefig("imagenes/Fig10.eps")
plt.show()