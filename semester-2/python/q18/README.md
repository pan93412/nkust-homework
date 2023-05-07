---
title: "練習一下Q18.py"
course: "S2 - Intermediate Python Programming"
---

假設 car 的類別定義如下:

```py
class Car:
    def __init__(self, color):
        self.color = color

    def show(self):
        print(f'color={self.color}')
```

- 試著定義一個Truck類別，繼承自Car類別。Truck的__init()__函數可以接收dr、ow和co 三個參數，分別用來設定door、owner和color三個實例屬性，其中，color 屬性的設定必須呼叫父類別的__init__()函數。
- 試在Truck 類別中，加入一個show()函數，用來列印doors、owner和color三個實例屬性的值。
