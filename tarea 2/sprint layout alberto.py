# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:15:48 2019

@author: lapi7
"""

import networkx as nx
import matplotlib.pyplot as plot

A=nx.Graph()
A.add_edges_from([('R1','Sw1'),('Sw1','Sw2'),
                  ('Sw1','Sw3'),('Sw2','Pc2'),('Sw2','Pc3'),
                  ('Sw3','Pc4'),('Sw3','Pc5')])


sw=['R1','Sw1','Sw2','Sw3']
pc=['Pc2','Pc3','Pc4','Pc5']
swc=[('R1','Sw1'),('Sw1','Sw2'),('Sw1','Sw3')]
pcc=[('Sw2','Pc2'),('Sw2','Pc3'),('Sw3','Pc4'),('Sw3','Pc5')]

posicion=nx.spring_layout(A, k=1, iterations=400, threshold=0.0001, weight='weight', scale=1)

nx.draw_networkx_nodes(A,posicion, node_size=800, node_shape='s', nodelist=sw, node_color='#c9b323')
nx.draw_networkx_nodes(A,posicion, node_size=800, node_shape='o', nodelist=pc, node_color='#c68282')
nx.draw_networkx_edges(A,posicion, width=4, edgelist=swc,style='dashed')
nx.draw_networkx_edges(A,posicion, width=2, edgelist=pcc)
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial')


plot.axis('off')
plot.figure(figsize=(1,1)) 
plot.savefig("Graf1_spring_layout.eps")
plot.show(A)