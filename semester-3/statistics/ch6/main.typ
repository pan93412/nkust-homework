#import "template.typ": *

#show: project.with(title: [CH6: 連續型隨機變數及其常用的機率分配], authors: ("Yi-Jyun Pan",))

#outline(indent: auto)

= 積分入門

#blk[
  *面積的近似值*

  $
  sum_(i=1)^n f(c_i) Delta x
  $
]

#blk[
  *面積的精確值*

  $
  lim_(n->oo) sum_(i=1)^n f(c_i) Delta x \
    = integral^b_a f(x) dif x
  $
]

#blk[
  *不定積分*

  $
  integral y^n dif y = 1/(n+1) y^(n+1) + C
  $
]

#blk [
  *定積分*

  $
  integral^b_a y^n dif y = 1/(n+1) y^n+1 lr(|_a^b, size: #50%)
  $
]


== 連續型隨機變數的機率分配

+ 對所有 $Y$ 的可能值而言，$f(y) >= 0$
+ 隨機變數所有可能值的機率總和為 $1$，即：
  $
  integral^oo_(-oo) f(y) dif y = integral^b_a f(y) dif y = 1
  $ <機率總和為1>
+ 要求隨機變數 $Y$ 落在密度曲線下方與區間 $[c,d]$ 上方的面積，則：
  $
  P(c underline(<=) Y underline(<=) d) = integral^d_c f(y) dif y
  $

  $
  P(Y=y) = integral^y_y f(y) dif y = 0
  $

#question("ex6.1")[
  假設 $Y$ 是一個連續型隨機變數，且其機率密度函數為：

  $
  f(y) = cases(
    C(4y-y^2) "if" 0<=y<=3,
    0 "otherwise"
  )
  $

  試問：

  + $C$ 值
  + $P(1<=Y<=2)$
  + $P(1<Y<2)$
][
  *C 值*

  $
  &integral^oo_(-oo) f(y) dif y = 1 \
  => &integral^3_0 C(4y-y^2) dif y = 1 \
  => &C[integral^3_0 4 y dif y - integral^3_0 y^2 dif y] = 1 \
  => &C[4 dot 1/(1+1) y^(1+1) |^3_0 - 1/3 y^3 |^3_0] = 1 \
  => &C(2y^2 - 1/3 y^3)|^3_0 = 1  &space  "帶回 3, 0"\
  => &C[(2 dot 3^2 - 1/3 3^3) - 0] = 1 \
  => &9C = 1
  => C = 1/9
  $

  *$P(1<=Y<=2)$*

  $
  P(1<=Y<=2) &= integral_1^2 1/9 (4y-y^2) dif y \
  &= lr(1/9 (1/2 dot 4y^2 |_1^2 -1/3 dot y^3 |_1^2))\
  &= 1/9 (2y^2 - 1/3 y^3)|_1^2 & "(將2, 1帶回)" \
  &= 1/9 (2 dot 2^2 - 1/3 2^3 - 2 dot 1^2 + 1/3 1^3) \
  &= 1/9 (8 - 8/3 - (2 + 1/3)) \
  &= 1/9 times (18/3 - 7/3) = 1/9 times 11/3 = 11/27
  $
]

#question("ex6.2")[
  假設老鼠跑出迷宮，所花的時間是一個隨機變數 ($Y$, 分鐘)，其機率密度函數是

  $
  f(y) = cases(
    1/y^2 "if" 1<=y,
    0 "otherwise"
  )
  $

  試問老鼠在 3 分鐘內跑出迷宮的機率為何？
][
  $
    &integral^b_a f(y) dif y
  => &integral^b_a 1/y^k dif y
  => &integral^b_a y^(-k) dif y
  => &1/(-k+1) y^(-k+1) |_a^b
  $

  $
  P(Y<=3) &= integral^3_1 1/y^2 dif y \
  &= integral^3_1 y^(-2) dif y \
  &= 1/(-2+1) y^(-2+1) |_1^3 \
  &= -y^(-1) |_1^3  "帶回 3, 1" \
  &= -3^(-1) + 1^(-1) \
  &= -1/3 + 1 \
  &= 2/3
  $
]

