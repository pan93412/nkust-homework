#import "template.typ": *

#show: project.with(title: [CH9: 假設檢定], authors: ("Yi-Jyun Pan",))

#outline(indent: auto)

= 概論

在 Ch7 中，我們將已知的母體統計量 $mu$, $p$, $sigma^2$ 替換為給定 $n$ 個樣本的統計量（變數） $overline(x)$, $hat(p)$ 和 $s^2$

在 Ch8 中，我們想從 $n$ 個樣本統計量的點估計式（Ch7），推論母體統計量，如 $mu$。藉由信賴區間(C.I.)，我們可以製作出區間估計來推論 $mu$ 可能的區域範圍。

Ch9，雖然我們不知道 $mu$，但綜合專家、標識、猜測等，可以大概預測 $mu$ 落在某個點（提出假說）。 不過假說可能被認為是不可信的，所以抽出 $n$ 個樣本，將得到的 $overline(x)_s$ 點估計值當作「*證據*」驗證假說是否該「接受」還是「拒絕」。

極端的例子：(1) 假設抽樣之 $overline(x)_s = 59$，假設 $mu = 60$，這個假說是可以接受的——對立假說 ($H_0$)。(2) 假設 $n=30$，$overline(x)_s=40$，這個假說就相對不能接受（差太多了，從信賴區間來看）——虛無假說 ($H_1$)。

= 步驟 ⭐

+ $H_0$, $H_1$ 寫清楚
+ 決策法則（拒絕域），回想 Ch7 統計量分配
+ 實際抽樣資料（可能需要轉換），帶入決策法則判斷
  + 接受 $H_0$（不拒絕），或
  + 拒絕 $H_0$
+ 回到原問題，用 *白話文* 說出具體結論

= 進行假說檢定的三種方法

用於在不同尺度做決策分析。

== 臨界值法

- 特性：最直覺

=== 決策法則的流程

從 #link(<ex9.1>)[Example 9.1] 的步驟摘錄。

+ 寫出拒絕 $H_0$ 的區域，也就是 *拒絕域*（Reject Region, $R R$）
+ 在 $overline(x)$ 尺度上做決策，就是 *臨界值法*
+ 以 #link(<ex9.1>)[Example 9.1] 來說，$overline(x)$ 的分配：母體不是常態分配，且 $n>=30$
  $
  overline(x) approx N(mu, sigma^2/n), (overline(x)-mu)/(sigma/sqrt(n)) approx Z
  $
  此時把 $H_0$ 的 $mu=510$ 當真。令 $mu=M_0$ (510g), $sigma=s$, $n=49$.
+ 令小於 $c$（臨界值，critical value）的值為拒絕域。
  $
  R R = { overline(x) | overline(x) < c}
  $ <ex9.1-reject-region>
+ 拒絕域的機率是 $alpha$（顯著機率）為很有力的值。
  + 一般常約定 $alpha=0.05$（機率很小 ⭐），$alpha=0.01$（機率更小 ⭐ ⭐），$alpha=0.1$（機率非常小 ⭐ ⭐ ⭐ ）這三種。
  + $alpha$ 機率對應到 $c$
    $
    alpha &= 0.05 \
      &= P(overline(x) < c) \
      &= P(Z < (c-mu_0)/(sigma/sqrt(n))) \
      &= P(Z < (c-510)/(15/sqrt(49)))
    $
    其中
    $
    A = (c-510)/(15/sqrt(49)) = -Z_(0.05)
    $
    $A=-Z_alpha$，因為 $Z_alpha$ 才能查表。
    $
    Z_(alpha/2) &= Z_0.025 = 1.645 \
    c &= 510 + 1.645 times (15/sqrt(49)) \
      &= 506.475
    $
    *註*：$c$ 的機率可以記下來
    $
    c &= mu_0 - Z_alpha times (sigma/sqrt(n)), sigma=s
    $
    拒絕在左尾，叫做左尾檢定。

