import bs4
import requests

response = requests.get("https://ic.nkust.edu.tw/")
soup = bs4.BeautifulSoup(response.text, "lxml")

print("Title", type(soup.title), soup.title, sep="\t")

tag = soup.find("h1")

print("資料形態", type(tag), sep="\t")
print("Content", tag, sep="\t")
print("Text 屬性內容", "", tag.text, sep="\t")
print("String 屬性內容", "", tag.string, sep="\t")
