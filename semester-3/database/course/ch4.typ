#import "template.typ": *

#show: project.with(title: "CH4: 關聯式資料庫模型")

= 基礎

- Relational Database Model
- 1969年 E.F.Codd 博士在IBM公司的研究成果

== 組成元素

- 資料結構（Data Structures）：資料的組成方式，以關聯式資料模型來說，就是欄和列組成表格的關聯表（Relations）。
- 資料操作或運算（Data Manipulation 或 Operations）：資料相關操作的關聯式代數和計算。
- 完整性限制條件（Integrity Constraints）：維護資料完整性條件，其目的是確保儲存資料是合法資料

== 資料結構

- 是一組關聯表（Relations）的集合
- 關聯表是關聯式資料庫模型的資料結構，使用二維表格組織資料
    - 關聯表綱要（Relation Schema）：包含關聯表名稱、屬性名稱和其定義域。
    - 關聯表實例（Relation Instance）：指某個時間點儲存在關聯表的資料（因為儲存的資料可能隨時改變）
        - 可以視為是一個二維表格，其儲存的每一筆記錄是一個「值組」（Tuples）。

#image("assets/ch4-relation-data-structure.png")

== 術語

#image("assets/ch4-term.png")

- 關聯表（Relations）：相當於一個二維表格，不過不同於表格，並不用考慮各列和各欄資料的順序，每一個關聯表需要指定關聯表名稱。
- 屬性（Attributes）：在關聯表的所有屬性是一個「屬性集合」（Attribute Set），因為是集合，所以關聯表的屬性並不能重複。
- 值組（Tuples）：關聯表的一列，也就是一筆記錄，這是一組目前屬性值的集合。
- 維度（Degree）：關聯表的維度是指關聯表的屬性數目。
- 基數（Cardinality）：關聯表的基數是關聯表的值組數目。
- 主鍵（Primary Key）：在關聯表需要選擇一個或多個屬性的屬性子集（Attribute Subset）作為主鍵，這是用來識別值組是唯一的。
- 定義域（Domains）：相當於程式語言的資料型態，這是一組可能屬性值的集合。

== 各 layer 的 mapping

#table(
    columns: (1fr, 1fr, 1fr),
    inset: 0.5em,
    [*關聯式資料庫模型*], [*資料庫*], [*檔案系統*],
    [關聯表（Relation）], [值組（Tuple）], [屬性（Attribute）],
    [資料表（Table）], [資料列（Row）], [資料欄（Column）],
    [檔案（File）], [記錄（Record）], [欄位（Field）],
)


// 4.2 hw

== 表示法

- 關聯表綱要表示法的語法：
  #monospaced-block[
    relation_name(#underline[attribute1], attribute2, attribute3, … , attributeN)
  ]
  - relation_name：關聯表名稱
  - - attribute1, attribute2, attribute3, …. , attributeN：括號中是屬性清單，通常省略屬性的定義域。
  - 在屬性加上底線表示它是主鍵，外來鍵可以使用虛線底線或其他表示方法。

=== Example

以關聯表 `Students` 為例，其關聯表綱要，如下所示：

#monospaced-block[
    Students(#underline[sid], name, address, tel, birthday)
]


上述關聯表Students的主鍵是sid。如果在關聯表綱要需要標示定義域的int、char和datetime，可以使用括號標示在屬性後，如下所示：
Students(sid(int), name(char), address(varchar), tel(char), birthday(datetime))
