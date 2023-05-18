---
title: 練習一下 Q26
course: "S2 - Intermediate Python Programming"
---

- 嘗試建立一個套件為 `mypackage`
  - 在裡面分別建立四個模組 `add`, `sub`, `mul`, `div`
  - 每個模組都有一個函式，分別為 `add`, `sub`, `mul`, `div`
- 有一個檔案 `main.py` 如右：

  ```py
  from mypackage import add, sub, mul, div

  print(add.add(1, 3))
  print(sub.sub(1, 3))
  print(mul.mul(1, 3))
  print(div.div(1, 3))
  ```
