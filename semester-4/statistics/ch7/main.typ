#import "template.typ": *

#show: project.with(title: [CH7: 抽樣與抽樣分配], authors: ("Yi-Jyun Pan",))

#outline(indent: auto)

= 概論

- 母體 $N$: $x_1, x_2, ..., x_n$
  - 參數（希臘—唯一值—字母）：$mu, sigma^2, P$
  - 數量眾多，難以全部找全
- 樣本 $n$：母體數分集合，長得像母體
  - 參數（統計量）：$overline(x), s^2, overline(P)$
  - 目的：使 $overline(x)$ 接近 $mu$, $overline(P)$ 接近 $P$，$s^2 -> sigma^2$……

== 為何要抽樣分配？

因為 $n subset N$（樣本是母體的一部分），以體重為例，原則上母體是 $N= 10000, mu = 70$。但抽樣出的樣本考慮到只是部分集合，可能無法涵蓋到所有情境以致誤差（$n_1=100, overline(x_1)=69$），且抽出的不同樣本可能會有不同的結果（ex: $n_2=100, overline(x_2)=69.5$, $n_3=100, overline(x_3)=71.3$, …）。因此，我們需要推算出 $overline(x)$ 的機率分配，這樣我們才能知道 $overline(x)$ 的機率，並最終推算出最可能的 $mu$。

== 教學內容

在 $n$ 固定的情況下，知道：

- $overline(x)$ 的抽樣分配
- $overline(P)$ 的抽樣分配
- $overline(s^2)$ 的抽樣分配

= 抽樣分配

== 簡單隨機抽樣

以「班上 $50$ 人 ($N$)，抽 $5$ 位 ($n$) 給出獎品」這個 case 來說：

#let N=50
#let n=5

- 抽了放回 (simpling with replacement)：很有可能是某個人獨攬所有獎品，總機率是 \
  $
  (1/N)^n = (1/50)^5
  $
- 抽了不放回 (simpling with replacement): 每次抽樣都會拉掉前一個，總機率是 \
  $
  1/50 times 1/49 times ... times 1/46
  $

== 分層隨機抽樣

#question("ex7.1")[
  某個研究機構想要研究大學教育的問題，於是想要在台灣地區以隨機抽樣法選取 1,200 名大學生作爲樣本。倘若已知全省大學各年級之總人數及其學業平均成績的資料如@ex7.1-f1 所示：

  #figure(caption: "大學各年級之總人數及其學業平均成績")[
    #table(
      columns: (1fr,)*5,
      [*年級*], [*大一*], [*大二*], [*大三*], [*大四*],
      [*母體 $N$*], [25000], [21000], [18000], [16000],
      [*學業平均*], [82.6], [84.7], [81.3], [77.5]
    )
  ] <ex7.1-f1>

  試問倘若以分層比例抽樣法來選取樣本，則各年級應該抽取多少名學生？

  Similar: #badge(blue, "習題3")
][
  總個數（加總）$N=80000$。

  #table(
    columns: (1fr,)*6,
    [*年級*], [*大一*], [*大二*], [*大三*], [*大四*], [*$sum$*],
    [*母體 $N$*], [25000], [21000], [18000], [16000], [80000],
    [*合適的樣本 $n$*], [1200 $times$ 25/80], [1200 $times$ 21/80], [1200 $times$ 18/80], [1200 $times$ 16/80], [1200]
  )
]

== 部落抽樣

以台灣各個叢集 cluster（如東部、中部、南部、北部）來說，這些 cluster 和 clusters 之間是相似的，但 cluster 內的元素有著較大的差異。

部落抽樣很適合用在親訪調查：台灣的 clusters $N=4$，隨機抽樣 $n=2$ 個 cluster。這樣的話，就可以用 $n=2$ 個 cluster 的資料來推斷 $N=4$ 個 cluster 的資料，用在普查上可以節省交通時間和成本。

== 系統抽樣

假設班上有 $N=50$ 位同學，要抽出 $n=5$ 位同學。我們從這 10 個群組裡面依固定間隔（如每 $N/n=10$ 個）進行抽樣。

==注意週期性問題==：假設在以日子為單位的資料間隔選 7，得到的資料會只是不同週的同日子，使得結果偏頗。

= 抽樣分配

「統計量」：樣本內

