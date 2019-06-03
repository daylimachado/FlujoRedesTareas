# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:57:22 2019

@author: lapi7
"""

import csv
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np
import pingouin as pg
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd

df = pd.read_csv("datos2.csv", index_col=None,usecols=[1,2,3,4,9],dtype={'generador': 'category',
                                                                        'algoritmo_flujo': 'category',
                                                                        'vertices': 'category',
                                                                        'densidad':np.float64,
                                                                        'mediana': np.float64} )

logX = np.log1p(df['densidad'])
df = df.assign(convlogdensidad=logX.values)
df.drop(['densidad'], axis= 1, inplace= True)


his = plt.hist(round(df["convlogdensidad"],4),bins=3, density=True, facecolor='g', alpha=0.75)
plt.ylabel('Cantidad de valores')
plt.xlabel('rangos')
plt.savefig("Imagenes/Histogramadensidad.eps",bbox_inches='tight')
plt.show()


for column in range(0, df["convlogdensidad"].count()):
    pass
    if  df.iat[column, 4] >=0.0656 and df.iat[column, 4] < 0.0713:
        df.iat[column, 4] = 1
    elif df.iat[column, 4] >=0.0713 and df.iat[column, 4] < 0.077:
        df.iat[column, 4] = 2
    else: 
        df.iat[column, 4] = 3

print(df["convlogdensidad"])  
df['convlogdensidad'].replace({1: 'bajo', 2: 'medio', 3: 'alto'}, inplace= True)   
print(df["convlogdensidad"])       
plt.show()