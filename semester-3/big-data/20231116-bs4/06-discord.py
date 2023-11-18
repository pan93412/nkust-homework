import bs4
import requests

response = requests.get("https://dcard.tw")
soup = bs4.BeautifulSoup(response.text, "lxml")

print("Title", soup.title, sep="\t")
print(soup)