#question("ex9.1")[
  甲公司聲稱研發出一種新型的筆記型電腦，其平均重量小於 $510$ 公克，今隨機抽取 $49$ 台筆記型電腦進行測量，得到平均重量為 $overline(x)=505$ 公克，樣本標準差為 $s=15$ 公克，在顯著水準 $alpha=0.05$ 下，檢定其聲稱是否準確。
][
  *問題*：宣稱母體參數 $mu < 510"g"$，抽取 $n=49$ 個樣本，此樣本的 $overline(x)_s=505g, s=15g$. 顯著水準 $alpha=0.05$ 下，是否準確？

  *步驟*

  - 假說中只會出現 *母體參數*（$mu$, $p$, $sigma^2$）！
  - $H$ 是 Hypothesis 假說的縮寫。
  - $H_0$ 的 $0$ 是 null（虛無）的意思：虛無假說
    - *有等號 $=$ 的* 放虛無
  - $H_1$ 的 $1$ 是 alternative（對立）的意思：對立假說
    - 可以附註「宣稱」方便日後查看。

  + $
    cases(
      H_0: mu >= 510g (mu=510 "當真"),
      H_1: mu < 510g "(宣稱)"
    )
    $
  + 決策法則
    + 已知 $c=506.475$，將 $c$ 帶入@ex9.1-reject-region：
      $
      R R = { overline(x) | overline(x) < 506.475}
      $
      $n=49$, $overline(x)_s=505$ 帶入 $R R$ 判斷，可得到
      $overline(X)_s in R R$，所以拒絕 $R_0$（隱含支持對立的 $R_1$）。
    + *具體結論*#text(fill: white.darken(45%))[（回去 Step 1 查看）]
      + 在 $alpha=0.05$ 下，接受廠商筆電平均重量小於 $510g$ 的宣稱。
]

#question("ex9.3")[
  有一速食店業者廣告宜稱其對於在櫃檯顧客的服務等待的平均時間不會超過5分鐘，但消基會接到電話申訴等待時間並不如同速食店業者之廣告宣稱，認為服務等待的平均時間超過5分鐘，消基會在櫃檯隨機抽取20位顧客，並觀察其服務等待時間為

  #table(
    columns: (1fr,)*10,
    stroke: none,
    [4.5], [6.1], [5.2], [4.9], [5.3],
    [5.8], [4.1], [4.7], [4.8], [5.0],
    [4.2], [4.9], [5.0], [7.2], [5.1],
    [4.5], [4.8], [5.3], [5.4], [6.2]
  )

  假設母體爲常態分配，試在顯著水準 $alpha=0.01$ 下，檢定速食店業者之廣告宜稱是否準確。
][
  宣稱的等待時間母體 $mu<=5$，抽取 $n=20$ 個樣本，其 $overline(x)_s=5.15, s=0.73$，
  想要知道在 $alpha=0.01$ 下，宣稱是否準確？

  + $
    cases(
      H_0: mu <= 5 "(宣稱)",
      H_1: mu > 5
    )
    $
  + 決策法則 ($alpha=0.01$, $because$ $sigma^2$ 未知，$n<20$ 小樣本，故使用 $t$ 分配)
    $
    R R = { overline(x) | overline(x) > c}
    $
    （因為期待 $overline(x)>c$，故屬於右尾）
    $
    (overline(x)-mu_0)/(s/sqrt(n)) tilde t(n-1)
    $
    #figure(caption: [$mu=5.15$, $s=0.73$, $n=20$ 的 $t$ 分配], image("assets/q9.2.png"))
    $
    c &= 5 + t_(0.01)(19) times (0.73/sqrt(20)) \
      &approx 5.41
    $
  + $n=49$, $overline(x)_s=5.15$ 代入 $R R = { overline(x) | overline(x) > 5.41 }$ 判斷，可得到
    $overline(X)_s in.not R R$，所以不拒絕 $H_0$。
  + *具體結論*：在 $sigma=0.01$ 下，接受廠商平均等候時間不會超過5分鐘的宣稱。
]

