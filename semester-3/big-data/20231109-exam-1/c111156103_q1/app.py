import requests

url = "https://www.kcg.gov.tw/"
filename = "kcg.html"

try:
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "w") as f:
        f.write(repr(response.headers))
except Exception as e:
    print(f"發生錯誤：{e}")
