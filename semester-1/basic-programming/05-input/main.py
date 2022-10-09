#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
輸入 | input() 命令
====================

..code:
    變數: str = input([提示字串]: str)
"""

score = input("請輸入您的程式設計成績：")

# 等價
print("您的程式設計成績為：" + score)
print(f"您的程式設計成績為：{score}")
print("您的程式設計成績為：{}".format(score))
print("您的程式設計成績為：%s" % (score))

# -----

programming_score = input("請輸入您的程式設計成績：")
english_score = input("請輸入您的英文成績：")
math_score = input("請輸入您的數學成績：")

# 此例由於 *_score 都是 string，所以是 string concatenation！
total_score = programming_score + english_score + math_score
print(total_score)

# 此例由於 *_score 都是 string，所以是 string concatenation！
# 所以需要全部轉成數字 (int())，再加總才可以。
#
# 這裡使用比較進階的 Iterator Method：map() & sum()。
total_score = sum(map(int, [programming_score, english_score, math_score]))
print(total_score)

# 注意字串不能直接加數字。下方程式碼取消註釋會出錯。
# print("總成績是" + total_score)
#
# 正確的做法應該是：
#   a. 先將 total_score 轉成字串 (str())，再做字串合併。
#   b. 使用格式化字串。
print("總成績是：" + str(total_score))
print(f"總成績是：{total_score}")
