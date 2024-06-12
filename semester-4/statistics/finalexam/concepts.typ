#import "template.typ": *

#show: project.with(title: [期中考概念], authors: ("Yi-Jyun Pan",))

#outline(indent: auto)

= Ch9

目的：由樣本統計量推測母體統計量的假說是否正確。

== 步驟

+ 建立拒絕域 ($H_0, H_1$)
+ 判斷分配以及決策法則（拒絕域）
  + 正負與否取決於 $H_1$。$H_1$ 大於則為右尾；$H_1$ 小於則為左尾；$H_1$ 不等於則為雙尾。
+ 實際抽樣資料，帶入決策法則判斷是否接受或拒絕 $H_0$
+ 用白話文說出具體結論（在 $alpha=0.01$ 下，接受⋯⋯）

=== 拒絕域

- 拒絕域常見機率 $alpha=0.05, 0.01, 0.1$，分別為機率很小、機率更小、機率非常小。

== 方法

=== 臨界值法

令小於 $c$（臨界值）的值為拒絕域

$
R R = {overline(x) | overline(x)<c}
$

$c$ 的公式為

$
c &= mu_0 plus.minus Z_alpha times sigma/sqrt(n), sigma = s
$

