from http.client import HTTPResponse
from urllib.error import URLError, HTTPError
from urllib.request import urlopen

url = "https://www.kcg.gov.tw/"
filename = "myKS.html"

try:
    response: HTTPResponse = urlopen(url)
    with open(filename, "wb") as f:
        for chunk in response:
            f.write(chunk)
except HTTPError as e:
    print(f"請求 {url} 失敗: {e}")
except URLError as e:
    print(f"URL 格式錯誤：{e}")
