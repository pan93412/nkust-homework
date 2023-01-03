import random
from typing import List


# `: int`  和 `-> List[int]` 這些是「類型註釋」
# 可以用來方便使用者確定要傳入的內容、
# 讓 IDE 靜態核查數值的類型，
# 以及方便自動補全。如果看不太懂可以忽略這些內容，
# 只留 `def lotto(n, m):` 就好。
def lotto(n: int, m: int) -> List[int]:
    # https://docs.python.org/zh-tw/3.11/library/random.html#random.choices
    return random.choices(range(1, n + 1), k=m)
