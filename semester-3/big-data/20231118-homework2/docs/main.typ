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

#outline(indent: auto)

#v(1em)

#show: columns.with(2, gutter: 14pt)

= Usage <usage>

首先你需要安裝 #link("https://github.com/mitsuhiko/rye")[`rye`] 套件管理器，並且安裝本專案所需的套件以及 Python 版本：

```shell-unix-generic
$ rye sync
```

若沒有 `rye`，則得自行根據 `pyproject.toml` 的定義安裝套件和 Python 3.12。

其執行檔位於 `src/hw2`，故命令使用 `rye run python3 src/hw2` 開頭。下述命令可以抓取高科大官網「焦點新聞-頭條」的新聞標題、內容、發布時間，並分別呈現於終端機和儲存至 `output.json`（可用引數修改）。

```shell-unix-generic
$ rye run python3 src/hw2 epage "https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw"
```

完整引數可以使用 `--help` 取得。輸出見 @cli-help-output。

= Tech stack

本專案使用 Python 3.12 開發，並使用 `httpx`（`requests` 的改良版本，支援非同步 `asyncio` 函式）下載網頁，使用 `selectolax`（`beautifulsoup` 的極高效能頂替）作為擷取網頁內容的工具，另使用 `loguru` 輸出美化過的日誌。程式碼風格部分，是使用 `black` 格式化程式碼。

= Architecture

本專案由五個步驟組成，共同組成 `Flow` (`crawler.py`)：

+ Executor：主要的邏輯執行機器，傳入一個命令 (`Command`) 使喚 `Extractor`，然後得到由 `Extractor` 傳回的結構化資料，並且 `Extractor` 內部可以呼叫 `Executor` 執行特定命令抓回特定資料。
+ Extractor：負責擷取網頁內容。主結構由 `Executor` 建立，而 `Extractor` 應負責將網頁內容轉換成 `selectolax` 的 `HTML` 物件，並提供以領域區分的函式，來將資料轉換為結構化的資料。
+ Wrapper：將 `Extractor` 回傳的結構化資料，進一步轉換成通用的 `Response`，以便傳入任意 `Serializer`。
+ `Serializer`：將任意 `Response` 轉換成指定格式，如 JSON、XML、CSV 等。

Executor、Extractor、Serializer 和 Wrapper 均由一個 Abstract Class 和一個 Implementation 組成——如 `EpageExtractor` 是 `Executor` 的實作。這樣方便日後加入其他類似的實作（如 YahooExtractor）同時不破壞現有的函式呼叫約定。您亦可在 `__init__.py` 註冊你的自訂實作，這樣便能在 CLI 使用。

`Flow` 另外也有 `display()` 特性，本質是封裝 `Command` 並插入如 Logging 的擴充函式。

另外本專案附帶一個以 `argparse` 為基礎的 CLI 工具，將 `Flow` 以命令列的方式呈現，如 #link(<usage>)[Usage] 所示。

= Performance

得益於 `httpx` 提供的 `async` client，以及 `selectolax` 以 C++ 語言為基礎的 CSS 選擇器，本專案的效能非常優異。

目前沒有 `requests` + `BeautifulSoup` 的對照組，但網頁規模偏小，HTML 解析器的改進預期不會有太過明顯的差異，不過使用 `asyncio` 函式較使用同步函式有相當大的差異。以下展示了使用 `async` client (commit `98239dbeb`) 前後的效能表現，使用 `hyperfine` 統計：

#figure(caption: "Performance comparsion betwen async and old sync crawl program based on httpx.")[
  #image("comparsion.png")
]

可發現其效率較原本快約 4.83 倍。原始回傳結果請參考 @raw-data-perf。

= Features

== Type-safe structure

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

== Beautiful CLI output

本專案在「新聞資料顯示在螢幕上」上使用 ANSI 跳脫字元，將終端機輸出的新聞概覽美化，如下圖所示：

#figure(caption: "Beautiful CLI output")[
  #image("cli-output.png")
]

實作如下。其中 `x1b[1m` 為轉粗體；`\x1b[33m` 為轉黃色；`\x1b[0m` 為重置樣式狀態。

#figure(caption: "Implementation of `visualize_news_list`")[
  ```py
  def visualize_news_list(news_list: NewsList) -> None:
      for news in news_list:
          print(f"\x1b[1m#{news.seq} | \x1b[33m{news.title}\x1b[0m")
          print(f"{news.date.date().isoformat()}")
          print("\n".join(map(lambda line: "\t" + line, news.content.split("\n"))))
          print("\n\n")
  ```
]

== `Response` wrapper

老師預期的 JSON format 如下：

#figure(caption: "Expected JSON format")[
  #image("json-format.png")
]

可簡單將這個格式抽象成兩個部分： "Metadata" 和 "Data"。其中 "Metadata" 包含如 `date` 的屬性；而 "Data" 則是任意結構化字典。

#figure(caption: "Abstracted JSON format")[
  ```json
  {
    "date": "YYYY.MM.DD",
    "<key>": "<value>",
  }
  ```
]

考慮到 Metadata 的固定性，因此可以將固定的部分做成一個 `Response` 類別，並將 `data` 作為參數傳入，並使用 `to_dict()` 製造 Response，實作可參考 `structures/response.py`。

另外 `seq` 是使用 per-session 的  `InccrementalCounter` 類別產生的。每當呼叫 `next()` 時，會回傳一個新的遞增數字。

= Conclusion & Opinion

上一次的作業用了直覺的方式來寫爬蟲，這次嘗試造了一個爬蟲「框架」，並且試驗了更前衛或更適合多網頁爬取的技術，如 `asyncio`、`selectolax`、`rye` 等等。

這次寫得這麼複雜，確實很浪費時間 XD 不過試著學習像是 `scrapy` 這種框架的實作，對於自身了解基礎技術的能力有很大的幫助。另外，這次的作業也讓我更加熟悉 `asyncio` 的使用，以及深化對於 CSS Selector 的知識。

除此之外，試驗上課較少涉及的技術（如 `httpx` 的 Asynchronous Client）也是很有趣的事情，雖然對於爬單張網頁沒有太大的差異，但就如本例爬新聞內文，Async 使得爬取可以並行完成，進而提高效率（4.83x 的速度提升！）

下次的作業也不確定會嘗試什麼樣的撰寫風格，但希望都能像這份作業一樣可以學到新東西。

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
