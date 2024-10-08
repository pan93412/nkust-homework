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

#question("ex10.1")[
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
  $ <ex10.1-a-Z>

  C.I. 之機率分配：

  $
  1-alpha = 0.95 &= P(-Z_(alpha/2) < Z < Z_(alpha/2)) \
             &= P(-1.96 < Z < 1.96)
  $ <CI-possibility-for-two-group>

  #figure(caption: "C.I. 之圖像化解釋")[
    #image("assets/ex10.1-ci-explanation.png")
  ]

  將@ex10.1-a-Z 的 $Z$ 帶入@CI-possibility-for-two-group 可得

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

  #align(center)[
    $(overline(x) - overline(y))$ $plus.minus$ 查表分配的 $alpha/2$ 值 $times$ $(overline(x) - overline(y))$ 的標準差
  ]

  以此分配來說，是

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
      #image("assets/ex10.1-hypothesis-testing.png")
    ]
    #figure(caption: "本題假說檢定之標準化後的抽樣分配和其拒絕域")[
      #image("assets/ex10.1-hypothesis-testing-z.png")
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

=== 「獨立」母體屬於常態分配、$sigma$ 已知

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
    $ <ex10.3-question-2>
    在 $alpha=0.05$ 下，宣稱成立？

  *解題：$mu_1-mu_2$ 的 95% C.I.*

  因為兩個獨立母體的 $sigma_1^2$, $sigma_2^2$ 已知，且均屬於常態分配，根據@已知母體分配-sigma已知，$overline(x)-overline(y)$ 的抽樣分配為

  $
  overline(x)-overline(y) tilde N(mu_1-mu_2, sigma_1^2/n_1 + sigma_2^2/n_2)
  $ <ex10.3-抽樣分配>

  首先將其轉為 Z 值，可以得到

  $
  ((overline(x)-overline(y))-(mu_1-mu_2))/(sigma_1^2/n_1 + sigma_2^2/n_2) tilde N(0, 1) = Z
  $ <ex10.3-抽樣分配-Z>

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

  首先將@ex10.3-question-2 轉換為

  + 將 @ex10.3-question-2 轉換為
    $
    cases(
      H_0: mu_1-mu_2 <= 0 \
      H_1: mu_1-mu_2 > 0 "(宣稱)"
    )
    $ <ex10.3-question-2-orepr>
    為右尾檢定。
  + $overline(x)-overline(y)$ 的抽樣分配，如@ex10.3-抽樣分配 所寫，是
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
    $ <ex10.3-reject-region>
  + 將 $overline(x)-overline(y)$ 轉換為 $Z$ 值，根據@ex10.3-抽樣分配-Z 並代入 $mu_1-mu_2=0$，為
    $
    Z &= ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(sigma_1^2/n_1 + sigma_2^2/n_2)  \
    &= ((41-32)-0)/sqrt(36/12 + 25/18) \
    &= 4.2960
    $
    由於 $Z = 4.2060 > 1.645$，$Z in R R$，拒絕 $H_0$
  + 在 $alpha=0.05$ 下，接受 $mu_1 > mu_2$ 的宣稱。
 ]


=== 「獨立」母體屬於常態分配、$sigma$ 未知、小樣本、$sigma_1^2=sigma_2^2$

