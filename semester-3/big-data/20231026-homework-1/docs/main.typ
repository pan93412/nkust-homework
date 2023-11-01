#set text(font: ("Fira Sans", "Noto Sans TC"), size: 14pt)
#show par: it => pad(y: 0.1em, it)

= Homework 1：通用網站擷取

#image("overview.png")

== 用法

需要先安裝 `requests` 依賴，然後執行：

```sh
python3 main.py
```

檔案會放置在 `output` 資料夾內。

== 特色

- 輸出原始檔、JSON、CSV 到獨立資料夾
- 原始檔自動判斷副檔名
- 檔名自動清理，增強可讀性
- 模擬瀏覽器 UA

=== 檔名自動清理

```python
invalid_characters = re.compile(r"[^a-zA-Z0-9_]")

filename = re.sub(r"_+", "_", invalid_characters.sub("_", url)).strip("_")
```

檔名是輸入的 URL，然後把不是字母、數字、底線的字元換成底線，並且連續的底線會被合併成一個底線。

=== 原始檔自動判斷副檔名

首先取得回傳 header 的 `Content-Type` 欄位，得到的內容通常是 `MIME 類型; 編碼方式`。

```
Content-Type: text/html; charset=utf-8
```

接著程式碼會擷取裡面的 MIME 類型，並使用 Python 內建的 `mimetypes` 模組取得這個 MIME 常見的副檔名：

```python
mime = resp.headers["Content-Type"].split(";")[0]
extension = mimetypes.guess_extension(mime)
```

最後將清理好的檔名和自動判斷的副檔名加在一起，就是下載檔案的正確格式了。不過本例都是 `text/html` 故均是 `.html`。

== 欄位

=== JSON

```json
{
    "method": "GET",
    "headers": {
        "標頭名稱": "標頭內容"
    },
    "status_code": 200,
    "encoding": "編碼方式",
    "request_url": "請求 URL",
    "response_from": "原始檔案資料來源 URL",
    "content": "原始檔案資料內容"
}
```

== CSV

```csv
URL,MIME Type,Filename,Raw Response Filename,Content
網址,資料類型,檔名,下載檔名,內容
```
