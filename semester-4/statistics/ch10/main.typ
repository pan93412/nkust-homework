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
  分別從兩個獨立的常態分配⺟體中收集40位男⽣與35位女⽣的體重，男⽣的樣本平均體重爲68.5公⽄，女⽣的樣本平均體重爲53.6公⽄，倘若已知男⽣和女⽣體重的標準差分別為 $sigma_1=5, sigma_2=4$ ，試求男女⽣平均體重差 $mu_1-mu_2$ 的95%信賴區間。
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
  $

  #blk[
    *延伸*：兩個母體分配不確定，$sigma_1^2, sigma_2^2$ 已知，$n_1, n_2$ 均屬於 *大樣本*，根據 C.L.T

    $
    overline(x)-overline(y) approx N(mu_1-mu_2, sigma_1^2/n_1 + sigma_2^2/n_2)
    $
  ]

    #blk[
    *延伸*：兩個母體分配不確定，$sigma_1^2, sigma_2^2$ 未知，$n_1, n_2$ 均屬於 *大樣本*，根據 C.L.T.

    $
    overline(x)-overline(y) approx N(mu_1-mu_2, s^2/n_1 + s_2^2/n_2)
    $

    $sigma$ 利用 $s$ 估算。
  ]

]
