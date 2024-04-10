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
]


#question("習題 12")[
  有限母體的情況：某民調中心對政府的某一政策進行民意調查，支持率為 $P$，試問在95%的信心水準下，若希望p的估計誤差小於 0.03，所需的樣本數應為多少？
][
  // hw
]