#question("ex10.4")[
  從兩個獨立的常態分配母體中，隨機抽出兩個獨立的隨機樣本，資料如 @ex10.4-sample-table 所示。若兩母體之變異數 $sigma_1^2$ 和 $sigma_2^2$ 均不知道，但 $sigma_1^2=sigma_2^2=sigma^2$，試著求出 $mu_1-mu_2$ 的 95% 信賴區間，#highlight[以及 $mu_1-mu_2$ 是否大於0]。

  #figure(caption: "")[
    #table(
      columns: 2,
      inset: (x: 24pt, y: 8pt),
      stroke: none,
      table.header[樣本1][樣本2],
      table.hline(),
      [9], [6], [10], [7], [8], [4],
      [8], [5], [9], [6], [7], [8], [12]
    )
  ] <ex10.4-sample-table>
][
  #blk[
    *不知道 $sigma_1$ 和 $sigma_2$，是怎麼知道 $sigma_1^2=sigma_2^2$ 的？*

    因為有抽出樣本，也就代表有樣本變異數 $s_1^2$ 和 $s_2^2$，而有做過檢定 $s_1^2=s_2^2$，所以才能推斷 $sigma_1^2=sigma_2^2$。

    如果 $s_1^2 = s_2^2$，則要套用本題（情況3）的公式；反之（$s_1^2 != s_2^2$），就要套用情況4的公式。

    $sigma_1^2=sigma_2^2$ 是因為 $s_1^2=s_2^2$，實務上你得先做 $s_1^2=s_2^2$ 的檢定，才能確定 $sigma_1^2=sigma_2^2$。
  ]

  *題幹*

  兩個獨立常態母體 $X$, $Y$，其 $mu_1$ 和 $mu_2$ 均未知（而想做這兩個的比較），從中抽出的 $n_1, n_2$ 均為小樣本，其樣本統計量分別為 $overline(x), overline(y)$。

  欲求：

  + $mu_1-mu_2$ 的 95% C.I.
  + $
    cases(
      H_0: mu_1-mu_2 <= 0 \
      H_1: mu_1-mu_2 > 0 "(宣稱)"
    )
    $ <ex10.4-question-2>
    在 $alpha=0.05$ 下，宣稱成立？

  *抽樣分配*

  回想 Ch7，$overline(x)$ 是常態母體，$sigma$ 未知，且屬於小樣本 ($n<30$)，其符合 $t$ 分配

  $
  (overline(x) - mu_1)/(s_1/sqrt(n_1)) tilde t(n_1-1)
  $

  $overline(y)$ 亦為如此

  $
  (overline(y) - mu_2)/(s_2/sqrt(n_2)) tilde t(n_2-1)
  $

  透過一系列證明，可以得到本 $overline(x)-overline(y)$ 的抽樣分配為

  $
  ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1+s_2^2/n_2) tilde t(n_1+n_2-2)
  $ <normal-sigma-unknown-equal-small-sample-sigma-sampling>

  不過有個 #highlight[重點]：*$s_1^2$ 和 $s_2^2$ 是不可以直接代入的*。雖然兩個母體的變異數不知道，但是題幹說明「*相等*」。既然相等，代表他們有相同的 $sigma^2_p$（$p$ 表示 pooled，共同的），所以需要發展一個 *共同的樣本變異數* $s_p^2$ 去估計它。所以 $s_1^2$ 和 $s_2^2$ 應該用共同的 $s_p^2$ 替代。

  $s_p^2$ 計算的脈絡，可以從 $s_1^2$ 和 $s_2^2$ 的計算方式一窺

  $
  s_1^2 &= sum(x_i-overline(x))^2/(n_1-1) \
  s_2^2 &= sum(y_i-overline(y))^2/(n_2-1)
  $

  可以看到 $s_1^2$ 的自由度就是 $n_1-1$，$s_2^2$ 的自由度就是 $n_2-1$，因此 $s_p^2$ 的自由度就是 $n_1+n_2-2$。因此，#highlight[$s_p^2$ 的計算方式是]

  $
  s_p^2 = ((n_1-1)s_1^2 + (n_2-1)s_2^2)/(n_1+n_2-2)
  $ <normal-sigma-unknown-equal-small-sample-sigma-sampling-sp>

  *注意：@normal-sigma-unknown-equal-small-sample-sigma-sampling 到  @normal-sigma-unknown-equal-small-sample-sigma-sampling-sp 均屬於新的統計量*。另外 $t$ 分配沒有可加性，故和 #link(<ex10.1>)[Example 10.1] 的推導方式有異。

  *解題：$mu_1-mu_2$ 的 95% C.I.*

  本題的抽樣分配為@normal-sigma-unknown-equal-small-sample-sigma-sampling-sp，將其轉為 $t$ 分配，可以得到

  $
  ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1+s_2^2/n_2) tilde t(n_1+n_2-2)
  $

  $
  s_p^2 = ((n_1-1)s_1^2 + (n_2-1)s_2^2)/(n_1+n_2-2)
  $

  其中本題兩個樣本 $n_1=6, n_2=7$，分別計算其平均數和變異數

  $
  overline(x)_1 &= (sum x_(1,i))/n = 9 \
  overline(x)_2 &= (sum x_(2,i))/n = 6 \
  \
  s_1^2 &= (sum (x_(1,i)-overline(x)_1)^2)/(n_1-1) = 2.6667 \
  s_2^2 &= (sum (x_(2,i)-overline(x)_2)^2)/(n_2-1) = 2
  $

  $
  s_p^2 &= ((7-1)2.6667 + (6-1)2)/(7+6-2) = 2.3637
  $

  首先列出其機率式 (@CI-possibility-for-two-group)，注意 $t$ 分配是從 @normal-sigma-unknown-equal-small-sample-sigma-sampling 來的：

  $
  "df" = 6+7-2 = 11 \
  1-alpha = 0.95 &= P(-t_(alpha/2)(11) < T < t_(alpha/2)(11)) \
            &= P(-2.201 < T < 2.201)
  $

  套用 C.I. 公式 @CI-formula-for-two-group（注意標準差不同），可以得到

  $
  &(overline(x)-overline(y)) plus.minus t_(alpha/2)(11) times sqrt(s_p^2/n_1 + s_p^2/2) \
  =& (9-6) plus.minus 2.201 times sqrt(2.3637/6 + 2.3637/7) \
  =& 1.1174 or 4.8826
  $

  即 $mu_1-mu_2$ 的 95% C.I. 為 $(1.1174, 4.8826)$。

  *解題：$alpha=0.05$ 下 $mu_1>mu_2$？*

  + 將 @ex10.4-question-2 轉換為
    $
    cases(
      H_0: mu_1-mu_2 <= 0 \
      H_1: mu_1-mu_2 > 0 "(宣稱)"
    )
    $ <ex10.4-question-2-orepr>
    為右尾檢定。
  + $overline(x)-overline(y)$ 的抽樣分配，如@normal-sigma-unknown-equal-small-sample-sigma-sampling-sp 所寫，是
    $
    ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1+s_2^2/n_2) tilde t(n_1+n_2-2)
    $
    考慮到是右尾檢定，拒絕域為
    $
    R R = { T | T > t_(alpha)(11) }
    $
    題目要求 $alpha=0.05$，可得拒絕域
    $
    R R = { T | T > 1.796 }
    $ <ex10.4-reject-region>
  + 將 $overline(x)-overline(y)$ 轉換為 $t$ 值，根據@normal-sigma-unknown-equal-small-sample-sigma-sampling-sp 並代入 $mu_1-mu_2=0$，為
    $
    t &= ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1+s_2^2/n_2)  \
    &= ((9-6)-0)/sqrt(2.3637/6+2.3637/7) \
    &= 3.5073
    $
    由於 $t = 3.5073 > 1.796$，$t in R R$，拒絕 $H_0$
  + 在 $alpha=0.05$ 下，接受 $mu_1 > mu_2$ 的宣稱。
]

