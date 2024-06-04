#import "template.typ": *

#show: project.with(title: [CH10 - 小考4題目], authors: ("Yi-Jyun Pan",))

= Question 1

令舊機種為 $X_1$，新機種為 $X_2$

== 列出虛無假說

$
cases(
  H_0: mu_1-mu_2<0,
  H_1: mu_1-mu_2>=0 "(檢定)",
)
$

右尾檢定。

== 抽樣分配和拒絕域

因為為常態分配，且 $sigma$ 均未知，不過 $sigma_1=sigma_2$，故其抽樣分配為

$
((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1+s_2^2/n_2) tilde t(n_1+n_2-2)
$

故拒絕域 $R R$ 為 ($alpha=0.05$)

$
R R &= { t | t > t_(alpha)(10+10-2)} \
R R &= { t | t > t_(0.05)(18)} \
R R &= { t | t > 1.734}
$

== 計算檢定統計量

計算 pooled $s$

$
s_P &= sqrt(((n_1-1)s_1^2+(n_2-1)s_2^2)/(n_1+n_2-2)) \
   &= 3.255764119
$

$
t &= ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1+s_2^2/n_2) \
  &= 0.60899288
$
因為 $s_P < 1.734$, $s_P in.not R R$, 接受 $H_0$

== 結論

在 $alpha=0.05$ 下，不能接受冷氣公司的宣傳。

= Question 2

已知兩獨立母體 $X_1$, $X_2$，其樣本分別為

- $overline(X)_1$: $overline(x)_1=70, s_1=6$, $n_1=50>30$
- $overline(X)_2$: $overline(y)=55, s_2=5$, $n_2=45>30$

== 抽樣分配

獨立母體、$s_1$, $s_2$ 已知，且為大樣本，根據 C.L.T

$
overline(x)-overline(y) tilde N(mu_1-mu_2, s_1^2/n_1+s_2^2/n_2)
$

== 信賴區間

95% 的信賴區間，其 $alpha$ 為 $0.05$，$alpha/2$ 為 $0.025$。

$
Z_0.025 = 1.96
$

因此，其信賴上下界為：

$
c &= (overline(x) - overline(y)) plus.minus Z_0.025 times sqrt(s_1^2/n_1+s_2^2/n_2) \
  &= (70-55) plus.minus 1.96 times sqrt(6^2/50+5^2/45) \
  &= (12.79, 17.21)
$

故 $mu_1-mu_2$ 的 95% 信賴區間為 $(12.79, 17.21)$

= Question 3

已知兩獨立母體 $X_1$, $X_2$

- $overline(X)_1$: $overline(x) = 30000, n_1=250, s_1=1400$
- $overline(X)_2$: $overline(y) = 26000, n_2=300, s_2=1250$

欲求其 90% 信賴區間。

== 抽樣分配

因為 $n_1$, $n_2$ 都大於 30，且 $s_1$, $s_2$ 已知，根據 C.L.T. 其近似為常態分配。

$
overline(x)-overline(y) tilde N(mu_1-mu_2, s_1^2/n_1+s_2^2/n_2)
$

== 信賴區間

90% 的信賴區間，其 $alpha$ 為 $0.1$，$alpha/2$ 為 $0.05$。

$
Z_0.05 = 1.645
$

因此，其信賴上下界為：

$
c &= (overline(x) - overline(y)) plus.minus Z_0.05 times sqrt(s_1^2/n_1+s_2^2/n_2) \
  &= (30000-26000) plus.minus 1.645 times sqrt(1400^2/250+1250^2/300) \
  &= (3812.09, 4187.91)
$


= Question 4

已知兩獨立母體 $X_1$, $X_2$

- $overline(X)_1$: $n_1=145, overline(x)=4.9, s^2_1=3.45$
- $overline(X)_2$: $n_2=125, overline(y)=5.8, s^2_2=2.53$

欲檢定 $alpha=0.05$ 下，$mu_1-mu_2<0$

== 虛無假說

