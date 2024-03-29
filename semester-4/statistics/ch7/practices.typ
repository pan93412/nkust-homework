#import "template.typ": *

#show: project.with(title: [CH7: 抽樣與抽樣分配 – 習題], authors: ("Yi-Jyun Pan",))

#question("習題2")[
  wip
][

]
#question("習題3")[
  某研究機構想要瞭解高中教育的問題，於是在台北地區以隨機抽樣法選取 1500 名學生作為樣本。倘若已知高中各年級之人數及學業平均成績的資料如下表所示：

  #table(
    columns: (1fr,)*4,
    [*年級*], [*高一*], [*高二*], [*高三*],
    [*人數*], [12,000], [11,000], [13,500],
    [*平均成績*], [85], [80], [83]
  )

  試問：

  + 高中生學業成績之總平均數為何？
  + 若以分層比例抽樣法抽取樣本，則各年級應抽取多少名學生？
][
  *Q1*

  $
  overline{X} = (12000 times 85 + 11000 times 80 + 13500 times 83) / (12000 + 11000 + 13500) = 6041/73 = 82.7534
  $

  *Q2*

  - 高一：$1500 times 12000/(12000+11000+13500) = 493$
  - 高二：$1500 times 11000/(12000+11000+13500) = 452$
  - 高三：$1500 times 13500/(12000+11000+13500) = 555$
]

#question("習題4")[
  某工廠生產的磚塊，其平均重量 $mu=2.95$ 磅，標準差 $sigma=0.4$ 磅，試問：

  + 當抽樣數 $n=36$ 與 $n=81$ 時樣本平均數 $overline(X)$ 的抽樣分配期望值與標準差各為何？
  + 同第一小題，哪一種抽樣數其樣本平均數 $overline(X)$ 與母體平均數 $mu$ 之差在 $0.02$ 磅之內的機率會較大？
  + 同第二小題，試說明抽樣數對於樣本平均數與母體平均數之間的關係有何影響？
][
  *Q1*

  - 當 $n>30$ 時為大樣本，此時 $E[overline(X)] = mu$
  - $V(X) = (sigma^2)/n$

  Therefore, when $n=36$:

  $
  E[overline(X)] = mu = 36 \
  sqrt(V(X)) = 0.4/sqrt(36) = 0.067
  $

  When $n=81$:

  $
  E[overline(X)] = mu \
  sqrt(V(X)) = 0.4/sqrt(81) = 0.0445
  $

  *Q2*

  $
  &P(abs(overline(x)-mu)<0.02)
  =& P(abs(overline(x)-mu)<0.02) \
  $

  When $n=36, s=0.067$:

  $
  &P(-0.02/0.067 < (overline(X)-mu)/s < 0.02/0.067) \
  = &P(-0.2985 < Z < 0.2985) \
  = &Phi(0.2985) - Phi(-0.2985) \
  = &0.2358
  $

  When $n=81, s=0.0445$:

  $
  &P(-0.02/0.0445 < (overline(X)-mu)/s < 0.02/0.0445) \
  = &P(-0.4494 < Z < 0.4494) \
  = &Phi(0.4494) - Phi(-0.4494) \
  = &0.3472
  $


  We know that $P_(n=81)>P_(n=36)$, therefore $n=81$ has much higher possibility.

  *Q3*

  $
  n arrow.t, overline(X) -> mu
  $
]

#question("習題5")[
  假設有一個母體的機率分配如下：

  #table(
    columns: (1fr,)*6,
    [$x$], [1], [2], [3], [4], [5],
    [$f(x)$], [0.3], [0.1], [0.2], [0.3], [0.1]
  )

  採取「抽取放回」的方式，隨機抽出樣本大小為 2 的樣本，表為 $(X_1, X_2)$，試求：

  + 樣本平均數 $overline(X)$ 的抽樣分配。
  + 期望值 $E[overline(X)]$ 與變異數 $V(overline(X))$，其與母體之平均數及變異數間有何關係？
][
  *Q1*

  畫出 $(X_1, X_2)$ 的可能值表格：wip

  *Q2*

  $
  E[overline(X)] = sum (x dot f(x)) = 2.8
  $

  $
  sigma^2 &= E[X^2] - (E[X])^2 = 9.8-7.84 = 1.96 \
  V(overline(X)) &= sigma^2/n = 1.96/2 = 0.98
  $
]

