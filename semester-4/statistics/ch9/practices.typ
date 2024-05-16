#import "template.typ": *

#show: project.with(title: [CH9: 假設檢定 – 習題], authors: ("Yi-Jyun Pan",))

#question("Question 1")[
  假設檢定是什麼？
][
  「假設檢定」指對母體參數做一個假設或主張，然後根據樣本的統計量檢定母體參數是否符合這個假設，以此來判斷這個假設是否成立。
]

#question("Question 2")[
  什麼是虛無假設和對立假設？
][
  *虛無假設*（null hypothesis, $H_0$）是對母體參數的一個假設，是我們建立而想拒絕的假設；*對立假設*（alternative hypothesis）則是我們建立而想接受的假設。
]

#question("Question 3")[
  何謂 型-I 誤差與 型-II 誤差?
][
  Type-I 誤差為「$H_0$ 為真，但拒絕 $H_0$」；Type-II 誤差為「$H_0$ 為假，但接受 $H_0$」。
]

#question("Question 4")[
  在進行假設檢定時，$alpha$ 與 $beta$ 的發生時機分別出現在何時?
][
  #table(
    columns: (2fr, 1fr, 1fr),
    [決策結果/真實情況], [$H_0$ true], [$H_1$ true],
    [接受 $H_0$], [$1 - alpha$], [$beta$],
    [拒絕 $H_0$], [$alpha$], [$1 - beta$]
  )
]

#question("Question 5")[
  颱風來襲時，要不要放假這個問題一直深深地困擾著地方首長。現假設有一強烈颱風正快速逼近本省，台北市長必須決定明天要不要放假，於是他先建立了兩個假設如下：

  $
  cases(
    H_0: "颱風不會經過台北市" \
    H_1: "颱風會經過台北市"
  )
  $

  + 「不該放假而放假」為何種誤差? (type-I or type-II)；其機率為 $alpha$ 或 $beta$ ?
  + 「該放假而未放假」為何種誤差? (type-I or type-II)；其機率為 $alpha$ 或 $beta$ ?
  + 「寧可錯放」為增加 $alpha$ 或 $beta$？而減少 $alpha$ 或 $beta$ ?
][
  #text(fill: red.darken(25%))[
    + 不該放假而放假，屬於是 $H_0$ 為真但拒絕，故為 type-I 誤差，其機率為 $alpha$。
    + 該放假而未放假，屬於是 $H_0$ 為假但接受，故為 type-II 誤差，其機率為 $beta$。
    + 寧可錯放，指增加「不該放假而放假」的機率，故為增加 $alpha$ 而減少 $beta$。
  ]
]

#question("Question 6")[
  某捷運系統進口了三套監測系統A、B、C，若軌道出現異常物時，監測系統隨即強迫捷運緊急停駛。今測試結果如下：A 系統較無規律，該停不停，不該停卻停；B 系統經常有錯誤訊息，使得不該停亂停；C 系統則反應遲鈍，該停不停。

  + 試著以統計假設檢定說明監測實況與決策行動。
  + 何者為型-I 錯誤與型-II 錯誤?
  + 這三套系統分別犯了何種錯誤?
][
  *Question 1*

  #table(
    columns: (1fr, 1fr, 1fr),
    table.header(
      table.cell(rowspan: 2)[決策行動],
      table.cell(colspan: 2)[監測實況],
      [無異常物], [有異常物]
    ),
    [未停駛], [正確], [Type-II error],
    [停駛], [Type-I error], [正確]
  )

  *Question 2*

  - Type-I error: 沒有異常物但停駛。
  - Type-II error: 有異常物但未停駛。

  *Question 3*

  - A 系統：Type-I error 和 Type-II error 均犯。
  - B 系統：犯 Type-I error。
  - C 系統：犯 Type-II error。
]

#question("Question 22")[
  某項測驗成績長期以來呈常態分配，標準差約為15 分，測驗機構認為若標準差低於15 分時，將不具鑑別度。某次模擬命題共有31 位考生應考，測得成績的標準差為10 分，試問本次模擬命題是否具鑑別度?
][
  母體為常態分配，且 $sigma=15$，從中抽取31個樣本，$s=10$，而 $sigma<15$ 代表不具鑑別度。假設 $alpha=0.95$。

  *Step 1: 列出虛無和對立假說*

  $
  cases(
    H_0: sigma >= 15 "(不具鑑別度)",
    H_1: sigma < 15 "(具鑑別度)"
  )
  $

  *Step 2: 統計量分配、決策法則*

  由於母體 $mu$ 未知，故其分配是

  $
  ((n-1) times S^2_mu)/sigma^2 tilde chi^2(30)
  $

  以 $alpha=0.05$ 為顯著水準，則拒絕域為（使用標準統計量檢定法）

  $
  R = { chi^2 | chi^2 < chi^2_(0.05)(30) }
  $

  *Step 3: 判斷是否在拒絕域*

  $chi^2_(0.05)(30)$ 查表的值為 $43.7730$，而

  $
  ((n-1) times S^2_mu)/sigma^2 = 30 times (10^2)/(15^2) = 13.3333
  $

  由於 $13.3333 < 43.7730$，故 $((n-1) times S^2_mu)/sigma^2 in R R$，拒絕 $H_0$。

  *Step 4: 具體結論*

  在 $alpha=0.05$ 下，本次模擬命題不具鑑別度。
]
