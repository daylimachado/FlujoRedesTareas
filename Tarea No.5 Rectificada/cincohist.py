# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:10:17 2019

@author: lapi7
"""
import networkx as nx
import numpy as np 
import pandas as pd
import random as rdm
import matplotlib.pyplot as plt
from time import time
import datetime as dt
from scipy.stats import truncnorm
from networkx.algorithms.flow import boykov_kolmogorov
from networkx.algorithms.flow import maximum_flow
from networkx.algorithms.flow import edmonds_karp

def lee_grafo(nombre):
    ds = pd.read_csv(nombre, header=None)
    G = nx.from_pandas_adjacency(ds)  
    return G

def lee_propiedades (nombre):
    ds = pd.read_csv(nombre) 
    return ds
    

i=["grafo1.csv", "grafo2.csv", "grafo3.csv", "grafo4.csv", "grafo5.csv"]
g=[]
for x in i:
    G=lee_grafo(x) 
    
    dic={}  
    Nodes=G.nodes;
    dic["Nodo"]=Nodes
    dic["DistGrado"]=[G.degree(i) for i in Nodes]
    dic["CoefAgrup"]=[nx.clustering(G,i) for i in Nodes]
    dic["CentCercania"]=[nx.closeness_centrality(G,i) for i in Nodes]
    dic["CentCarga"]=[nx.load_centrality(G,i) for i in Nodes]
    dic["ExcentCarga"]=[round(nx.eccentricity(G,i), 2) for i in Nodes]
    PageR=nx.pagerank(G,weight="capacity")
    dic["PageR"]=[PageR[i] for i in Nodes]
    df=pd.DataFrame(dic)
    df.to_csv("propiedades"+str(x)+".csv", index=None)
    g.append("propiedades"+str(x)+".csv")

print (g)

j=["DistGrado","CoefAgrup","CentCercania","CentCarga", "ExcentCarga","PageR"] 
for y in g:
    H=lee_propiedades(y)  
    for i in j:   
        fig = plt.figure(figsize=(5, 5))
        ax = fig.add_subplot(1, 1, 1)
        his = ax.hist(H[i],bins=len(H[j]), facecolor='#8a36f8', alpha=0.75)
        ax.set_xlabel("Valores de " + i)
        ax.set_ylabel("Ocurencia")
#        plt.savefig("histograma"+ y + i + ".png", bbox_inches="tight", dpi=100)
        plt.savefig("histograma"+ y + i + ".eps", bbox_inches="tight", dpi=100)     
        plt.show()    

print("fin")