=== 「獨立」母體屬於常態分配，$sigma$ 未知、小樣本、$sigma_1^2 != sigma_2^2$

今在一起 $overline(x)-overline(y)$ 分配

$
((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1 + s_2^2/n_2) tilde t(r)
$

#highlight[*而 $r$ 是*]

$
r = floor( (s_1^2/n_1 + s_2^2/n_2)^2 / (((s_1^2/n_1)^2)/(n_1-1) + ((s_2^2/n_2)^2)/(n_2-1)))
$ <sigma-not-equal-r-calculation>

#question("ex10.5")[
  分別從兩個獨立常態分配⺟體中抽取樣本⼤⼩為 $n_1=15$ 與及 $n_2=20$ 的兩組隨機樣本，其所得到的統計數據如下表所示：

  #figure[
    #table(
      columns: 4,
      table.header[樣本][樣本大小][樣本平均數][樣本變異數],
      [樣本 1], [15], [66], [8],
      [樣本 2], [20], [59], [6]
    )
  ]

  試著求出

  + 假如兩個獨立母體之間的變異數相等，也就是 $sigma_1^2 = sigma_2^2$ 時，$mu_1-mu_2$ 之 95% 信賴區間
  + 如果 $sigma_1^2 != sigma_2^2$ 時，其 $mu_1-mu_2$ 之 95% 信賴區間為何？
  + $mu_1-mu_2>0$ 宣稱 $alpha=0.05$ 做檢定
][
  *題幹*

  兩個常態母體互相獨立，未知其 $sigma_1^2$ 和 $sigma_2^2$ 但已知不相等。從中抽出兩個樣本，分別 $n_1=15, overline(x)=66, s_1^2=8$ 和 $n_2=20, overline(y)=59, s_2^2=6$。

  *第一題*

  本題為常態母體樣本但未知其 $sigma$，故應屬於 $t$ 分配

  $
  ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1 + s_2^2/n_2) tilde t(n_1+n_2-2) \
  $

  $
  s_1^2 &= s_2^2 = s^2_p \
      &= ((n_1-1)s_1^2 + (n_2-1)s_2^2)/(n_1+n_2-2) \
      &= ((15-1)8 + (20-1)6)/(15+20-2) = 6.8485

  $

  考慮到 $1-alpha=0.95, alpha=0.05, alpha/2=0.025$，其 95% 信賴區間數值分別如下

  $
  t_(alpha/2)(n_1+n_2-2) &= t_(0.025)(33) = 2.03 \
  c &= (overline(x)-overline(y)) plus.minus t_(alpha/2)(r) times sqrt(s_p^2/n_1 + s_p^2/n_2) \
    &= (66-59) plus.minus 2.03 times sqrt(6.8485/15 + 6.8485/20) \
    &= 5.1855 or 8.8145
  $

  故 $mu_1-mu_2$ 的 95% 信賴區間為 $(5.1855, 8.8145)$。

  *第二題*

  因為 $sigma_1^2 != sigma_2^2$，故其抽樣分配為

  $
  ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1 + s_2^2/n_2) tilde t(r)
  $ <ex10.5-q2-抽樣分配>

  $r$ 應利用 @sigma-not-equal-r-calculation 計算

  $
  r &= floor( (s_1^2/n_1 + s_2^2/n_2)^2 / ((s_1^2/n_1)^2/(n_1-1) + (s_2^2/n_2)^2/(n_2-1)) )
    &= floor( (8/15 + 6/20)^2 / ((64/15)^2/14 + (36/20)^2/19) )
    &= 27
  $

  從 $t$ 表中可以查出 $t_0.025(28)=2.048$，其 95% 信賴區間數值分別如下

  $
  c &= (overline(x)-overline(y)) plus.minus t_(alpha/2)(r) times sqrt(s_1^2/n_1 + s_2^2/n_2) \
    &= (66-59) plus.minus 2.048 times sqrt(8/15 + 6/20) \
    &= 5.1304 or 8.8696
  $

  故 $mu_1-mu_2$ 的 95% 信賴區間為 $(5.1304, 8.8696)$。

  *第三題*

  + 列出虛無和對立假設
    $
    cases(
      H_0: mu_1-mu_2 <= 0 \
      H_1: mu_1-mu_2 > 0 "(宣稱)"
    )
    $
  + 抽樣分配如 @ex10.5-q2-抽樣分配 所寫，拒絕域如下
    $
    R R &= { T | T > t_(alpha)(27) } \
        &= { T | T > 2.048 }
    $
  + 將 $overline(x)-overline(y)=0$ 代入，判斷 $t$ 值是否在拒絕域中
    $
    t &= ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1 + s_2^2/n_2)  \
    &= ((66-59)-0)/sqrt(8/15+6/20) \
    &= 7.6681
    $
    因為 $t = 7.6681 > 2.048$，$t in R R$，拒絕 $H_0$
  + 在 $alpha=0.05$ 下，接受 $mu_1 > mu_2$ 的宣稱。
]

