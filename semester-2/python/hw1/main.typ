#import "template.typ": *

// Take a look at the file `template.typ` in the file panel
// to customize this template and discover how it works.
#show: project.with(
  title: "Python Homework, Part I",
  authors: (
    (name: "潘奕濬", grade: "智商一甲", id: "C111156103"),
  ),
  date: "April 19, 2023",
)

= 作業說明

每一個題目都會分成兩個部分：老師一開始出的題目（以及附上我的思路補充）、程式碼以及執行結果。程式碼會寫上對應的 Step。

所有程式碼和其輸出均是透過中間編譯指令稿 (`build.py`) 自動嵌入。

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

//cb: question1.py

== 解釋

Step 1, Step 3 和 Step 5 的 `Windows()` 或 `Windows(12, 8)` 是 Python 建構 class 的語法。

Step 2 的 `getArea()` 的公式，是四邊形的面積公式：$A = w times h$。

Step 4 的 `__eq__()` 魔法方法，對應到 Step 5 的 `==`。而我們 Step 4 判斷是否相等的方式，就是判斷面積是否相等：$A_"self" = A_"other"$。

#pagebreak(weak: true)

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

//cb: question2.py

== 解釋

根據 #link("https://www.tutorialspoint.com/difference-between-composition-and-aggregation")[tutorialspoint 的說明]，Composition（組合）是強關聯的類型 (_strong association type_)——父實體持有子實體的所有權，沒有父實體就沒有子實體。因此，我在 `__init__()` 階段建立子實體（而非之後再 pass 進去）。

相對的，Aggregation 就沒有「沒有父實體就沒有子實體」的限制。子實體可以和父實體共同存在，而且子實體是可以獨立使用的（_Has-A_ 關係）。因此我不在建立 `Notebook` 的階段建立 `Mouse` 等等的類別，而是之後再 construct 之後傳入。

`connect`, `insert` 和 `link` 實際上就是跟連結、插入有關的單字，這部份沒有特別的挑選理由。另外這份 Code 大量使用 Python 的 Type Hint。

#pagebreak(weak: true)

= 第三題

假設 `Car` 的類別定義如下：

#code(margin: true)[
  ```py3
  class Car:
      def __init__(self, color):
          self.color = color
      def show(self):
          print(f'color={self.color}')
  ```
]

1. 請在 `Car` 當中，新增一個屬性 `oil`，並加入兩個 abstract method：`setOil()` 和 `getOil()`。
2. 定義一個 `Truck` 類別，繼承自 `Car` 類別。`Truck` 的 `__init()__` 函數可以接收 `dr`、`ow`、`co` 和 `oil` 四個參數，分別用來設定 `door`、`owner`、`color` 和 `oil` 四個屬性。其中，`color` 屬性的設定必須呼叫父類別的 `__init__()` 函數。
3. 試在 `Truck` 類別中，加入一個 `show()` 函數，用來設定 `door`、`owner`、`color` 和 `oil` 四個屬性的值。
4. 建立物件 `myTruck`，並設定屬性分別為 `door=2`、`owner=Me`、`color=blue` 和 `oil=95`，並印出 show() 的結果。

//cb: question3.py

== 解釋

Step 1 的 `ABC`，#link("https://github.com/python/cpython/blob/main/Lib/abc.py#L184-L188")[實際上是 metaclass `ABCMeta` 的封裝版本]。`ABCMeta` 會檢查繼承 `Car` 類別的 `setOil()` 和 `getOil()` 是否有被具象化；倘若沒有，#link("https://github.com/python/cpython/blob/main/Lib/abc.py#L107")[則會在 `__init__()` 時拋出錯誤]。

Annotation `@abstractmethod` #link("https://github.com/python/cpython/blob/main/Lib/abc.py#L24")[本質上是標記我們的 method placeholder 為 _abstract method_]。Step 1 的 `setOil()` 和 `getOil()` 使用 `@abstractmethod` 標成 _abstract method_，Step 2 的 `Truck` 類別中會具象化這兩個 methods。

Step 2 的 `Truck` 的 `__init__()` 方法，有使用 `super()` 來呼叫父類別的 `__init__()` 方法。Step 4 則有用到 named parameter。

Step 3 就是單純的 _override_ 原先的 `show()` 函式，並沒有什麼特別之處。

#pagebreak(weak: true)

= 第四題

#v(1em)

1. 建立一個 data class 紀錄梯形的上底(`top`)、下底(`bottom`)、高(`height`)
2. 在 data class 中加入一個 method `getArea()` 可以計算梯形面積
  - 梯形面積公式:
    $
    frac(("上底" + "下底") times "高", 2)
    $
3. 建立一個 instance `w0`，上底 = $4$、下底 = $6$、高 = $10$，並印出 `getArea()` 的結果。

//cb: question4.py

== 解釋

Step 1 的 `dataclass` 是個 _annotation_，會透過一系列魔法將 field 放入 `__init__()` 以及其他的操作。我並未深入閱讀這方面的原始碼，故暫時不做解釋。

我在 dataclass `Trapezoid` 標記 `frozen=True`，使 `Trapezoid` 是不可變（_immutable_）的。雖然說這並不是題幹要求，但這樣確保了 `Trapezoid` 的 instance 一旦被建立，就不會再遭受意外修改。

Step 2 的 `getArea()` 會取本 instance 的三個 field，並透過 $frac(("上底" + "下底") times "高", 2)$ 的公式計算梯形面積。

Step 3 的 `w0` 建立一個 `Trapezoid` 的 instance，並且透過 `getArea()` 印出梯形面積。
