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

「統計量」：樣本內隨機變數的實數值函數

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
  + $overline(X) tilde N(mu, sigma^2)$
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
  X tilde N(mu=173, sigma^2=4.8^2)
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
  =& 150 times 0.8756 \
  =& 131.34
  $
]

== 抽樣分配形狀

#figure(caption: [$overline(x)$ 之抽樣分配的各種分配形狀])[
  #image("fig7-1.png")
]

= 樣本比例 $hat(p)$ 的抽樣分配

== 定義

樣本比例 $hat(p) = Y/n$ 用來估計母體比例 $p$，其中 $Y$ 表示從具有不良品、成功或某種特性的比例或機率是 $p$ 的母體中隨機抽取樣本大小為 $n$ 的隨機樣本中，不良品、成功或某種特性的個數。

$Y$ 的機率分配是具有參數 $n$ 與 $p$ 的二項分配。

== 分配結論

抽取放回：

$
E[hat(p)] &= p \
V(hat(p)) &= (p(1-p))/n
$

當 $n p>=10$ 且 $n(1-p) >= 10$（另一種說法是 $n p>5$ 且 $n(1-p) > 5$）時：

$
hat(p) approx N(P, P(1-P)/n)
$

抽取不放回之 $V(hat(p))$ 應補上有限母體校正因子 $(N-n)/(n-1)$，$n/N<0.05$ 時則可省略。

#question("ex7.8")[
  wip
][
  *$hat(p)$ 的抽樣分配*

  $
  hat(p) approx N(P, P(1-P)/n) \
  E[X]=P=0.1 \
  V(X)=P(1-P)/n=0.0009 \
  sigma_(hat(p))=sqrt(V(X))=0.03
  $

  *Calculate $P(-0.05 <= hat(p) - p <= 0.05)$*

  #image("2024-03-20-10-40-48.png")

  $
  &P(-0.05 <= hat(p) - p <= 0.05) \
  =& P(-0.05/0.03 <= (hat(p) - p)/0.03 <= 0.05/0.03) \
  =& P(-1.67 <= Z <= 1.67) \
  =& P(Z<=1.67) - P(Z<=-1.67) \
  =& 1 - 2 times 0.0475 = 0.905 \
  $
]

= $t$ 分配

$
X tilde N(mu, sigma^2) =>^n (overline(x) - mu)/(s/sqrt(n)) tilde t(n-1)
$

常態母體 $X tilde N(mu, sigma^2)$，搭配固定抽樣 $n$，可以轉為 $(overline(x) - mu)/(s/sqrt(n)) tilde t(n-1)$，其中 $sigma^2$ 可由 $s$ 估計而來。

== 圖形

#figure(caption: [$t$ 分配的圖形以及 $r$ ($v$) 的關係])[
  #image("t-distribution.png")
]

== 性質

- 當自由度 $r->oo$ 的時候，$t$ 分配近似於標準常態分配。$r>30$ 基本就可以將 $t$ 分配看成近似於標準常態分配。
- $t$ 分配與 $Z$ 分配相似，皆為以 0 為中心的對稱分配，故 $P(T<=-t)=P(T>=t)$.
- $t_(1-alpha)(r) = -t_(alpha)(r)$
- $t^2(r) = F(1, r)$

== 查表

- $T tilde t(r)$
- $"df"$ 是 degree of freedom 的意思
- $t(k)$ 是右尾機率
- $"df"$ 和 $t(k)$ 的交叉點是臨界值

#question("ex7.12")[
  試著求出:

  - 自由度 $r=18$，$P(T>=1.734)$
  - 自由度 $r=18$，$P(abs(T) >= 1.734)$
  - 自由度 $r=24$，$P(-1.318<T<2.064)$
][
+ $P(T(18) >= 1.734) = 0.05$
  - 找到 $"df"=18$
  - 找到臨界值是 $1.734$ 的位置
  - 往上查，發現是 $t_(0.050)(k)$，故機率為 $0.05$。
+ $P(abs(T(18)) >= 1.734) = 0.1$
  + 可以拆成 $P(T(18) <= -1.734) + P(T(18) >= 1.734)$
    #image("fig4.3.2.png", width: 40%)
  + 因為是對稱的，所以是 $2 times P(T(18) >= 1.734) = 2 times 0.05 = 0.1$
+ $P(-1.318 < T(24) < 2.064) = 0.875$
  #image("fig4.3.3.png", width: 40%)
  + $1 - P(T(24) < -1.318) - P(T(24) > 2.064)$
  + 其中 $P(T(24) < -1.318)$ 不能直接查，但可以轉換成 $P(T(24) > 1.318)$（對稱），是 $0.1$；$P(T(24) > 2.064)$ 可以查，是 $0.025$。
  + $1-0.1-0.025 = 0.875$.
]