== 連續型隨機變數的累積分配函數

（實際教學是接在常態分配 (@常態分配) 之後。）

#blk[
  *定義 6.1.2* 一個連續型隨機變數 $Y$，其累積分配函數為：

  $
  F(y) &= P(Y <= y) \
      &= integral^y_(-oo) f(y) dif y
  $ <def-6.1.2>
]

#question("ex6.3")[
  令 $Y$ 為一個隨機變數，其機率密度函數為：

  $
  f(y) = cases(
    (1/2)(2-y) "if" 0<=y<=2,
    0 "otherwise"
  )
  $

  試求：

  + 累積分配函數 $F(y)$
  + 試著利用 $F(y)$ 求得 $P(1<=Y<=2)$
][
  *$F(y)$*


  根據定義 6.1.2 (@def-6.1.2)：

  $
  F(y) &= P(Y <= y) \
      &= integral^y_(-oo) f(t) dif t
  $

  對上式進行討論：

  #let part1(x) = text(fill: red, $#x$)
  #let part2(x) = text(fill: blue, $#x$)
  #let part3(x) = text(fill: green, $#x$)

  $
  F(y) = \
  &cases(
    part1(integral^y_(-oo) 0 dif t) &= space part1(0) \
      &space "if" 0<=y<=1,
    part1(integral^0_(-oo) 0 dif t) + part2(integral^y_0 (1/2)(2-t) dif t) &= space part2(t - 1/4 t^2 |^y_0) \
      &space "if" 1<=y<=2,
    part1(integral^0_(-oo) 0 dif t) + part2(integral^2_0 (1/2)(2-t) dif t) + part3(integral^y_2 0 dif t) &= space part2(t - 1/4 t^2 |^2_0) = 0 &space \
      &space "if" 2<=y<=oo
  )
  $

  *$P(1<=Y<=2)$*

  $
  P(1<=Y<=2) &= P(Y <= 2) - P(Y <= 1) \
             &= F(2) - F(1) \
             &= (2 - 1/4 dot 2^2) - (1 - 1/4 dot 1^2) \
             &= 1/4
  $
]

= 期望值（平均數）及變異數

#blk[
  *複習：離散型隨機變數的期望值*

  $
  E[Y] = mu = sum y p(y)
  $
]

#blk[
  *複習：離散型隨機變數的變異數*

  $
  V[Y] = sigma^2 = sum (y-mu)^2 p(y) = E[Y^2] - (E[Y])^2
  $
]

== 期望值

#blk[
  *連續型隨機變數的期望值* (def 6.2.1)

  $
  E[Y] = mu = integral^oo_(-oo) y f(y) dif y
  $
]

#blk[
  若 $g(y)$ 為連續型隨機變數 #highlight[函數]，則其期望值為： (Theorem 6.2.1)

  $
  E[g(Y)] = integral^oo_(-oo) g(y) f(y) d y
  $
]

== 變異數

根據定理 6.1，可知變異數定義如下：

#blk[
  *連續型隨機變數的變異數* (def. 6.2.2)

  $
  V[Y] = sigma^2 &= E[(Y-mu)^2] = integral^oo_(-oo) (y-mu)^2 f(y) dif y
                 &=
  $

  其正平方根 $sigma = sqrt(sigma^2) = "SD"(Y)$ 稱為隨機變數 $Y$ 的標準差。
]

#question("ex6.4")[
  $Y$ 為一個連續型隨機變數，其機率密度函數：

  $
  f(y) = cases(
    2y "if" 0<=y<=1,
    0 "otherwise"
  )
  $

  試求 $Y$ 的期望值/平均值 $E[Y]$ 及變異數 $V(Y)$。
][
  根據題幹，可列出：

  *期望值*

  $
  E[Y] &= integral^oo_(-oo) y dot f(y) d y \
       &= integral^1_0 y dot 2y dif y \
       &= integral^1_0 2 dot y^2 dif y \
       &= 2 dot 1/3 y^3 |_0^1 \
       &= 2/3 y^3 |_0^1 & "(帶入 0, 1)"\
       &= 2/3 (1^3 - 0^3) = 2/3
  $

  *變異數*

  $
  sigma^2 = V(Y) &= integral^oo_(-oo) (y-mu)^2 f(y) dif y \
                 &= integral^1_0 (y-2/3)^2 2y dif y \
                 &= integral^1_0 2y (y^2 - 4/3 y + 4/9) dif y \
                 &= integral^1_0 2y^3 - 8/3 y^2 + 8/9 y dif y \
                 &= 2 dot 1/4 dot y^4 - 8/3 dot 1/3 y^3 + 8/9 dot 1/2 y^2 |_0^1 \
                 &= 1/2 y^4 - 8/9 y^3 + 8/18 y^2 |_0^1 & "(帶入 0, 1)"\
                 &= 1/2 - 8/9 + 8/18 = 1/18

  $
]