#question("ex7.5")[
  我們從一個包含 $1,2,3,4$ 共 $N=4$ 個數值的母體中，依抽取後放回的方式隨機抽出樣本大小為 $n$ 的一組隨機樣本，試求當樣本大小 $n$ 分別為（a）$n=1$；（b）$n=2$；（c）$n=3$ 時的樣本平均數 $X$ 之抽樣分配，以圖示來表示，並求出個別的期望值或平均 $E(overline(x))$ 與變異數 $V(overline(X))$。

  Similar: #badge(blue, "習題6") #badge(blue, "習題7")
][
  According to the question, we calculate the averages and variances of this:

  #table(
    columns: (1fr,)*5,
    [$x$], [1], [2], [3], [4],
    [$P(x)$], [1/4], [1/4], [1/4], [1/4]
  )

  $
  E[x] = mu &= sum x dot P(x) = 1 times 1/4 + 2 times 1/4 + 3 times 1/4 + 4 times 1/4 = 2.5 \
  V(x) = sigma^2 &= sum (x-mu)^2 dot P(x) = sum x^2 dot p(x) - mu^2 \
     &= 1.25
  $

  *For $n=1$:* (wip)

  *Discussion* ⭐

  #table(
    columns: (1fr,)*5,
    [$n$], [1], [2], [3], [$N$],
    [$E[overline(x)]$], [2.5], [2.5], [2.5], [2.5],
    [$V(overline(x))$], [1.25], [0.625], [0.4167],[0],
  )
  *Conclusion*

  #blk[
    *中央極限定理* (C.L.T.)

    $N$ 母體 $arrow.r$ $n$ 樣本，若抽後放回：

    - 當母體愈來愈大時，樣本平均數趨近於常態分佈 \
      $n arrow.r infinity$, $overline(x) approx N(E(overline(x), V(overline(x))))$
      - where $E(overline(x)) = mu_(overline(x))$, $V(overline(x)) = sigma^2_(overline(x))$

    We define the sample with $n>=30$ as a large sample.

    WIP: Figure 7-1
  ]
]

#question("ex7.6")[
    一個在全省各地開了三千家分店的大企業，想要抽樣估計去年每家分店發生物品損壞的平均損失金額。假設母體平均數 $mu=1630$ 元，而母體標準差 $sigma = 400$ 元，試求 (a) 倘若抽取 $n=100$ 家分店當成隨機様本，則樣本平均數與母體不均數之差在60元以內的機率是多少？
][
  題意可知 $N=3000, mu=1630, sigma=400$，測試抽出 $n=100$，欲求 $P(abs(overline(x) < mu) < 60)$ 為 $X$。

  $
  &P(abs(overline(x) - mu) < 60) \
  =& P(-60 < overline(x) - mu < 60)
  $

  其中 $overline(x)$ 是變數，$mu$ 為 $1630$。

  + 是大樣本嗎？因為 $100 div 3000 = 0.03 < 0.5$，故可以省略校正因子。
  + $sigma^2_(overline(x)) = sigma^2 div n = 400^2 div 10^2 = 1600$
  + $overline(X) ~ N(mu, sigma^2)$
    + $
      &P(a < x < b) \
      =& P((a-mu)/sigma < (x-mu)/sigma < (b-mu)/sigma) \
      =& P((a-mu)/sigma < Z < (b-mu)/sigma) \
      =& P(-1.5 < Z < 1.5) \
      =& Phi(1.5) - Phi(-1.5) \
      =& 0.9332 - 0.0668 = 0.8664
      $
]

#question("ex7.7")[
  設某間高中的高三所有 1,200 位學生的身高呈現#underline[常態分配]，其平均數 $mu=173$ 公分，而標準差 $sigma=4.8$ 公分，若從全部的高三學生中，隨機抽取樣本數 $n=16$ 之 $150$ 個可能的樣本。試求：

  + 樣本平均數之抽樣分配的期望值與標準差。
  + 樣本平均數介於170.5公分到174.5公分之間的樣本個數。
  + 樣本平均數大於171公分的樣本個數
][
  根據題意，可以知道（$N$ 表示常態分配，$X$ 為母體）：

  $
  X~N(mu=173, sigma^2=4.8^2)
  $

  *Question 1*

  目的是抽取 150 個 $n=16$ 的樣本。因為是常態分配，且母體 $sigma^2$ 已知，故：

  + $E(overline(x)) = 173$
  + $V(overline(x)) = (4.8/4)^2 = 1.2^2$
    + $n/N=16/1200=0.013<0.05$，不用校正。

  *Question 2*

  $
  &N(170.5 < overline(X) < 174.5) \
  =& 150 times P(170.5 < overline(X) < 174.5) \
  $

  接著將 $overline(X)$ 轉換成 $Z$。轉法：$overline(X) - mu \/ sigma^2$：

  #image("ex7.7.png")

  $
  =& 150 times P((170.5-173)/1.2 < Z < (174.5-173)/1.2) \
  =& 150 times P(-2.08 < Z < 1.25) \
  =& 150 times (1-P(Z>1.25)-P(Z>2.08)) \
  =& 150 times (1-0.1056-0.0188) \
  =& 150 times 0.8756
  =& 131.34
  $
]
