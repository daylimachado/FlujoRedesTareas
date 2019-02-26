# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:03:20 2019

@author: lapi7
"""

import networkx as nx
import matplotlib.pyplot as plot


A=nx.Graph()
A.add_edges_from([('Dr.FL','Dra.AA'),('Dr.FL','Dra.YR'),
                  ('Dr.FL','Dr.RS'),('Dr.FL','Dra.ES'),
                  ('Dra.YR','Dr.VB'),('Dra.YR','Dr.RR'),
                  ('Dra.YR','Dr.RS'),('Dra.AA','Dra.IM'),
                  ('Dra.AA','Dr.RR'),('Dra.IM','Dr.VB'),
                  ('Dra.IM','Dra.AS'),('Dra.IM','Dr.RS'),
                  ('Dra.IM','Dr.VB'),('Dr.VB','Dr.RS'),
                  ('Dra.AS','Dr.VB'),('Dra.AS','Dr.RR'),
                  ('Dra.AS','Dr.RS'),('Dra.ES','Dr.RR'),
                  ('Dra.AA','Dra.ES'),('Dra.IM','Dra.ES')])



posicion=nx.kamada_kawai_layout(A, dist=None, pos=None, weight='weight', scale=0.5, center=None, dim=2)
nx.draw_networkx_nodes(A,posicion, node_size=1700, node_color=range(9),cmap=plot.cm.Blues)
nx.draw_networkx_edges(A,posicion, width=2,edge_color='#46267d')
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial',
                        font_color='#846c16', font_weight='bold')

plot.axis('off')
plot.savefig("Graf2_kamada_kawai_layout.eps")
plot.show(A)