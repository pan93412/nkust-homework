#import "template.typ": *
#show: project.with(title: "小考 2", authors: ("Yi-Jyun Pan",))

= 選擇題

#let choose = counter("choose")

= 計算題

#let calculate = counter("calculate")

#question(calculate, wrong: false)[
  請問平均唸書時間、唸書時間的中位數、眾數各為多少？
][
  + 平均 $overline(x)$
    $
    overline(x) = (14.5+15+dots+25.5)/40 = 736/40 = 18.4
    $
  + 中位數 $M_e$
    $
    (18+18)/2 = 18
    $
    - $40 times 1/2 = 20$ 取 $20$ 位、$21$ 位平均。
  + 眾數 $M_o$ 等於 19（有五筆）
]

請問乎均唸書時間、唸書時間的中位數、眾數各為多少？
根據①的結果，計算出唸書時間的變異數及標準差。
請計算出四分位距為多少？
請指出最多與最少的唸書時數，並計算出全距。

#question(calculate, wrong: false)[
  根據①的結果，計算出唸書時間的變異數及標準差。
][
  + 變異數
    $
    s^2 &= (sum_(i=1)^n (x_i - overline(x))^2)/(n-1) \
        &= 237.6/40-1 \
        &= 6.0923
    $
  + 標準差
    $
    s = sqrt(s^2) = sqrt(6.0923) = 2.4683
    $
]

#question(calculate, wrong: false)[
  請計算出四分位距為多少？
][
  + $Q_3 = (19+19.5)/2 = 19.25$
    - $40 times 75% = 30$ $=>$ 因為 $30$ 是整數，所以得取本數和它下一位數字（30、31）位的平均。
  + $Q_1 = 40 times 25% = 10$ $=>$ 取 10、11 位的平均。
  + $"IQR" = 19.25 - 16.75 = 2.5$
]

#question(calculate, wrong: false)[
  請指出最多與最少的唸書時數，並計算出全距。
][
  + $"Max"=25.5$
  + $"Min"=14.5$
  + $R = 25.5-14.5=11$
]