$
cases(
  H_0: mu_1-mu_2>=0,
  H_1: mu_1-mu_2<0 "(檢定)",
)
$

左尾檢定。

== 抽樣分配和拒絕域

常態分配，$s_1$, $s_2$ 均已知，且 $n_1$, $n_2$ 都大於 30，故其抽樣分配接近常態分配

$
overline(x)-overline(y) tilde N(mu_1-mu_2, s_1^2/n_1+s_2^2/n_2)
$

拒絕域 $R R$ 為

$
R R &= { z | z < z_(alpha)} \
    &= { z | z < z_(0.05)} \
    &= { z | z < -1.645}
$

== 計算檢定統計量

$
z &= ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1+s_2^2/n_2) \
  &= -4.29
$

因為 $z = -4.29 < -1.645$, $z in R R$，故拒絕 $H_0$

== 結論

在 $alpha=0.05$ 下，同意男同學每日念書時間少於女同學。

= Question 5

已知兩獨立母體 $X_1$, $X_2$

- $overline(X)_1$: $n_1=25, overline(x)=6, s^2_1=2.08$
- $overline(X)_2$: $n_1=20, overline(x)=7.2, s^2_1=1.85$

想求 99% 信賴區間，以及檢定 $mu_1-mu_2<0$

== 抽樣分配

因為 $overline(X)_1$, $overline(X)_2$ 均為小樣本，$sigma$ 未知且 $s_1 != s_2$，故應適用 case 4

$
(overline(x) - overline(y))/sqrt(s_1^2/n_1+s_2^2/n_2) tilde t(r)
$

其中

#blk[
  $
  r &= floor((s_1^2/n_1+s_2^2/n_2)^2)/((s_1^2/n_1)^2/(n_1-1)+(s_2^2/n_2)^2/(n_2-1)) \
    &= 41
  $
]

== 信賴區間

99% 的信賴區間，其 $alpha$ 為 $0.01$，$alpha/2$ 為 $0.005$。

$
t_(0.005)(41) = 2.423
$

因此，其信賴上下界為：

$
c &= (overline(x) - overline(y)) plus.minus t_(0.005)(41) times sqrt(s_1^2/n_1+s_2^2/n_2) \
  &= -2.33 or -0.07
$

故 $mu_1-mu_2$ 的 99% 信賴區間為 $(-2.33, -0.07)$

== 檢定

=== 虛無假說

$
cases(
  H_0: mu_1-mu_2>=0,
  H_1: mu_1-mu_2<0 "(檢定)",
)
$

左尾檢定。

=== 抽樣分配和拒絕域

見上。拒絕域為

$
R R &= { t | t < t_(0.01)(41)} \
    &= { t | t < -2.421}
$

=== 計算檢定統計量

$
t &= ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1+s_2^2/n_2) \
  &= -2.86
$

因為 $t = -2.86 < -2.421$, $t in R R$，故拒絕 $H_0$

== 結論

在 $alpha=0.01$ 下，同意男性每日睡眠時數少於女性。

= Question 6

已知兩獨立母體 $X_1$, $X_2$，其中 $sigma_1=6, sigma_2=5$

- $overline(X)_1$: $n_1=20, overline(x)=176.5$
- $overline(X)_2$: $n_2=15, overline(y)=163$

想要求出 $mu_1-mu_2$ 的 95% 信賴區間。

== 抽樣分配

因為 $sigma_1$, $sigma_2$ 已知，且為符合常態分配的獨立母體，故

$
overline(x)-overline(y) tilde N(mu_1-mu_2, sigma_1^2/n_1+sigma_2^2/n_2)
$


== 信賴區間

95% 的信賴區間，其 $alpha$ 為 $0.05$，$alpha/2$ 為 $0.025$。

$
Z_0.025 = 1.96
$

因此，其信賴上下界為：

$
c &= (overline(x) - overline(y)) plus.minus Z_0.025 times sqrt(sigma_1^2/n_1+sigma_2^2/n_2) \
  &= 9.85 or 17.15
