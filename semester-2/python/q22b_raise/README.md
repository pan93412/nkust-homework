---
title: Raise 拋出例外
course: "S2 - Intermediate Python Programming"
---

- 可以使用 `raise` 語句拋出例外，語法如下:

    ```py
    raise [例外類型[(e)]]
    ```

```py
def checkZeroNumber(num):
    if num > 0:
        raise Exception("數值大於0")
    if num < 0:
        raise Exception("數值小於0")

checkZeroNumber(1)
```

```plain
Exception: 數值大於0
```
