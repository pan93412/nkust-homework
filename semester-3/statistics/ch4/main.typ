#import "template.typ": *

#show: project.with(title: "CH4: 機率概論", authors: ("Yi-Jyun Pan",))

#outline(indent: auto)

= 定義

/ 機率: 衡量某一事件在未來發生的可能性，並將這個可能性數量化
  - 機率的值介於 $[0,1]$ 之間。
/ 實驗 (Experiment): 記錄一些觀察值量測值的過程。
  - 如擲一個硬幣 100 次。
  - 如擲一個骰子 20  次。
/ 樣本空間 (Sample Space, $S$): 實驗的 *所有可能結果的集合*，以 $S$ 表示。
  - 擲一個色子1次，$S={1,2,3,4,5,6}$.
  - 擲一個銅板2次，$S={"正正", "正反", "反正", "反反"}$
/ 事件 (Event): 實驗的結果，其包含 1 或數個樣本點，亦即為樣本空間的子集合或部分集合。(#link(<ex4.2-1>)[Example 4.2])
  + 單一事件 (Simple event): 事件無法分解，只包含一個樣本點。又稱「簡單事件」。
  + 複合事件 (Compound event): 事件可以分解為數個，包含至少兩個樣本點的事件。
/ 機率表示: 事件 $A$ 的機率，通常以 $P(A)$ 表示。若 $P(A)=0$ 則表示事件 $A$ 不可能發生；若 $P(A)=1$ 則表示事件 $A$ 必定發生。
/ 機率三公理: 事件 $A$ 和其機率 $P(A)$ 必須滿足以下三個條件：
  1. $0 <= A <= 1$
  2. $S$ 為樣本空間，則 $P(S) = 1$
  3. 對於兩個彼此互斥的事件 $A_1, A_2, dots, A_n$，則 $P(A_1 union A_2 union dots union A_n)$ $=$ $P(A_1) + P(A_2) + dots + P(A_n)$

#question("ex4.1", <ex4.1>, ("實驗",))[
  以下三例子均稱為「實驗」：
][
  - 隨機從剛出廠的電燈泡群中抽取 3 顆電燈泡，每一個燈泡分類為亮或不亮，並檢驗損壞之個數。 (ex4.1)
  - 投擲一個公平的色子，觀察其面朝上的點數。 (ex4.1)
  - 記錄 1-5 號田徑選手跑完百米競賽後的排名次序。 (ex4.1)
]

#question("ex4.2 (1)", <ex4.2-1>, ("樣本空間", "事件"))[
  根據 #link(<ex4.1>)[Example 4.1] 的第一個實驗（隨機抽取 3 個電燈泡），列出其樣本空間 $S$ 及以下事件：

  - $A$: 抽取之 3 顆燈泡都為 *良好* 的事件。
  - $B$: 抽取之 3 顆燈泡中，*至少* 有兩顆損壞的事件。
][
  - 樣本空間
    $
    S={"GGG","GGB","GBG","BGG","GBB","BGB","BBG","BBB"}
    $
  - 事件 $A={"GGG"}$ → 單一事件（簡單事件）
  - 事件 $B={"GBB","BGB","BBG", "BBB"}$ → 複合事件
]

#question("ex4.2 (2)", <ex4.2-2>, ("樣本空間", "事件"))[
  根據 #link(<ex4.1>)[Example 4.1] 的第二個實驗（隨機投擲一個公平的色子），列出其樣本空間 $S$ 及以下事件：

  - $A$: 面朝上的點數，正好出現3點的事件。
  - $B$: 面朝上的點數，出現超過3點的事件。
][
  - 樣本空間
    $
    S={1,2,3,4,5,6}
    $
  - 事件 $A={3}$ → 單一事件（簡單事件）
  - 事件 $B={4,5,6}$ → 複合事件
]

