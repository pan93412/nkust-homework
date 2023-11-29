#set text(font: ("STIX Two Text", "AR MingB5Std"), lang: "zh", region: "TW")
#set par(leading: 0.75em)
#set heading(numbering: "1.")
#set page(header: [
  #locate(it => [
    #if it.page() != 1 [
    ]
    #if it.page() != 1 [
      #align(right, text(size: 12pt)[*Homework 2*])
    ]
  ])
], footer: [
  #locate(it => {
    set text(size: 12pt)
    let p = it.page()

    if calc.odd(p) [
      #align(right, str(p))
    ] else [
      #align(left, str(p))
    ]
  })
])
#show heading: it => [
  #it
  #v(0.2em)
]
#show link: underline

#align(center, pad(bottom: 0.5em, [
  #text(size: 24pt)[*Homework 2*]

  #v(-1.5em)

  C111156103, 潘奕濬
]))

#pad(x: 2.5em, [
  本程式嘗試利用物件導向理念，開發流程分明、易擴充、靜態類型的 Python 爬蟲，且以 Epage（高科大官網的基礎）作為本爬蟲的首個支援站台。
])

#outline()

#v(1em)

#show: columns.with(2, gutter: 14pt)

= Usage <usage>

首先你需要安裝 #link("https://github.com/mitsuhiko/rye")[`rye`] 套件管理器，並且安裝本專案所需的套件以及 Python 版本：

```shell-unix-generic
$ rye sync
```

若沒有 `rye`，則得自行根據 `pyproject.toml` 的定義安裝套件和 Python 3.12。

其執行檔位於 `src/hw2`，故命令使用 `rye run python3 src/hw2` 開頭。下述命令可以抓取高科大官網「焦點新聞-頭條」的新聞標題、內容、發布時間。

```shell-unix-generic
$ rye run python3 src/hw2 epage "https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw"
```

完整引數可以使用 `--help` 取得。輸出見 @cli-help-output。

= Tech stack

本專案使用 Python 3.12 開發，並使用 `httpx`（`requests` 的改良版本，支援非同步 `asyncio` 函式）下載網頁，使用 `selectolax`（`beautifulsoup` 的極高效能頂替）作為擷取網頁內容的工具，另使用 `loguru` 輸出美化過的日誌。

程式碼風格部分，是使用 `black` 格式化程式碼。

= Architecture

本專案由五個步驟組成，共同組成 `Flow` (`crawler.py`)：

+ Executor：主要的邏輯執行機器，傳入一個命令 (`Command`) 使喚 `Extractor`，然後得到由 `Extractor` 傳回的結構化資料，並且 `Extractor` 內部可以呼叫 `Executor` 執行特定命令抓回特定資料。
+ Extractor：負責擷取網頁內容。主結構由 `Executor` 建立，而 `Extractor` 應負責將網頁內容轉換成 `selectolax` 的 `HTML` 物件，並提供以領域區分的函式，來將資料轉換為結構化的資料。
+ Wrapper：將 `Extractor` 回傳的結構化資料，進一步轉換成通用的 `Response`，以便傳入任意 `Serializer`。
+ `Serializer`：將任意 `Response` 轉換成指定格式，如 JSON、XML、CSV 等。

`Flow` 另外也有 `display()` 特性，本質是封裝 `Command` 並插入如 Logging 的擴充函式。

另外本專案附帶一個以 `argparse` 為基礎的 CLI 工具，將 `Flow` 以命令列的方式呈現，如 #link(<usage>)[Usage] 所示。

= Performance

得利於 `httpx` 提供的 `async` client，以及 `selectolax` 以 C++ 語言為基礎的 CSS 選擇器，本專案的效能非常優異。

以下展示了使用 `async` client (commit `98239dbeb`) 前後的效能表現，使用 `hyperfine` 統計：

#figure(caption: "Performance comparsion betwen async and old sync crawl program based on httpx.")[
  #image("comparsion.png")
]

可發現其效率較原本快約 4.83 倍。原始回傳結果請參考 @raw-data-perf。

= Type-safe structure

這個專案大量使用 Python 的靜態類型標示，防止錯誤參數的傳入或錯誤的回傳值，並取得更好的 IDE 和靜態分析支援。

由於使用到進階靜態類型，因此需要比較新的 Python 版本（目前只在 3.12 測試）方能執行。就以`src/hw2/utils/fn_describer.py` 中的 `FnDescriber` 來說，使用新的 `ParamSpec` 泛型標記，可以的程式碼，可以做到 `__call__` 函式簽名與 `fn` 相同，同時還能加上自己的 `description`：

#figure(caption: "Usage of FnDescriber")[
  ```py
  @describe_fn("Add the length of b to a")
  def foo(a: int, b: str) -> int:
      return a + len(b)

  print(f"{foo!r}")
  # Output: Add the length of b to a.
  ```
]


#figure(caption: [Type-safe `FnDescriber`])[
  ```py
  P = ParamSpec("P")
  O = TypeVar("O")

  def describe_fn(description: str) -> Callable[[Callable[P, O]], "FnDescriber[P, O]"]:
    """The decorator of FnDescriber."""
    return lambda fn: FnDescriber(fn, description)

  class FnDescriber(Generic[P, O]):
      def __init__(self, fn: Callable[P, O], description: str):
          self.fn = fn
          self.desc = description

      def __call__(self, *args: P.args, **kwargs: P.kwargs) -> O:
          return self.fn(*args, **kwargs)
  ```
]

= Appendix

== `--help` output of the CLI tool <cli-help-output>

```txt
$ rye run python3 src/hw2 --help
usage: hw2 [-h] [--method {news}] [--format {json}] [--out-prefix OUT_PREFIX] {epage} url

positional arguments:
  {epage}               the generator type of this page
  url                   the page url to crawl

options:
  -h, --help            show this help message and exit
  --method {news}       the extract method of this page
  --format {json}       the output format of the result
  --out-prefix OUT_PREFIX
                        the prefix of output file
```

== Raw data of Performance comparsion <raw-data-perf>

```txt
Benchmark 1: python3 old-async/src/hw2/ epage https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw
  Time (mean ± σ):      6.349 s ±  0.221 s    [User: 0.255 s, System: 0.055 s]
  Range (min … max):    6.041 s …  6.665 s    10 runs

Benchmark 2: python3 src/hw2 epage https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw
  Time (mean ± σ):      1.315 s ±  0.081 s    [User: 0.208 s, System: 0.032 s]
  Range (min … max):    1.248 s …  1.515 s    10 runs

Summary
  python3 src/hw2 epage https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw ran
    4.83 ± 0.34 times faster than python3 old-async/src/hw2/ epage https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw
```
