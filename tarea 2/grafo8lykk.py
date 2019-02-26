# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:09:39 2019

@author: lapi7
"""

import matplotlib.pyplot as plot
import networkx as nx

G  =  nx.MultiGraph ()

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
G.add_edge(5,1, weight=3)
G.add_edge(5,1, weight=4)
G.add_edge(1,3, weight=3)
G.add_edge(1,3, weight=4)
G.add_edge(5,3, weight=3)
G.add_edge(5,3, weight=4)

green=[(1,2),(2,3),(3,4),(4,5),(5,1),(1,3),(5,3)]
yellow=[(1,2),(2,3),(3,4),(4,5),(5,1),(1,3),(5,3)]

pos = nx.kamada_kawai_layout(G, dist=None, pos=None, weight='weight', scale=0.5, center=None, dim=2)

plt.axis('off')

nx.draw_networkx_nodes(G, pos ,node_size=400, node_color='r', node_shape='o')

nx.draw_networkx_edges(G, pos, edgelist=green, width=3, alpha=0.5,
edge_color='g', style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=yellow,width=4, alpha=0.5,
edge_color='y')

plt.savefig("imagenes1/Fig08.eps")

plt.show()