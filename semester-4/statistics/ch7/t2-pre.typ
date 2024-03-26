#import "template.typ": *

#show: project.with(title: [CH7: 抽樣與抽樣分配 – 第2次小考 (Pre)], authors: ("Yi-Jyun Pan",))

#question("Group 1")[
  假設 $x$ 表示某高中女生的體重，已知其分配為平均數 $mu=55$，而標準差 $sigma$ 未知的常態分配，亦即 $X tilde N(55, sigma^2)$。

  倘若今從班級中隨機抽出 $n=9$ 位女學生當成樣本，其樣本標準差 $s=2$，則這 9 位女同學之平均體重 $overline(x)$ 在某一數值 $k$ 以下的機率為0.99，試求此 $k$ 值為多少?($k$ 值四捨五入取到小數點後第 2 位)

  F: #badge(blue)[Student-T Distribution]
][
  *Concept*

  Since $sigma$ is unknown, we should use t-distribution to solve this problem.

  The t-distribution can be defined as follows:

  $
  T = (overline(X) - mu)/(s/sqrt(n)) tilde t(n-1)
  $

  where $t(n-1)$ is the t-distribution with $n-1$ degrees of freedom.

  *Abstraction of question*

  We are asked to find the value of $k$ such that $P(overline(X) <= k) = 0.99$.

  Meanwhile, we have known $mu=55$ and $s=2$.

  *Solution*

  Since $n=9$, we can use the t-distribution with 8 degrees of freedom.

  $
  P(overline(X) <= k) &= 0.99 \
  P((overline(X) - 55)/(2/3)) <= (k-55)/(2/3)) &= 0.99 \
  P(T <= (3(k-55))/2) &= 0.99 \
  P(T <= 1.5k-82.5) &= 0.99 \
  P(T >= 1.5k-82.5) &= 0.01
  $

  According to the t-distribution table, we can find that $t_(0.995)(8) = 2.896$. Therefore:

  $
  1.5k-82.5 = 2.896 \
  k approx bold(56.93)
  $
]

#question("Group 2")[
  假設台北市某計程車行通常每天耗用的燃料費為一常態分配，平均數為30元，標準差為5元，若某家計程車行有5輛計程車，試問：

  + 此5輛計程車平均值的機率分配為何？並求其平均值與變異數？
  + 在台北市隨機抽取一輛計程車，其每天耗用的燃料費超過35元的機率為多少？
  + 某家計程車行有5 輛計程車，則5輛計程車每天平均的燃料費為多少元？其平均值超過 35元的機率為何？

  F: #badge(green.darken(50%))[Normal Distribution for Samples]
][
  + 因為 $sigma=5$ 已知且為常態分配，故 $overline(X) tilde N(overline(x)=30, s^2=5^2/5=5)$
  + 這裡計算「母體」之標準差分佈。
    $
    &P(x >= 35) \
    =& P((x-30)/5 >= (35-30)/5) \
    =& P(Z >= 1.00) = 0.01587
    $
    答案是 1.58%。
  + for 5 輛計程車的平均，為樣本之常態分配。
    $
    &P(overline(X) >= 35) \
    =& P((overline(X)-30)/sqrt(5) >= (35-30)/sqrt(5)) \
    =& P(Z >= 2.23606) = 0.0125
    $
    答案是 1.25%。
]

