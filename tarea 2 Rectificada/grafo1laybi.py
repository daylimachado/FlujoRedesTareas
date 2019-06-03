# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:34:52 2019
@author: Dayli
"""
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_node(2)
G.add_node(4)

G.add_node(1)
G.add_node(3)
G.add_node(5)

G.add_edges_from([(1,2), (3,4)])
G.add_edges_from([(2,3), (4,5)])

labels = {}
labels[1] = r'H3C'
labels[2] = r'H2C'
labels[3] = r'CH2'
labels[4] = r'H2C'
labels[5] = r'CH3'

pos = nx.bipartite_layout(G, {1,3,5},align='horizontal', scale=0.05)

nx.draw_networkx_nodes(G,pos, node_size=800, node_color='b')
nx.draw_networkx_edges(G,pos, width=3)
nx.draw_networkx_labels(G,pos, labels, font_size=10)
plt.axis('off')
plt.savefig("imagenes1/Fig01.eps")

plt.show()


