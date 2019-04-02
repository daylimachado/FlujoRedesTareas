# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:58:37 2019

@author: lapi7
"""

import os
paquete=input("paquete a instalar")
paquete=str(paquete)
while True:
    try:
        codigo='pip install'+paquete
        os.system(codigo)
        print ('paquete instalado')
    except:
        print('error al instalar')
    continuar=input ('quiere instalar otro')
    continuar=str(continuar)     
    if continuar=='S' or continuar=='s':
        paquete=input('new paquete a instalar')
        paquete=str(paquete)
    else:
        break
print('fin')    