#question("ex4.2 (3)", <ex4.2-3>, ("樣本空間", "事件"))[
  根據 #link(<ex4.1>)[Example 4.1] 的第三個實驗（1-5 號田徑選手跑完百米競賽後的排名次序），列出其樣本空間 $S$ 及以下事件：

  - $A$: 百米競賽最後順序為 $(2,1,4,3,5)$：${"2 號選手跑第一", "1 號選手跑第二", dots}$ 的事件。
  - $B$：百米競賽最後順序為 3 號跑第一的事件。
][
  - 樣本空間：
    $
    S = &{(1, 2, 3, 4, 5), \
        &(1, 2, 3, 5, 4), \
        &(1, 2, 4, 3, 5), \
        &dots, \
        &(5, 4, 3, 1, 2), \
        &(5, 4, 3, 2, 1)}
    $

    ```py
    >>> list(itertools.permutations([1,2,3,4,5], r=5))
    ```

  - 事件 $A={(2,1,4,3,5)}$
  - 事件 $B$ $=$ ${(3, 1, 2, 4, 5),
    (3, 1, 2, 5, 4),
    dots,
    (3, 5, 4, 1, 2),
    (3, 5, 4, 2, 1)}$
    ```python
    >>> list(filter(
      lambda p: p[0] == 3,
      itertools.permutations([1,2,3,4,5], r=5)
    ))
    ```
]

#question("ex4.2 (3)", <ex4.2-3>, ("三定理",))[
  假設某一實驗，其 $S$ 包含 5 個樣本點：$S={e_1, e_2, e_3, e_4, e_5}$。

  + 若 $P(e_1)=P(e_2)=0.15$, $P(e_3)=0.4$ 和 $P(e_4)=2P(e_5)$，求 $P(e_4)$, $P(e_5)$.
  + 若 $P(e_1)=3P(e_2)=0.3$ 且其餘樣本機率均相等，求其餘樣本點的機率。
][
  *Q1:*

  Let $P(e_5) = a$, $P(e_4) = 2a$.

  $
  P(S) &= 1 = P(e_1) + P(e_2) + P(e_3) + P(e_4) + P(e_5) \
       &= 0.15+0.15+0.4+2a+a \
       &= 0.7+3a \
  a &= 0.1
  $

  Therefore, $P(e_4) = 0.2$ and $P(e_5) = 0.1$.

  *Q2:*

  $
  3P(e_2)&=0.3 \
  P(e_2)&=0.1
  $

  $
  P(S) &= 1 = P(e_1) + P(e_2) + P(e_3) + P(e_4) + P(e_5) \
       &= 0.3 + 0.1 + k + k + k \
       &= 0.4 + 3k \
  3k   &= 0.6 \
  k    &= 0.2
  $

  Therefore, $P(e_3) = P(e_4) = P(e_5) = 0.2$.
]

= 機率理論種類

== 古典機率 (Classical Probability)

- 限制條件
  + 實驗的樣本空間必須是有限的。
  + 實驗之每一個樣本點發生的機率必須相等。

#formula[
  *事件 $A$ 發生的機率*

  $
  P(A) = N(A)/N(S)
  $

  其中，$N(A)$ 為事件 $A$ 本身所包含的樣本點個數；$N(S)$ 為樣本空間所包含的樣本點個數。
]

#question("ex4.4", <ex4.4>, ("古典機率",))[
  試著投擲一個公平的硬幣兩次，試著用古典機率，算出其剛好 (exactly) 出現正面一次的機率。
][
  Exp：投擲一個公平的硬幣兩次。

  $
  S &= {"HH", "HT", "TH", "TT"} \
  N(S) &= 4 \
  \
  A &= {"HT", "TH"} \
  N(A) &= 2 \
  \
  P(A) &= N(A)/N(S) = 2/4 = 0.5
  $
]

== 客觀機率 (Objective Probability)

- 包含 *相對次數機率 (relative frequency probability)* 和 *經驗機率 (empirical probability)*。
- 定義：在相同的情況下反覆實驗 $N$ 次，而事件 $A$ 出現的次數為 $N(A)$，則 $N(A)/N$ 為事件 $A$ 發生機率 $P(A)$ 的一個很好的估計值。
- 缺點：若隨機實驗（結果無法預測）不能長期實施或大量調查，則不能依據此機率理論求得其發生機率。