#question("ex9.2")[
  有一廠商根據過去經驗其所生產之輪胎平均壽命 $50,000$ 英哩，標準差為 $sigma=3,000$ 英哩，該廠商使用新的製程生產輪胎，聲稱其新生產的輪胎平均壽命已經改變，不再是平均壽命 $mu=50,000$ 英哩，該廠商品管人員隨機抽取 $40$ 個輪胎樣本進行測試，得到平均壽命為 $overline(x)=48,500$ 英哩，在顯著水準 $alpha=0.05$ 下，檢定其聲稱是否準確。
][
  宣稱的母體參數 $sigma=3000$, $mu eq.not 50,000$（互補 $mu=50,000$），抽出 $n=40$ 個樣本，其參數為 $overline(x)_s=48,500$。

  + $
    cases(
      H_0: mu = 50000,
      H_1: mu eq.not 50000 "(宣稱)"
    )
    $
  + 決策法則
    + $mu$, $sigma$ 均已知，$n>=30$，故使用 $Z$ 分配
      #figure(caption: [$mu=48,500$, $sigma=3,000$, $n=40$ 的 $Z$ 分配], image("assets/q9.3.png"))
      $
      R R = { overline(x) | overline(x) < c or overline(x) > c}
      $
      因為 $n=40>30$ 為大樣本，根據 C.L.T 使用 $Z$ 分配。
      $
      overline(X) approx_("C.L.T") N(mu=mu_0, sigma^2=(s/sqrt(n))^2)
      $
      $
      c_1 &= mu_0 - Z_(alpha/2) dot sigma/sqrt(n) \
         &= 50000 - Z_(0.025) times 3000/sqrt(40) \
         &= 50000 - 1.96 times 3000/sqrt(40) \
         &approx 49070.29
      $
      $
      c_2 &= mu_0 + Z_(alpha/2) dot sigma/sqrt(n) \
         &= 50000 + Z_(0.025) times 3000/sqrt(40) \
         &= 50000 + 1.96 times 3000/sqrt(40) \
         &approx 50929.71
      $
      代回 $R R$:
      $
      R R = { overline(x) | overline(x) < 49070.29 or overline(x) > 50929.71}
      $
  + $n=40$, $overline(x)_s=48,500$ 代入 $R R$ 判斷，可得到
    $overline(X)_s in R R$，所以拒絕 $H_0$。
  + *具體結論*：在 $alpha=0.05$ 下，接受廠商輪胎平均壽命為 $50,000$ 英哩的宣稱。
]

== 標準統計量檢定法

- 轉到 *查表分配* 的尺度進行判斷
- 特性
  - 拒絕域比較簡單
  - 手作檢定比較容易
- 之後的章節，檢定都用這種方法

#question("ex9.4")[
  在 #link(<ex9.1>)[ex9.1] 中，試運用標準統計量檢定法，在顯著水準 $alpha=0.05$ 時，檢定甲公司之聲稱是否準確。
][
  *問題*：宣稱母體參數 $mu < 510"g"$，抽取 $n=49$ 個樣本，此樣本的 $overline(x)_s=505g, s=15g$. 顯著水準 $alpha=0.05$ 下，是否準確？

  + $
    cases(
      H_0: mu >= 510g,
      H_1: mu < 510g "(宣稱)"
    )
    $
  + 決策法則
    + $overline(x)$ 轉換後查表分配尺度來判定
    + $n=49>30$ 為大樣本，且未宣告為常態分配，故屬於 $Z$ 分配
      $
      overline(x) approx_("C.L.T") N(mu=mu_0=510, sigma^2=(s/sqrt(n))^2)
      $
      #figure(caption: [$mu=505$, $sigma=15$, $n=49$ 的 $Z$ 分配], image("assets/q9.4.png"))
    + *轉換為標準 Z 值*
      #figure(caption: [$mu=505$, $sigma=15$, $n=49$ 的標準化後 $Z$ 分配], image("assets/q9.4-2.png"))
    + $
      R R &= { Z | Z < -Z_(alpha=0.05)} \
          &= { Z | Z < -1.645}
      $
  + $n=49$, $overline(x)_s=505$ *進行標準化*
    $
    Z = (overline(x)-mu_0)/(sigma/sqrt(n)) = (505-510)/(15/sqrt(49)) = -2.33
    $
    $-2.33 in R R$，所以拒絕 $H_0$
  + 在 $alpha=0.05$ 時，接受廠商筆電平均重量小於 $510g$ 的宣稱。

  #blk[大量使用 $Z$ 值，故這種方法又稱 $Z$ 值法]
]

