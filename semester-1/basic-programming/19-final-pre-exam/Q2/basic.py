#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Question 2"""

# 在開始之前，我們先釐清問題是什麼。
#
# 老師希望有兩種處理方式。字典希望是這樣：
#
# 輸入內容  表示法
# --------  --------------
#           {
# 金 4          "金": 4,
# 銀 5          "銀": 5,
# 銅 9          "銅": 9,
# 優 7          "優": 7
#           }
#
# 而串列希望是這樣：
#
# 輸入內容  表示法
# --------  --------------
#           [
# 金 4          4,
# 銀 5          5,
# 銅 9          9,
# 優 7          7
#           ]
#
# 串列隱含「金、銀、銅、優」的順序。

# 第二項串列的順序，顯示用。
award_display_names = ["金", "銀", "銅", "優"]


# 將輸入內容變成字典。這裡使用到自訂函數 (def)。
def read_to_dict():
    # 定義一個 dict，用來放獎牌及其個數。
    award_table = {}

    # `_` 是「佔位符」，用不到的意思。
    for _ in range(0, 4):
        # 這裡的解釋詳見 Q1 的解答。
        [award, amount] = input("").split(" ")

        # 「獎牌數目」要記得轉成數字。
        amount = int(amount)

        # 把獎牌 -> 數目寫入 award_table
        award_table[award] = amount

    return award_table


# 將輸入內容變成串列。這裡使用到自訂函數 (def)。
def read_to_list():
    award_list = []

    for _ in range(0, 4):
        # _ 是佔位符，代表忽略。
        [_, amount] = input("").split(" ")

        amount = int(amount)

        # 將 amount 加入串列。
        award_list.append(amount)

    return award_list


approach = input("處理方式 (1)字典 (2)串列：")

if approach == "1":
    inputs = read_to_dict()

    # items() 回傳一個迭代器（現階段可以想像成串列），裡面是
    # (key, value) 的組合。
    for (award, amount) in inputs.items():
        print(f"{award}牌獲得 {amount} 面")
elif approach == "2":
    inputs = read_to_list()

    # zip() 會合併兩個迭代器（現階段可以想像成串列）的內容
    # 視覺化顯示是這樣的：
    #
    # award_display_names       inputs
    # 金                        4       ==> ("金", 4)
    # 銀                        5       ==> ("銀", 5)
    # 銅                        9       ==> ("銅", 9)
    # 優                        7       ==> ("優", 7)
    for (display_name, amount) in zip(award_display_names, inputs):
        print(f"{display_name}牌獲得 {amount} 面")