#formula[
  *客觀機率*

  $
  P(A) = lim_(N->oo) N(A)/N
  $

  可得出*「大數法則 (law of large number)」*：實驗次數愈多 → 相對次數愈穩定 → 機率估計愈準確。
]

#question("teacher-ex1", <teacher-ex1>, ("客觀機率",))[
  假設台北市教育局想知道台北市小學生上網的比例，並對此進行「小學生上網問卷調查」調查。假設共調查 3,600 位小學生，其中 3,020 位小學生會上網，則小學生上網的客觀機率為多少？
][
  $
  P("上網小學生") = 3020/3600 = 0.84
  $
]

== 主觀機率 (Subjective Probability)

- 單由個人過去經驗，主觀的觀點，相關主觀的判斷事件發生的機率。
- 此時 $P(A)$ $=$ 對事件 $A$ 發生的信心。
- 範例
  + NBA 冠軍賽：公牛 v.s. 爵士，球迷主觀認為公牛贏球的機率為 80%。
  + 下屆總統大選各候選人當選的 *可能性*（機率）為何？

= 事件關係形式

- 聯集 (Union): $A$ 事件發生或 $B$ 事件發生，或 $A$ 與 $B$ 事件同時發生的新事件，*以 $A union B$ 表示*。 _p.4-8_
  #image("a-union-b-venn.svg", width: 40%)
- 交集 (Intersection): $A$ 與 $B$ 事件同時發生的新事件，*以 $A sect B$ 表示*。 _p.4-9_
  #image("a-sect-b-venn.svg", width: 40%)
- 餘集 (Complement): 不在事件 $A$ 中的所有樣本點，*以 $A^c$ 或 $overline(A)$ 表示*。 _p.4-10_
  #image("abs-complement.svg", width: 40%)

#question("ex4.5", <ex4.5>, ("事件關係形式",))[
  假設某一個實驗的樣本空間包含七個樣本點：

  $
  S = {e_1, e_2, e_3, e_4, e_5, e_6, e_7}
  $

  定義兩事件 $A$, $B$ 如下：

  $
  A &= {e_2, e_4, e_7} \
  B &= {e_1, e_2, e_5}
  $

  列出以下新事件所包含的樣本點：

  + $A sect B$
  + $B^c$
  + $A sect B^C$
  + $A union B$
][
  // wip_ check
  $
  A sect B &= {e_2} \
  B^c &= {e_3, e_4, e_6, e_7} \
  A sect B^c &= {e_4, e_7} \
  A union B &= {e_1, e_2, e_4, e_5, e_7}
  $
]

#question("ex4.6", <ex4.6>, ("事件關係形式","古典機率"))[
  設定某一個實驗為：投擲三個公平的硬幣，並觀察其正反面情形。

  定義兩事件：$A$ 為 #text(fill:red)[至少] 有一個正面的事件，$B$ 為 #text(fill:red)[至少] 有一個反面的事件。試著列出以下事件其各自所含的樣本點並計算其機率：$A$, $B$, $A sect B$, $A union B$。
][
  $
  S = { "HHH", "HHT", "HTH", "THH", "HTT", "THT", "TTH", "TTT" }
  $

  - $A$ 事件為至少含有一個正面。
    $
    A = {"HHH", "HHT", "HTH", "THH", "HTT", "THT", "TTH"}
    $
  - $B$ 事件為至少含有一個反面
    $
    B = {"HHT", "HTH", "THH", "HTT", "THT", "TTH", "TTT"}
    $
  - $A sect B$ 至少含有一個正面、一個反面：
    $
    A sect B = {"HHT", "HTH", "THH", "HTT", "THT", "TTH"}
    $
  - $A union B$ 至少含有一個正面或一個反面：
    $
    A union B = S
    $

  計算其機率：

  $
  P(A) &= 7/8  \
  P(B) &= 7/8  \
  P(A sect B) &= 6/8  \
  P(A union B) &= P(S) \
               &= 8/8 = 1
  $
]

