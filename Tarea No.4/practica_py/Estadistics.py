# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 23:06:53 2019

@author: lapi7
"""

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

df = pd.read_csv("Datos.csv", index_col=None,usecols=[1,2,3,4,8],dtype={'generador': 'category',
                                                                        'algoritmo_flujo': 'category','vertices': 'category','aristas': 'category', 'mediana': np.float64} )

logX = np.log1p(df['mediana'])
df = df.assign(mediana_log=logX.values)
df.drop(['mediana'], axis= 1, inplace= True)



factores=["vertices","generador","aristas","algoritmo_flujo"]
plt.figure(figsize=(8, 6))
for i in factores:
    print(rp.summary_cont(df['mediana_log'].groupby(df[i])))

    anova = pg.anova (dv='mediana_log', between=i, data=df, detailed=True , )
    pg._export_table (anova,("ANOVA"+i+".csv"))

    ax=sns.boxplot(x=df["mediana_log"], y=df[i], data=df, palette="Set1")
    plt.savefig("boxplot_"+ i+".png", bbox_inches='tight')
    plt.savefig("boxplot_" + i + ".eps", bbox_inches='tight')
    tukey = pairwise_tukeyhsd(endog = df["mediana_log"],     # Data
                          groups= df[i],   # Groups
                          alpha=0.05)          # Significance level

    tukey.plot_simultaneous(xlabel='Time', ylabel=i)    # Plot group confidence intervals
    plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")

    plt.savefig("simultaneous_tukey"+ i+".png", bbox_inches='tight')
    plt.savefig("simultaneous_tukey" + i + ".eps", bbox_inches='tight')
    print(tukey.summary())
    plt.show()