// #question("ex10.9")[
//   某製造業公司為了要了解哪⼀家廠商所供應的零件其品便能夠決定到底要下訂單給甲廠商或是⼄廠商。因此分別各從兩家供應商隨機抽取 16 個產品來做試驗，得到甲供應商的樣本平均數 $overline(x)=300$，樣本標準差 $s_1=15$，⽽⼄供應商的樣本平均數 $overline(y)=276$，樣本標準差 $s_2=18$。在假定⼆獨立⺟體分配近似於常態分配的情況下且兩⺟體的變異數不相等，亦即 $sigma_1^2!=sigma_2^2$，試以 $alpha=0.05$ 為顯著⽔準，檢定兩家供應所提供的產品品質是否有差異。
// ][
//   今在一起 $overline(x)-overline(y)$ 分配

//   $
//   ((overline(x)-overline(y))-(mu_1-mu_2))/sqrt(s_1^2/n_1 + s_2^2/n_2) tilde t(r)
//   $

//   #highlight[*而 $r$ 是*]

//   $
//   r = floor( (s_1^2/n_1 + s_2^2/n_2)^2 / (((s_1^2/n_1)^2)/(n_1-1) + ((s_2^2/n_2)^2)/(n_2-1)))
//   $

//   *題幹*

//   兩個常態母體互相獨立，未知其 $sigma_1^2$ 和 $sigma_2^2$ 但已知不相等。從中抽出兩個樣本，分別 $n_1=15, overline(x)=66, s_1^2=8$ 和 $n_2=20, overline(y)=59, s_2^2=6$。


