#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Question 1'''

from textui import TextUi

class Q1TextUi(TextUi):
    loop = True
    input_until_condition = lambda v: v == "end"

    def main(self):
        input_string = self.input_exit(
            "檢測的字串 (end 結束)："
        )

        character_to_detect = self.input("檢測的單一字元：")

        [character_to_replace, replacement_count] = \
            self.input_split("取代字元與取代次數：")(" ")

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
                character_to_detect,    # 檢測字元
                character_to_replace,   # 取代字元
                replacement_count       # 取代次數
            )
        )

    def on_exit(self):
        print("檢測結束")

if __name__ == "__main__":
    Q1TextUi()()
