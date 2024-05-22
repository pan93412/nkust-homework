#import "template.typ": *

#show: project.with(title: [CH10: 兩個母體比較的統計推論], authors: ("Yi-Jyun Pan",))

#outline(indent: auto)

= 概論

- 有兩個母體 1、母體 2，想比較裡面的統計量（如 $mu_1$, $mu_2$; $p_1$, $p_2$; $sigma_1^2$, $sigma_2^2$）
- 自然想法：抽樣本出來比較
  - 假說：$H_0: mu_1=mu_2$
  - 因為在乎差值，所以轉換成 $H_0: mu_1-mu_2=0$ 或 $>$ 或 $<$。
    - 依此類推，$p_1=p_2$ 轉換成 $p_1-p_2=0$
    - $sigma$ 有不一樣的地方，$H_0: sigma_1^2=sigma_2^2$ 轉換成 $H_0: sigma_1^2/sigma_2^2 = 1$ 或 $>$ 或 $<$
    - 把 $H_0: mu_1-mu_2$, $H_0: sigma_1^2/sigma_2^2 = 1$ 的 $mu_1-mu_2$, $sigma_1^2/sigma_2^2$ 想像成新的母體參數
- 自母體 1, 2 抽出分別 $n_1$, $n_2$ 個樣本，計算樣本平均數 $overline(x)_1-overline(x)_2$、樣本比例 $hat(p)_1-hat(p)_2$、樣本變異數 $s_1^2/s_2^2$，進行統計推論
- 得知道新樣本統計量的分配，才知道如何進行檢定，故學習重點 1: *新的統計量的分配*
- 假設已知 $overline(x)_1-overline(x)_2$ 的抽樣分配，就可以透過 $overline(x)_(1,s) - overline(x)_(2,s)$ 點估計值，加上 $overline(x)_1-overline(x)_2$ 分配，對 $mu_1-mu_2$ 做 $(1-alpha) times 100%$ 的 *信賴區間(C.I.)*。
- 然後令 $mu_1-mu_2 = 0$ 為假說，可以使用 $(overline(x)_(1,s) - overline(x)_(2,s)) + (overline(x)_1 - overline(x)_2)$ 進行 *假說檢定*。

== ⼆個⺟體平均數差的統計推論

=== 例題導讀

