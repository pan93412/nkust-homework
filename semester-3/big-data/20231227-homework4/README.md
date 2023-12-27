# 作業4

## 使用說明

需要安裝這幾個套件：

```bash
pip install httpx loguru selectolax aiofiles
python3 src/hw4
```

或者是直接使用 `rye` 安裝並執行：

```bash
rye sync
rye run python3 src/hw4
```

## 套件說明

- httpx: 用來並行取得網頁、下載檔案
- loguru: 用來取代內建的 logging，讓 log 更好看
- selectolax: 用來解析 HTML，比 BeautifulSoup 快、API 也比較好用
- aiofiles: 用來並行寫入檔案，防止寫入檔案時造成的 event loop 阻塞

## 程式說明

- 所有下載都是並行的，不會等待上一個下載完成才開始下載下一個，因此從程式開始執行到全部下載回來，不會超過 4 秒鐘。
  - 使用 `asyncio.TaskGroup` 讓所有的下載任務並行完成，讓執行效率最大化。
- 使用 Regex 擷取 `javascript:window.open()` 裡面的連結，這樣子即使下載點更換也可以不受影響。
- 透過判斷檔名是否存在決定是否下載，防止重複下載。如果檔案都已經下載完全，執行時間可以控制在 1 秒鐘內完成。
- 程式碼的每個部分也拆得很清晰，一個檔案就把所有邏輯完成，方便後人維護。

## 執行結果

以下結果均不含 DEBUG 訊息。

### 冷執行（從頭下載）

```bash
$ LOGURU_LEVEL="INFO" python3 src/hw4
2023-12-27 23:07:13.867 | INFO     | __main__:main:31 - 正在取回清單頁面……
2023-12-27 23:07:14.891 | INFO     | __main__:main:36 - 正在解析表格……
2023-12-27 23:07:14.898 | INFO     | __main__:main:62 - 正在檢查下載清單……
2023-12-27 23:07:15.998 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_21.zip
2023-12-27 23:07:16.044 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_22.zip
2023-12-27 23:07:16.405 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_26.zip
2023-12-27 23:07:16.411 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_25.zip
2023-12-27 23:07:16.493 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_15.zip
2023-12-27 23:07:16.541 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_16.zip
2023-12-27 23:07:16.599 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_24.zip
2023-12-27 23:07:16.643 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_17.zip
2023-12-27 23:07:16.728 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_04.zip
2023-12-27 23:07:16.728 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_27.zip
2023-12-27 23:07:16.895 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_21.zip
2023-12-27 23:07:16.985 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_29.zip
2023-12-27 23:07:17.215 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_14.zip
2023-12-27 23:07:17.333 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_11.zip
2023-12-27 23:07:17.347 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_23.zip
2023-12-27 23:07:17.432 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_30.zip
2023-12-27 23:07:17.469 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_13.zip
2023-12-27 23:07:17.480 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_01.zip
2023-12-27 23:07:17.603 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_06.zip
2023-12-27 23:07:17.604 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_22.zip
2023-12-27 23:07:17.638 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_12.zip
2023-12-27 23:07:17.638 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_28.zip
2023-12-27 23:07:17.700 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_19.zip
2023-12-27 23:07:17.711 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_20.zip
2023-12-27 23:07:17.856 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_08.zip
2023-12-27 23:07:17.878 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_07.zip
2023-12-27 23:07:17.878 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_11_27.zip
2023-12-27 23:07:17.941 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_20.zip
2023-12-27 23:07:17.967 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_18.zip
2023-12-27 23:07:18.102 | INFO     | __main__:download_and_save:24 - 正在寫入：downloads/OptionsDaily_2023_12_05.zip
2023-12-27 23:07:18.103 | INFO     | __main__:main:79 - 下載完成。
```

### 熱執行（檔案已經下載完全）

```bash
$ LOGURU_LEVEL="INFO" python3 src/hw4
2023-12-27 23:07:51.584 | INFO     | __main__:main:31 - 正在取回清單頁面……
2023-12-27 23:07:52.220 | INFO     | __main__:main:36 - 正在解析表格……
2023-12-27 23:07:52.224 | INFO     | __main__:main:62 - 正在檢查下載清單……
2023-12-27 23:07:52.225 | INFO     | __main__:main:79 - 下載完成。
```

## 心得

- 非同步真的把整個程式加速非常多！不過之後要限制下載次數，以免被他們系統當成是 DoS 攻擊 🌚
- 把程式寫簡單不只讓別人好讀，也節省自己的時間和未來的擴充性，感覺比作業 2 用各種物件導向的方式寫來得簡潔很多。
- 原本教授是教「儲存成 lastUpdate.txt」的做法，但我後來發現：「假如檔案有不小心被刪除，或者是下載失敗，那 lastUpdate.txt 的設計沒有辦法查出這些錯誤」，因此我改成「檢查檔案是否存在」的方式，這樣子就可以避免這個問題。
- 另外教授原本是用寫死的連結，我改用老師在第十章教的「正規表示式」，這樣子就算下載點更換，也不會受到影響，同時也讓程式讀起來更為簡單。
- 可惜這次的作業還沒有機會對資料進行分析和清洗，最近在學習資料視覺化 (streamlit)，希望之後的作業有機會把資料呈現出來。
