# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:23:54 2019

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

a= {1}
b= {2}
c= {3}
d= {4}
e= {5}

G.add_edge(1,2, weight=3)
G.add_edge(1,2, weight=4)
G.add_edge(1,2, weight=5)
G.add_edge(2,3, weight=3)
G.add_edge(2,3, weight=4)
G.add_edge(2,3, weight=4)
G.add_edge(3,4, weight=3)
G.add_edge(3,4, weight=3)
G.add_edge(3,4, weight=3)
G.add_edge(4,5, weight=3)
G.add_edge(4,5, weight=3)
G.add_edge(4,5, weight=3)


y=[(1,2),(2,3),(3,4),(4,5)]
g=[(1,2),(2,3),(3,4),(4,5)]
r=[(1,2),(2,3),(3,4),(4,5)]

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, nodelist=a, node_size=300, node_color='black', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=b, node_size=300, node_color='y', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=c, node_size=300, node_color='b', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=d, node_size=300, node_color='r', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=e, node_size=300, node_color='g', node_shape='o')

nx.draw_networkx_edges(G, pos, edgelist=y, width=8, alpha=1,
edge_color='y', style='dashed')

nx.draw_networkx_edges(G, pos, edgelist=g, width=6, alpha=0.5,
edge_color='g')

nx.draw_networkx_edges(G, pos, edgelist=r, width=2, alpha=0.8,
edge_color='r')

plt.axis('off')

plt.savefig("imagenes/Fig12.eps")
plt.show()