== 機率理論種類

- 空集合：$A sect B = emptyset$，稱兩事件為互斥 (mutually exclusive, 兩事件不可能同時發生)。

#question("ex4.7", <ex4.7>, ("空集合",))[
  補充：
][
  + $A^c$ 為 $A$ 事件的餘事件，所以 $A$ 與 $A^c$ 將整個樣本空間分割成兩個部分，且 $A sect A^c = emptyset$。A 事件與本身餘事件 ($A^c$) 互斥，不可能同時發生。
  + 一個樣本空間有數個樣本點，如 image 4-7 /* wip */ 所示。它們將整個樣本空間分成多個部分，多個單一事件
]

= 條件機率與獨立事件

+ 聯合機率：兩個或兩個以上事件同時發生的機率。見下聯合機率表。
  #formula[
    *聯合機率表*

    $P(S) = 1 = P(A sect B) + P(A sect B^c) + P(A^c sect B) + P(A^c sect B^c)$，若從此班任意抽取一位同學：

    #table(
      columns: (1fr,)*4,
      [*性別/分數*], [*及格 $B$*], [*不及格 ($B^c$)*], [*合計*],
      [*男生 $A$*], [$P(A sect B)$], [$P(A sect B^c)$], [$P(A)$ $=$ $P(A sect B)$ $+$ $P(A sect B^c)$],
      [*女生 $A^c$*], [$P(A^c sect B)$], [$P(A^c sect B^c)$], [$P(A^c)$ = $P(A^c sect B)$ $+$ $P(A^c sect B^c)$],
      [*合計*], [$P(B)$], [$P(B^c)$], [1],
    )
  ]
+ 邊際機率：兩個或兩個以上類別的樣本空間中，若 *只考量某一個類別個別發生的機率*，則在 *聯合機率表* 中 *垂直相加* 或 *平時相加* 所得的機率則稱為邊際機率。/*wip: p4-15, table 4.2*/
+ 條件機率：令 $A$, $B$ 為定義於樣本空間的事件，*已知發生事件 $B$* 之後再 *發生事件 $A$* 的機率，且 $P(B) > 0$.
  #formula(questions: (<ex4.9>, <ex4.10>))[
    *條件機率*

    $
    P(A|B) = P(A sect B)/P(B)
    $ <條件機率-formula>
  ]

#question("ex4.9", <ex4.9>, ("條件機率",))[wip][
  According to @條件機率-formula:


  + $
    P(A|B) = P(A sect B)/P(B) = 0.1/0.3 = 1/3
    $
  + $
    P(B|A) = P(B sect A)/P(A) = 0.1/0.5 = 1/5
    $

  Note that $P(A sect B) = P(B sect A)$.
]

#question("ex4.10", <ex4.10>, ("條件機率",))[wip][
  According to @條件機率-formula:

  *Subquestion 1*

  - 定義事件
    - A: 抽取此人統計學成績不及格。
    - B: 抽取此人是男同學。
  - 目的：*已知抽到男同學* 的情況下，求此人統計學不及格的機率。
  - 算法：
    $
    P(A|B) = P(A sect B)/P(B) = 0.4/0.6 = 2/3
    $

  *Subquestion 2*

  - 定義事件
    - C: 抽取此人統計學成績不及格。
    - D: 抽取此人是女同學。
  - 目的：*已知抽到女同學* 的情況下，求此人統計學不及格的機率。
  - 算法：
    $
    P(C|D) = P(C sect D)/P(D) = 0.1/0.4 = 1/4
    $
]

= 補充附錄

== 機率單字

/ exactly: 恰好 2 ($=2$) <exactly>
/ at least: 至少 2 ($>=2$)
/ at most: 最多 2 ($<=2$)
/ more than: 多於 2 ($>2$)
/ less than: 低於 2 ($<2$)