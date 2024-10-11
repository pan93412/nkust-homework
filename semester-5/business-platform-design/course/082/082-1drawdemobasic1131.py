# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:57:09 2022

@author: user
"""
#基礎各種圖形展示，折線圖, bar, pie, scatter

import pandas as pd
import matplotlib.pyplot as plt

orders= pd.read_csv('orders.csv', encoding="big5")

orders

orders1=orders.sample(10).reset_index(drop=True)

orders1

orders1[['orderId','grossmarg']].plot()

orders1[['orderId','grossmarg']].set_index('orderId').plot()

orders1[['orderId','grossmarg']].set_index('orderId').plot(kind='bar')

orders1[['orderId','grossmarg']].set_index('orderId').plot(kind='pie',subplots=True, autopct='%0.1f%%')

orders1[['orderId','grossmarg']].set_index('orderId').plot(kind='pie',subplots=True, autopct='%0.1f%%', legend=False)

orders1[['orderId','grossmarg']].plot(kind='bar')

orders1[['orderId','grossmarg']].plot.scatter('orderId','grossmarg',s='grossmarg')

orders1.plot.scatter('orderId','grossmarg',s='grossmarg') #與上述圖形相同

orders1['grossmarg'].hist(bins=10)

orders1['grossmarg'].plot(kind='bar')

orders1['grossmarg'].plot(kind='box')

orders1.groupby('product')['orderId'].count().plot()

orders1.groupby('product')['orderId'].count().plot(kind='bar')

orders1.groupby('product')['grossmarg'].sum().plot()

orders1.groupby('product')['grossmarg'].sum().plot(kind='bar')
#------------------------------------------------------------------------------
#雙圖:兩種不同的圖(長條圖、折線圖)在同一個ax
fig,ax=plt.subplots(figsize=(10,6))

orders1.groupby('product')['orderId'].count().plot(kind='bar',ax=ax)

plt.ylabel('訂單數')

orders1.groupby('product')['grossmarg'].sum().plot(ax=ax,secondary_y='grossmarg',color='black')

plt.title('雙圖展示')

#------------------------------------------------------------------------------
##問題：請將上述雙圖進行修正，(1)中文字型顯示'Microsoft JhengHei'，並且圖中所有中文宇型皆為16pt(2)多增加右Y座標軸標籤為"毛利"


