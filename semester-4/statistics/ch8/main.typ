#import "template.typ": *

#show: project.with(title: [CH8: 估計], authors: ("Yi-Jyun Pan",))

#outline(indent: auto)

= 概論

現在已經知道可以從 $n$ 個樣本中知道其樣本統計量 ($overline(x)$, $hat(p)$, $s^2$, …) 的分配，而這次想要從樣本的統計量推估母體的參數（$mu$, $p$, $sigma^2$, …）。

但是，以往學習的「點估計」$overline(x)_s -> mu$ 可能是有 *抽樣誤差* 的，且目前還沒有描述。現在我們已經學會 $overline(x)$ 和 $mu$ 有著誤差，接下來希望可以知道$P(abs(overline(x)_s-mu))$ 的區間，另外日後假如加入更多樣本，如 $overline(x)_s^'$，有多少機率可以涵蓋到母體平均值 $mu$。

- *信心水準*：有多少機率可以涵蓋到母體參數
- 本章學習重點：*區間估計*

= 估計式

== 特性

目的：自 $hat(theta) -> theta$（$hat$ 表估計。）
- 要具有 *不偏性*：$E(hat(theta)) = theta$，如 $E(overline(x)) = mu$ 就具有不偏性。