#question("ex9.6")[
    在 #link(<ex9.3>)[ex9.3] 中，試運用標準統計量檢定法，在顯著水準 $alpha=0.01$ 時，檢定該速食店業者之廣告宜稱是否準確。
][
  宣稱的等待時間母體 $mu<=5$，抽取 $n=20$ 個樣本，其 $overline(x)_s=5.15, s=0.73$，
  想要知道在 $alpha=0.01$ 下，宣稱是否準確？

  + $
    cases(
      H_0: mu <= 5 "(宣稱)",
      H_1: mu > 5
    )
    $
  + 決策法則
    + $n=20<30$ 為小樣本，且未知是否為常態分配，故採用 T 分配。
      $mu$
      #figure(caption: [$mu=5.15$, $sigma=0.73$, $n=20$ 的標準化後 $t$ 分配], image("assets/q9.6.png"))
    + $
      R R &= { t | t > t_(alpha=0.01)(19)} \
          &= { t | t > 2.539}
      $
  + $n=20$, $overline(x)_s=5.15$ (分鐘)
    + $overline(x)_s$ 要先轉換成 $t$ 值
      $
      t &= (overline(x)-mu_0)/(s/sqrt(n))
        &= (5.15-5)/(0.73/sqrt(20))
        &= 0.92
      $
    + $t=0.92$ 帶入 $R R$，發現 $t in.not R$，故接受 $R_0$
  + *具體結論*：在 $alpha=0.01$ 下，接受廠商平均等候時間不會超過5分鐘的宣稱。
]

#question("ex9.5")[
  [HW] 在 #link(<ex9.2>)[ex9.2] 中，試運用標準統計量檢定法，在顯著水準 $alpha=0.005$ 時，檢定該廠商之聲稱是否準確。
][
  + $
    cases(
      H_0: mu = 50000,
      H_1: mu eq.not 50000 "(宣稱)"
    )
    $
  + 決策法則
    + $n=40>30$ 為大樣本，且已知 $mu$, $sigma$，故使用 $Z$ 分配
    + 分配圖形應為左右兩側都有 $alpha$ (故一邊為 $alpha/2$) 的 $mu=0, sigma=1$ 的圖形。
    + $
      R R &= { Z | Z < -Z_(alpha/2) or Z > Z_(alpha/2)} \
          &= { Z | Z < -Z_(0.005/2) or Z > Z_(0.005/2)} \
          &= { Z | Z < -2.576 or Z > 2.576}
      $
  + $n=40$, $overline(x)_s=48,500$ 先轉換為 $Z$ 值
    $
    Z = (overline(x)-mu_0)/(sigma/sqrt(n)) = (48500-50000)/(3000/sqrt(40)) = -3.1622776602
    $
    代入 $R R$ 判斷，$overline(X)_s in R R$，所以拒絕 $H_0$。
  + *具體結論*：在 $alpha=0.005$ 下，接受廠商輪胎平均壽命為 $50,000$ 英哩的宣稱。
]

== $p$ 值法

- 特性
  - 計算機率 ($p$ 值) 比較困難
  - 判斷準則單一，很簡單
- 統計軟體會幫忙計算 $p$ 值，所以都會使用這個方法
  - 實際應用上都是使用統計軟體計算
  - 最需要清楚記得

=== $p$ 值決策法則的概念

+ 臨界值法
  #figure(caption: [$mu=505$, $sigma=15$, $n=49$ 的 $Z$ 分配], image("assets/q9.7.png"))
+ 標準統計量檢定法
  #figure(caption: [$mu=505$, $sigma=15$, $n=49$ 的標準化後 $Z$ 分配], image("assets/q9.7-2.png"))
+ $p$ 值法
  #figure(caption: [$mu=505$, $sigma=15$, $n=49$ 的 $Z$ 分配], image("assets/q9.7-3.png"))
  + $p$ 值法的目的，就是將臨界值 $c$ 轉換為機率 $alpha$。如果轉換後的值 $in R R$，則拒絕；反之接受。
  + $p$ 值：變數 $overline(x)$ 比起 $overline(x)_s$ 值更偏向拒絕方向範圍的機率。
  + $p$ 值 $<= alpha$ $=>$ $overline(x)_s in R R$, $R R = { p | p <= alpha }$.

