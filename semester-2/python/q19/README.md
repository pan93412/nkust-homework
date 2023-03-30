# 練習一下Q19.py

設Person類別的定義如下:

```py
class Person:
    def __init__(self, na):
        self.name = na
```

- 試於person類別內加入print_name()函數，可以印出屬性name的值。
- 試定義一個Student類別，他繼承自Person類別，並設計__init__()函數，使得實例屬性name和gender 可以被設值，其中name 的值須呼叫父類別的__init__()函數。
- 試在Student 類別內定義一個print_info()函數，可印出name和gender的值。