== 基本定理

#blk[
  *定理 6.2：*若 $Y$ 是一個連續型，$a, b$ 為兩常數，$g_1(Y), g_2(Y), ..., g_k(Y)$ 為隨機變數 $Y$ 之 $k$ 個函數，則

  + $E[a Y + b] = a E[Y] + b$
  + $V(a Y + b) = a^2 V(Y)$
  + $E[g_1(Y) + g_2(Y) + ... + g_k(Y)]$ $= E[g_1(Y)] + E[g_2(Y)] + ... + E[g_k(Y)]$ (線性組合)
]

#blk[
  *定理 6.3*: 若一個連續型隨機變數 $Y$，期望值或平均數 $E[Y] = mu$，則變異數

  $
  V[Y] = sigma^2 = E[Y^2] - (E[Y])^2 = E[Y^2] - mu^2
  $
]
#question("ex6.5")[
  若 $Y$ 為一個連續型隨機變數，證明 $E[a Y+b]=a E[Y] + b$.
][
  $
  E[a Y + b] &= integral^oo_(-oo) (a y + b) f(y) dif y \
             &= integral^oo_(-oo) a y f(y) dif y + integral^oo_(-oo) b f(y) dif y \
             &= a integral^oo_(-oo) y f(y) dif y + b integral^oo_(-oo) f(y) dif y \
             &= a E[Y] + b & "(" E[Y] = integral^oo_(-oo) y f(y) dif y  ")" \
             && "(" 1 = integral^oo_(-oo) f(y) dif y  ")"
  $

  + $1 = integral^oo_(-oo) f(y) dif y$ 參考 @機率總和為1
]

#question("ex6.6")[wip-回家練習][]


// wip - not categorized

= 常態分配 <常態分配>

== 概念 (wip)

+ 計算機率
+ 找落點
+ 方法：畫圖+查表

// wip: organize the photos

#question("extra-ex.1")[
  隨機變數 $X~N$（平均數 = 18, 標準差 = 6.5）：

  - 計算 $P(X>20)$
  - 左尾機率為 95% 的落點

  // wip: img
][]


== 定義

#blk[
  *定義 6.5.1* 連續隨機變數 $Y$，若其機率密度函數為：

  $
  f(y) = 1/(sigma sqrt(2 pi)) e^(-(y-mu)^2/(2 sigma^2)), \
  -oo < y < oo, -oo < mu < oo, sigma^2 > 0
  $

  則稱 $Y$ 為一個常態分配，記為 $Y~N(mu, sigma^2)$。
]

#blk[
  *定理 6.7* 若 $Y$ 是一個常態隨機變數，$Y~N(mu, sigma^2)$，則:

  - 期望值：$E[Y] = mu$
  - 變異數：$V(Y) = sigma^2$

  #figure(caption: "常態分佈密度曲線")[
    #image("figure-6.5.png")
  ] <常態分佈密度曲線>
]

從 @常態分佈密度曲線 可知：

- 常態分佈曲線兩端尾巴和橫軸逐漸接近，但絕不和橫軸相交。
- 常態分配是以 $mu$ 為中心的左右對稱分配，且曲線形狀類似鐘形。由於其對稱性質，故有以下對稱特性：
  - $P(Y<mu) = P(Y>mu) = 0.5$
  - 對常數 $a$, $b$：
    - $P(Y < -a) = 1-P(Y<=a)=P(Y>a)$ （$P(Y < -a)$ 和 $P(Y>a)$ 面積相同，亦等於所有面積減去 $P(Y<=a)$）
    - $P(a<Y<b) = P(Y<b) - P(Y<=a)$ （$P(a<Y<b)$ 等於 $P(Y<b)$ 的範圍減去 $P(Y<=a)$）
