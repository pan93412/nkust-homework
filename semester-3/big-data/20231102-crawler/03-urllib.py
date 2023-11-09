import urllib.request

url = "http://www.baidu.com/"
response = urllib.request.urlopen(url)

print(response.read().decode("utf-8"))