//   *答案*

//   $
//   95% = 1-alpha, alpha=0.05, alpha/2=0.025 \
//   c = (overline(x)-overline(y)) plus.minus t_(alpha/2)(r) dot sqrt((s_1^2/n_1) + (s_2^2/n_2))
//   $

//   $
//   r

//   $
// ]

= 成對樣本之兩個⺟體平均數差的統計推論

在 $X_(1 j)$ 和 $X_(2 j)$ 不獨立 ($"COV"(X_(1j), X_(2j)) != 0$) 的情況下，需要用樣本的差值

$
D_i=x_(1 j )-x_(2 j )
$ <10.2-Di>

來進行推論，如下表所示

#figure[
  #table(
    columns: 4,
    inset: (x: 12pt, y: 6pt),
    table.header[成對樣本][樣本1][樣本2][兩者差異],
    [1], [$X_11$], [$X_21$], [$X_11-X_21=D_1$],
    [2], [$X_12$], [$X_22$], [$X_12-X_22=D_2$],
    [$dots.v$], [$dots.v$], [$dots.v$], [$dots.v$],
    [n], [$X_1n$], [$X_2n$], [$X_1n-X_2n=D_n$]
  )
]

這樣就可以把兩母體平均數差 $mu_1-mu_2$ 的問題，轉換成單一母體平均數 $mu_D$ 的問題。得到的 $D_1, D_2, ..., D_n$ 這 $n$ 個隨機樣本，則可視為取自 *常態分配*，其母體平均數 $mu_D$ 與母體變異數 $sigma^2_D$ 之一組隨機樣本，也就是

$
E(D_i) = mu_D \
V(D_i) = sigma^2_D
$

而 $overline(D) = (sum D_i)/n$ 的抽樣分配，則如下所示：

設 $D_i = X_(1i) - X_(2i), i=1,2,...,n$，為取自常態分配，其母體平均數為 $mu_D$ 而母體變異數為 $sigma^2_D$，則 $overline(D)$ 的抽樣分配，$D_i tilde N(mu_D, sigma^2_D)$，

$
overline(D) &= 1/n sum D_i = mu_D \
S^2_D &= sum(D_i-overline(D))^2/(n-1)
$

此時 $overline(D)$ 的抽樣分配的

$
E(overline(D)) &= mu_D \
V(overline(D)) &= sigma^2_D/n
$

對於小樣本，$overline(D)$ 的抽樣分配則為 $t$ 分配，其自由度為 $n-1$，即

$
(overline(D)-mu_D)/(s_D\/sqrt(n)) tilde t(n-1)
$ <10.2-overlineD-小樣本抽樣分配>

