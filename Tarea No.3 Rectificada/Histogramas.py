# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:12:52 2019

@author: lapi7
"""

import random as rnd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as nup
import datetime as dt
import pandas as pd
import statistics as stats

data = pd.read_csv("1.csv")



plt.hist(nup.log1p(data["Media_A1bc"]), 5, facecolor='blue', alpha=0.5, edgecolor = 'black',  linewidth=1)
plt.ylabel('Frecuencia de ocurrencia')
plt.xlabel('Tiempo de Ejecucion')
plt.savefig("Imagenes/Histograma1.eps",bbox_inches='tight')
plt.show()


plt.hist(nup.log1p(data["Media_A2mc"]), 5, facecolor='red', alpha=0.5,  edgecolor = 'black',  linewidth=1)
plt.ylabel('Frecuencia de ocurrencia')
plt.xlabel('Tiempo de Ejecucion')
plt.savefig("Imagenes/Histograma2.eps",bbox_inches='tight')
plt.show()

plt.hist(nup.log1p(data["Media_A3gc"]), 5, facecolor='green', alpha=0.5, edgecolor = 'black',  linewidth=1)
plt.ylabel('Frecuencia de ocurrencia')
plt.xlabel('Tiempo de Ejecucion')
plt.savefig("Imagenes/Histograma3.eps",bbox_inches='tight')
plt.show()

plt.hist(nup.log1p(data["Media_A4mf"]), 5, facecolor='yellow', alpha=0.5, edgecolor = 'black',  linewidth=1)
plt.ylabel('Frecuencia de ocurrencia')
plt.xlabel('Tiempo de Ejecucion')
plt.savefig("Imagenes/Histograma4.eps",bbox_inches='tight')
plt.show()

plt.hist(nup.log1p(data["Media_A5mst"]), 5, facecolor='pink', alpha=0.5, edgecolor = 'black',  linewidth=1)
plt.ylabel('Frecuencia de ocurrencia')
plt.xlabel('Tiempo de Ejecucion')
plt.savefig("Imagenes/Histograma5.eps",bbox_inches='tight')
plt.show()
