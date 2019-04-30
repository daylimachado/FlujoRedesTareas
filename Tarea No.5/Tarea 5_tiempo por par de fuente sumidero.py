# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:46:18 2019

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
    fm=edmonds_karp(G, a, b,capacity="weight")
    time_elapsed = time() - start_time 
    return time_elapsed

def DibujarRes(G,pos,fuentes,sumideros): 
#    pos=nx.spring_layout(R)
    negros=[]
    flowrojos=[]
    rojos=[]
    negrospesos=[]
    rojospesos=[]
    maxi=0
    for edge in G.edges():            
        if G.edges[edge]['flow']==0:            
           negros.append(edge)  
           negrospesos.append( G.edges[edge]['capacity'] )
        else:                                                                                                                        
           rojos.append(edge) 
           rojospesos.append( G.edges[edge]['capacity'] ) 
           flowrojos.append(G.edges[edge]['flow'] )
    flowrojos[:] = [x+100 for x in flowrojos] 
    for i in flowrojos:
        if i>maxi:
            maxi=i
    negrospesos[:] = [x/10*x/7 for x in  negrospesos] 
    rojospesos[:] = [x/10*x/7 for x in  rojospesos] 
    nx.draw_networkx_nodes(G, pos, node_size=200, node_color='y', node_shape='o')   
    nx.draw_networkx_nodes(G, pos,nodelist=fuentes, node_size=200, node_color='r', node_shape='o')   
    nx.draw_networkx_nodes(G, pos,nodelist=sumideros, node_size=200, node_color='b', node_shape='o')   
    nx.draw_networkx_edges(G, pos, edgelist=negros, edge_color='g', width= negrospesos,arrows=False)   
    nx.draw_networkx_edges(G, pos,edgelist=rojos, edge_cmap=plt.cm.Blues, width=rojospesos,edge_color=flowrojos,edge_vmin=0,edge_vmax=maxi)  
    labels = {}
    for i in G.nodes:
        labels[i]=str(i)
    nx.draw_networkx_labels(G, pos, labels, font_size=8 )
    plt.axis('off')       
    plt.savefig("res1.png",dpi=500)
    
    
def DibujaGrafo(G):    
    #pos=nx.kamada_kawai_layout(G,scale=1.2)
    pesos=[]
    for edge in G.edges():            
        pesos.append(G.edges[edge]['weight']) 
    pesos[:] = [x/10*x/7 for x in pesos]
    pos=nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=400, node_color='#38ec1d', node_shape='o')   
    nx.draw_networkx_edges(G, pos, width=pesos,edge_color='black')   
    labels = {}
    for i in G.nodes:
        labels[i]=str(i)
    nx.draw_networkx_labels(G, pos, labels, font_size=15 )
#    nx.draw_networkx_edge_labels(G, pos, font_size=7, label_pos=.5)
    plt.axis('off')
    plt.savefig("fig1a.png",dpi=500)
    plt.savefig("fig1a.eps",dpi=500)
    df=pd.DataFrame(pos)
    df.to_csv("pos_grafo1.csv", index=None, header=None)
    return pos
    
def GeneraPropiedades(G):   
    dic={}  
    Nodes=G.nodes;
    dic["Nodo"]=Nodes
    dic["DistGrado"]=[G.degree(i) for i in Nodes]
    dic["CoefAgrup"]=[nx.clustering(G,i) for i in Nodes]
    dic["CentCercania"]=[nx.closeness_centrality(G,i) for i in Nodes]
    dic["CentCarga"]=[nx.load_centrality(G,i) for i in Nodes]
    dic["ExcentCarga"]=[nx.eccentricity(G,i) for i in Nodes]
    PageR=nx.pagerank(G,weight="capacity")
    dic["PageR"]=[PageR[i] for i in Nodes]
    df=pd.DataFrame(dic)
    df.to_csv("propiedades_nodog1.csv", index=None)
    
def Time(G):
    dic={"Fuente":[], "Sumidero":[] , "Mediatime":[], "Medianatime":[], "Stdtime":[],"Flujomaximo":[]}  
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
    df=pd.DataFrame(dic)
    df.to_csv("TiempoyFlujog1.csv", index=None)   

#def PrintGrafoResult(fm):    
#    #pos=nx.kamada_kawai_layout(G,scale=1.2)
#    pos=nx.spring_layout(fm)
#    nx.draw_networkx_nodes(fm, pos, node_size=400, node_color='#38ec1d', node_shape='o')   
#    nx.draw_networkx_edges(fm, pos, edge_color='black')   
#    labels = {}
#    for i in fm.nodes:
#        labels[i]=str(i)
#    nx.draw_networkx_labels(fm, pos, labels, font_size=15 )
#    nx.draw_networkx_edge_labels(fm, pos, font_size=7, label_pos=.5)
#    plt.axis('off')
#    plt.savefig("fig1b.png",dpi=500)
#    plt.savefig("fig1b.eps",dpi=500)


G=lee_grafo("grafo1.csv")



GeneraPropiedades(G) 
#DibujaGrafo(G)
Time(G)   

print("aquí")

R=edmonds_karp(G, 2, 9,capacity="weight")
pos = pd.read_csv("pos_grafo1.csv", header=None)
DibujarRes(R,pos,[2],[9])