$

故 $mu_1-mu_2$ 的 95% 信賴區間為 $(9.85, 17.15)$

= Question 7

已知兩成對母體 $X_1$, $X_2$：

#figure[
  #table(
    inset: (x: 12pt, y: 8pt),
    columns: 9,
    [*學生*], [1], [2], [3], [4], [5], [6], [7], [8],
    [*參加前*], [45], [50], [46], [59], [65], [51], [42], [55],
    [*參加後*], [50], [52], [48], [60], [65], [53], [48], [62],
    [*差距*], [-5], [-2], [-2], [-1], [0], [-2], [-6], [-7],
  )
]

欲求 $mu_1-mu_2$ 的 95% 信賴區間，並檢定在 $alpha=0.05$ 時 $mu_1-mu_2<0$.

#blk[
  $
  E[D_i] &= mu_D \
  V(D_i) &= sigma^2_D
  $
]

== 抽樣分配

因為 $n_1, n_2$ 均小於 30，且母體屬於常態分配，故

$
(overline(D)-mu_D)/(s_D\/sqrt(n)) tilde t_(alpha/2)(n-1)
$

== 信賴區間

95% 的信賴區間，其 $alpha$ 為 $0.05$，$alpha/2$ 為 $0.025$。

因為 $n_1, n_2$ 均小於 30，且母體屬於常態分配，故

$
(overline(D)-mu_D)/(s_D\/sqrt(n)) tilde t_(alpha/2)(n-1)
$

$
t_(alpha/2)(n-1) = t_(0.025)(7) = 2.365
$

因此，其信賴上下界為：

$
c &= overline(D) plus.minus t_(0.025)(7) times s_D/sqrt(n) \
  &= -5.24 or -1.01
$

故 $mu_1-mu_2$ 的 95% 信賴區間為 $(-5.24, -1.01)$

== 檢定

=== 虛無假說

$
mu_1-mu_2 = mu_D
$

$
cases(
  H_0: mu_D>=0,
  H_1: mu_D<0 "(檢定)",
)
$

左尾檢定。

=== 抽樣分配和拒絕域

拒絕域為

$
R R &= { t | t < -t_(0.05)(7)} \
    &= { t | t < -1.895}
$

=== 計算檢定統計量

$
t &= (overline(D)-mu_D)/(s_D/sqrt(n)) \
  &= (-3.125-0)/(2.532/sqrt(8)) \
  &= -3.49
$

因為 $t = -3.49 < -1.895$, $t in R R$，故拒絕 $H_0$。

=== 結論

在 $alpha=0.05$ 下，同意實驗有助於提升學生成績。

= Question 8

已知兩常態獨立 (???) 母體 $X_1$, $X_2$，其 $sigma$ 分別為 $sigma_1^2=20, sigma_2^2=35$，其中

- $X_1$: $n_1=14, overline(x)=55$
- $X_2$: $n_2=16, overline(y)=48$

想要求出 $mu_1-mu_2$ 的點估計式和 95% 信賴區間。

== 點估計式

「點估計式」是對單個 $mu_1-mu_2$ 的估計，所以

$
mu_1-mu_2 &= overline(x) - overline(y) \
           &= 55 - 48 \
           &= 7
$

== 抽樣分配

因為母體屬於獨立常態分配，且 $sigma$ 均已知，故

$
overline(x)-overline(y) tilde N(mu_1-mu_2, sigma_1^2/n_1+sigma_2^2/n_2)
$

== 信賴區間

95% 的信賴區間，其 $alpha$ 為 $0.05$，$alpha/2$ 為 $0.025$。

因此，其信賴上下界為：

$
c &= (overline(x) - overline(y)) plus.minus Z_0.025 times sqrt(sigma_1^2/n_1+sigma_2^2/n_2) \
  &= 3.27 or 10.73
$

故 $mu_1-mu_2$ 的 95% 信賴區間為 $(3.27, 10.73)$

= Question 10

已知兩母體 $X_1, X_2$
