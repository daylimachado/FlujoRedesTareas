# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:23:01 2019

@author: lapi7
"""

import random as rnd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as nup
import datetime as dt
import pandas as pd
import statistics as stats

def Scatter_Nodos(nombre):
    colors = ["y","r","b","black","g"] 
    data = pd.read_csv(nombre)
    markers=["d","s","*","8","x"]   
    
    x=data["Media_A1bc"]
    y=data["grafoN"]
    area=300
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="d")
    print(y)    
   
    x=data["Media_A2mc"]
    y=data["clicgrafoN"]
    area=300
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="s")
    print(y)    

    x=data["Media_A3gc"]
    y=data["digrafoN"]
    area=300
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="*")
    print(y)    
    
    x=data["Media_A4mf"]
    y=data["digrafoN"]
    area=300
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="8")
    print(y)    
    
    x=data["Media_A5mst"]
    y=data["grafoN"]
    area=300
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="x")
    print(y)    
    
    
    plt.savefig("Imagenes/Fig2.eps")
    plt.show()
    
Scatter_Nodos("1.csv")


def Scatter_Edges(nombre):
    colors = ["y","r","b","black","g"] 
    data = pd.read_csv(nombre)
    markers=["d","s","*","8","x"]   
    
    x=data["Media_A1bc"]
    y=data["grafoE"]
    area=300
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="d")
    print(y)    
   
    x=data["Media_A2mc"]
    y=data["clicgrafoE"]
    area=300
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="s")
    print(y)    

    x=data["Media_A3gc"]
    y=data["digrafoE"]
    area=300
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="*")
    print(y)    
    
    x=data["Media_A4mf"]
    y=data["digrafoE"]
    area=300
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="8")
    print(y)    
    
    x=data["Media_A5mst"]
    y=data["grafoE"]
    area=300
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker="x")
    print(y)    
    
    
    plt.savefig("Imagenes/Fig3.eps")
    plt.show()
    
Scatter_Edges("1.csv")