#question("ex9.7")[
  在 #link(<ex9.1>)[ex9.1] 中，試運用 $p$ 值檢定法，在顯著水準 $alpha=0.05$ 時，檢定甲公司之聲稱是否準確。
][
  *問題*：宣稱母體參數 $mu < 510"g"$，抽取 $n=49$ 個樣本，此樣本的 $overline(x)_s=505g, s=15g$. 顯著水準 $alpha=0.05$ 下，是否準確？

  + $
    cases(
      H_0: mu >= 510g,
      H_1: mu < 510g "(宣稱)"
    )
    $
  + 決策法則（不論任何問題，單一法則）
    $
    R R = {p space "值" | p space "值" <= alpha}, alpha = 0.05 \
    R R = {p space "值" | p space "值" <= 0.05}
    $
  + 已知 $n=49, overline(x)_s=505, s=15$.
    + $p$ 值的機率圖
      #figure(caption: [$mu=505$, $sigma=15$, $n=49$ 的 $Z$ 分配], image("assets/q9.7-4.png"))
    + $
      P"值" &= P(overline(X) < overline(x) | mu = mu_0) \
            &= P(overline(X) < 505 | mu = 510) \
            &= P(Z < (505-510)/(15/sqrt(49))) \
            &= P(Z < -2.33) \
            &= 0.01
      $
  + 代入 $R R$ 判斷，因為 $p space "值" = 0.01 in R R$，故拒絕 $H_0$
  + *具體結論*：在 $alpha=0.05$ 下，接受廠商筆電平均重量小於 $510g$ 的宣稱。
]

#question("ex9.9")[
    在 #link(<ex9.3>)[ex9.3] 中，試運用 $p$ 值檢定法，在顯著水準 $alpha=0.01$ 時，檢定該速食店業者之廣告宜稱是否準確。
][
  宣稱的等待時間母體 $mu<=5$，抽取 $n=20$ 個樣本，其 $overline(x)_s=5.15, s=0.73$，想要知道在 $alpha=0.01$ 下，宣稱是否準確？

  + $
    cases(
      H_0: mu <= 5 "(宣稱)",
      H_1: mu > 5
    )
    $
  + 決策法則
    $
    R R = {p space "值" | p space "值" <= alpha}, alpha = 0.01 \
    R R = {p space "值" | p space "值" <= 0.01}
    $
  + 已知 $n=20, overline(x)_s=5.15, s=0.73$.
    #figure(caption: [$mu=5.15$, $sigma=0.73$, $n=20$ 的 $t$ 分配], image("assets/q9.9.png"))
    $
    P(overline(X) > overline(x)_s) &= P(overline(X) > 5.15) \
      &= P((overline(x)-mu_0)/(s/sqrt(n)) > (5.15-5)/(0.73/sqrt(20))) \
      &= P(t(19) > 0.92)
    $
    考慮到 $t_(0.100)(k) = 1.328$, $t_(0.050)(k) = 1.729$，往右走數字愈小。$overline(x)_s$ 在左邊，其 $p$ 值肯定大於 $0.1$，故接受 $H_0$。
    #figure(caption: [$mu=5.15$, $sigma=0.73$, $n=20$ 的 $t$ 機率與 $p$ 值關係], image("assets/q9.9-2.png"))
  + *具體結論*：在 $alpha=0.01$ 下，接受廠商平均等候時間不會超過5分鐘的宣稱。
]

