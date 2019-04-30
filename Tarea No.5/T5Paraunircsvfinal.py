# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:17:23 2019

@author: lapi7
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:37:07 2019

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

def lee_grafo(adress):
    ds = pd.read_csv((adress+".csv"), header=None)
    G = nx.from_pandas_adjacency(ds)  
    return G

def calcula_tiempo(G,a,b):
    start_time=time()          
#    fm=nx.maximum_flow(G, a, b,capacity="weight")
    for i in range (100):
        fm=edmonds_karp(G, a, b,capacity="weight")
        print(i)
    time_elapsed = time() - start_time
    
    return time_elapsed
 

def Todo(G,nombre):
    dic={"Grafo":[],
         "Fuente":[],
         "Sumidero":[] , 
         "Mediatime":[],
         "Medianatime":[],
         "Stdtime":[],
         "Flujomaximo":[],
         "DistGrado":[],
         "CoefAgrup":[],
         "CentCercania":[],
         "CentCarga":[],
         "ExcentCarga":[],
         "PageR":[]}
    
    Nodes=G.nodes;
    for i in Nodes:
        for j in Nodes:          
            if i!=j: 
                t=[]                    
                for k in range(10):
                   t.append(calcula_tiempo(G,i,j))                 
                dic["Grafo"].append(nombre)
                dic["Fuente"].append(i)    
                dic["Sumidero"] .append(j)  
                dic["Mediatime"].append(np.mean(t))    
                dic["Medianatime"].append(np.median(t))    
                dic["Stdtime"].append(np.std(t))
                dic["Flujomaximo"].append(nx.maximum_flow_value(G,i,j,capacity="weight"))
               
                dic["DistGrado"].append(G.degree(i))
                dic["CoefAgrup"].append(nx.clustering(G,i))
                dic["CentCercania"].append(nx.closeness_centrality(G,i))
                dic["CentCarga"].append(nx.load_centrality(G,i))
                dic["ExcentCarga"].append(nx.eccentricity(G,i))
                PageR=nx.pagerank(G,weight="capacity")
                dic["PageR"].append(PageR[i])
    
    
    df=pd.DataFrame(dic)
    df.to_csv("CSVunido.csv", index=None, mode="a")   


i=["grafo1", "grafo2", "grafo3", "grafo4", "grafo5"]
for x in i:
    print (x)
    G=lee_grafo(x)
    Todo(G,x)   
   

print("fin")