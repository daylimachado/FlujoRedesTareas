# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:24:06 2019

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


df = pd.read_csv("CSVunido.csv", index_col=None,usecols=[4,7,8,9,10,11,12],dtype={'Medianatime':np.float64,
                                                                                   'DistGrado': np.int,
                                                                                   'CoefAgrup': np.float64,
                                                                                   'CentCercania':np.float64,
                                                                                   'CentCarga': np.float64,
                                                                                   'ExcentCarga': np.int,
                                                                                   'PageR': np.float64})


#his,b,r = plt.hist((df["DistGrado"]),bins=3, density=True, facecolor='g', alpha=0.75)
#plt.xlabel ("rangos")
#plt.ylabel("cantidad de valores")
#plt.title("Histograma")
#plt.savefig("Imagenes/histDistGrado"+".png")
#plt.savefig("Imagenes/histDistGrado"+".eps")
#print("bins %s" % b, end="\n\n")

for row in range(0, df["DistGrado"].count()):
    pass
    if  df.iat[row, 1] >=2 and df.iat[row, 1] < 5 :
        df.iat[row, 1] = 1
    elif df.iat[row, 1] >=5 and df.iat[row, 1] < 7:
        df.iat[row, 1] = 2
    else: 
        df.iat[row, 1] = 3

print(df["DistGrado"])  
df['DistGrado'].replace({1: 'bajo', 2: 'medio', 3: 'alto'}, inplace= True)   
#print(df["DistGrado"])   


for row in range(0, df["CoefAgrup"].count()):
    pass
    if  df.iat[row, 2] >=0 and df.iat[row, 2] < 0.2 :
        df.iat[row, 2] = 1
    elif df.iat[row, 2] >=0.2 and df.iat[row, 2] < 0.4:
        df.iat[row, 2] = 2
    else: 
        df.iat[row, 2] = 3

print(df["CoefAgrup"])  
df['CoefAgrup'].replace({1: 'bajo', 2: 'medio', 3: 'alto'}, inplace= True)   
#print(df["CoefAgrup"])   


for row in range(0, df["CentCercania"].count()):
    pass
    if  df.iat[row, 3] >=0.3 and df.iat[row, 3] < 0.46 :
        df.iat[row, 3] = 1
    elif df.iat[row, 3] >=0.46 and df.iat[row, 3] < 0.5:
        df.iat[row, 3] = 2
    else: 
        df.iat[row, 3] = 3

print(df["CentCercania"])  
df['CentCercania'].replace({1: 'bajo', 2: 'medio', 3: 'alto'}, inplace= True)   
#print(df["CentCercania"])    

for row in range(0, df["CentCarga"].count()):
    pass
    if  df.iat[row, 4] >=0.0046 and df.iat[row, 4] < 0.096 :
        df.iat[row, 4] = 1
    elif df.iat[row, 4] >=0.096 and df.iat[row, 4] < 0.18:
        df.iat[row, 4] = 2
    else: 
        df.iat[row, 4] = 3

print(df["CentCarga"])  
df['CentCarga'].replace({1: 'bajo', 2: 'medio', 3: 'alto'}, inplace= True)   
#print(df["CentCercania"]) 

for row in range(0, df["ExcentCarga"].count()):
    pass
    if  df.iat[row, 5] >=2 and df.iat[row, 5] < 3 :
        df.iat[row, 5] = 1
    elif df.iat[row, 5] >=3 and df.iat[row, 5] < 4:
        df.iat[row, 5] = 2
    else: 
        df.iat[row, 5] = 3

print(df["ExcentCarga"])  
df['ExcentCarga'].replace({1: 'bajo', 2: 'medio', 3: 'alto'}, inplace= True)   
#print(df["ExcentCarga"]) 

for row in range(0, df["PageR"].count()):
    pass
    if  df.iat[row, 6] >=0.02 and df.iat[row, 6] < 0.04 :
        df.iat[row, 6] = 1
    elif df.iat[row, 6] >=0.04 and df.iat[row, 6] < 0.06:
        df.iat[row, 6] = 2
    else: 
        df.iat[row, 6] = 3
print(df["PageR"])  
df['PageR'].replace({1: 'bajo', 2: 'medio', 3: 'alto'}, inplace= True)   
#print(df["PageR"]) 

#ANOVA-------------------------------------

logX = np.log1p(df['Medianatime'])
df = df.assign(convlogmediana=logX.values)
df.drop(['Medianatime'], axis= 1, inplace= True)

anova_factores=["DistGrado","CoefAgrup","CentCercania","CentCarga","ExcentCarga","PageR" ]
plt.figure(figsize=(8, 10))
for i in anova_factores:
    
    print(rp.summary_cont(df['convlogmediana'].groupby(df[i])))

    anovaporfactor = pg.anova (dv='convlogmediana', between=i, data=df, detailed=True , )
    pg._export_table (anovaporfactor,("Imagenes/Tabla_ANOVATime"+i+".csv"))

    ejes=sns.boxplot(x=df["convlogmediana"], y=df[i], data=df, palette="Set2")
    plt.savefig("Imagenes/aboxplot"+ i+".png", bbox_inches='tight')
    plt.savefig("Imagenes/aboxplot" + i + ".eps", bbox_inches='tight')
    tukey = pairwise_tukeyhsd(endog = df["convlogmediana"],     # Data
                          groups= df[i],   # Groups
                          alpha=0.05)          # Significance level

    tukey.plot_simultaneous(xlabel='Tiempo', ylabel=i)    # Plot group confidence intervals
#    plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")

    plt.savefig("Imagenes/tablatukeyTime"+ i+".png", bbox_inches='tight')
    plt.savefig("Imagenes/tablatukeyTime" + i + ".eps", bbox_inches='tight')
    print(tukey.summary())
    
    excel_tukey = open("Imagenes/TukeyTime"+i+".csv", 'w')
    with excel_tukey:
        writer = csv.writer(excel_tukey)
        writer.writerows(tukey.summary())

#model_name = ols('convlogmediana ~ generador+algoritmo_flujo+vertices+convlogdensidad +generador*algoritmo_flujo+algoritmo_flujo*vertices+vertices*convlogdensidad+generador*vertices+generador*convlogdensidad+algoritmo_flujo+vertices*convlogdensidad', data=df).fit()
#model_name.summary()
#aov_table = sm.stats.anova_lm(model_name, typ=2)
#df1=pd.DataFrame(aov_table)
#df1.to_csv("multianova.csv")   
   
plt.show()
print ("fin")















print ("fin")