- 常態隨機變數 $Y$ 落在以 $mu$ 為中心，左右一個標準差 $mu$ 的距離的機率為：
  $
  P(mu-sigma<Y<mu+sigma) = P(-1<Z<1) = 0.6826
  $
  落在以 $mu$ 為中心，左右兩個標準差 $mu$ 的距離的機率為：
  $
  P(mu-2sigma<Y<mu+2sigma) = P(-2<Z<2) = 0.9544
  $

== 標準常態分配和標準化

標準常態分配 (Standard Normal Distribution) 指期望值 $mu = 0$，變異數 $sigma^2 = 1$ 的常態分配。一般常態分配，可利用「標準化」程序（線性轉換）將其轉換為標準常態分配。

#blk[
  *定義 6.5.2* 連續型機率函數 $Y$，若其機率密度函數為：

  $
  f(y) = 1/sqrt(2 pi) e^(-y^2/2) &, -oo < y < oo
  $

  則 $Y$ 為一個標準常態分配，記為 $Z~N(0, 1)$。
]

通常我們以 $X$, $Y$ 表示原始資料，$Z$ 表示標準化後的資料。另 $Z$ 的累積分配函數如下：

$
  Phi(z) = P(Z<=z) = integral^z_(-oo) 1/sqrt(2 pi) e^(-y^2/2) dif y
$

由於標準常態機率密度函數是對稱的，所以 $Phi(-z) = 1-Phi(z)$。標準常態機率密度表通常都是已知的（#link("https://ie.ntu.edu.tw/dr_chen/Files/Service/normaltable.htm")[見此連結，內含 $Phi(z)$ 之表格]），故透過查詢 $Phi(Z<k)$ 表格，即可算出所有標準常態分配所需求出的機率值。

#question("ex6.11")[
  若有一個標準常態分配為 $Z~N(0,1)$，試著求出：

  + $P(Z>0)$
  + $P(Z>1.24)$
  + $P(-2<Z<2)$
  + $P(0<Z<1.64)$
][
  + $P(Z>0) = 0.5$

  + $P(Z>1.24) = 0.1075$ (查 $z=-1.24$ 的表格)
    + 或者是 $P(Z>1.24) = 1-P(Z<1.24)$，然後查 $z=1.24$ 的表格：$1-0.8925 = 0.1075$

  + $
    &P(Z<2) - P(Z < -2) \
    = &P(Z<2) - P(Z > 2) \
    = &Phi(2) - Phi(-2) \
    = &0.9772 - 0.0228
    $

    或者是：

    $
    &P(Z<2) - P(Z < -2) \
    = &P(Z<2) - P(Z>2) \
    = &P(Z<2) - (1-P(Z<2)) \
    = &0.9772-(1-0.9772)=0.9544 \
    $

  + $
    &P(0<Z<1.64) \
    = &P(Z<1.64) - P(Z<0) \
    = &Phi(1.64) - Phi(0) \
    = &0.9495 - 0.5 \
    = &0.4495
    $
]

=== 線性轉換

#blk[
  *定理 6.8* 若 $Y$ 為一個常態分配，$Y~N(mu, sigma^2)$。令：

  $
  Z = (Y-mu)/sigma
  $

  則 $Z$ 為一個標準常態分配，$Z~N(0,1)$。
]

