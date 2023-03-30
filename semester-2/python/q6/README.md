# 練習六 Q6.py

已知求體積為 $\frac{4}{3} \pi r^3$，表面積為 $4\pi r^2$。

1. 建立一個 `Sphere` 類別，內含一個 `__init__(r)` 函數，可將 `rad` 屬性值設為 `r`。
2. 試在 `Sphere` 類別中，定義 `volume()` 函數，來回傳球體積。
3. 試在 `Sphere` 類別中，定義 `surface_area()` 函數，來回傳球表面積。
4. 試建立一個 `rad=2` 的 `Sphere` 類別的物件 `s0`，並求出物件的體積和表面積。
5. 在 `Sphere` 類別中，定義 `__repr__()`，當 `Sphere` 被查詢時，回傳 `Sphere object, rad=r` 字串。`r` 為 `rad` 的值。
6. 在 `Sphere` 類別中，定義 `__repr__()`，當 `Sphere` 被以 `print()` 印出時，回傳 `Sphere object, rad= r, volume=v, surface_area=s` 字串。`r` 為 `rad` 的值。
