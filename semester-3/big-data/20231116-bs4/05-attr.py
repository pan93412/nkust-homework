import bs4
import requests

with open("page.html") as f:
    soup = bs4.BeautifulSoup(f, "lxml")

    msg = soup.find(id="hidden-msg")
    print(msg.attrs)
