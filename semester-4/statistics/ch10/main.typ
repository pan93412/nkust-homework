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

