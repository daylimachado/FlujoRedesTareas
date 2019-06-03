# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:57:23 2019

@author: lapi7
"""

import xlsxwriter
b = ['0.0656', '0.0713', '0.077',  '0.0827']
workbook = xlsxwriter.Workbook('b.xlsx')
worksheet = workbook.add_worksheet()


       

col = 0

for row, data in enumerate(b):
   worksheet.write_column(row, col, data)

workbook.close()


#ds = pd.DataFrame(b)
#ds.to_csv("b.csv", encoding="utf-8", index=None)
#print("fin")