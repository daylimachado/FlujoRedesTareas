# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 23:06:53 2019

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


df = pd.read_csv("datos (2).csv", index_col=None,usecols=[1,2,3,4,9],dtype={'generador': 'category',
                                                                        'algoritmo_flujo': 'category',
                                                                        'vertices': 'category',
                                                                        'densidad':np.float64,
                                                                        'mediana': np.float64})
#mejorar los valores de la mediana 
logX = np.log1p(df['mediana'])
df = df.assign(convlogmediana=logX.values)
df.drop(['mediana'], axis= 1, inplace= True)

#agrupar los valos de densidad y convertirlo en grupos de baja, media y alta densidad


logX = np.log1p(df['densidad'])
df = df.assign(convlogdensidad=logX.values)
df.drop(['densidad'], axis= 1, inplace= True)


his = plt.hist(round(df["convlogdensidad"],4),bins=3, density=True, facecolor='g', alpha=0.75)
plt.xlabel ("rangos")
plt.ylabel("cantidad de valores")
plt.title("Histograma para agrupar densidad")
plt.savefig("Imagenes/Histogramadensidad"+".png")
plt.savefig("Imagenes/Histogramadensidad"+".eps")

print("bins %s" % bins, end="\n\n")

b=[0.0656, 0.0713, 0.077,  0.0827] #arreglo de densidad
i = 0
arregl_densi = open("Arreglodensid.csv", "w+")
for valor in b:
    i += 1
    arregl_densi.write(str(valor))
    if i < len(b):
        arregl_densi.write(",")
arregl_densi.write("\r\n")
arregl_densi.close()
  
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

#Aplicación de ANOVA a las transformaciones de mediana y densidad y al resto de factores

anova_factores=["generador","algoritmo_flujo","vertices","convlogdensidad"]
plt.figure(figsize=(8, 10))
for i in anova_factores:
    
    print(rp.summary_cont(df['convlogmediana'].groupby(df[i])))

    anovaporfactor = pg.anova (dv='convlogmediana', between=i, data=df, detailed=True , )
    pg._export_table (anovaporfactor,("estadisttable/Tabla_ANOVA"+i+".csv"))

    ejes=sns.boxplot(x=df["convlogmediana"], y=df[i], data=df, palette="Set2")
    plt.savefig("Imagenes/aboxplot"+ i+".png", bbox_inches='tight')
    plt.savefig("Imagenes/aboxplot" + i + ".eps", bbox_inches='tight')
    tukey = pairwise_tukeyhsd(endog = df["convlogmediana"],     # Data
                          groups= df[i],   # Groups
                          alpha=0.05)          # Significance level

    tukey.plot_simultaneous(xlabel='Tiempo', ylabel=i)    # Plot group confidence intervals
#    plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")

    plt.savefig("Imagenes/tablatukey"+ i+".png", bbox_inches='tight')
    plt.savefig("Imagenes/tablatukey" + i + ".eps", bbox_inches='tight')
    print(tukey.summary())
    
    excel_tukey = open("estadisttable/Tukey"+i+".csv", 'w')
    with excel_tukey:
        writer = csv.writer(excel_tukey)
        writer.writerows(tukey.summary())

model_name = ols('convlogmediana ~ generador+algoritmo_flujo+vertices+convlogdensidad +generador*algoritmo_flujo+algoritmo_flujo*vertices+vertices*convlogdensidad+generador*vertices+generador*convlogdensidad+algoritmo_flujo+vertices*convlogdensidad', data=df).fit()
model_name.summary()
aov_table = sm.stats.anova_lm(model_name, typ=2)
df1=pd.DataFrame(aov_table)
df1.to_csv("multianova.csv")   
   
plt.show()
print ("fin")