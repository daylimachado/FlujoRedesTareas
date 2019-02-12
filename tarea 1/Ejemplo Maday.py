# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:08:34 2019

@author: Dayli
"""

import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . MultiGraph ()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)


G.add_edge(4,3, weight=3)
G.add_edge(4,3, weight=5)
G.add_edge(3,7, weight=4)
G.add_edge(3,7, weight=3)
G.add_edge(1,5)
G.add_edge(5,3)
G.add_edge(3,6)
G.add_edge(6,2)

blue=[(4,3),(3,7),(1,5),(5,3),(3,6),(6,2)]
red=[(4,3),(3,7)]

pos = {1:(400, 400), 2:(300,300), 3:(100, 100), 4:(500,500), 5:(650,650),6:(250,500), 7:(100
       ,700), 8:(500, 300), 9:(700,300)}

nx.draw_networkx_nodes(G, pos ,node_size=400, node_color='y', node_shape='o')


nx.draw_networkx_edges(G, pos, edgelist=blue,width=6, alpha=0.5,
edge_color='b', style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=red,width=4, alpha=0.5,
edge_color='r')

#labels = {}
#labels[1] = r'$Presa$'

labels = {}
labels[1] = r'$R1$'
labels[2] = r'$R2$'
labels[3] = r'$S$'
labels[4] = r'$O$'
labels[5] = r'$O$'
labels[6] = r'$O$'
labels[7] = r'$O$'


plt.axis('off')

nx.draw_networkx_labels(G, pos, labels, font_size=10)


#nx.draw_networkx_labels(G, pos, labels, font_size=12)




plot.xlim(20,800)
plot.axis('off')
plot.savefig("8.eps")

plot.show()