== 例題導讀

#question("ex10.10")[
  某個⾏銷公司的老闆想嘗試看看新的紅利計查是否能夠提升公司的盈餘業續，想評估⼀下此計畫的可⾏性，因此便選了八位公司裡的銷售員來試⾏此計畫⼀段時間。此計畫在實施前與實施後的⼀週銷售量分別列表如 @ex10.10-t 所⽰：

  #figure(caption: "成對樣本資料")[
    #table(
      columns: 9,
      [],
      table.cell(colspan: 8)[銷售員],
      [], [1], [2], [3], [4], [5], [6], [7], [8],
      [實施前],
      [10], [9], [12], [8], [11], [9], [11], [10],
      [實施後],
      [13], [14], [15], [12], [14], [10], [13], [13],
    )
  ] <ex10.10-t>

  + 對每一個銷售員計算其在實施新的紅利計畫之前後的銷售差異
  + 計算樣本平均數 $overline(d)$
  + 計算樣本標準差 $s_D$
  + 求出平均每週銷售的增加量 $mu_D = mu_2-mu_1$ 的 95% 信賴區間
  + 試著以 $alpha=0.05$ 為顯著水準，檢定這個新的紅利計畫是否可以增加銷售員平均每週的銷售量 ($mu_2-mu_1>0$)
][
  *Q1*

  #figure[
    #table(
      columns: 9,
      inset: (x: 8pt, y: 6pt),
      table.cell(rowspan: 2)[],
      table.cell(colspan: 8)[銷售員],
      [1], [2], [3], [4], [5], [6], [7], [8],
      [實施前],
      [10], [9], [12], [8], [11], [9], [11], [10],
      [實施後],
      [13], [14], [15], [12], [14], [10], [13], [13],
      [$X_(2,N)-X_(1,N)$], [3], [5], [3], [4], [3], [1], [2], [3]
    )
  ]

  *Q2*

  $
  overline(D) &= (sum D_i)/N = 3 \
  $

  *Q3*

  $
  s_D &= sum(D-overline(D))^2/(n-1) &= 1.1952
  $

  *Q4*

  由於為小樣本，根據 @10.2-overlineD-小樣本抽樣分配 可以知道 $overline(D)$ 的抽樣分配為 $t$ 分配，其自由度為 $n-1=7$。

  $
  (3-mu_D)/(1.1952\/sqrt(8)) tilde t(7)
  $ <ex10.10-sampling-distribution>

  其 95% 信賴區間轉換為 $alpha$ 是 $95% = 1-alpha, alpha=0.05, alpha/2=0.025$。

  $
  c &= overline(D) plus.minus t_(alpha/2)(n-1) times s_D/sqrt(n) \
    &= 3 plus.minus t_(0.025)(7) times 1.1952/sqrt(8) \
    &= 3 plus.minus 2.365 times 0.4226 \
    &= 2.0005 or 3.9994
  $

  故在 95% 信賴區間下，平均每週銷售的增加量 $mu_D$ 為 $(2.0005, 3.9994)$。

  *Q5*

  + 列出虛無和對立假設
    $
    cases(
      H_0: mu_2-mu_1 <= 0 \
      H_1: mu_2-mu_1 > 0 "(宣稱)"
    )
    $
  + 判斷抽樣分配，建立拒絕域。

    已知其分配為 $t$ 分配 (@ex10.10-sampling-distribution) 。$alpha=0.05$。

    $
    R R &= { T | T > t_(alpha)(7) } \
        &= { T | T > 1.895 }
    $

  + 將 $overline(D)=3$ 代入，判斷 $t$ 值是否在拒絕域中

    $
    t &= (overline(D)-mu_D)/(s_D\/sqrt(n))  \
      &= (3-0)/(1.1952\/sqrt(8)) \
      &= 7.0995
    $

    由於 $t=7.0995>1.895$，$t in R R$，拒絕 $H_0$
  + 在 $alpha=0.05$ 下，接受 $mu_2-mu_1>0$ 的宣稱。
]

== 判斷

