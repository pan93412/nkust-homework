#set text(font: "Songti TC", lang: "zh", region: "TW")

= Q1

令身高為 $h$，男生標準體重為 $w_m$，女生標準體重為 $w_f$，則：

$
cases(
    w_m &= &(h - 80) times 0.7,
    w_f &= &(h - 70) times 0.6
)
$

試寫一個程式可以計算男生女生的標準體重。

== 執行

```bash
python3 -m q1
```

== 執行結果

```
root@f488866d6ade:/app# python3 -m q1
175 1
66.5
root@f488866d6ade:/app# python3 -m q1
165 2
57.0
```

#image("result.png")
