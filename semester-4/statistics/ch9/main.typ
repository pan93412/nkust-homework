#import "template.typ": *

#show: project.with(title: [CH8: 估計], authors: ("Yi-Jyun Pan",))

#outline(indent: auto)

= 概論

現在已經知道可以從 $n$ 個樣本中知道其樣本統計量 ($overline(x)$, $hat(p)$, $s^2$, …) 的分配，而這次想要從樣本的統計量推估母體的參數（$mu$, $p$, $sigma^2$, …）。

但是，以往學習的「點估計」$overline(x)_s -> mu$ 可能是有 *抽樣誤差* 的，且目前還沒有描述。現在我們已經學會 $overline(x)$ 和 $mu$ 有著誤差，接下來希望可以知道$P(abs(overline(x)_s-mu))$ 的區間，另外日後假如加入更多樣本，如 $overline(x)_s^'$，有多少機率可以涵蓋到母體平均值 $mu$。

- *信心水準*：有多少機率可以涵蓋到母體參數
- 本章學習重點：*區間估計*

= 估計式

== 特性

目的：自 $hat(theta) -> theta$（$hat$ 表估計。）

- 要具有 *不偏性*：$E(hat(theta)) = theta$，如 $E(overline(x)) = mu$ 就具有不偏性。
- 要具有 *有效性*：$theta$ 眾多的估計式中，$theta_1$, $theta_2$ 都是不偏的
  - $V(hat(theta_1)), V(hat(theta_2))$, R.E. (Relative Efficiency)
    $
    "R.E." = V(hat(theta_1))/V(hat(theta_2)) < 1
    $
    此時 $hat(theta_1)$ 比起 $hat(theta_2)$ 相對有效。
  - $V(hat(theta))$ 是所有估計式裡面最小的，最小變量是不偏估計式 (MVUE)。
- 要具有 *一致性*：當 $n -> oo$ 時，$hat(theta) -> theta$。
  - $E(overline(X)) = mu$ 時 $lim_(n->oo) V(overline(x)) = sigma^2/n = 0$.

結論：滿足不偏性、有效性、一致性的估計式是最佳的估計式。

=== 舉例

FIXME: understand it.

令 $X$ 為國小學生每人每週看電視的時間的母體，欲求其母體平均數 $mu$。考慮到 $X$ 巨大，本次抽取 $n=1600$ 個樣本後計算得出樣本平均數 $overline(x) = 21$ 小時。

要如何由 $overline(x)$ 建立 $mu$ 的 *信賴區間* (confidence interval, C.I.)（也就是 $mu$ 的落點機率）——`(信賴下限 confidence lower limit, 信賴上限 confidence upper limit)`——呢？

有幾個常用的信心水準（就是機率）：90%、95%、99%。實務上會將其轉換成 $(1-alpha) 100 %$：

$
90 &= (1-alpha) times 100% \
0.9 &= 1 - alpha \
0.1 &= alpha
$

$
90% &= (1-alpha) times 100%,space& alpha &= 0.1 \
95% &= (1-alpha) times 100%,space& alpha &= 0.05 \
99% &= (1-alpha) times 100%,space& alpha &= 0.01
$

*製作信賴區間*

固定抽樣大小 $n=1600$，$overline(x)$ 為變數，則回想 Ch7 有什麼抽樣分配可以表達。

- 沒有說到這個母體是不是「常態分配」
- $n=1600>30$ 為大樣本

故根據中央極限定理（Central Limit Theorem, CLT）：

$
X approx N(mu = space ?, sigma^2 = 4^2), n=1600
$

然而以 $mu$ 為中心不容易查表，故先將 $overline(x)$ 標準化為 $Z$ 值後查表。

$
(overline(x) - mu)/(sigma / sqrt(n)) = Z
$

中心點為 $1-alpha$，左右兩邊為 $alpha/2$，兩邊合起來就是 $alpha$（常態分配兩邊對稱）：

$
P(-Z_(alpha/2) < Z < Z_(alpha/2)) = 1-alpha
$

$
P(-1.96 < (overline(x)-mu)/(sigma/sqrt(n)) < 1.96) = 0.95
$

Note that $overline(x)$ can be considered as $overline(x)_s$.

不等式三邊同時乘以 $sigma/sqrt(n)$:

$
    &P(-1.96 times sigma/sqrt(n) < overline(x) - mu < 1.96 times sigma/sqrt(n)) = 0.95 \
=>  &P(1.96 times sigma/n > -overline(x) + mu > -1.96 times sigma/sqrt(n)) = 0.95 \
=>  &P(-1.96 times sigma/n < -overline(x) + mu < 1.96 times sigma/sqrt(n)) = 0.95
$