#question("Group 3")[
  假設 $T$ 服從自由度為 $r$ 的 $t$ 分配，試著求出下列的各機率值。

  + 當自由度 $r=6$ 時，$P(T>=1.44)$.
  + 當自由度 $r=6$ 時，$P(T <= 1.44)$.
  + 當自由度 $r=6$ 時，$P(abs(T) >= 1.44)$.
  + 當自由度 $r=7$ 時，$P(-1.895 < T < 2.998)$.

  F: #badge(blue)[Student-T Distribution]
][
  *Q1*

  According to t-distribution table, we can find that $t_(alpha = 0.100)(k) = 1.440$. Therefore:

  $
  P(T >= 1.44) = alpha = bold(0.1)
  $

  *Q2*

  To turn $P(T<t(k))$ to $P(T>t(k))$, we minus the original probability from 1.

  $
  P(T <= 1.44) = 1 - P(T >= 1.44) = bold(0.9)
  $

  *Q3*

  Since $t$ distribution is symmetric, we can calculate the probability of $P(T >= 1.44)$ and multiply it by 2.

  $
  &P(abs(T) >= 1.44) \
  =& P(T >= 1.44) + P(T <= -1.44) \
  =& 2 times P(T >= 1.44) = 2 times 0.1 = bold(0.2)
  $

  *Q4*

  According to t-distribution table, we can find that $t_(0.050)(k) = 1.895$ and $t_(0.010)(k) = 2.998$. Therefore:

  $
  &P(-1.895 < T < 2.998) \
  =& 1 - P(T >= 2.998) - P(T <= -1.895) \
  =& 1 - 0.010 - 0.050 \
  =& bold(0.940)
  $
]

#question("Group 4")[
  某國家的銀髮族(75 歲以上者)中有70%為女性，今隨機抽取1000 個銀髮族為樣本，試問此1000 人中超過350 人為男性的機率為何?

  F: #badge(yellow.darken(50%))[Sample Proportion]
][
  因為是二項分配，故適用於「樣本比例」。令 $p=1-70%=0.3$ 為母體中為男性的比例；$hat(p)$ 為抽樣樣本中為男性的比例。欲求：

  $
  P(hat(p)>=0.35) = space ?
  $

  由中央極限定理，當 $n$ 足夠大時，$hat(p)$ 之分配會接近常態分配 $N(mu=p, sigma^2=p(1-p)/n)$。因此，我們可以利用常態分配的性質來求解。

  $
  E[hat(p)] = p = 0.3 \
  V(hat(p)) = p(1-p)/n = (0.7 times 0.3)/1000 = 0.00021 \
  sigma = sqrt(V(X)) = 0.01449
  $

  $
  &P(hat(p)>=0.35) \
  <=>& P((hat(p)-0.3)/0.0458 >= (0.35-0.3)/0.01449) \
  <=>& P(Z >= 3.45) \
  =& 0.0003
  $

  因此，超過 35 人為男性的機率為 0.03%。
]

#question("Group 5")[
  某國家的銀髮族(65 歲以上者)中有60%為女性，今隨機抽取300 個銀髮族樣本，試問300 人中超過100 人為男性的機率為何？

  F: #badge(yellow.darken(50%))[Sample Proportion] \
  Like: Group 4
][
  *Concept*

  Since it is a binomial distribution, we can use the *sample proportion* to solve this problem.

  The sample proportion has these properties:

  $
  E[hat(p)] = p \
  V(hat(p)) = p(1-p)/n
  $

  Besides, the Z value of normal distribution in the possibility can be calculated from:

  $
  Z = (x_i - E[hat(p)])/sqrt(V(hat(p)))
  $

  *Abstraction of question*

  Let $p$ be the proportion of elder men:

  $
  p = 1-0.6=0.4
  $

  We are asked to find the probability of $P(hat(p) > 0.33)$.

  *Solution*

  According to the _central limit theorem_, *when $n$ is large enough ($n p>5, n(1-p)>5$)*, the distribution of $hat(p)$ will be close to the normal distribution $N(mu=p, sigma^2=p(1-p)/n)$:

  $
  E[hat(p)] = p = 0.4 \
  V(hat(p)) = p(1-p)/n = (0.6 times 0.4)/300 = 0.0008 \
  sigma = sqrt(V(X)) = 0.0283
  $

  $
  &P(hat(p) > 0.33) \
  =& P((hat(p) - 0.4)/0.0283 > (0.33-0.4)/0.0283) \
  =& P(Z > -2.47) = 1 - P(Z <= -2.47) \
  =& 1 - P(Z >= 2.47) = 1-0.0068 = bold(0.9932)
  $
]

