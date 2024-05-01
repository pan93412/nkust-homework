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
      H_0: mu >= 510g,
      H_1: mu < 510g "(宣稱)"
    )
    $
  + 決策法則
    + 寫出拒絕 $H_0$ 的區域，也就是 *拒絕域*（Reject Region, $R R$）
    + 在 $overline(x)$ 尺度上做決策，就是 *臨界值法*
    + $overline(x)$ 的分配：母體不是常態分配，且 $n>=30$
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
    $overline(X)_s cancel(in) R R$，所以不拒絕 $H_0$。
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

]

== P值法

- 特性
  - 計算機率 (P值) 比較困難
  - 判斷準則單一，很簡單
- 統計軟體會幫忙計算 P 值，所以都會使用這個方法
  - 實際應用上都是使用統計軟體計算
  - 最需要清楚記得
