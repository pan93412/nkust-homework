#import "template.typ": *

#show: project.with(title: [CH10 期末考 calculate paper], authors: ("Yi-Jyun Pan",))

#question("Ch9T3Q1", 0)[
  某學生欲調查班上同學之手機電池健康度平均是否低於
90%，於是隨機抽取10位學生其手機電池健康度 (%)為：91,90,77,84,81,95,80,97,89,74。 假設母體為常態分配，試在顯著水準 $alpha=0.05$ 下，試以 臨界值檢定法 檢定該班上學生之手機電池健康度平均是否低於 90%。
][
  因為 $n=10$ 是小樣本，母體為常態分配但 $sigma$ 未知，因此使用 $t$ 分配

  $
  (overline(x) - mu)/(sigma/sqrt(n)) tilde t(n-1)
  $

  *Step 1*: 列出虛無假說

  $
  cases(
    H_0: mu >= 90 \
    H_1: mu < 90 "(假說)"
  )
  $

  *Step 2*: 使用「臨界值檢定法」進行檢定。因為 $H_1$ 是小於，故為左尾檢定。
  Point: 檢定用 $mu$，判斷用 $overline(x)$

  $
  c &= mu minus t_(0.05)(9) times sigma/sqrt(n), sigma=s \
    &= 90 minus 1.833 times 7.76/sqrt(10) \
    &= 90 - 4.4981 = 85.5019
  $

  故拒絕域為

  $
  R R = { overline(x) | overline(x) < 85.5019 }
  $

  *Step 3*: $n=10, overline(x)=85.8$ 帶入 $R R$，發現
  $overline(x) = 85.8 > 85.5019$, $overline(x) in.not R R$，
  故不拒絕 $H_0$。

  *Step 4*: 在 $alpha=0.05$ 下，班上學生的手機電池健康度平均沒有低於90%。
]

#question("Ch9T3Q2", 0)[
  一般人多認為肥胖和心臟病有相當大的關係，其研究機構為驗證此種說法是否可靠，隨機抽樣
1200位肥胖患者進行調查，發現其中 650位肥胖患者 有心臟病 。已知台灣人 心臟病 比例 50%，試在顯著水準 $alpha=0.01$ 下， 試以 標準統計量檢定法 檢定肥胖與心臟病到底有無關聯？
][
  令 $p$ 為肥胖患者的心臟病比例。

  因為 $n p>10, n(1-p)>10$，故屬於大樣本

  $
  hat(p) approx N(p, p(1-p)/n)
  $

  *Step 1*: 列出虛無假說

  $
  cases(
    H_0: p <= 0.5 " (無關)" \
    H_1: p > 0.5 " (有關)"
  )
  $

  *Step 2*: 列出拒絕域

  $
  R R &= { overline(x) | overline(x) > Z_(alpha=0.01) } \
      &= { overline(x) | overline(x) > 2.33 }
  $

  *Step 3*: 帶入數字

  $
  Z &= (hat(p) - p)/sqrt(p(1-p)/n) \
    &= (650/1200 - 0.5)/sqrt((0.5 times 0.5)/1200) \
    &= 0.0417/0.0141 \
    &= 2.9574
  $

  因為 $Z = 2.9574>2.33$，$Z in R R$，拒絕 $H_0$

  *Step 4*: 在 $alpha=0.05$ 的情況下，肥胖與心臟病有關聯。
]

#question("Ch9T3Q3", 0)[
  全國成年人血液膽固醇平均濃度為 190mg/dL。因飲食習慣差異，公衛學者 猜想 某地區成年人膽固醇平均濃度與全國的情形 不一致 ，並非 190mg/dL。 假設成年人血液膽固醇濃度為常態分配公衛學者於該地區隨機抽樣 25位成年民眾並測量其血液膽固醇濃度，樣本平均數為 220mg/dL，母體標準差已知為 $sigma$=45mg/dL，當公衛學者願意承擔 0.05的機率 (風險 )犯型一錯誤下， 以 臨界值檢定法 檢定是否正確 ?
][
  考慮到母體為常態分配，且$sigma$已知，故分配為

  $
  overline(X) tilde N(mu, sigma^2/n)
  $

  *Step 1*: 列出 $H_0$

  $
  cases(
    H_0: mu = 190 \
    H_1: mu eq.not 190 "(假說)"
  )
  $

  *Step 2*: 拒絕域

  $
  c &= mu plus.minus Z_0.05 times sigma/sqrt(n) \
    &= 190 plus.minus 1.96 times 45/25 \
    &= 190 plus.minus 3.52 \
    &= 186.4 or 193.52
  $

  $
  R R = { overline(x) | overline(x) > 193.52 or overline(x) < 186.4}
  $

  *Step 3*: 帶入判斷

  $overline(x)=220$ 帶入，發現 $overline(x) in R R$，故拒絕 $H_0$

  *Step 4*: 在 $alpha=0.05$ 下，接受某地區成年人膽固醇平均濃度與全國的情形不一致
]

