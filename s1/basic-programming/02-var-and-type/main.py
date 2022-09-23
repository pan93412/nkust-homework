"""
一、變數
========

* 大小寫不同
* 可以使用的變數名稱
    * 大小寫英文字母
    * 數字
    * 中文 (不建議)
    * 底線 (``_``)
* 開頭不能是數字
"""
    
x = 1 ; y = 0.1 # C int float
a = b = c = 0
age, name = 18, "智慧商務系"

print(a, b)

"""
二、變數資料形態
================

類型
----
* 整數 (``int``)
* 浮點數 (``float``)
* 字串 (``str``)
* 布林 (``bool``, ``True`` or ``False``)

工具函數
--------
* 查看資料形態：``type()``
* 資料形態的轉換：``int()``, ``float()``, ``str()``
"""

age: int = 2
justdoit: bool = False
name: str = 'Alex'
weight: float = 123.5
zipcode: str = "545"
msg = """
Alex
Rooney
Peko
"""

########

print("Value\tType")
for i in [age, justdoit, name, weight, zipcode, msg]:
    print(f"{i}\t{type(i)}")

print()
for i in [int(zipcode), float(age), str(weight)]:
    print(f"{i}\t{type(i)}")

########

num1 = 8 + True
num2 = 8 + False
# It introduces compiler error!
# num3 = age + zipcode
# But the following works:
num3 = age + int(zipcode)
num4 = str(age) + zipcode