#question("Group 6")[
  假設 $T$ 服從自由度為 $r$ 的 $t$ 分配，試著求出下列機率值：

  + 當自由度 $r=1$ 時，$P(T >= 6.314)$.
  + 當自由度 $r=1$ 時，$P(T < 6.314)$.
  + 當自由度 $r=1$ 時，$P(abs(T) >= 6.314)$.
  + 當自由度 $r=2$ 時，$P(-1.866 < T < 4.303)$.

  F: #badge(blue)[Student-T Distribution] \
  Like: Group 3
][
  *Q1*

  According to t-distribution table, we can find that when $r=1$, $t_(0.050)(k) = 6.314$. Therefore:

  $
  P(T >= 6.314) = bold(0.050)
  $

  *Q2*

  To turn $P(T<t(k))$ to $P(T>t(k))$, we minus the original probability from 1.

  $
  P(T < 6.314) = 1 - P(T >= 6.314) = bold(0.950)
  $

  *Q3*

  Since $t$ distribution is symmetric, we can calculate the probability of $P(T >= 6.314)$ and multiply it by 2.

  $
  &P(abs(T) >= 6.314) \
  =& P(T >= 6.314) + P(T <= -6.314) \
  =& 2 times P(T >= 6.314) = 2 times 0.050 = bold(0.100)
  $

  *Q4*

  According to t-distribution table, we can find that $t_(0.100)(k) = 1.866$ and $t_(0.025)(k) = 4.303$. Therefore:

  $
  &P(-1.866 < T < 4.303) \
  =& 1 - P(T >= 4.303) - P(T <= -1.866) \
  =& 1 - 0.025 - 0.100 \
  =& bold(0.875)
  $
]

#question("Group 7")[
  假設某一母體比例 $p=0.8$，當樣本大小 $n$ 各為$100$、$400$、$1600$ 時，則樣本比例 $hat(p)$ 的標準差各多少？並且說明當樣本數增加時，對樣本比例 $hat(p)$ 的標準差大小會有什麼影響？
][
  *Concept*

  The sample proportion has these properties:

  $
  E[hat(p)] = p \
  V(hat(p)) = p(1-p)/n
  $

  *Solution*

  $
  n=100,space&V(hat(p))=(0.8 times 0.2)/100 = 0.0016 \
  n=400,space&V(hat(p))=(0.8 times 0.2)/400 = 0.0004 \
  n=1600,space&V(hat(p))=(0.8 times 0.2)/1600 = 0.0001
  $

  We can find that *the variance of $hat(p)$ decreases as the sample size increases.* Therefore, the standard deviation of $hat(p)$ will decrease as the sample size increases.

  樣本愈大，樣本比例標準差愈小。
]

#question("Group 8")[
  設某電子產品的電池壽命呈現常態分配，其平均壽命為400小時，標準差為10小時。從這批電池中抽取樣本數為25的150個可能樣本。

  試求：

  + 樣本平均壽命之抽樣分配的期望值與標準差。
  + 樣本平均壽命介於395小時到405小時之間的樣本個數。
  + 樣本平均壽命大於397小時的樣本個數。
][
  *Concept*

  Since the battery life is normally distributed, we can use the *sample mean* to solve this problem.

  The sample mean has these properties:

  $
  E[overline(X)] = mu \
  V(overline(X)) = sigma^2/n
  $

  *Solution*

  _Q1._ According to the _central limit theorem_, the distribution of the sample mean is $N(mu=400, sigma^2=10^2/25=4)$.

  _Q2._

  $
  &P(395 < overline(X) < 405) \
  =& P((395-400)/2 < (overline(X)-400)/2 < (405-400)/2) \
  =& P(-2.5 < Z < 2.5) \
  =& 1-2 times P(Z>2.5) = 1-2 times 0.0062 = 0.9876
  $

  $
  150 times 0.9876 approx bold(148)
  $

  _Q3._

  $
  &P(overline(X) > 397) \
  =& P(Z > (397-400)/2) \
  =& 1-P(Z < -1.5) \
  =& 1-P(Z>1.5)=1-0.0668 \
  =& 0.9332
  $

  $
  150 times 0.9332 approx bold(140)
  $
]