#question("ex9.8")[
  在 #link(<ex9.2>)[ex9.2] 中，試運用 $p$ 值檢定法，在顯著水準 $alpha=0.005$ 時，檢定該廠商之聲稱是否準確。
][
  宣稱的母體參數 $sigma=3000$, $mu eq.not 50,000$（互補 $mu=50,000$），抽出 $n=40$ 個樣本，其參數為 $overline(x)_s=48,500$。

  + $
    cases(
      H_0: mu = 50000,
      H_1: mu eq.not 50000 "(宣稱)"
    )
    $
  + 決策法則
    $
    R R = {p space "值" | p space "值" <= alpha}, alpha = 0.005 \
    R R = {p space "值" | p space "值" <= 0.005}
    $
  + 已知 $n=40, overline(x)_s=48500, s=3000$。因為 $n=40>30$ 為大樣本，根據 C.L.T 使用 $Z$ 分配。
    $
    overline(X) approx_("C.L.T") N(mu=mu_0, sigma^2=(s/sqrt(n))^2)
    $
    #figure(caption: [$mu=48500$, $sigma=3000$, $n=40$ 的 $Z$ 分配及 $c$ 區塊], image("assets/q9.8.png")) <fig-q9.8-1>
    從 @fig-q9.8-1 可以理解 $overline(x)_s < mu_0$ 為左尾 $R R$ 區域 ($p'$)；$overline(x)_s > mu_0$ 為右尾 $R R$ 區域 ($p'$)。$2 times p' space "值" <= alpha/2 times 2 = p space "值" <= alpha$.

    $
    P space "值" &= 2 times P(overline(X)  < overline(x)_s) \
                 &= 2 times P((overline(x)-mu_0)/(sigma/sqrt(n)) < (48500-50000)/(3000/sqrt(40))) \
                 &= 2 times P(Z < -3.162) \
                 &= 2 times P(Z > 3.16) \
                 &= 2 times 0.0008 = 0.0016
    $

    考慮到 $P space "值" = 0.0016$ $in R R$，故拒絕 $R_0$.
  + *具體結論*：在 $alpha=0.005$ 下，接受廠商輪胎平均壽命不再是 $50,000$ 英哩的宣稱。
]

= 對母體比例 $p$ 的假說檢定