#question("ex9.1")[
  分別從兩個獨立的常態分配⺟體中收集40位男⽣與35位女⽣的體重，男⽣的樣本平均體重爲68.5公⽄，女⽣的樣本平均體重爲53.6公⽄，倘若已知男⽣和女⽣體重的標準差分別為 $sigma_1=5, sigma_2=4$ ，試求男女⽣平均體重差 $mu_1-mu_2$ 的95%信賴區間，#highlight[以及男女平均體重是否相等]。
][
  原題目想要從母體 1 中抽取 $n_1=40$ 個樣本；母體 2 中抽取 $n=35$ 個樣本，得到第一組樣本的 $overline(x)_1=68.5, sigma=5$，第二組樣本 $overline(x)_2=51.6, sigma=4$。

  欲求：

  + $mu_1-mu_2$ 母體參數的 95% C.I.
  + 虛無假說 $H_0: mu_1=mu_2$ 在 $alpha=0.05$ 的顯著水準下做假說檢定。

  - 新的母體參數：$mu_1-mu_2$
  - 新的樣本統計量：$overline(x)_1-overline(x)_2$

  *概念 1：$overline(x_1)-overline(x_2)$ 的抽樣分配*

  - 男生母體 ($mu_1$ 未知，$sigma_1=5$) 抽取 $n_1=40$ 個樣本，其統計量 $overline(x)_1=68.5$
    $
    overline(X)_1 tilde N(mu_1, (sigma^1/sqrt(n_1))^2)
    $
  - 女生母體 ($mu_2$ 未知，$sigma_2=4$) 抽取 $n_2=35$ 個樣本，其統計量 $overline(x)_2=53.6$。
    $
    overline(X)_2 tilde N(mu_2, (sigma^2/sqrt(n_2))^2)
    $

  $overline(x)-overline(y)$ 的統計量：

  $
  E[overline(x_1) - overline(x_2)] &= E[overline(x_1)] - E[overline(x_2)] \
             &= mu_1 - mu_2 \
  bold(V(overline(x)_1-overline(x)_2) &= V(overline(x)_1) + V(overline(x)_2)) - 2 "COV"(overline(x), overline(y)) \
    &= (sigma_1^2/n_1 + sigma_2^2/n_2) - 2 "COV"(overline(x), overline(y)) \
    &= sigma_1^2/n_1 + sigma_2^2/n_2 \
    & space "where" "COV"(overline(x), overline(y)) = 0 \
    & space space because overline(x)_1, overline(x)_2 "independent" \
  $

  $overline(x)_1 - overline(x)_2$ 的分配符合 #highlight[*可加性*]，因為

  $
  Z=X+Y
  $

  $X$, $Y$ 均為常數，因為常態分配變數的線性組合還是常態分配，所以 $Z$ 也是常數。結論來說，*兩個常態母體 $sigma_1^2$, $sigma_2^2$ 已知，不論抽出 $n_1$, $n_2$ 樣本大小*

  $
  overline(x)_1-overline(x)_2 tilde N(mu_1-mu_2, sigma_1^2/n_1 + sigma_2^2/n_2)
  $ <已知母體分配-sigma已知>

  #blk[
    *延伸*：兩個 *獨立* 母體分配不確定，$sigma_1^2, sigma_2^2$ 已知，$n_1, n_2$ 均屬於 *大樣本*，根據 C.L.T

    $
    overline(x)_1-overline(x)_2 approx N(mu_1-mu_2, sigma_1^2/n_1 + sigma_2^2/n_2)
    $ <未知母體分配-sigma已知-大樣本>
  ]

    #blk[
    *延伸*：兩個 *獨立* 母體分配不確定，$sigma_1^2, sigma_2^2$ 未知，$n_1, n_2$ 均屬於 *大樣本*，根據 C.L.T.

    $
    overline(x)_1-overline(x)_2 approx N(mu_1-mu_2, s^2/n_1 + s_2^2/n_2)
    $

    $sigma$ 利用 $s$ 估算。
  ]

  *解題：$mu_1-mu_2$ 的 95% C.I.*

  本題應當利用 @未知母體分配-sigma已知-大樣本 所列之分配

  $
  overline(x)_1-overline(x)_2 approx N(mu_1-mu_2, sigma_1^2/n_1 + sigma_2^2/n_2)
  $

  將其轉為 $Z$ 值，可得

  $
  ((overline(x)_1-overline(x)_2) - (mu_1-mu-2))/(sqrt(sigma_1^2/n_1 + sigma_2^2/n_2)) approx N(0, 1) = Z
  $ <ex9.1-a-Z>

  C.I. 之機率分配：

  $
  1-alpha = 0.95 &= P(-Z_(alpha/2) < Z < Z_(alpha/2)) \
             &= P(-1.96 < Z < 1.96)
  $ <CI-possibility-for-two-group>

  #figure(caption: "C.I. 之圖像化解釋")[
    #image("assets/ex9.1-ci-explanation.png")
  ]

  將@ex9.1-a-Z 的 $Z$ 帶入@CI-possibility-for-two-group 可得

  $
  & P(-1.96 < Z < 1.96 ) \
  =& P(-1.96 < ((overline(x)_1-overline(x)_2) - (mu_1-mu-2))/(sqrt(sigma_1^2/n_1 + sigma_2^2/n_2)) < 1.96) \
  =& P(-c < mu_1-mu_2 < c)
  $

  其中 $c$ 是

  $
  plus.minus c = (overline(x)_1-overline(x)_2) plus.minus 1.96 times sqrt(sigma_1^2/n_1 + sigma_2^2/n_2)
  $

  #highlight[所以，我們可以得到 $(mu_1-mu_2)$ 的 $(1-alpha) times 100%$ C.I. 公式為]

  $
  (overline(x)_1-overline(x)_2) plus.minus Z_(alpha/2) times sqrt(sigma_1^2/n_1 + sigma_2^2/n_2)
  $ <CI-formula-for-two-group>

  將本題統計量帶入@CI-formula-for-two-group，可得

  $
  &(68.5-53.6) plus.minus 1.96 times sqrt(5^2/40 + 4^2/35) \
  =& 12.8616 or 16.9384
  $

  即為信賴區間 – $mu_1-mu_2$ 的 95% CI 為 $(12.8616, 16.9384)$。

  #blk[
    *回憶*：$mu$ 的 $(1-alpha) times 100%$ C.I.

    $
    overline(x) plus.minus Z_(alpha/2) times sigma/sqrt(n)
    $

    與@CI-formula-for-two-group 結構相當類似（推導邏輯一致），惟需記得

    $
    mu &= overline(x)_1 - overline(x)_2 \
    sigma/sqrt(n) &= sqrt(sigma_1^2/n_1 + sigma_2^2/n_2)
    $
  ]

  *解題：$H_0: mu_1=mu_2$ 的假說檢定*

  + $
    cases(
      H_0: mu_1-mu_2=0 "(宣稱)" \
      H_1: mu_1-mu_2 eq.not 0
    )
    $
    根據 $H_1$，可知為 *雙尾檢定*
  + 其抽樣分配如下
    #figure(caption: "本題假說檢定之原始抽樣分配")[
      #image("assets/ex9.1-hypothesis-testing.png")
    ]
    #figure(caption: "本題假說檢定之標準化後的抽樣分配和其拒絕域")[
      #image("assets/ex9.1-hypothesis-testing-z.png")
    ]
    考慮到是雙尾檢定，故拒絕域有兩邊（小於 $-Z_(alpha/2)$ 和大於 $Z_(alpha/2)$）。
    題目要求 $alpha=0.05$，可得拒絕域 $R R$

    $
    R R &= { Z | Z < -Z_(alpha/2) or Z > Z_(alpha/2) } \
        &= { Z | Z < -1.96 or Z > 1.96 }
    $
  + 將 $overline(x)_1-overline(x)_2$ 標準化，得到 $Z$ 值
    $
    Z &= ((overline(x)_1-overline(x)_2) - (mu_1-mu_2)) / sqrt(sigma_1^2/n_1 + sigma_2^2/n_2) \
      &= ((68.5-53.6) - 0) / sqrt(5^2/40 + 4^2/35) \
      &= 14.3233
    $
    發現到 $Z = 14.3233 > 1.96$，$Z in R R$，拒絕 $R_0$
  + 在 $alpha=0.05$ 下，拒絕男女平均體重相等的宣稱。
]

