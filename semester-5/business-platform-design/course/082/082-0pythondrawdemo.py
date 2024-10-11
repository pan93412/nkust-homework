# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:15:50 2022

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

listgrade=[[90,99,100],
      [99,87,94],
      [92,85,76],
      [87,67,72],
      [85,89,67],
      ]

gradedf=pd.DataFrame(listgrade,
                     columns=['數學','英文','物理'],
                     index=['No1','No2','No3','No4','No5'])

gradedf

gradedf.plot()
plt.show()

#-------------------------------------------------------------------------------
#兩種不同的圖在同一個ax

fig,ax=plt.subplots()

gradedf.plot(ax=ax)

gradedf.plot(kind='bar',legend=False, secondary_y=True,ax=ax)

plt.show()

#------------------------------------------------------------------------------
#兩種不同的圖在不同的ax，空白畫布展示
fig,ax=plt.subplots(1,2,figsize=(10,6))

ax

#兩種不同的圖在不同的ax
fig,ax=plt.subplots(1,2,figsize=(10,6))

gradedf.plot(ax=ax[0])

gradedf.plot(kind='bar',ax=ax[1])

plt.suptitle('折線與長條圖')

plt.show()

#------------------------------------------------------------------------------
###問題: 請將上面兩張圖改為折線圖在左上，長條圖在右下