#question("ex9.10")[
  乙公司根據過去資料在台北市家庭使用其生產之產品的佔有率為 20%，公司使用新的製程改善產品品質後，聲稱其新產品之市場佔有率超過 20%，於是隨機抽取 100 戶進行電話訪查，其中有 30 戶使用其產品，試在顯著水準 $alpha=0.01$ 時，檢定乙公司所聲稱產品之市場占有率超過 20% 是否準確。
][
  母體宣稱 $p>0.2$，從中抽取 $n=100$ 個樣本，其中樣本的 $overline(x)=30, hat(p) = 0.2$，欲求顯著水準 $alpha=0.01$ 是否成立。

  + $
    cases(
      H_0: P <= 0.2,
      H_1: P > 0.2 "(宣稱)"
    )
    $
  + 決策法則
    + 當 $n p >=10$ 且 $n(1-p) >= 10$ 時，
      $
      hat(p) approx_("C.L.T.") N(p, p(1-p)/n)
      $
    + 臨界值法
      $
      R R = { hat(p) | hat(p) > c } \
      c = P_0 + Z_(alpha) times sqrt((P_0(1-P_0))/n)
      $
    + 標準統計量檢定法
      #figure(caption: [$p=0.3$, $n=100$ 的 $Z$ 分配 in 標準統計量檢定法], image("assets/q9.10.png"))
      $
      R R &= { Z | Z > Z_(alpha) } \
          &= { Z | Z > Z_0.01 } \
          &= { Z | Z > 2.33 }
      $
    + $p$ 值法
      $
      R R &= { p space "值" | p space "值" <= alpha } \
          &= { p space "值" | p space "值" <= 0.01 }
      $
  + 確認是否在拒絕域
    + 臨界值法
      $
      c &= 0.2 + 2.33 times sqrt((0.2(1-0.2))/100) \
        &= 0.2 + 2.33 times sqrt(0.16/100) \
        &= 0.2932
      $
      $
      R R = { hat(p) | hat(p) > 0.2932 }
      $
      $n=100$, $hat(p)=30/100=0.3$ 代入 $R R$ 判斷，可得到 $overline(X)_s in R R$，所以拒絕 $H_0$。
    + Z 值法
      將 $n=100$, $hat(p)=30/100=0.3$ 進行標準化：
      $
      Z = (hat(p)_s-P_0)/sqrt((P_0(1-P_0))/n) = (0.3-0.2)/sqrt((0.2(1-0.2))/100) = 2.5
      $
      $2.5$ 帶入 $R R$ 發現 $2.5>2.33$ $in R R$，故拒絕 $H_0$.
    + p 值法
      $n=100, hat(p)_s=30/100=0.3$.

      $
      p space "值" &= P(hat(p) > 0.3) \
                   &= P(Z > (0.3-0.2)/(sqrt((0.2(1-0.2))/100)) \
                   &= 0.0062
      $

      帶入 $R R$ 判斷，發現 $p space "值" in R R$，故拒絕 $H_0$.
  + *具體結論*：在 $alpha=0.01$ 下，接受乙公司所聲稱產品之市場占有率超過 20% 的宣稱。
]

= 母體變異數的假設檢定

== 臨界值檢定法

#question("ex9.13")[
  某廠商廣告宣稱其所生產滑鼠內之圓球直徑標準差不會超過 0.01公分，今某獨立消費團體隨機抽取 25 個滑鼠，發現滑鼠內之圓球直徑樣本標準差為 $s=0.012$ 公分，假設滑鼠內之圓球直徑分配為常態分配，試在顯著水準 $alpha=0.05$ 下，檢定該廠商之廣告宣稱是否值得採信？
][
  廠商宣稱母體的 $sigma <= 0.01$，從中抽出 $n=25$ 個樣本，其中 $s=0.012$，想知道在 $alpha=0.05$ 下是否可以採信。

  由於未知標準差的抽樣分配（只知道變異數 $s^2$），故對 $s=0.012$ 進行平方。

  *Step 1: 虛無和對立假說*

  $
  cases(
    H_0: sigma^2 <= 0.01^2 "(宣稱)" \
    H_1: sigma^2 > 0.01^2
  )
  $

  *Step 2: 抽樣尺度、決策法則*

  #figure(caption: [Q9.13 $"df"=24$ 的卡方分配], image("assets/q9.2.png"))

  $
  R R = { s^2 | s^2 > c }
  $

  $
  alpha = P(s^2 > c) &= P(((n-1) dot S^2)/sigma^2 > ((n-1) dot c) / sigma_0^2) \
  &= P(chi^2(24) > (24c)/(0.01^2))
  $

  // wip: why??

  $
  c &= (sigma_0^2 times chi_alpha^2(n-1))/(n-1) \
    &= ((0.01)^2 dot chi_(0.05)^2(24))/24 \
    &= (0.0001 times 36.4150)/24 \
    &= 0.000152
  $

  最終整理為

  $
  R R = { s^2 | s^2 > 0.000152 }
  $

  *Step 3: 判斷是否落在拒絕域*

  $n=25, s^2 = 0.012^2 = 0.0001444$ 代入 $R R$ 判斷，可以發現 $s^2 in.not R R$，故接受 $H_0$

  *Step 4: 實際結論*

  在 $alpha=0.05$ 下，接受滑鼠直徑標準差不超過 0.01cm 的宣稱。
]

== 標準統計量檢定法

#question("ex9.14")[
  在例9.13 中，試應用 $chi^2$ 檢定，在 $alpha=0.05$ 下，檢定該廠商之廣告宣稱是否值得採信？
][
  *Step 1: 虛無和對立假說*

  $
  cases(
    H_0: sigma^2 <= 0.01^2 "(宣稱)" \
    H_1: sigma^2 > 0.01^2
  )
  $

  *Step 2: 檢定統計量和決策法則*

  $n=25, sigma=0.05, chi_0.05^2(24)=36.42$

  $
  R R = { chi^2 | chi^2 > chi^2_alpha(n-1) } \
  R R = { chi^2 | chi^2 > 36.42 }
  $

  *Step 3: 判斷是否落在拒絕域*

  $n=25, s^2=0.012^2$

  $
  chi^2 &= ((n-1) dot s^2)/(sigma_0^2) \
     &= (24 times 0.012^2)/(0.01^2) \
     &= 34.56
  $

  發現到 $chi^2=34.56 cancel(>) 36.42$，$chi^2 in.not R R$，故接受 $H_0$

  *Step 4: 實際結論*

  在 $alpha=0.05$ 下，接受滑鼠直徑標準差不超過 0.01cm 的宣稱。
]

==