#question("習題6")[
  設一個母體，其元素包含 $1,3,5,7$ 共 $N=4$ 個數值，今從此一母體中抽出 $n=2$ 個爲一組隨機樣本 ($X_1, X_2$)。倘若採用「抽取後放回」的方式，試求樣本平均數 $overline(X)$ 的抽樣分配、期望值 $E[overline(X)]$ 與變異數 $V[overline(X)]$。
][
  *抽樣分配*

  畫出 $(X_1, X_2)$ 的可能值表格：

  #table(
    columns: (1fr,)*5,
    [$(x_1, x_2, overline(x))$], [1], [3], [5], [7],
    [1], [(1,1),1], [(1,3),2], [(1,5),3], [(1,7),4],
    [3], [(3,1),2], [(3,3),3], [(3,5),4], [(3,7),5],
    [5], [(5,1),3], [(5,3),4], [(5,5),5], [(5,7),6],
    [7], [(7,1),4], [(7,3),5], [(7,5),6], [(7,7),7]
  )

  Therefore, for possibility – 常態分配！

  #table(
    columns: (1fr,)*8,
    [$overline(x)$], [1], [2], [3], [4], [5], [6], [7],
    [$P(overline(x))$], [1/16], [2/16], [3/16], [4/16], [3/16], [2/16], [1/16]
  )

  $
  E[overline(X)] &= sum (x dot f(x)) = 4
  $

  $
  E[overline(X)^2] &= 18.5 \
  V(overline(X)) &= 18.5 - (4)^2 = 2.5
  $
]

#question("習題7")[
同 #link(<習題6>)[習題 6.]，倘若採用「抽取後不放回」的方式，試求樣本平均數 $overline(x)$ 的抽樣分配、期望值 $E[X]$ 與變異數 $V(X)$，並且驗證

- $E[overline(x)] = mu$
- $V(overline(X)) = sigma^2/n times (N-n)/(N-1)$
][
  畫出 $(X_1, X_2)$ 的可能值表格：

  #table(
    columns: (1fr,)*5,
    [$(x_1, x_2, overline(x))$], [1], [3], [5], [7],
    [1], [], [(1,3),2], [(1,5),3], [(1,7),4],
    [3], [(3,1),2], [], [(3,5),4], [(3,7),5],
    [5], [(5,1),3], [(5,3),4], [], [(5,7),6],
    [7], [(7,1),4], [(7,3),5], [(7,5),6], []
  )

  Therefore, for possibility – 常態分配！

  #table(
    columns: (1fr,)*6,
    [$overline(x)$], [2], [3], [4], [5], [6],
    [$P(overline(x))$], [2/12], [2/12], [4/12], [2/12], [2/12],
  )

  *Q1: Is $E[overline(X)] = mu$?*

  $
  mu &= sum (x dot f(x)) = 4 \
  E[overline(X)] &= 4 \
  mu &= E[overline(X)]
  $

  *Q2: Is $V(overline(X)) = sigma^2/n times (N-n)/(N-1)$?*

  Since $n/N > 0.05$, the population is finite, therefore:

  $
  sigma^2 &= E[X^2] - (E[X])^2 = 21-4^2 = 5 \
  V(overline(X)) &= 5/2 times (5-2)/(5-1) \
       &= 5/2 times 3/4 \
       &= 15/8
  $

  vs:

  $
  E[overline(X)^2] &= 212/12 \
  V(overline(X)) &= (212/12) - 192/12 = 20/12 = 10/6 = 5/3
  $


]

#question("習題27")[
  假設 $X_1, X_2, ..., X_20$ 是從常態分配隨機抽取的一組樣本，平均數 $mu=42$，標準差 $sigma=8$，求出下列機率：

  + $P(614 < sum_(i=1)^20 (X_i-42)^2 < 1810)$
  + $P(648 < sum_(i=1)^20 (X_i-overline(X))^2 < 1929)$
][
  *Q1*

  這個式子最接近的分配型態是這樣的：

  $
  sum(X_i-mu)^2/sigma^2 ~ chi^2(n)
  $

  故：

  $
  &P(614 < sum_(i=1)^20 (X_i-42)^2 < 1810) \
  =& P(614/64 < chi^2(20) < 1810/64) \
  =& P(9.59375 < chi^2(20) < 28.28125) \
  =& chi^2(20, 9.59375) - chi^2(20, 28.28125)\
  approx& 0.975 - 0.1 = 0.875
  $

  *Q2*

  這個式子最接近的分配型態是這樣的：

  $
  sum(X_i-overline(X))^2/sigma^2 ~ chi^2(n-1)
  $

  Therefore:

  $
  &P(648 < sum_(i=1)^20 (X_i-overline(X))^2 < 1929) \
  =& P(648/64 < chi^2(19) < 1929/64) \
  =& P(10.125 < chi^2(19) < 30.140625) \
  =& chi^2(19, 10.125) - chi^2(19, 30.140625) \
  approx& 0.95 - 0.05 = 0.9
  $
]
