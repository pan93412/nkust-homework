#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Question 1"""

# 寫一個無窮迴圈，不停接收資料。
while True:
    input_string = input("檢測的字串 (end 結束)：")

    # 如果使用者輸入 end，則停止迴圈。
    if input_string == "end":
        break

    character_to_detect = input("檢測的單一字元：")

    # 我們可以看到 input 的內容是用空白隔開的
    # （[取代字元] [取代次數])，所以我們先 split
    # 切開「取代字元」和「取代次數」。
    #
    # 接下來，split() 回傳的是一個列表 (List)，
    # 我們用 unpack 語法，把列表做一一對應：
    #
    #           [ character_to_replace, replacement_count ]
    # split():  [ 'a',                  '2'               ]
    [character_to_replace, replacement_count] = \
        input("取代字元與取代次數：").split(" ")

    # 「取代次數」要先轉成數字，
    # 才可以傳進去等等的 replace() 函數。
    replacement_count = int(replacement_count)

    print(
        # https://medium.com/seaniap/python的字串格式語法-format-與f-string-90d0bc219628
        f"字元 {character_to_detect} 出現次數為:",
        # count() 會計算字串中，某個字元出現的次數。
        input_string.count(character_to_detect)
    )

    print(
        "取代後字串為:",
        input_string.replace(
            character_to_detect,  # 檢測字元
            character_to_replace,  # 取代字元
            replacement_count  # 取代次數
        )
    )

# 停止迴圈之後，顯示「檢測結束」。
# 然後程式就會到達結尾，結束執行。
print("檢測結束")