可以看到 lower limit (C.L.L.)、upper limit (C.U.L.) 和信心水準：lower limit is $-1.96 times sigma/sqrt(n)$ while upper limit is $1.96 times sigma/sqrt(n)$ 為信賴區間，信心水準為 $0.95$。公式 $mu$ 的 $(1-alpha) times 100% 的 C.I.$ 為：

$
(overline(x) - Z_(alpha/2) times sigma/sqrt(n), space overline(x) + Z_(alpha/2) times sigma/sqrt(n))
$

其中左右兩邊就是：

$
overline(x) plus.minus "查表右尾" alpha/2 "值" times overline(x) "的標準差"
$

總結上面，95% 的信賴區間答案如下：

$
overline(x)_s = 21 "hrs"
1-alpha = 0.95 \
alpha = 0.05 \
alpha/2 = 0.025
$

然後：

$
21 plus.minus Z times sigma/sqrt(n) => (20.804, 21.196) -> mu
$

== 常見信賴區間和 Z 值對照表

#figure(caption: "常見信賴區間和 Z 值對照表")[
  #table(
    columns: (1fr, 1fr),
    [*信賴區間*], [*Z 值*],
    [95%], [1.96],
    [90%], [1.645],
    [99%], [2.576]
  )
]

== 題目

#question("ex8.9")[
  小樣本：隨機抽查磁碟片8片，其重量分別為 62，65，63，61，65，64，62，66 公克，假設所有磁碟片重量服從常態分配，試求出所有磁碟片平均重量 $mu$ 的95%信賴區間。
][
  We have known $"weight" tilde N(mu, sigma^2)$, while $mu$ and $sigma^2$ is unknown. Meanwhile, we picked a sample with $n=8$. For this sample, we can calculate

  $
  overline(x) &= (62+65+63+61+65+64+62+66)/8 \
    &= 127/2 = 63.5 \
  s^2 &= (sum (x_i - overline(x))^2)/(bold(n-1)) \
    &= 1.773^2
  $

  We want to create the 95% C.I. of $mu$ from $overline(x)=63.5$, and the $alpha$ is:

  $
  1-alpha&=0.95\
  alpha&=0.05\
  alpha/2&=0.025
  $

  The formula is:

  #align(center)[
    ⭐ 點估計值 $plus.minus$ 查表分配右尾 $alpha/2$ 查表值 $times$ 標準差

    $
    overline(x) plus.minus t_(alpha/2)(n-1) times s/sqrt(n)
    $
  ]

  $
  &63.5 plus.minus t_(0.025)(7) times 1.773^2/2.82 \
  =& 63.5 plus.minus 2.365 times 0.628 \
  $

  The C.I. range is:

  $
  &(63.5 - 2.365 times 0.628, 63.5 + 2.365 times 0.628) \
  =& (62.01478, 64.98522)
  $
]

#question("ex8.12")[
  大樣本：從一批生產出的罐頭隨機抽出100個罐頭檢查，結果發現其中有10個為不良品，試求出該批罐頭不良率 $p$ 的點估計值與95%信賴區間。
][
  首先計算點估計式：$hat(p) = 10/100 = 0.1$。

  因為 $n=100$ 為大樣本，故 $(hat(p)-p)/(sqrt((p(1-p))/n)) approx bold(Z)$。$bold(Z)$ 為變數。

  #align(center)[
    當 $h p>=10$ 且 $h(1-p) >= 10$ 時，$hat(p) approx N(P, (p(1-p))/n)$。
  ]

  又已知 95% 的信賴區間，其 $alpha=0.05$，$Z_(alpha/2) = Z_(0.025) = 1.96$，所以：

  $
  &    P(-Z_(alpha/2) < bold(Z) < Z_(alpha/2)) = 0.95 \
  <=>&   P(-1.96 < (hat(p)-p)/(sqrt((p(1-p))/n)) < 1.96) = 0.95 \
  <=>&  P(-1.96 < (0.1-p)/(sqrt((0.1(1-0.1))/100)) < 1.96) = 0.95 \
  <=>&  P(-1.96 times 0.03 < 0.1-p < 1.96 times 0.03) = 0.95 \
  <=>&  P(-1.96 times 0.03 - 0.1 < -p < 1.96 times 0.03 - 0.1) = 0.95 \
  <=>&  P(397/2500 > p > 103/2500) = 0.95 \
  <=>&  P(0.0412 < p < 0.1588) = 0.95
  $

  此時機率左邊的是 C.L.L.，右邊的是 C.U.L.，所以不良率 $p$ 的 95% 信賴區間為 $(0.041, 0.159)$。

  從這裡可以達到結論：

  #blk[
    *$p$ 的信賴區間公式*

    $
    hat(p) plus.minus Z_(alpha/2) times sqrt((hat(p)(1-hat(p)))/n)
    $

    $n$ 愈大，區間範圍愈小。若要使區間範圍變小，樣本應更多。<p的信賴區間公式>
  ]
]


