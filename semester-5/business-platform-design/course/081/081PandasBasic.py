#!/usr/bin/env python
# coding: utf-8


#DataFrame 基礎

# 製作 Dataframe  資料集----from dic
import pandas as pd

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

member = pd.DataFrame(data)

member


# 查看前五筆資料
member.head()

# 查看欄位資訊
member.info()

#查看各欄位統計結果
member.describe()

member.describe(include='all')

# 查看多少筆多少欄位(列數,欄數)
member.shape

# 如何取出筆數
member.shape[0]

member.shape[1]

# 製作 Dataframe  資料集----from list
listmember=[['Howard',25],['Lily',21],['Kai',35],['Jojo',18],['Ivan',15], ]


member1 = pd.DataFrame(listmember, columns=(['name','age']))

member1

# 查看前五筆資料
member1.head()

# 查看欄位資訊
member1.info()

# 查看多少筆多少欄位(列數,欄數)
member1.shape

#------------------------------------------------------------------------------
# zip用法
name=['John','Mary','Peter']
grade=[90,66,77]

list(zip(name,grade))
member2=pd.DataFrame(zip(name,grade))

member2
#------------------------------------------------------------------------------
# 資料集的複製方法一,member會受影響
test = member

test.columns

test.columns =  ['num','word','fix']

# test與member的差異-->前面的member也會受到影響
test
member

#資料集的複製方法二，member不會受影響

test = member.copy()

test.columns

test.columns =  ['numdddd','1','2']

# test與member的差異-->前面的member不會受到影響
test
member

#------------------------------------------------------------------------------
# 重新以Data frame產出member資料

member = pd.DataFrame(data)

# 取得一欄資料，df[‘columename’]
member['name']

# 取得多欄資料方法一, 多個欄位使用list包起來
member[ ['name','age'] ]

# 取得多欄資料方法二, 多個欄位使用list包起來
colname = ['name','age']

member[colname]

### 問題：取出 uid 與age 欄位


#------------------------------------------------------------------------------
# 增加一欄
member["education"]=['大學','高中','大學','小學','研究所']

# 增加一列
member.loc[len(member)]=[6,'Alisa',100,'大學']

# 定位與讀取DataFrame元素
member[:2] #前2筆

member[-3:] #後3筆

member.iloc[::, 0:2] #取前2欄資料

#依據條件抓取DataFrame資料
member['age']<20 #<20 歲

member[member['age']<20]

(member['age']<20) | (member['age']>80) #小於20或大於100

member[(member['age']<20) | (member['age']>80)]

# 依條件修改dataframe資料

member.loc[member['age']>80, 'age']=99
member

###問題: 將Lily改名為LilyChen


#------------------------------------------------------------------------------
#常見計算

member['age']

# 平均會員年紀
member['age'].mean()

# 最大會員年紀
member['age'].max()

# 最小會員年紀
member['age'].min()

# 其他常見統計
member['age'].describe()

# 排序(遞增)
member['age'].sort_values()

# 排序(遞減)
member['age'].sort_values(ascending = False)

#計數某欄種類次數
member['education'].value_counts()


###問題: age的加總，age欄位值有幾種不同的年紀
member['age'].sum()
member['age'].value_counts()


#------------------------------------------------------------------------------

# 移除欄位 drop
member2 = member.drop(columns=['uid'])

member2

### 問題：移除 uid 與 age

----------------------------------------------------------------------

# 把data frame轉回list

memberlist=member.values.tolist()

memberlist

#------------------------------------------------------------------------------

# 整欄資料型別轉換
member['age'].dtype #查看原來型態

member['age'] = member['age'].astype('float64')
member['age']

member['age'] = member['age'].astype('int')
member['age']

member['age'] =  member['age'].astype('str')
member['age'].mean()

member['age'] =  member['age'].astype('int')
member['age'].mean()



#------------------------------------------------------------------------------
#欄位加總

import pandas as pd

# 載入資料集transaction
transaction = pd.read_csv('transaction.csv')

# 直接整欄計算 + - * /

transaction['sales']=transaction['quantity'] * transaction['price']

transaction

#------------------------------------------------------------------------------
# 切分群組
#  pd.cut (切割的資料 ,分成幾等分,要替換的標籤)
transaction['pricelabel']=pd.cut(transaction['price'],3,
       labels=["Cheap", "medium", "expensive"])

#  pd.cut (切割的資料,自訂條件,要替換的標籤)
criterials=[0,20,40,transaction['price'].max()]

transaction['pricelabel']=pd.cut(transaction['price'],criterials,
       labels=["Cheap", "medium", "expensive"])

transaction
#------------------------------------------------------------------------------
# 合併 merge，根據某欄位合併
newdata=pd.merge(transaction, member,
          how='left', on=['uid'])

newdata1=transaction.merge(member, on='uid') #另一種寫法

#------------------------------------------------------------------------------
#合併 concate,不根據某欄位合併
priceclass = pd.cut(transaction['price'],3,
       labels=["Cheap", "medium", "expensive"])

newdata =  pd.concat([transaction, priceclass] , axis =1)

newdata

#------------------------------------------------------------------------------
#刪除重覆值DaraFrame duplicate

transaction.drop_duplicates()

transaction.drop_duplicates(subset=["tid"])

#------------------------------------------------------------------------------
#群組計算 groupby
transaction.groupby("product")

transaction.groupby("product").sum() #全部橺位sum

transaction.groupby("product")['quantity'].sum() #取特定欄位sum

transaction.groupby("product").size() #全部欄位size

transaction.groupby("product")['quantity'].size() #特定欄位size

transaction.groupby("product")['quantity'].count() #特定欄位個數


#先挑選欄位再groupby，再計算
name = ['product','quantity']

transaction[name].groupby("product").sum()


### 問題 如何計算 每個商品quantity的平均？


### 問題 如何計算 每個商品的總業績額


###問題 計算每個商品總業績的平均，最小，以及最大值



