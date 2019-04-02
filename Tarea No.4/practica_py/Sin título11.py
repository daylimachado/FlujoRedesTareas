# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:16:38 2019

@author: lapi7
"""

b = ['0.0656', '0.0713', '0.077',  '0.0827']
i = 0
arregl_densi = open("Arreglodensid.csv", "w+")
for valor in b:
    i += 1
    arregl_densi.write(valor)
    if i < len(b):
        arregl_densi.write(",")
arregl_densi.write("\r\n")
arregl_densi.close()