#question("習題 12")[
  有限母體的情況：某民調中心對政府的某一政策進行民意調查，支持率為 $P$，試問在95%的信心水準下，若希望p的估計誤差小於 0.03，所需的樣本數應為多少？
][
  // hw
]

= 反推抽樣數

== 原因

- #link(<p的信賴區間公式>)[樣本數的大小會影響估計出的結果]
  - 樣本數愈大，則估計誤差會愈小，獲得的有關資訊會愈豐富，但抽樣成本會較高
  - 樣本數愈小，則估計誤差會愈大，獲得較少有關資訊，抽樣成本會較低。
- 決定樣本數時，應該要同時考慮到抽樣成本與估計誤差，當然這牽涉到取捨均衡的問題，在比較過兩者之後，再選擇適當的樣本數。

== 要求

- 信心水準 $(1-alpha) times 100%$
- 估計誤差（精確度）

== 概念

#blk[
  *最大誤差 / 誤差範圍* (margin of error)

  假設估計誤差 $abs(overline(x) - mu)$ 不超過 $E$，且希望信賴水準為 $1-alpha$，此時在母體變異數已知的情況下，則令估計的最大誤差或誤差範圍 (margin of error) $Z_(alpha/2) sigma/sqrt(n) = bold(E)$。 <margin-of-error>
]

== 作法

#question("ex8.15")[
  有一組電燈泡的壽命服從標準差 $sigma$ 為30的常態分配，但平均數 $mu$ 未知。根據抽樣的結果發現，在95%的信賴水準下，試求出利用樣本平均數 $overline(x)$ 來估計母體平均數 $mu$ 的估計誤差 $abs(overline(x) - mu)$ 不超過 $E=8$ 小時所需的樣本大小。
][
  令壽命為 $L$。已知 $L tilde N(mu = space?, sigma^2=30^2)$，欲求 $n$，同時滿足：

  - 95% 信心水準 $=>$ $1-alpha = 0.95$
  - $abs(overline(x) - mu) <= 8 = E$

  考慮到母體是 *常態分配*，而且 $sigma^2$ 已知，所以：

  $
  (overline(x) - mu)(sigma/sqrt(n)) tilde Z
  $

  故 $mu$ 在 $(1-alpha) times 100%$ 信賴區間的公式如下：

  $
  overline(x) plus.minus Z_(alpha/2) times sigma/sqrt(n)
  $

  求 $E$，也就是單邊信賴區間長度，之公式：

  $
  Z_(alpha/2) times sigma/sqrt(n) = E
  $

  *計算*

  $
  &Z_(alpha/2 = 0.025) times (sigma = 30)/sqrt(n) = 8 \
  <=>& 1.96 times 30/sqrt(n) = 8 \
  <=>& (1.96 times 30)/8 = sqrt(n) \
  <=>& 54.0225
  $

  答案向上取整。$ceil(54.0225) = 55$
]

#question("ex8.16")[
  對於某廠商所製造的 CPU（中央處理器），隨機抽取 160 個 CPU，發現有10個 CPU 不符合所要求的規格，在95%的信賴水準下，試求出買方所要求估計誤差 $abs(hat(p)-p)$ 不超過3%時所需的樣本大小。
][
  題目從不良率 $P$ 中，抽出 $n=160$ 個樣本（預抽，為了得到 $hat(p)$），發現是不良品的樣本比例為：

  $
  hat(p) = x/n = 10/160 = 0.0625
  $

  要求：

  + $1-alpha=0.95$
  + $abs(hat(p) - p) <= 0.03 = E$，決定 $n$

  從 $hat(p)$ 建立 $p$ 的 $(1-alpha) times 100%$ C.I. 公式為：

  $
  hat(p) plus.minus Z_(alpha/2) times sqrt((hat(p)(1-hat(p)))/n)
  $

  （其中 $Z_(alpha/2) times sqrt((hat(p)(1-hat(p)))/n)$ 為單邊信賴區間寬度）

  *解題技巧*：單邊信賴區間寬度 = $E$

  $
  &Z_(alpha/2) times sqrt((hat(p)(1-hat(p)))/n) = E \
  =>& 1.96 times sqrt((0.0625 times 0.9375)/n) = 0.03 \
  <=>& n = (0.0625 times 0.9375) times (1.96 / 0.03)^2 = script((Z_(alpha/2)/E)^2 times hat(p)(1-hat(p))) \
  <=>& n = 250.104 \
  =>& ceil(n) = 251
  $
]

