# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 04:26:31 2019

@author: lapi7
"""

import pandas as pd

dnr = pd.read_csv("cantNE.csv")
dmr = pd.read_csv("algori_med.csv")

last = pd.concat([dmr, dnr], axis=1)

print(last)

last.to_csv("1.csv", index=None)