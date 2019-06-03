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
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

data = pd.read_csv("1.csv")
    
figure, axes = plt.subplots(figsize=(10, 10))    
x=data["Media_A1bc"]
y=data["grafoN"]
xerr=data["Desvi_A1bc"]

axes.errorbar(x, y,  xerr=xerr, fmt='D',color="#932525", alpha=1, label="BC")
print(y)    
   
x=data["Media_A2mc"]
y=data["clicgrafoN"]
xerr=data["Desvi_A2mc"]

axes.errorbar(x, y, xerr=xerr, fmt='s',color="#129f10", alpha=1, label="MC")
print(y)    

x=data["Media_A3gc"]
y=data["digrafoN"]
xerr=data["Desvi_A3gc"]

axes.errorbar(x, y, xerr=xerr,fmt='8',color="#093ea8", alpha=1, label="GC")
print(y)    

x=data["Media_A4mf"]
y=data["digrafoN"]
xerr=data["Desvi_A4mf"]

axes.errorbar(x, y,xerr=xerr, fmt='>',color="#adcb18", alpha=1, label="MF")
print(y)    

x=data["Media_A5mst"]
y=data["grafoN"]
xerr=data["Desvi_A5mst"]
   
axes.errorbar(x, y,xerr=xerr, fmt='o',color="#ee9110", alpha=1, label="MST")
print(y)   

axes.set_ylabel("Vertices", fontsize=12, fontfamily="arial", fontweight="bold")
axes.set_xlabel("Tiempo de Ejecucion", fontsize=12, fontfamily="arial", fontweight="bold")
axes.legend()
plt.savefig("Imagenes/Fig2.eps")
plt.show()



figure, axes = plt.subplots(figsize=(10, 10)) 
    
x=data["Media_A1bc"]
y=data["grafoE"]
xerr=data["Desvi_A1bc"]
axes.errorbar(x, y, xerr=xerr, fmt='D',color="#932525", alpha=1, label="BC")
print(y)    
   
x=data["Media_A2mc"]
y=data["clicgrafoE"]
xerr=data["Desvi_A2mc"]
axes.errorbar(x, y, xerr=xerr, fmt='s',color="#129f10", alpha=1, label="MC")
print(y)    

x=data["Media_A3gc"]
y=data["digrafoE"]
xerr=data["Desvi_A3gc"]
axes.errorbar(x, y, xerr=xerr,fmt='8',color="#093ea8", alpha=1, label="GC")
print(y)    

x=data["Media_A4mf"]
y=data["digrafoE"]
xerr=data["Desvi_A4mf"]
axes.errorbar(x, y, xerr=xerr, fmt='>',color="#adcb18", alpha=1, label="MF")
print(y)    

x=data["Media_A5mst"]
y=data["grafoE"]
xerr=data["Desvi_A5mst"]
axes.errorbar(x, y,fmt='o',color="#ee9110", alpha=1, label="MST")
print(y)    

axes.set_ylabel("Aritas", fontsize=12, fontfamily="arial", fontweight="bold")
axes.set_xlabel("Tiempo de Ejecucion", fontsize=12, fontfamily="arial", fontweight="bold")
axes.legend()
plt.savefig("Imagenes/Fig3.eps")
plt.show()
    