#question("ex6.12")[
  若有一個常態隨機變數 $Y$，其期望值或平均數為 $3$，變異數為 $9$，即 $Y~N(3, 9)$，求：

  - $P(Y>0)$
  - $P(3<Y<6)$
][
  *標準化*

  $
  mu &= 3 \
  sigma^2 &= 9 => sigma = 3
  $

  *$P(Y>0)$*

  $
  P(Y>0) &=> P((Y-3)/3 > (0-3)/3) \
         &=> P(Z > -1) \
         &= 1 - P(Z < -1) \
         &= 1 - P(Z > 1) \
         &= 1 - Phi(-1) \
         &= 1 - 0.1587 \
         &= 0.8413
  $

  替代解法：

  $
  P(Y>0) &= P((Y-3)/3 > (0-3)/3) \
         &= P(Z > -1) \
         &= 1-P(Z < -1) \
         &= 1-(1-P(Z < 1)) \
         &= 1-(1-0.8413) \
         &= 0.8413
  $

  *$P(3<Y<6)$*

  $
  P(3 < Y < 6) &=> P((3-3)/3 < (Y-3)/3 < (6-3)/3) \
               &=> P(0 < Z < 1) \
               &= P(Z < 1) - P(Z < 0) \
               &= Phi(1) - Phi(0) \
               &= 0.8413 - 0.5 \
               &= 0.3413
  $
]

#question("ex6.13")[
  ⭐ 有一個入學考試，考生入學成績恰好為一個期望值或平均數為 100 分，標準差為 40 分的常態分配。試問：

  + 若隨機抽取一位考生，其成績恰好在 90 與 110 分之間的機率為何？
  + 若此項考試預估錄取率為 30%，則你能預估上榜門檻的保險分數嗎？
][
  $
  mu = 100 \
  sigma = 10
  $

  *Q1*

  列式：$P(90 < Y < 110)$. 由於 $Y$ 為常態分配，故可先標準化：

  $
  P(90 < Y < 110) &= P((90-100)/40 < (Y-100)/40 < (110-100)/40) \
    &= P(-0.25 < Z < 0.25) \
    &= P(Z < 0.25) - P(Z < -0.25) \
    &= Phi(0.25) - Phi(-0.25) \
    &= 0.5987 - 0.4013 \
    &= 0.1974
  $

  替代算法：

  $
    &P(Z < 0.25) - P(Z < -0.25) \
    = &P(Z<0.25) - (1-P(Z<0.25)) \
    = &0.5987 - (1-0.5987) \
    = &0.1974
  $

  *Q2*

  令上榜原始分數為 $k$，預期 $P(Y > k) = 0.3$.

  $
  P(Y > k) &= P((Y-100)/40 > (k-100)/40) \
    &= P(Z > (k-100)/40) \
    &= 1 - P(Z < (k-100)/40) \
    &= 1 - Phi((k-100)/40) \
    &= 0.3
  $

  #let left(x) = text(fill: red, $#x$)
  #let right(x) = text(fill: blue, $#x$)

  根據表格，已知 $Phi(left(0.52)) = right(0.3005)$ $<$ $Phi(left(z))$ $=$ $right(0.3)$ $<$ $Phi(left(0.53))$ $=$ $right(0.2995)$，故得使用「內插法」逼近 $Phi(z)$ 的值。

  *內插法*

  $
  a/b = a/b \
  => left((z-(0.52))/(0.53-0.52)) = right((0.3-0.2995)/(0.3005-0.2995)) \
  => z=0.525
  $

  $
  (A-100)/40 = 0.525 \
  => A = 121
  $
]

== 二項分配近似於常態分配

#blk[
  *定理 6.9* 若 $Y$ 為一個二項隨機變數，$Y~b(n;p)$，當其 $n$ 很大時，此時 $(Y-E[Y])/sqrt(V(Y))$ 之機率分配近似於標準常態分配。

  詳細證明見課本。
]

= 均勻分配

假設一個隨機變數 $Y$，在某一區間 $[a,b]$ 內發生的機率均相同，則 $Y$ 的機率分配稱為「均勻分配。」

#blk[
  *定義 6.3.1* 連續隨機變數 $Y$，若其機率密度函數為：

  $
  f(y) = cases(
    1/(b-a) "if" a<=y<=b,
    0 "otherwise"
  )
  $

  則 $Y$ 的機率分配稱為均勻分配。
]

// wip: 均勻分配圖 (圖 6.3)

#blk[
  *定理 6.4* 若 $Y$ 為一個均勻分配，上下界分別是 $b$ 和 $a$，$Y~U(a,b)$，則：

  - 期望值：$E[Y] = (a+b)/2$
  - 變異數：$V(Y) = (b-a)^2/12$
]