== 保守公式（常用）⭐⭐

過往在「反推抽樣數」中，會使這個公式進行應抽樣本數的估計（*粗體*都是要求），但 $hat(p)$ 是未知的，要如何抽？

$
bold(Z_(alpha/2)) times sqrt((hat(p)(1-hat(p)))/n) = bold(E) \
$

移項後，可以發現「當 $hat(p)(1-hat(p))$ 愈大，$n$ 也會愈大。」$n$ 愈大，誤差當然愈小。

$
n=(Z_(alpha/2)/E)^2 times hat(p)(1-hat(p))
$

而保守公式的算法就是將 $hat(p)$ 用 $1/2$ 代替，得出公式：


$
bold(Z_(alpha/2)) times sqrt((0.5 times 0.5/2)/n) = bold(E) \
n=(Z_(alpha/2)/E)^2 times 0.25
$

== 範例

#question("ex8.17")[
  保守公式：以 #link(<ex8.16>)[Example 8.16] 為基礎，若無法取得樣本比例 $hat(p)$ 的資料，試求出買方所要求估計誤差 $abs(hat(p) - p)$ 不超過3%時所需要的樣本大小。
][
  $
  &Z_(alpha/2) times sqrt((0.5 times 0.5)/n) = E \
  => &1.96 times sqrt(0.25/n) = 0.03 \
  => &0.25/n = (0.03/1.96)^2 \
  => &n = 0.25/(0.03/1.96)^2 = 1067.1 => ceil(n) = 1068
  $
]

= 母體 $sigma^2$ 的區間估計

#question("ex8.18")[
  某工廠製造出一批玩具機器人，隨機抽取9個玩具機器人並測量其重量（公克）分別為 401、405、410、403、406、411、409、408、403， 假設玩具機器人的重量服從常態分配，試求出此工廠製造的玩具機器人重量變異數 $sigma^2$ 的點估計值與90%信賴區間。
][
  先計算樣本平均數和變異數：

  $
  overline(x) &= (sum_(i=1)^n x_i) / n = 406.22 \
  s^2 &= (sum_(i=1)^n (x_i - overline(x))^2) / (n-1) = 12.194
  $

  因此 $sigma^2$ 的點估計式為樣本變異數 $s^2=12.194, n=9, 1-alpha=0.90, alpha=0.5$。

  考慮到 $mu$ 未知，故適用卡方分配：

  #blk[
    *卡方分配—當 $mu$ 未知時*

    $
    (sum_(i=1)^n (x_i-overline(x))^2) / sigma^2 tilde chi^2 (n-1)
    $
  ]

  $
  &P(chi^2_(alpha/2)(n-1) < chi^2 (n-1) < chi^2_(1-alpha/2)(n-1)) = 1-alpha \
  <=>& P(chi^2_(0.05)(8) < chi^2 (8) < chi^2_(0.95)(8)) = 0.90 \
  <=>& P(2.732 < chi^2 (8) < 15.507) = 0.90 \
  <=>& P(2.732 < (n-1)s^2/sigma^2 < 15.507) = 0.90 \
  <=>& P(2.732 < 8 times 12.194/sigma^2 < 15.507) = 0.90 \
  <=>& P(2.732 < 97.552/sigma^2 < 15.507) = 0.90 \
  <=>& P(97.552/15.507 < sigma^2 < 97.552/2.732) = 0.90 \
  <=>& P(6.290 < sigma^2 < 35.734) = 0.90
  $

  #blk[
    $s^2$ 到 $sigma^2$ 的 $(1-alpha) times 100%$ C.I.，為：

    $
    (((n-1)s^2)/(chi^2_(alpha/2) (n-1)), ((n-1)s^2)/(chi^2_(1 - alpha/2) (n-1)))
    $
  ]

  因此上面的式子，可以使用上面的公式計算：

  $
  &(((n-1)s^2)/(chi^2_(alpha/2) (n-1)), ((n-1)s^2)/(chi^2_(1 - alpha/2) (n-1))) \
  =>& ((8 times 12.194)/15.51, (8 times 12.194)/2.73) \
  =>& (6.290, 35.734) ("g"^2)
  $
]
