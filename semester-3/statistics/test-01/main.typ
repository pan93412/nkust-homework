#import "template.typ": *
#show: project.with(title: "小考 1", authors: ("Yi-Jyun Pan",))

= 選擇題

#let choose = counter("choose")

#question(choose, wrong: false)[
  下列關於資料之敘述，何者為真？
][
  + *資料依取得來源，可分為原始與次級資料兩大類*
  + 資料直接由來源處蒐集、經整理後之資料，稱之為原始資料
  + 政府定期或不定期所公佈、出版之資料，屬於原始資料
  + 原始與次級資料之優缺點相同，所以需要時採用任一類並無差異
]

#question(choose, wrong: false)[
  某硏究機構欲針對全國之觀光飯店，進行一項觀光問卷調査，試問下列何者錯誤？
][
  + 全國所有觀光飯店為此調查之母體
  + 若從全國所有觀光飯店中，抽出 30 家調查，此即為樣本 #comment["不是敘述"]
  + *若針對全國所有觀光飯店作調查，此即為普査，由分析結果可作為推論統計之基礎*
  + 問卷中調查之項目，如飯店類型、員工人數、房間數、營業收入等為分析之隨機變數
]

#question(choose, wrong: false)[
  有關於資料轉換，下列何者正確？
  #comment("名目 → 順序 → 區間 → 比率")
][
  + 順序尺度可轉換成名目尺度
  + 區間尺度可轉換成順序尺度
  + 區間尺度可轉換成名目尺度
  + *以上皆是*
]

#question(choose, wrong: false)[
  某燈具製造商宣稱其產品不良率少於1%• 某代理商為了確認，
  從其產品#underline[隨機取樣 200 件進行測試，結果發現有 4
  件是不良品]，則對於 4/200=0.02 的敘述何者正確？
][
  + 是參數
  + *是一個敘述統計量*
  + 是一個推論統計
  + 是真實不良品的機率
]

#question(choose, wrong: false)[
  學生每天消耗之卡路里數，屬於下列何類尺度？
  #comment[0 有意義。]
][
  + 名目尺度 (Nominal Scale)
  + 順序尺度 (Ordinal Scale)
  + 區間尺度 (Interval Scale)
  + *比率尺度 (Ratio Scale)*
]



