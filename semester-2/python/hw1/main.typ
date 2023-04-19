#import "template.typ": *

// Take a look at the file `template.typ` in the file panel
// to customize this template and discover how it works.
#show: project.with(
  title: "Python Homework, Part I",
  authors: (
    (name: "Yi-Jyun Pan", email: "pan93412@gmail.com"),
  ),
  date: "April 19, 2023",
)

= 作業說明

每一個題目都會分成兩個部分：老師一開始出的題目（以及附上我的思路補充）、程式碼以及執行結果。程式碼會寫上對應的 Step。

= 第一題

假設 `Windows` 類別如下：

#code(margin: true)[
  ```py3
  class Windows:
    def __init__(self, w=10, h=5):
      self.width = w
      self.height = h
  ```
]

1. 建立一個 `Windows` 類別的物件 `w0`，其屬性 `weight` 與 `height` 為預設值。
2. 新增一個方法 `getArea()`，用來計算 `Windows` 的面積。
3. 建立物件 `w0`，使其屬性 `width` 與 `height` 為 $12$ 和 $8$，並印出面積。
4. 新增一個方法 `__eq__()`，比較面積是否相等，若相等回傳 `True` 否則回傳 `False`。
5. 建立物件 `w1`，使其屬性 `width` 與 `height` 為 $12$ 和 $8$，並印出與 w0 比較之結果。

#pagebreak(weak: true)

#srcresult("question1.py")[
  #code[
  ```py3
//embed: question1.py
  ```
  ]
][
  ```
//run: python3 question1.py
  ```
]

== 解釋

Step 1, Step 3 和 Step 5 的 `Windows()` 或 `Windows(12, 8)` 是 Python 建構 class 的語法。

Step 2 的 `getArea()` 的公式，是四邊形的面積公式：$A = w times h$。

Step 4 的 `__eq__()` 魔法方法，對應到 Step 5 的 `==`。而我們 Step 4 判斷是否相等的方式，就是判斷面積是否相等：$A_"self" = A_"other"$。

= 第二題

假設現在有一部筆電，有以下設備，並且 Composition 和 Aggregation 關係分別如下:

- CPU: Composition
- 螢幕 (Monitor): Composition
- 滑鼠 (Mouse): Aggregation
- 鍵盤 (Keyboard): Composition
- 硬碟 (SSD): Composition
- 讀卡機 (reader): Composition
- UsbHub: Aggregation
- 列表機 (printer) : Aggregation

請根據 Composition 和 Aggregation 關係，定義出 Class `Notebook`

#srcresult("question2.py")[
  #code[
    ```py3
//embed: question2.py
    ```
  ]
][
  ```
//run: python3 question2.py
  ```
]

== 解釋

根據 #link("https://www.tutorialspoint.com/difference-between-composition-and-aggregation")[tutorialspoint 的說明]，Composition（組合）是強關聯的類型 (_strong association type_)——父實體持有子實體的所有權，沒有父實體就沒有子實體。因此，我在 `__init__()` 階段建立子實體（而非之後再 pass 進去）。

相對的，Aggregation 就沒有「沒有父實體就沒有子實體」的限制。子實體可以和父實體共同存在，而且子實體是可以獨立使用的（_Has-A_ 關係）。因此我不在建立 `Notebook` 的階段建立 `Mouse` 等等的類別，而是之後再 construct 之後傳入。

`connect`, `insert` 和 `link` 實際上就是跟連結、插入有關的單字，這部份沒有特別的挑選理由。另外這份 Code 大量使用 Python 的 Type Hint。
