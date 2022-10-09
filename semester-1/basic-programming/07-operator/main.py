#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
運算子
======

* 算數運算子
    * ``+``, ``-``, ``*``, ``/``
    * ``//`` (商)
    * ``%`` (餘數)
    * ``**`` (指數)
* 比較運算子
    * ``==``, ``<=``, ``>=``, ``<``, ``>``, ``!=``
* 邏輯運算子
    * ``not``, ``and``, ``or``
* 複合指定運算子
    * ``+=``, ``-=``, ``*=``, ``/=``, ``//=``, ``%=``, ``**=``
"""

# 數值運算
a = 5
b = 3
print(a / b)
print(a + b)
print(a ** b)
print(a % b)

# 範例 1（梯形面積）
top, bottom, height = float(input("上底：")), float(input("下底：")), float(input("高："))
area = (top + bottom) * height / 2
print(f"梯形面積為：{area}")

# 範例 2（溫度轉換）
c = float(input("請輸入攝氏溫度："))
f = c * 9 / 5 + 32
print(str(f) + "℉")
print(f"{c:>.2f} ℃ = {f:>.2f} ℉")
print("{:>.2f} ℃ = {:>.2f} ℉".format(c, f))
print("{1:>.2f} ℉ = {0:>.2f} ℃".format(c, f))
print("%.2f ℃ = %.2f ℉" % (c, f))

# 範例 3 (BMI)
h = float(input("請輸入身高："))
w = float(input("請輸入體重："))
bmi = w / (h / 100) ** 2
print(f"身高：{h}cm, 體重：{w}kg, BMI：{bmi:.2f}")

"""比較運算子"""
x = 5
y = 2
print(x == y)
print(x >= y)
print(x <= y)
print(x != y)
print(x > y)
print(x < y)