#question("例題 6")[
  一家軟體公司宣稱他們最近發展了一種新的打字軟體，可以大大改進打字員的打字速度。因此隨機抽出八位打字員，讓他們接受此軟體之訓練課程，之後看看是否能夠增進他們的打字能力。假設打字速度的母體爲一常態分配，訓練前的平均打字速度為 $mu=1$，訓練後的打字速度爲 $mu_2$。下表即爲這八位打字員的打字速度（字/分鐘）：

  #table(
    columns: 9,
    [打字員], [1], [2], [3], [4], [5], [6], [7], [8],
    [訓練前], [45], [50], [46], [59], [65], [51], [42], [48],
    [訓練後], [50], [52], [48], [60], [65], [53], [7], [55]
  )

  試著求出：

  + 是獨立/成對樣本？
  + $mu_1-mu_2$ 的 95% 信賴區間
  + 檢定此企業的宣稱是否正確
][
  *Q1*: 是成對樣本，兩個樣本有關係且以變化呈現。
]

#question("例題 8")[
  想要比較兩種訓練計畫何者可得到較佳的訓練效果，因此隨機選取 12 位員工施予訓練計畫A，另外也隨機選取12位員工施予訓練計畫 B。在完成訓練之後，所有參加訓練課程的人員都必須接受一項技能的測驗，此測驗主要在測試員工完成一項技能所花費的時間。測驗結果列表如下：（單位：分鐘）（假設兩母體為常態分配、變異數未知但相等）

  #table(
    columns: 13,
    [員工], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12],
    [計畫 A], [30], [35], [22], [41], [36], [25], [28], [35], [29], [40], [32], [30],
    [計畫 B], [26], [28], [24], [35], [31], [40], [32], [29], [25], [35], [31], [27]
  )

  試著求出：

  + 是獨立/成對樣本？
  + 兩種計畫平均數差 $mu_1-mu_2$ 的 95% 信賴區間
  + 在顯著水準 $alpha=0.05$ 下，檢定是否可認為計畫 B 的訓練效果比計畫 A 的效果還好
][
  *Q1*: 獨立樣本，兩個樣本沒有關係。
]

#question("例題 9")[

  某製造公司宣稱他們所出售的新型機種比舊型的機種在生產速度上快的多。因此分別在這兩種機型各作12次的實驗，而其所得到的生產速度列表如下：（以秒爲單位）

  #table(
    columns: 13,
    [舊機種], [32], [25], [38], [42], [29], [35], [34], [32], [36], [37], [31], [40],
    [新機種], [39], [36], [42], [35], [36], [38], [45], [32], [40], [36], [37], [38]
  )

  假設兩種機種的生產速度均爲常態分配，且兩者的母體變異數均相等，試求在顯著水準 $alpha=0.05$  下，此製造公司的宣稱是否正確。
][
  *為獨立樣本*.
]

= 兩個母體比例差 $p_1-p_2$ 之區間估計

#blk[
  *比例大樣本*

  $
  n p >= 10 and n(1-p)>= 10 \
  n_1p_1, n_1(1-p_1) >= 10 \
  n_2p_2, n_2(1-p_2) >= 10
  $ <3-big-sample>
]

#blk[
  *新的統計量和分配*

  $
  hat(p)_1-hat(p)_2
  $ <3-new-statistic>

  $
  ((hat(p)_1-hat(p)_2) - (p_1-p_2))/sqrt((p_1(1-p_1))/n_1+(p_2(1-p_2))/n_2) tilde Z
  $ <3-sampling-distribution>
]

== 大樣本，$p_1-p_2=0$

