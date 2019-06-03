# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:09:42 2019

@author: lapi7
"""

import matplotlib.pyplot as plot
import networkx as nx

G=nx.MultiGraph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_edge(1,2, weight=4)
G.add_edge(2,3, weight=3)
G.add_edge(2,3, weight=4)
G.add_edge(3,4, weight=3)
G.add_edge(3,4, weight=4)
G.add_edge(4,5, weight=3)
G.add_edge(4,5, weight=4)
G.add_edge(5,1, weight=3)
G.add_edge(5,1, weight=4)
G.add_edge(1,3, weight=3)
G.add_edge(1,3, weight=4)
G.add_edge(5,3, weight=3)
G.add_edge(5,3, weight=4)

node_A = {1}
node_S = {2}
node_E = {3}
node_V = {4}
node_C = {5}


green=[(1,2),(2,3),(3,4),(4,5),(5,1),(1,3),(5,3)]
yellow=[(1,2),(2,3),(3,4),(4,5),(5,1),(1,3),(5,3)]

pos = nx.random_layout(G, dim=2, center=None)  # Se puede usar el random en este caso
#pos = nx.circular_layout(G, dim=2, center=None)

plt.axis('off')

nx.draw_networkx_nodes(G, pos, nodelist=node_A, node_size=300, node_color='g', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=node_S, node_size=300, node_color='y', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=node_E, node_size=300, node_color='b', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=node_V, node_size=300, node_color='r', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=node_C, node_size=300, node_color='black', node_shape='o')


nx.draw_networkx_edges(G, pos, edgelist=green, width=3, alpha=0.5,
edge_color='g', style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=yellow,width=4, alpha=0.5,
edge_color='y')

plt.savefig("imagenes1/Fig09.eps")

plt.show()