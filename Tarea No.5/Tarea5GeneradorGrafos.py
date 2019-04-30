# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:00:59 2019

@author: lapi7
"""

import networkx as nx
import pandas as pd
from scipy.stats import truncnorm
import matplotlib.pyplot as plt

def PrintGraph(G,w):  
    w[:] = [x/10*x/7 for x in w] #buen aporte para dibujar los weight con for reducido!
    pos=nx.spring_layout(G)
    #pos=nx.kamada_kawai_layout(G,scale=1.2)
    nx.draw_networkx_nodes(G, pos, node_size=400, node_color='#38ec1d', node_shape='o')   
    nx.draw_networkx_edges(G, pos, edge_color='black',width=w)   
    labels = {}
    for i in G.nodes:
        labels[i]=str(i)
    nx.draw_networkx_labels(G, pos, labels, font_size=15 )
    plt.axis('off')
#    plt.savefig("fig1.eps",dpi=200)
#    plt.savefig("fig1.png",dpi=200)
    
def Generador_grafo(n,k,p):
    #S=nx.watts_strogatz_graph(n, k, p,) 
    S=nx.connected_watts_strogatz_graph(n,k,p,tries=100, seed=None)
    scale = 2
    rang = 11
    size = S.number_of_edges()  
    e=S.edges(nbunch=None, data=True, default=None)   
    X = truncnorm(a=-rang/scale, b=+rang/scale, scale=scale).rvs(size=size)
    X = X.round().astype(int)+rang
    G=nx.Graph()
    count=0;
    for i in e:
        G.add_edge(i[0],i[1],capacity=X[count])
        count+=1
    df = pd.DataFrame()
    df = nx.to_pandas_adjacency(G, dtype=int, weight='capacity')
    df.to_csv("grafo5.csv", index=None, header=None)
    PrintGraph(S,X)

Generador_grafo(20,7,0.5)