#question("ex10.12")[
  某私立大學統計系的學生因爲發覺女性抽煙的人數有日益增多的傾向，因此想要做一項統計調查，看看女性抽煙的比例是否逐漸逼近男性抽煙的比例。他從一群人中隨機抽出200位男性，發現其中有85 位有抽煙的習慣；另外也隨機抽出150位女性，發現其中有30 位有抽煙的習慣。試求兩性抽煙比例差 $p_1-p_2$ 之95%的信賴區間。
][
  *題幹*

  兩個母體 $p_1, p_2$，抽出兩個樣本：

  + $n_1=200, hat(p)_1 &= 85/200 = 0.425$ \
  + $n_2=150, hat(p)_2 &= 30/150 = 0.2$

  想要求出

  + $p_1-p_2$ 的 95% C.I.
  + $p_1-p_2>0$ 嗎？

  *Question 1*

  因為符合 @3-big-sample (大於 10)，本題之抽樣分配為 @3-sampling-distribution

  $
  ((hat(p)_1-hat(p)_2) - (p_1-p_2))/sqrt((p_1(1-p_1))/n_1+(p_2(1-p_2))/n_2) tilde Z
  $

  計算 $p_1-p_2$ 的 95% 信賴區間

  $
  c &= (hat(p)_1-hat(p)_2) plus.minus Z_(alpha/2) sqrt((hat(p)_1(1-hat(p)_1))/n_1+(hat(p)_2(1-hat(p)_2))/n_2) \
    &= 0.131 or 0.319
  $

  故 $p_1-p_2$ 的 95% 信賴區間為 $(0.131, 0.319)$。

  *Question 2*

  + $
    cases(
      H_0: p_1-p_2 <= 0 \
      H_1: p_1-p_2 > 0 "(宣稱)"
    )
    $
  + 拒絕域

    $
    R R &= { Z | Z > Z_(alpha) } \
        &= { Z | Z > 1.645 }
    $
  + 計算 $p_1-p_2$ 的 $Z$ 值。這裡要使用 pooled value

    $
    hat(p)_P &= (overline(x)_1 + overline(x)_2)/(n_1+n_2) \
       &= (85+30)/(200+150) = 0.3285714286
    $

    $
    Z &= (0.225-0)/sqrt((hat(p)_1(1-hat(p)_1))/n_1+(hat(p)_2(1-hat(p)_2))/n_2) \
      &= (0.225-0)/sqrt((hat(p)_P(1-hat(p)_P))/n_1+(hat(p)_P(1-hat(p)_P))/n_2) \
      &= 4.44
    $

    因為 $Z=4.44 > 1.645$，$Z in R R$，拒絕 $H_0$。

    故在 95% 信賴區間下，接受 $p_1-p_2>0$ 的宣稱。
]

#question("ex10.14")[
  //wip
][]

== 大樣本，$p_1-p_2!=0$

#question("ex10.13")[
  某洗面乳製造廠商廣告宣稱，購買其公司之洗面乳產品的女性顧客多於男性顧客至少20%。但消基會懷疑廠商的廣告宣稱，因此隨機抽出300位女性，其中有120位使用此產品；另外也隨機抽出200位男性，其中則有50位使用此產品。試求在顯著水準為$alpha=0.05$的條件下，檢定廠商所廣告宣稱是否正確。
][
  兩個母體 $p_1, p_2$，分別抽出 $n_1=300, hat(p)_1=120/300=0.4$ 和 $n_2=120, hat(p)_2=50/200=0.25$ 的樣本.

  *建立虛無假設*

  $
  cases(
    H_0: p_1-p_2 >= 0.2 "(宣稱)" \
    H_1: p_1-p_2 < 0.2
  )
  $

  *抽樣分配*

  因為是大樣本，所以分配是

  $
  ((hat(p)_1-hat(p)_2) - (p_1-p_2))/sqrt((p_1(1-p_1))/n_1+(p_2(1-p_2))/n_2) tilde Z
  $

  故 $p_1-p_2$ 的 $alpha=0.05$ 拒絕域為

  $
  R R = { Z | Z < Z_(alpha) } = { Z | Z < -1.645 }
  $

  *計算 $p_1-p_2$ 的 $Z$ 值*

  $
  hat(p_1)-hat(p_2) = 0.4-0.25=0.15
  $

  $
  Z &= (0.15 - 0.2)/sqrt((p_1(1-p_1))/n_1+(p_2(1-p_2))/n_2) \
    &= -1.20
  $

  因為 $Z=-1.20 > -1.645$，$Z in.not R R$，不拒絕 $H_0$。

  *結論*

  故在 $alpha=0.05$ 下，接受廠商的宣稱。
]
