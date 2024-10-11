# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 09:32:31 2021

@author: user
"""
#------------------------------------------------------------------------------
#Pandas圓餅圖

import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 檔案
orders = pd.read_csv('orders.csv', encoding="big5")

# 設置字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

# 分組並計算毛利總和及畫圖
orders.groupby("product")["grossmarg"].sum().plot(
    kind="pie",
    autopct='%.2f%%', 
    fontsize=10, 
) 

# 添加標題
plt.title("各產品毛利", fontsize=15)

# 顯示圖表
plt.show()

#------------------------------------------------------------------------------
#Pandas長條圖 類別-連續(dataframe method)

import pandas as pd
import matplotlib.pyplot as plt

orders= pd.read_csv('orders.csv', encoding="big5")

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

orders.groupby("product")["grossmarg"].sum().plot(kind="bar") 

plt.title("各產品毛利",fontsize=15)
plt.xlabel("產品")
plt.ylabel("毛利")
plt.show()

#在上面長條圖上顯示數值
import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 檔案
orders = pd.read_csv('orders.csv', encoding="big5")

# 設置字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

# 分組並計算毛利總和及繪製長條圖
ax=orders.groupby("product")["grossmarg"].sum().plot(kind="bar", fontsize=10)


# 添加標題和軸標籤
plt.title("各產品毛利", fontsize=15)
plt.xlabel("產品")
plt.ylabel("毛利")

# 在每個柱子上顯示數值
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='baseline', fontsize=10, color='black', xytext=(0, 3), 
                textcoords='offset points')

# 顯示圖表
plt.show()

#------------------------------------------------------------------------------

#matplotlib長條圖 類別-連續(plt method)
import pandas as pd
import matplotlib.pyplot as plt

pdbar=orders.groupby("product")["grossmarg"].sum().reset_index()

plt.bar(pdbar['product'],pdbar["grossmarg"])

plt.title("各產品毛利")
plt.xlabel("產品")
plt.ylabel("毛利")
plt.show()

#------------------------------------------------------------------------------
# matplotlib散佈圖
##orderdate group
import pandas as pd
import matplotlib.pyplot as plt

orders= pd.read_csv('orders.csv', encoding="big5")

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']


orders_by_orderdate=orders.groupby("orderdate")["grossmarg"].sum().reset_index()

plt.figure(figsize=(10,8))

plt.scatter(orders_by_orderdate["orderdate"], orders_by_orderdate["grossmarg"])

plt.title('每日毛利')
plt.xlabel('時間')
plt.ylabel('毛利')
plt.xticks(rotation=90)
plt.show()


# ### 註記: scatter另一種畫法
plt.figure(figsize=(10,8))

orders_by_orderdate.plot.scatter("orderdate", "grossmarg")

plt.title('每日毛利')
plt.xlabel('時間')
plt.ylabel('毛利')
plt.xticks(rotation=90)
plt.show()


#------------------------------------------------------------------------------
##orderdate groupby month

import pandas as pd
import matplotlib.pyplot as plt

orders= pd.read_csv('orders.csv', encoding="big5")
orders.info()

orders['orderdate']=pd.to_datetime(orders['orderdate'])
orders.info()

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

orders_by_orderdate1=orders.groupby(pd.Grouper(key='orderdate', freq="M"))["grossmarg"].mean().reset_index()

plt.figure(figsize=(10,8))

plt.scatter(orders_by_orderdate1["orderdate"], orders_by_orderdate1["grossmarg"])
plt.title('每月毛利')
plt.xlabel('時間')
plt.ylabel('毛利')
plt.xticks(orders_by_orderdate1['orderdate'],rotation=90)
plt.show()

#------------------------------------------------------------------------------
# pandas 繪圖，計算每日毛利額與訂單次數 

import pandas as pd
import matplotlib.pyplot as plt

orders= pd.read_csv('orders.csv', encoding="big5")


orders_by_orderdate=orders.groupby("orderdate").agg({"grossmarg":"sum","orderId":"count"})


orders_by_orderdate.columns=['毛利總合','訂單次數']
orders_by_orderdate.plot() #折線圖

plt.title('每日毛利總合與訂單次數')
plt.xlabel('時間')
plt.ylabel('毛利')
plt.xticks(rotation=90)
plt.show()


#------------------------------------------------------------------------------
#seaborn 長條圖雙類別-產品性別方法一
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

orders= pd.read_csv('orders.csv', encoding="big5")

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #無襯線字體設置為「微軟正黑體」

pdbar=orders[['product','gender','grossmarg']].groupby(["product","gender"], as_index=False)["grossmarg"].sum()

sns.barplot(x="product", y="grossmarg", data=pdbar,hue="gender").set_title("各產品毛利")

plt.show()

#------------------------------------------------------------------------------
#pivot_table長條圖雙類別-產品性別方法二
import pandas as pd
import matplotlib.pyplot as plt

orders= pd.read_csv('orders.csv', encoding="big5")

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

pd.pivot_table(orders,index='product', columns='gender',values='grossmarg',aggfunc=sum).plot(kind="bar")


#------------------------------------------------------------------------------
#unstack()長條圖雙類別-產品性別方法三
import pandas as pd
import matplotlib.pyplot as plt

orders= pd.read_csv('orders.csv', encoding="big5")

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

pdbar1=orders[['product','gender','grossmarg']].groupby(["product","gender"])["grossmarg"].sum().unstack()

pdbar1.plot(kind='bar')

plt.show()

#------------------------------------------------------------------------------
#Pandas 長條圖，以訂單日期為X軸
import pandas as pd

orders= pd.read_csv('orders.csv', encoding="big5")

pdbar=orders.groupby(["orderdate"])["grossmarg"].sum()[:20].plot(kind="bar")

plt.xticks(rotation=90)
plt.title("每日毛利")

###問題: 請將上題改為: Pandas 長條圖，以每月訂單日期為X軸
import pandas as pd

orders= pd.read_csv('orders.csv', encoding="big5")
orders.info()
orders["orderdate"]=pd.to_datetime(orders["orderdate"])
orders.info()

pdbar=orders.groupby(pd.Grouper(key="orderdate",freq="M"))["grossmarg"].sum().plot(kind="bar")

plt.xticks(rotation=90)
plt.title("每月毛利")


#------------------------------------------------------------------------------
#顯示多張組圖，左上為每日訂單數量，右下為各產品總銷售數量

orders= pd.read_csv('orders.csv', encoding="big5")

fig, ax = plt.subplots(2,2,figsize=(10,8))

orders.groupby("orderdate")['orderId'].count().plot(kind='bar',ax=ax[0,0],title='每日訂單數量')

orders.groupby('product')['orderId'].count().plot(kind='bar',ax=ax[1,1],title='產品總銷售數量')

plt.suptitle('四張組圖展示')

#------------------------------------------------------------------------------
#請以下列資料集製作圖表，X軸為電影名稱，左Y軸標籤為聲量(顯示刻度即可)，右Y軸標籤為情緒分數(顯示刻度即可)，以bar圖形顯示
##2個長條圖2個座標
import pandas as pd
import matplotlib.pyplot as plt
allmv_VEA_df=pd.DataFrame( [['007特警',555,0.8],['蜘蜘人',322,0.2],['變形金',444,0.5]],columns=(['電影名稱','聲量','情緒分數']))

#allmv_VEA_df.set_index('電影名稱').plot(kind='bar') #共用座標軸
allmv_VEA_df.set_index('電影名稱').plot(kind='bar',secondary_y='情緒分數',width=0.7) #沒有共用座標軸

###問題:修改上圖(1)將情緒以折線圖表示(2)顯示兩個座標軸刻度，並加入左Y軸標籤"電影聲量", 右Y軸標籤"情緒分數"(3)加入title"聲量情緒圖"(4)X軸標籤"電影名稱"




