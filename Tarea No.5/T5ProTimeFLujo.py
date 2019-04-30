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
    ds = pd.read_csv(adress, header=None)
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
 
def DibujaGrafo(G):    
    
    pesos=[]
    for edge in G.edges():            
        pesos.append(G.edges[edge]['weight']) 
    pesos[:] = [x/7*x/10 for x in pesos]
    
#    pos=nx.spring_layout(G)
    pos=nx.kamada_kawai_layout(G,scale=10)
    
    nx.draw_networkx_nodes(G, pos, node_size=400, node_color='#38ec1d', node_shape='o')   
    nx.draw_networkx_edges(G, pos, width=pesos,edge_color='black')   
    labels = {}
    for i in G.nodes:
        labels[i]=str(i)
    nx.draw_networkx_labels(G, pos, labels, font_size=15 )

    plt.axis('off')
    plt.savefig("fig5a.png",dpi=600)
    plt.savefig("fig5a.eps",dpi=600)
    df=pd.DataFrame(pos)
    df.to_csv("pos_grafo5.csv", index=None, header=None)
    return pos
    
#def GeneraPropiedades(G):   
#    dic={}  
#    Nodes=G.nodes;
#    dic["Nodo"]=Nodes
#    dic["DistGrado"]=[G.degree(i) for i in Nodes]
#    dic["CoefAgrup"]=[nx.clustering(G,i) for i in Nodes]
#    dic["CentCercania"]=[nx.closeness_centrality(G,i) for i in Nodes]
#    dic["CentCarga"]=[nx.load_centrality(G,i) for i in Nodes]
#    dic["ExcentCarga"]=[nx.eccentricity(G,i) for i in Nodes]
#    PageR=nx.pagerank(G,weight="capacity")
#    dic["PageR"]=[PageR[i] for i in Nodes]
#    
#    
#    
#    df=pd.DataFrame(dic)
#    df.to_csv("propiedadesnodosg1.csv", index=None)
    
def Todo(G):
    dic={"Fuente":[],
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
    df.to_csv("Todosvaloresg5.csv", index=None)   

def DibujarRes(G,pos,fuentes,sumideros): 
#    pos=nx.spring_layout(R)
    sinflujo=[]
    flowconflujo=[]
    conflujo=[]
    sinflujopesos=[]
    conflujopesos=[]
    maxi=0
    for edge in G.edges():            
        if G.edges[edge]['flow']==0:            
           sinflujo.append(edge)  
           sinflujopesos.append( G.edges[edge]['capacity'] )
        elif G.edges[edge]['flow']>0:                                                                                                                         
           conflujo.append(edge) 
           conflujopesos.append( G.edges[edge]['capacity'] ) 
           flowconflujo.append(G.edges[edge]['flow'] )
    flowconflujo[:] = [x+50 for x in flowconflujo] 
    for i in flowconflujo:
        if i>maxi:
            maxi=i
    sinflujopesos[:] = [x/10*x/5 for x in  sinflujopesos] 
    conflujopesos[:] = [x/10*x/5 for x in  conflujopesos] 
    nx.draw_networkx_nodes(G, pos, node_size=400, node_color='#38ec1d', node_shape='o')   
    nx.draw_networkx_nodes(G, pos,nodelist=fuentes, node_size=400, node_color='r', node_shape='o')   
    nx.draw_networkx_nodes(G, pos,nodelist=sumideros, node_size=400, node_color='b', node_shape='o')   
    nx.draw_networkx_edges(G, pos, edgelist=sinflujo, edge_color='#eef1f2', width= sinflujopesos,arrows=False)   
    nx.draw_networkx_edges(G, pos,edgelist=conflujo, edge_cmap=plt.cm.Reds, width=conflujopesos,edge_color=flowconflujo,edge_vmin=0,edge_vmax=maxi)  
    labels = {}
    for i in G.nodes:
        labels[i]=str(i)
    nx.draw_networkx_labels(G, pos, labels, font_size=15 )
    plt.axis('off')       
    plt.savefig("fig5b1.png",dpi=600)
    plt.savefig("fig5b1.eps",dpi=600)
    

G=lee_grafo("grafo5.csv")
GeneraPropiedades(G) 
DibujaGrafo(G)
Todo(G)   

R=edmonds_karp(G,4,9,capacity="weight")
pos = pd.read_csv("pos_grafo5.csv", header=None)
DibujarRes(R,pos,[4],[9])

print("fin")