#question("ex10.3")[
  已知兩個母體的變異數分別為 $sigma_1=36$ 與 $sigma_2=25$，倘若此時從兩獨立常態分配母體中分別抽出樣本數 $n_1=12$ 與樣本數 $n_2=18$ 個隨機樣本，而第1個母體的樣本平均數為 $overline(x)=41$，第2個母體的樣本平均為 $overline(y)=32$，試著求出 $mu_1-mu_2$ 之95%的信賴區間，以及 #highlight[第一個母體的平均數是否在 $alpha=0.05$ 下大於第二個母體的平均數]？
][
  *題幹*

  令兩母體 $X$, $Y$，其中 $X$, $Y$ 均符合常態分配。

  - 從 $X$ 母體（$mu$ 未知，$sigma_1^2=26$）中抽出 $n_1=12$ 個樣本，其中這個樣本的 $overline(x)=41$。
  - 從 $Y$ 母體（$mu$ 未知，$sigma_2^2=25$）中抽出 $n_2=18$ 個樣本，其中這個樣本的 $overline(y)=32$。

  欲求：

  + $mu_1-mu_2$ 的 95% C.I.
  + $
    cases(
      H_0: mu_1 <= mu_2 \
      H_1: mu_1 > mu_2 "(宣稱)"
    )
    $ <ex9.3-question-2>
    在 $alpha=0.05$ 下，宣稱成立？

  *解題：$mu_1-mu_2$ 的 95% C.I.*

  因為兩個獨立母體的 $sigma_1^2$, $sigma_2^2$ 已知，且均屬於常態分配，根據@已知母體分配-sigma已知，$overline(x)-overline(y)$ 的抽樣分配為

  $
  overline(x)-overline(y) tilde N(mu_1-mu_2, sigma_1^2/n_1 + sigma_2^2/n_2)
  $ <ex9.3-抽樣分配>

  首先將其轉為 Z 值，可以得到

  $
  ((overline(x)-overline(y))-(mu_1-mu_2))/(sigma_1^2/n_1 + sigma_2^2/n_2) tilde N(0, 1) = Z
  $ <ex9.3-抽樣分配-Z>

  其 C.I. 機率分配，根據@CI-possibility-for-two-group，為

  $
  1-alpha = 0.95 &= P(-Z_(alpha/2) < Z < Z_(alpha/2)) \
             &= P(-1.96 < Z < 1.96)
  $

  套用 $mu_1-mu_2$ 的 C.I. 公式（@CI-formula-for-two-group）

  $
  &(overline(x)-overline(y)) plus.minus Z_(alpha/2) times sqrt(sigma_1^2/n_1 + sigma_2^2/n_2) \
  =& (41-32) plus.minus 1.96 times sqrt(36/12 + 25/18) \
  =& 4.8938 or 13.1062
  $

  即 $mu_1-mu_2$ 的 95% C.I. 為 $(4.8938, 13.1062)$。

  *解題：$alpha=0.05$ 下 $mu_1>mu_2$？*

  首先將@ex9.3-question-2 轉換為

  + 將 @ex9.3-question-2 轉換為
    $
    cases(
      H_0: mu_1-mu_2 <= 0 \
      H_1: mu_1-mu_2 > 0 "(宣稱)"
    )
    $ <ex9.3-question-2-orepr>
    為右尾檢定。
  + $overline(x)-overline(y)$ 的抽樣分配，如@ex9.3-抽樣分配 所寫，是
    $
    overline(x)-overline(y) tilde N(mu_1-mu_2, sigma_1^2/n_1 + sigma_2^2/n_2)
    $
    考慮到是右尾檢定，拒絕域為
    $
    R R = { Z | Z > Z_(alpha) }
    $
    題目要求 $alpha=0.05$，可得拒絕域
    $
    R R = { Z | Z > 1.645 }
    $ <ex9.3-reject-region>
  + 將 $overline(x)-overline(y)$ 轉換為 $Z$ 值，根據@ex9.3-抽樣分配-Z 並代入 $mu_1-mu_2=0$，為
    $
    Z &= ((overline(x)-overline(y))-(mu_1-mu_2))/(sigma_1^2/n_1 + sigma_2^2/n_2)  \
    &= ((41-32)-0)/(36/12 + 25/18) \
    &= 2.0506
    $
    由於 $Z = 2.0506 > 1.645$，$Z in R R$，拒絕 $H_0$
  + 在 $alpha=0.05$ 下，接受 $mu_1 > mu_2$ 的宣稱。
 ]
