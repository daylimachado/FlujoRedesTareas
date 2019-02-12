# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:39:04 2019

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
G.add_edge(1,2, weight=5)
G.add_edge(2,3, weight=3)
G.add_edge(2,3, weight=4)
G.add_edge(2,4, weight=3)

G.add_edge(2,5, weight=3)
G.add_edge(3,2, weight=4)
G.add_edge(3,2, weight=3)


y=[(1,2),(2,3),(3,2)]
g=[(1,2),(2,3),(3,2)]
r=[(1,2),(2,4),(2,5)]

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=400, node_color='b', node_shape='o')

nx.draw_networkx_edges(G, pos, edgelist=y, width=10, alpha=0.2,
edge_color='y', style='dashed')

nx.draw_networkx_edges(G, pos, edgelist=g, width=6, alpha=0.5,
edge_color='g')

nx.draw_networkx_edges(G, pos, edgelist=r, width=2, alpha=0.8,
edge_color='r')

labels = {}
labels[1] = r'1'
labels[2] = r'2'
labels[3] = r'Lab'
labels[4] = r'3'
labels[5] = r'4'


plt.axis('off')

nx.draw_networkx_labels(G, pos, labels, font_size=10)

plt.savefig("imagenes/Fig11.eps")
plt.show()