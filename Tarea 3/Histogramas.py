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
plt.figure(figsize=(12, 6))

plt.subplot(321)
x = plt.hist(data["Media_A1bc"], 5, facecolor='blue', alpha=0.5)

plt.subplot(322)
x = plt.hist(data["Media_A2mc"], 5, facecolor='red', alpha=0.5)
print(x)
plt.subplot(323)
x = plt.hist(data["Media_A3gc"], 5, facecolor='green', alpha=0.5)

plt.subplot(324)
x = plt.hist(data["Media_A4mf"], 5, facecolor='yellow', alpha=0.5)

plt.subplot(325)
x = plt.hist(data["Media_A5mst"], 5, facecolor='pink', alpha=0.5)


plt.subplots_adjust(left=0.15)
plt.savefig("Imagenes/Fig01.eps")
plt.show()
