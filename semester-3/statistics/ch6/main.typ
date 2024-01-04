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

(wip, 下週)

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
  + $E[g_1(Y) + g_2(Y) + ... + g_k(Y)] = E[g_1(Y)] + E[g_2(Y)] + ... + E[g_k(Y)]$ (線性組合)
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

/*

// wip - not categorized

= 常態分配求解

+ 計算機率
+ 找落點
+ 方法：畫圖+查表

// wip: organize the photos

❶ 表示 ❶.