#image("t-critical-value.svg")

== 應用

#question("ex7.13")[
  假設 $X$ 是某國中之男生的體重，已知其分配為平均數 $u=63$，標準差 $sigma$ 未知的常態分配，也就是 $X tilde N(63, sigma^2)$。倘若今天從這個班級中，隨機抽出 $n=16$ 位男學生作為樣本，其樣本標準差 $s=3.5$，則這 16 位男同學之平均體重 $overline(X)$ 在某一個數值 $k$ 以下的機率為 $0.975$，請問這個 $k$ 值是多少？
][
  *脈絡*

  可以知道題幹 *母體* 是 $X tilde N(63, sigma^2 = ?)$。

  另外，根據題幹也可以列出：

  $
  P(overline(X) < k) = 0.975, k = ?
  $

  $overline(x)$ 是變數，可以查表；$k$ 這是值。

  由於樣本是小樣本，且母體的標準差 $sigma$ 未知，其樣本標準差 $s=3.5$，故統計量：

  $
  T=(overline(x) - mu)/(s/(sqrt(n))) tilde t(n-1) \
  => T=(overline(X)-63)/(3.5/sqrt(16)) tilde t(15)
  $

  轉換為 $t$ 分配形式，可求得：

  $
  &P(overline(X) < k) = 0.975 \
  =>& P((overline(x) - 63) / (3.5/sqrt(16)) < (k-63)/(3.5/sqrt(16))) = 0.975 \
  =>& P(t(15) < (k-63)/(3.5/sqrt(16))) = 0.975 \
  =>& P(t(15) > (k-63)/(3.5/sqrt(16))) = 0.025 \
  =>& (k-63)/(3.5/sqrt(16)) = 2.131 \
  =>& k=63+2.131 times 3.5/sqrt(16) approx 64.86
  $
]

= 卡方分配

== 公式

若 $X_1, X_2, dots, X_n$ 是從常態分配 $N(mu, sigma^2)$ 抽出一組樣本數為 $n$ 的隨機樣本，且 $overline(X) = 1/n sum_(i=1)^(n) X_i$，$S^2=1/(n-1) sum_(i=1)^n (X_i-overline(X))^2$。

#blk[
  *當 $mu$ 已知時*

  $
  S^2_mu = (sum_(i=1)^n (X_i-mu)^2)/n
  $

  and:

  $
  (n dot S^2_mu)/sigma^2 tilde chi^2 (n)
  $

  其中 $n$ 和 $sigma^2$ 是常數，$S^2_mu$ 是變數。

  一形式：

  $
  (cancel(n) dot (sum_(i=1)^n (X_i-mu)^2)/cancel(n)) / sigma^2 = (sum_(i=1)^n (X_i-mu)^2) / sigma^2  tilde chi^2 (n)
  $
]

#blk[
  *當 $mu$ 未知時*

  $
  S^2 = (sum_(i=1)^n (X_i-overline(X))^2)/(n-1)
  $

  and:

  $
  (n-1) dot S^2/sigma^2 tilde chi^2 (n-1)
  $

  一形式：

  $
  (cancel(n-1) dot (sum_(i=1)^n (X_i-overline(X))^2)/cancel(n-1)) / sigma^2 = (sum_(i=1)^n (X_i-overline(X))^2) / sigma^2 tilde chi^2 (n-1)
  $
]

== 圖形

#figure[
  #image("2024-03-20-10-46-52.png", width: 45%)
]

X 軸是 $X tilde chi^2(r)$，其中 $X$ 必定為正值，且是右偏分配。自由度 $r$ ($k$) 變大時，分配曲線向右移動。

$
E[X] &= r \
V(X) &= 2r
$


== 應用

#question("ex7.11")[
  由一個平均數 $mu$ 未知，變異數 $sigma^2=16$ 的常態分配母體中抽出一組樣本數 $n$ 為 $20$ 的隨機樣本，試求：

  + 其樣本變異數 $S^2$ 會超過 $27.67$ 的機率
  + 其樣本變異數 $S^2$ 介於 $8.52$ 和 $25.384$ 之間的機率
][
  *脈絡*

  $
  X tilde N(mu=?, sigma^2=16) "母體" \
  arrow.b space (n=20) \
  S^2 = sum(X_i-overline(X))^2 / (n-1)
  $

  問題：

  + $P(S^2 > 27.67) = ?$ (省略)
  + $P(8.52 < S^2 < 25.384) = ?$
    + 知道 $S^2$ 是變數，知道其分配，然後查表。

  *Solution*

  其分配最可能是「卡方分配」：

  $
  (sum_(i=1)^n (X_i-overline(X))^2) / sigma^2 tilde chi^2 (n-1)
  $

  $
  P(8.52 < S^2 < 25.384)
  $
]
