import bs4
import requests

response = requests.get("https://example.com")
soup = bs4.BeautifulSoup(response.text, "lxml")

tag = soup.find("h1")

print("資料形態", type(tag), sep="\t")
print("Content", tag, sep="\t")
print("Text 屬性內容", "", tag.text, sep="\t")
print("String 屬性內容", "", tag.string, sep="\t")
