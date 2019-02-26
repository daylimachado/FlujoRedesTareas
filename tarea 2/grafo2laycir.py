# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:25:28 2019

@author: Dayli
"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_nodes_from([0,1,2,3,4])

G.add_edge(0,1)
G.add_edge(0,3)
G.add_edge(1,4)
G.add_edge(1,2)
G.add_edge(3,1)
G.add_edge(0,4)
G.add_edge(2,4)

labels = {}
labels[0] = r'Markt'
labels[1] = r'Prod'
labels[2] = r'Cald'
labels[3] = r'Comerc'
labels[4] = r'Planif'

pos = nx.circular_layout(G, scale=0.5)
#pos = nx.spring_layout(G, scale=0.5)  

nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='#756b6b', node_shape='o')
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='black')
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='white')



plt.axis('off')

plt.savefig("imagenes1/Fig02.eps")

plt.show()
